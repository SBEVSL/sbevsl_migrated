'''
FUNC:Jfa_1bgg_3_2_1_21
PDB:1bgg
EC:3.2.1.21
RESI:glu,asn,glu
LOCI:a-166,294,352;
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
jesstemp13 ='jessatom0 x. %s'%(1.252400+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp16 ='n.  cg '
jesstemp17 ='r. asn'
jesstemp18 ='r. gln'
jesstemp19 ='jessatom0 x. %s'%(4.464200+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(5.686300+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(3.696600+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp16+')&('+jesstemp17+'))|(('+jesstemp16+')&('+jesstemp18+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.464200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.696600+(d*0.300000)))
jesstemp22 ='jessatom0 x. %s'%(5.625700+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(6.847800+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(4.908600+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.232200+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp5+')&('+jesstemp17+'))|(('+jesstemp5+')&('+jesstemp18+')))&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.847800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.908600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.232200+(d*0.300000)))
jesstemp27 ='n.  nd2'
jesstemp28 ='jessatom0 x. %s'%(3.484500+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(4.676300+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(2.918900+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(1.333200+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.252300+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp27+')&('+jesstemp17+'))|(('+jesstemp27+')&('+jesstemp18+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.484500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.676300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.918900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.252300+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(5.110600+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(5.868100+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(4.343000+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(3.615800+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(3.949100+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(3.120900+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.110600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.868100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.343000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(3.615800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.949100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.120900+(d*0.300000)))
jesstemp40 ='jessatom0 x. %s'%(4.565200+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(5.231800+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(3.636000+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(3.747100+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(4.373300+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(3.272400+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.565200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.636000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.747100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.373300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.272400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp48 ='jessatom0 x. %s'%(4.938900+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(5.625700+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(4.454100+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(3.969300+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(4.272300+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(3.141100+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.454100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(3.969300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.272300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.141100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('Jfa_1bgg_3_2_1_21', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
