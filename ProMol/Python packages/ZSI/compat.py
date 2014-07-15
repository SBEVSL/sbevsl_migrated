#! /usr/bin/env python
"""Compatibility module, imported by ZSI if you don't have PyXML 0.7.

No copyright violations -- we're only using parts of PyXML that we
wrote.
"""

from ZSI import _copyright

class SOAP:
    ENV         = "http://schemas.xmlsoap.org/soap/envelope/"
    ENC         = "http://schemas.xmlsoap.org/soap/encoding/"
    ACTOR_NEXT  = "http://schemas.xmlsoap.org/soap/actor/next"

class SCHEMA:
    XSD1        = "http://www.w3.org/1999/XMLSchema"
    XSD2        = "http://www.w3.org/2000/10/XMLSchema"
    XSD3        = "http://www.w3.org/2001/XMLSchema"
    XSI1        = "http://www.w3.org/1999/XMLSchema-instance"
    XSI2        = "http://www.w3.org/2000/10/XMLSchema-instance"
    XSI3        = "http://www.w3.org/2001/XMLSchema-instance"
    BASE        = XSD3

_copyright += "\n\nPortions are also: "
_copyright += '''Copyright 2001, Zolera Systems Inc.  All Rights Reserved.
Copyright 2001, MIT. All Rights Reserved.

Distributed under the terms of:
  Python 2.0 License or later.
  http://www.python.org/2.0.1/license.html
or
  W3C Software License
  http://www.w3.org/Consortium/Legal/copyright-software-19980720
'''

from xml.dom import Node
try:
    from xml.ns import XMLNS
except:
    class XMLNS:
        BASE = "http://www.w3.org/2000/xmlns/"
        XML = "http://www.w3.org/XML/1998/namespace"
import cStringIO as StringIO

_attrs = lambda E: (E.attributes and E.attributes.values()) or []
_children = lambda E: E.childNodes or []
_IN_XML_NS = lambda n: n.namespaceURI == XMLNS.XML

# Does a document/PI has lesser/greater document order than the
# first element?
_LesserElement, _Element, _GreaterElement = range(3)

def _sorter(n1,n2):
    '''_sorter(n1,n2) -> int
    Sorting predicate for non-NS attributes.'''

    i = cmp(n1.namespaceURI, n2.namespaceURI)
    if i: return i
    return cmp(n1.localName, n2.localName)


def _sorter_ns(n1,n2):
    '''_sorter_ns((n,v),(n,v)) -> int
    "(an empty namespace URI is lexicographically least)."'''

    if n1[0] == 'xmlns': return -1
    if n2[0] == 'xmlns': return 1
    return cmp(n1[0], n2[0])

def _utilized(n, node, other_attrs, unsuppressedPrefixes):
    '''_utilized(n, node, other_attrs, unsuppressedPrefixes) -> boolean
    Return true if that nodespace is utilized within the node'''

    if n.startswith('xmlns:'):
        n = n[6:]
    elif n.startswith('xmlns'):
        n = n[5:]
    if n == node.prefix or n in unsuppressedPrefixes: return 1
    for attr in other_attrs:
        if n == attr.prefix: return 1
    return 0

_in_subset = lambda subset, node: not subset or node in subset

class _implementation:
    '''Implementation class for C14N. This accompanies a node during it's
    processing and includes the parameters and processing state.'''

    # Handler for each node type; populated during module instantiation.
    handlers = {}

    def __init__(self, node, write, **kw):
        '''Create and run the implementation.'''

        self.write = write
        self.subset = kw.get('subset')
        if self.subset:
            self.comments = kw.get('comments', 1)
        else:
            self.comments = kw.get('comments', 0)
        self.unsuppressedPrefixes = kw.get('unsuppressedPrefixes')
        nsdict = kw.get('nsdict', { 'xml': XMLNS.XML, 'xmlns': XMLNS.BASE })

        # Processing state.
        self.state = (nsdict, ['xml'], [])

        if node.nodeType == Node.DOCUMENT_NODE:
            self._do_document(node)
        elif node.nodeType == Node.ELEMENT_NODE:
            self.documentOrder = _Element        # At document element
            if self.unsuppressedPrefixes is not None:
                self._do_element(node)
            else:
                inherited = self._inherit_context(node)
                self._do_element(node, inherited)
        elif node.nodeType == Node.DOCUMENT_TYPE_NODE:
            pass
        else:
            raise TypeError, str(node)


    def _inherit_context(self, node):
        '''_inherit_context(self, node) -> list
        Scan ancestors of attribute and namespace context.  Used only
        for single element node canonicalization, not for subset
        canonicalization.'''

        # Collect the initial list of xml:foo attributes.
        xmlattrs = filter(_IN_XML_NS, _attrs(node))

        # Walk up and get all xml:XXX attributes we inherit.
        inherited, parent = [], node.parentNode
        while parent and parent.nodeType == Node.ELEMENT_NODE:
            for a in filter(_IN_XML_NS, _attrs(parent)):
                n = a.localName
                if n not in xmlattrs:
                    xmlattrs.append(n)
                    inherited.append(a)
            parent = parent.parentNode
        return inherited


    def _do_document(self, node):
        '''_do_document(self, node) -> None
        Process a document node. documentOrder holds whether the document
        element has been encountered such that PIs/comments can be written
        as specified.'''

        self.documentOrder = _LesserElement
        for child in node.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                self.documentOrder = _Element        # At document element
                self._do_element(child)
                self.documentOrder = _GreaterElement # After document element
            elif child.nodeType == Node.PROCESSING_INSTRUCTION_NODE:
                self._do_pi(child)
            elif child.nodeType == Node.COMMENT_NODE:
                self._do_comment(child)
            elif child.nodeType == Node.DOCUMENT_TYPE_NODE:
                pass
            else:
                raise TypeError, str(child)
    handlers[Node.DOCUMENT_NODE] = _do_document


    def _do_text(self, node):
        '''_do_text(self, node) -> None
        Process a text or CDATA node.  Render various special characters
        as their C14N entity representations.'''
        if not _in_subset(self.subset, node): return
        s = node.data \
                .replace("&", "&amp;") \
                .replace("<", "&lt;") \
                .replace(">", "&gt;") \
                .replace("\015", "&#xD;")
        if s: self.write(s)
    handlers[Node.TEXT_NODE] = _do_text
    handlers[Node.CDATA_SECTION_NODE] = _do_text


    def _do_pi(self, node):
        '''_do_pi(self, node) -> None
        Process a PI node. Render a leading or trailing #xA if the
        document order of the PI is greater or lesser (respectively)
        than the document element.
        '''
        if not _in_subset(self.subset, node): return
        W = self.write
        if self.documentOrder == _GreaterElement: W('\n')
        W('<?')
        W(node.nodeName)
        s = node.data
        if s:
            W(' ')
            W(s)
        W('?>')
        if self.documentOrder == _LesserElement: W('\n')
    handlers[Node.PROCESSING_INSTRUCTION_NODE] = _do_pi


    def _do_comment(self, node):
        '''_do_comment(self, node) -> None
        Process a comment node. Render a leading or trailing #xA if the
        document order of the comment is greater or lesser (respectively)
        than the document element.
        '''
        if not _in_subset(self.subset, node): return
        if self.comments:
            W = self.write
            if self.documentOrder == _GreaterElement: W('\n')
            W('<!--')
            W(node.data)
            W('-->')
            if self.documentOrder == _LesserElement: W('\n')
    handlers[Node.COMMENT_NODE] = _do_comment


    def _do_attr(self, n, value):
        ''''_do_attr(self, node) -> None
        Process an attribute.'''

        W = self.write
        W(' ')
        W(n)
        W('="')
        s = value \
            .replace("&", "&amp;") \
            .replace("<", "&lt;") \
            .replace('"', '&quot;') \
            .replace('\011', '&#x9') \
            .replace('\012', '&#xA') \
            .replace('\015', '&#xD')
        W(s)
        W('"')


    def _do_element(self, node, initial_other_attrs = []):
        '''_do_element(self, node, initial_other_attrs = []) -> None
        Process an element (and its children).'''

        # Get state (from the stack) make local copies.
        #       ns_parent -- NS declarations in parent
        #       ns_rendered -- NS nodes rendered by ancestors
        #       xml_attrs -- Attributes in XML namespace from parent
        #       ns_local -- NS declarations relevant to this element
        ns_parent, ns_rendered, xml_attrs = \
                self.state[0], self.state[1][:], self.state[2][:]
        ns_local = ns_parent.copy()

        # Divide attributes into NS, XML, and others.
        other_attrs = initial_other_attrs[:]
        in_subset = _in_subset(self.subset, node)
        for a in _attrs(node):
            if a.namespaceURI == XMLNS.BASE:
                n = a.nodeName
                if n == "xmlns:": n = "xmlns"        # DOM bug workaround
                ns_local[n] = a.nodeValue
            elif a.namespaceURI == XMLNS.XML:
                if self.unsuppressedPrefixes is None or in_subset:
                    xml_attrs.append(a)
            else:
                other_attrs.append(a)

        # Render the node
        W, name = self.write, None
        if in_subset:
            name = node.nodeName
            W('<')
            W(name)

            # Create list of NS attributes to render.
            ns_to_render = []
            for n,v in ns_local.items():
                pval = ns_parent.get(n)

                # If default namespace is XMLNS.BASE or empty, skip
                if n == "xmlns" \
                and v in [ XMLNS.BASE, '' ] and pval in [ XMLNS.BASE, '' ]:
                    continue

                # "omit namespace node with local name xml, which defines
                # the xml prefix, if its string value is
                # http://www.w3.org/XML/1998/namespace."
                if n == "xmlns:xml" \
                and v in [ 'http://www.w3.org/XML/1998/namespace' ]:
                    continue

                # If different from parent, or parent didn't render
                # and if not exclusive, or this prefix is needed or
                # not suppressed
                if (v != pval or n not in ns_rendered) \
                  and (self.unsuppressedPrefixes is None or \
                  _utilized(n, node, other_attrs, self.unsuppressedPrefixes)):
                    ns_to_render.append((n, v))

            # Sort and render the ns, marking what was rendered.
            ns_to_render.sort(_sorter_ns)
            for n,v in ns_to_render:
                self._do_attr(n, v)
                ns_rendered.append(n)

            # Add in the XML attributes (don't pass to children, since
            # we're rendering them), sort, and render.
            other_attrs.extend(xml_attrs)
            xml_attrs = []
            other_attrs.sort(_sorter)
            for a in other_attrs:
                self._do_attr(a.nodeName, a.value)
            W('>')

        # Push state, recurse, pop state.
        state, self.state = self.state, (ns_local, ns_rendered, xml_attrs)
        for c in _children(node):
            _implementation.handlers[c.nodeType](self, c)
        self.state = state

        if name: W('</%s>' % name)
    handlers[Node.ELEMENT_NODE] = _do_element


def Canonicalize(node, output=None, **kw):
    '''Canonicalize(node, output=None, **kw) -> UTF-8

    Canonicalize a DOM document/element node and all descendents.
    Return the text; if output is specified then output.write will
    be called to output the text and None will be returned
    Keyword parameters:
        nsdict: a dictionary of prefix:uri namespace entries
                assumed to exist in the surrounding context
        comments: keep comments if non-zero (default is 1 if subset, 0 if not)
        subset: Canonical XML subsetting resulting from XPath
                (default is [])
        unsuppressedPrefixes: do exclusive C14N, and this specifies the
                prefixes that should be inherited.
    '''

    if output:
        _implementation(node, output.write, **kw)
    else:
        s = StringIO.StringIO()
        _implementation(node, s.write, **kw)
        return s.getvalue()

if __name__ == '__main__': print _copyright
