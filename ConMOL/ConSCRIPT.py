import Pmw
import pymol
from pymol import cmd
import Tkinter
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import string
import os
import tkFileDialog
import re
import urllib2
import StringIO
import gzip
import time
import pmg_tk
from pmg_tk import startup

#Make sure it will work on Linux/Mac (with X11)/ and of course Windows
try:
    PYMOL_PATH=os.environ['PYMOL_PATH']
except KeyError:
    PYMOL_PATH='./'

filestack = []
filelevel = 0
UserDefinedGroups = {}


Pmw.initialise()

#Add it to the PyMOL menu Bar
def __init__(self):
    self.menuBar.addmenuitem('Plugin', 'command',
                             'Easy GUI',
                             label = 'ConSCRIPT',    
                             command = lambda s=self : converter(s))

class converter:
    def __init__(self, app):

        # create the dialog box which contains the GUI
        parent = app.root
        self.dialog = Pmw.Dialog(parent, title = 'ConSCRIPT')
        
        # set the size of the 
        #self.dialog.geometry('550x550')
        interior = self.dialog.interior()
            
        #TITLE BAR
        lab = Label(interior, 
            text='ConSCRIPT (C) Copyright 2007-2008\nS. Mottarella, C. Craig, H. Bernstein\nGPL, No Warranty', 
            background='#000066', foreground='white')
                        
        lab.pack(expand=0, fill='x', padx=4, pady=0)
	#Makes pages possible
        notebook = Pmw.NoteBook(interior)
        notebook.pack(fill='both', expand=1, padx=10, pady=10)

        page = notebook.add('SBEVSL Script Loader')
        notebook.tab('SBEVSL Script Loader').focus_set()
        group = Pmw.Group(page, tag_text = 'Log Controls')
        group.grid(row=0, column=0, padx=0, pady=0)
        interior = group.interior()
                
        #Run the Boffo Function	
        openbtn = Button(interior, text = 'Open Script')
        openbtn.grid()

        ##-----Select Function-----##
        def select( allparameters ):

            selection = ''
            
            if allparameters=='false':
                return allparameters
            elif allparameters.replace( ' ', '' )=='':
                return ''

            ## list of elements in the periodic table how they are entered in RasMol and PyMOL
            ## dictionary data structure { RasMol: PyMOL }
            
            periodictable = {'hydrogen': 'h','helium': 'he','lithium': 'li','beryllium': 'be','boron': 'b','carbon': 'c',
                             'nitrogen': 'n','oxygen': 'o','flourine': 'f','neon': 'ne','sodium': 'na','magnesium': 'mg',
                             'aluminum': 'al','silicon': 'si','phosphorus': 'p','sulfur': 's','chlorine': 'cl','argon': 'ar',
                             'potassium': 'k','calcium': 'ca','scandium': 'sc','titanium': 'ti','vanadium': 'v',
                             'chromium': 'cr','manganese': 'mn','iron': 'fe','cobalt': 'co','nickel': 'ni','copper': 'cu',
                             'zinc': 'zn','gallium': 'ga','germanium': 'ge','arsenic': 'as','selenium': 'se','bromine': 'br',
                             'krypton': 'kr','rubidium': 'rb','strontium': 'sr','yttrium': 'y','zirconium': 'zr',
                             'niobium': 'nb','molybdenum': 'mo','technetium': 'tc','ruthenium': 'ru','rhodium': 'rh',
                             'palladium': 'pd','silver': 'ag','cadmium': 'cd','indium': 'in','tin': 'sn','antimony': 'sb',
                             'tellurium': 'te','iodine': 'i','xenon': 'xe','cesium': 'cs','barium': 'ba','lanthanum': 'la',
                             'cerium': 'ce','praseodymium': 'pr','neodymium': 'nd','promethium': 'pm','samarium': 'sm',
                             'europium': 'eu','gadolinium': 'gd','terbium': 'tb','dysprosium': 'dy','holmium': 'ho',
                             'erbium': 'er','thulium': 'tm','ytterbium': 'yb','lutetium': 'lu','hafnium': 'hf',
                             'tantalum': 'ta','tungsten': 'w','rhenium': 're','osmium': 'os','iridium': 'ir','platinum': 'pt',
                             'gold': 'au','mercury': 'hg','thallium': 'tl','lead': 'pb','bismuth': 'bi','polonium': 'po',
                             'astatine': 'at','radon': 'rn','francium': 'fr','radium': 'ra','actinium': 'ac','thorium': 'th',
                             'protactinium': 'pa','uranium': 'u','neptunium': 'np','plutonium': 'pu','americium': 'am',
                             'curium': 'cm','berkelium': 'bk','californium': 'cf','einsteinium': 'es',
                             'fermium': 'fm','mendelevium': 'md','nobelium': 'no','lawrencium': 'lr',
                             'rutherfordium': 'rf','dubnium': 'db','seaborgium': 'sg','bohrium': 'bh','hassium': 'hs',
                             'meitnerium': 'mt'}
            
            ## RasMol's predefined sets and PyMOL's equivalents
            ## dictionary data structure { RasMol: PyMOL }
            
            predefinedlists = {'acidic': ' resn asp+glu ',
                               'acyclic': ' resn met+ile+val+leu+ala+gly+ser+gln+thr+asn+cys+lys+arg+asp+glu ',
                               'aliphatic': ' resn gly+ala+leu+val+ile ',
                               'alpha': ' name ca ',
                               'amino': ' resn gln+asn+asp+glu+arg+lys+his+thr+cys+tyr+ser+gly+trp+phe+pro+leu+val+ile+met',
                               'aromatic': ' resn his+tyr+tr+phe+pro ',
                               'basic': ' resn arg+lys+his ',
                               'buried': ' resn ala+leu+val+ile+phe+cys+met+trp ',
                               'charged': ' resn asp+glu+arg+lys+his ',
                               'cyclic': ' resn pro+phe+trp+tyr+his ',
                               'cystine': ' (byres (((all) & r. CYS+CYX & n. SG) & bound_to ((all) & r. CYS+CYX & n. SG))) & n. CA+CB+SG',
                               'helix': ' ss h ',
                               'hetero': ' hetatm ',
                               'hydrophobic': ' resn ala+leu+val+ile+met+trp+phe+pro ',
                               'large': ' resn glu+arg+lys+his+gln+tyr+leu+ile+met+trp+phe ',
                               'medium': ' resn val+thr+asp+asn+pro+cys ',
                               'small': ' resn gly+ala+ser ',
                               'neutral': ' resn asn+thr+cys+gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro ',
                               'nucleic': ' resn a+t+c+g ',
                               'polar': ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+ser+gly+tyr ',
                               'protein': ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro ',
                               'purine': ' resn a+g ',
                               'pyrimidine': ' resn c+t ',
                               'selected': 'SelectionSBEVSL',
                               'sheet': ' ss s ',
                               'backbone': ' name o1p+o2p+o3p+p+c1*+c2*+c3*+c4*+c5*+o2*+o3*+o4*+o5*+c+o+n+ca ',
                               'sidechain': ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro+a+t+c+g and not name o1p+o2p+o3p+p+c1*+c2*+c3*+c4*+c5*+o2*+o3*+o4*+o5*+c+o+n+ca ',
                               'surface': ' resn gly+ser+thr+lys+asp+asn+glu+pro+arg+gln+tyr+his ',
                               'turn': ' ss 1 ',
                               'water': ' resn hoh '}
            ## Amino Acids as they appear in both RasMol and PyMOL
            aminolist = ['gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr',
                         'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu',
                         'asn', 'gln']

            try:

                selection = 'false'
                f = '('

                ##if parentheses are used
                if '(' in allparameters:
                    indicies = [i for i in xrange(len(allparameters)) if allparameters.startswith(f, i)]
                    for x in indicies:
                            if allparameters[x-6:x]=='within' or allparameters[x-7:x]=='within ':
                                    indicies.remove(x)
                    if not indicies==[]:
                        selection = selectpar( allparameters + ' ' )
                        x = len( allparameters )
                    else:
                        selection = selectwithin( allparameters )
                        x = len( allparameters )
                                
                ##if an or is used
                elif ' or ' in allparameters:
                    found = allparameters.find( ' or ' )
                    selection = select( allparameters[:found] ) + ' or ' + select( allparameters[found+4:] )

                ##if an and is used
                elif ' and ' in allparameters:
                    found = allparameters.find( ' and ' )
                    selection = select( allparameters[:found] ) + ' and ' + select( allparameters[found+5:] )

                ##The only possibility remaining is a single command.
                else:
                    if allparameters[:4]=='not ':
                        selection = 'not ' + select( allparameters[4:] )
                    elif '.' in allparameters:
                        found = allparameters.find('.')
                        selection = select( allparameters[:found] ) + ' and name ' + select( allparameters[found+1:] )
                    elif ':' in allparameters:
                        found = allparameters.find(':')
                        if len( allparameters[:found] )>0:
                            selection = select( allparameters[:found] ) + ' and chain ' + allparameters[found+1:]
                        else:
                            selection = ' chain ' + allparameters[found+1:]
                    elif allparameters=='all' or allparameters=='*' or allparameters=='':
                        selection = 'all'
                    elif predefinedlists.has_key( allparameters ):
                        selection = predefinedlists[allparameters]
                    elif UserDefinedGroups.has_key( allparameters ):
                        selection = select( UserDefinedGroups[allparameters] )
                    elif periodictable.has_key( allparameters ):
                        selection = 'symbol ' + periodictable[allparameters]
                    elif allparameters in aminolist:
                        selection = 'resn ' + allparameters
                    elif allparameters[:6]=='atomno':
                        lower = 1
                        upper = 999999999
                        if '>' in allparameters:
                            found = allparameters.find('>')
                            if allparameters[found+1:found+2]=='=':
                                lower = int( allparameters[found+2:] )
                            else:
                                lower = int( allparameters[found+1:] ) + 1
                        elif '<' in allparameters:
                            found = allparameters.find('<')
                            if allparameters[found+1:found+2]=='=':
                                upper = int( allparameters[found+2:] )
                            else:
                                upper = int( allparameters[found+1:] ) - 1
                        elif '=' in allparameters:
                            found = allparameters.find('=')
                            upper = int( allparameters[found+1:] )
                            lower = int( allparameters[found+1:] )
                        selection = 'id ' + str( lower ) + '-' + str( upper )
                    else:
                        selection = 'resi ' + allparameters.replace( ',', '+' )
                            
            except:
                selection = 'false'

            return selection 

        ## Select method when parantheses are used.  This method removes each object in the parantheses and performs the select method on them.
        def selectpar( allparameters ):

            selection = ''

            first = 0
            x = allparameters.find('(')
            if x>-1:
                if not ( allparameters[x-6:x]=='within' or allparameters[x-7:x]=='within ' ):
                    first = x
            
            stack = []
            for x in range(first+1, len( allparameters )):
                if allparameters[x:x+1] == '(':
                    stack.append('(')
                if allparameters[x:x+1] == ')':
                    if stack == []:
                        last = x
                        x = len( allparameters )
                    else:
                        stack.pop()

            stack = []
            temp = first
            for x in range( first, last+1 ):
                if allparameters[x:x+1]=='(':
                    stack.append('(')
                    if allparameters[x+1:x+2]==' ':
                        allparameters[x+1:x+2].replace( ' ', '' )
                elif allparameters[x:x+1]==')':
                    if stack==[]:
                        selection = 'false'
                    elif stack==['(']:
                        if len( selection )==0:
                            selection = select( allparameters[:first] ) + select( allparameters[temp+1:x] ) + select( allparameters[last+1:] )
                            if allparameters[x+1:x+2]==' ':
                                temp = x+1
                            else:
                                temp = x
                        else:
                            selection = selection + ' or ' + select( allparameters[:first] ) + select( allparameters[temp+1:x] ) + select( allparameters[last+1:] )
                            if allparameters[x+1:x+2]==' ':
                                temp = x+1
                            else:
                                temp = x
                    else:
                        stack.pop()
                elif allparameters[x:x+1]==',':
                    if stack==['(']:
                        if len( selection )==0:
                            selection = select( allparameters[:first] ) + select( allparameters[temp+1:x] ) + select( allparameters[last+1:] )
                            if allparameters[x+1:x+2]==' ':
                                temp = x+1
                            else:
                                temp = x
                        else:
                            selection = selection + ' or ' + select( allparameters[:first] ) + select( allparameters[temp+1:x] ) + select( allparameters[last+1:] )
                            if allparameters[x+1:x+2]==' ':
                                temp = x+1
                            else:
                                temp = x
                    else:
                        pass
                    if allparameters[x+1:x+2]==' ':
                        allparameters[x+1:x+2].replace( ' ', '' )
                else:
                    pass

            return selection

        ## Handles Select Within options
        def selectwithin( allparameters ):
            
            try:
                selection = 'false'
                found = allparameters.find( 'within' )
                begin = allparameters[found:].find( '(' )

                stack = []
                for x in range( begin + 1, len( allparameters ) ):
                    if allparameters[x:x+1] == '(':
                        stack.append('(')
                    if allparameters[x:x+1] == ')':
                        if stack == []:
                            end = x
                            x = len( allparameters )
                        else:
                            stack.pop()
                            
                comma = allparameters[found:].find( ',' )
                if allparameters[comma+1:comma+2]==' ':
                    selection = select( allparameters[:found] ) + select( allparameters[comma+2:end] ) + ' expand ' + allparameters[begin+1:comma] + select( allparameters[end+1:] )
                else:
                    selection = select( allparameters[:found] ) + select( allparameters[comma+1:end] ) + ' expand ' + allparameters[begin+1:comma] + select( allparameters[end+1:] ) 

            except:
                selection = 'false'

            return selection

        ## Handles RGB Triplet for colors
        def RGBTriplet(triplet):

            try:
                cmd.set_color( triplet, triplet )

            except:
                print "RGB Triplet not valid."

            return triplet

        ## Defines HBonds for a structure
        def HBonds():

            try:
                cmd.h_add('all')
 
                cmd.select( 'don', '(elem n,o and (neighbor elem h) and SelectionSBEVSL)' )
                cmd.select( 'acc', '(elem o or (elem n and not (neighbor elem h))) and SelectionSBEVSL' )
                cmd.distance( 'HBA', '(acc)','(don)', '3.2' )
                cmd.distance( 'HBD', '(don)','(acc)', '3.2' )
                cmd.delete( 'don' )
                cmd.delete( 'acc' )
                cmd.hide( '(elem h)' )
                 
                cmd.hide( 'labels','HBA' )
                cmd.hide( 'labels','HBD' )
            except:
                print 'Error occured with calculating HBonds.'

        ## Defines SSBonds for a structure
        def SSBonds():

            try:
                cmd.h_add('all')
 
                cmd.select( 'SSCys', '(elem S and resn Cys) and SelectionSBEVSL' )
                cmd.distance( 'SSCysteines', '(SSCys)','(SSCys)', '3.0' )
                cmd.delete( 'SSCys' )
                cmd.hide( '(elem h)' )
                 
                cmd.hide( 'labels','SSCysteines' )
            except:
                print 'Error occured with calculating SSBonds.'
        
        ## Handle a command line
        def handlecommand( p ):

                if( p.replace( ' ', '' )=="\n" ):
                    return

                if( p.replace( ' ', '' )[:1]=='#' ):
                    print p
                    return
            
                p = p.rstrip()

                print p

                ##---------------Load---------------##

                firstword = p.split( ' ', 1 )[0].upper()
                loadCmd = 'LOAD'
		
                if loadCmd==firstword:
                    try:
                        loadfile = p[5:]
                        cmd.load( loadfile )
                        cmd.rotate( 'x', 180 )
                        print loadfile + '<--LOADFILE'
                    except:
                        print loadfile + '<--LOADFILE'
                        print 'EXCEPTION THROWN'


                ##---------------Save---------------##

                firstword = p.split( ' ', 1 )[0].upper()
                saveCmd = ['WRITE', 'SAVE']
                
                if firstword in saveCmd:
                    s = ''
                    for i in p.split( ' ', 1 )[1]:
                        s = s + i + ' '
                    cmd.save( s )

                ##---------LOWER-----------##
                p = p.lower()

                #-----------Background color------------#
                
                if p[:10] == 'background':
                    colorx = p.split( ' ', 1 )[1].lower()
                    colorx = colorx.replace( ' ', '' )
                    try:
                        if colorx[:1]=='[':
                            colorx = RGBTriplet( colorx )
                            cmd.color( colorx, 'SelectionSBEVSL' )
                        else:
                            cmd.bg_color(colorx)
                    except:
                        print 'No selection was made for bgcolor, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
                    print p 

                #----------------Select-----------------#
                        
                if p[:6]=='select':
                    selected = select( p[7:].lower() )                            
                    print selected + '<--SELECTED'
                    try:
                        cmd.select( 'SelectionSBEVSL', selected)
                    except:
                        print 'No selection was made for select, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
                   
                #----------------Restrict-----------------#
                        
                if p[:8]=='restrict':
                    selected = select( p[9:].lower() )
                    restricted = 'all and not (' + selected + ')'
                    print restricted + '<--RESTRICTED'
                    try:
                        cmd.select( 'SelectionSBEVSL', selected )
                        cmd.hide( 'everything', restricted )
                    except:
                        print 'No selection was made for restrict, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'

                ##---------------Center---------------##

                if p[:6]=='center' or p[:6]=='centre':
                    centerselected = select( p[7:].lower() )   
                    print centerselection + '<--CENTER'
                    try:
                        cmd.select( 'CenterSelection', centerselection)
                        cmd.center( centerselection )
                    except:
                        print 'No selection was made for center, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
                     
                ##---------------Color---------------##
                            
                if p[:5]=='color' or p[:6]=='colour':
                    colory = p.split( ' ', 1)[1].lower()
                    colory = colory.replace( ' ', '' )
                    try:
                        if colory[:1]=='[':
                            colory = RGBTriplet( colory )
                            cmd.color( colory, 'SelectionSBEVSL' )
                        else:
                            cmd.color(colory, 'SelectionSBEVSL' )
                    except:
                        print 'No selection was made for color, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
                    print 'COLOR ' + colory

                ##------------View Options----------------##

                selectDict = {'wireframe': 'lines', 'cartoon': 'cartoon', 'dots': 'dots', 'cpk': 'spheres', 'spacefill': 'spheres', 'trace': 'ribbon',
                              'ribbon': 'ribbon'}		

                firstword = p.split( ' ', 1 )[0].lower()

                try:

                    if firstword in selectDict: #if the first word on the line is one of the supportable view options
                        q = p + ' '
                        command = q.split( ' ', 1 )[1][:-1].lower()
                        if command=='false' or command=='off':
                            cmd.hide( selectDict[firstword], 'SelectionSBEVSL')
                            print firstword + ' off complete'
                        elif command=='true' or command=='on' or command=='':
                            cmd.show( selectDict[firstword], 'SelectionSBEVSL')
                            print firstword + ' on complete'
                        else:
                            print 'That function is not supported by PyMOL'

                except:
                    print 'No selection was made for view option, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'


                ##---------------Zoom---------------##

                if 'zoom' in p:
                    entry1.delete(0, 100000 )
                    entry1.insert(0, p)
                    entry1.delete(0, 4)
                    try:
##                    zoomnum = 10
##                    print selection + '<--ZOOM SELECTION'
##                    print zoomnum + '<--ZOOMNUM'
##                    cmd.do( 'zoom ' + selection + ', ' + zoomnum )
##                    print 'ZOOM ' + zoomnum
                        zoomnum = 10
                        cmd.zoom( 'SelectionSBEVSL', zoomnum )
                    except:
                        print 'Zoom did not execute properly.  Please revise your zoom command'

                ##---------------Rotate--------------##		
                rotateCmd = 'rotate'
                if rotateCmd==p[:6]:
                    axis = p.split()[1]
                    rotation = p.split()[2]
                    if axis == 'z':
                        rotation = '-' + rotation
                    try:
                        cmd.rotate( axis, rotation )
                    except:
                        print 'The parameters you have given for the rotate command have been entered improperly.  Please rewrite them as rotate (axis) (rotation in degrees)'

                ##---------------HBonds---------------##

                if p[:6]=='hbonds':
                    try:
                        command = p.split( ' ', 1 )[1].lower()
                        print command
                        if command=='false' or command=='off':
                            HBonds()
                            print 'HBonds off complete'
                        elif command=='true' or command=='on' or command=='':
                            print 'Starting HBonds on:'
                            HBonds()
                            print 'HBonds on complete'
                        else:
                            print 'That function is not supported by PyMOL'
                    except:
                        print 'HBonds did not execute properly.  Check spelling and implementation of this HBonds command.'        

                ##---------------SSBonds---------------##

                if p[:6]=='ssbonds':
                    try:
                        command = p.split( ' ', 1 )[1].lower()
                        print command
                        if command=='false' or command=='off':
                            SSBonds()
                            print 'SSBonds off complete'
                        elif command=='true' or command=='on' or command=='':
                            print 'Starting HBonds on:'
                            SSBonds()
                            print 'SSBonds on complete'
                        else:
                            print 'That function is not supported by PyMOL'
                    except:
                        print 'SSBonds did not execute properly.  Check spelling and implementation of this SSBonds command.'

                ##---------------Backbone--------------##

                if p[:8]=='backbone':
                    try:
                        cmd.show( 'ribbon', select('backbone') )
                    except:
                        print 'An error occured while trying to display the backbone.'

                ##---------------Zap---------------##

                if p=='zap':
                    print 'reinitialize'
                    cmd.reinitialize()

                ##---------------Stereo---------------##
                stereoCmd = 'stereo'

                if stereoCmd==p[:6]:
                    tmpstring = p.split()[1]
                    if 'on' in tmpstring:
                        cmd.stereo('on')
                    elif 'off' in tmpstring:
                        cmd.stereo('off')
                    else:
                        print 'That function is not supported by PyMOL.'

                ##---------------Refresh---------------##

                if 'refresh' in p:
                    print 'refresh'
                    cmd.refresh()

                ##---------------Reset---------------##

                if 'reset' in p:
                    print 'reset'
                    cmd.reset()

                ##---------------Echo---------------##

                if p[:4]=='echo':
                    returnval = p[5:]
                    if returnval[:1]=='"':
                        returnval = returnval[1:]
                    if returnval[-1:]=='"':
                        returnval = returnval[:-1]
                    print returnval

                ##---------------Define---------------##

                if p[:6]=='define':
                    defparams = p[7:].split( ' ', 1 )
                    cmd.select( defparams[0], select(defparams[1]) )
                    UserDefinedGroups[ defparams[0] ] =  defparams[1]
                    
                ##-----------Pause/Wait---------------------##

                if p[:5]=='pause':
                    keystroke=False
                    while not keystroke:
                        if event.char==event.keysym:
                            keystroke=True

                ##---------------Quit/Exit---------------##
                firstword = p.upper()

                if firstword in ['QUIT', 'EXIT']:
                    cmd.quit()

                return




        
        ## Handler for processing a script from a file
        def processSBEVSLscript( Q ):

            
            #Open the script 
            f = open(Q, 'rU')
            pmg_tk.startup.ConSCRIPT.filestack.append(f)
            pmg_tk.startup.ConSCRIPT.filelevel = pmg_tk.startup.ConSCRIPT.filelevel+1
            
            #Make a loop
            try:
                for p in f:
                    handlecommand(p)
            finally:
                #Close the file
                f.close()
                pmg_tk.startup.ConSCRIPT.filelevel = pmg_tk.startup.ConSCRIPT.filelevel-1
                return
            
        #Define the Boffo Function
        def Boffo(Event):

            Q = tkFileDialog.askopenfilename(initialdir=('./modules/pmg_tk/startup'))
            pmg_tk.startup.ConSCRIPT.filelevel = 0
            pmg_tk.startup.ConSCRIPT.filestack = []
            processSBEVSLscript(Q)
            #Reset the GUI
            interior.mainloop()


        #Bind button the function
        openbtn.bind('<Button-1>', Boffo)
                    
                    

 
                                
