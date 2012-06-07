'''
FUNC:Jfa_5yas_4_1_2_39
PDB:5yas
EC:4.1.2.39
RESI:thr,ser,asp,his
LOCI:a-11,80,207,235;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.474500+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.424100+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. asp'
jesstemp12 ='r. glu'
jesstemp13 ='jessatom0 x. %s'%(8.251700+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(8.019400+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(7.726500+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.251700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.019400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.726500+(d*0.300000)))
jesstemp16 ='n.  od1'
jesstemp17 ='n.  od2'
jesstemp18 ='n.  oe1'
jesstemp19 ='n.  oe2'
jesstemp20 ='jessatom1 x. %s'%(7.827500+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(7.352800+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.251700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.827500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.352800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp24 ='n.  od2'
jesstemp25 ='n.  od1'
jesstemp26 ='n.  oe2'
jesstemp27 ='n.  oe1'
jesstemp28 ='jessatom0 x. %s'%(7.302300+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(7.211400+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(7.080100+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(1.232200+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp11+'))|((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp12+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.302300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.211400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.080100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.232200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.181600+(d*0.300000)))
jesstemp34 ='r. his'
jesstemp35 ='jessatom0 x. %s'%(6.322600+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(5.474200+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(5.302500+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(3.908700+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(3.464300+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(3.747100+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.322600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.474200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.302500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(3.908700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.464300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.747100+(d*0.300000)))
jesstemp41 ='n.  nd1'
jesstemp42 ='jessatom0 x. %s'%(5.585300+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(4.989400+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(4.797500+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(3.312800+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(3.060300+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(2.868400+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(1.333200+(d*0.300000))
jesstemp49 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp41+')&('+jesstemp34+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.312800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.060300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(2.868400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.333200+(d*0.300000)))
jesstemp50 ='n.  ne2'
jesstemp51 ='jessatom0 x. %s'%(4.524800+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(3.464300+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(3.191600+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(5.383300+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(4.928800+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(4.949000+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(2.151300+(d*0.300000))
jesstemp58 ='br. jessatom6'
jesstemp59 ='jessatom7 x. %s'%(2.121000+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp50+')&('+jesstemp34+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.524800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.464300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(3.191600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.383300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.151300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.121000+(d*0.300000)))
cmd.select('Jfa_5yas_4_1_2_39', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
