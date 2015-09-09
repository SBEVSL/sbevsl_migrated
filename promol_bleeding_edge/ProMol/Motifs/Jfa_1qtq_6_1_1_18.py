'''
FUNC:Jfa_1qtq_6_1_1_18
PDB:1qtq
EC:6.1.1.18
RESI:glu,arg,lys
LOCI:a-34,260,270;
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
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp15 ='n.  ne '
jesstemp16 ='r. arg'
jesstemp17 ='jessatom0 x. %s'%(14.624800+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(13.463300+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(15.614600+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(14.624800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(13.463300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(15.614600+(d*0.300000)))
jesstemp20 ='n.  nh1'
jesstemp21 ='n.  nh2'
jesstemp22 ='jessatom0 x. %s'%(12.473500+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(11.301900+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(13.483500+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.323000+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp16+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.473500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.301900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(13.483500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.323000+(d*0.300000)))
jesstemp27 ='n.  nh2'
jesstemp28 ='n.  nh1'
jesstemp29 ='jessatom0 x. %s'%(12.938100+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(11.817000+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(13.897600+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.323000+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp16+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp25+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.938100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.817000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(13.897600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
jesstemp34 ='r. lys'
jesstemp35 ='jessatom0 x. %s'%(7.322500+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(6.868000+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(7.989100+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(11.200900+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(9.827300+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(8.938500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.322500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.868000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.989100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.200900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.827300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.938500+(d*0.300000)))
jesstemp41 ='n.  ce '
jesstemp42 ='jessatom0 x. %s'%(6.908400+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(6.474100+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(7.756800+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(11.009000+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(9.494000+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(8.847600+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp49 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp41+')&('+jesstemp34+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.908400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.474100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.756800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(11.009000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.494000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.847600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
jesstemp50 ='n.  nz '
jesstemp51 ='jessatom0 x. %s'%(5.979200+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(5.363100+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(6.938700+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(10.382800+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(8.645600+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(8.332500+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(2.504800+(d*0.300000))
jesstemp58 ='br. jessatom6'
jesstemp59 ='jessatom7 x. %s'%(1.504900+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp50+')&('+jesstemp34+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.938700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(10.382800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.645600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.504800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.504900+(d*0.300000)))
cmd.select('Jfa_1qtq_6_1_1_18', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
