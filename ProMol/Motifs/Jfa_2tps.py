'''
FUNC:Jfa_2tps
PDB:2tps
EC:2.5.1.3
PFAM:PF05690,PF02581
RESI:arg,ser,lys
LOCI:a-59,130,159;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.292700+(d*0.300000))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.292700+(d*0.300000)))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='jessatom0 x. %s'%(2.282600+(d*0.300000))
jesstemp10 ='br. jessatom0'
jesstemp11 ='jessatom1 x. %s'%(2.343200+(d*0.300000))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.282600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.343200+(d*0.300000)))
jesstemp12 ='n.  ca '
jesstemp13 ='r. ser'
jesstemp14 ='r. thr'
jesstemp15 ='jessatom0 x. %s'%(10.746400+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(12.756300+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(11.382700+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp12+')&('+jesstemp13+'))|(('+jesstemp12+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.746400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.756300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(11.382700+(d*0.300000)))
jesstemp18 ='n.  cb '
jesstemp19 ='jessatom0 x. %s'%(9.514200+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(11.493800+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(9.988900+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp18+')&('+jesstemp13+'))|(('+jesstemp18+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.514200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.493800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.988900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp24 ='n.  og '
jesstemp25 ='jessatom0 x. %s'%(8.282000+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(10.302000+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(8.968800+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(2.464400+(d*0.300000))
jesstemp29 ='br. jessatom3'
jesstemp30 ='jessatom4 x. %s'%(1.454400+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp24+')&('+jesstemp13+'))|(('+jesstemp24+')&('+jesstemp14+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.282000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.302000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.968800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.464400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.454400+(d*0.300000)))
jesstemp31 ='n.  cd '
jesstemp32 ='r. lys'
jesstemp33 ='jessatom0 x. %s'%(5.413600+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(6.019600+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(4.060200+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(9.271800+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(7.817400+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(7.211400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.019600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.060200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.211400+(d*0.300000)))
jesstemp39 ='n.  ce '
jesstemp40 ='jessatom0 x. %s'%(6.272100+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(7.150800+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(4.979300+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(8.706200+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(7.201300+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(6.827600+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.525100+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp39+')&('+jesstemp32+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.272100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.150800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.979300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.201300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.827600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.525100+(d*0.300000)))
jesstemp48 ='n.  nz '
jesstemp49 ='jessatom0 x. %s'%(6.110500+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(7.029600+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(4.706600+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(9.261700+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(7.716400+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(7.332600+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(2.545200+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(1.494800+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp48+')&('+jesstemp32+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.110500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.706600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.261700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.716400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.332600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.545200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.494800+(d*0.300000)))
cmd.select('Jfa_2tps', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
