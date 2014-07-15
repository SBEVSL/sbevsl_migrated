############################################################################
# Joshua R. Boverhof, LBNL
# Monte M. Goode, LBNL
# David W. Robertson, LBNL
# See LBNLCopyright for copyright notice!
###########################################################################
import sys, re, weakref
from xml.dom.ext import SplitQName
from xml.ns import SOAP, SCHEMA
import ZSI
from ZSI.typeinterpreter import BaseTypeInterpreter
from ZSI.wsdlInterface import ZSIWsdlAdapter, ZSISchemaAdapter

# $Id: wsdl2python.py,v 1.49 2004/02/19 01:14:16 tyger23 Exp $

"""
wsdl2python:
    This module generates an client interface module and a module containing
    all of the types (typecodes) for use with the zsi library.  

Arch:
    WriteServiceModule
      -Takes a wsdl object and creates the client interface and typecodes for 
       the service.
      -Handles writing of import complexities and class definition order.
      -Delegates to ServiceDescription interpretation of service definition.
      -Delegates to SchemaDescription interpretation of schema definition.

    ServiceDescription
      -Interprets the service definition, creates client interface and
       port descriptions code.
      -Delegates to MessageWriter

       MessageWriter
         -Generates a message's class definition.

          PartWriter
            -Generates a message part's description.


    SchemaDescription
      -Interprets the schema definition, creates typecode module code.

       TypeWriter
         -Generates a type's description/typecode.
"""


ID1 = '    '
ID2 = 2*ID1
ID3 = 3*ID1
ID4 = 4*ID1
ID5 = 5*ID1
ID6 = 6*ID1

IDSP2 = '  '

DEBUG  = 0
NSDICT = {}

def print_debug(msg, level=1, *l, **kw):
    if DEBUG >= level:
        for i in l:
            msg += '\n*\t' + str(i)
        for k,v in kw.items():
            msg += '\n**\t%s: %s' %(k,v)
        print "WSDL2PYTHON(%d): %s" %(level,msg)

def nonColonizedName_to_moduleName(name):
    """Take a non-colonized name, create a legal module name.
       Replace . -- _
    """
    return re.sub('\.', '_', name)

def textProtect(s):
    """process any strings we cant have illegal chracters in"""
    return re.sub('[-./:?]', '_', s)

class WsdlGeneratorError(Exception):
    pass

class NamespaceHash:
    """Keep track of the various namespaces used in a service and assign
    aliases to said namespaces for brevity.  A lookup table
    """
    NSCOUNT = 1
    NSDICT = {}
    NSORDER = []

    def __init__(self):
        pass

    def add(self, ns):

        if not NamespaceHash.NSDICT.has_key(ns):
            NamespaceHash.NSDICT[ns] = ( self.namespace_to_moduleName(ns),
                                         'ns%s' % NamespaceHash.NSCOUNT )
            NamespaceHash.NSORDER.append(ns)
            NamespaceHash.NSCOUNT += 1


    def getModuleName(self, ns):

        if NamespaceHash.NSDICT.has_key(ns):
            return NamespaceHash.NSDICT[ns][0]
        else:
            raise WsdlGeneratorError, 'could not retrieve mod name for %s' % ns

    def getAlias(self, ns):

        if NamespaceHash.NSDICT.has_key(ns):
            return NamespaceHash.NSDICT[ns][1]
        else:
            self.dump()
            raise WsdlGeneratorError, 'could not retrieve alias for %s' % ns

    def getNSList(self):
        return NamespaceHash.NSORDER


    def namespace_to_moduleName(self, n):
        name = n
        
        if name.startswith('http://'):
            name = name[7:]

        name = textProtect(name)

        if name.endswith('_'):
            name = name[:-1]
        
        return name

    def dump(self):
        print NamespaceHash.NSDICT

    def reset(self):
        NamespaceHash.NSCOUNT = 1
        NamespaceHash.NSDICT = {}
        NamespaceHash.NSORDER = []


class StringWriter:
    def __init__(self, val=None):
        self.data = []
        if val:
            self.data.append(val)
            
    def set(self, val):
        if self.data:
            # in some cases the empty list reassignment fails, so....
            self.data = None
            self.data = []
            
        self.data.append(val)
        
    def write(self, val):
        self.data.append(val)
        
    def __iadd__(self, val):
        self.data.append(val)
        return self

    def getvalue(self):
        if self.data:
            return ''.join(self.data)
        else:
            return ''

        
class WriteServiceModule:
    """Takes a wsdl object and creates the client interface and typecodes for 
       the service.
    """
    def __init__(self, wsdl, importlib=None, typewriter=None):
        """wsdl - wsdl.Wsdl instance
        """
        self.wsdl  = wsdl
        self._wa = ZSIWsdlAdapter( self.wsdl )
        self.nsh = NamespaceHash()
        self.tns_wrote = {}
        self.tns_imported = {}
        self._nscount = 1
        self._nsdict  = {}
        self._importlib  = importlib
        self._typewriter = typewriter
        self.typeDict = {}

    def write(self, schemaOnly=False):
        """Write schema instance contents w/respect to dependency requirements, 
           and create client interface.  Not guaranteed to work for mutual 
           depenedencies.
        """

        f_types, f_services = self.get_module_names()
        hasSchema = len(self._wa.getSchemaDict())
        if hasSchema:
            fd = open(f_types + ".py", 'w+')
            self.write_service_types(f_types, fd)
            fd.close()

        if schemaOnly:
            return

        fd = open(f_services + ".py", 'w+')
        self.write_services(f_types, f_services, fd, hasSchema)
        fd.close()

        
    def get_module_names(self):
        if self._wa.getName():
            name = nonColonizedName_to_moduleName( self._wa.getName() )
        else:
            raise WsdlGeneratorError, 'could not determine a service name'

        name = SplitQName(name)[1]
        f_types = '%s_services_types' % name
        f_services = '%s_services' % name
        return f_types, f_services


    def write_service_types(self, f_types, fd):
        header = '%s \n# %s.py \n# generated by %s \n# \n# \n%s\n\n'\
	          %('#'*50, f_types, self.__module__, '#'*50)

        imports = ['\nimport ZSI']
        imports.append('\nfrom ZSI.TCcompound import Struct')

        if self._importlib:
            exec( 'import %s' % self._importlib )
            exec( 'obj = %s' % self._importlib )
            if hasattr( obj, 'typeimports' ):
                imports += obj.typeimports

	fd.write(header)
	fd.writelines(imports)
	fd.write('\n'*2)

        for schema in self._wa.getSchemaDict().values():
            self.write_dependent_schema(schema, fd)
            

    def write_services(self, f_types, f_services, fd, hasSchema):
        header = '%s \n# %s.py \n# generated by %s \n# \n# \n%s\n\n'\
	          %('#'*50, f_services, self.__module__, '#'*50)

	fd.write(header)
        
        for service in self._wa.getServicesList():
            sd = ServiceDescription()
            if hasSchema:
                sd.imports += ['\nfrom %s import *' % f_types]
                for ns in self.nsh.getNSList():
                    sd.imports += ['\nfrom %s import \\\n    %s as %s' \
                                  % ( f_types,
                                      self.nsh.getModuleName(ns),
                                      self.nsh.getAlias(ns)) ]

            sd.fromWsdl(service, self.typeDict)
            
            if self._importlib:
                exec( 'import %s' % self._importlib )
                exec( 'obj = %s' % self._importlib )
                if hasattr(obj, 'clientimports' ):
                    sd.imports += obj.clientimports
                    

            sd.write(fd)

        fd.write('\n')


    def write_dependent_schema(self, schema, fd):
        """Write schema instance contents w/respect to dependency requirements.
           First write any schema that is imported directly into current schema,
           then check current schema's xmlns and see if any of these represent
           currently held schema instances.

           schema -- schema.Schema instance
           fd -- file descriptor
        """

        # check imports
        for ns in schema.getImports():
            if self.tns_imported.has_key(ns):
                raise WsdlGeneratorError,\
                      'suspect circular import of %s - not suported' % ns
            if ns not in SCHEMA.XSD_LIST and \
               ns not in [SOAP.ENC]:
                self.tns_imported[ns] = 1
            if self._wa.getSchemaDict().has_key(ns) and \
                   (not self.tns_wrote.has_key(ns)):
                self.write_dependent_schema(self._wa.\
                                            getSchemaDict().get(ns), fd)
            if schema.getImportSchema(ns) and \
               (not self.tns_wrote.has_key(ns)):
                self.write_dependent_schema(schema.getImportSchema(ns), fd)

        # next...xmlns
        for ns in schema.getXmlnsDict().values():
            if self._wa.getSchemaDict().has_key(ns) and \
                   (not self.tns_wrote.has_key(ns)) and \
                   (ns != schema.getTargetNamespace()) and \
                   (not schema.getTargetNamespace() in \
                    self._wa.getSchemaDict().get(ns).getXmlnsDict().values()):
                self.write_dependent_schema(self._wa.getSchemaDict().get(ns),
                                            fd)
        
        # fall through
        else:
            if not self.tns_wrote.has_key(schema.getTargetNamespace()):
                self.nsh.add(schema.getTargetNamespace())
                self.tns_wrote[schema.getTargetNamespace()] = 1
                if self._importlib and self._typewriter:
                    alternateWriter = ( self._importlib, self._typewriter )
                else:
                    alternateWriter = None
                sd = SchemaDescription()
                sd.fromWsdl(schema, alternateWriter)
                sd.write(fd)
                    # typeDict used when generating 'services' file
                    # to generate docstrings for each operation
                self.typeDict.update(sd.typeDict)

    def __del__(self):
        self.nsh.reset()
 
class ServiceDescription:
    """Generates client interface.  Writes out an abstract interface, 
       a locator class, and port classes.
    """
    def __init__(self):
	self.imports = []
        return

    def write(self, fd=sys.stdout):
        """Write service instance contents.  Must call fromWsdl with
           service instance before calling write.
        """
	fd.writelines(self.imports)
	fd.write(self.serviceInterface)
	fd.write(self.serviceLocator)
        fd.write(self.serviceBindings)
        keys = self.messages.keys()
        keys.sort()
        [fd.write(str(self.messages[k])) for k in keys]
            
    def fromWsdl(self, service, typeDict=None):
        """service -- wsdl.Service instance
        """
	self.imports += '\nimport urlparse, types'
	self.imports += '\nfrom ZSI.TCcompound import Struct'
	self.imports += '\nfrom ZSI import client'
	self.imports += '\nimport ZSI'
        self.messages = {}
	self.serviceInterface = '\n\nclass %sInterface:\n' % \
                                (service.getName())
	self.serviceLocator = '\n\nclass %sLocator(%sInterface):\n' % \
                              (service.getName(), service.getName())
        self.serviceBindings = ''

        for p in service.getPortList():

            # -----------------------------
            # REQUIRED: WSDLv1.2 Bindings
            #  skip port if not present
	    #  port.soap
	    #    soap:address  location
            # -----------------------------
        
            hasSoapAddress = False
            soapAddress    = None

            for e in p.getExtensions():
                if isinstance(e,
                              ZSI.wsdlInterface.ZSISoapAddressAdapter):
                    hasSoapAddress = True
                    soapAddress = e

            if not hasSoapAddress:
                continue

            # -----------------------------
	    #  class variable address

	    self.serviceLocator += ID1 
            self.serviceLocator += '%s_address = "%s"\n' % \
                                   ( p.getBinding().getPortType().getName(),
                                     soapAddress.getLocation() )

            # -----------------------------
	    #  getPortTypeAddress

	    self.serviceLocator += ID1 
	    self.serviceLocator +=  'def get%sAddress(self):\n' % \
                                   ( p.getBinding().getPortType().getName() )
	    self.serviceLocator += ID2 
	    self.serviceLocator +=  'return %sLocator.%s_address\n\n' % \
                                   ( service.getName(),
                                     p.getBinding().getPortType().getName() )


            # -----------------------------
            #  getPortType(portAddress)

	    self.serviceInterface += \
                                  ID1 + \
                                  'def get%s(self, portAddress=None, **kw):\n'\
                                  % ( p.getBinding().getPortType().getName() )
	    self.serviceInterface += ID2 
	    self.serviceInterface += 'raise NonImplementationError, "method not implemented"\n'

	    self.serviceLocator += \
                                ID1 + \
                                'def get%s(self, portAddress=None, **kw):\n' \
                                % ( p.getBinding().getPortType().getName() )
	    self.serviceLocator += ID2 
	    self.serviceLocator += 'return %sSOAP(portAddress or %sLocator.%s_address, **kw)\n' \
                                   % ( p.getBinding().getName(),
                                       service.getName(),
                                       p.getBinding().getPortType().getName() )

	    myBinding = {'class':'\n\nclass %sSOAP:' % \
                         (p.getBinding().getName()), 'defs':{} }



            # -----------------------------
            # Methods
            # -----------------------------
            myBinding['defs']['__init__'] =  '\n%sdef __init__(self, addr, **kw):' %(ID1)
            myBinding['defs']['__init__'] += '\n%snetloc = (urlparse.urlparse(addr)[1]).split(":") + [80,]' %(ID2)
            myBinding['defs']['__init__'] += '\n%sif not kw.has_key("host"):' \
                                             % ( ID2 )
            myBinding['defs']['__init__'] += '\n%skw["host"] = netloc[0]' % ID3
            myBinding['defs']['__init__'] += '\n%sif not kw.has_key("port"):' \
                                             % ( ID2 )
            myBinding['defs']['__init__'] += '\n%skw["port"] = int(netloc[1])'\
                                             % ( ID3 )
            myBinding['defs']['__init__'] += '\n%sif not kw.has_key("url"):'\
                                             % ID2
            myBinding['defs']['__init__'] += '\n%skw["url"] =  urlparse.urlparse(addr)[2]' %(ID3)
            myBinding['defs']['__init__'] += '\n%sself.binding = client.Binding(**kw)' %(ID2)

            for op in p.getBinding().getPortType().getOperationList():
                # -----------------------------
                #  REQUIREMENTS SOAP Bindings
	        #  port.binding.operations.soap[binding,operations]
	        #  port.binding.soap[binding]
                #        style, transport
                # -----------------------------
                operation = p.getBinding().getOperationDict().get(op.getName())

                style      = None
                transport  = None
                
                if operation.getSoapBinding():
                    style      = operation.getSoapBinding().getStyle()
                    transport  = operation.getSoapBinding().getTransport()
                    soapAction = operation.getSoapBinding().getAction()
                else:
                    style      = p.getBinding().getSoapBinding().getStyle()
                    transport  = p.getBinding().getSoapBinding().getTransport()

                
                soapAction = None
                
                if operation.getSoapOperation():
                    soapAction = operation.getSoapOperation().getAction()

                use           = None
                namespace     = None
                encodingStyle = None

                if operation.getInput().getSoapBody():
                    use           = operation.getInput().getSoapBody()\
                                    .getUse()
                    namespace     = operation.getInput().getSoapBody()\
                                    .getNamespace()
                    encodingStyle = operation.getInput().getSoapBody()\
                                    .getEncoding()

                # -----------------------------
		# Methods
                # -----------------------------

                if op.getInput():
                    inputName = op.getInput().getMessage().getName()
                    # these have been moved here to build up the typecodes
                    # needed to generate types in the docstrings
                    self.messages[inputName] = self.__class__.MessageWriter()
                
                    self.messages[inputName].\
                                  fromMessage(op.getInput().getMessage(), 
                                          op.getName(), namespace, style, use)
                
                    outputName = None
                    if op.getOutput() and op.getOutput().getMessage():
                        outputName = op.getOutput().getMessage().getName()
                        self.messages[outputName] = \
                                      self.__class__.MessageWriter()
                        self.messages[outputName].\
                                      fromMessage(op.getOutput().getMessage(), 
                                                  outputName,
                                                  namespace,
                                                  style,
                                                  use, op)

		    myBinding['defs'][op.getName()] = \
                                                    '\n%sdef %s(self, request):' % \
                                                    (ID1, op.getName())
                    myBinding['defs'][op.getName()] += '\n%s"""\n' % ID2
                    myBinding['defs'][op.getName()] += self.messages[inputName].\
                                         docString(typeDict, inputName, True)
                    myBinding['defs'][op.getName()] += '\n'
                    if outputName:
                        myBinding['defs'][op.getName()] += self.messages[outputName].\
                                         docString(typeDict, outputName, False)
                    myBinding['defs'][op.getName()] += '%s"""\n' % ID2
                    
                    # checking to handle the special case of an
                    # element declaration of a primitive type.
                    # you will find these in document/literal ops.
                    kwstring = None
                    simpleType = self.isSimpleElementDeclaration(op)
                    if simpleType:
                        kwstring = "\n%skw = {'requestclass': %sWrapper}" \
                                   % (ID2, inputName )
                        myBinding['defs'][op.getName()] +=\
                                                        '\n%sif not type(request) == %s:' %( ID2, simpleType)
                    else:
                        kwstring = '\n%skw = {}' % ID2

                        myBinding['defs'][op.getName()] +=\
                                                        '\n%sif not isinstance(request, %s) and\\\n%snot issubclass(%s, request.__class__):'\
                                                        %(ID2, inputName,
                                                          ID3, inputName)
		    myBinding['defs'][op.getName()] +=\
                                                    '\n%sraise TypeError, %s' % \
                                                    (ID3, r'"%s incorrect request type" %(request.__class__)')

                    myBinding['defs'][op.getName()] += kwstring


                    if outputName:

			myBinding['defs'][op.getName()] +=\
                            '\n%sresponse = self.binding.Send(None, None, request, soapaction="%s", **kw)' %(ID2, soapAction)
			myBinding['defs'][op.getName()] +=\
                            '\n%sresponse = self.binding.Receive(%sWrapper())' % \
                            (ID2, outputName)
			myBinding['defs'][op.getName()] +=\
                            '\n%sif not isinstance(response, %s) and\\\n%snot issubclass(%s, response.__class__):'\
                            %(ID2, outputName, ID3, outputName)
			myBinding['defs'][op.getName()] +=\
			    '\n%sraise TypeError, %s' %(ID3, r'"%s incorrect response type" %(response.__class__)')
		        myBinding['defs'][op.getName()] += '\n%sreturn response' %(ID2)
                        
		    else:
			myBinding['defs'][op.getName()] += '\n%sself.binding.Send(None, None, request )' %(ID2)
		        myBinding['defs'][op.getName()] += '\n%sreturn' %(ID2)

		elif op.output:
		    pass
		else:
		    raise WsdlGeneratorError,\
                          'Operation w/o input and/or output'

            else:
	        self.serviceBindings += myBinding['class']
		self.serviceBindings += "\n%s\n" \
                                        % (myBinding['defs']['__init__'])
		del myBinding['defs']['__init__']

                keys = myBinding['defs'].keys()
                keys.sort()
                for mn in keys:
                    d = myBinding['defs'][mn]
		    self.serviceBindings += "\n%s\n" %(d)
		else:
	            self.serviceBindings += "\n"

        return

    def isSimpleElementDeclaration(self, op):
        if len( op.getInput().getMessage().getPartList() ) == 1:
            prt = op.getInput().getMessage().getPartList()[0]

            if prt.getElement():
                return prt.getElement().isBasicElement()

        return False

    class MessageWriter:
        """Generates a class representing a message.
        """
	def __init__(self):
            self.nsh = NamespaceHash()
	    self.typecode = None
            self.typeList = []

	def __str__(self):
	    return self.typecode

	def fromMessage(self, message, name, namespace, style, use, op=None):
	    """message -- wsdl.Message instance
               name -- operation name
               namespace -- soap binding namespace
               style -- 'rpc' or 'encoded'
               use -- 'document' or 'literal'
            """
            if use == 'encoded':
                self.fromMessageEncoded(message, name, namespace, style, op)
            elif use == 'literal':
                self.fromMessageLiteral(message, name, namespace, style)
            else:
                raise WsdlGeneratorError, 'unsupported use=%s' %(use)


        def fromMessageEncoded(self, message, name, namespace, style, op):
	    l = []

            classname = ''

            if message.isOutput() and style == 'rpc':
                if not op:
                    # this is mostly a temp bulletproofing exception.
                    raise WsdlGeneratorError, 'operation object is none - bad'
                else:
                    name = op.getName() + 'Response'

	    self.typecode = '\n\nclass %s (ZSI.TCcompound.Struct): '\
                            %(message.getName())
            self.typecode += '\n%sdef __init__(self, name=None, ns=None):'\
                             %(ID1)

	    for p in message.getPartList():
                if p.getType():
                    tns = p.getType().getTargetNamespace()
                    tp = self.__class__.PartWriter()
                    tp.fromPart(p)
                    if tp.typecode[0][0:3] == 'ZSI':
                        l += tp.typecode
                        self.typecode += '\n%sself._%s = None'\
                                         % ( ID2, p.getName() )
                            # for later use in docstring generation
                        self.typeList.append(['_' + tp.docCode[0], tp.docCode[1], False])
                    else:
                        qualifiedtc = tp.typecode[0:]
                        idx = qualifiedtc[0].find('(')
                        qualifiedtc[0] = self.nsh.getAlias(tns) + \
                                         '.' + qualifiedtc[0][0:idx] + \
                                         '_Def' + qualifiedtc[0][idx:]
                        l += qualifiedtc
                        defclass = tp.typecode[0][0:]
                        defclass = defclass[0:defclass.find('(')] + '_Def()'
                        self.typecode += '\n%sself._%s = %s.%s'\
                                         % ( ID2, p.getName(),
                                             self.nsh.getAlias(tns),
                                             defclass )
                        self.typeList.append(['_' + tp.docCode[0],
                                                   '%s.%s_Def' % (self.nsh.getAlias(tns), tp.docCode[1]), False])
                elif p.getElement():
                    raise WsdlGeneratorError, 'Bad encoding'
                else:
                    raise WsdlGeneratorError, 'FIX'
	    else:
                self.typecode += '\n\n%soname = None' % ID2
                self.typecode += '\n%sif name:' % ID2
                self.typecode += '\n%soname = name' % ID3
                self.typecode += '\n%sif ns:' % ID3
                self.typecode += "\n%soname += ' xmlns=\"%%s\"' %% ns" % ID4
		tcs = ''
		for i in l: tcs += (i + ',')
                self.typecode += '\n%sZSI.TC.Struct.__init__(self, %s, [%s], pname=name, aname="_%%s" %% name, oname=oname )'\
                                 %( ID3, message.getName(), tcs )

            # do the wrapper do go with the message

            if style == 'document':
                name = None
            elif style == 'rpc':
                name = "'" + name + "'"
            else:
                raise WsdlGeneratorError, 'incorrect document type -> ?'

            self.typecode += '\n\n'
            self.typecode += 'class %sWrapper(%s):\n' \
                             % (message.getName(), message.getName())
            self.typecode += '%s"""wrapper for %s:encoded message"""\n\n' \
                             % ( ID1, style )

            self.typecode +=\
                          "%stypecode = %s(name=%s, ns='%s')"\
                          % ( ID1, message.getName(), name, namespace )
            self.typecode += '\n%sdef __init__( self, name=None, ns=None ):'\
                             % ( ID1 )
            self.typecode += "\n%s%s.__init__( self, name=%s, ns='%s' )"\
                             % (ID2, message.getName(), name, namespace)
            

        def fromMessageLiteral(self, message, name, namespace, style):

	    l = []

	    self.typecode = '\n\nclass %s: ' %(message.getName())
	    self.typecode += '\n%sdef __init__(self, name=None, ns=None):' \
                             % (ID1)

	    for p in message.getPartList():
		if p.getElement():
		    tp = self.__class__.PartWriter()
		    tp.fromPart(p)
		    if tp.name:
                        nsp = self.nsh.getAlias(p.getElement().\
                                                getTargetNamespace())
                        self.typecode = '\n\nclass %s(%s.%s): ' %\
                                         (message.getName(),nsp,
                                          tp.name + '_Dec')
                        self.typecode += '\n%sif not hasattr( %s.%s(), "typecode" ):' % (ID1, nsp, tp.name + '_Dec')
                        self.typecode += '\n%stypecode = %s.%s()' \
                                         % (ID2, nsp, tp.name + \
                                            '_Dec' )

			self.typecode += '\n\n%sdef __init__(self, name=None, ns=None):'\
                                         %(ID1)
                        self.typecode += '\n%s%s.%s.__init__(self, name=None, ns=None)'\
                                         % (ID2, nsp, tp.name + '_Dec')
                            # for later use in docstring generation
                        self.typeList.append(['literal', '%s.%sLOCAL_Def' % (nsp, tp.name), False])
		    else:
			self.typecode = '\n\nclass %s: ' % (message.getName())
			self.typecode += '\n%sdef __init__(self, name=None, ns=None): pass' %(ID1)
		    break
		else:
		    if p.getType():
			tp = self.__class__.PartWriter()
			tp.fromPart(p)
                        if tp.typecode[0][0:3] != 'ZSI':
                            qualifiedtc = tp.typecode[0:]
                            idx = qualifiedtc[0].find('(')
                            qualifiedtc[0] = self.nsh.getAlias(tp.tns) + \
                                             '.' + qualifiedtc[0][0:idx] + \
                                             '_Def' + qualifiedtc[0][idx:]
                            l += qualifiedtc
                        else:
                            l += tp.typecode
		    else:
			raise WsdlGeneratorError, \
                              'Missing attribute for <message name=\"%s\"><part name=\"%s\">' % (message.getName(),p.getName())

	    else:
                # XXX: not very good wsdl - put warning message here
		tcs = ''
		for i in l: tcs += (i + ',')
                if namespace == None:
                    namespace = ''
                if style == 'rpc':
                    namespace = ''
		self.typecode += '\n%s%s.typecode = Struct(%s,[%s], pname=name, aname="_%%s" %% name, oname="%%s  xmlns=\\"%s\\"" %% name )'\
			     %(ID2,message.getName(),message.getName(),
                               tcs,namespace)

            # do the wrapper to go w/the message

            if style == 'document':
                name = None
            elif style == 'rpc':
                name = "'" + name + "'"
            else:
                raise WsdlGeneratorError, 'incorrect document type -> ?'

            self.typecode += '\n\n'
            self.typecode += 'class %sWrapper(%s):\n' \
                             % (message.getName(), message.getName())
            self.typecode += '%s"""wrapper for %s:literal message"""\n\n' \
                             % (ID1, style )

            self.typecode += '%stypecode = %s( name=%s, ns=None ).typecode'\
                             % (ID1, message.getName(), name )
            self.typecode += '\n%sdef __init__( self, name=None, ns=None ):'\
                             % ID1
            self.typecode += '\n%s%s.__init__( self, name=%s, ns=None )' \
                             % (ID2, message.getName(), name )


        def docString(self, allTypeDict, messageName, isInput):
            """Generates a docstring giving the input and output
               message names, and their associated parameters and
               parameter sub-fields.
            """
            docList = []
            if self.typeList:
                self.typeList.sort()

            for item in self.typeList:
                if item[1]:
                    item[1] = item[1].replace('LOCAL_Def', '_Def')
                else:
                    item[1] = 'Any'
            alreadyListed = []
            paramList = self.recurseTypeList(allTypeDict, self.typeList,
                                                       1, alreadyListed)
            if paramList:
                if paramList[0].startswith('*Simple*'):
                    startIndex = len('*Simple*') + 1
                    if isInput:
                        docList.append('%s@param: request is %s\n' % (ID2, paramList[0][startIndex:]))
                    else:
                        docList.append('%s@return: response is %s\n' % (ID2, paramList[0][startIndex:]))
                    return ''.join(docList)

            if isInput:
                docList.append('%s@param: request to %s' % (ID2, messageName))
            else:
                docList.append('%s@return: response from %s' % (ID2, messageName))
            if self.typeList:
                docList.append('::\n')
            docList.extend(paramList)
            return ''.join(docList)


        def recurseTypeList(self, allTypeDict, typeList, level, alreadyListed):
            """Recurse through a dictionary of type lists until reach
               Python types.
            """
            if level > 12:  # just in case
                return
            strList = []
            for item in typeList:
                if item[0].startswith('_'):
                    if not item[0].startswith('__param'):
                        indent = ID2 + IDSP2*level
                        strList.append('%s%s: %s' % (indent, item[0], item[1]))
                        if item[2]:
                            strList.append(', optional')
                        strList.append('\n')
                    else:
                        return ['*Simple* %s' % item[1]]
                if allTypeDict.has_key(item[1]):
                    if item[1] not in alreadyListed:
                        alreadyListed.append(item[1])
                        strList.extend(self.recurseTypeList(allTypeDict,
                               allTypeDict[item[1]], level+1, alreadyListed))
            return strList


	class PartWriter:
            """Generates a string representation of a typecode representing
               a <message><part>
            """
	    def __init__(self):
		self.typecode = None
                self.tns = None
		self.name = None
                self.docCode = []

	    def __recurse_tdc(self, tp):
                """tp -- schema.TypeDescriptionComponent instance
                """
		tp.type
		if isinstance(tp.type, TypeDescriptionComponent):
		    tp.type
		    tp = self.__recurse_tdc(tp.type)
		else:
		    return tp.type

	    def fromPart(self, part):
                """part -- wsdl.Part instance
                """

		bti = BaseTypeInterpreter()

		if part.getType():
		    tp = part.getType()
		elif part.getElement():
		    tp = part.getElement()
		    self.name = tp.getName()
		    return
                else:
                    raise WsdlGeneratorError, 'whoa!  part typing problem!'

		self.typecode = []

                self.tns = tp.getTargetNamespace()

                if not isinstance(tp, ZSI.wsdlInterface.ZSITypeAdapter):
                    raise TypeError, 'not a type adapter'

		elif tp.isSimpleType():
		    if tp.getQName():
			tpc = bti.get_typeclass(tp.getQName(),
                                                tp.getTargetNamespace())
                        self.docCode.append('%s' % part.getName())
                        self.docCode.append(bti.get_pythontype(tp.getQName(),
                                                tp.getTargetNamespace()))

                        if not tpc:
                            # fail over
                            t = tp.getName()
                        else:
                            t = tpc

			self.typecode.append('%s(pname="%s",aname="_%s",optional=1)' \
                                             %(t, part.getName(),
                                               part.getName()))
		    elif tp.getName():

                        self.docCode.append(part.getName())
                        self.docCode.append(tp.getName())
			self.typecode.append('%s(pname="%s",aname="_%s",optional=1)' \
                                             %(tp.getName(), part.getName(),
                                               part.getName()))
		    else:
			raise WsdlGeneratorError, 'shouldnt happen'

		elif tp.isComplexType():
                    self.docCode.append(part.getName())
                    self.docCode.append(tp.getName())
		    self.typecode.append('%s( name="%s", ns=ns )'\
                                         %(tp.getName(), part.getName()))

		else:
                    raise WsdlGeneratorError, 'shouldnt happen'
		return


class SchemaDescription:
    """Generates classes for all global definitions and declarations in 
       a schema instance.
    """
    def __init__(self):
        self.nsh = NamespaceHash()
        self.typeDict = {}
        return

    def fromWsdl(self, schema, alternateWriter):
        """schema -- schema.Schema instance
        """
        if not isinstance(schema, ZSISchemaAdapter):
	    raise TypeError, 'type %s not a Schema' %(schema.__class__)

	self.header = '%s \n# %s \n#\n# %s \n%s\n' \
                      %('#'*30, 'targetNamespace',
                        schema.getTargetNamespace(), '#'*30)

        self.header += '\n\n# imported as: %s' % \
                       self.nsh.getAlias(schema.getTargetNamespace())

        self.header += '\nclass %s:' % \
                       self.nsh.getModuleName(schema.getTargetNamespace())
        self.header += "\n%stargetNamespace = '%s'" % \
                       (ID1, schema.getTargetNamespace())

	self.body = ''
        self.last = ''
        
        self.class_dict = {}
        self.class_list = []
        
        self.generate(schema.getTypesDict(), alternateWriter)
        self.generate(schema.getElementsDict(), alternateWriter)
        self.getClassDefs(self.class_list, self.class_dict)
        
        self.body += '\n\n# define class alias for subsequent ns classes'
        self.body += '\n%s = %s' \
                     % ( self.nsh.getAlias(schema.getTargetNamespace()),
                         self.nsh.getModuleName(schema.getTargetNamespace()))
        if self.last:
            self.body += self.last

    def generate(self, sdict, alternateWriter):

        if alternateWriter:
            exec( 'import %s' % alternateWriter[0] )
            alternateWriter = '%s.%s()' % (alternateWriter[0],
                                           alternateWriter[1] )
        
	for name, tp in sdict.items():
            
            defaultWriter = 'self.__class__.TypeWriter()'
            
            if alternateWriter:
                exec( 'tw = %s' % alternateWriter )
            else:
                exec( 'tw = %s' % defaultWriter )

            ref = weakref.ref(self)

            tw.fromType(tp, ref)
            if tw.precede:
                if self.class_dict.has_key(tw.precede):
                    self.class_dict[tw.precede].append(tw)
                else:
                    self.class_dict[tw.precede] = [tw]
            else:
                self.class_list.append(tw.name)
                self.extractCode(tw)
            self.typeDict.update(tw.typeDict)


    def getClassDefs(self, class_list, class_dict):
        check_list = []
        for indx in range(len(class_list)):
            if class_dict.has_key(class_list[indx]):
                for tw in class_dict[class_list[indx]]:
                    self.extractCode(tw)
                    check_list.append(tw.name)
                else:
                    del class_dict[class_list[indx]]
        if check_list:
            self.getClassDefs(check_list, class_dict)
        else:
            for l in class_dict.values():
                for tw in l:
                    self.extractCode(tw)

    def extractCode(self, tw):
        self.body += tw.prepend.getvalue()
        self.body += tw.classdef.getvalue()
        self.body += tw.classvar.getvalue()
        self.body += tw.initdef.getvalue()
        self.body += tw.initcode.getvalue()
        self.body += tw.basector.getvalue()
        self.body += tw.postpend.getvalue()


    def write(self, fd=sys.stdout):
	fd.write(self.header)
	fd.write(self.body)
	fd.write('\n'*4)

    class TypeWriter:
        """Generates a string representation of a typecode representing
           a schema declaration or definition.
        """
	def __init__(self):
	    self.bti = BaseTypeInterpreter()
            self.nsh = NamespaceHash()
	    self.name = None
	    self.precede = None
            self.prepend  = StringWriter()
            self.classdef = StringWriter()
            self.classvar = StringWriter()
            self.initdef  = StringWriter()
            self.initcode = StringWriter()
            self.basector = StringWriter()
            self.postpend = StringWriter()
            self.allOptional = False
            self.hasRepeatable = False
            self.typeList = []
            self.typeDict = {}
	    return

	def fromType(self, myType, parentRef):
            """myType -- Type representation
            """

	    tp = myType

            if tp.isSimpleType():
                self.name = tp.getName() + '_Def'
                self._fromSimpleType(tp)

	    elif tp.isWildCard():
                self._fromWildCard(tp)

            elif tp.isElement():
                self.name = tp.getName() + '_Dec'
                self._fromElement(tp)

	    elif tp.isComplexType():
                self.name = tp.getName() + '_Def'
                self._fromComplexType(tp)

            elif tp.isAttribute():

                self._fromAttribute(tp)

	    else:
		raise WsdlGeneratorError, 'WARNING: NOT HANDLED %s' \
                      % (tp.__class__)

            alias = self.nsh.getAlias(tp.getTargetNamespace())
            key = "%s.%s_Def" % (alias, tp.getName())
            if self.typeList:
                self.typeList.sort()
                    # add entry to type dictionary for later use in
                    # docstring generation
                self.typeDict[key] = self.typeList
	    return

        def _fromSimpleType(self, tp):
            
            tp = tp.getDefinition()
            
            if tp.getName():
                tpc = tp.getTypeclass()
                self.initdef.set('\n%sdef __init__(self, name=None, ns=None, **kw):' % (ID2))
                objName = '_' + tp.getName()
                if tpc:
                    typeName = self.bti.get_pythontype(None, None, tpc)
                    if not typeName:
                        typeName = 'Any'
                    self.precede  = '%s' % (tpc)
                    self.classdef.set('\n\n%sclass %s(%s):' \
                                      % (ID1, tp.getName() + '_Def', tpc))
                    self.basector.set('\n%s%s.__init__(self,pname="%s",optional=1,repeatable=1)' % (ID3,tpc,tp.getName()))
                else:
                    typeName = 'Any'
                    # XXX: currently, unions will get shuffled thru here.
                    self.classdef.set('\n\n%sclass %s(ZSI.TC.Any):' \
                                      % (ID1, tp.getName() + '_Def'))
                    self.initcode.write('\n%s# probably a union - dont trust it' % ID3)
                    self.basector.set('\n%sZSI.TC.Any.__init__(self,pname=name,aname="_%%s" %% name , optional=1,repeatable=1, **kw)' % ID3)

                self.typeDoc('optional=1', objName, typeName)
            else:
                raise WsdlGeneratorError, 'shouldnt happen'

        def _fromWildCard(self, tp):
            # XXX: not particularly trustworthy either.  pending further work.
            tp = tp.getDeclaration()
            self.classdef.set('\n\n%sclass %s(ZSI.TC.XML):' \
                              % (ID1, tp.getName()))
            self.initdef.set('\n%s__init__(self,pname):' % (ID2))
            self.basector.set('\n%sZSI.TC.XML.__init__(self,pname,**kw)' % ID3)

        def _fromAttribute(self, tp):
            self.classdef.set('\n\n%sclass %s:' % (ID1, tp.getName()))
            self.classvar.set('\n%s# not yet implemented' % ID2)
            self.classvar.write('\n%s# attribute declaration' % ID2)
            self.classvar.write('\n%spass\n' % ID2)

        def _fromElement(self, tp):

            etp = tp.getType()

            if etp and etp.isDefinition():    

                if etp.isSimpleType():
                    self._elementSimpleType(tp, etp)

                elif etp.isComplexType():
                    self._elementComplexType(tp, etp)


            elif not etp:
                self.classdef.set('\n\n%sclass %s(Struct):' \
                                  % (ID1, tp.getName()))
                self.initdef.set('\n%sdef __init__(self, name=None, ns=None, **kw):' % (ID2))
                self.basector.set('\n%sStruct.__init__(self, self.__class__, [], pname="%s", aname="_%s", inline=1)' % (ID3,tp.getName(),tp.getName()))
            else:
                raise WsdlGeneratorError, 'Unknown type(%s) not handled ' \
                      % (etp.__class__)

        def _elementSimpleType(self, tp, etp):

            tpc = etp.getTypeclass()
            self.precede   = '%s' % (tpc)

            self.classdef.set('\n\n%sclass %s(%s):' \
                              % (ID1, tp.getName() + '_Dec', tpc))
            
            self.classvar.set('\n%sliteral = "%s"' % (ID2, tp.getName()))
            self.classvar.write('\n%sschema = "%s"' % \
                                (ID2,tp.getTargetNamespace()))
            
            self.initdef.set('\n\n%sdef __init__(self, name=None, ns=None, **kw):' \
                             % ID2)

            self.initcode.set('\n%sname = name or self.__class__.literal' \
                              % ID3)
            self.initcode.write('\n%sns = ns or self.__class__.schema' % ID3)

            self.basector.set('\n\n%s%s.__init__(self,pname=name, **kw)' % (ID3,tpc))
            typeName = self.bti.get_pythontype(None, None, tpc)
            self.typeDoc('', '__param', typeName)
                  

        def _elementComplexType(self, tp, etp):

            if etp.getName():

                self.precede  = '%s' %(etp.getName() + '_Def' )
                
                if etp.getTargetNamespace() != tp.getTargetNamespace():

                    nsp = etp.getTargetNamespace()
                    self.classdef.set('\n\n%sclass %s(%s.%s):' \
                                      % (ID1, tp.getName() + '_Dec',
                                         self.nsh.getAlias(nsp),
                                         etp.getName() + '_Def'))
                else:
                    self.classdef.set('\n\n%sclass %s(%s):' \
                                      % (ID1, tp.getName() + '_Dec',
                                         etp.getName() + '_Def'))

                self.classvar.set('\n%sliteral = "%s"' % ( ID2, tp.getName()))
                self.classvar.write('\n%sschema = "%s"' \
                                    % ( ID2,tp.getTargetNamespace()))
                
                self.initdef.set('\n\n%sdef __init__(self, name=None, ns=None, **kw):' %(ID2))

                self.initcode.set('\n%sname = name or self.__class__.literal'\
                                  % ID3 )
                self.initcode.write('\n%sns = ns or self.__class__.schema'\
                                    % ID3 )

                nsp = etp.getTargetNamespace()
                
                typeName = '%s.%s_Def' % (self.nsh.getAlias(nsp), etp.getName())
                self.basector.set('\n\n%s%s.__init__(self, name=name, ns=ns, **kw)'  % (ID3, typeName))
                self.postpend.set('\n%sself.typecode = %s(name=name, ns=ns, **kw)' % (ID3, typeName))
                self.typeDoc('', '_' + tp.getName(), typeName)
            else:
                # at this point what we have is an global element declaration
                # containing a local complex type definition.

                # so, this is a little odd voodoo so that we can
                # use the code for processing complex types.

                self._fromComplexType(etp.expressLocalAsGlobal(tp))

                # now we are discaring the _Dec(LOCAL_Def) subclassing
                # and expressing the declaration w/the local def as
                # a def.  retweek the classdef and off we go...

                self.classdef.set('\n\n%sclass %s(ZSI.TCcompound.Struct):' \
                                  %(ID1, tp.getName() + '_Dec'))

                self.classvar.set( re.sub('type', 'literal',
                                          self.classvar.getvalue()))
                self.initcode.set('\n%sname = name or self.__class__.literal\n%sns = ns or self.__class__.schema\n%s' % ( ID3, ID3, self.initcode.getvalue()))
                
                return


        def _fromComplexType(self, tp):

            if isinstance(tp, ZSI.wsdlInterface.ZSISchemaTypeAdapter ):
                # the "usual"
                tp = tp.getDefinition()
            else:
                # this is when an element has
                # a local complex type def
                pass
                
            typecodelist = '['


            if tp.isComplexContent():
                self._complexTypeComplexContent(tp)
                return

            if tp.isSimpleContent():
                self._complexTypeSimpleContent(tp)
                return 
            

            # ok, it's not derived content and therefore has a model group
            # write out the class def and class variables

            self.classdef.set('\n\n%sclass %s:' \
                              %(ID1, tp.getName() + '_Def'))
            
            if self._complexTypeHandleAttributes(tp):
                # not yet implemented
                pass
            
            self.classvar.set("\n%sschema = '%s'" % (ID2,
                                                     tp.getTargetNamespace()))
            self.classvar.write("\n%stype = '%s'\n" % (ID2, tp.getName()))

            self.initdef.set('\n%sdef __init__(self, name=None, ns=None, **kw):' % (ID2))

            typecodelist = '['

            mg = tp.getModelGroup()
                
            if mg.isAll() or mg.isSequence():
                typecodelist += self._complexTypeAllOrSequence(tp, mg)
                
            elif mg.isChoice():
                typecodelist += self._complexTypeChoice(tp, mg)
                    
            else:
                # if we get here, we hit a "void" model group.  ie:
                # <xsd:element name="getValue">
                #  <xsd:complexType/>
                # </xsd:element>
                self.classdef.set('\n\n%sclass %s(ZSI.TCcompound.Struct):'\
                                  %(ID1, tp.getName() + '_Def'))
                pass


            typecodelist += ']'

            self._complexTypecodeLogic( typecodelist )

            return

        def _complexTypeComplexContent(self, tp):

            dt = tp.getDerivedTypes()
            tc = dt.getTypeclass()

            if not tc:
                # ie: not in a default namespace
                if dt.getDerivation():
                    # XXX: this will need more work

                    # ok, i'm totally cheating here.  getDerivedContent
                    # returns a ModelGroupAdapter even tho it's not
                    # technically a model group.  however, i can then
                    # feed it to the complex type generation methods to
                    # harvest a type code list.  to end the cheat,
                    # self.initdef|classdef are re-assigned to here and
                    # off we go.
                    if dt.contentIsSequence() or dt.contentIsAll():
                        tclist = self._complexTypeAllOrSequence(tp,
                                                                dt.getContent())
                    elif dt.contentIsChoice():
                        tclist = self._complexTypeChoice(tp,
                                                         dt.getContent())
                    else:
                        # dubious?
                        tclist = ''
                        
                    # end cheating....
                    
                    self.precede  = '%s%s' % ( dt.getDerivation(), '_Def' )
                    nsp = self.nsh.getAlias(tp.getTargetNamespace())
                    self.classdef.set('\n\n%sclass %s(%s):' \
                                      %(ID1, tp.getName() + '_Def',
                                        dt.getDerivation() + '_Def'))
                    self.classvar.set('\n%s# rudimentary - more soon' % ID2)
                    self.classvar.write("\n%sschema = '%s'" % \
                                        (ID2, tp.getTargetNamespace()))
                    self.classvar.write("\n%stype = '%s'" % (ID2,tp.getName()))
                    self.initdef.set('\n\n%sdef __init__(self, name=None, ns=None, **kw):' % ID2)
                    self.initcode.write('\n\n%sif name:' % ID3)
                    self.initcode.write('\n%sTCList = [%s]' % (ID4, tclist))
                    self.basector.set('\n%s%s.%s.__init__(self, name=name, ns=ns, **kw)' % (ID4, nsp, dt.getDerivation() + '_Def' ))
                    if dt.isExtension():
                        self.postpend.set('\n%s# extending....' % ID4)
                        self.postpend.write('\n%sself.ofwhat += tuple(TCList)'\
                                            % ID4)
                        self.postpend.write('\n%sself.lenofwhat += len(TCList)' % ID4)
                    elif dt.isRestriction():
                        self.postpend.set('\n%s# restricting....' % ID4)
                        self.postpend.write('\n%sself.ofwhat = tuple(TCList)' \
                                            % ID4)
                        self.postpend.write('\n%sself.lenofwhat = len(TCList)'\
                                            % ID4)
                else:
                    self.classdef.set('\n\n%sclass %s:' \
                                      % (ID1, tp.getName() + '_Dec'))
                    self.classvar.set('\n%s# not yet implemented' % ID2)
                    self.classvar.write('\n%s# non array complexContent' % ID2)
                    self.classvar.write('\n%spass\n' % ID2)
            elif '%s' % tc == 'ZSI.TCcompound.Array':
                # ladies and gents, we have an array
                self.classdef.set('\n\n%sclass %s(%s):' \
                                  % (ID1, tp.getName() + '_Def', tc))
                self.initdef.set("\n%sdef __init__(self, name = None, ns = None, **kw):" % ID2)

                arrayinfo = dt.getArrayType()
                
                if arrayinfo:
                    nsp = ''
                    if arrayinfo[2]:
                        nsp  = self.nsh.getAlias(tp.getTargetNamespace())
                        nsp += '.'
                        atype = arrayinfo[1] + '_Def'
                        typeName = '%s%s' % (nsp, atype)
                    else:
                        atype = arrayinfo[1]
                        typeName = self.bti.get_pythontype(None, None, atype)
                        if not typeName:
                            typeName = 'Any'

                    self.basector.set("\n%s%s.__init__(self, '%s', %s%s(name=None), pname=name, aname='_%%s' %% name, oname='%%s xmlns=\"%s\"' %% name, **kw)" \
                                      % (ID3, tc, arrayinfo[0], nsp,
                                         atype, tp.getTargetNamespace()))
                        
                    self.typeDoc('', '_element', typeName)
                else:
                    raise WsdlGeneratorError, 'failed to handle array!'
            else:
                raise WsdlGeneratorError, 'failed to handle complex content'
            
            return

        def _complexTypeSimpleContent(self, tp):
            dt = tp.getDerivedTypes()

            if dt.isSimpleContent() and dt.getTypeclass():
                self.classdef.set('\n\n%sclass %s(%s):' \
                                  % (ID1, tp.getName() + '_Def',
                                     dt.getTypeclass()))
                self.classvar.set('\n%s# rudimentary support' % ID2)
                self.classvar.write('\n%stag = "%s"' % (ID2, tp.getName()))
                self.classvar.write('\n%sliteral = "%s"' %(ID2, tp.getName()))
                self.classvar.write('\n%sschema = "%s"' % \
                                    (ID2, tp.getTargetNamespace()))
                
                self.initdef.set('\n\n%sdef __init__(self, name=None, ns=None, **kw):' % ID2)
                self.initcode.set('\n%sname = name or self.__class__.literal'\
                                  % ID3)
                self.initcode.write('\n%sns = ns or self.__class__.schema' \
                                    % ID3)
                self.basector.set('\n\n%s%s.__init__(self, pname=name, **kw)' \
                                  %( ID3, dt.getTypeclass()))
                return
            else:
                raise WsdlGeneratorError, \
                      'could not determine simple content base'


        def _complexTypeAllOrSequence(self, tp, mg):

            self.classdef.set('\n\n%sclass %s(ZSI.TCcompound.Struct):'\
                              %(ID1, tp.getName() + '_Def'))

            typecodelist = ''

            self.initcode.set('\n%s# internal vars' % ID3)
                
            for e in mg.getContent():
                if e.isDeclaration() and e.isElement():

                    etp = None
                            
                    if e.getType():
                        etp = e.getType()
         
                    if e.getName():
                        self.initcode.write('\n%sself._%s = None' \
                                            % (ID3, e.getName()))
                    elif etp and etp.getName():
                        # element references
                        self.initcode.write('\n%sself._%s = None' \
                                            % (ID3, etp.getName()))

                    if e.getName():
                        objName = '_' + e.getName()
                    else:
                        objName = '_None'   # fix
                    occurs = None

                    if e.isDeclaration() and e.isWildCard():
                        occurs = self._calculateOccurance(e)

                        typeName = 'Any'
                        typecodelist += self._getWildcardTypecode(e, occurs)

                    elif e.isDeclaration() and e.isAnyType():
                        typeName = 'XML'
                        typecodelist  += 'ZSI.TC.XML(pname="%s",aname="_%s"), '\
                                         %(e.getName(),e.getName())

                    elif e.isDeclaration() and e.isElementReference():
                        occurs = self._calculateOccurance(e)
                        nsp = self.nsh.getAlias(etp.getTargetNamespace())
                        typeName = '%s.%s' % (nsp, e.getName()) + '_Dec'
                        typecodelist +='%s(ns=ns%s), '\
                                        %(typeName, occurs)

                    elif etp.isDefinition() and etp.isSimpleType():
                        occurs = self._calculateOccurance(e)

                        tpc = None
                        tpc = etp.getTypeclass()

                        if tpc:
                            typeName = self.bti.get_pythontype(None, None, tpc)
                            if not typeName:
                                typeName = 'Any'
                                            
                            typecodelist +=\
                                         '%s(pname="%s",aname="_%s"%s), ' \
                                         %(tpc,e.getName(),e.getName(),
                                           occurs)
                        else:
                            nsp = self.nsh.getAlias(etp.getTargetNamespace())
                            typeName = '%s.%s' % (nsp, etp.getName()) + '_Def'
                            typecodelist +='%s(name="%s",ns=ns%s), '\
                                            %(typeName, e.getName(), occurs)

                    elif etp.isDefinition() and etp.isComplexType():
                        occurs = self._calculateOccurance(e)

                        nsp = self.nsh.getAlias(etp.getTargetNamespace())
                        typeName = '%s.%s' % (nsp,etp.getName()) + '_Def'
                        typecodelist  += '%s(name="%s", ns=ns%s), ' \
                                         %(typeName, e.getName(), occurs)
                        self.precede = '%s%s' % ( etp.getName(), '_Def' )

                    elif etp:
                        # here we have a hold of a LocalElementDef
                        # like an element reference.  bogosity.
                        # we dont hit this much
                        occurs = self._calculateOccurance(e)
                        typeName = etp.getType().getName()
                                
                        typecodelist  += '%s(name="%s",ns=ns%s), '\
                                         % (typeName, etp.getName(), occurs)
                    elif e:
                        raise WsdlGeneratorError, 'instance %s not handled '\
                              % (e.getName())
                    else:
                        raise WsdlGeneratorError, 'instance %s not handled '\
                              % (e)

                    self.typeDoc(occurs, objName, typeName)

                else:
                    raise WsdlGeneratorError, 'instance %s not handled '\
                          % (e.__class__)
            else:
                pass

            return typecodelist

        def _complexTypeChoice( self, tp, mg ):

            # XXX: this has been somewhat neglected

            self.allOptional = True

            return self._complexTypeAllOrSequence( tp, mg )

            # the rest of this is pending further work, using
            # the All/Sequence gives us immediate functionality.

            # we shall get back to this....

            typecodelist = 'ZSI.TCcompound.Choice(['

            self.initcode.set('\n%s# internal vars' % ID3)
		    
            for e in mg.getContent():
                        
                if e.isDeclaration() and e.isElement():
                            
                    etp = None
                    if e.getType():
                        etp = e.getType()
				
                    self.initcode.write('\n%sself._%s = None' \
                                        % (ID2, e.getName()))
                            
                    if e.isAnyType():
                        typecodelist += 'ZSI.TC.Any(pname="%s",aname="%s"), '\
                                        %(e.getName(),e.getName())

                    elif etp.isDefinition() and etp.isSimpleType():
                        occurs = self._calculateOccurance(e)

                        tpc = None
                        tpc = etp.getTypeclass()

                        typecodelist  += '%s(pname="%s",aname="_%s"%s), '\
                                         %(tpc,e.getName(),e.getName(),
                                           occurs)

                    elif etp.isDefinition() and etp.isComplexType():
                        typecodelist  += 'Struct(%s,%s().typecode,pname="%s",aname="_%s"), '\
                                         %(etp.getName(),etp.getName(),
                                           e.getName(),e.getName())
			    
                    elif etp:
                        self.initcode.write('\n%sself._%s = None' % \
                                            (ID2, e.getName()))
                        typecodelist  += '%s("%s"), '\
                                         %(etp.getName(), e.getName())
                    elif e:
                        raise WsdlGeneratorError, 'instance %s not handled '\
                              %(e.getName())
                    else:
                        raise WsdlGeneratorError, \
                              'instance %s not handled ' % (e)
                else:
                    raise WsdlGeneratorError, 'instance %s not handled '\
                          %(e.__class__)
            else:
                    pass

            return typecodelist

        def _complexTypecodeLogic( self, typecodelist ):

            # extra "smarts" for all regular (model group) complex type defs.

            extraFlags = ''

            if self.hasRepeatable:
                extraFlags += 'hasextras=1, '


            self.initcode.write('\n\n%sTClist = %s' % (ID3, typecodelist))
            self.initcode.write('\n\n%soname = name' % ID3)


            self.initcode.write('\n\n%sif name:' % ID3)
            self.initcode.write("\n%saname = '_%%s' %% name" % ID4)
            self.initcode.write('\n%sif ns:' % ID4)
            self.initcode.write("\n%soname += ' xmlns=\"%%s\"' %% ns" % ID5)
            self.initcode.write('\n%selse:' % ID4)
            self.initcode.write("\n%soname += ' xmlns=\"%%s\"' %% self.__class__.schema"%(ID5))
            self.initcode.write("\n%selse:" % ID3)
            self.initcode.write("\n%saname = None" % ID4)

            self.basector.write('\n\n%sZSI.TCcompound.Struct.__init__(' % ID3)
            self.basector.write('self, self.__class__, TClist,')
            self.basector.write('\n%s%spname=name, inorder=0,' % (ID3,
                                                                  ' ' * 31))
            self.basector.write('\n%s%saname=aname, oname=oname,'\
                                % (ID3, ' ' * 31))
            self.basector.write('\n%s%s%s**kw)' % (ID3, ' ' * 31,
                                                   extraFlags))



        def _complexTypeHandleAttributes(self, tp):
            # XXX: need to revisit attributes - incomplete
            
            tmp = ''

            for a in tp.getAttributes():
                #tmp += '("%s","%s"),' % (a.getName(), a.getQName())
                pass

            return tmp

        def _calculateOccurance(self, e):
            occurs = ''
            
            if e.getMaxOccurs() == 'unbounded' or \
                   int(e.getMaxOccurs()) > 1:
                occurs += ', repeatable=1'
                self.hasRepeatable = True
                                
            if int(e.getMinOccurs()) == 0 or \
                   e.isNillable() or self.allOptional:
                occurs += ', optional=1'

            return occurs

	def __recurse_tdc(self, tp):
	    tp.type
	    if isinstance(tp.type, TypeDescriptionComponent):
		tp.type
		tp = self.__recurse_tdc(tp.type)
	    else:
		return tp.type

        
        def typeDoc(self, occurs, objName, typeName):
            """Generates an entry in the type list for later use
               by docstring generation.
            """
            if not occurs:
                self.typeList.append([objName, typeName, False])
            elif occurs.find('optional=1') == -1:
                self.typeList.append([objName, typeName, False])
            else:
                self.typeList.append([objName, typeName, True])


        def _getWildcardTypecode(self, e, occurs):
            return 'ZSI.TC.Any(pname="%s",aname="_%s"%s), '\
                   %(e.getName(),e.getName(),occurs)
