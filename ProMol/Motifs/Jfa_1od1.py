'''
FUNC:Jfa_1od1
PDB:1od1
EC:3.4.23.22
PFAM:PF00026
RESI:asp,thr,asp,thr
LOCI:a-35,36,219,222;
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
jesstemp13 ='jessatom0 x. %s'%(1.272600+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.252300+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.252300+(d*0.300000)))
jesstemp16 ='n.  ca '
jesstemp17 ='r. ser'
jesstemp18 ='r. thr'
jesstemp19 ='jessatom0 x. %s'%(4.585400+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(4.989400+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(4.090500+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp16+')&('+jesstemp17+'))|(('+jesstemp16+')&('+jesstemp18+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.585400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.090500+(d*0.300000)))
jesstemp22 ='n.  cb '
jesstemp23 ='jessatom0 x. %s'%(4.181400+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(4.848000+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(3.302700+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(1.555400+(d*0.300000))
jesstemp27 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp22+')&('+jesstemp17+'))|(('+jesstemp22+')&('+jesstemp18+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.181400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.848000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.302700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.555400+(d*0.300000)))
jesstemp28 ='n.  og '
jesstemp29 ='jessatom0 x. %s'%(3.413800+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(4.373300+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(2.575500+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(2.494700+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(1.444300+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp28+')&('+jesstemp17+'))|(('+jesstemp28+')&('+jesstemp18+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.413800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.373300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.575500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.494700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.444300+(d*0.300000)))
jesstemp35 ='jessatom0 x. %s'%(5.302500+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(4.070300+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(5.918600+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(7.393200+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(7.665900+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(7.807300+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.302500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.070300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.393200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.807300+(d*0.300000)))
jesstemp41 ='jessatom0 x. %s'%(4.292500+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(3.040100+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(5.090400+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(6.847800+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(7.090200+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(7.049800+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.292500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(3.040100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.090400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.847800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.049800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp49 ='jessatom0 x. %s'%(5.565100+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(4.454100+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(5.928700+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(7.383100+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(7.514400+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(7.797200+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.565100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.454100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.928700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.383100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.514400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.797200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.242200+(d*0.300000)))
cmd.select('Jfa_1od1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
