'''
FUNC:Jfa_1daa_2_6_1_21
PDB:1daa
EC:2.6.1.21
RESI:lys,glu,leu
LOCI:a-145,177,201;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. lys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  ce '
jesstemp3 ='r. lys'
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='n.  nz '
jesstemp7 ='jessatom0 x. %s'%(2.434100+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.454400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.434100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.454400+(d*0.300000)))
jesstemp10 ='r. glu'
jesstemp11 ='r. asp'
jesstemp12 ='jessatom0 x. %s'%(10.079800+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(10.433300+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(9.312200+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp10+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.079800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.433300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.312200+(d*0.300000)))
jesstemp15 ='n.  oe1'
jesstemp16 ='n.  oe2'
jesstemp17 ='n.  od1'
jesstemp18 ='n.  od2'
jesstemp19 ='jessatom0 x. %s'%(9.332400+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(9.665700+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(8.564800+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.232200+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+'))|((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.332400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.665700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.232200+(d*0.300000)))
jesstemp24 ='n.  oe2'
jesstemp25 ='n.  oe1'
jesstemp26 ='n.  od2'
jesstemp27 ='n.  od1'
jesstemp28 ='jessatom0 x. %s'%(9.837400+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(10.302000+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(9.241500+(d*0.300000))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(2.121000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+'))|((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp22+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.837400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.302000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.232200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.121000+(d*0.300000)))
jesstemp33 ='n.  cg '
jesstemp34 ='r. leu'
jesstemp35 ='jessatom0 x. %s'%(5.019700+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(5.898400+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(5.474200+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(6.201400+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(5.312600+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(6.100400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.898400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.474200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.100400+(d*0.300000)))
jesstemp41 ='n.  cd1'
jesstemp42 ='n.  cd2'
jesstemp43 ='jessatom0 x. %s'%(4.757100+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(5.948900+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(5.817600+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(7.130600+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(6.403400+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(6.797300+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp50 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp41+')|('+jesstemp42+'))&('+jesstemp34+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.757100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.948900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.817600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.130600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.403400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.797300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
jesstemp51 ='n.  cd2'
jesstemp52 ='n.  cd1'
jesstemp53 ='jessatom0 x. %s'%(3.999600+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(4.615700+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(4.040000+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(6.534700+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(5.615600+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(6.514500+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(1.515000+(d*0.300000))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(2.504800+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp51+')|('+jesstemp52+'))&('+jesstemp34+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.615700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.040000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.534700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.615600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.514500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.515000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.504800+(d*0.300000)))
cmd.select('Jfa_1daa_2_6_1_21', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
