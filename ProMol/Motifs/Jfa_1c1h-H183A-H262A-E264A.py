'''
FUNC:Jfa_1c1h-H183A-H262A-E264A
PDB:1c1h
EC:4.99.1.1
PFAM:PF00762
RESI:his,his,glu
LOCI:a-183,262,264;
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
jesstemp10 ='jessatom0 x. %s'%(10.938300+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(12.079600+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(10.584800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.938300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.079600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(10.584800+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(12.332100+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(13.453200+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(11.918000+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp17 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.332100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.453200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(11.918000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(11.897800+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(13.039100+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(11.705900+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(2.222000+(d*0.300000))
jesstemp22 ='br. jessatom3'
jesstemp23 ='jessatom4 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.897800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.039100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.705900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.161400+(d*0.300000)))
jesstemp24 ='n.  cd '
jesstemp25 ='r. glu'
jesstemp26 ='r. asp'
jesstemp27 ='jessatom0 x. %s'%(5.918600+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(6.807400+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(4.999500+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(5.999400+(d*0.300000))
jesstemp31 ='jessatom4 x. %s'%(7.272000+(d*0.300000))
jesstemp32 ='jessatom5 x. %s'%(7.595200+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp24+')&('+jesstemp25+'))|(('+jesstemp24+')&('+jesstemp26+')))&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.807400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.999400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.272000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.595200+(d*0.300000)))
jesstemp33 ='n.  oe1'
jesstemp34 ='n.  oe2'
jesstemp35 ='n.  od1'
jesstemp36 ='n.  od2'
jesstemp37 ='jessatom0 x. %s'%(6.080200+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(6.767000+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(4.777300+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(6.464000+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(7.665900+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(7.938600+(d*0.300000))
jesstemp43 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp33+')|('+jesstemp34+'))&('+jesstemp25+'))|((('+jesstemp35+')|('+jesstemp36+'))&('+jesstemp26+')))&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.080200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.767000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.464000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp45 ='n.  oe2'
jesstemp46 ='n.  oe1'
jesstemp47 ='n.  od2'
jesstemp48 ='n.  od1'
jesstemp49 ='jessatom0 x. %s'%(6.706400+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(7.726500+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(6.060000+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(4.807600+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(6.100400+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(6.453900+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp45+')|('+jesstemp46+'))&('+jesstemp25+'))|((('+jesstemp47+')|('+jesstemp48+'))&('+jesstemp26+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp43+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.706400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.726500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.807600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.100400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.453900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1c1h-H183A-H262A-E264A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
