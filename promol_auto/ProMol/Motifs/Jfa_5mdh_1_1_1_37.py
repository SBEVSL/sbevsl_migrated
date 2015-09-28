'''
FUNC:Jfa_5mdh_1_1_1_37
PDB:5mdh
EC:1.1.1.37
RESI:asp,asn
LOCI:a-158,185;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.272600+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.272600+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp16 ='n.  ne '
jesstemp17 ='r. arg'
jesstemp18 ='jessatom0 x. %s'%(6.251900+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(5.363100+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(7.352800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.251900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.352800+(d*0.300000)))
jesstemp21 ='n.  nh1'
jesstemp22 ='n.  nh2'
jesstemp23 ='jessatom0 x. %s'%(4.959100+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(3.817800+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(5.878200+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(2.363400+(d*0.300000))
jesstemp27 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp21+')|('+jesstemp22+'))&('+jesstemp17+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.959100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.817800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.363400+(d*0.300000)))
jesstemp28 ='n.  nh2'
jesstemp29 ='n.  nh1'
jesstemp30 ='jessatom0 x. %s'%(7.201300+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.130700+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(8.100200+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(2.302800+(d*0.300000))
jesstemp34 ='br. jessatom3'
jesstemp35 ='jessatom4 x. %s'%(2.353300+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp28+')|('+jesstemp29+'))&('+jesstemp17+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.201300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.130700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.100200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.302800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.353300+(d*0.300000)))
jesstemp36 ='r. his'
jesstemp37 ='jessatom0 x. %s'%(4.676300+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(4.666200+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(3.817800+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(9.009200+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(6.908400+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(8.746600+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(4.676300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.666200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(3.817800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.009200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.908400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.746600+(d*0.300000)))
jesstemp43 ='n.  nd1'
jesstemp44 ='jessatom0 x. %s'%(3.312800+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(3.272400+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(2.595700+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(7.817400+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(5.807500+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(7.797200+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.403900+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp43+')&('+jesstemp36+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(3.312800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(3.272400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(2.595700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.797200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.403900+(d*0.300000)))
jesstemp52 ='n.  ne2'
jesstemp53 ='jessatom0 x. %s'%(4.837900+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(4.353100+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(4.484400+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(7.494200+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(5.332800+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(6.857900+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(2.171500+(d*0.300000))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(2.141200+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp52+')&('+jesstemp36+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.837900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.353100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.484400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.494200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.332800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.171500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.141200+(d*0.300000)))
cmd.select('Jfa_5mdh_1_1_1_37', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
