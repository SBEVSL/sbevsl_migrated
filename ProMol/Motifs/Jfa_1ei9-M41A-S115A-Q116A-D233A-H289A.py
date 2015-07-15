'''
FUNC:Jfa_1ei9-M41A-S115A-Q116A-D233A-H289A
PDB:1ei9
EC:3.1.2.22
PFAM:PF02089
RESI:met,ser,gln,asp,his
LOCI:a-41,115,116,233,289;
'''
jesstemp0 ='n.  n  '
cmd.select('jessatom0', '(('+jesstemp0+'))')
jesstemp1 ='n.  ca '
jesstemp2 ='jessatom0 x. %s'%(1.464500+(d*0.300000))
jesstemp3 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp1+')&('+jesstemp2+')&('+jesstemp3+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.464500+(d*0.300000)))
jesstemp4 ='n.  c  '
jesstemp5 ='jessatom0 x. %s'%(2.525000+(d*0.300000))
jesstemp6 ='br. jessatom0'
jesstemp7 ='jessatom1 x. %s'%(1.545300+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.525000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.545300+(d*0.300000)))
jesstemp8 ='r. ser'
jesstemp9 ='r. thr'
jesstemp10 ='jessatom0 x. %s'%(6.019600+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(7.322500+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(8.181000+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp1+')&('+jesstemp8+'))|(('+jesstemp1+')&('+jesstemp9+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.019600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.322500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(8.181000+(d*0.300000)))
jesstemp13 ='n.  cb '
jesstemp14 ='jessatom0 x. %s'%(4.888400+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(6.120600+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(6.837700+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp18 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp13+')&('+jesstemp8+'))|(('+jesstemp13+')&('+jesstemp9+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.888400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.120600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.837700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp19 ='n.  og '
jesstemp20 ='jessatom0 x. %s'%(5.241900+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(6.241800+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(6.928600+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(2.444200+(d*0.300000))
jesstemp24 ='br. jessatom3'
jesstemp25 ='jessatom4 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp19+')&('+jesstemp8+'))|(('+jesstemp19+')&('+jesstemp9+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.241900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.928600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.424100+(d*0.300000)))
jesstemp26 ='jessatom0 x. %s'%(5.050000+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(6.211500+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(7.423500+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(2.494700+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(2.807800+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(3.252200+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+'))|(('+jesstemp0+')))&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.050000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.211500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.423500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(2.494700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(2.807800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.252200+(d*0.300000)))
jesstemp32 ='n.  ca '
jesstemp33 ='jessatom0 x. %s'%(5.575200+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(6.585200+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(7.968900+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(3.868300+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(4.282400+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(4.625800+(d*0.300000))
jesstemp39 ='jessatom6 x. %s'%(1.484700+(d*0.300000))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp32+'))|(('+jesstemp32+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.575200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.585200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.968900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.868300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.282400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.484700+(d*0.300000)))
jesstemp41 ='n.  c  '
jesstemp42 ='jessatom0 x. %s'%(6.080200+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(7.181100+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(8.564800+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(4.444000+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(5.060100+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(5.736800+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(2.504800+(d*0.300000))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(1.535200+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp41+'))|(('+jesstemp41+')))&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.080200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.181100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.444000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.060100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.736800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.504800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.535200+(d*0.300000)))
jesstemp51 ='n.  cg '
jesstemp52 ='r. asp'
jesstemp53 ='r. glu'
jesstemp54 ='jessatom0 x. %s'%(12.958300+(d*0.300000))
jesstemp55 ='jessatom1 x. %s'%(13.614800+(d*0.300000))
jesstemp56 ='jessatom2 x. %s'%(13.877400+(d*0.300000))
jesstemp57 ='jessatom3 x. %s'%(9.110200+(d*0.300000))
jesstemp58 ='jessatom4 x. %s'%(9.019300+(d*0.300000))
jesstemp59 ='jessatom5 x. %s'%(8.049700+(d*0.300000))
jesstemp60 ='jessatom6 x. %s'%(10.615100+(d*0.300000))
jesstemp61 ='jessatom7 x. %s'%(11.716000+(d*0.300000))
jesstemp62 ='jessatom8 x. %s'%(12.877500+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp51+')&('+jesstemp52+'))|(('+jesstemp51+')&('+jesstemp53+')))&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(12.958300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(13.614800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(13.877400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(9.110200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.019300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(8.049700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(10.615100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(11.716000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(12.877500+(d*0.300000)))
jesstemp63 ='n.  od1'
jesstemp64 ='n.  od2'
jesstemp65 ='n.  oe1'
jesstemp66 ='n.  oe2'
jesstemp67 ='jessatom0 x. %s'%(12.503800+(d*0.300000))
jesstemp68 ='jessatom1 x. %s'%(13.049200+(d*0.300000))
jesstemp69 ='jessatom2 x. %s'%(13.261300+(d*0.300000))
jesstemp70 ='jessatom3 x. %s'%(9.201100+(d*0.300000))
jesstemp71 ='jessatom4 x. %s'%(8.928400+(d*0.300000))
jesstemp72 ='jessatom5 x. %s'%(7.827500+(d*0.300000))
jesstemp73 ='jessatom6 x. %s'%(10.524200+(d*0.300000))
jesstemp74 ='jessatom7 x. %s'%(11.615000+(d*0.300000))
jesstemp75 ='jessatom8 x. %s'%(12.867400+(d*0.300000))
jesstemp76 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp77 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp63+')|('+jesstemp64+'))&('+jesstemp52+'))|((('+jesstemp65+')|('+jesstemp66+'))&('+jesstemp53+')))&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(12.503800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(13.049200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(13.261300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(8.928400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(7.827500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(10.524200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(11.615000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(12.867400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp78 ='n.  od2'
jesstemp79 ='n.  od1'
jesstemp80 ='n.  oe2'
jesstemp81 ='n.  oe1'
jesstemp82 ='jessatom0 x. %s'%(12.301800+(d*0.300000))
jesstemp83 ='jessatom1 x. %s'%(13.069400+(d*0.300000))
jesstemp84 ='jessatom2 x. %s'%(13.392600+(d*0.300000))
jesstemp85 ='jessatom3 x. %s'%(8.090100+(d*0.300000))
jesstemp86 ='jessatom4 x. %s'%(8.110300+(d*0.300000))
jesstemp87 ='jessatom5 x. %s'%(7.251800+(d*0.300000))
jesstemp88 ='jessatom6 x. %s'%(9.726300+(d*0.300000))
jesstemp89 ='jessatom7 x. %s'%(10.867600+(d*0.300000))
jesstemp90 ='jessatom8 x. %s'%(11.948300+(d*0.300000))
jesstemp91 ='br. jessatom9'
jesstemp92 ='jessatom10 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp78+')|('+jesstemp79+'))&('+jesstemp52+'))|((('+jesstemp80+')|('+jesstemp81+'))&('+jesstemp53+')))&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp76+')&('+jesstemp91+')&('+jesstemp92+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(12.301800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(13.069400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(13.392600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(8.090100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(8.110300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(7.251800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(9.726300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(10.867600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(11.948300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
jesstemp93 ='r. his'
jesstemp94 ='jessatom0 x. %s'%(9.271800+(d*0.300000))
jesstemp95 ='jessatom1 x. %s'%(9.978800+(d*0.300000))
jesstemp96 ='jessatom2 x. %s'%(10.069700+(d*0.300000))
jesstemp97 ='jessatom3 x. %s'%(6.292300+(d*0.300000))
jesstemp98 ='jessatom4 x. %s'%(5.696400+(d*0.300000))
jesstemp99 ='jessatom5 x. %s'%(4.868200+(d*0.300000))
jesstemp100 ='jessatom6 x. %s'%(7.968900+(d*0.300000))
jesstemp101 ='jessatom7 x. %s'%(9.322300+(d*0.300000))
jesstemp102 ='jessatom8 x. %s'%(10.413100+(d*0.300000))
jesstemp103 ='jessatom9 x. %s'%(4.221800+(d*0.300000))
jesstemp104 ='jessatom10 x. %s'%(3.999600+(d*0.300000))
jesstemp105 ='jessatom11 x. %s'%(3.686500+(d*0.300000))
cmd.select('jessatom12', '(('+jesstemp51+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+')&('+jesstemp98+')&('+jesstemp99+')&('+jesstemp100+')&('+jesstemp101+')&('+jesstemp102+')&('+jesstemp103+')&('+jesstemp104+')&('+jesstemp105+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom12 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom12 x. %s)'%(9.978800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom12 x. %s)'%(10.069700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom12 x. %s)'%(6.292300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom12 x. %s)'%(5.696400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom12 x. %s)'%(4.868200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom12 x. %s)'%(7.968900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom12 x. %s)'%(9.322300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom12 x. %s)'%(10.413100+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom12 x. %s)'%(4.221800+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom12 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom12 x. %s)'%(3.686500+(d*0.300000)))
jesstemp106 ='n.  nd1'
jesstemp107 ='jessatom0 x. %s'%(9.504100+(d*0.300000))
jesstemp108 ='jessatom1 x. %s'%(10.332300+(d*0.300000))
jesstemp109 ='jessatom2 x. %s'%(10.605000+(d*0.300000))
jesstemp110 ='jessatom3 x. %s'%(5.686300+(d*0.300000))
jesstemp111 ='jessatom4 x. %s'%(5.413600+(d*0.300000))
jesstemp112 ='jessatom5 x. %s'%(4.605600+(d*0.300000))
jesstemp113 ='jessatom6 x. %s'%(7.433600+(d*0.300000))
jesstemp114 ='jessatom7 x. %s'%(8.726400+(d*0.300000))
jesstemp115 ='jessatom8 x. %s'%(9.797000+(d*0.300000))
jesstemp116 ='jessatom9 x. %s'%(3.757200+(d*0.300000))
jesstemp117 ='jessatom10 x. %s'%(3.827900+(d*0.300000))
jesstemp118 ='jessatom11 x. %s'%(2.918900+(d*0.300000))
jesstemp119 ='jessatom12 x. %s'%(1.393800+(d*0.300000))
jesstemp120 ='br. jessatom12'
cmd.select('jessatom13', '(('+jesstemp106+')&('+jesstemp93+')&('+jesstemp107+')&('+jesstemp108+')&('+jesstemp109+')&('+jesstemp110+')&('+jesstemp111+')&('+jesstemp112+')&('+jesstemp113+')&('+jesstemp114+')&('+jesstemp115+')&('+jesstemp116+')&('+jesstemp117+')&('+jesstemp118+')&('+jesstemp119+')&('+jesstemp120+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom13 x. %s)'%(9.504100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom13 x. %s)'%(10.332300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom13 x. %s)'%(10.605000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom13 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom13 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom13 x. %s)'%(4.605600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom13 x. %s)'%(7.433600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom13 x. %s)'%(8.726400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom13 x. %s)'%(9.797000+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom13 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom13 x. %s)'%(3.827900+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom13 x. %s)'%(2.918900+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom13 x. %s)'%(1.393800+(d*0.300000)))
jesstemp121 ='n.  ne2'
jesstemp122 ='jessatom0 x. %s'%(7.342700+(d*0.300000))
jesstemp123 ='jessatom1 x. %s'%(8.170900+(d*0.300000))
jesstemp124 ='jessatom2 x. %s'%(8.484000+(d*0.300000))
jesstemp125 ='jessatom3 x. %s'%(4.272300+(d*0.300000))
jesstemp126 ='jessatom4 x. %s'%(3.565300+(d*0.300000))
jesstemp127 ='jessatom5 x. %s'%(2.656300+(d*0.300000))
jesstemp128 ='jessatom6 x. %s'%(5.777200+(d*0.300000))
jesstemp129 ='jessatom7 x. %s'%(7.150800+(d*0.300000))
jesstemp130 ='jessatom8 x. %s'%(8.241600+(d*0.300000))
jesstemp131 ='jessatom9 x. %s'%(5.746900+(d*0.300000))
jesstemp132 ='jessatom10 x. %s'%(5.524700+(d*0.300000))
jesstemp133 ='jessatom11 x. %s'%(5.009600+(d*0.300000))
jesstemp134 ='jessatom12 x. %s'%(2.211900+(d*0.300000))
jesstemp135 ='br. jessatom12'
jesstemp136 ='jessatom13 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom14', '(('+jesstemp121+')&('+jesstemp93+')&('+jesstemp122+')&('+jesstemp123+')&('+jesstemp124+')&('+jesstemp125+')&('+jesstemp126+')&('+jesstemp127+')&('+jesstemp128+')&('+jesstemp129+')&('+jesstemp130+')&('+jesstemp131+')&('+jesstemp132+')&('+jesstemp133+')&('+jesstemp134+')&('+jesstemp135+')&('+jesstemp136+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom14 x. %s)'%(7.342700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom14 x. %s)'%(8.170900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom14 x. %s)'%(8.484000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom14 x. %s)'%(4.272300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom14 x. %s)'%(3.565300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom14 x. %s)'%(2.656300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom14 x. %s)'%(5.777200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom14 x. %s)'%(7.150800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom14 x. %s)'%(8.241600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom14 x. %s)'%(5.746900+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom14 x. %s)'%(5.524700+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom14 x. %s)'%(5.009600+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom14 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom13', 'jessatom13 & (jessatom14 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_1ei9-M41A-S115A-Q116A-D233A-H289A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
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
