'''
FUNC:Jfa_1i2r_2_2_1_2
PDB:1i2r
EC:2.2.1.2
RESI:asp,glu,lys
LOCI:a-17,96,132;
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
jesstemp14 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp15 ='n.  cd '
jesstemp16 ='jessatom0 x. %s'%(10.817100+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(9.837400+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(10.807000+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp15+')&('+jesstemp2+'))|(('+jesstemp15+')&('+jesstemp1+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.817100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.837400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(10.807000+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(9.554600+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(8.574900+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(9.564700+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+'))|((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.554600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.574900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.564700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(11.503900+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(10.605000+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(11.372600+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+'))|((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp22+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.503900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.605000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.372600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp29 ='r. lys'
jesstemp30 ='jessatom0 x. %s'%(8.312300+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(7.241700+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(8.625400+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(4.403600+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(3.676400+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(5.332800+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp15+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.312300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.241700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.625400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.403600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.676400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.332800+(d*0.300000)))
jesstemp36 ='n.  ce '
jesstemp37 ='jessatom0 x. %s'%(7.383100+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(6.443800+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(7.534600+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(4.736900+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(3.827900+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(5.454000+(d*0.300000))
jesstemp43 ='jessatom6 x. %s'%(1.525100+(d*0.300000))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp36+')&('+jesstemp29+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.383100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.443800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.534600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.736900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.827900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.454000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.525100+(d*0.300000)))
jesstemp45 ='n.  nz '
jesstemp46 ='jessatom0 x. %s'%(5.959000+(d*0.300000))
jesstemp47 ='jessatom1 x. %s'%(4.979300+(d*0.300000))
jesstemp48 ='jessatom2 x. %s'%(6.150900+(d*0.300000))
jesstemp49 ='jessatom3 x. %s'%(5.464100+(d*0.300000))
jesstemp50 ='jessatom4 x. %s'%(4.332900+(d*0.300000))
jesstemp51 ='jessatom5 x. %s'%(6.241800+(d*0.300000))
jesstemp52 ='jessatom6 x. %s'%(2.514900+(d*0.300000))
jesstemp53 ='br. jessatom6'
jesstemp54 ='jessatom7 x. %s'%(1.494800+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp45+')&('+jesstemp29+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.979300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.150900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.464100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.332900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.514900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.494800+(d*0.300000)))
cmd.select('Jfa_1i2r_2_2_1_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
