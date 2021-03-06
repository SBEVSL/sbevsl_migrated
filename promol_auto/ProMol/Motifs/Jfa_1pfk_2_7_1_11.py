'''
FUNC:Jfa_1pfk_2_7_1_11
PDB:1pfk
EC:2.7.1.11
RESI:gly,arg,thr,asp,arg
LOCI:a-11,72,125,127,171;
'''
jesstemp0 ='n.  n  '
cmd.select('jessatom0', '(('+jesstemp0+'))')
jesstemp1 ='n.  ca '
jesstemp2 ='jessatom0 x. %s'%(1.484700+(d*0.300000))
jesstemp3 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp1+')&('+jesstemp2+')&('+jesstemp3+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.484700+(d*0.300000)))
jesstemp4 ='n.  c  '
jesstemp5 ='jessatom0 x. %s'%(2.474500+(d*0.300000))
jesstemp6 ='br. jessatom0'
jesstemp7 ='jessatom1 x. %s'%(1.535200+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.535200+(d*0.300000)))
jesstemp8 ='n.  ne '
jesstemp9 ='r. arg'
jesstemp10 ='jessatom0 x. %s'%(4.666200+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(4.949000+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(6.443800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.666200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.443800+(d*0.300000)))
jesstemp13 ='n.  nh1'
jesstemp14 ='n.  nh2'
jesstemp15 ='jessatom0 x. %s'%(3.615800+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(4.292500+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(5.767100+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(2.373500+(d*0.300000))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp13+')|('+jesstemp14+'))&('+jesstemp9+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.615800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.292500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.767100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.373500+(d*0.300000)))
jesstemp20 ='n.  nh2'
jesstemp21 ='n.  nh1'
jesstemp22 ='jessatom0 x. %s'%(3.787500+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(3.585500+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(5.080300+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.333100+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp9+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.787500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.585500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.080300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.333100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.312900+(d*0.300000)))
jesstemp28 ='r. thr'
jesstemp29 ='r. ser'
jesstemp30 ='jessatom0 x. %s'%(6.706400+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.514500+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(5.858000+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(10.655500+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(8.898100+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(8.797100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp1+')&('+jesstemp28+'))|(('+jesstemp1+')&('+jesstemp29+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.706400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.514500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.858000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.655500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.898100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.797100+(d*0.300000)))
jesstemp36 ='n.  cb '
jesstemp37 ='jessatom0 x. %s'%(6.585200+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(6.635700+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(6.312500+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(10.211100+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(8.221400+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(8.423400+(d*0.300000))
jesstemp43 ='jessatom6 x. %s'%(1.595800+(d*0.300000))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp36+')&('+jesstemp28+'))|(('+jesstemp36+')&('+jesstemp29+')))&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.585200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.312500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.211100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.221400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.423400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.595800+(d*0.300000)))
jesstemp45 ='n.  og1'
jesstemp46 ='jessatom0 x. %s'%(6.262000+(d*0.300000))
jesstemp47 ='jessatom1 x. %s'%(6.161000+(d*0.300000))
jesstemp48 ='jessatom2 x. %s'%(6.090300+(d*0.300000))
jesstemp49 ='jessatom3 x. %s'%(9.393000+(d*0.300000))
jesstemp50 ='jessatom4 x. %s'%(7.463900+(d*0.300000))
jesstemp51 ='jessatom5 x. %s'%(7.463900+(d*0.300000))
jesstemp52 ='jessatom6 x. %s'%(2.444200+(d*0.300000))
jesstemp53 ='br. jessatom6'
jesstemp54 ='jessatom7 x. %s'%(1.484700+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp45+')&('+jesstemp28+'))|(('+jesstemp45+')&('+jesstemp29+')))&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.262000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.161000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.090300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.393000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.484700+(d*0.300000)))
jesstemp55 ='n.  cg '
jesstemp56 ='r. asp'
jesstemp57 ='r. glu'
jesstemp58 ='jessatom0 x. %s'%(8.564800+(d*0.300000))
jesstemp59 ='jessatom1 x. %s'%(8.191100+(d*0.300000))
jesstemp60 ='jessatom2 x. %s'%(8.564800+(d*0.300000))
jesstemp61 ='jessatom3 x. %s'%(9.978800+(d*0.300000))
jesstemp62 ='jessatom4 x. %s'%(8.342600+(d*0.300000))
jesstemp63 ='jessatom5 x. %s'%(7.878000+(d*0.300000))
jesstemp64 ='jessatom6 x. %s'%(6.110500+(d*0.300000))
jesstemp65 ='jessatom7 x. %s'%(5.363100+(d*0.300000))
jesstemp66 ='jessatom8 x. %s'%(3.999600+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp55+')&('+jesstemp56+'))|(('+jesstemp55+')&('+jesstemp57+')))&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(8.191100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(9.978800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(8.342600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.878000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(6.110500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(3.999600+(d*0.300000)))
jesstemp67 ='n.  od1'
jesstemp68 ='n.  od2'
jesstemp69 ='n.  oe1'
jesstemp70 ='n.  oe2'
jesstemp71 ='jessatom0 x. %s'%(8.958700+(d*0.300000))
jesstemp72 ='jessatom1 x. %s'%(8.393100+(d*0.300000))
jesstemp73 ='jessatom2 x. %s'%(8.736500+(d*0.300000))
jesstemp74 ='jessatom3 x. %s'%(10.201000+(d*0.300000))
jesstemp75 ='jessatom4 x. %s'%(8.807200+(d*0.300000))
jesstemp76 ='jessatom5 x. %s'%(8.009300+(d*0.300000))
jesstemp77 ='jessatom6 x. %s'%(6.635700+(d*0.300000))
jesstemp78 ='jessatom7 x. %s'%(6.150900+(d*0.300000))
jesstemp79 ='jessatom8 x. %s'%(4.777300+(d*0.300000))
jesstemp80 ='jessatom9 x. %s'%(1.252400+(d*0.300000))
jesstemp81 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp67+')|('+jesstemp68+'))&('+jesstemp56+'))|((('+jesstemp69+')|('+jesstemp70+'))&('+jesstemp57+')))&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(8.958700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(8.393100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(8.736500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(10.201000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(8.807200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(8.009300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.150900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.252400+(d*0.300000)))
jesstemp82 ='n.  od2'
jesstemp83 ='n.  od1'
jesstemp84 ='n.  oe2'
jesstemp85 ='n.  oe1'
jesstemp86 ='jessatom0 x. %s'%(7.857800+(d*0.300000))
jesstemp87 ='jessatom1 x. %s'%(7.635600+(d*0.300000))
jesstemp88 ='jessatom2 x. %s'%(8.201200+(d*0.300000))
jesstemp89 ='jessatom3 x. %s'%(8.978900+(d*0.300000))
jesstemp90 ='jessatom4 x. %s'%(7.282100+(d*0.300000))
jesstemp91 ='jessatom5 x. %s'%(6.999300+(d*0.300000))
jesstemp92 ='jessatom6 x. %s'%(6.322600+(d*0.300000))
jesstemp93 ='jessatom7 x. %s'%(5.393400+(d*0.300000))
jesstemp94 ='jessatom8 x. %s'%(3.989500+(d*0.300000))
jesstemp95 ='jessatom9 x. %s'%(1.272600+(d*0.300000))
jesstemp96 ='br. jessatom9'
jesstemp97 ='jessatom10 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp82+')|('+jesstemp83+'))&('+jesstemp56+'))|((('+jesstemp84+')|('+jesstemp85+'))&('+jesstemp57+')))&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(7.282100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(6.999300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(6.322600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(5.393400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(3.989500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.201800+(d*0.300000)))
jesstemp98 ='jessatom0 x. %s'%(9.090000+(d*0.300000))
jesstemp99 ='jessatom1 x. %s'%(9.251600+(d*0.300000))
jesstemp100 ='jessatom2 x. %s'%(10.504000+(d*0.300000))
jesstemp101 ='jessatom3 x. %s'%(7.403300+(d*0.300000))
jesstemp102 ='jessatom4 x. %s'%(6.282200+(d*0.300000))
jesstemp103 ='jessatom5 x. %s'%(6.544800+(d*0.300000))
jesstemp104 ='jessatom6 x. %s'%(10.908000+(d*0.300000))
jesstemp105 ='jessatom7 x. %s'%(9.786900+(d*0.300000))
jesstemp106 ='jessatom8 x. %s'%(8.544600+(d*0.300000))
jesstemp107 ='jessatom9 x. %s'%(6.514500+(d*0.300000))
jesstemp108 ='jessatom10 x. %s'%(6.918500+(d*0.300000))
jesstemp109 ='jessatom11 x. %s'%(5.403500+(d*0.300000))
cmd.select('jessatom12', '(('+jesstemp8+')&('+jesstemp9+')&('+jesstemp98+')&('+jesstemp99+')&('+jesstemp100+')&('+jesstemp101+')&('+jesstemp102+')&('+jesstemp103+')&('+jesstemp104+')&('+jesstemp105+')&('+jesstemp106+')&('+jesstemp107+')&('+jesstemp108+')&('+jesstemp109+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom12 x. %s)'%(9.090000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom12 x. %s)'%(9.251600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom12 x. %s)'%(10.504000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom12 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom12 x. %s)'%(6.282200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom12 x. %s)'%(6.544800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom12 x. %s)'%(10.908000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom12 x. %s)'%(9.786900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom12 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom12 x. %s)'%(6.514500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom12 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom12 x. %s)'%(5.403500+(d*0.300000)))
jesstemp110 ='jessatom0 x. %s'%(6.797300+(d*0.300000))
jesstemp111 ='jessatom1 x. %s'%(6.979100+(d*0.300000))
jesstemp112 ='jessatom2 x. %s'%(8.302200+(d*0.300000))
jesstemp113 ='jessatom3 x. %s'%(5.262100+(d*0.300000))
jesstemp114 ='jessatom4 x. %s'%(3.999600+(d*0.300000))
jesstemp115 ='jessatom5 x. %s'%(4.282400+(d*0.300000))
jesstemp116 ='jessatom6 x. %s'%(9.494000+(d*0.300000))
jesstemp117 ='jessatom7 x. %s'%(8.514300+(d*0.300000))
jesstemp118 ='jessatom8 x. %s'%(7.312400+(d*0.300000))
jesstemp119 ='jessatom9 x. %s'%(6.231700+(d*0.300000))
jesstemp120 ='jessatom10 x. %s'%(6.645800+(d*0.300000))
jesstemp121 ='jessatom11 x. %s'%(5.029800+(d*0.300000))
jesstemp122 ='jessatom12 x. %s'%(2.353300+(d*0.300000))
jesstemp123 ='br. jessatom12'
cmd.select('jessatom13', '((('+jesstemp13+')|('+jesstemp14+'))&('+jesstemp9+')&('+jesstemp110+')&('+jesstemp111+')&('+jesstemp112+')&('+jesstemp113+')&('+jesstemp114+')&('+jesstemp115+')&('+jesstemp116+')&('+jesstemp117+')&('+jesstemp118+')&('+jesstemp119+')&('+jesstemp120+')&('+jesstemp121+')&('+jesstemp122+')&('+jesstemp123+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom13 x. %s)'%(6.797300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom13 x. %s)'%(6.979100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom13 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom13 x. %s)'%(5.262100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom13 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom13 x. %s)'%(4.282400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom13 x. %s)'%(9.494000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom13 x. %s)'%(8.514300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom13 x. %s)'%(7.312400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom13 x. %s)'%(6.231700+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom13 x. %s)'%(6.645800+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom13 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom13 x. %s)'%(2.353300+(d*0.300000)))
jesstemp124 ='jessatom0 x. %s'%(8.585000+(d*0.300000))
jesstemp125 ='jessatom1 x. %s'%(8.837500+(d*0.300000))
jesstemp126 ='jessatom2 x. %s'%(10.271700+(d*0.300000))
jesstemp127 ='jessatom3 x. %s'%(5.837800+(d*0.300000))
jesstemp128 ='jessatom4 x. %s'%(5.252000+(d*0.300000))
jesstemp129 ='jessatom5 x. %s'%(5.635800+(d*0.300000))
jesstemp130 ='jessatom6 x. %s'%(11.827100+(d*0.300000))
jesstemp131 ='jessatom7 x. %s'%(10.817100+(d*0.300000))
jesstemp132 ='jessatom8 x. %s'%(9.635400+(d*0.300000))
jesstemp133 ='jessatom9 x. %s'%(8.221400+(d*0.300000))
jesstemp134 ='jessatom10 x. %s'%(8.564800+(d*0.300000))
jesstemp135 ='jessatom11 x. %s'%(7.070000+(d*0.300000))
jesstemp136 ='jessatom12 x. %s'%(2.312900+(d*0.300000))
jesstemp137 ='br. jessatom12'
jesstemp138 ='jessatom13 x. %s'%(2.343200+(d*0.300000))
cmd.select('jessatom14', '((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp9+')&('+jesstemp124+')&('+jesstemp125+')&('+jesstemp126+')&('+jesstemp127+')&('+jesstemp128+')&('+jesstemp129+')&('+jesstemp130+')&('+jesstemp131+')&('+jesstemp132+')&('+jesstemp133+')&('+jesstemp134+')&('+jesstemp135+')&('+jesstemp136+')&('+jesstemp137+')&('+jesstemp138+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom14 x. %s)'%(8.585000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom14 x. %s)'%(8.837500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom14 x. %s)'%(10.271700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom14 x. %s)'%(5.837800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom14 x. %s)'%(5.252000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom14 x. %s)'%(5.635800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom14 x. %s)'%(11.827100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom14 x. %s)'%(10.817100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom14 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom14 x. %s)'%(8.221400+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom14 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom14 x. %s)'%(7.070000+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom14 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('jessatom13', 'jessatom13 & (jessatom14 x. %s)'%(2.343200+(d*0.300000)))
cmd.select('Jfa_1pfk_2_7_1_11', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
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
