'''
FUNC:Jfa_1chd-S164A-T165A-H190A-M283A-D286A
PDB:1chd
EC:3.1.1.61
PFAM:PF01339
RESI:ser,thr,his,met,asp
LOCI:a-164,165,190,283,286;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.403800+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.403800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.424100+(d*0.300000)))
jesstemp10 ='n.  n  '
jesstemp11 ='jessatom0 x. %s'%(2.484600+(d*0.300000))
jesstemp12 ='jessatom1 x. %s'%(2.888600+(d*0.300000))
jesstemp13 ='jessatom2 x. %s'%(2.646200+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+'))|(('+jesstemp10+')))&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(2.484600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(2.888600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(2.646200+(d*0.300000)))
jesstemp14 ='n.  ca '
jesstemp15 ='jessatom0 x. %s'%(3.878400+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(4.343000+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(3.928900+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(1.464500+(d*0.300000))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp14+'))|(('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.878400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.343000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.928900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.464500+(d*0.300000)))
jesstemp20 ='n.  c  '
jesstemp21 ='jessatom0 x. %s'%(4.534900+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(5.211600+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(5.140900+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(2.525000+(d*0.300000))
jesstemp25 ='br. jessatom3'
jesstemp26 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp20+'))|(('+jesstemp20+')))&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.534900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.211600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.140900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.525000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp27 ='n.  cg '
jesstemp28 ='r. his'
jesstemp29 ='jessatom0 x. %s'%(4.454100+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(4.009700+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(4.181400+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(6.292300+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(7.635600+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(8.716300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(4.454100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.009700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.181400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.292300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.716300+(d*0.300000)))
jesstemp35 ='n.  nd1'
jesstemp36 ='jessatom0 x. %s'%(4.383400+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(3.474400+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(3.535000+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(5.969100+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(7.332600+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(8.463800+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp35+')&('+jesstemp28+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.383400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(3.474400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.535000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.969100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.332600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.463800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp44 ='n.  ne2'
jesstemp45 ='jessatom0 x. %s'%(5.827700+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(5.090400+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(5.524700+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(7.807300+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(9.231400+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(10.221200+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(2.222000+(d*0.300000))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp44+')&('+jesstemp28+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.090400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.524700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.807300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.231400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(10.221200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.171500+(d*0.300000)))
jesstemp54 ='n.  n  '
jesstemp55 ='jessatom0 x. %s'%(5.110600+(d*0.300000))
jesstemp56 ='jessatom1 x. %s'%(3.949100+(d*0.300000))
jesstemp57 ='jessatom2 x. %s'%(3.747100+(d*0.300000))
jesstemp58 ='jessatom3 x. %s'%(4.474300+(d*0.300000))
jesstemp59 ='jessatom4 x. %s'%(5.191400+(d*0.300000))
jesstemp60 ='jessatom5 x. %s'%(5.878200+(d*0.300000))
jesstemp61 ='jessatom6 x. %s'%(7.231600+(d*0.300000))
jesstemp62 ='jessatom7 x. %s'%(6.120600+(d*0.300000))
jesstemp63 ='jessatom8 x. %s'%(7.676000+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.110600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(3.949100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(3.747100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(4.474300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(5.191400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(7.231600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(6.120600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(7.676000+(d*0.300000)))
jesstemp64 ='jessatom0 x. %s'%(6.393300+(d*0.300000))
jesstemp65 ='jessatom1 x. %s'%(5.110600+(d*0.300000))
jesstemp66 ='jessatom2 x. %s'%(4.696500+(d*0.300000))
jesstemp67 ='jessatom3 x. %s'%(5.726700+(d*0.300000))
jesstemp68 ='jessatom4 x. %s'%(6.332700+(d*0.300000))
jesstemp69 ='jessatom5 x. %s'%(7.120500+(d*0.300000))
jesstemp70 ='jessatom6 x. %s'%(7.888100+(d*0.300000))
jesstemp71 ='jessatom7 x. %s'%(6.645800+(d*0.300000))
jesstemp72 ='jessatom8 x. %s'%(8.150700+(d*0.300000))
jesstemp73 ='jessatom9 x. %s'%(1.464500+(d*0.300000))
jesstemp74 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp0+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(6.393300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(5.110600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(4.696500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(6.332700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(7.120500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(7.888100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.645800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(8.150700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.464500+(d*0.300000)))
jesstemp75 ='n.  c  '
jesstemp76 ='jessatom0 x. %s'%(6.767000+(d*0.300000))
jesstemp77 ='jessatom1 x. %s'%(5.312600+(d*0.300000))
jesstemp78 ='jessatom2 x. %s'%(5.029800+(d*0.300000))
jesstemp79 ='jessatom3 x. %s'%(6.605400+(d*0.300000))
jesstemp80 ='jessatom4 x. %s'%(7.433600+(d*0.300000))
jesstemp81 ='jessatom5 x. %s'%(8.292100+(d*0.300000))
jesstemp82 ='jessatom6 x. %s'%(7.443700+(d*0.300000))
jesstemp83 ='jessatom7 x. %s'%(6.110500+(d*0.300000))
jesstemp84 ='jessatom8 x. %s'%(7.342700+(d*0.300000))
jesstemp85 ='jessatom9 x. %s'%(2.474500+(d*0.300000))
jesstemp86 ='br. jessatom9'
jesstemp87 ='jessatom10 x. %s'%(1.535200+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(6.767000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(6.605400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(7.433600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(8.292100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.443700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(6.110500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(7.342700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.535200+(d*0.300000)))
jesstemp88 ='r. asp'
jesstemp89 ='r. glu'
jesstemp90 ='jessatom0 x. %s'%(8.888000+(d*0.300000))
jesstemp91 ='jessatom1 x. %s'%(7.918400+(d*0.300000))
jesstemp92 ='jessatom2 x. %s'%(8.463800+(d*0.300000))
jesstemp93 ='jessatom3 x. %s'%(10.786800+(d*0.300000))
jesstemp94 ='jessatom4 x. %s'%(12.221000+(d*0.300000))
jesstemp95 ='jessatom5 x. %s'%(13.089600+(d*0.300000))
jesstemp96 ='jessatom6 x. %s'%(5.948900+(d*0.300000))
jesstemp97 ='jessatom7 x. %s'%(5.494400+(d*0.300000))
jesstemp98 ='jessatom8 x. %s'%(3.737000+(d*0.300000))
jesstemp99 ='jessatom9 x. %s'%(9.302100+(d*0.300000))
jesstemp100 ='jessatom10 x. %s'%(9.433400+(d*0.300000))
jesstemp101 ='jessatom11 x. %s'%(8.181000+(d*0.300000))
cmd.select('jessatom12', '(((('+jesstemp27+')&('+jesstemp88+'))|(('+jesstemp27+')&('+jesstemp89+')))&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+')&('+jesstemp98+')&('+jesstemp99+')&('+jesstemp100+')&('+jesstemp101+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom12 x. %s)'%(8.888000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom12 x. %s)'%(7.918400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom12 x. %s)'%(8.463800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom12 x. %s)'%(10.786800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom12 x. %s)'%(12.221000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom12 x. %s)'%(13.089600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom12 x. %s)'%(5.948900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom12 x. %s)'%(5.494400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom12 x. %s)'%(3.737000+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom12 x. %s)'%(9.302100+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom12 x. %s)'%(9.433400+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom12 x. %s)'%(8.181000+(d*0.300000)))
jesstemp102 ='n.  od1'
jesstemp103 ='n.  od2'
jesstemp104 ='n.  oe1'
jesstemp105 ='n.  oe2'
jesstemp106 ='jessatom0 x. %s'%(10.069700+(d*0.300000))
jesstemp107 ='jessatom1 x. %s'%(9.130400+(d*0.300000))
jesstemp108 ='jessatom2 x. %s'%(9.716200+(d*0.300000))
jesstemp109 ='jessatom3 x. %s'%(12.008900+(d*0.300000))
jesstemp110 ='jessatom4 x. %s'%(13.453200+(d*0.300000))
jesstemp111 ='jessatom5 x. %s'%(14.281400+(d*0.300000))
jesstemp112 ='jessatom6 x. %s'%(7.120500+(d*0.300000))
jesstemp113 ='jessatom7 x. %s'%(6.736700+(d*0.300000))
jesstemp114 ='jessatom8 x. %s'%(4.898500+(d*0.300000))
jesstemp115 ='jessatom9 x. %s'%(10.423200+(d*0.300000))
jesstemp116 ='jessatom10 x. %s'%(10.514100+(d*0.300000))
jesstemp117 ='jessatom11 x. %s'%(9.201100+(d*0.300000))
jesstemp118 ='jessatom12 x. %s'%(1.262500+(d*0.300000))
jesstemp119 ='br. jessatom12'
cmd.select('jessatom13', '((((('+jesstemp102+')|('+jesstemp103+'))&('+jesstemp88+'))|((('+jesstemp104+')|('+jesstemp105+'))&('+jesstemp89+')))&('+jesstemp106+')&('+jesstemp107+')&('+jesstemp108+')&('+jesstemp109+')&('+jesstemp110+')&('+jesstemp111+')&('+jesstemp112+')&('+jesstemp113+')&('+jesstemp114+')&('+jesstemp115+')&('+jesstemp116+')&('+jesstemp117+')&('+jesstemp118+')&('+jesstemp119+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom13 x. %s)'%(10.069700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom13 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom13 x. %s)'%(9.716200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom13 x. %s)'%(12.008900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom13 x. %s)'%(13.453200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom13 x. %s)'%(14.281400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom13 x. %s)'%(7.120500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom13 x. %s)'%(6.736700+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom13 x. %s)'%(4.898500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom13 x. %s)'%(10.423200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom13 x. %s)'%(10.514100+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom13 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom13 x. %s)'%(1.262500+(d*0.300000)))
jesstemp120 ='n.  od2'
jesstemp121 ='n.  od1'
jesstemp122 ='n.  oe2'
jesstemp123 ='n.  oe1'
jesstemp124 ='jessatom0 x. %s'%(8.271900+(d*0.300000))
jesstemp125 ='jessatom1 x. %s'%(7.423500+(d*0.300000))
jesstemp126 ='jessatom2 x. %s'%(7.968900+(d*0.300000))
jesstemp127 ='jessatom3 x. %s'%(10.281800+(d*0.300000))
jesstemp128 ='jessatom4 x. %s'%(11.726100+(d*0.300000))
jesstemp129 ='jessatom5 x. %s'%(12.625000+(d*0.300000))
jesstemp130 ='jessatom6 x. %s'%(4.979300+(d*0.300000))
jesstemp131 ='jessatom7 x. %s'%(4.767200+(d*0.300000))
jesstemp132 ='jessatom8 x. %s'%(2.777500+(d*0.300000))
jesstemp133 ='jessatom9 x. %s'%(9.312200+(d*0.300000))
jesstemp134 ='jessatom10 x. %s'%(9.564700+(d*0.300000))
jesstemp135 ='jessatom11 x. %s'%(8.423400+(d*0.300000))
jesstemp136 ='br. jessatom12'
jesstemp137 ='jessatom13 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom14', '((((('+jesstemp120+')|('+jesstemp121+'))&('+jesstemp88+'))|((('+jesstemp122+')|('+jesstemp123+'))&('+jesstemp89+')))&('+jesstemp124+')&('+jesstemp125+')&('+jesstemp126+')&('+jesstemp127+')&('+jesstemp128+')&('+jesstemp129+')&('+jesstemp130+')&('+jesstemp131+')&('+jesstemp132+')&('+jesstemp133+')&('+jesstemp134+')&('+jesstemp135+')&('+jesstemp118+')&('+jesstemp136+')&('+jesstemp137+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom14 x. %s)'%(8.271900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom14 x. %s)'%(7.423500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom14 x. %s)'%(7.968900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom14 x. %s)'%(10.281800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom14 x. %s)'%(11.726100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom14 x. %s)'%(12.625000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom14 x. %s)'%(4.979300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom14 x. %s)'%(4.767200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom14 x. %s)'%(2.777500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom14 x. %s)'%(9.312200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom14 x. %s)'%(9.564700+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom14 x. %s)'%(8.423400+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom14 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom13', 'jessatom13 & (jessatom14 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('Jfa_1chd-S164A-T165A-H190A-M283A-D286A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
cmd.delete('jessatom12')
cmd.delete('jessatom13')
cmd.delete('jessatom14')
