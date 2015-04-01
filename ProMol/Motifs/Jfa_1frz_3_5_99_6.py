'''
FUNC:Jfa_1frz_3_5_99_6
PDB:1frz
EC:3.5.99.6
RESI:asp,asp,his,glu
LOCI:a-72,141,143,148;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp15 ='jessatom0 x. %s'%(13.049200+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(13.584500+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(12.059400+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(13.049200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(13.584500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(12.059400+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(12.200800+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(12.726000+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(11.170600+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(1.272600+(d*0.300000))
jesstemp22 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.200800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.726000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(11.170600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.272600+(d*0.300000)))
jesstemp23 ='jessatom0 x. %s'%(12.806800+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(13.372400+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(11.887700+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp21+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.806800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.372400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.887700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp28 ='r. his'
jesstemp29 ='jessatom0 x. %s'%(8.837500+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(9.453600+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(7.746700+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(4.514700+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(3.514800+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(4.706600+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.837500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.453600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.746700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.514700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.514800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.706600+(d*0.300000)))
jesstemp35 ='n.  nd1'
jesstemp36 ='jessatom0 x. %s'%(9.090000+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(9.635400+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(8.110300+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(3.959200+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(3.191600+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(3.888500+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.383700+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp35+')&('+jesstemp28+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.090000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.110300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.959200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.191600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.888500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.383700+(d*0.300000)))
jesstemp44 ='n.  ne2'
jesstemp45 ='jessatom0 x. %s'%(7.948700+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(8.302200+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(6.969000+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(5.615600+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(4.625800+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(5.777200+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(2.222000+(d*0.300000))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp44+')&('+jesstemp28+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.948700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.969000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.615600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.777200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
jesstemp54 ='n.  cd '
jesstemp55 ='jessatom0 x. %s'%(10.140400+(d*0.300000))
jesstemp56 ='jessatom1 x. %s'%(10.847400+(d*0.300000))
jesstemp57 ='jessatom2 x. %s'%(9.403100+(d*0.300000))
jesstemp58 ='jessatom3 x. %s'%(5.080300+(d*0.300000))
jesstemp59 ='jessatom4 x. %s'%(5.231800+(d*0.300000))
jesstemp60 ='jessatom5 x. %s'%(4.080400+(d*0.300000))
jesstemp61 ='jessatom6 x. %s'%(4.635900+(d*0.300000))
jesstemp62 ='jessatom7 x. %s'%(3.747100+(d*0.300000))
jesstemp63 ='jessatom8 x. %s'%(5.595400+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp54+')&('+jesstemp2+'))|(('+jesstemp54+')&('+jesstemp1+')))&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(10.140400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(10.847400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(9.403100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(5.080300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(4.080400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(4.635900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(3.747100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(5.595400+(d*0.300000)))
jesstemp64 ='jessatom0 x. %s'%(10.251500+(d*0.300000))
jesstemp65 ='jessatom1 x. %s'%(10.938300+(d*0.300000))
jesstemp66 ='jessatom4 x. %s'%(3.999600+(d*0.300000))
jesstemp67 ='jessatom5 x. %s'%(3.120900+(d*0.300000))
jesstemp68 ='jessatom6 x. %s'%(3.625900+(d*0.300000))
jesstemp69 ='jessatom7 x. %s'%(2.727000+(d*0.300000))
jesstemp70 ='jessatom8 x. %s'%(4.777300+(d*0.300000))
jesstemp71 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp72 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+'))|((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+')))&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp57+')&('+jesstemp39+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(10.251500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(10.938300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(9.403100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(3.959200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(3.120900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(3.625900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(2.727000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp73 ='jessatom0 x. %s'%(10.362600+(d*0.300000))
jesstemp74 ='jessatom1 x. %s'%(10.978700+(d*0.300000))
jesstemp75 ='jessatom2 x. %s'%(9.736400+(d*0.300000))
jesstemp76 ='jessatom3 x. %s'%(5.605500+(d*0.300000))
jesstemp77 ='jessatom4 x. %s'%(5.878200+(d*0.300000))
jesstemp78 ='jessatom5 x. %s'%(4.514700+(d*0.300000))
jesstemp79 ='jessatom6 x. %s'%(5.494400+(d*0.300000))
jesstemp80 ='jessatom7 x. %s'%(4.393500+(d*0.300000))
jesstemp81 ='jessatom8 x. %s'%(6.039800+(d*0.300000))
jesstemp82 ='br. jessatom9'
jesstemp83 ='jessatom10 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+'))|((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+')))&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp71+')&('+jesstemp82+')&('+jesstemp83+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(10.362600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(10.978700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(9.736400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(5.605500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(4.514700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(5.494400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(4.393500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.039800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1frz_3_5_99_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
