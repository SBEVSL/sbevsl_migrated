'''
FUNC:Jfa_1h1y-H36A-D38A-H69A-D178A
PDB:1h1y
EC:5.1.3.1
PFAM:PF00834
RESI:his,asp,his,asp
LOCI:a-36,38,69,178;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.393800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.393800+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.222000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp10 ='r. asp'
jesstemp11 ='r. glu'
jesstemp12 ='jessatom0 x. %s'%(5.110600+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(5.868100+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.070300+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp10+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.110600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.868100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.070300+(d*0.300000)))
jesstemp15 ='n.  od1'
jesstemp16 ='n.  od2'
jesstemp17 ='n.  oe1'
jesstemp18 ='n.  oe2'
jesstemp19 ='jessatom0 x. %s'%(5.029800+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(5.524700+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(3.494600+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+'))|((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.524700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.494600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp24 ='n.  od2'
jesstemp25 ='n.  od1'
jesstemp26 ='n.  oe2'
jesstemp27 ='n.  oe1'
jesstemp28 ='jessatom0 x. %s'%(4.787400+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(5.777200+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(4.201600+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+'))|((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.787400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.777200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.201600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(6.181200+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(5.615600+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(4.141000+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(5.464100+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(4.373300+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(6.413500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.181200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.615600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.141000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.464100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.373300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.413500+(d*0.300000)))
jesstemp40 ='jessatom0 x. %s'%(6.070100+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(5.656000+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(3.868300+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(4.949000+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(3.737000+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(5.827700+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.070100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.656000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.868300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.737000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp48 ='jessatom0 x. %s'%(8.080000+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(7.484100+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(5.918600+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(6.857900+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(5.656000+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(7.837600+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(2.211900+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.080000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.484100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.656000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.837600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
jesstemp57 ='jessatom0 x. %s'%(5.686300+(d*0.300000))
jesstemp58 ='jessatom1 x. %s'%(5.918600+(d*0.300000))
jesstemp59 ='jessatom2 x. %s'%(4.605600+(d*0.300000))
jesstemp60 ='jessatom3 x. %s'%(5.807500+(d*0.300000))
jesstemp61 ='jessatom4 x. %s'%(5.151000+(d*0.300000))
jesstemp62 ='jessatom5 x. %s'%(5.534800+(d*0.300000))
jesstemp63 ='jessatom6 x. %s'%(6.696300+(d*0.300000))
jesstemp64 ='jessatom7 x. %s'%(5.504500+(d*0.300000))
jesstemp65 ='jessatom8 x. %s'%(7.150800+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp10+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(4.605600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(5.151000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(5.534800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(5.504500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(7.150800+(d*0.300000)))
jesstemp66 ='jessatom0 x. %s'%(6.140800+(d*0.300000))
jesstemp67 ='jessatom1 x. %s'%(6.595300+(d*0.300000))
jesstemp68 ='jessatom2 x. %s'%(5.413600+(d*0.300000))
jesstemp69 ='jessatom3 x. %s'%(6.150900+(d*0.300000))
jesstemp70 ='jessatom4 x. %s'%(5.716600+(d*0.300000))
jesstemp71 ='jessatom5 x. %s'%(5.645900+(d*0.300000))
jesstemp72 ='jessatom6 x. %s'%(7.817400+(d*0.300000))
jesstemp73 ='jessatom7 x. %s'%(6.635700+(d*0.300000))
jesstemp74 ='jessatom8 x. %s'%(8.332500+(d*0.300000))
jesstemp75 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp76 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+'))|((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+')))&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(6.595300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(6.150900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(5.716600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(5.645900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp77 ='jessatom0 x. %s'%(5.171200+(d*0.300000))
jesstemp78 ='jessatom1 x. %s'%(5.423700+(d*0.300000))
jesstemp79 ='jessatom2 x. %s'%(3.777400+(d*0.300000))
jesstemp80 ='jessatom3 x. %s'%(4.696500+(d*0.300000))
jesstemp81 ='jessatom4 x. %s'%(3.949100+(d*0.300000))
jesstemp82 ='jessatom5 x. %s'%(4.595500+(d*0.300000))
jesstemp83 ='jessatom6 x. %s'%(5.635800+(d*0.300000))
jesstemp84 ='jessatom7 x. %s'%(4.444000+(d*0.300000))
jesstemp85 ='jessatom8 x. %s'%(6.221600+(d*0.300000))
jesstemp86 ='jessatom9 x. %s'%(1.252400+(d*0.300000))
jesstemp87 ='br. jessatom9'
jesstemp88 ='jessatom10 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+'))|((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+')))&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(5.423700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(3.777400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(4.696500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(3.949100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(5.635800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(4.444000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.221600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('Jfa_1h1y-H36A-D38A-H69A-D178A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
