'''
FUNC:Jfa_4hoh-H50A-E58A-H92A
PDB:4hoh
EC:3.1.27.3
PFAM:PF00545
RESI:his,glu,his
LOCI:a-50,58,92;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.393800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.393800+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.211900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. glu'
jesstemp12 ='r. asp'
jesstemp13 ='jessatom0 x. %s'%(5.029800+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(4.423800+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(3.656200+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.423800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.656200+(d*0.300000)))
jesstemp16 ='n.  oe1'
jesstemp17 ='n.  oe2'
jesstemp18 ='n.  od1'
jesstemp19 ='n.  od2'
jesstemp20 ='jessatom0 x. %s'%(5.797400+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(5.393400+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(4.191500+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.797400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.393400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.191500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp25 ='n.  oe2'
jesstemp26 ='n.  oe1'
jesstemp27 ='n.  od2'
jesstemp28 ='n.  od1'
jesstemp29 ='jessatom1 x. %s'%(4.141000+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(3.605700+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.141000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.605700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(12.483600+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(11.938200+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(10.362600+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(8.302200+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(7.383100+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(8.282000+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.483600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.938200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.362600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.383100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.282000+(d*0.300000)))
jesstemp40 ='jessatom0 x. %s'%(12.200800+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(11.514000+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(10.079800+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(8.069900+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(7.312400+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(7.857800+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(12.200800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.514000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.079800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.069900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.312400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp48 ='jessatom0 x. %s'%(10.352500+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(9.817200+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(8.201200+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(6.464000+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(5.595400+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(6.383200+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(2.211900+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(10.352500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.817200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.464000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.595400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.383200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_4hoh-H50A-E58A-H92A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
