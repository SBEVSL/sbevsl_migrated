# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 cindent:
# This file is formatted using spaces for indentation.
# 4 spaces = 1 "tab" or indent. Do NOT mix tab characters with spaces.
import Pmw
import pymol
from pymol import cmd
import Tkinter
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

    
## Global defintions

map_name = 0
map_type = 'gaussian'
map_grid = 1.0
map_level = 1.0
map_selection = 'VSLselection'
centerselection = '( all )'
zoomnum = 0
clip_dist_near = -50.0
clip_dist_far = 50.0
filestack = []
filelevel = 0
UserDefinedGroups = {}
VSLselection = "( all )"
VSLselectionsaved = "( all )"
VSLVerbose = 0
VSLenabled = False

### /* Lexeme Tokens */
IdentTok =      256
NumberTok =     257
FloatTok =      258
StringTok =     259

### /* Command Tokens */
AdviseTok =     260
BackboneTok =   261
CartoonTok =    262
CentreTok =     263
ClipboardTok =  264
ColourTok =     265
ColourModeTok = 609
ConcealTok  =   611
ConnectTok =    266
DashTok =       267
DefineTok =     268
DelayTok =      269
DepthTok =      270
DisplayTok =    271
EchoTok =       272
ExitTok =       273
GenerateTok =   274
HelpTok =       275
LabelTok =      276
LoadTok =       277
LoopTok =       278
MapTok =        279
MaskTok =       280
MoleculeTok =   281
MolSurfTok =    282 
MonitorTok =    283
MoveTok =       284
NoToggleTok =   610
PrintTok =      285
QuitTok =       286
RefreshTok =    287
RenumTok =      288
ResetTok =      289
ResizeTok =     290
RestoreTok =    291
RestrictTok =   292
RevealTok   =   612
RotateTok =     293
SaveTok =       294
ScriptTok =     295
SelectTok =     296
SetTok =        297
ShowTok =       298
SlabTok =       299
SourceTok =     300
SpacefillTok =  301
StarTok =       302
StructureTok =  303
SurfaceTok =    304
SymmetryTok =   305
TitleTok =      306
TraceTok =      307
TranslateTok =  308
ViewTok =       309
WaitTok =       310
WireframeTok =  311
WriteTok =      312
ZapTok =        313
ZoomTok =       314

### /* Predicate Tokens */

AlphaTok =      320
AminoTok =      321
ATTok =         322
BondedTok =     323
CGTok =         324
CystineTok =    325
DNATok =        326
HelixTok =      327
HeteroTok =     328
HydrogenTok =   329
IonTok =        330
LigandTok =     331
MainChainTok =  332
NucleicTok =    333
ProteinTok =    334
PurineTok =     335
PyrimidineTok = 336
RNATok =        337
SelectedTok =   338
SheetTok =      339
SidechainTok =  340
SolventTok =    341
TurnTok =       342
WaterTok =      343

AcidicTok =     344
AcyclicTok =    345
AliphaticTok =  346
AromaticTok =   347
BasicTok =      348
BuriedTok =     349
ChargedTok =    350
CisBondedTok =  351
CyclicTok =     352
HydrophobicTok =353
LargeTok =      354
MediumTok =     355
NeutralTok =    356
PolarTok =      357
SmallTok =      358



### /* Property Tokens */
TemperatureTok =360
RadiusTok =     361
AtomNoTok =     362
ElemNoTok =     363
ModelTok =      364
ResNoTok =      365
AltlTok =       366

### /* File Format Tokens */
### /* Warning! Tokens are related to Format values */

PDBTok =        370
MacroModelTok = 371
GaussianTok =   372
AlchemyTok =    373
NMRPDBTok =     374
CharmmTok =     375
BiosymTok =     376
MOPACTok =      377
SHELXTok =      378
Mol2Tok =       379
FDATTok =       380
MMDBTok =       381
MDLTok =        382
XYZTok =        383
CIFTok =        384
CEXTok =        385

### /* Raster Tokens */
GIFTok =        390
PPMTok =        391
SUNTok =        392
SUNRLETok =     393
EPSFTok =       394
PICTTok =       395
IRISTok =       396
BMPTok =        397
MonoPSTok =     398
JPEGTok =       399
PNGTok =        400
VectPSTok =     401
KinemageTok =   402
MolScriptTok =  403
POVRayTok =     404
POVRay2Tok =    404
POVRay3Tok =    405
VRMLTok =       406
Raster3DTok =   407
RamachanTok =   408  ### /* ok, this isn't a real image format ... */
RamPrintTok =   409
MirrorTok =     410

### /* Feature Tokens */
AtomTok =       421
BondTok =       422
DotsTok =       423
HBondTok =      424
RibbonTok =     425
SSBondTok =     426
Ribbon1Tok =    427
Ribbon2Tok =    428
UnBondTok =     429

### /* Expression Tokens */
TrueTok =       430
FalseTok =      431
AllTok =        432
NoneTok =       433
AndTok =        434
OrTok =         435
NotTok =        436
WithinTok =     437
XorTok =        438
MeanTok =       439
NextTok =       440
NewTok =        441

### /* Colour Tokens */
### /* Warning! Tokens are related to colour values */

BlackTok =      442
BlueTok =       443
BlueTintTok =   444
BrownTok =      445
CyanTok =       446
GoldTok =       447
GrayTok =       448
GreenTok =      449
GreenBlueTok =  450
GreenTintTok =  451
HotPinkTok =    452
MagentaTok =    453
OrangeTok =     454
PinkTok =       455
PinkTintTok =   456
PurpleTok =     457
RedTok =        458
RedOrangeTok =  459
SeaGreenTok =   460
SkyBlueTok =    461
VioletTok =     462
WhiteTok =      463
YellowTok =     464
YellowTintTok = 465

CPKTok =        466
ShapelyTok =    467
ResidueTok =    468
UserTok =       469
GroupTok =      470
ChainTok =      471
TypeTok =       472
PotentialTok =  473
ChargeTok =     474
CpkNewTok =     475

### /* Variable Tokens */
AmbientTok =    480
AxesTok =       481
BackFadeTok =   482
BackgroundTok = 483
BondModeTok =   484
BoundBoxTok =   485
CisAngleTok =   486
ContourTok =    487
DepthCueTok =   488
FontSizeTok =   489
FontStrokeTok = 490
HourGlassTok =  491
LevelTok =      ContourTok
MenusTok =      493
MouseTok =      494
PickingTok =    495
ResolutionTok = 496
ShadePowerTok = 497
ShadowTok =     498
SlabModeTok =   499
SpacingTok =    500
SpecularTok =   501
SpecPowerTok =  502
SpreadTok =     503
StrandsTok =    504
TransparentTok =505
UnitCellTok =   506
WidthTok =      SpreadTok

### /* SlabMode Tokens */
RejectTok =     510
HalfTok =       511
HollowTok =     512
SolidTok =      513
SectionTok =    514

### /* MouseMode Tokens */
RasMolTok =     520
InsightTok =    521
QuantaTok =     522
SybylTok =      523

### /* Information Tokens */
InfoTok =       524
SequenceTok =   525
VersionTok =    526
PhiPsiTok =     527

### /* Display Mode Tokens */
NormalTok =     528
StereoTok =     529
MonoTok =       530
HardwareTok =   531

### /* Axis Tokens */
XTok =          532
YTok =          533
ZTok =          534

### /* Picking Tokens */
IdentifyTok =   535
CoordTok =      536
DistanceTok =   537
AngleTok =      538
TorsionTok =    539
OriginTok =     540

### /* Misc Tokens */
InLineTok =     541
VDWTok =        542
HeaderTok =     543
CIFDataTok =    544
FSTok =         545
PSTok =         EPSFTok

### /* Clipboard Tokens */
ImageTok =      546
PositionTok =   547
CopyTok =       548
PasteTok =      549

### /* Language Tokens */
EnglishTok =    600
FrenchTok =     601
GermanTok =     602
ItalianTok =    603
SpanishTok =    604
RussianTok =    605
ChineseTok =    606
JapaneseTok =   607
BulgarianTok =  608


def IsPredTok( x ):
    if (((x)>=AlphaTok) and ((x)<=SmallTok)):
        return True
    else:
        return False
      
def PredTokOrd( x ):
     if  ((x)-AlphaTok):
        return True
     else:
        return False
        
def PredTokChr( x ):
     if ((x)+AlphaTok):
         return True
     else:
         return False

def IsPropTok( x ):
    if  (((x)>=TemperatureTok) and ((x)<=AltlTok)):
        return True
    else:
        return False

def IsColourToken( x ):
    if (((x)>=BlackTok) and ((x)<=YellowTintTok)):
        return True
    else:
        return False

def Token2Colour( x ):
    return  ((x)-BlackTok)

def IsImageToken( x ):
    if (((((x)>=GIFTok) and ((x)<=RamPrintTok)) or ((x) == PhiPsiTok))):
        return True
    else:
        return False

def IsMoleculeToken( x ):  
    if (((x)>=PDBTok) and ((x)<=CEXTok)):
        return True
    else:
        return False

VSLTok = {}

VSLTok["ACIDIC"] = AcidicTok
VSLTok["ACYCLIC"] = AcyclicTok 
VSLTok["ALCHEMY"] = AlchemyTok
VSLTok["ALIPHATIC"] = AliphaticTok
VSLTok["ALL"] = AllTok 
VSLTok["ALPHA"] = AlphaTok
VSLTok["ALT"] = AltlTok
VSLTok["AMBIENT"] = AmbientTok
VSLTok["AMINO"] = AminoTok
VSLTok["AND"] = AndTok
VSLTok["ANGLE"] = AngleTok
VSLTok["ANGLES"] = AngleTok
VSLTok["AROMATIC"] = AromaticTok
VSLTok["ASSE"] = AxesTok
VSLTok["ASSI"] = AxesTok
VSLTok["AT"] = ATTok
VSLTok["ATOM"] = AtomTok
VSLTok["ATOMNO"] = AtomNoTok
VSLTok["ATOMNUMBER"] = AtomNoTok
VSLTok["ATOMS"] = AtomTok
VSLTok["AXES"] = AxesTok
VSLTok["AXIS"] = AxesTok
VSLTok["AVERAGE"] = MeanTok
VSLTok["BACKBONE"] = BackboneTok
VSLTok["BACKFADE"] = BackFadeTok
VSLTok["BACKGROUND"] = BackgroundTok
VSLTok["BASIC"] = BasicTok
VSLTok["BIOSYM"] = BiosymTok
VSLTok["BLACK"] = BlackTok
VSLTok["BLUE"] = BlueTok
VSLTok["BLUETINT"] = BlueTintTok
VSLTok["BMP"] = BMPTok
VSLTok["BOND"] = BondTok
VSLTok["BONDED"] = BondedTok
VSLTok["BONDMODE"] = BondModeTok
VSLTok["BONDS"] = BondTok
VSLTok["BOUNDBOX"] = BoundBoxTok
VSLTok["BOUNDINGBOX"] = BoundBoxTok
VSLTok["BROWN"] = BrownTok
VSLTok["BURIED"] = BuriedTok
VSLTok["CADENA"] = ChainTok
VSLTok["CADENAS"] = ChainTok
VSLTok["CARTOON"] = CartoonTok
VSLTok["CARTOONS"] = CartoonTok
VSLTok["CATENA"] = ChainTok
VSLTok["CATENE"] = ChainTok
VSLTok["CENTER"] = CentreTok
VSLTok["CENTRE"] = CentreTok
VSLTok["CEX"] = CEXTok
VSLTok["CG"] = CGTok
VSLTok["CHAIN"] = ChainTok
VSLTok["CHAINS"] = ChainTok
VSLTok["CHARGE"] = ChargeTok
VSLTok["CHARGED"] = ChargedTok
VSLTok["CHARGES"] = ChargeTok
VSLTok["CHARMM"] = CharmmTok
VSLTok["CHINESE"] = ChineseTok
VSLTok["CIF"] = CIFTok
VSLTok["CISANGLE"] = CisAngleTok
VSLTok["CISBONDED"] = CisBondedTok
VSLTok["CLIPBOARD"] = ClipboardTok
VSLTok["COLOR"] = ColourTok
VSLTok["COLORMODE"] = ColourModeTok
VSLTok["COLORS"] = ColourTok
VSLTok["COLOUR"] = ColourTok
VSLTok["COLOURMODE"] = ColourModeTok
VSLTok["COLOURS"] = ColourTok
VSLTok["CONCEAL"] = ConcealTok
VSLTok["CONNECT"] = ConnectTok
VSLTok["CONTOUR"] = ContourTok
VSLTok["COORDINATE"] = CoordTok
VSLTok["COORDINATES"] = CoordTok
VSLTok["COORD"] = CoordTok
VSLTok["COORDS"] = CoordTok
VSLTok["COPY"] = CopyTok
VSLTok["CPK"] = CPKTok
VSLTok["CPKNEW"] = CpkNewTok
VSLTok["CYAN"] = CyanTok
VSLTok["CYCLIC"] = CyclicTok
VSLTok["CYSTINE"] = CystineTok
VSLTok["DASH"] = DashTok
VSLTok["DASHES"] = DashTok
VSLTok["DATA_"] = CIFDataTok
VSLTok["DEFINE"] = DefineTok
VSLTok["DEPTH"] = DepthTok
VSLTok["DEPTHCUE"] = DepthCueTok
VSLTok["DIBUJO"] = CartoonTok
VSLTok["DIBUJOS"] = CartoonTok
VSLTok["DISPLAY"] = DisplayTok
VSLTok["DISTANCE"] = DistanceTok
VSLTok["DISTANCES"] = DistanceTok
VSLTok["DNA"] = DNATok
VSLTok["DOTS"] = DotsTok
VSLTok["E"] = AndTok
VSLTok["ECHO"] = EchoTok
VSLTok["EJE"] = AxesTok
VSLTok["EJES"] = AxesTok
VSLTok["ELANCE"] = BondTok
VSLTok["ELANCES"] = BondTok
VSLTok["ELEMNO"] = ElemNoTok
VSLTok["ELEMENTNUMBER"] = ElemNoTok
VSLTok["ELICHE"] = HelixTok
VSLTok["ENGLISH"] = EnglishTok
VSLTok["EPSF"] = EPSFTok
VSLTok["ELICHE"] = HelixTok
VSLTok["ESQUELETO"] = BackboneTok
VSLTok["ETIQUETA"] = LabelTok
VSLTok["ETIQUETAS"] = LabelTok
VSLTok["ETICHETTA"] = LabelTok
VSLTok["ETICHETTE"] = LabelTok  
VSLTok["EXIT"] = ExitTok
VSLTok["FALSE"] = FalseTok
VSLTok["FDAT"] = FDATTok
VSLTok["FILODIFERRO"] = WireframeTok
VSLTok["FILDIFERRO"] = WireframeTok
VSLTok["FILI"] = StrandsTok  
VSLTok["FONTSIZE"] = FontSizeTok
VSLTok["FONTSTROKE"] = FontStrokeTok
VSLTok["FRENCH"] = FrenchTok
VSLTok["FS"] = FSTok
VSLTok["GAUSSIAN"] = GaussianTok
VSLTok["GENERATE"] = GenerateTok   
VSLTok["GIF"] = GIFTok
VSLTok["GIRO"] = TurnTok
VSLTok["GIROS"] = TurnTok
VSLTok["GOLD"] = GoldTok
VSLTok["GRAY"] = GrayTok
VSLTok["GREEN"] = GreenTok
VSLTok["GREENBLUE"] = GreenBlueTok
VSLTok["GREENTINT"] = GreenTintTok
VSLTok["GREY"] = GrayTok
VSLTok["GROUP"] = GroupTok
VSLTok["GRUPO"] = GroupTok
VSLTok["GRUPPO"] = GroupTok 
VSLTok["HALF"] = HalfTok
VSLTok["HARDWARE"] = HardwareTok
VSLTok["HBOND"] = HBondTok
VSLTok["HBONDS"] = HBondTok
VSLTok["HEADER"] = HeaderTok
VSLTok["HEBRAS"] = StrandsTok
VSLTok["HELICES"] = HelixTok
VSLTok["HELIX"] = HelixTok
VSLTok["HELP"] = HelpTok
VSLTok["HETERO"] = HeteroTok
VSLTok["HOLLOW"] = HollowTok
VSLTok["HOTPINK"] = HotPinkTok
VSLTok["HOURGLASS"] = HourGlassTok
VSLTok["HYDROGEN"] = HydrogenTok
VSLTok["HYDROPHOBIC"] = HydrophobicTok
VSLTok["IDENT"] = IdentifyTok
VSLTok["IDENTIFY"] = IdentifyTok
VSLTok["IMAGE"] = ImageTok
VSLTok["INFO"] = InfoTok
VSLTok["INFORMATION"] = InfoTok
VSLTok["INLINE"] = InLineTok
VSLTok["INSIGHT"] = InsightTok
VSLTok["ION"] = IonTok
VSLTok["IONS"] = IonTok
VSLTok["IRIS"] = IRISTok
VSLTok["ITALIAN"] = ItalianTok
VSLTok["JAPANESE"] = JapaneseTok
VSLTok["JPEG"] = JPEGTok
VSLTok["KINEMAGE"] = KinemageTok
VSLTok["LABEL"] = LabelTok
VSLTok["LABELS"] = LabelTok
VSLTok["LARGE"] = LargeTok
VSLTok["LEVEL"] = LevelTok
VSLTok["LIGAND"] = LigandTok
VSLTok["LIGANDS"] = LigandTok
VSLTok["LOAD"] = LoadTok
VSLTok["MACROMODEL"] = MacroModelTok
VSLTok["MAGENTA"] = MagentaTok
VSLTok["MAINCHAIN"] = MainChainTok
VSLTok["MAP"] = MapTok
VSLTok["MASK"] = MaskTok
VSLTok["MDL"] = MDLTok
VSLTok["MEAN"] = MeanTok
VSLTok["MEDIUM"] = MediumTok
VSLTok["MENUS"] = MenusTok
VSLTok["MESH"] = WireframeTok
VSLTok["MIRROR"] = MirrorTok
VSLTok["MMDB"] = MMDBTok
VSLTok["MODEL"] = ModelTok
VSLTok["MOL2"] = Mol2Tok
VSLTok["MOLECULE"] = MoleculeTok
VSLTok["MOLSCRIPT"] = MolScriptTok
VSLTok["MOLSURF"] = MolSurfTok
VSLTok["MONITOR"] = MonitorTok
VSLTok["MONITORS"] = MonitorTok
VSLTok["MONO"] = MonoTok
VSLTok["MONOCHROME"] = MonoTok
VSLTok["MONOPS"] = MonoPSTok
VSLTok["MOPAC"] = MOPACTok
VSLTok["MOSTRAR"] = DisplayTok
VSLTok["MOUSE"] = MouseTok
VSLTok["MOUSEMODE"] = MouseTok
VSLTok["NASTRO"] = RibbonTok 
VSLTok["NASTRI"] = RibbonTok 
VSLTok["NEGATIVE"] = AcidicTok
VSLTok["NEW"] = NewTok
VSLTok["NEUTRAL"] = NeutralTok
VSLTok["NEXT"] = NextTok
VSLTok["NMRPDB"] = NMRPDBTok
VSLTok["NONE"] = NoneTok
VSLTok["NORMAL"] = NormalTok
VSLTok["NOT"] = NotTok
VSLTok["NOTOGGLE"] = NoToggleTok
VSLTok["NUCLEIC"] = NucleicTok
VSLTok["OFF"] = FalseTok
VSLTok["ON"] = TrueTok
VSLTok["OR"] = OrTok
VSLTok["ORANGE"] = OrangeTok
VSLTok["ORIGIN"] = OriginTok
VSLTok["PASTE"] = PasteTok
VSLTok["PAUSE"] = WaitTok
VSLTok["PDB"] = PDBTok
VSLTok["PHIPSI"] = PhiPsiTok
VSLTok["PICK"] = PickingTok
VSLTok["PICKING"] = PickingTok
VSLTok["PICT"] = PICTTok
VSLTok["PINK"] = PinkTok
VSLTok["PINKTINT"] = PinkTintTok
VSLTok["PNG"] = PNGTok
VSLTok["POLAR"] = PolarTok
VSLTok["POSITIVE"] = BasicTok
VSLTok["POSITION"] = PositionTok
VSLTok["POTENTIAL"] = PotentialTok
VSLTok["POVRAY"] = POVRayTok
VSLTok["POVRAY2"] = POVRay2Tok
VSLTok["POVRAY3"] = POVRay3Tok
VSLTok["PPM"] = PPMTok
VSLTok["PRINT"] = PrintTok
VSLTok["PROTEIN"] = ProteinTok
VSLTok["PS"] = EPSFTok
VSLTok["PURINE"] = PurineTok
VSLTok["PURINES"] = PurineTok
VSLTok["PURPLE"] = PurpleTok
VSLTok["PYRIMIDINE"] = PyrimidineTok
VSLTok["PYRIMIDINES"] = PyrimidineTok
VSLTok["QUANTA"] = QuantaTok
VSLTok["QUIT"] = QuitTok
VSLTok["R3D"] = Raster3DTok
VSLTok["RADIUS"] = RadiusTok
VSLTok["RAMACHAN"] = RamachanTok
VSLTok["RAMACHANDRANDATAFILE"] = RamachanTok
VSLTok["RAMACHANDRANPRINTERPLOT"] = RamPrintTok
VSLTok["RAMDATA"] = RamachanTok
VSLTok["RAMPRINT"] = RamPrintTok
VSLTok["RASMAC"] = RasMolTok
VSLTok["RASMOL"] = RasMolTok
VSLTok["RASTER3D"] = Raster3DTok
VSLTok["RASWIN"] = RasMolTok
VSLTok["RDF"] = RamachanTok
VSLTok["RED"] = RedTok
VSLTok["REDORANGE"] = RedOrangeTok
VSLTok["REFRESH"] = RefreshTok
VSLTok["REJECT"] = RejectTok
VSLTok["RENUM"] = RenumTok
VSLTok["RENUMBER"] = RenumTok
VSLTok["RESET"] = ResetTok
VSLTok["RESIDUE"] = ResidueTok
VSLTok["RESIDUENUMBER"] = ResNoTok
VSLTok["RESIZE"] = ResizeTok
VSLTok["RESNO"] = ResNoTok
VSLTok["RESOLUTION"] = ResolutionTok
VSLTok["RESTRICT"] = RestrictTok
VSLTok["REVEAL"] = RevealTok
VSLTok["RGB"] = IRISTok
VSLTok["RIBBON"] = RibbonTok
VSLTok["RIBBON1"] = Ribbon1Tok
VSLTok["RIBBON2"] = Ribbon2Tok
VSLTok["RIBBONS"] = RibbonTok
VSLTok["RIBBONS1"] = Ribbon1Tok
VSLTok["RIBBONS2"] = Ribbon2Tok
VSLTok["RIEMPIMENTO"] = SpacefillTok
VSLTok["RNA"] = RNATok
VSLTok["ROT"] = RotateTok
VSLTok["ROTATE"] = RotateTok
VSLTok["ROTATION"] = RotateTok
VSLTok["RPP"] = RamPrintTok
VSLTok["SALIR"] = ExitTok
VSLTok["SAVE"] = SaveTok
VSLTok["SCHELETRO"] = BackboneTok
VSLTok["SCRIPT"] = ScriptTok
VSLTok["SECTION"] = SectionTok
VSLTok["SEAGREEN"] = SeaGreenTok
VSLTok["SELECT"] = SelectTok
VSLTok["SELECTED"] = SelectedTok
VSLTok["SELECTION"] = SelectedTok
VSLTok["SEQUENCE"] = SequenceTok
VSLTok["SET"] = SetTok
VSLTok["SHADEPOWER"] = ShadePowerTok
VSLTok["SHADOW"] = ShadowTok
VSLTok["SHADOWS"] = ShadowTok
VSLTok["SHAPELY"] = ShapelyTok
VSLTok["SHEET"] = SheetTok
VSLTok["SHEETS"] = SheetTok
VSLTok["SHELX"] = SHELXTok
VSLTok["SHOW"] = ShowTok
VSLTok["SIDECHAIN"] = SidechainTok
VSLTok["SKYBLUE"] = SkyBlueTok
VSLTok["SLAB"] = SlabTok
VSLTok["SLABMODE"] = SlabModeTok
VSLTok["SMALL"] = SmallTok
VSLTok["SOLID"] = SolidTok
VSLTok["SOLVENT"] = SolventTok
VSLTok["SOLVENTS"] = SolventTok
VSLTok["SOURCE"] = SourceTok
VSLTok["SPACEFILL"] = SpacefillTok
VSLTok["SPACING"] = SpacingTok
VSLTok["SPANISH"] = SpanishTok
VSLTok["SPECPOWER"] = SpecPowerTok
VSLTok["SPECULAR"] = SpecularTok
VSLTok["SPREAD"] = SpreadTok
VSLTok["SSBOND"] = SSBondTok
VSLTok["SSBONDS"] = SSBondTok
VSLTok["STAR"] = StarTok
VSLTok["STARS"] = StarTok
VSLTok["STEREO"] = StereoTok
VSLTok["STRANDS"] = StrandsTok
VSLTok["STRUCTURE"] = StructureTok
VSLTok["SUN"] = SUNTok
VSLTok["SUNRLE"] = SUNRLETok
VSLTok["SURFACE"] = SurfaceTok
VSLTok["SYBYL"] = SybylTok
VSLTok["SYMMETRY"] = SymmetryTok
VSLTok["TEMPERATURE"] = TemperatureTok
VSLTok["TITLE"] = TitleTok
VSLTok["TODO"] = AllTok
VSLTok["TORSION"] = TorsionTok
VSLTok["TORSIONS"] = TorsionTok
VSLTok["TRACE"] = TraceTok
VSLTok["TRANSLATE"] = TranslateTok
VSLTok["TRANSLATION"] = TranslateTok
VSLTok["TRANSPARENT"] = TransparentTok
VSLTok["TRUE"] = TrueTok
VSLTok["TURN"] = TurnTok
VSLTok["TURNS"] = TurnTok
VSLTok["TUTTO"] = AllTok 
VSLTok["TYPE"] = TypeTok
VSLTok["UNBOND"] = UnBondTok
VSLTok["UNITCELL"] = UnitCellTok
VSLTok["USER"] = UserTok
VSLTok["VDW"] = VDWTok
VSLTok["VECTPS"] = VectPSTok
VSLTok["VIEW"] = ViewTok
VSLTok["VIGNETTA"] = CartoonTok
VSLTok["VIOLET"] = VioletTok
VSLTok["VISUALIZZA"] = DisplayTok 
VSLTok["VRML"] = VRMLTok
VSLTok["WAIT"] = WaitTok
VSLTok["WATER"] = WaterTok
VSLTok["WATERS"] = WaterTok
VSLTok["WHITE"] = WhiteTok
VSLTok["WIDTH"] = WidthTok
VSLTok["WIREFRAME"] = WireframeTok
VSLTok["WITHIN"] = WithinTok
VSLTok["WRITE"] = WriteTok
VSLTok["X"] = XTok
VSLTok["XYZ"] = XYZTok
VSLTok["Y"] = YTok
VSLTok["YELLOW"] = YellowTok
VSLTok["YELLOWTINT"] = YellowTintTok
VSLTok["Z"] = ZTok
VSLTok["ZAP"] = ZapTok
VSLTok["ZOOM"] = ZoomTok


ErrSyntax   =    0
ErrBigNum   =    1
ErrBadOpt   =    2
ErrParam    =    3
ErrFilNam   =    4
ErrBadLoad  =    5
ErrNotNum   =    6
ErrNotSep   =    7
ErrNotBrac  =    8
ErrNoCol    =    9
ErrColour   =   10
ErrBadArg   =   11
ErrBadExpr  =   12
ErrParen    =   13
ErrScript   =   14
ErrFunc     =   15
ErrSetName  =   16
ErrBadSet   =   17
ErrInScrpt  =   18
ErrOutScrpt =   19
ErrBadMolDB =   20
ErrNoBond   =   21
ErrBlocSel  =   22

MsgStrs = {}

MsgStrs[ErrSyntax]  = "Invalid command syntax!"
MsgStrs[ErrBigNum]  = "Parameter value too large!"
MsgStrs[ErrBadOpt]  = "Invalid parameter setting!"
MsgStrs[ErrParam]  = "Invalid parameter name!"
MsgStrs[ErrFilNam]  = "Filename string expected!"
MsgStrs[ErrBadLoad]  = "Molecule database loaded!"
MsgStrs[ErrNotNum]  = "Integer value expected!"
MsgStrs[ErrNotSep]  = "Comma separator missing!"
MsgStrs[ErrNotBrac]  = "Close bracket ']' expected!"
MsgStrs[ErrNoCol]  = "No colour specified!"
MsgStrs[ErrColour]  = "Unknown or incorrect colour!"
MsgStrs[ErrBadArg]  = "Invalid command argument!"
MsgStrs[ErrBadExpr]  = "Syntax error in expression!"
MsgStrs[ErrParen]  = "Close parenthesis ')' expected!"
MsgStrs[ErrScript]  = "Script command stack too deep!"
MsgStrs[ErrFunc]  = "Open parenthesis '(' expected!"
MsgStrs[ErrSetName]  = "Invalid or missing atom set name!"
MsgStrs[ErrBadSet]  = "Not enough memory to define set!"
MsgStrs[ErrInScrpt]  = "Command disabled in script file!"
MsgStrs[ErrOutScrpt]  = "Command invalid (valid only within a script)!"
MsgStrs[ErrBadMolDB]  = "Molecule database not loaded!"
MsgStrs[ErrNoBond]  = "Bond for rotation not picked!"


VSLColourTable = {}

VSLColourTable[BlackTok] =      [   0/255.,   0/255.,   0/255. ]
VSLColourTable[BlueTok] =       [   0/255.,   0/255., 255/255. ]
VSLColourTable[BlueTintTok] =   [ 175/255., 214/255., 255/255. ]
VSLColourTable[BrownTok] =      [ 175/255., 117/255.,  89/255. ]
VSLColourTable[CyanTok] =       [   0/255., 255/255., 255/255. ]
VSLColourTable[GoldTok] =       [ 255/255., 156/255.,   0/255. ]
VSLColourTable[GrayTok] =       [ 125/255., 125/255., 125/255. ]
VSLColourTable[GreenTok] =      [   0/255., 255/255.,   0/255. ]
VSLColourTable[GreenBlueTok] =  [  46/255., 139/255.,  87/255. ]
VSLColourTable[GreenTintTok] =  [ 152/255., 255/255., 179/255. ]
VSLColourTable[HotPinkTok] =    [ 255/255.,   0/255., 101/255. ]
VSLColourTable[MagentaTok] =    [ 255/255.,   0/255., 255/255. ]
VSLColourTable[OrangeTok] =     [ 255/255., 165/255.,   0/255. ]
VSLColourTable[PinkTok] =       [ 255/255., 101/255., 117/255. ]
VSLColourTable[PinkTintTok] =   [ 255/255., 171/255., 187/255. ]
VSLColourTable[PurpleTok] =     [ 160/255.,  32/255., 240/255. ]
VSLColourTable[RedTok] =        [ 255/255.,   0/255.,   0/255. ]
VSLColourTable[RedOrangeTok] =  [ 255/255.,  69/255.,   0/255. ]
VSLColourTable[SeaGreenTok] =   [   0/255., 250/255., 109/255. ]
VSLColourTable[SkyBlueTok] =    [  58/255., 144/255., 255/255. ]
VSLColourTable[VioletTok] =     [ 238/255., 130/255., 238/255. ]
VSLColourTable[WhiteTok] =      [ 255/255., 255/255., 255/255. ]
VSLColourTable[YellowTok] =     [ 255/255., 255/255.,   0/255. ]
VSLColourTable[YellowTintTok] = [ 246/255., 246/255., 117/255. ]

VSLCPKTable = {}

VSLCPKTable[0] =   "[ .7843, .7843, .7843 ]" #/*  0 Light Grey   */
VSLCPKTable[1] =   "[ .5607, .5607, 1.    ]" #/*  1 Sky Blue     */
VSLCPKTable[2] =   "[ .9411, 0.,    0.    ]" #/*  2 Red          */
VSLCPKTable[3] =   "[ 1.,    .7843, .1960 ]" #/*  3 Yellow       */
VSLCPKTable[4] =   "[ 1.,    1.,    1.    ]" #/*  4 White        */
VSLCPKTable[5] =   "[ 1.,    .7529, .7960 ]" #/*  5 Pink         */
VSLCPKTable[6] =   "[ .8549, .6470, .1254 ]" #/*  6 Golden Rod   */
VSLCPKTable[7] =   "[ 0.,    0.,    1.    ]" #/*  7 Blue         */
VSLCPKTable[8] =   "[ 1.,    .6470, 0.    ]" #/*  8 Orange       */
VSLCPKTable[9] =   "[ .5019, .5019, .5647 ]" #/*  9 Dark Grey    */
VSLCPKTable[10] =  "[ .6470, .1647, .1647 ]" #/* 10 Brown        */
VSLCPKTable[11] =  "[ .6274, .1254, .9411 ]" #/* 11 Purple       */
VSLCPKTable[12] =  "[ 1.,    .0784, .5764 ]" #/* 12 Deep Pink    */
VSLCPKTable[13] =  "[ 0.,    1.,    0.    ]" #/* 13 Green        */
VSLCPKTable[14] =  "[ .6980, .1333, .1333 ]" #/* 14 Fire Brick   */
VSLCPKTable[15] =  "[ .1333, .5450, .1333 ]" #/* 15 Forest Green */




def LookUpKeyword( kw ):
    if kw.upper() in VSLTok:
      return VSLTok[ kw.upper() ]
    else:
      return IdentTok
      
##  Command Line Lexical Analysis  */

def IsIdentChar( c ):
    if c.isalnum() or c=='$' or c== '_' :
      return True
    else:
      return False

def VSLFetchToken( p, baseTokenPtr):
    TokenPtr = baseTokenPtr
    TokenStart = TokenPtr
    CurToken = 0
    TokenIdent = ""
    TokenValue = 0
    if TokenPtr >= len(p):
        ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
        return (TokenPtr, 0, TokenStart, TokenIdent, TokenValue)
    while TokenPtr < len(p) :
        ch =  p[TokenPtr:TokenPtr+1]
        if not ch.isspace() :
            break
        TokenPtr = TokenPtr+1
    TokenStart = TokenPtr
    ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
    if TokenPtr < len(p) :
        ch = p[TokenPtr]
        ### debug: print 'Starting scan with ch ='+ch
        if ch == '#' :
            ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
            return (TokenPtr, 0, TokenStart, TokenIdent, TokenValue)
        TokenPtr = TokenPtr+1
        if  ch.isalpha() :
             ### debug: print ' First character is alpha'
             TokenLength = 1
             TokenIdentL = []
             TokenIdentL.append(ch.upper())
             while IsIdentChar(p[TokenPtr])==True and TokenLength < 32 :
                 ch = p[TokenPtr]
                 TokenPtr = TokenPtr+1
                 TokenIdentL.append(ch.upper())
                 TokenLength = TokenLength+1
                 if TokenPtr >= len(p):
                     break
             if TokenLength==32 :
                 ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
                 return (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
             else:
                 TokenIdent = ''.join(TokenIdentL)
                 CurToken = LookUpKeyword(TokenIdent)
                 ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
                 return (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
        elif ch.isdigit() :
            ### debug: print ' First character is digit '
            TokenValue = int(ch)
            while TokenPtr < len(p):
                ch = p[TokenPtr]
                if ch == '#' or not ch.isdigit():
                    break
                TokenPtr = TokenPtr+1
                TokenValue = 10*TokenValue + int(ch)
            CurToken = NumberTok
            ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
            return (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
        elif  (ch=='\'') or (ch=='\"') or (ch=='`') :
            ### debug: print ' First character is quot '
            TokenLength = 0
            TokenIdentL = []
            TokenIdentL.append(ch)
            while  (TokenPtr < len(p)) and (TokenLength<128) and (p[TokenPtr]!=ch) :
                TokenIdentL.append(p[TokenPtr])
                TokenPtr = TokenPtr+1
            if ch != p[TokenPtr] :
                ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
                return (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
            else:
                TokenPtr = TokenPtr+1
                TokenIdent = ''.join(TokenIdentL)
                CurToken = StringTok
                ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
                return (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
        else :
            CurToken = -ord(ch)
            ### debug:  print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
            return (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
    ### debug: print 'CurToken, TokenPtr, TokenStart ' + str(CurToken) + ' '+str(TokenPtr)+' '+str(TokenStart)
    return (TokenPtr, 0, TokenStart, TokenIdent, TokenValue)


def VSLNextIf( tok, err, p, TokenPtr ) :

    ### debug: print 'VSLNextIf TokenPtr, p ' + str(TokenPtr) + ' ' +p
    (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr) 
    if CurToken != tok :
       print MsgStrs[err]
       return (True,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)
    else:
       return (False, TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue)


def VSLParseColour( p, baseTokenPtr, baseCurToken ):


    TokenPtr = baseTokenPtr
    CurToken = baseCurToken
    ### debug: print 'VSLParseColour TokenPtr, CurToken, p ' + str(TokenPtr) + ' ' +str(CurToken) + ' ' + p
    
    if IsColourToken(CurToken) == True :
        rgb = VSLColourTable[CurToken]        
        ### debug: print ' rgb '+str(rgb)
        return (True, rgb)

    elif  CurToken == -ord('[') :
        rgb = [0., 0., 0.]

        (result,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLNextIf(NumberTok, ErrNotNum, p, TokenPtr)
        if result==True :
            return (False, rgb)
        else:
            if TokenValue > 255:
                print MsgStrs[ErrBigNum]
                return (False, rgb)
            else:
                RVal = TokenValue
                
        (result,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLNextIf(-ord(','), ErrNotSep, p, TokenPtr)
        if result==True :
            return (False, rgb)

        (result,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLNextIf(NumberTok, ErrNotNum, p, TokenPtr)
        if result==True :
            return (False, rgb)
        else:
            if TokenValue > 255:
                print MsgStrs[ErrBigNum]
                return (False, rgb)
            else:
                GVal = TokenValue

        (result,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLNextIf(-ord(','), ErrNotSep, p, TokenPtr)
        if result==True :
            return (False, rgb)

        (result,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLNextIf(NumberTok, ErrNotNum, p, TokenPtr)
        if result==True :
            return (False, rgb)
        else:
            if TokenValue > 255:
                print MsgStrs[ErrBigNum]
                return (False, rgb)
            else:
                BVal = TokenValue

        (result,  TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLNextIf(-ord(']'), ErrNotBrac, p, TokenPtr)
        if result==True :
            return (False, rgb)
        else:
            rgb = []
            rgb.append(RVal/255.)
            rgb.append(GVal/255.)
            rgb.append(BVal/255.)
            return (True, rgb)
            
    else:
        return (False, [0., 0., 0.])
        
    ### Warning, need to hook to locally named colors
    



Pmw.initialise()

#Add it to the PyMOL menu Bar
def __init__(self):
    """Add a ConSCRIPT menu to the tcl/tk GUI"""
    self.menuBar.addmenuitem('Plugin', 'command',
                             'VSL Script Loader',
                             label = 'ConSCRIPT',    
                             command = lambda s=self : csDialog(s))

class csDialog:
    """Create a Tk GUI Dialog for ConSCRIPT options"""
    def __init__(self, app):
        """Initialize the Tk GUI"""
        global VSLenabled

        # create the dialog box which contains the GUI
        self.parent = app.root
        self.dialog = Pmw.Dialog(self.parent, title = 'ConSCRIPT')
        
        # set the size of the 
        #self.dialog.geometry('550x550')
        self.interior = self.dialog.interior()
            
        #TITLE BAR
        self.lab = Tkinter.Label(self.interior, 
            text='ConSCRIPT (C) Copyright 2007-2008\nS. Mottarella, P. Craig, H. Bernstein\nGPL, No Warranty', 
            background='#000066', foreground='white')
                        
        self.lab.pack(expand=0, fill='x', padx=4, pady=0)
	    #Makes pages possible
        self.notebook = Pmw.NoteBook(self.interior)
        self.notebook.pack(fill='both', expand=1, padx=10, pady=10)

        self.page = self.notebook.add('VSL Script Loader')
        self.notebook.tab('VSL Script Loader').focus_set()
        self.group = Pmw.Group(self.page, tag_text = ' SBEVSL ')
        self.group.grid(row=0, column=0, padx=0, pady=0)
        self.interior = self.group.interior()
                
        # Open Script button
        self.btnOpen = Tkinter.Button(self.interior, text = 'Open Script',
                command=self.btnOpen_clicked)
        self.btnOpen.grid()
        
        self.pagecmd = self.notebook.add('VSL Command Enable')
        self.notebook.tab('VSL Command Enable').focus_set()
        self.groupcmd = Pmw.Group(self.pagecmd, tag_text = ' SBEVSL ')
        self.groupcmd.grid(row=0, column=0, padx=0, pady=0)
        self.interiorcmd = self.groupcmd.interior()
                
        # Enable VSL button
        # here I replaced the button with a checkbutton (checkbox) and
        # disguised it as a button for a similar appearance. - GM
        self.chkEnableVSL = Tkinter.Checkbutton(self.interiorcmd, text = 'Enable VSL',
				indicatoron=False, padx=10, pady=4,
                command=self.chkEnableVSL_clicked)
        if VSLenabled == True:
            # set the text. here we're disabling it just termporarily
            # until we've found a method to 'unextend' the pymol commands.
            self.chkEnableVSL.config(text='VSL Enabled', state=Tkinter.DISABLED)
            self.chkEnableVSL.select()
        self.chkEnableVSL.grid()


    #Define the Boffo Function
    def btnOpen_clicked(self):
        """Open an SBEVSL script"""
    
        global filelevel
        global filestack

        try:
            Q = tkFileDialog.askopenfilename()
            filelevel = 0
            filestack = []
            donext = processVSLscript(Q)
            if donext == QuitTok:
                cmd.quit()
        except:
            print 'An unknown exception occurred while opening file.'

    #Define the Boffocmd Function
    def chkEnableVSL_clicked(self):
        """Enable the use of the 'VSL' command on the command line"""
        global VSLenabled

        print 'VSLenabled', VSLenabled

        if VSLenabled == False:
            cmd.extend('VSL', VSL)
            cmd.extend('vsl', VSL)
            cmd.extend('SBEVSL', VSL)
            cmd.extend('sbevsl', VSL)
            VSLenabled = True

            self.chkEnableVSL.config(text="VSL Enabled.", state=Tkinter.DISABLED)
            #interiorcmd.mainloop()
            #Reset the GUI
            #interior.mainloop()
        else:
            pass
            # disabled it for now since there's no working code here
            # TODO: Disable VSL somehow.
        
##---Apply Color to Selection--##
def apply_color(rgbcolor, selection):
    sc = rgbcolor
    sc = sc.replace(' ','')
    cmd.set_color("vslc_"+sc,rgbcolor)
    cmd.color("vslc_"+sc,selection)
    return

##-----Color CPK-----------##
def color_cpk( selection ):
    global VSLCPKTable
    colstr = ' and ( ' + selection + ')'
    apply_color(VSLCPKTable[12],  selection)
    apply_color(VSLCPKTable[4],  "(elem H)" + colstr)
    apply_color(VSLCPKTable[14], "(elem He)" + colstr)
    apply_color(VSLCPKTable[13], "(elem He)" + colstr)
    apply_color(VSLCPKTable[0],  "(elem C)" + colstr)
    apply_color(VSLCPKTable[1],  "(elem N)" + colstr)
    apply_color(VSLCPKTable[2],  "(elem O)" + colstr)
    apply_color(VSLCPKTable[6],  "(elem Au+F+Si)" + colstr)
    apply_color(VSLCPKTable[7],  "(elem Na)" + colstr)
    apply_color(VSLCPKTable[15], "(elem Mg)" + colstr)
    apply_color(VSLCPKTable[9],  "(elem Ca+Mn+Al+Ti+Cr+Ag)" + colstr )
    apply_color(VSLCPKTable[8],  "(elem P+Fe+Ba)" + colstr)
    apply_color(VSLCPKTable[3],  "(elem S)" + colstr)
    apply_color(VSLCPKTable[11], "(elem I)" + colstr)
    apply_color(VSLCPKTable[10], "(elem Br+Zn+Cu+Ni)" + colstr)
    return



##-----Select Function-----##
def select( allparameters ):

    global UserDefinedGroups

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
                       'selected': ' VSLselection ',
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

## Handles all map commands
def mapsupport( parameters ):
    parameterslist = parameters.split( ' ' )
    try:
        if int(parameterslist[0]):
            print 'You gave a number. The Count says "Good Job!"'
            handlemap( parameterslist[1:] )
    except:
        print 'Map command'
        handlemap( parameterslist )

## Handles all map commands.
def handlemap( parameterslist ):
    goodlist = ['generate', 'level']
    badlist = ['load', 'mask', 'resolution', 'restrict', 'save', 'select', 'show', 'spacing', 'spread', 'zap']
    global map_name, map_type, map_grid, map_level, map_selection, centerselection, zoomnum
    try:
        if parameterslist[0] in goodlist:
            if parameterslist[0] == 'generate':
                if parameterslist[1] == 'mesh':
                    cmd.do( 'map_new ' + str(map_name)+ ', ' + map_type + ', ' + str(map_grid) + ', ' + map_selection )
                    cmd.do( 'isomesh mesh_' + str(map_name) + ', ' + str(map_name) + ', ' + str(map_level) )
                    map_name += 1
                    cmd.do( 'zoom ' + centerselection + ', ' + str(zoomnum) )
                    print 'Mesh map complete'
                elif parameterslist[1] == 'dots':
                    cmd.do( 'map_new ' + str(map_name)+ ', ' + map_type + ', ' + str(map_grid) + ', ' + map_selection )
                    cmd.do( 'isodot dot_' + str(map_name) + ', ' + str(map_name) )
                    map_name += 1
                    cmd.do( 'zoom ' + centerselection + ', ' + str(zoomnum) )
                    print 'Dots map complete'
                elif parameterslist[1] == 'surface':
                    cmd.do( 'map_new ' + str(map_name)+ ', ' + map_type + ', ' + str(map_grid) + ', ' + map_selection )
                    cmd.show( 'surface' )                          
                    map_name += 1
                    cmd.do( 'zoom ' + centerselection + ', ' + str(zoomnum) )
                    print 'Surface map complete'
            elif parameterslist[0] == 'level':
                if parameterslist[1] == 'mean':
                    print 'The MEAN function is not supported by PyMOL.'
            else:
                    map_level = int(parameterslist[1])
        else:
            print 'That map command is currently not supported by ConSCRIPT and PyMOL.'
    except:
        print 'An error has occured with a map command.'

## Handles RGB Triplet for colors
def RGBTriplet(name, triplet):

    try:
        cmd.set_color( name, triplet )

    except:
        print "RGB Triplet not valid."

    return name

## Defines HBonds for a structure
def HBonds():

    try:
        cmd.h_add('all')

        cmd.select( 'don', '(elem n,o and (neighbor elem h) and VSLselection)' )
        cmd.select( 'acc', '(elem o or (elem n and not (neighbor elem h))) and VSLselection' )
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

        cmd.select( 'SSCys', '(elem S and resn Cys) and VSLselection' )
        cmd.distance( 'SSCysteines', '(SSCys)','(SSCys)', '3.0' )
        cmd.delete( 'SSCys' )
        cmd.hide( '(elem h)' )
         
        cmd.hide( 'labels','SSCysteines' )
    except:
        print 'Error occured with calculating SSBonds.'

## Handle a command line
def handlecommand( p ):

    global VSLselection
    global VSLselectionsaved
    global VSLVerbose
    global clip_dist_near
    global clip_dist_far
    global centerselection
    global zoomnum

    if( p.replace( ' ', '' )=="\n" ):
        return 0

    if( p.replace( ' ', '' )[:1]=='#' ):
        print p
        return 0
    
    TokenPtr = 0
    TokenStart = 0
    CurToken = 0
    TokenIdent = ""
    TokenValue = 0
    
    try:
      (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
    except:
      print 'VSLFetchToken failed TokenPtr = ' + str(TokenPtr)
      
    # handle temporary selection
    VSLselectionsaved = VSLselection
    if CurToken == -ord('('):
      stack = []
      end = -1
      for x in range( TokenStart + 1, len( p ) ):
        if p[x:x+1] == '(':
          stack.append('(')
        if p[x:x+1] == ')':
          if stack == []:
            end = x
            x = len(p)
          else:
            stack.pop()
      if end != -1:
        q = p[TokenStart:end+1]
        q = q.lower() 
        VSLselection = select(q)
        if VSLVerbose > 0:
          print 'VSLselection: ' + VSLselection
        if end < len(p)-1 and p[end+1:end+2] == '.':
          end = end+1
        TokenPtr = 0
        TokenStart = 0
        CurToken = 0
        TokenIdent = ""
        TokenValue = 0
        p = p[end+1:len(p)]
        try:
          (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
        except:
          print 'VSLFetchToken failed TokenPtr = ' + str(TokenPtr)

    selected = VSLselection           
    cmd.select('VSLselection',VSLselection)
    if VSLVerbose > 0:
      print 'VSLselection: ' + VSLselection
      print 'VSLcommand: ' + p


    ##---------------Script---------------##

    if CurToken == ScriptTok or CurToken == SourceTok:
        try:
          (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
        except:
          print 'VSLFetchToken failed TokenPtr = ' + str(TokenPtr)
        if CurToken == 0:
            print p
            print 'Does not contain a valid filename'
        elif CurToken == StringTok:
            try:
                print '\"'+TokenIdent+'\"' + '<--SCRIPTFILE'
                return processVSLscript( TokenIdent )
            except:
                print '\"'+TokenIdent+'\"' + '<--SCRIPTFILE'
                print 'EXCEPTION THROWN'                    
        else:
            ts = p[TokenStart:len(p)]
            try:
                print ts + '<--SCRIPTFILE'
                return processVSLscript( ts )
            except:
                print ts + '<--SCRIPTFILE'
                print 'EXCEPTION THROWN'
        return 0            



    ##---------------Load---------------##

    if CurToken == LoadTok:
        try:
          (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
        except:
          print 'VSLFetchToken failed TokenPtr = ' + str(TokenPtr)
        if IsMoleculeToken(CurToken):
            try:
              (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
            except:
              print 'VSLFetchToken failed TokenPtr = ' + str(TokenPtr)
        if CurToken == 0:
            print p
            print 'Does not contain a valid filename'
        elif CurToken == StringTok:
            try:
                print '\"'+TokenIdent+'\"' + '<--LOADFILE'
                cmd.load( '\"'+TokenIdent+'\"' )
                cmd.rotate( 'x', 180 )
                cmd.select('VSLselection','( all )')
                cmd.select('VSLCenterSelection', centerselection)
                cmd.center( centerselection )
                VSLselection = '( all )'
                color_cpk( VSLselection )
                if VSLVerbose > 0:
                  print 'VSLselection: ' + VSLselection
            except:
                print '\"'+TokenIdent+'\"' + '<--LOADFILE'
                print 'EXCEPTION THROWN'                    
        else:
            ts = p[TokenStart:len(p)]
            try:
                print ts + '<--LOADFILE'
                cmd.load( ts )
                cmd.rotate( 'x', 180 )
                cmd.select('VSLselection','( all )')
                cmd.select('VSLCenterSelection', centerselection)
                cmd.center( centerselection )
                VSLselection = '( all )'
                color_cpk( VSLselection )
                if VSLVerbose > 0:
                  print 'VSLselection: ' + VSLselection
            except:
                print ts + '<--LOADFILE'
                print 'EXCEPTION THROWN'
        return 0            

    ##---------------Save---------------##

    firstword = p.split( ' ', 1 )[0].upper()
    saveCmd = ['WRITE', 'SAVE']
    
    if firstword in saveCmd:
        s = ''
        for i in p.split( ' ', 1 )[1]:
            s = s + i + ' '
        cmd.save( s )
        return 0

    ##---------------Echo---------------##

    if p[:4]=='echo':
        returnval = p[5:]
        if returnval[:1]=='"':
            returnval = returnval[1:]
        if returnval[-1:]=='"':
            returnval = returnval[:-1]
        print returnval
        return 0

    ##---------LOWER-----------##
    p = p.lower()

    #-----------Background color------------#
    
    if CurToken == BackgroundTok:
        try:
          (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
        except:
          print 'VSLFetchToken failed TokenPtr = ' + str(TokenPtr)
        (result, rgb) = VSLParseColour( p, TokenPtr, CurToken )
        if result == True:
            colorx = RGBTriplet( 'VSLColor', rgb)
            cmd.bg_color(colorx)
        else:
            print MsgStrs[ErrSyntax]
        return 0
    
    #----------------Select-----------------#
            
    if p[:6]=='select':
        selected = select( p[7:].lower() )                            
        print selected + '<--SELECTED'
        try:
            cmd.select( 'VSLselection', selected)
            pmg_tk.startup.ConSCRIPT.VSLselection = selected
            if VSLVerbose > 0:
              print 'VSLselection: ' + VSLselection
        except:
            print 'No selection was made for select, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
        return 0
       
    #----------------Restrict-----------------#
            
    if p[:8]=='restrict':
        selected = select( p[9:].lower() )
        restricted = 'all and not (' + selected + ')'
        print selected + '<--RESTRICTED'
        try:
            cmd.select( 'VSLselection', selected )
            pmg_tk.startup.ConSCRIPT.VSLselection = selected
            if VSLVerbose > 0:
              print 'VSLselection: ' + VSLselection
            cmd.hide( 'everything', restricted )
        except:
            print 'No selection was made for restrict, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
        return 0

    ##---------------Center---------------##

    if p[:6]=='center' or p[:6]=='centre':
        centerselection = select( p[7:].lower() )   
        print centerselection + '<--CENTER'
        try:
            cmd.select( 'VSLCenterSelection', centerselection)
            cmd.center( centerselection )
        except:
            print 'No selection was made for center, please specify a selection.  If you have specified a selection, please check your selection for errors.  If no error can be found, try rewriting your selections a different way.'
        return 0
         
    ##---------------Color---------------##
                
    if CurToken == ColourTok:
        (TokenPtr, CurToken, TokenStart, TokenIdent, TokenValue) = VSLFetchToken( p, TokenPtr)
        print str(CurToken)+' vs '+str(CPKTok)
        if CurToken == CPKTok:
            color_cpk(VSLselection)
            return 0
        if p[TokenStart] != '[':
            colory = p.split( ' ', 1)[1].lower()
            colory = colory.replace( ' ', '' )
            try:
                cmd.color( colory, '( '+ VSLselection +' )' )
                return 0
            except:
                print 'VSL color name '+colory+' not recognized'
        (xresult, rgb) = VSLParseColour( p, TokenPtr, CurToken )
        if xresult != True:
            print MsgStrs[ErrSyntax]
            return 0
        colorx = RGBTriplet( 'VSLColor', rgb)
        if VSLVerbose > 0:
            print 'VSLselection: ' + VSLselection
        cmd.color( 'VSLColor', '( '+ VSLselection +' )' )

        return 0

    ##---------------Spacefill/CPK---------------##

    if p[:9]=='spacefill' or p[:3]=='cpk' or p[:6]=='cpknew':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                cmd.hide( 'spheres', 'VSLselection' )
                print 'Spacefill off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.show( 'spheres', 'VSLselection' )
                print 'Spacefill on complete'
            elif float(command)>=0 and float(command)<=1500:
                cmd.show( 'spheres', 'VSLselection' )
                if '.' in command:
                    command = float(command)
                else:
                    command = float(command)/250
                cmd.set( 'sphere_scale', command )
        except:
            print 'An error occured with the spacefill/cpk command'
        return 0

    ##---------------Cartoon---------------##

    if p[:7]=='cartoon':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                cmd.hide( 'cartoon', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                print 'Cartoon off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.cartoon( 'rectangle', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                cmd.show( 'cartoon', 'VSLselection' )
                print 'Cartoon on complete'
            elif float(command)>=0 and float(command)<=500:
                if '.' in command:
                    command = float(command)
                else:
                    command = float(command)/250
                cmd.cartoon( 'rectangle', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                cmd.show( 'cartoon', 'VSLselection' )
                cmd.set( 'cartoon_rect_length', command )
                print 'Cartoon on complete'
        except:
            print 'An error occured with the cartoon command'
        return 0

    ##---------------Trace---------------##

    if p[:5]=='trace':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                cmd.hide( 'cartoon', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                print 'Trace off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.cartoon( 'tube', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                cmd.show( 'cartoon', 'VSLselection' )
                print 'Trace on complete'
            elif float(command)>=0 and float(command)<=500:
                if '.' in command:
                    command = float(command) * 10
                else:
                    command = ( float(command)/250 ) * 10
                cmd.cartoon( 'tube', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                cmd.show( 'cartoon', 'VSLselection' )
                cmd.set( 'cartoon_tube_radius', command )
                print 'Trace on complete'
        except:
            print 'An error occured with the trace command'
        return 0

    ##---------------Ribbon---------------##

    if p[:6]=='ribbon':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                cmd.hide( 'cartoon', 'VSLselection' )
                cmd.hide( 'ribbon', 'VSLselection' )
                print 'Ribbon off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.hide( 'cartoon', 'VSLselection' )
                cmd.show( 'ribbon', 'VSLselection' )
                print 'Ribbon on complete'
            elif float(command)>=0 and float(command)<=500:
                if '.' in command:
                    command = float(command)
                else:
                    command = float(command)/250
                cmd.hide( 'cartoon', 'VSLselection' )
                cmd.show( 'ribbon', 'VSLselection' )
                cmd.set( 'ribbon_width', command )
                print 'Ribbon on complete'
        except:
            print 'An error occured with the ribbon command'
        return 0

    ##---------------Wireframe---------------##

    if p[:9]=='wireframe':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                cmd.hide( 'lines', 'VSLselection' )
                print 'Wireframe off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.show( 'lines', 'VSLselection' )
                print 'Wireframe on complete'
            elif float(command)>=0 and float(command)<=1500:
                if '.' in command:
                    command =  float(command)
                else:
                    command =  float(command)/ 250  
                cmd.show( 'sticks', 'VSLselection' )
                cmd.set( 'stick_radius', command )
                print 'Wireframe on complete'
        except:
            print 'An error occured with the wireframe command'
            return 0
        return 0

    ##---------------Dots---------------##

    if p[:4]=='dots':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off' or command=='0':
                cmd.hide( 'dots', 'VSLselection' )
                print 'Dots off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.show( 'dots', 'VSLselection' )
                print 'Dots on complete'
            elif int(command)>0 and int(command)<=1000:
                command = int(command)
                cmd.show( 'dots', 'VSLselection' )
                if command in range(1, 5):
                    cmd.set( 'dot_density', 0 )
                elif command in range(5, 20):
                    cmd.set( 'dot_density', 1 )
                elif command in range(20, 140):
                    cmd.set( 'dot_density', 2 )
                elif command in range(140, 625):
                    cmd.set( 'dot_density', 3 )
                elif command in range(325, 1000):
                    cmd.set( 'dot_density', 4 )
                print 'Dots on complete'
        except:
            print 'An error occured with the dots command'
        return 0

    ##---------------Zoom---------------##

    if p[:4]=='zoom':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off' or command=='':
                zoomnum = 0
                cmd.zoom( 'VSLCenterSelection', zoomnum )
                print 'Zoom off complete'
            elif command=='true' or command=='on':
                zoomnum = -25
                cmd.zoom( 'VSLCenterSelection', zoomnum )
                print 'Zoom on complete'
            elif int(command) in range(0, 100):
                zoomnum = int(command)
                zoomnum = -( (zoomnum-100) )
                print 'Zoom ' + str(zoomnum)
                cmd.zoom( 'VSLCenterSelection', zoomnum )
            elif int(command) in range(100, 5000):
                zoomnum = int(command)
                zoomnum = -( (zoomnum-100)/20 )
                print 'Zoom ' + str(zoomnum)
                cmd.zoom( 'VSLCenterSelection', zoomnum )
            else:
                print 'That function is not supported by PyMOL.'
        except:
            print 'Zoom did not execute properly.  Please revise your zoom command'
        return 0

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
        return 0

    ##---------------Translate---------------##

    if p[:9]=='translate':
        try:
            commandlist = p.split( ' ' )
            if commandlist[1]=='x':
                cmd.center( 'VSLCenterSelection' )
                cmd.translate( [int(commandlist[2]),0,0] )
            elif commandlist[1]=='y':
                cmd.center( 'VSLCenterSelection' )
                cmd.translate( '[0,-' + commandlist[2] + ',0]' )
            elif commandlist[1]=='z':
                cmd.center( 'VSLCenterSelection' )
                cmd.translate( '[0,0,-' + commandlist[2] + ']' )
            else:
                print 'That function is not supported by PyMOL at all'
        except:
            print 'Translate did not execute properly.  Please revise your translate command'
        return 0

    ##---------------Slab---------------##

    if p[:4]=='slab':
        try:
            cmd.clip( 'near', -clip_dist_near )
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                clip_dist_near = 0
                print 'Slab off complete'
            elif command=='true' or command=='on' or command=='':
                print clip_dist_near
                cmd.clip( 'near', clip_dist_near )
                print 'Slab on complete'
            elif float(command)>=0 and float(command)<=100:
                command = float(command)
                clip_dist_near = command-100
                cmd.clip( 'near', clip_dist_near )
                print 'Slab on complete'
        except:
            print 'An error occured with the slab command'
        return 0

    ##---------------Depth---------------##

    if p[:5]=='depth':
        try:
            cmd.clip( 'far', -clip_dist_far )
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                clip_dist_far = 0
                print 'Depth off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.clip( 'far', clip_dist_far )
                print 'Depth on complete'
            elif float(command)>=0 and float(command)<=100:
                command = float(command)
                clip_dist_far = command
                cmd.clip( 'far', clip_dist_far )
                print 'Depth on complete'
        except:
            print 'An error occured with the depth command'
        return 0
        
    ##---------------HBonds---------------##

    if p[:6]=='hbonds':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
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
        return 0

    ##---------------SSBonds---------------##

    if p[:6]=='ssbonds':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
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
        return 0

    ##---------------Backbone--------------##

    if p[:8]=='backbone':
        try:
            p = p + ' '
            command = p.split( ' ', 1 )[1].rstrip()
            if command=='false' or command=='off':
                cmd.hide( 'cartoon', select('backbone') )
                print 'Backbone off complete'
            elif command=='true' or command=='on' or command=='':
                cmd.cartoon( 'tube', 'VSLselection' )
                cmd.show( 'cartoon', select('backbone') )
                print 'Backbone on complete'
            elif command=='dash':
                print 'PyMOL does not include funcionality for this command...yet...'
            elif float(command)>=0 and float(command)<=500:
                if '.' in command:
                    command = float(command)
                else:
                    command = float(command)/250
                cmd.cartoon( 'tube', 'VSLselection' )
                cmd.show( 'cartoon', select('backbone') )
                cmd.set( 'cartoon_tube_radius', command )
                print 'Backbone on complete'
            else:
                print 'That function is not supported by PyMOL.'
        except:
            print 'An error occured while trying to display the backbone.'
        return 0

    ##---------------Monitor---------------##

    if p[:7]=='monitor':
        try:
            parameters = p.split( ' ' )
            if len(parameters) == 3:
                cmd.distance( 'monitor', 'id ' + parameters[1],  'id ' + parameters[2] )
            elif len(parameters) == 2:
                command = parameters[1]
                if command=='false' or command=='off':
                    cmd.hide( 'labels' )
                    cmd.hide( 'dashes' )
                    print 'Monitor off complete'
                elif command=='true' or command=='on' or command=='':
                    pass
                else:
                    print 'That function is not supported by PyMOL'
            else:
                print 'That function is not supported by PyMOL'
        except:
            print 'An error occured while trying to display the labels.'
        return 0

    ##---------------Zap---------------##

    if p=='zap':
        print 'reinitialize'
        cmd.reinitialize()
        return 0

    ##---------------Stereo---------------##

    if p[:6]=='stereo':
        tmpstring = p.split()[1]
        if 'on' in tmpstring:
            cmd.stereo('on')
        elif 'off' in tmpstring:
                cmd.stereo('off')
        else:
            print 'That function is not supported by PyMOL.'
        return 0

    ##---------------Map---------------##

    if p[:3]=='map':
        try:
            parameters = p[4:]
            mapsupport( parameters )
            return 0
        except:
            print 'An error occured with a map command.'

    ##---------------Refresh---------------##

    if 'refresh' in p:
        print 'refresh'
        cmd.refresh()
        return 0

    ##---------------Reset---------------##

    if 'reset' in p:
        print 'reset'
        cmd.reset()
        return 0

    ##---------------Define---------------##

    if p[:6]=='define':
        defparams = p[7:].split( ' ', 1 )
        cmd.select( defparams[0], select(defparams[1]) )
        UserDefinedGroups[ defparams[0] ] =  defparams[1]
        return 0
        
    ##-----------Pause/Wait---------------------##

    if p[:5]=='pause':
        keystroke=False
        while not keystroke:
            if event.char==event.keysym:
                keystroke=True
        return 0
        
    ##-------Quit/Exit/blank/comment------------##

    if CurToken == ExitTok or CurToken == QuitTok or CurToken == 0 :
        return CurToken

    
    ##--------------------CONCEAL--------------------##
    if CurToken == ConcealTok:
        # get next token
        try:
            (TokenPtr, CurToken, TokenStart, TokenIdent,
             TokenValue) = VSLFetchToken(p, TokenPtr)

        except:
            pass
            print 'VSLFetchToken failed TokenPtr =', TokenPtr

        # if there is no token
        if CurToken == 0:
            cmd.hide()  # just call hide, no args.
        return 0

    ##--------------------REVEAL--------------------##
    if CurToken == RevealTok:
        # get next token
        try:
            (TokenPtr, CurToken, TokenStart, TokenIdent,
             TokenValue) = VSLFetchToken(p, TokenPtr)
        except:
            pass
            #print 'VSLFetchToken failed TokenPtr = ',
                    #str(TokenPtr)

        if CurToken == 0:
            cmd.show()
            return 0
        return 0

    print p
    print 'not implemented as a VSL command'
    return 0


## Handler for SBEVSL commands from the command line
def VSL( *args, **kwargs  ):
    p = ' '.join(args)
    donext = handlecommand(p.rstrip())
    if donext == QuitTok or donext == ExitTok:
        cmd.quit()
    return donext



## Handler for processing a script from a file
def processVSLscript( Q ):

    global filelevel
    global filestack
    
    #Open the script 
    f = open(Q, 'rU')
    filestack.append(f)
    filelevel = filelevel+1
    
    #Make a loop
    try:
        for p in f:
            donext = handlecommand(p.rstrip())
            if donext == ExitTok or donext == QuitTok:
              f.close()
              filelevel = filelevel-1
              if donext == QuitTok:
                return QuitTok
              else:
                return 0  
    finally:
        #Close the file
        f.close()
        filelevel = filelevel-1
        return 0
        
