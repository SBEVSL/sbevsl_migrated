'''
FUNC:Jfa_1upu
PDB:1upu
EC:2.4.2.9
PFAM:PF14681
RESI:arg,thr,asp
LOCI:a-137,141,235;b-37,141,235;c-37,141,235;d-37,141,235;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.333100+(d*0.300000))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.333100+(d*0.300000)))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='br. jessatom0'
jesstemp10 ='jessatom1 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp9+')&('+jesstemp10+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.333100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.312900+(d*0.300000)))
jesstemp11 ='n.  ca '
jesstemp12 ='r. thr'
jesstemp13 ='r. ser'
jesstemp14 ='jessatom0 x. %s'%(9.776800+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(10.302000+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(11.413000+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp11+')&('+jesstemp12+'))|(('+jesstemp11+')&('+jesstemp13+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.776800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.302000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(11.413000+(d*0.300000)))
jesstemp17 ='n.  cb '
jesstemp18 ='jessatom0 x. %s'%(9.797000+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(10.403000+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(11.241300+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(1.585700+(d*0.300000))
jesstemp22 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp17+')&('+jesstemp12+'))|(('+jesstemp17+')&('+jesstemp13+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.797000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(10.403000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(11.241300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.585700+(d*0.300000)))
jesstemp23 ='n.  og1'
jesstemp24 ='jessatom0 x. %s'%(9.948500+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(10.857500+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(11.493800+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.504800+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(1.454400+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp23+')&('+jesstemp12+'))|(('+jesstemp23+')&('+jesstemp13+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.948500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.857500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.493800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.504800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.454400+(d*0.300000)))
jesstemp30 ='n.  cg '
jesstemp31 ='r. asp'
jesstemp32 ='r. glu'
jesstemp33 ='jessatom0 x. %s'%(12.513900+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(12.524000+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(12.958300+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(20.038400+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(20.755500+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(20.917100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp30+')&('+jesstemp31+'))|(('+jesstemp30+')&('+jesstemp32+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.513900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(12.524000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(12.958300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(20.038400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(20.755500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(20.917100+(d*0.300000)))
jesstemp39 ='n.  od1'
jesstemp40 ='n.  od2'
jesstemp41 ='n.  oe1'
jesstemp42 ='n.  oe2'
jesstemp43 ='jessatom0 x. %s'%(12.897700+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(13.079500+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(13.321900+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(20.604000+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(21.270600+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(21.351400+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp50 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp39+')|('+jesstemp40+'))&('+jesstemp31+'))|((('+jesstemp41+')|('+jesstemp42+'))&('+jesstemp32+')))&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(12.897700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(13.079500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(13.321900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(20.604000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(21.270600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(21.351400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp51 ='n.  od2'
jesstemp52 ='n.  od1'
jesstemp53 ='n.  oe2'
jesstemp54 ='n.  oe1'
jesstemp55 ='jessatom0 x. %s'%(11.382700+(d*0.300000))
jesstemp56 ='jessatom1 x. %s'%(11.392800+(d*0.300000))
jesstemp57 ='jessatom2 x. %s'%(11.928100+(d*0.300000))
jesstemp58 ='jessatom3 x. %s'%(18.786000+(d*0.300000))
jesstemp59 ='jessatom4 x. %s'%(19.513200+(d*0.300000))
jesstemp60 ='jessatom5 x. %s'%(19.684900+(d*0.300000))
jesstemp61 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp62 ='br. jessatom6'
jesstemp63 ='jessatom7 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp51+')|('+jesstemp52+'))&('+jesstemp31+'))|((('+jesstemp53+')|('+jesstemp54+'))&('+jesstemp32+')))&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(11.382700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(11.392800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(11.928100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(18.786000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(19.513200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(19.684900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('Jfa_1upu', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
