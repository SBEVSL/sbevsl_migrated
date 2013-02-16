'''
FUNC:Jfa_12as_6_3_1_1
PDB:12as
EC:6.3.1.1
RESI:asp,arg,gln
LOCI:a-46,100,116;
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
jesstemp15 ='n.  ne '
jesstemp16 ='r. arg'
jesstemp17 ='jessatom0 x. %s'%(7.423500+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(7.958800+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(6.666000+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.423500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.958800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.666000+(d*0.300000)))
jesstemp20 ='n.  nh1'
jesstemp21 ='n.  nh2'
jesstemp22 ='jessatom0 x. %s'%(6.433700+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(6.746800+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(5.605500+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.272500+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp16+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.433700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.746800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.605500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.272500+(d*0.300000)))
jesstemp27 ='n.  nh2'
jesstemp28 ='n.  nh1'
jesstemp29 ='jessatom0 x. %s'%(5.827700+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(6.544800+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(4.858100+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(2.323000+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp16+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.544800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.272500+(d*0.300000)))
jesstemp35 ='n.  cd '
jesstemp36 ='r. gln'
jesstemp37 ='r. asn'
jesstemp38 ='jessatom0 x. %s'%(8.423400+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(9.382900+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(7.211400+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(6.524600+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(6.464000+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(4.797500+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp35+')&('+jesstemp36+'))|(('+jesstemp35+')&('+jesstemp37+')))&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.423400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.382900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.211400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.524600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.464000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.797500+(d*0.300000)))
jesstemp44 ='jessatom0 x. %s'%(7.766900+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(8.665800+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(6.554900+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(5.363100+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(5.231800+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(3.636000+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp5+')&('+jesstemp36+'))|(('+jesstemp5+')&('+jesstemp37+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.766900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.665800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.554900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.636000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp52 ='n.  ne2'
jesstemp53 ='jessatom0 x. %s'%(8.029500+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(9.039500+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(6.857900+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(7.383100+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(7.171000+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(5.403500+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(1.343300+(d*0.300000))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp52+')&('+jesstemp36+'))|(('+jesstemp52+')&('+jesstemp37+')))&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.029500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.039500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.383100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.171000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.403500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.262400+(d*0.300000)))
cmd.select('Jfa_12as_6_3_1_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
