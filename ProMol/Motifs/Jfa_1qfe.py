'''
FUNC:Jfa_1qfe
PDB:1qfe
EC:4.2.1.10
PFAM:PF01487
RESI:glu,his,lys
LOCI:a-86,143,170;
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
jesstemp15 ='n.  cg '
jesstemp16 ='r. his'
jesstemp17 ='jessatom0 x. %s'%(4.827800+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(3.787500+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(5.868100+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.827800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.787500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.868100+(d*0.300000)))
jesstemp20 ='n.  nd1'
jesstemp21 ='jessatom0 x. %s'%(4.019800+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(2.828000+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(5.019700+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp25 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp20+')&('+jesstemp16+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.019800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(2.828000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp26 ='n.  ne2'
jesstemp27 ='jessatom0 x. %s'%(6.130700+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(4.928800+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(7.130600+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(2.211900+(d*0.300000))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp26+')&('+jesstemp16+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.130700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.130600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.161400+(d*0.300000)))
jesstemp33 ='r. lys'
jesstemp34 ='jessatom0 x. %s'%(9.726300+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(8.463800+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(10.433300+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(6.231700+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(6.060000+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(4.332900+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.726300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.463800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.433300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.231700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.332900+(d*0.300000)))
jesstemp40 ='n.  ce '
jesstemp41 ='jessatom0 x. %s'%(9.645500+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(8.393100+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(10.493900+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(5.615600+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(5.726700+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(3.716800+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.525100+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp40+')&('+jesstemp33+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.393100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.493900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.615600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.716800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.525100+(d*0.300000)))
jesstemp49 ='n.  nz '
jesstemp50 ='jessatom0 x. %s'%(8.908200+(d*0.300000))
jesstemp51 ='jessatom1 x. %s'%(7.676000+(d*0.300000))
jesstemp52 ='jessatom2 x. %s'%(9.837400+(d*0.300000))
jesstemp53 ='jessatom3 x. %s'%(5.039900+(d*0.300000))
jesstemp54 ='jessatom4 x. %s'%(5.039900+(d*0.300000))
jesstemp55 ='jessatom5 x. %s'%(2.929000+(d*0.300000))
jesstemp56 ='jessatom6 x. %s'%(2.474500+(d*0.300000))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(1.474600+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp49+')&('+jesstemp33+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.908200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.676000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.837400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.039900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.039900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(2.929000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.474600+(d*0.300000)))
cmd.select('Jfa_1qfe', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
