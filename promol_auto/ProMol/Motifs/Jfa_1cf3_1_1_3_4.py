'''
FUNC:Jfa_1cf3_1_1_3_4
PDB:1cf3
EC:1.1.3.4
RESI:glu,his,his
LOCI:a-412,516,559;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  oe1'
jesstemp4 ='n.  oe2'
jesstemp5 ='n.  od1'
jesstemp6 ='n.  od2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  oe2'
jesstemp10 ='n.  oe1'
jesstemp11 ='n.  od2'
jesstemp12 ='n.  od1'
jesstemp13 ='jessatom0 x. %s'%(1.272600+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.232100+(d*0.300000)))
jesstemp16 ='n.  cg '
jesstemp17 ='r. his'
jesstemp18 ='jessatom0 x. %s'%(9.393000+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(8.342600+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(9.716200+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.393000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.342600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.716200+(d*0.300000)))
jesstemp21 ='n.  nd1'
jesstemp22 ='jessatom0 x. %s'%(8.130500+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(7.039700+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(8.534500+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.403900+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp21+')&('+jesstemp17+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.130500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.534500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.403900+(d*0.300000)))
jesstemp27 ='n.  ne2'
jesstemp28 ='jessatom0 x. %s'%(8.484000+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(7.534600+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(8.554700+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(2.211900+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp27+')&('+jesstemp17+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.484000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.534600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.554700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.181600+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(5.262100+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(4.797500+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(4.777300+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(7.272000+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(6.302400+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(5.393400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.262100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.272000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.302400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.393400+(d*0.300000)))
jesstemp40 ='jessatom1 x. %s'%(4.858100+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(4.726800+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(6.726600+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(5.878200+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(4.837900+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp21+')&('+jesstemp17+')&('+jesstemp34+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.262100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.726800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.726600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.837900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp47 ='jessatom0 x. %s'%(3.393600+(d*0.300000))
jesstemp48 ='jessatom1 x. %s'%(3.333000+(d*0.300000))
jesstemp49 ='jessatom2 x. %s'%(2.666400+(d*0.300000))
jesstemp50 ='jessatom3 x. %s'%(8.201200+(d*0.300000))
jesstemp51 ='jessatom4 x. %s'%(7.130600+(d*0.300000))
jesstemp52 ='jessatom5 x. %s'%(6.605400+(d*0.300000))
jesstemp53 ='jessatom6 x. %s'%(2.222000+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp27+')&('+jesstemp17+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(3.393600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.333000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(2.666400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.130600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.605400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.171500+(d*0.300000)))
cmd.select('Jfa_1cf3_1_1_3_4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
