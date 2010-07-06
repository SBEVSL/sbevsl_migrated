'''ConSCRIPT a Rasmol to Pymol converter
   ConSCRIPT (C) Copyright 2007-2010
   S. Mottarella, P. Craig, H. Bernstein
   GPL, No Warranty
   
/*************************** GPL NOTICES ******************************
 *                                                                    *
 * This program is free software; you can redistribute it and/or      *
 * modify it under the terms of the GNU General Public License as     *
 * published by the Free Software Foundation; either version 2 of     *
 * (the License, or (at your option) any later version.               *
 *                                                                    *
 * This program is distributed in the hope that it will be useful,    *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of     *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the      *
 * GNU General Public License for more details.                       *
 *                                                                    *
 * You should have received a copy of the GNU General Public License  *
 * along with this program; if not, write to the Free Software        *
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA           *
 * 02111-1307  USA                                                    *
 *                                                                    *
 **********************************************************************/'''
from pymol import cmd
from pymol import util
from pymol import stored
import os
import tkFileDialog
from pymol.cgo import *
from pymol.vfont import plain
import platform
PLATFORM = platform.system()
CONSCRIPT_PATH = os.path.dirname(__file__)
try:
    HOME = os.environ['HOME']
except KeyError:
    HOME = os.environ['USERPROFILE']
if PLATFORM == 'Windows':
    OFFSITE = os.path.join(os.environ['AppData'], 'SBEVSL', 'ConSCRIPT')
elif PLATFORM == 'Darwin':
    OFFSITE = os.path.join(HOME, 'Library', 'Application Support', 'SBEVSL',
        'ConSCRIPT')
else:
    OFFSITE = os.path.join(HOME, '.sbevsl', 'ConSCRIPT')
if not os.path.isdir(OFFSITE):
    os.makedirs(OFFSITE)
#DIRS = ()
#for DIR in DIRS:
#    DIR = os.path.join(OFFSITE, DIR)
#    if not os.path.isdir(DIR):
#       os.mkdir(DIR)
class ConSCRIPTConverter:
    '''The ConSCRIPT Converter'''
    def __init__(self):
        '''Set up some stuff'''
        self.assign = 0
        self.vsltok = {}
        self.templist = []
        self.map_name = 0
        self.map_type = 'gaussian'
        self.map_grid = 1.0
        self.map_level = 1.0
        self.map_selection = 0
        self.map_unspecified_selection = True
        self.centerselection = '(all)'
        self.zoomnum = 0
        self.clip_dist_near = -50.0
        self.clip_dist_far = 50.0
        self.userdefinedgroups = {}
        self.vslselection = "(all)"
        self.vslselectionsaved = "(all)"
        self.vslverbose = 0
        self.bondfirstatom = 0
        self.bondsecondatom = 0
        self.hbonds_backbone = False
        self.ssbonds_backbone = False
        self.hydrogen = False
        self.hetero = True
        self.solvent = False
        self.radius = 0.0
        self.set_monitor = True
        self.tokenptr = 0
        self.tokenstart = 0
        self.curtoken = 0
        self.tokenident = ""
        self.tokenvalue = 0
        self.not_coded = ['bulgarian', 'chinese', 'english', 'french', 'pause',
            'italian', 'japanese', 'russian', 'spanish', 'clipboard', 'wait',
            'colourmode', 'connect', 'help', 'molecule', 'notoggle', 'print',
            'renumber', 'show', 'star', 'strands', 'structure']
        
        ### /* Lexeme Tokens */
        self.identtok =       self._assigntok('ident')
        self.numbertok =      self._assigntok('number')
        self.floattok =       self._assigntok('float')
        self.stringtok =      self._assigntok('string')

        ### /* Command Tokens */
        self.advisetok =      self._assigntok('advise')
        self.backbonetok =    self._assigntok('backbone', 'esqueleto',
            'scheletro')
        self.cartoontok =     self._assigntok('cartoon', 'cartoons', 'dibujo',
            'dibujos', 'vignetta')
        self.centretok =      self._assigntok('center', 'centre')
        self.clipboardtok =   self._assigntok('clipboard')
        self.colourtok =      self._assigntok('color', 'colors', 'colour',
            'colours')
        self.colourmodetok =  self._assigntok('colormode', 'colourmode')
        self.connecttok =     self._assigntok('connect')
        self.dashtok =        self._assigntok('dash', 'dashes')
        self.definetok =      self._assigntok('define')
        self.delaytok =       self._assigntok('delay')
        self.depthtok =       self._assigntok('depth')
        self.displaytok =     self._assigntok('display', 'mostrar',
            'visualizza')
        self.echotok =        self._assigntok('echo')
        self.exittok =        self._assigntok('exit', 'salir')
        self.generatetok =    self._assigntok('generate')
        self.helptok =        self._assigntok('help')
        self.labeltok =       self._assigntok('label', 'labels', 'etiqueta',
            'etiquetas', 'etichetta', 'etichette')
        self.loadtok =        self._assigntok('load')
        self.looptok =        self._assigntok('loop')
        self.maptok =         self._assigntok('map')
        self.masktok =        self._assigntok('mask')
        self.moleculetok =    self._assigntok('molecule')
        self.molsurftok =     self._assigntok('molsurf')
        self.monitortok =     self._assigntok('monitor', 'monitors')
        self.movetok =        self._assigntok('move')
        self.notoggletok =    self._assigntok('notoggle')
        self.pausetok =       self._assigntok('pause', 'wait')
        self.printtok =       self._assigntok('print')
        self.quittok =        self._assigntok('quit')
        self.refreshtok =     self._assigntok('refresh')
        self.renumtok =       self._assigntok('renum', 'renumber')
        self.resettok =       self._assigntok('reset')
        self.resizetok =      self._assigntok('resize')
        self.restoretok =     self._assigntok('restore')
        self.restricttok =    self._assigntok('restrict')
        self.rotatetok =      self._assigntok('rotate', 'rot', 'rotation')
        self.savetok =        self._assigntok('save')
        self.scripttok =      self._assigntok('script')
        self.selecttok =      self._assigntok('select')
        self.settok =         self._assigntok('set')
        self.showtok =        self._assigntok('show')
        self.slabtok =        self._assigntok('slab')
        self.sourcetok =      self._assigntok('source')
        self.spacefilltok =   self._assigntok('spacefill', 'riempimento')
        self.startok =        self._assigntok('star', 'stars')
        self.structuretok =   self._assigntok('structure')
        self.surfacetok =     self._assigntok('surface')
        self.symmetrytok =    self._assigntok('symmetry')
        self.titletok =       self._assigntok('title')
        self.tracetok =       self._assigntok('trace')
        self.translatetok =   self._assigntok('translate', 'translation')
        self.viewtok =        self._assigntok('view')
        self.wireframetok =   self._assigntok('wireframe', 'filodiferro',
            'fildiferro', 'mesh')
        self.writetok =       self._assigntok('write')
        self.zaptok =         self._assigntok('zap')
        self.zoomtok =        self._assigntok('zoom')

        ### /* Predicate Tokens */
        self.alphatok =       self._assigntok('alpha')
        self.aminotok =       self._assigntok('amino')
        self.attok =          self._assigntok('at')
        self.bondedtok =      self._assigntok('bonded')
        self.cgtok =          self._assigntok('cg')
        self.cystinetok =     self._assigntok('cystine')
        self.dnatok =         self._assigntok('dna')
        self.helixtok =       self._assigntok('helix', 'helices', 'eliche')
        self.heterotok =      self._assigntok('hetero')
        self.hydrogentok =    self._assigntok('hydrogen')
        self.iontok =         self._assigntok('ion', 'ions')
        self.ligandtok =      self._assigntok('ligand', 'ligands')
        self.mainchaintok =   self._assigntok('mainchain')
        self.nucleictok =     self._assigntok('nucleic')
        self.proteintok =     self._assigntok('protein')
        self.purinetok =      self._assigntok('purine', 'purines')
        self.pyrimidinetok =  self._assigntok('pyrimidine', 'pyrimibines')
        self.rnatok =         self._assigntok('rna')
        self.selectedtok =    self._assigntok('selected', 'selection')
        self.sheettok =       self._assigntok('sheet', 'sheets')
        self.sidechaintok =   self._assigntok('sidechain')
        self.solventtok =     self._assigntok('solvent', 'solvents')
        self.turntok =        self._assigntok('turn', 'turns', 'giro', 'giros')
        self.watertok =       self._assigntok('water', 'waters')
        self.acidictok =      self._assigntok('acidic', 'negative')
        self.acyclictok =     self._assigntok('acyclic')
        self.aliphatictok =   self._assigntok('aliphatic')
        self.aromatictok =    self._assigntok('aromatic')
        self.basictok =       self._assigntok('basic', 'positive')
        self.buriedtok =      self._assigntok('buried')
        self.chargedtok =     self._assigntok('charged')
        self.cisbondedtok =   self._assigntok('cisbonded')
        self.cyclictok =      self._assigntok('cyclic')
        self.hydrophobictok = self._assigntok('hydrophobic')
        self.largetok =       self._assigntok('large')
        self.mediumtok =      self._assigntok('medium')
        self.neutraltok =     self._assigntok('neutral')
        self.polartok =       self._assigntok('polar')
        self.smalltok =       self._assigntok('small')

        ### /* Property Tokens */
        self.temperaturetok = self._assigntok('temperature')
        self.radiustok =      self._assigntok('radius')
        self.atomnotok =      self._assigntok('atomno', 'atomnumber')
        self.elemnotok =      self._assigntok('elemno')
        self.modeltok =       self._assigntok('model')
        self.resnotok =       self._assigntok('resno', 'residuenumber')
        self.altltok =        self._assigntok('alt')

        ### /* File Format Tokens */
        ### /* Warning! Tokens are related to Format values */
        self.pdbtok =         self._assigntok('pdb')
        self.ramprinttok =    self._assigntok('ramprint', 'rpp', 'macromodel',
            'ramachandranprinterplot')
        self.gaussiantok =    self._assigntok('gaussian')
        self.alchemytok =     self._assigntok('alchemy')
        self.nmrpdbtok =      self._assigntok('nmrpdb')
        self.charmmtok =      self._assigntok('charmm')
        self.biosymtok =      self._assigntok('biosym')
        self.mopactok =       self._assigntok('mopac')
        self.shelxtok =       self._assigntok('shelx')
        self.mol2tok =        self._assigntok('mol2')
        self.fdattok =        self._assigntok('fdat')
        self.mmdbtok =        self._assigntok('mmdb')
        self.mdltok =         self._assigntok('mdl')
        self.xyztok =         self._assigntok('xyz')
        self.ciftok =         self._assigntok('cif')
        self.cextok =         self._assigntok('cex')

        ### /* Raster Tokens */
        self.giftok =         self._assigntok('gif')
        self.ppmtok =         self._assigntok('ppm')
        self.suntok =         self._assigntok('sun')
        self.sunrletok =      self._assigntok('sunrle')
        self.epsftok =        self._assigntok('epsf', 'ps')
        self.picttok =        self._assigntok('pict')
        self.iristok =        self._assigntok('iris', 'rgb')
        self.bmptok =         self._assigntok('bmp')
        self.monopstok =      self._assigntok('monops')
        self.jpegtok =        self._assigntok('jpeg')
        self.pngtok =         self._assigntok('png')
        self.vectpstok =      self._assigntok('vectps')
        self.kinemagetok =    self._assigntok('kinemage')
        self.molscripttok =   self._assigntok('molscript')
        self.povraytok =      self._assigntok('povray')
        self.povray2tok =     self._assigntok('povray2')
        self.povray3tok =     self._assigntok('povray3')
        self.vrmltok =        self._assigntok('vrml')
        self.raster3dtok =    self._assigntok('raster3d', 'r3d')
        self.ramachantok =    self._assigntok('ramachan', 'ramdata', 'rdf',
            'ramachandrandatafile')
        self.mirrortok =      self._assigntok('mirror')

        ### /* Feature Tokens */
        self.atomtok =        self._assigntok('atom', 'atoms')
        self.bondtok =        self._assigntok('bond', 'bonds', 'elance',
            'elances')
        self.dotstok =        self._assigntok('dots')
        self.hbondtok =       self._assigntok('hbond', 'hbonds')
        self.ribbontok =      self._assigntok('ribbon', 'nastro', 'nastri',
            'ribbons')
        self.ssbondtok =      self._assigntok('ssbond', 'ssbonds')
        self.ribbon1tok =     self._assigntok('ribbon1', 'ribbons1')
        self.ribbon2tok =     self._assigntok('ribbon2', 'ribbons2')
        self.unbondtok =      self._assigntok('unbond')

        ### /* Expression Tokens */
        self.truetok =        self._assigntok('true', 'on')
        self.falsetok =       self._assigntok('false', 'off')
        self.alltok =         self._assigntok('all', 'todo', 'tutto')
        self.nonetok =        self._assigntok('none')
        self.andtok =         self._assigntok('and', 'e')
        self.ortok =          self._assigntok('or')
        self.nottok =         self._assigntok('not')
        self.withintok =      self._assigntok('within')
        self.xortok =         self._assigntok('xor')
        self.meantok =        self._assigntok('average', 'mean')
        self.nexttok =        self._assigntok('next')
        self.newtok =         self._assigntok('new')

        ### /* Colour Tokens */
        ### /* Warning! Tokens are related to colour values */
        self.blacktok =       self._assigntok('black')
        self.bluetok =        self._assigntok('blue')
        self.bluetinttok =    self._assigntok('bluetint')
        self.browntok =       self._assigntok('brown')
        self.cyantok =        self._assigntok('cyan')
        self.goldtok =        self._assigntok('gold')
        self.graytok =        self._assigntok('gray', 'grey')
        self.greentok =       self._assigntok('green')
        self.greenbluetok =   self._assigntok('greenblue')
        self.greentinttok =   self._assigntok('greentint')
        self.hotpinktok =     self._assigntok('hotpink')
        self.magentatok =     self._assigntok('magenta')
        self.orangetok =      self._assigntok('orange')
        self.pinktok =        self._assigntok('pink')
        self.pinktinttok =    self._assigntok('pinktint')
        self.purpletok =      self._assigntok('purple')
        self.redtok =         self._assigntok('red')
        self.redorangetok =   self._assigntok('redorange')
        self.seagreentok =    self._assigntok('seagreen')
        self.skybluetok =     self._assigntok('skyblue')
        self.violettok =      self._assigntok('violet')
        self.whitetok =       self._assigntok('white')
        self.yellowtok =      self._assigntok('yellow')
        self.yellowtinttok =  self._assigntok('yellowtint')
        self.cpktok =         self._assigntok('cpk')
        self.shapelytok =     self._assigntok('shapely')
        self.residuetok =     self._assigntok('residue')
        self.usertok =        self._assigntok('user')
        self.grouptok =       self._assigntok('group', 'grupo', 'gruppo')
        self.chaintok =       self._assigntok('chain', 'chains', 'cadena',
            'cadenas', 'catena', 'catene')
        self.typetok =        self._assigntok('type')
        self.potentialtok =   self._assigntok('potential')
        self.chargetok =      self._assigntok('charge', 'charges')
        self.eastertok =      self._assigntok('easter')
        self.cpknewtok =      self._assigntok('cpknew')

        ### /* Variable Tokens */
        self.ambienttok =     self._assigntok('ambient')
        self.axestok =        self._assigntok('axes', 'asse', 'assi', 'axis',
            'eje', 'ejes')
        self.backfadetok =    self._assigntok('backfade')
        self.backgroundtok =  self._assigntok('background')
        self.bondmodetok =    self._assigntok('bondmode')
        self.boundboxtok =    self._assigntok('boundbox', 'boundingbox')
        self.cisangletok =    self._assigntok('cisangle')
        self.contourtok =     self._assigntok('contour', 'level')
        self.depthcuetok =    self._assigntok('depthcue')
        self.fontsizetok =    self._assigntok('fontsize')
        self.fontstroketok =  self._assigntok('fontstroke')
        self.hourglasstok =   self._assigntok('hourglass')
        self.menustok =       self._assigntok('menus')
        self.mousetok =       self._assigntok('mouse', 'mousemode')
        self.pickingtok =     self._assigntok('pick', 'picking')
        self.resolutiontok =  self._assigntok('resolution')
        self.shadepowertok =  self._assigntok('shadepower')
        self.shadowtok =      self._assigntok('shadow', 'shadows')
        self.slabmodetok =    self._assigntok('slabmode')
        self.spacingtok =     self._assigntok('spacing')
        self.speculartok =    self._assigntok('specular')
        self.specpowertok =   self._assigntok('specpower')
        self.spreadtok =      self._assigntok('spread', 'width')
        self.strandstok =     self._assigntok('strands', 'fili', 'hebras')
        self.transparenttok = self._assigntok('transparent')
        self.unitcelltok =    self._assigntok('unitcell')

        ### /* SlabMode Tokens */
        self.rejecttok =      self._assigntok('reject')
        self.halftok =        self._assigntok('half')
        self.hollowtok =      self._assigntok('hollow')
        self.solidtok =       self._assigntok('solid')
        self.sectiontok =     self._assigntok('section')

        ### /* MouseMode Tokens */
        self.rasmoltok =      self._assigntok('rasmol', 'rasmac', 'raswin')
        self.insighttok =     self._assigntok('insight')
        self.quantatok =      self._assigntok('quanta')
        self.sybyltok =       self._assigntok('sybyl')

        ### /* Information Tokens */
        self.infotok =        self._assigntok('info', 'information')
        self.sequencetok =    self._assigntok('sequence')
        self.versiontok =     self._assigntok('version')
        self.phipsitok =      self._assigntok('phipsi')

        ### /* Display Mode Tokens */
        self.normaltok =      self._assigntok('normal')
        self.stereotok =      self._assigntok('stereo')
        self.monotok =        self._assigntok('mono', 'monochrome')
        self.hardwaretok =    self._assigntok('hardware')

        ### /* Axis Tokens */
        self.xtok =           self._assigntok('x')
        self.ytok =           self._assigntok('y')
        self.ztok =           self._assigntok('z')

        ### /* Picking Tokens */
        self.identifytok =    self._assigntok('identify')
        self.coordtok =       self._assigntok('coord', 'coords', 'coordinate',
            'coordinates')
        self.distancetok =    self._assigntok('distance', 'distances')
        self.angletok =       self._assigntok('angle', 'angles')
        self.torsiontok =     self._assigntok('torsion', 'torsions')
        self.origintok =      self._assigntok('origin')

        ### /* Misc Tokens */
        self.inlinetok =      self._assigntok('inline')
        self.vdwtok =         self._assigntok('vdw')
        self.headertok =      self._assigntok('header')
        self.cifdatatok =     self._assigntok('data_')
        self.fstok =          self._assigntok('fs')

        ### /* Clipboard Tokens */
        self.imagetok =       self._assigntok('image')
        self.positiontok =    self._assigntok('position')
        self.copytok =        self._assigntok('copy')
        self.pastetok =       self._assigntok('paste')

        ### /* Language Tokens */
        self.englishtok =     self._assigntok('english')
        self.frenchtok =      self._assigntok('french')
        self.germantok =      self._assigntok('german')
        self.italiantok =     self._assigntok('italian')
        self.spanishtok =     self._assigntok('spanish')
        self.russiantok =     self._assigntok('russian')
        self.chinesetok =     self._assigntok('chinese')
        self.japanesetok =    self._assigntok('japanese')
        self.bulgariantok =   self._assigntok('bulgarian')

        self.errsyntax   =    0
        self.errbignum   =    1
        self.errbadopt   =    2
        self.errparam    =    3
        self.errfilnam   =    4
        self.errbadload  =    5
        self.errnotnum   =    6
        self.errnotsep   =    7
        self.errnotbrac  =    8
        self.errnocol    =    9
        self.errcolour   =   10
        self.errbadarg   =   11
        self.errbadexpr  =   12
        self.errparen    =   13
        self.errscript   =   14
        self.errfunc     =   15
        self.errsetname  =   16
        self.errbadset   =   17
        self.errinscrpt  =   18
        self.erroutscrpt =   19
        self.errbadmoldb =   20
        self.errnobond   =   21
        self.errnosuppt  =   22

        self.msgstrs = {}
        self.msgstrs[self.errsyntax]  = "Invalid command syntax!"
        self.msgstrs[self.errbignum]  = "Parameter value too large!"
        self.msgstrs[self.errbadopt]  = "Invalid parameter setting!"
        self.msgstrs[self.errparam]  = "Invalid parameter name!"
        self.msgstrs[self.errfilnam]  = "Filename string expected!"
        self.msgstrs[self.errbadload]  = "Molecule database loaded!"
        self.msgstrs[self.errnotnum]  = "Integer value expected!"
        self.msgstrs[self.errnotsep]  = "Comma separator missing!"
        self.msgstrs[self.errnotbrac]  = "Close bracket ']' expected!"
        self.msgstrs[self.errnocol]  = "No colour specified!"
        self.msgstrs[self.errcolour]  = "Unknown or incorrect colour!"
        self.msgstrs[self.errbadarg]  = "Invalid command argument!"
        self.msgstrs[self.errbadexpr]  = "Syntax error in expression!"
        self.msgstrs[self.errparen]  = "Close parenthesis ')' expected!"
        self.msgstrs[self.errscript]  = "Script command stack too deep!"
        self.msgstrs[self.errfunc]  = "Open parenthesis '(' expected!"
        self.msgstrs[self.errsetname]  = "Invalid or missing atom set name!"
        self.msgstrs[self.errbadset]  = "Not enough memory to define set!"
        self.msgstrs[self.errinscrpt]  = "Command disabled in script file!"
        self.msgstrs[self.erroutscrpt]  = "Command only within a script!"
        self.msgstrs[self.errbadmoldb]  = "Molecule database not loaded!"
        self.msgstrs[self.errnobond]  = "Bond for rotation not picked!"
        self.msgstrs[self.errnosuppt] = "That command is not supported!"

        self.vslcolourtable = {}
        self.vslcolourtable[self.blacktok] =      [  0/255.,   0/255.,   0/255.]
        self.vslcolourtable[self.bluetok] =       [  0/255.,   0/255., 255/255.]
        self.vslcolourtable[self.bluetinttok] =   [175/255., 214/255., 255/255.]
        self.vslcolourtable[self.browntok] =      [175/255., 117/255.,  89/255.]
        self.vslcolourtable[self.cyantok] =       [  0/255., 255/255., 255/255.]
        self.vslcolourtable[self.goldtok] =       [255/255., 156/255.,   0/255.]
        self.vslcolourtable[self.graytok] =       [125/255., 125/255., 125/255.]
        self.vslcolourtable[self.greentok] =      [  0/255., 255/255.,   0/255.]
        self.vslcolourtable[self.greenbluetok] =  [ 46/255., 139/255.,  87/255.]
        self.vslcolourtable[self.greentinttok] =  [152/255., 255/255., 179/255.]
        self.vslcolourtable[self.hotpinktok] =    [255/255.,   0/255., 101/255.]
        self.vslcolourtable[self.magentatok] =    [255/255.,   0/255., 255/255.]
        self.vslcolourtable[self.orangetok] =     [255/255., 165/255.,   0/255.]
        self.vslcolourtable[self.pinktok] =       [255/255., 101/255., 117/255.]
        self.vslcolourtable[self.pinktinttok] =   [255/255., 171/255., 187/255.]
        self.vslcolourtable[self.purpletok] =     [160/255.,  32/255., 240/255.]
        self.vslcolourtable[self.redtok] =        [255/255.,   0/255.,   0/255.]
        self.vslcolourtable[self.redorangetok] =  [255/255.,  69/255.,   0/255.]
        self.vslcolourtable[self.seagreentok] =   [  0/255., 250/255., 109/255.]
        self.vslcolourtable[self.skybluetok] =    [ 58/255., 144/255., 255/255.]
        self.vslcolourtable[self.violettok] =     [238/255., 130/255., 238/255.]
        self.vslcolourtable[self.whitetok] =      [255/255., 255/255., 255/255.]
        self.vslcolourtable[self.yellowtok] =     [255/255., 255/255.,   0/255.]
        self.vslcolourtable[self.yellowtinttok] = [246/255., 246/255., 117/255.]

        #the original CPK plastic models developed by Corey, Pauling and Kultun
        self.cpkdict = {}
        self.cpkdict['Ni'] =  '[0.647, 0.165, 0.165]'
        self.cpkdict['S'] =   '[1.000, 1.000, 0.000]'
        self.cpkdict['Na'] =  '[0.000, 0.000, 1.000]'
        self.cpkdict['Mg'] =  '[0.133, 0.139, 0.133]'
        self.cpkdict['Li'] =  '[0.698, 0.133, 0.133]'
        self.cpkdict['Ti'] =  '[0.502, 0.502, 0.565]'
        self.cpkdict['Ba'] =  '[1.000, 0.647, 0.000]'
        self.cpkdict['Fe'] =  '[1.000, 0.647, 0.000]'
        self.cpkdict['Br'] =  '[0.647, 0.165, 0.165]'
        self.cpkdict['He'] =  '[1.000, 0.753, 0.796]'
        self.cpkdict['C'] =   '[0.784, 0.784, 0.784]'
        self.cpkdict['B'] =   '[0.000, 1.000, 0.000]'
        self.cpkdict['F'] =   '[0.855, 0.647, 0.125]'
        self.cpkdict['I'] =   '[0.627, 0.125, 0.941]'
        self.cpkdict['H'] =   '[1.000, 1.000, 1.000]'
        self.cpkdict['Mn'] =  '[0.502, 0.502, 0.565]'
        self.cpkdict['O'] =   '[1.000, 0.000, 0.000]'
        self.cpkdict['N'] =   '[0.561, 0.561, 1.000]'
        self.cpkdict['P'] =   '[1.000, 0.647, 0.000]'
        self.cpkdict['Si'] =  '[0.855, 0.647, 0.125]'
        self.cpkdict['UNK'] = '[1.000, 0.078, 0.576]'
        self.cpkdict['Zn'] =  '[0.647, 0.165, 0.165]'
        self.cpkdict['Ag'] =  '[0.502, 0.502, 0.565]'
        self.cpkdict['Cl'] =  '[0.000, 1.000, 0.000]'
        self.cpkdict['Ca'] =  '[0.502, 0.502, 0.565]'
        self.cpkdict['Al'] =  '[0.502, 0.502, 0.565]'
        self.cpkdict['Au'] =  '[0.855, 0.647, 0.125]'
        self.cpkdict['Cr'] =  '[0.502, 0.502, 0.565]'
        self.cpkdict['Cu'] =  '[0.647, 0.165, 0.165]'
        #CPKNew Based off the original CPK plastic models
        self.cpknewdict = {}
        self.cpknewdict['Ni'] =  '[0.502, 0.157, 0.157]'
        self.cpknewdict['S'] =   '[1.000, 1.000, 0.000]'
        self.cpknewdict['Na'] =  '[0.000, 0.000, 1.000]'
        self.cpknewdict['Mg'] =  '[0.133, 0.139, 0.133]'
        self.cpknewdict['Li'] =  '[0.698, 0.129, 0.129]'
        self.cpknewdict['Ti'] =  '[0.412, 0.412, 0.412]'
        self.cpknewdict['Ba'] =  '[1.000, 0.667, 0.000]'
        self.cpknewdict['Fe'] =  '[1.000, 0.667, 0.000]'
        self.cpknewdict['Br'] =  '[0.502, 0.157, 0.157]'
        self.cpknewdict['He'] =  '[1.000, 0.753, 0.796]'
        self.cpknewdict['C'] =   '[0.827, 0.827, 0.827]'
        self.cpknewdict['B'] =   '[0.000, 1.000, 0.000]'
        self.cpknewdict['F'] =   '[0.855, 0.647, 0.125]'
        self.cpknewdict['I'] =   '[0.627, 0.125, 0.941]'
        self.cpknewdict['H'] =   '[1.000, 1.000, 1.000]'
        self.cpknewdict['Mn'] =  '[0.412, 0.412, 0.412]'
        self.cpknewdict['O'] =   '[1.000, 0.000, 0.000]'
        self.cpknewdict['N'] =   '[0.529, 0.808, 0.922]'
        self.cpknewdict['P'] =   '[1.000, 0.667, 0.000]'
        self.cpknewdict['Si'] =  '[0.855, 0.647, 0.125]'
        self.cpknewdict['UNK'] = '[1.000, 0.086, 0.569]'
        self.cpknewdict['Zn'] =  '[0.502, 0.157, 0.157]'
        self.cpknewdict['Ag'] =  '[0.412, 0.412, 0.412]'
        self.cpknewdict['Cl'] =  '[0.000, 1.000, 0.000]'
        self.cpknewdict['Ca'] =  '[0.412, 0.412, 0.412]'
        self.cpknewdict['Al'] =  '[0.412, 0.412, 0.412]'
        self.cpknewdict['Au'] =  '[0.855, 0.647, 0.125]'
        self.cpknewdict['Cr'] =  '[0.412, 0.412, 0.412]'
        self.cpknewdict['Cu'] =  '[0.502, 0.157, 0.157]'
        #Shapely colors based off of Bob Fletterick's "Shapely Models"
        self.shapelydict = {}
        self.shapelydict['ILE'] =      '[0.000, 0.298, 0.000]'
        self.shapelydict['GLN'] =      '[1.000, 0.298, 0.298]'
        self.shapelydict['GLX'] =      '[1.000, 0.000, 1.000]'
        self.shapelydict['GLY'] =      '[1.000, 1.000, 1.000]'
        self.shapelydict['PCA'] =      '[1.000, 0.000, 1.000]'
        self.shapelydict['GLU'] =      '[0.400, 0.000, 0.000]'
        self.shapelydict['CYS'] =      '[1.000, 1.000, 0.439]'
        self.shapelydict['ASP'] =      '[0.627, 0.000, 0.259]'
        self.shapelydict['SER'] =      '[1.000, 0.439, 0.259]'
        self.shapelydict['LYS'] =      '[0.278, 0.278, 0.722]'
        self.shapelydict['PRO'] =      '[0.322, 0.322, 0.322]'
        self.shapelydict['ASX'] =      '[1.000, 0.000, 1.000]'
        self.shapelydict['ASN'] =      '[1.000, 0.486, 0.439]'
        self.shapelydict['A'] =        '[0.627, 0.627, 1.000]'
        self.shapelydict['C'] =        '[1.000, 0.549, 0.294]'
        self.shapelydict['Special'] =  '[0.369, 0.000, 0.369]'
        self.shapelydict['VAL'] =      '[1.000, 0.549, 1.000]'
        self.shapelydict['Backbone'] = '[0.722, 0.722, 0.722]'
        self.shapelydict['THR'] =      '[0.722, 0.298, 0.000]'
        self.shapelydict['HIS'] =      '[0.439, 0.439, 1.000]'
        self.shapelydict['T'] =        '[0.627, 1.000, 0.627]'
        self.shapelydict['TRP'] =      '[0.310, 0.275, 0.000]'
        self.shapelydict['UNK'] =      '[1.000, 0.000, 1.000]'
        self.shapelydict['HYP'] =      '[1.000, 0.000, 1.000]'
        self.shapelydict['G'] =        '[1.000, 0.439, 0.439]'
        self.shapelydict['PHE'] =      '[0.325, 0.298, 0.259]'
        self.shapelydict['ALA'] =      '[0.549, 1.000, 0.549]'
        self.shapelydict['MET'] =      '[0.722, 0.627, 0.259]'
        self.shapelydict['LEU'] =      '[0.271, 0.369, 0.271]'
        self.shapelydict['ARG'] =      '[0.000, 0.000, 0.486]'
        self.shapelydict['TYR'] =      '[0.549, 0.439, 0.298]'
        #amino colors according to traditional amino acid properties
        self.aminodict = {}
        self.aminodict['CYS'] = '[0.902, 0.902, 0.000]'
        self.aminodict['UNK'] = '[0.745, 0.627, 0.431]'
        self.aminodict['ASP'] = '[0.902, 0.902, 0.039]'
        self.aminodict['SER'] = '[0.980, 0.588, 0.000]'
        self.aminodict['GLN'] = '[0.000, 0.863, 0.863]'
        self.aminodict['LYS'] = '[0.078, 0.353, 1.000]'
        self.aminodict['PRO'] = '[0.863, 0.588, 0.510]'
        self.aminodict['GLY'] = '[0.922, 0.922, 0.922]'
        self.aminodict['THR'] = '[0.980, 0.588, 0.000]'
        self.aminodict['PHE'] = '[0.196, 0.196, 0.667]'
        self.aminodict['ASN'] = '[0.000, 0.863, 0.863]'
        self.aminodict['HIS'] = '[0.510, 0.510, 0.824]'
        self.aminodict['MET'] = '[0.902, 0.902, 0.000]'
        self.aminodict['ILE'] = '[0.059, 0.510, 0.059]'
        self.aminodict['LEU'] = '[0.059, 0.510, 0.059]'
        self.aminodict['ARG'] = '[0.078, 0.353, 1.000]'
        self.aminodict['TRP'] = '[0.706, 0.353, 0.706]'
        self.aminodict['ALA'] = '[0.784, 0.784, 0.784]'
        self.aminodict['VAL'] = '[0.059, 0.510, 0.059]'
        self.aminodict['GLU'] = '[0.902, 0.902, 0.039]'
        self.aminodict['TYR'] = '[0.196, 0.196, 0.667]'
        
    def gettok(self, tok):
        '''returns token number of a specified command'''
        return self.vsltok[tok.lower()]
    
    def _assigntok(self, *args):
        '''assigns tokens incrementally and assigns args to a dictionary'''
        self.assign += 1
        for arg in args:
            self.vsltok[arg.lower()] = self.assign
        return self.assign

    ##---Apply Color to Selection--##
    def _ispredtok(self, abc):
        '''************************'''
        if (((abc)>=self.alphatok) and ((abc)<=self.smalltok)):
            return True
        else:
            return False

    def _predtokord(self, abc):
        '''************************'''
        if  ((abc)-self.alphatok):
            return True
        else:
            return False

    def _predtokchr(self, abc):
        '''************************'''
        if ((abc)+self.alphatok):
            return True
        else:
            return False

    def _isproptok(self, abc):
        '''************************'''
        if  (((abc)>=self.temperaturetok) and ((abc)<=self.altltok)):
            return True
        else:
            return False

    def _iscolourtoken(self, abc):
        '''************************'''
        if (((abc)>=self.blacktok) and ((abc)<=self.yellowtinttok)):
            return True
        else:
            return False

    def _token2colour(self, abc):
        '''************************'''
        return  ((abc)-self.blacktok)

    def _isimagetoken(self, abc):
        '''************************'''
        if (((((abc)>=self.giftok) and ((abc)<=self.ramprinttok)) or
            ((abc) == self.phipsitok))):
            return True
        else:
            return False

    def _ismoleculetoken(self, abc):
        '''************************'''
        if (((abc)>=self.pdbtok) and ((abc)<=self.cextok)):
            return True
        else:
            return False

    def _lookupkeyword(self, keyw):
        '''************************'''
        if keyw.lower() in self.vsltok:
            return self.vsltok[ keyw.lower() ]
        else:
            return self.identtok

    def _isidentchar(self, abc):
        '''************************'''
        if abc.isalnum() or abc == '$' or abc== '_':
            return True
        else:
            return False

    def _vslfetchtoken(self, commands):
        '''************************'''
        def debug():
            '''************************'''
            print 'curtoken, tokenptr, tokenstart %s %s %s' % (self.curtoken,
                self.tokenptr, self.tokenstart)
        self.tokenstart = self.tokenptr
        self.curtoken = 0
        self.tokenident = ""
        self.tokenvalue = 0
        if self.tokenptr >= len(commands):
            #**debug()
            self.curtoken = 0
            return False
        while self.tokenptr < len(commands):
            chm =  commands[self.tokenptr:self.tokenptr+1]
            if not chm.isspace():
                break
            self.tokenptr += 1
        self.tokenstart = self.tokenptr
        #**debug()
        if self.tokenptr < len(commands):
            chm = commands[self.tokenptr]
            #**print 'Starting scan with chm ='+chm
            if chm == '#':
                #**debug()
                self.curtoken = 0
                return False
            self.tokenptr += 1
            if chm.isalpha():
                #**print ' First character is alpha'
                tokenlength = 1
                tokenidentl = []
                tokenidentl.append(chm.upper())
                while self.tokenptr < len(commands) and tokenlength < 32 and\
                    self._isidentchar(commands[self.tokenptr]) == True:
                    chm = commands[self.tokenptr]
                    self.tokenptr += 1
                    tokenidentl.append(chm.upper())
                    tokenlength += 1
                if tokenlength != 32:
                    self.tokenident = ''.join(tokenidentl)
                    self.curtoken = self._lookupkeyword(self.tokenident)
                    #**debug()
                else:
                    #**debug()
                    pass
            elif chm.isdigit():
                #**print ' First character is digit '
                self.tokenvalue = int(chm)
                while self.tokenptr < len(commands):
                    chm = commands[self.tokenptr]
                    if chm == '#' or not chm.isdigit():
                        break
                    self.tokenptr += 1
                    self.tokenvalue = 10*self.tokenvalue + int(chm)
                self.curtoken = self.numbertok
                #**debug()
            elif (chm == '\'') or (chm == '\"') or (chm == '`'):
                #**print ' First character is quot '
                tokenlength = 0
                tokenidentl = []
                tokenidentl.append(chm)
                while self.tokenptr < len(commands) and tokenlength < 128 and\
                    (commands[self.tokenptr]!=chm):
                    tokenidentl.append(commands[self.tokenptr])
                    self.tokenptr += 1
                if chm == commands[self.tokenptr]:
                    self.tokenptr += 1
                    self.tokenident = ''.join(tokenidentl)
                    self.curtoken = self.stringtok
                    #**debug()
                else:
                    #**debug()
                    pass
            else:
                self.curtoken = -ord(chm)
                #**debug()
        else:
            #**debug()
            self.curtoken = 0
            return False

    def _vslparsecolour(self, commands, tok=False):
        '''************************'''
        #**print 'parsecolour tokenptr, curtoken, p %s %s %s' % (self.tokenptr,
            #**self.curtoken, commands)
        if self._iscolourtoken(self.curtoken) == True:
            rgb = self.vslcolourtable[self.curtoken]
            #**print ' rgb '+str(rgb)
        elif self.curtoken == -ord('['):
            rgb = []
            for i in range(5):
                self._vslfetchtoken(commands)
                if i % 2 == 0:
                    if self.curtoken != self.numbertok:
                        print self.msgstrs[self.errnotnum]
                        break
                    elif self.tokenvalue > 255:
                        print self.msgstrs[self.errbignum]
                        break
                    rgb.append(self.tokenvalue/255.)
                elif self.curtoken != -ord(','):
                    print self.msgstrs[self.errnotsep]
                    break
            else:
                self._vslfetchtoken(commands)
                if self.curtoken != -ord(']'):
                    print self.msgstrs[self.errnotbrac]
        elif tok == self.atomtok:
            if self.curtoken == self.altltok:
                stored.alternate = []
                set_colors = []
                conformers = {}
                cmd.iterate(self.vslselectionsaved,
                    'stored.alternate.append((resi, alt))')
                altlcolors = [self.cyantok, self.greentok, self.magentatok, 
                    self.orangetok, self.redtok, self.violettok, self.purpletok,
                    self.yellowtok]
                cmd.set_color('NoConformer', self.vslcolourtable[self.bluetok])
                cmd.color('NoConformer', self.vslselectionsaved)
                for alt in stored.alternate:
                    if alt[0] not in conformers:
                        conformers[alt[0]] = []
                    if alt[1] != '' and alt[1] not in conformers[alt[0]]:
                        conformers[alt[0]].append(alt[1])
                for alternate in conformers:
                    if conformers[alternate] == []:
                        continue
                    colrsi = 0
                    for alt in conformers[alternate]:
                        if alt == '':
                            continue
                        color_to_set = 'Con%s' % alt
                        if color_to_set not in set_colors:
                            cmd.set_color(color_to_set,
                                self.vslcolourtable[altlcolors[colrsi]])
                            set_colors.append(color_to_set)
                        cmd.color(color_to_set, '%s and alt %s' % (
                            self.vslselectionsaved, alt))
                        colrsi += 1
                        if colrsi == 8:
                            colrsi = 0
            elif self.curtoken == self.aminotok:
                self._shapely(amino=True)
            elif self.curtoken == self.chaintok:
                util.cbc(self.vslselectionsaved)
            elif self.curtoken == self.chargetok:
                cmd.spectrum('b', 'rainbow_rev', 
                    '%s and not r. hoh' % self.vslselectionsaved)
            elif self.curtoken == self.cpktok:
                self._cpk()
            elif self.curtoken == self.cpknewtok:
                self._cpk(True)
            elif self.curtoken == self.grouptok:
                util.chainbow(self.vslselectionsaved)
            elif self.curtoken == self.modeltok:
                states = cmd.count_states()
                cmd.select('states', 'all')
                try:
                    cmd.split_states('states')
                except:
                    pass
                tocolour = self._interpolate_colour(1, states)
                for toc in tocolour:
                    zeros = 4-len(str(tocolour[toc][0]))
                    cselec = 'states_%s%s' % ('0'*zeros, tocolour[toc][0])
                    cmd.color(tocolour[toc][1], cselec)
            elif self.curtoken == self.shapelytok:
                self._shapely()
            elif self.curtoken == self.structuretok:
                cmd.set_color('helix', [.941, 0., .502])
                cmd.set_color('sheet', [1., 1., 0.])
                cmd.set_color('turn', [.376, .502, 1.])
                cmd.color('helix', 'ss h')
                cmd.color('sheet', 'ss s')
                cmd.color('turn', "ss ''")
                cmd.color('white', "not (ss h or ss s or ss '')")
            elif self.curtoken == self.temperaturetok:
                stored.temp = []
                cmd.iterate(self.vslselectionsaved,'stored.temp.append(b)')
                try:
                    cmd.spectrum('b', 'rainbow', 
                        '%s and not r. hoh' % self.vslselectionsaved)
                except ValueError:
                    return False
            elif self.curtoken == self.eastertok:
                stored.temp = []
                cmd.iterate(self.vslselectionsaved,'stored.temp.append(b)')
                try:
                    import math
                    minn = int(math.floor(min(stored.temp)))
                    maxx = int(math.ceil(max(stored.temp)))
                    tocolour = {}
                    itr = 0
                    for col in range(minn, maxx + 1, 2):
                        tocolour[itr] = col
                        itr += 1
                except ValueError:
                    return False
                for toc in tocolour:
                    if (toc+1) not in tocolour:
                        cselec = '(b = %s) or (b > %s)' % (tocolour[toc],
                            tocolour[toc])
                    else:
                        cselec = '(b = %s) or (b > %s and b < %s)' % (
                            tocolour[toc], tocolour[toc], tocolour[toc+1])
                    cmd.color(tocolour[toc], cselec)
            elif self.curtoken == self.usertok:
                return False
            return True
        else:
            return False
        try:
            name = ('vslc_%s' % rgb).replace(' ','')
            cmd.set_color(name, rgb)
            return name
        except:
            print "RGB Triplet not valid."
            return False
    
    def _interpolate_colour(self, minn, maxx):
        """Interpolates from red to blue"""
        minn = int(minn)
        maxx = int(maxx)
        steps = []
        tocol = {}
        intrp = {}
        colours = [1., 0., 0.], [0., 1., 0.], [0., 0., 1.]
        stti, midi, endi = 0, 1, 2
        stt, mid, end = colours
        for step in range(minn, maxx + 1):
            steps.append(step)
        stepsl = len(steps)/4.
        cnt = .5
        for step in steps:
            if cnt <= stepsl:
                abc = 1.
                efg = mid[midi]*(cnt/stepsl)
                hij = 0.
            elif cnt <= stepsl*2.:
                abc = 1. - stt[stti]*((cnt-stepsl)/stepsl)
                efg = 1.
                hij = 0.
            elif cnt <= stepsl*3.:
                abc = 0.
                efg = 1.
                hij = end[endi]*((cnt-(stepsl*2.))/stepsl)
            else:
                abc = 0
                efg = 1. - mid[midi]*((cnt-(stepsl*3.))/stepsl)
                hij = 1.
            intrp[step] = [abc, efg, hij]
            cnt += 1.
        #**import pprint
        #**pprint.pprint(intrp)
        itr = 0
        for trp in intrp:
            fstr = 'itp%.f' % (trp)
            cmd.set_color(fstr, intrp[trp])
            tocol[itr] = (trp, fstr)
            itr += 1
        return tocol
    
    def _shapely(self, amino=False):
        '''Color by shapely or amino'''
        colorindex = {}
        selection = self.vslselectionsaved
        for i in cmd.get_color_indices():
            key, val = i
            colorindex[key] = val
        if amino:
            shp = self.aminodict
            suffix = 'ami'
        else:
            shp = self.shapelydict
            suffix = 'shp'
        for key in shp:
            color = '%s%s' % (key, suffix)
            if color not in colorindex:
                cmd.set_color(color, shp[key])
        unk = 'not r. '
        for key in shp:
            if key == 'Backbone':
                continue
            if key == 'Special':
                continue
            if key != 'UNK':
                cmd.color('%s%s' % (key, suffix),
                    '(r. %s & %s)' % (key, selection))
                unk += '%s+' % key
        cmd.color('UNK%s' % suffix, '((%s) & %s)' % (unk[:-1], selection))

    def _cpk(self, cpknew=False):
        '''Color in cpk or cpknew'''
        colorindex = {}
        selection = self.vslselectionsaved
        for i in cmd.get_color_indices():
            key, val = i
            colorindex[key] = val
        if cpknew:
            cpk = self.cpknewdict
            suffix = 'cpknew'
        else:
            cpk = self.cpkdict
            suffix = 'cpk'
        for key in cpk:
            color = '%s%s' % (key, suffix)
            if color not in colorindex:
                cmd.set_color(color, cpk[key])
        unk = 'not e. '
        for key in cpk:
            if key != 'UNK':
                cmd.color('%s%s' % (key, suffix),
                    '(e. %s & %s)' % (key, selection))
                unk += '%s+' % key
        cmd.color('UNK%s' % suffix, '((%s) & %s)' % (unk[:-1], selection))

    def _preselect(self, presel):
        '''Run before _select to seperate commands 
           from parentheses and others'''
        selection = ''
        #**print presel
        preseldict = {}
        preselpos = 0
        curpos = 0
        skiplist = ['not', 'and', 'or', '(', ')', ' ']
        andin = [i for i in xrange(len(presel)) if presel.startswith('and', i)]
        orin = [i for i in xrange(len(presel)) if presel.startswith('or', i)]
        notin = [i for i in xrange(len(presel)) if presel.startswith('not', i)]

        for iii in presel:
            if preselpos not in preseldict:
                preseldict[preselpos] = ''
            if iii == '(':
                preselpos += preseldict[preselpos] == '' and 0 or 1
                preseldict[preselpos] = ''
                preseldict[preselpos] += iii
                preselpos += 1
            elif iii == ')':
                preselpos += preseldict[preselpos] == '' and 0 or 1
                preseldict[preselpos] = ''
                preseldict[preselpos] += iii
                preselpos += 1
            elif curpos in andin:
                preselpos += preseldict[preselpos] == '' and 0 or 1
                preseldict[preselpos] = ''
                preseldict[preselpos] += iii
            elif curpos-1 in andin:
                preseldict[preselpos] += iii
            elif curpos-2 in andin:
                preseldict[preselpos] += iii
                preselpos += 1
            elif curpos in notin:
                preselpos += preseldict[preselpos] == '' and 0 or 1
                preseldict[preselpos] = ''
                preseldict[preselpos] += iii
            elif curpos-1 in notin:
                preseldict[preselpos] += iii
            elif curpos-2 in notin:
                preseldict[preselpos] += iii
                preselpos += 1
            elif curpos in orin:
                preselpos += preseldict[preselpos] == '' and 0 or 1
                preseldict[preselpos] = ''
                preseldict[preselpos] += iii
            elif curpos-1 in orin:
                preseldict[preselpos] += iii
                preselpos += 1
            else:
                preseldict[preselpos] += iii
            curpos += 1
        
        #**import pprint
        #**pprint.pprint(preseldict)
        if len(preseldict) == 0:
            return self._select('')
        restrict = -1
        for abc in preseldict:
            if 'within' in preseldict[abc]:
                if preseldict[abc+1] == '(':
                    if ',' in preseldict[abc+2]:
                        within = preseldict[abc+2].split(',')
                        if preseldict[abc+3] == ')':
                            restrict = abc+3
                            selection = '%s%s expand %s ' % (selection,
                                self._select(within[1]), within[0])
            if abc <= restrict:
                continue
            if preseldict[abc] in skiplist:
                selection = '%s%s ' % (selection, preseldict[abc].strip())
            else:
                selection = '%s%s ' % (selection, self._select(preseldict[abc]))
        return selection

    ##-----Select Function-----##
    def _select(self, allparameters):
        '''************************'''
        allparameters = allparameters.strip()
        if allparameters == 'false':
            return allparameters

        ## list of elements in the periodic table how they are entered in
        ## RasMol and PyMOL
        ## dictionary data structure { RasMol: PyMOL }
        periodictable = {}
        periodictable['gold'] = 'au'
        periodictable['neon'] = 'ne'
        periodictable['cobalt'] = 'co'
        periodictable['germanium'] = 'ge'
        periodictable['fermium'] = 'fm'
        periodictable['gadolinium'] = 'gd'
        periodictable['zinc'] = 'zn'
        periodictable['neodymium'] = 'nd'
        periodictable['sodium'] = 'na'
        periodictable['selenium'] = 'se'
        periodictable['technetium'] = 'tc'
        periodictable['meitnerium'] = 'mt'
        periodictable['sulfur'] = 's'
        periodictable['beryllium'] = 'be'
        periodictable['americium'] = 'am'
        periodictable['barium'] = 'ba'
        periodictable['californium'] = 'cf'
        periodictable['tungsten'] = 'w'
        periodictable['protactinium'] = 'pa'
        periodictable['silver'] = 'ag'
        periodictable['terbium'] = 'tb'
        periodictable['aluminum'] = 'al'
        periodictable['molybdenum'] = 'mo'
        periodictable['hassium'] = 'hs'
        periodictable['lawrencium'] = 'lr'
        periodictable['indium'] = 'in'
        periodictable['krypton'] = 'kr'
        periodictable['rubidium'] = 'rb'
        periodictable['nitrogen'] = 'n'
        periodictable['radium'] = 'ra'
        periodictable['astatine'] = 'at'
        periodictable['berkelium'] = 'bk'
        periodictable['antimony'] = 'sb'
        periodictable['europium'] = 'eu'
        periodictable['lead'] = 'pb'
        periodictable['lutetium'] = 'lu'
        periodictable['nobelium'] = 'no'
        periodictable['flourine'] = 'f'
        periodictable['cerium'] = 'ce'
        periodictable['osmium'] = 'os'
        periodictable['rhodium'] = 'rh'
        periodictable['curium'] = 'cm'
        periodictable['mercury'] = 'hg'
        periodictable['yttrium'] = 'y'
        periodictable['samarium'] = 'sm'
        periodictable['thorium'] = 'th'
        periodictable['strontium'] = 'sr'
        periodictable['bromine'] = 'br'
        periodictable['boron'] = 'b'
        periodictable['carbon'] = 'c'
        periodictable['chlorine'] = 'cl'
        periodictable['ytterbium'] = 'yb'
        periodictable['gallium'] = 'ga'
        periodictable['silicon'] = 'si'
        periodictable['tantalum'] = 'ta'
        periodictable['cadmium'] = 'cd'
        periodictable['cesium'] = 'cs'
        periodictable['copper'] = 'cu'
        periodictable['oxygen'] = 'o'
        periodictable['praseodymium'] = 'pr'
        periodictable['arsenic'] = 'as'
        periodictable['chromium'] = 'cr'
        periodictable['platinum'] = 'pt'
        periodictable['mendelevium'] = 'md'
        periodictable['actinium'] = 'ac'
        periodictable['thulium'] = 'tm'
        periodictable['nickel'] = 'ni'
        periodictable['ruthenium'] = 'ru'
        periodictable['potassium'] = 'k'
        periodictable['dubnium'] = 'db'
        periodictable['argon'] = 'ar'
        periodictable['palladium'] = 'pd'
        periodictable['promethium'] = 'pm'
        periodictable['bismuth'] = 'bi'
        periodictable['neptunium'] = 'np'
        periodictable['lanthanum'] = 'la'
        periodictable['francium'] = 'fr'
        periodictable['zirconium'] = 'zr'
        periodictable['erbium'] = 'er'
        periodictable['radon'] = 'rn'
        periodictable['niobium'] = 'nb'
        periodictable['calcium'] = 'ca'
        periodictable['iridium'] = 'ir'
        periodictable['magnesium'] = 'mg'
        periodictable['iron'] = 'fe'
        periodictable['plutonium'] = 'pu'
        periodictable['dysprosium'] = 'dy'
        periodictable['iodine'] = 'i'
        periodictable['rhenium'] = 're'
        periodictable['titanium'] = 'ti'
        periodictable['hydrogen'] = 'h'
        periodictable['thallium'] = 'tl'
        periodictable['helium'] = 'he'
        periodictable['uranium'] = 'u'
        periodictable['seaborgium'] = 'sg'
        periodictable['tin'] = 'sn'
        periodictable['holmium'] = 'ho'
        periodictable['lithium'] = 'li'
        periodictable['polonium'] = 'po'
        periodictable['bohrium'] = 'bh'
        periodictable['hafnium'] = 'hf'
        periodictable['scandium'] = 'sc'
        periodictable['einsteinium'] = 'es'
        periodictable['phosphorus'] = 'p'
        periodictable['rutherfordium'] = 'rf'
        periodictable['vanadium'] = 'v'
        periodictable['manganese'] = 'mn'
        periodictable['tellurium'] = 'te'
        periodictable['xenon'] = 'xe'
        ## RasMol's predefined sets and PyMOL's equivalents
        ## dictionary data structure { RasMol: PyMOL }
        predefinedlists = {}
        predefinedlists['selected'] = ' vslselection '
        predefinedlists['sidechain'] = ' resn asp+glu+arg+lys+his+asn+thr+cys+\
gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro+a+t+c+g and not name o1p+o2p+\
o3p+p+c1*+c2*+c3*+c4*+c5*+o2*+o3*+o4*+o5*+c+o+n+ca '
        predefinedlists['surface'] = ' resn gly+ser+thr+lys+asp+asn+glu+pro+arg\
+gln+tyr+his '
        predefinedlists['nucleic'] = ' resn a+t+c+g '
        predefinedlists['aliphatic'] = ' resn gly+ala+leu+val+ile '
        predefinedlists['pyrimidine'] = ' resn c+t '
        predefinedlists['buried'] = ' resn ala+leu+val+ile+phe+cys+met+trp '
        predefinedlists['protein'] = ' resn asp+glu+arg+lys+his+asn+thr+cys+gln\
+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro '
        predefinedlists['purine'] = ' resn a+g '
        predefinedlists['sheet'] = ' ss s '
        predefinedlists['hetero'] = ' hetatm '
        predefinedlists['aromatic'] = ' resn his+tyr+tr+phe+pro '
        predefinedlists['helix'] = ' ss h '
        predefinedlists['basic'] = ' resn arg+lys+his '
        predefinedlists['acidic'] = ' resn asp+glu '
        predefinedlists['amino'] = ' resn gln+asn+asp+glu+arg+lys+his+thr+cys+\
tyr+ser+gly+trp+phe+pro+leu+val+ile+met'
        predefinedlists['cystine'] = ' (byres (((all) & r. CYS+CYX & n. SG) & \
bound_to ((all) & r. CYS+CYX & n. SG))) & n. CA+CB+SG'
        predefinedlists['polar'] = ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+\
ser+gly+tyr '
        predefinedlists['medium'] = ' resn val+thr+asp+asn+pro+cys '
        predefinedlists['backbone'] = ' name o1p+o2p+o3p+p+c1*+c2*+c3*+c4*+c5*+\
o2*+o3*+o4*+o5*+c+o+n+ca '
        predefinedlists['hoh'] = ' resn hoh '
        predefinedlists['water'] = ' resn hoh '
        predefinedlists['neutral'] = ' resn asn+thr+cys+gln+tyr+ser+gly+ala+leu\
+val+ile+met+trp+phe+pro '
        predefinedlists['alpha'] = ' name ca '
        predefinedlists['cyclic'] = ' resn pro+phe+trp+tyr+his '
        predefinedlists['large'] = ' resn glu+arg+lys+his+gln+tyr+leu+ile+met+\
trp+phe '
        predefinedlists['turn'] = ' ss 1 '
        predefinedlists['small'] = ' resn gly+ala+ser '
        predefinedlists['acyclic'] = ' resn met+ile+val+leu+ala+gly+ser+gln+thr\
+asn+cys+lys+arg+asp+glu '
        predefinedlists['hydrophobic'] = ' resn ala+leu+val+ile+met+trp+phe+pro '
        predefinedlists['charged'] = ' resn asp+glu+arg+lys+his '
        ## Amino Acids as they appear in both RasMol and PyMOL
        aminolist = ['gly', 'ala', 'val', 'leu', 'ile', 'met', 'pro', 'phe',
            'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp',
            'glu', 'asn', 'gln']

        selection = 'false'
        if '.' in allparameters:
            found = allparameters.split('.')
            selection = '%s and name %s' % (self._select(found[0]),
                self._select(found[1]))
        elif ':' in allparameters:
            found = allparameters.split(':')
            if len(found[0])>0:
                selection = '%s and chain %s' % (self._select(found[0]),
                    found[1])
            else:
                selection = 'chain %s' % found[1]
        elif allparameters == 'all' or allparameters == '*':
            selection = 'all'
        elif allparameters == '':
            if self.hydrogen:
                cmd.h_add('all')
                if self.hetero:
                    selection = 'all'
                else:
                    selection = 'all and not hetero'
            else:
                if self.hetero:
                    selection = 'all and not hydrogen'
                else:
                    selection = 'all and not hydrogen or hetero'
        elif allparameters in predefinedlists:
            selection = predefinedlists[allparameters]
        elif allparameters in self.userdefinedgroups:
            selection = self._select(self.userdefinedgroups[allparameters])
        elif allparameters in periodictable:
            selection = 'symbol %s' % periodictable[allparameters]
        elif allparameters in aminolist:
            selection = 'resn %s' % allparameters
        elif allparameters[:6] == 'atomno':
            lower = 1
            upper = 999999999
            if '>' in allparameters:
                found = allparameters.split('>=')
                if len(found) == 2:
                    lower = int(found[1])
                else:
                    lower = int(found[0].split('>')[1]) + 1
            elif '<' in allparameters:
                found = allparameters.split('<=')
                if len(found) == 2:
                    upper = int(found[1])
                else:
                    upper = int(found[0].split('<')[1]) - 1
            elif '=' in allparameters:
                found = allparameters.split('=')
                upper = int(found[1])
                lower = int(found[1])
            selection = 'id %s-%s' % (lower, upper)
        else:
            selection = 'resi %s' % allparameters.replace(',', '+')
        return selection

    ## Handles all map commands
    def _mapsupport(self, parameters):
        '''************************'''
        parameterslist = parameters.split(' ')
        try:
            if int(parameterslist[0]):
                self.map_selection = int(parameterslist[0])
                self.map_unspecified_selection = False
                print 'You gave a number: ' + str(self.map_selection)
                if self.map_selection > self.map_name:
                    self.map_name = self.map_selection
                self._handlemap(parameterslist[1:])
        except:
            print 'Map command'
            self.map_unspecified_selection = True
            self._handlemap(parameterslist)

    ## Handles all map commands.
    def _handlemap(self, parameterslist):
        '''************************'''
        goodlist = ['generate', 'level', 'color', 'zap']
        badlist = ['load', 'mask', 'resolution', 'restrict', 'save', 'select',
            'show', 'spacing', 'spread']
        try:
            if parameterslist[0] == 'generate':
                if parameterslist[1] == 'mesh':
                    if self.map_unspecified_selection:
                        self.map_selection = self.map_name
                    self.map_name += 1
                    cmd.do('map_new %s, %s, %s, vslselection' % (
                        self.map_selection, self.map_type, self.map_grid))
                    cmd.do('isomesh mesh_%s, %s, %s' % (self.map_selection,
                        self.map_selection, self.map_level))
                    cmd.do('zoom %s, %s' % (self.centerselection, self.zoomnum))
                    print 'Mesh map complete'
                elif parameterslist[1] == 'dots':
                    if self.map_unspecified_selection:
                        self.map_selection = self.map_name
                    self.map_name += 1
                    cmd.do('map_new %s, %s, %s, vslselection' % (
                        self.map_selection, self.map_type, self.map_grid))
                    cmd.do('isomesh dot_%s, %s, %s' % (self.map_selection,
                        self.map_selection, self.map_level))
                    cmd.do('zoom %s, %s' % (self.centerselection, self.zoomnum))
                    print 'Dots map complete'
                elif parameterslist[1] == 'surface':
                    if self.map_unspecified_selection:
                        self.map_selection = self.map_name
                    self.map_name += 1
                    cmd.select(str(self.map_selection), self.vslselectionsaved)
                    cmd.show('surface', self.map_selection)
                    cmd.do('set surface_color, white')
                    cmd.do('zoom %s, %s' % (self.centerselection, self.zoomnum))
                    print 'Surface map complete'
            elif parameterslist[0] == 'level':
                if parameterslist[1] == 'mean':
                    print 'The MEAN function is not supported by PyMOL.'
                else:
                    self.map_level = int(parameterslist[1])
            elif parameterslist[0] == 'color':
                if self.map_unspecified_selection:
                    cmd.do('color %s, mesh_*' % parameterslist[1])
                    cmd.do('color %s, dot_*' % parameterslist[1])
                    cmd.do('set surface_color, %s' % parameterslist[1])
                else:
                    cmd.do('color %s, mesh_%s' % (parameterslist[1],
                        self.map_selection))
                    cmd.do('color %s, dot_%s' % (parameterslist[1],
                        self.map_selection))
                    cmd.do('set surface_color, %s' % parameterslist[1])
            elif parameterslist[0] == 'zap':
                cmd.delete('mesh_*')
                cmd.delete('dot_*')
                cmd.hide('surface')
                for i in range(0, self.map_name):
                    cmd.delete(str(i))
        except:
            print 'An error has occured with a map command.'

    ##Handles parameters that can be changed using the 'set' command
    def _set_parameters(self, parameters):
        '''************************'''
        not_coded = ['backfade', 'bondmode', 'bonds', 'cisangle', 'fontstroke',
            'hourglass ', 'kinemage', 'menus', 'strands', 'transparent',
            'vectps', 'write', 'boundbox', 'display', 'mouse', 'picking',
            'shadepower', 'slabmode', 'specpower', 'cartoon', 'hbonds',
            'radius', 'ssbonds']
        try:
            parameters = parameters.split(' ')
            ##Check the parameter to see if it something that will convert in
            #the first place
            if parameters[0].rstrip() in not_coded:
                print 'That setting does not translate into PyMOL.'
            else:
                ##Seperate the parameter by spaces for ease of recalling them
                #later
                first = parameters[0].rstrip().lower()
                if len(parameters) > 1:
                    second = parameters[1].rstrip().lower()
                ##PARAMETER: background - complete
                if first == 'background':
                    cmd.bg_color(second)
                ##PARAMETER: ambient - PyMOL ambient only seems noticable on
                #some views
                elif first == 'ambient':
                    light = int(second)/50 - 1
                    cmd.set('ambient', light)
                ##PARAMETER: unitcell - Uses PyMOL's view 'cell'
                elif first == 'unitcell':
                    if second == 'on' or second == 'true':
                        cmd.show('cell')
                    elif second == 'false' or second == 'off':
                        cmd.hide('cell')
                    else:
                        print 'An error has occured with unitcell parameter.'
                ##PARAMETER: cartoon
                elif first == 'cartoon':
                    cmd.cartoon('rectangle', '(all)')
                    if len(parameters) == 1:
                        cmd.set('cartoon_fancy_sheets', 1)
                        cmd.set('cartoon_rect_length', 1.5)
                    else:
                        if second == 'on' or second == 'true':
                            cmd.set('cartoon_fancy_sheets', 1)
                            cmd.set('cartoon_rect_length', 1.5)
                        elif second == 'off' or second == 'false':
                            cmd.set('cartoon_fancy_sheets', 0)
                        else:
                            ##cmd.set( 'cartoon_rect_length',
                            pass
                ##PARAMETER: axes - produces axes at origin showing x, y and z
                ##planes, lines center at origin, not center of molecule
                elif first == 'axes':
                    if second == 'on' or second == 'true':
                        #Credit goes to the contributors of the PyMOLwiki
                        # (pymolwiki.org) on the article 'Axes': Krother, Tree
                        # and Inchoate  Thank you
                        # create the axes object, draw axes with cylinders
                        # coloured red, green, blue for X, Y and Z

                        obj = [
                            CYLINDER, 0., 0., 0., 10., 0., 0., 0.2, 1.0, 1.0,
                                1.0, 1.0, 0.0, 0.,
                            CYLINDER, 0., 0., 0., 0., 10., 0., 0.2, 1.0, 1.0,
                                1.0, 0., 1.0, 0.,
                            CYLINDER, 0., 0., 0., 0., 0., 10., 0.2, 1.0, 1.0,
                                1.0, 0., 0.0, 1.0,
                            ]
                        # add labels to axes object (requires pymol version
                        # 0.8 or greater, I believe
                        cyl_text(obj, plain, [-5., -5., -1], 'Origin', 0.20,
                            axes=[[3, 0, 0], [0, 3, 0], [0, 0, 3]])
                        cyl_text(obj, plain, [10., 0., 0.], 'X', 0.20,
                            axes=[[3, 0, 0], [0, 3, 0], [0, 0, 3]])
                        cyl_text(obj, plain, [0., 10., 0.], 'Y', 0.20,
                            axes=[[3, 0, 0], [0, 3, 0], [0, 0, 3]])
                        cyl_text(obj, plain, [0., 0., 10.], 'Z', 0.20,
                            axes=[[3, 0, 0], [0, 3, 0], [0, 0, 3]])
                        # then we load it into PyMOL
                        cmd.load_cgo(obj, 'axes')
                        cmd.zoom('all')
                    elif second == 'false' or second == 'off':
                        cmd.delete('axes')
                        cmd.zoom('all')
                    else:
                        print 'An error occured with the axes command.'
                ##PARAMETER: fontsize - complete
                elif first == 'fontsize':
                    cmd.set('label_size', int(second))
                ##PARAMETER: stereo - stereo angle is not the same between the
                ##programs, PyMOL shifts the images, RasMol rotates them
                elif first == 'stereo':
                    if second == 'on' or second == 'true' or second == '':
                        cmd.set('stereo', 1)
                    elif second == 'false' or second == 'off':
                        cmd.set('stereo', 0)
                    else:
                        print 'ConSCRIPT does not support this setting.'
                ##PARAMETER: hbonds
                elif first == 'hbonds':
                    if second == 'sidechain':
                        self.hbonds_backbone = False
                    elif second == 'backbone':
                        self.hbonds_backbone = True
                    else:
                        print 'That parameter is not a valid RasMol parameter.'
                ##PARAMETER: ssbonds
                elif first == 'ssbonds':
                    if second == 'sidechain':
                        self.ssbonds_backbone = False
                    elif second == 'backbone':
                        self.ssbonds_backbone = True
                    else:
                        print 'That parameter is not a valid RasMol parameter.'
                ##PARAMETER: hydrogen - complete
                elif first == 'hydrogen':
                    if second == 'on' or second == 'true':
                        self.hydrogen = True
                    elif second == 'off' or second == 'false':
                        self.hydrogen = False
                    else:
                        print 'An error has occured with the hydrogen setting.'
                ##PARAMETER: hetero - complete
                elif first == 'hetero':
                    if second == 'on' or second == 'true':
                        self.hetero = True
                    elif second == 'off' or second == 'false':
                        self.hetero = False
                    else:
                        print 'An error has occured with the hetero setting.'
                ##PARAMETER: solvent - complete
                elif first == 'solvent':
                    if second == 'on' or second == 'true':
                        self.solvent = True
                        self.radius = 1.2
                    elif second == 'off' or second == 'false':
                        self.solvent = False
                        self.radius = 0.0
                    else:
                        print 'An error has occured with the solvent setting.'
                ##PARAMETER: radius - failed to get PyMOL dot-radius setting to
                ##work, unable to determine setting ratio
                elif first == 'radius':
                    cmd.set('dot_radius', int(second))
                ##PARAMETER: monitor - complete
                elif first == 'monitor':
                    if second == 'on' or second == 'true':
                        self.set_monitor = True
                        cmd.show('labels')
                    elif second == 'off' or second == 'false':
                        self.set_monitor = False
                        cmd.hide('labels')
                    else:
                        print 'An error occured with the monitor setting.'
                ##PARAMETER: specular - does not work with version 0.99,
                ##requires 1.0 or newer
                elif first == 'specular':
                    if second == 'on' or second == 'true':
                        cmd.set('specular', 'on')
                    elif second == 'off' or second == 'false':
                        cmd.set('specular', 'off')
                    else:
                        print 'An error has occured with the specular setting.'
                ##PARAMETER: shadow - cant get this to work in PyMOL but this
                ##what should work
                elif first == 'shadow':
                    if second == 'on' or second == 'true':
                        cmd.set('ray_shadows', 'on')
                    elif second == 'off' or second == 'false':
                        cmd.set('ray_shadows', 'off')
                    else:
                        print 'An error has occured with the Shadows setting.'
                ##PARAMETER: verbose -- set the self.vslverbose flag
                elif first == 'verbose':
                    if second == 'on' or second == 'true':
                        self.vslverbose = 1
                    elif second == 'off' or second == 'false':
                        self.vslverbose = 0
                    else:
                        print 'An error has occured with the Verbose setting.'
                else:
                    print 'That setting is not a valid RasMol setting.'
        except:
            print 'An error has occured with a setting.'

    ## Defines hbonds for a structure
    def _hbonds(self):
        '''************************'''
        try:
            cmd.h_add('all')
            cmd.select('don',
                '(elem n,o and (neighbor elem h) and vslselection)')
            cmd.select('acc',
              '(elem o or (elem n and not (neighbor elem h))) and vslselection')
            cmd.distance('HBA', '(acc)', '(don)', '3.2')
            cmd.distance('HBD', '(don)', '(acc)', '3.2')
            cmd.delete('don')
            cmd.delete('acc')
            cmd.hide('(elem h)')
            cmd.hide('labels', 'HBA')
            cmd.hide('labels', 'HBD')
        except:
            print 'Error occured with calculating hbonds.'

    ## Defines ssbonds for a structure
    def _ssbonds(self):
        '''************************'''
        try:
            cmd.h_add('all')
            cmd.select('SSCys', '(elem S and resn Cys) and vslselection')
            cmd.distance('SSCysteines', '(SSCys)', '(SSCys)', '3.0')
            cmd.delete('SSCys')
            cmd.hide('(elem h)')
            cmd.hide('labels', 'SSCysteines')
        except:
            print 'Error occured with calculating ssbonds.'

    ## Handle a command line
    def handlecommand(self, commands):
        '''************************'''
        self.tokenstart = 0 
        self.tokenptr = 0
        self.curtoken = 0
        self.tokenident = ""
        self.tokenvalue = 0
        if(commands.replace(' ', '') == "\n"):
            return 0

        if(commands.replace(' ', '')[:1] == '#'):
            print commands
            return 0
        commands = commands.lower()
        self._vslfetchtoken(commands)

        # handle temporary selection
        self.vslselectionsaved = self.vslselection
        if self.curtoken == -ord('('):
            stack = []
            end = -1
            for per in range(self.tokenstart + 1, len(commands)):
                if commands[per:per+1] == '(':
                    stack.append('(')
                if commands[per:per+1] == ')':
                    if stack == []:
                        end = per
                        per = len(commands)
                    else:
                        stack.pop()
            if end != -1:
                chm = commands[self.tokenstart:end+1]
                chm = chm.lower()
                self.vslselection = self._preselect(chm)
                if self.vslverbose > 0:
                    print 'vslselection: ' + self.vslselection
                if end < len(commands)-1 and commands[end+1:end+2] == '.':
                    end = end+1
                self.tokenptr = 0
                self.tokenstart = 0
                self.curtoken = 0
                self.tokenident = ""
                self.tokenvalue = 0
                commands = commands[end+1:len(commands)]
                try:
                    self._vslfetchtoken(commands)
                except:
                    print 'vslfetchtoken failed tokenptr = %s' % (self.tokenptr)
 
        if self.vslverbose > 0:
            print os.times()
            print 'vslselection: ' + self.vslselection
            print 'VSLcommand: ' + commands

        ##---------------Script---------------##

        if self.curtoken == self.scripttok or self.curtoken == self.sourcetok:
            self._vslfetchtoken(commands)
            if self.curtoken == 0:
                print commands
                print 'Does not contain a valid filename'
            elif self.curtoken == self.stringtok:
                try:
                    print '\"'+self.tokenident+'\"' + '<--SCRIPTFILE'
                    return vslcmd(filename=self.tokenident)
                except:
                    print '\"'+self.tokenident+'\"' + '<--SCRIPTFILE'
                    print 'EXCEPTION THROWN'
            else:
                chm = commands[self.tokenstart:len(commands)]
                try:
                    print chm + '<--SCRIPTFILE'
                    return vslcmd(filename=chm)
                except:
                    print chm + '<--SCRIPTFILE'
                    print 'EXCEPTION THROWN'
            return 0
        ##---------------Load---------------##

        if self.curtoken == self.loadtok:
            self._vslfetchtoken(commands)
            if self._ismoleculetoken(self.curtoken):
                try:
                    self._vslfetchtoken(commands)
                except:
                    print 'vslfetchtoken failed tokenptr = %s' % (self.tokenptr)
            if self.curtoken == 0:
                print p
                print 'Does not contain a valid filename'
            elif self.curtoken == self.stringtok:
                try:
                    self.tokenident = self.tokenident.strip('"\'')
                    print self.tokenident + '<--LOADFILE'
                    cmd.load(self.tokenident)
                    cmd.rotate('x', 180)
                    cmd.select('vslselection', '(all)')
                    cmd.select('VSLCenterSelection', self.centerselection)
                    cmd.center(self.centerselection)
                    self.vslselection = '(all)'
                    self.vslselectionsaved = self.vslselection
                    self._cpk()
                    if self.vslverbose > 0:
                        print 'vslselection: ' + self.vslselection
                except:
                    print '\"'+self.tokenident+'\"' + '<--LOADFILE'
                    print 'EXCEPTION THROWN'
            else:
                chm = commands[self.tokenstart:len(commands)]
                try:
                    chm = chm.strip('"\'')
                    print chm + '<--LOADFILE'
                    cmd.load(chm)
                    cmd.rotate('x', 180)
                    cmd.select('vslselection', '(all)')
                    cmd.select('VSLCenterSelection', self.centerselection)
                    cmd.center(self.centerselection)
                    self.vslselection = '(all)'
                    self.vslselectionsaved = self.vslselection
                    self._cpk()
                    if self.vslverbose > 0:
                        print 'vslselection: %s' % self.vslselection
                except:
                    print chm + '<--LOADFILE'
                    print 'EXCEPTION THROWN'
            return 0

        ##---------------Save---------------##

        if self.curtoken == self.writetok or self.curtoken == self.savetok:
            sav = ''
            for i in commands.split(' ', 1)[1]:
                sav = '%s%s' % (sav, i)
            print sav + '<--SAVEFILE'
            if sav[-3:] == 'bmp' or sav[-3:] == 'gif':
                cmd.png(sav)
            else:
                cmd.save(sav)
            return 0

        ##---------------Echo---------------##

        if self.curtoken == self.echotok:
            returnval = commands[len(self.tokenident)+1:]
            if returnval[:1] == '"':
                returnval = returnval[1:]
            if returnval[-1:] == '"':
                returnval = returnval[:-1]
            print returnval
            return 0

        ##---------------Label---------------##

        if self.curtoken == self.labeltok:
            commands += ' '
            labeltext = commands.split(' ', 1)[1]
            specifier_conv = {'a':'name', 'b':'b', 't':'b', 'c':'chain',
                's':'chain', 'e':'type', 'i':'ID', 'n':'resn', 'r':'resi'}
            specifiers = []
            if labeltext[:4].rstrip() == 'off' or\
                labeltext[:5].rstrip() == 'false':
                cmd.do('label vslselection,')
            elif labeltext[:2].rstrip() == 'on' or\
                labeltext[:4].rstrip() == 'true' or labeltext.rstrip() == '':
                cmd.do('label vslselection, "%s%s:%s.%s"' % ('resn', 'resi',
                    'chain', 'name'))
            else:
                for i in range(0, len(labeltext)-1):
                    if labeltext[i] == '%':
                        if str(labeltext[i+1]) in specifier_conv:
                            specifiers += [specifier_conv[str(labeltext[i+1])]]
                            labeltext = labeltext[:i] + '%s' + labeltext[i+2:]
                        else:
                            print 'That expansion specifier is not supported.'
                cmd.do('label vslselection, "%s" % (%s)' % (labeltext,
                    str(specifiers)[1:-1].replace('\'', '')))

        #-----------Background color------------#

        if self.curtoken == self.backgroundtok:
            self._vslfetchtoken(commands)
            result = self._vslparsecolour(commands)
            if result != False:
                cmd.bg_color(result)
            else:
                print self.msgstrs[self.errsyntax]
            return 0

        #----------------Select-----------------#

        if self.curtoken == self.selecttok:
            selected = self._preselect(commands[len(self.tokenident)+1:].lower())
            print selected + '<--SELECTED'
            try:
                cmd.select('vslselection', selected)
                self.vslselection = selected
                if self.vslverbose > 0:
                    print 'vslselection: ' + self.vslselection
            except:
                print '''No selection was made for select, please specify a
                    selection.  If you have specified a selection, please 
                    check your selection for errors.  If no error can be found, 
                    try rewriting your selections a different way.'''
            return 0

        #----------------Restrict-----------------#

        if self.curtoken == self.restricttok:
            selected = self._preselect(commands[len(self.tokenident)+1:].lower())
            restricted = 'all and not (' + selected + ')'
            print selected + '<--RESTRICTED'
            try:
                cmd.select('vslselection', selected)
                self.vslselection = selected
                if self.vslverbose > 0:
                    print 'vslselection: ' + self.vslselection
                cmd.hide('everything', restricted)
            except:
                print '''No selection was made for select, please specify a
                    selection.  If you have specified a selection, please 
                    check your selection for errors.  If no error can be found, 
                    try rewriting your selections a different way.'''
                return 0

        ##---------------Center---------------##

        if self.curtoken == self.centretok:
            self.centerselection = self._preselect(commands[len(self.tokenident)+1:].lower())
            print self.centerselection + '<--CENTER'
            try:
                cmd.select('VSLCenterSelection', self.centerselection)
                cmd.center(self.centerselection)
            except:
                print '''No selection was made for select, please specify a
                    selection.  If you have specified a selection, please 
                    check your selection for errors.  If no error can be found, 
                    try rewriting your selections a different way.'''
                return 0

        ##---------------Color---------------##

        if self.curtoken == self.colourtok:
            self._vslfetchtoken(commands)
            if self.curtoken == self.bondtok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.bondtok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                else:
                    try:
                        cmd.set_bond('stick_color', result, 
                            self.vslselectionsaved)
                    except AttributeError:
                        print 'ERROR: colour bond requires pymol 1.0 or higher'
            elif self.curtoken == self.backbonetok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.backbonetok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            elif self.curtoken == self.ribbontok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.ribbontok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            elif self.curtoken == self.labeltok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.labeltok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            elif self.curtoken == self.dotstok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.dotstok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            elif self.curtoken == self.hbondtok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.hbondtok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            elif self.curtoken == self.maptok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.maptok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            elif self.curtoken == self.ssbondtok:
                self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.ssbondtok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    print self.msgstrs[self.errnosuppt]
            else:
                if self.curtoken == self.atomtok:
                    self._vslfetchtoken(commands)
                result = self._vslparsecolour(commands, self.atomtok)
                if result == False:
                    print self.msgstrs[self.errsyntax]
                elif result == True:
                    pass
                else:
                    cmd.color(result, self.vslselectionsaved)
            return 0

        ##---------------Spacefill/CPK---------------##

        if self.curtoken == self.spacefilltok or self.curtoken == self.cpktok \
            or self.curtoken == self.cpknewtok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    cmd.hide('spheres', self.vslselectionsaved)
                    print 'Spacefill off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.show('spheres', self.vslselectionsaved)
                    print 'Spacefill on complete'
                elif float(command)>=0 and float(command)<=1500:
                    cmd.show('spheres', self.vslselectionsaved)
                    if '.' in command:
                        command = float(command)
                    else:
                        command = float(command)/250
                    cmd.set('sphere_scale', command)
            except:
                print 'An error occured with the spacefill/cpk command'
            return 0

        ##---------------Cartoon---------------##

        if self.curtoken == self.cartoontok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    cmd.hide('cartoon', self.vslselectionsaved)
                    cmd.hide('ribbon', self.vslselectionsaved)
                    print 'Cartoon off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.hide('ribbon', self.vslselectionsaved)
                    cmd.cartoon('rectangle', self.vslselectionsaved)
                    cmd.show('cartoon', self.vslselectionsaved)
                    print 'Cartoon on complete'
                elif float(command)>=0 and float(command)<=500:
                    if '.' in command:
                        command = float(command)
                    else:
                        command = float(command)/250
                    cmd.cartoon('rectangle', self.vslselectionsaved)
                    cmd.hide('ribbon', self.vslselectionsaved)
                    cmd.set('cartoon_rect_length', command)
                    cmd.show('cartoon', self.vslselectionsaved)
                    print 'Cartoon on complete'
            except:
                print 'An error occured with the cartoon command'
            return 0

        ##---------------Trace---------------##

        if self.curtoken == self.tracetok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    cmd.hide('cartoon', self.vslselectionsaved)
                    cmd.hide('ribbon', self.vslselectionsaved)
                    print 'Trace off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.cartoon('tube', self.vslselectionsaved)
                    cmd.hide('ribbon', self.vslselectionsaved)
                    cmd.show('cartoon', self.vslselectionsaved)
                    print 'Trace on complete'
                elif float(command)>=0 and float(command)<=500:
                    if '.' in command:
                        command = float(command) * 10
                    else:
                        command = (float(command)/250) * 10
                    cmd.cartoon('tube', self.vslselectionsaved)
                    cmd.hide('ribbon', self.vslselectionsaved)
                    cmd.show('cartoon', self.vslselectionsaved)
                    cmd.set('cartoon_tube_radius', command)
                    print 'Trace on complete'
            except:
                print 'An error occured with the trace command'
            return 0

        ##---------------Ribbon---------------##

        if self.curtoken == self.ribbontok or self.curtoken == self.ribbon1tok\
            or self.curtoken == self.ribbon2tok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    cmd.hide('cartoon', self.vslselectionsaved)
                    cmd.hide('ribbon', self.vslselectionsaved)
                    print 'Ribbon off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.hide('cartoon', self.vslselectionsaved)
                    cmd.show('ribbon', self.vslselectionsaved)
                    print 'Ribbon on complete'
                elif float(command)>=0 and float(command)<=500:
                    if '.' in command:
                        command = float(command)
                    else:
                        command = float(command)/250
                    cmd.hide('cartoon', self.vslselectionsaved)
                    cmd.show('ribbon', self.vslselectionsaved)
                    cmd.set('ribbon_width', command)
                    print 'Ribbon on complete'
            except:
                print 'An error occured with the ribbon command'
            return 0

        ##---------------Wireframe---------------##

        if self.curtoken == self.wireframetok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    cmd.hide('lines', self.vslselectionsaved)
                    print 'Wireframe off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.show('lines', self.vslselectionsaved)
                    print 'Wireframe on complete'
                elif float(command)>=0 and float(command)<=1500:
                    if '.' in command:
                        command =  float(command)
                    else:
                        command =  float(command)/ 250
                    cmd.show('sticks', self.vslselectionsaved)
                    cmd.set('stick_radius', command)
                    print 'Wireframe on complete'
            except:
                print 'An error occured with the wireframe command'
                return 0
            return 0

        ##---------------Dots---------------##

        if self.curtoken == self.dotstok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off' or command == '0':
                    cmd.hide('dots', self.vslselectionsaved)
                    print 'Dots off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.show('dots', self.vslselectionsaved)
                    if self.solvent:
                        cmd.set('dot_solvent', 'on')
                    else:
                        cmd.set('dot_solvent', 'off')
                    cmd.set('dot_radius', self.radius)
                    print 'Dots on complete'
                elif int(command)>0 and int(command)<=1000:
                    command = int(command)
                    cmd.show('dots', self.vslselectionsaved)
                    if self.solvent:
                        cmd.set('dot_solvent', 'on')
                    else:
                        cmd.set('dot_solvent', 'off')
                    cmd.set('dot_radius', self.radius)
                    if command in range(1, 5):
                        cmd.set('dot_density', 0)
                    elif command in range(5, 20):
                        cmd.set('dot_density', 1)
                    elif command in range(20, 140):
                        cmd.set('dot_density', 2)
                    elif command in range(140, 625):
                        cmd.set('dot_density', 3)
                    elif command in range(325, 1000):
                        cmd.set('dot_density', 4)
                    print 'Dots on complete'
            except:
                print 'An error occured with the dots command'
            return 0

        ##---------------Surface--------------##

        if self.curtoken == self.surfacetok:
            try:
                cmd.show('surface', self.vslselectionsaved)
            except:
                print 'An error has occurred with the surface command'
            return 0

        ##---------------Bond---------------##
        if self.curtoken == self.bondtok:
            try:
                commands = commands + ' '
                firstatom = commands.split(' ')[1].rstrip()
                secondatom = commands.split(' ')[2].rstrip()
                if commands.rstrip()[-1] == '+':
                    cmd.bond('id ' + firstatom, 'id ' + secondatom)
                    print '''To create a new bond, use bond <number> <number>.
                        Increasing bond order is not currently supported. 
                        The bond specified has been created if it did not
                        already exist'''
                elif commands.rstrip()[-4:] == 'pick':
                    self.bondfirstatom = firstatom
                    self.bondsecondatom = secondatom
                elif firstatom == 'rotate':
                    print 'PyMOL does not support rotation of bonds'
                elif (int(firstatom) > 0 and int(secondatom) > 0):
                    cmd.bond('id ' + firstatom, 'id ' + secondatom)
                else:
                    print 'That function is not supported by PyMOL'
            except:
                print 'An error has occurred with the bond command'
            return 0

        ##---------------Unbond---------------##
        if self.curtoken == self.unbondtok:
            try:
                if int(commands.rstrip()[-1])>0:
                    firstatom = commands.split(' ')[1].rstrip()
                    secondatom = commands.split(' ')[2].rstrip()
                    cmd.unbond('id ' + firstatom, 'id ' + secondatom)
                elif self.bondfirstatom > 0 and self.bondsecondatom > 0:
                    cmd.unbond(self.bondfirstatom, self.bondsecondatom)
                else:
                    print 'No selection was made.'
            except:
                print 'An error has occured with the unbond command'
            return 0

        ##---------------Zoom---------------##

        if self.curtoken == self.zoomtok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                cmd.select('VSLCenterSelection', self.centerselection)
                if command == 'false' or command == 'off' or command == '':
                    self.zoomnum = 0
                    cmd.zoom('all', self.zoomnum)
                    cmd.center(self.centerselection)
                    print 'Zoom off complete'
                elif command == 'true' or command == 'on':
                    self.zoomnum = -25
                    cmd.zoom('all', self.zoomnum)
                    cmd.center(self.centerselection)
                    print 'Zoom on complete'
                elif int(command) in range(0, 100):
                    self.zoomnum = int(command)
                    self.zoomnum = -((self.zoomnum-100))
                    print 'Zoom ' + str(self.zoomnum)
                    cmd.zoom('all', self.zoomnum)
                    cmd.center(self.centerselection)
                elif int(command) in range(100, 5000):
                    self.zoomnum = int(command)
                    self.zoomnum = -((self.zoomnum-100)/20)
                    print 'Zoom ' + str(self.zoomnum)
                    cmd.zoom('all', self.zoomnum)
                    cmd.center(self.centerselection)
                else:
                    print 'That function is not supported by PyMOL.'
            except:
                print 'Zoom did not execute properly.'
                print 'Please revise your zoom command'
            return 0

        ##---------------Rotate--------------##		

        if self.curtoken == self.rotatetok:
            axis = commands.split()[1]
            rotation = commands.split()[2]
            if axis == 'z':
                rotation = '-' + rotation
            try:
                cmd.rotate(axis, rotation)
            except:
                print '''The parameters you have given for the rotate command 
                    have been entered improperly.  Please rewrite them as rotate
                    (axis) (rotation in degrees)'''
            return 0

        ##---------------Translate---------------##

        if self.curtoken == self.translatetok:
            try:
                commandlist = commands.split(' ')
                if commandlist[1] == 'x':
                    cmd.center('VSLCenterSelection')
                    cmd.translate([int(commandlist[2]), 0, 0])
                elif commandlist[1] == 'y':
                    cmd.center('VSLCenterSelection')
                    cmd.translate('[0,-' + commandlist[2] + ',0]')
                elif commandlist[1] == 'z':
                    cmd.center('VSLCenterSelection')
                    cmd.translate('[0,0,-' + commandlist[2] + ']')
                else:
                    print 'That function is not supported by PyMOL at all'
            except:
                print '''Translate did not execute properly.
                    Please revise your translate command'''
            return 0

        ##---------------Slab---------------##

        if self.curtoken == self.slabtok:
            try:
                cmd.clip('near', -self.clip_dist_near)
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    self.clip_dist_near = 0
                    print 'Slab off complete'
                elif command == 'true' or command == 'on' or command == '':
                    print self.clip_dist_near
                    cmd.clip('near', self.clip_dist_near)
                    print 'Slab on complete'
                elif float(command)>=0 and float(command)<=100:
                    command = float(command)
                    self.clip_dist_near = command-100
                    cmd.clip('near', self.clip_dist_near)
                    print 'Slab on complete'
            except:
                print 'An error occured with the slab command'
            return 0

        ##---------------Depth---------------##

        if self.curtoken == self.depthtok:
            try:
                cmd.clip('far', -self.clip_dist_far)
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    self.clip_dist_far = 0
                    print 'Depth off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.clip('far', self.clip_dist_far)
                    print 'Depth on complete'
                elif float(command)>=0 and float(command)<=100:
                    command = float(command)
                    self.clip_dist_far = command
                    cmd.clip('far', self.clip_dist_far)
                    print 'Depth on complete'
            except:
                print 'An error occured with the depth command'
            return 0

        ##---------------hbonds---------------##

        if self.curtoken == self.hbondtok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    self._hbonds()
                    print 'hbonds off complete'
                elif command == 'true' or command == 'on' or command == '':
                    print 'Starting hbonds on:'
                    self._hbonds()
                    print 'hbonds on complete'
                else:
                    print 'That function is not supported by PyMOL'
            except:
                print '''hbonds did not execute properly.
                    Check spelling and implementation of this hbonds command.'''
            return 0

        ##---------------ssbonds---------------##

        if self.curtoken == self.ssbondtok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                if command == 'false' or command == 'off':
                    self._ssbonds()
                    print 'ssbonds off complete'
                elif command == 'true' or command == 'on' or command == '':
                    print 'Starting hbonds on:'
                    self._ssbonds()
                    print 'ssbonds on complete'
                else:
                    print 'That function is not supported by PyMOL'
            except:
                print '''ssbonds did not execute properly.
                Check spelling and implementation of this ssbonds command.'''
            return 0

        ##---------------Backbone--------------##

        if self.curtoken == self.backbonetok:
            try:
                commands = commands + ' '
                command = commands.split(' ', 1)[1].rstrip()
                cmd.set('ribbon_sampling', 20)
                cmd.set('ribbon_smooth', 1)
                cmd.set('ribbon_width', 0.02)
                if command == 'false' or command == 'off':
                    cmd.hide('ribbon' , self.vslselectionsaved)
                    print 'Backbone off complete'
                elif command == 'true' or command == 'on' or command == '':
                    cmd.show('ribbon', self.vslselectionsaved)
                    print 'Backbone on complete'
                elif command == 'dash':
                    print 'PyMOL does not include funcionality for this command.'
                elif float(command)>=0 and float(command)<=500:
                    if '.' in command:
                        command = float(command) * 5
                    else:
                        command = float(command)/50
                    cmd.show('ribbon' , self.vslselectionsaved)
                    cmd.set('ribbon_width', command)
                    print 'Backbone on complete'
                else:
                    print 'That function is not supported by PyMOL.'
            except:
                print 'An error occured while trying to display the backbone.'
            return 0

        ##---------------Monitor---------------##

        if self.curtoken == self.monitortok:
            try:
                parameters = commands.split(' ')
                if len(parameters) == 3:
                    cmd.distance('monitor', 'id %s' % parameters[1],
                        'id %s' % parameters[2])
                    if not self.set_monitor:
                        cmd.hide('labels' , self.vslselectionsaved)
                elif len(parameters) == 2:
                    command = parameters[1]
                    if command == 'false' or command == 'off':
                        cmd.hide('labels' , self.vslselectionsaved)
                        cmd.hide('dashes' , self.vslselectionsaved)
                        print 'Monitor off complete'
                    elif command == 'true' or command == 'on' or command == '':
                        pass
                    else:
                        print 'That function is not supported by PyMOL'
                else:
                    print 'That function is not supported by PyMOL'
            except:
                print 'An error occured while trying to display the labels.'
            return 0

        ##---------------Zap---------------##

        if self.curtoken == self.zaptok:
            print 'reinitialize'
            cmd.reinitialize()
            return 0

        ##---------------Stereo---------------##

        if self.curtoken == self.stereotok:
            tmpstring = commands.split()[1]
            if 'on' in tmpstring:
                cmd.stereo('on')
            elif 'off' in tmpstring:
                cmd.stereo('off')
            else:
                print 'That function is not supported by PyMOL.'
            return 0

        ##---------------Map---------------##

        if self.curtoken == self.maptok:
            try:
                parameters = commands[len(self.tokenident)+1:]
                self._mapsupport(parameters)
                return 0
            except:
                print 'An error occured with a map command.'

        ##---------------Set---------------##

        if self.curtoken == self.settok:
            try:
                parameters = commands[len(self.tokenident)+1:]
                self._set_parameters(parameters)
                return 0
            except:
                print 'An error occured with a set command.'

        ##---------------Refresh---------------##

        if 'refresh' in commands:
            print 'refresh'
            cmd.refresh()
            return 0

        ##---------------Reset---------------##

        if 'reset' in commands:
            print 'reset'
            cmd.reset()
            return 0

        ##---------------Define---------------##

        if self.curtoken == self.definetok:
            defparams = commands[len(self.tokenident)+1:].split(' ', 1)
            cmd.select(defparams[0], self._preselect(defparams[1]))
            self.userdefinedgroups[ defparams[0] ] =  defparams[1]
            return 0

        ##-------Quit/Exit/blank/comment------------##

        if self.curtoken == self.exittok or self.curtoken == self.quittok or\
            self.curtoken == 0:
            return self.curtoken

        ##---------------Not-Coded---------------##

        if commands.split(' ', 1)[0] in self.not_coded:
            print '''That command is not coded for using ConSCRIPT.
                Support for that function may be added at a later date.'''

        print commands
        print 'not implemented as a VSL command'
        return 0
CSC = ConSCRIPTConverter()

def __init__(self):
    '''************************'''
    self.menuBar.addmenuitem('Plugin', 'command',
                             'VSL Script Loader',
                             label = 'ConSCRIPT 2.0rc1',
                             command = vslcmd)

def vslcmd(commands=None, args=None, filename=None):
    '''Handler for SBEVSL commands'''
    if commands == None:
        if filename == None:
            filename = tkFileDialog.askopenfilename(initialdir=HOME,
                filetypes=[('RasMol Script', '.scr'),('Text Files', '.txt')], 
                title='ConSCRIPT (C)Copyright 2007-10 GPL No Warranty')
        if filename:
            fileobj = open(filename, 'rbU')
            for line in fileobj:
                CSC.handlecommand(line.rstrip())
            fileobj.close()
    else:
        if args == ():
            CSC.handlecommand(commands)
        else:
            CSC.handlecommand('%s %s' % (commands, ','.join(args).rstrip()))
            
def gettok(tok):
    '''return token of a command'''
    print CSC.gettok(tok)
#**cmd.extend('gettok', gettok)

def r(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def R(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def vsl(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def VSL(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def SBEVSL(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def sbevsl(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def RASMOL(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

def rasmol(commands, *args, **keys):
    '''************************'''
    vslcmd(commands, args)

cmd.extend('R', R)
cmd.extend('r', r)
cmd.extend('VSL', VSL)
cmd.extend('vsl', vsl)
cmd.extend('SBEVSL', SBEVSL)
cmd.extend('sbevsl', sbevsl)
cmd.extend('RASMOL', RASMOL)
cmd.extend('rasmol', rasmol)