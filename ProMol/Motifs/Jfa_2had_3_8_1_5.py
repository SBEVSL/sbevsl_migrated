'''
FUNC:Jfa_2had_3_8_1_5
PDB:2had
EC:3.8.1.5
RESI:asp,asp,his
LOCI:a-124,260,289;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.222100+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.222100+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.313000+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.313000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.242200+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(8.645600+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(7.756800+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(9.857600+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.645600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.756800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.857600+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(8.554700+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(7.575000+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(9.706100+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.222100+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.554700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.575000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.706100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.222100+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(7.766900+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(6.948800+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(9.039500+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(1.323100+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.766900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.039500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.323100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.242200+(d*0.300000)))
jesstemp30 ='r. his'
jesstemp31 ='jessatom0 x. %s'%(5.585300+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(4.888400+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(6.645800+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(3.949100+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(3.797600+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(3.676400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.888400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.645800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(3.949100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.797600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.676400+(d*0.300000)))
jesstemp37 ='n.  nd1'
jesstemp38 ='jessatom0 x. %s'%(5.252000+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(4.444000+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(6.443800+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(3.484500+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(3.484500+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(2.848200+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(1.383700+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp37+')&('+jesstemp30+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.252000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.444000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.443800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.484500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.484500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(2.848200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.383700+(d*0.300000)))
jesstemp46 ='n.  ne2'
jesstemp47 ='jessatom0 x. %s'%(3.423900+(d*0.300000))
jesstemp48 ='jessatom1 x. %s'%(2.737100+(d*0.300000))
jesstemp49 ='jessatom2 x. %s'%(4.474300+(d*0.300000))
jesstemp50 ='jessatom3 x. %s'%(5.625700+(d*0.300000))
jesstemp51 ='jessatom4 x. %s'%(5.443900+(d*0.300000))
jesstemp52 ='jessatom5 x. %s'%(5.019700+(d*0.300000))
jesstemp53 ='jessatom6 x. %s'%(2.191700+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp46+')&('+jesstemp30+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(3.423900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(2.737100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.474300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.443900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.181600+(d*0.300000)))
cmd.select('Jfa_2had_3_8_1_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
