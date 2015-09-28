'''
FUNC:Jfa_3lip_3_1_1_3
PDB:3lip
EC:3.1.1.3
RESI:ser,asp,his
LOCI:a-87,264,286;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.494700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.434200+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.494700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.434200+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. asp'
jesstemp12 ='r. glu'
jesstemp13 ='jessatom0 x. %s'%(8.332500+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(8.393100+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(7.908300+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.393100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.908300+(d*0.300000)))
jesstemp16 ='n.  od1'
jesstemp17 ='n.  od2'
jesstemp18 ='n.  oe1'
jesstemp19 ='n.  oe2'
jesstemp20 ='jessatom0 x. %s'%(8.403200+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(8.372900+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(7.686100+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.403200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.372900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.686100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp25 ='n.  od2'
jesstemp26 ='n.  od1'
jesstemp27 ='n.  oe2'
jesstemp28 ='n.  oe1'
jesstemp29 ='jessatom0 x. %s'%(7.302300+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(7.484100+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(7.160900+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.302300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.484100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.160900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.171500+(d*0.300000)))
jesstemp35 ='r. his'
jesstemp36 ='jessatom0 x. %s'%(6.211500+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(5.575200+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(5.019700+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(4.110700+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(4.060200+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(3.858200+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.211500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.575200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.110700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.060200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.858200+(d*0.300000)))
jesstemp42 ='n.  nd1'
jesstemp43 ='jessatom0 x. %s'%(5.413600+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(5.100500+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(4.656100+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(3.524900+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(3.605700+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(2.929000+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(1.403900+(d*0.300000))
jesstemp50 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp42+')&('+jesstemp35+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.100500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.656100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.524900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.605700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(2.929000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.403900+(d*0.300000)))
jesstemp51 ='n.  ne2'
jesstemp52 ='jessatom0 x. %s'%(4.282400+(d*0.300000))
jesstemp53 ='jessatom1 x. %s'%(3.474400+(d*0.300000))
jesstemp54 ='jessatom2 x. %s'%(2.807800+(d*0.300000))
jesstemp55 ='jessatom3 x. %s'%(5.595400+(d*0.300000))
jesstemp56 ='jessatom4 x. %s'%(5.433800+(d*0.300000))
jesstemp57 ='jessatom5 x. %s'%(5.019700+(d*0.300000))
jesstemp58 ='jessatom6 x. %s'%(2.211900+(d*0.300000))
jesstemp59 ='br. jessatom6'
jesstemp60 ='jessatom7 x. %s'%(2.151300+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp51+')&('+jesstemp35+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.282400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.474400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(2.807800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.595400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.433800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.151300+(d*0.300000)))
cmd.select('Jfa_3lip_3_1_1_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
