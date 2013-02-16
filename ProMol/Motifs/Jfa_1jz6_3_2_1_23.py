'''
FUNC:Jfa_1jz6_3_2_1_23
PDB:1jz6
EC:3.2.1.23
RESI:glu,tyr,glu
LOCI:a-461,503,537;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  oe2'
jesstemp4 ='n.  oe1'
jesstemp5 ='n.  od2'
jesstemp6 ='n.  od1'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  oe1'
jesstemp10 ='n.  oe2'
jesstemp11 ='n.  od1'
jesstemp12 ='n.  od2'
jesstemp13 ='jessatom0 x. %s'%(1.353400+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.282600+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.282600+(d*0.300000)))
jesstemp16 ='n.  ce1'
jesstemp17 ='r. tyr'
jesstemp18 ='jessatom0 x. %s'%(9.362700+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(9.554600+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(8.393100+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.362700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.554600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(8.393100+(d*0.300000)))
jesstemp21 ='n.  cz '
jesstemp22 ='jessatom0 x. %s'%(7.999200+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(8.160800+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(7.090200+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.414000+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp21+')&('+jesstemp17+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.999200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.414000+(d*0.300000)))
jesstemp27 ='n.  oh '
jesstemp28 ='jessatom0 x. %s'%(7.817400+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(7.766900+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(2.434100+(d*0.300000))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(1.403900+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp27+')&('+jesstemp17+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp24+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.766900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.434100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.403900+(d*0.300000)))
jesstemp33 ='jessatom0 x. %s'%(6.120600+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(6.191300+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(5.817600+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(5.353000+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(4.171300+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(3.636000+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.120600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.191300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.817600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.353000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.171300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.636000+(d*0.300000)))
jesstemp39 ='jessatom0 x. %s'%(5.565100+(d*0.300000))
jesstemp40 ='jessatom1 x. %s'%(5.565100+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(5.524700+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(6.575100+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(5.342900+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(4.747000+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.565100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.565100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.524700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.342900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp47 ='jessatom0 x. %s'%(5.878200+(d*0.300000))
jesstemp48 ='jessatom1 x. %s'%(5.908500+(d*0.300000))
jesstemp49 ='jessatom2 x. %s'%(5.403500+(d*0.300000))
jesstemp50 ='jessatom3 x. %s'%(4.514700+(d*0.300000))
jesstemp51 ='jessatom4 x. %s'%(3.191600+(d*0.300000))
jesstemp52 ='jessatom5 x. %s'%(2.605800+(d*0.300000))
jesstemp53 ='jessatom6 x. %s'%(1.292800+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.908500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.403500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.514700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(3.191600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(2.605800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.292800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('Jfa_1jz6_3_2_1_23', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
