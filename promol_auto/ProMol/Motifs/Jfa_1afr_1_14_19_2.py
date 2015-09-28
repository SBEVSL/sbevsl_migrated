'''
FUNC:Jfa_1afr_1_14_19_2
PDB:1afr
EC:1.14.19.2
RESI:trp,his,thr,asp
LOCI:a-62,146,199,228;
'''
jesstemp0 ='n.  ne1'
jesstemp1 ='r. trp'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cz2'
jesstemp3 ='r. trp'
jesstemp4 ='jessatom0 x. %s'%(2.555300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.555300+(d*0.300000)))
jesstemp6 ='n.  ch2'
jesstemp7 ='jessatom0 x. %s'%(3.737000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.383700+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.737000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.383700+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. his'
jesstemp12 ='jessatom0 x. %s'%(6.948800+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(4.938900+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.949000+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.949000+(d*0.300000)))
jesstemp15 ='n.  nd1'
jesstemp16 ='jessatom0 x. %s'%(7.403300+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(5.706500+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(5.979200+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.706500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp21 ='n.  ne2'
jesstemp22 ='jessatom0 x. %s'%(5.373200+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(4.019800+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(4.625800+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.211900+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.373200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.019800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp28 ='n.  ca '
jesstemp29 ='r. thr'
jesstemp30 ='r. ser'
jesstemp31 ='jessatom0 x. %s'%(13.927900+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(12.887600+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(13.362300+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(9.524300+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(8.322400+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(9.918200+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp28+')&('+jesstemp29+'))|(('+jesstemp28+')&('+jesstemp30+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(13.927900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(12.887600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(13.362300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.524300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.322400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.918200+(d*0.300000)))
jesstemp37 ='n.  cb '
jesstemp38 ='jessatom0 x. %s'%(13.089600+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(11.958400+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(12.412900+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(8.292100+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(7.059900+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(8.736500+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(1.555400+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp37+')&('+jesstemp29+'))|(('+jesstemp37+')&('+jesstemp30+')))&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(13.089600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.958400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(12.412900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.292100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.059900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.736500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.555400+(d*0.300000)))
jesstemp46 ='n.  og1'
jesstemp47 ='jessatom0 x. %s'%(12.604800+(d*0.300000))
jesstemp48 ='jessatom1 x. %s'%(11.695800+(d*0.300000))
jesstemp49 ='jessatom2 x. %s'%(12.281600+(d*0.300000))
jesstemp50 ='jessatom3 x. %s'%(8.231500+(d*0.300000))
jesstemp51 ='jessatom4 x. %s'%(6.888200+(d*0.300000))
jesstemp52 ='jessatom5 x. %s'%(8.332500+(d*0.300000))
jesstemp53 ='jessatom6 x. %s'%(2.454300+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(1.444300+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp46+')&('+jesstemp29+'))|(('+jesstemp46+')&('+jesstemp30+')))&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(12.604800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(11.695800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(12.281600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.231500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.888200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.444300+(d*0.300000)))
jesstemp56 ='r. asp'
jesstemp57 ='r. glu'
jesstemp58 ='jessatom0 x. %s'%(3.625900+(d*0.300000))
jesstemp59 ='jessatom1 x. %s'%(4.343000+(d*0.300000))
jesstemp60 ='jessatom2 x. %s'%(5.635800+(d*0.300000))
jesstemp61 ='jessatom3 x. %s'%(5.807500+(d*0.300000))
jesstemp62 ='jessatom4 x. %s'%(5.615600+(d*0.300000))
jesstemp63 ='jessatom5 x. %s'%(3.636000+(d*0.300000))
jesstemp64 ='jessatom6 x. %s'%(11.473600+(d*0.300000))
jesstemp65 ='jessatom7 x. %s'%(10.524200+(d*0.300000))
jesstemp66 ='jessatom8 x. %s'%(9.776800+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp10+')&('+jesstemp56+'))|(('+jesstemp10+')&('+jesstemp57+')))&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(3.625900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(4.343000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(5.635800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(5.615600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(3.636000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(11.473600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(10.524200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(9.776800+(d*0.300000)))
jesstemp67 ='n.  od1'
jesstemp68 ='n.  od2'
jesstemp69 ='n.  oe1'
jesstemp70 ='n.  oe2'
jesstemp71 ='jessatom0 x. %s'%(3.181500+(d*0.300000))
jesstemp72 ='jessatom1 x. %s'%(4.575300+(d*0.300000))
jesstemp73 ='jessatom2 x. %s'%(5.948900+(d*0.300000))
jesstemp74 ='jessatom3 x. %s'%(6.847800+(d*0.300000))
jesstemp75 ='jessatom4 x. %s'%(6.696300+(d*0.300000))
jesstemp76 ='jessatom5 x. %s'%(4.747000+(d*0.300000))
jesstemp77 ='jessatom6 x. %s'%(12.140200+(d*0.300000))
jesstemp78 ='jessatom7 x. %s'%(11.312000+(d*0.300000))
jesstemp79 ='jessatom8 x. %s'%(10.544400+(d*0.300000))
jesstemp80 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp81 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp67+')|('+jesstemp68+'))&('+jesstemp56+'))|((('+jesstemp69+')|('+jesstemp70+'))&('+jesstemp57+')))&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(3.181500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(4.575300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(5.948900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(6.847800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(12.140200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(11.312000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(10.544400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp82 ='n.  od2'
jesstemp83 ='n.  od1'
jesstemp84 ='n.  oe2'
jesstemp85 ='n.  oe1'
jesstemp86 ='jessatom0 x. %s'%(3.393600+(d*0.300000))
jesstemp87 ='jessatom1 x. %s'%(3.716800+(d*0.300000))
jesstemp88 ='jessatom2 x. %s'%(4.908600+(d*0.300000))
jesstemp89 ='jessatom3 x. %s'%(5.231800+(d*0.300000))
jesstemp90 ='jessatom4 x. %s'%(5.272200+(d*0.300000))
jesstemp91 ='jessatom5 x. %s'%(3.100700+(d*0.300000))
jesstemp92 ='jessatom6 x. %s'%(11.978600+(d*0.300000))
jesstemp93 ='jessatom7 x. %s'%(10.928200+(d*0.300000))
jesstemp94 ='jessatom8 x. %s'%(10.241400+(d*0.300000))
jesstemp95 ='br. jessatom9'
jesstemp96 ='jessatom10 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp82+')|('+jesstemp83+'))&('+jesstemp56+'))|((('+jesstemp84+')|('+jesstemp85+'))&('+jesstemp57+')))&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp80+')&('+jesstemp95+')&('+jesstemp96+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(3.393600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(3.716800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.908600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(5.272200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(3.100700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(11.978600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(10.928200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(10.241400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1afr_1_14_19_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
