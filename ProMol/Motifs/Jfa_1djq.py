'''
FUNC:Jfa_1djq
PDB:1djq
EC:1.5.99.7
PFAM:PF07992,PF00724,PF13450
RESI:tyr,his,asp
LOCI:a-169,172,267;
'''
jesstemp0 ='n.  ce1'
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cz '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.403900+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.403900+(d*0.300000)))
jesstemp6 ='n.  oh '
jesstemp7 ='jessatom0 x. %s'%(2.393700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.393700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.393800+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. his'
jesstemp12 ='jessatom0 x. %s'%(5.656000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(4.504600+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(3.535000+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.656000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.504600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.535000+(d*0.300000)))
jesstemp15 ='n.  nd1'
jesstemp16 ='jessatom0 x. %s'%(4.908600+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(3.615800+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(2.686600+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.908600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.615800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.686600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp21 ='n.  ne2'
jesstemp22 ='jessatom0 x. %s'%(7.019500+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(5.726700+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(4.696500+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.211900+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.019500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.696500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.161400+(d*0.300000)))
jesstemp28 ='r. asp'
jesstemp29 ='r. glu'
jesstemp30 ='jessatom0 x. %s'%(10.352500+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(9.009200+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(8.110300+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(5.878200+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(5.716600+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(3.726900+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp10+')&('+jesstemp28+'))|(('+jesstemp10+')&('+jesstemp29+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.352500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.009200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.110300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.716600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.726900+(d*0.300000)))
jesstemp36 ='n.  od1'
jesstemp37 ='n.  od2'
jesstemp38 ='n.  oe1'
jesstemp39 ='n.  oe2'
jesstemp40 ='jessatom0 x. %s'%(10.998900+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(9.645500+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(8.857700+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(6.878100+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(6.554900+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(4.747000+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp36+')|('+jesstemp37+'))&('+jesstemp28+'))|((('+jesstemp38+')|('+jesstemp39+'))&('+jesstemp29+')))&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.998900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.857700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.878100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.554900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp48 ='n.  od2'
jesstemp49 ='n.  od1'
jesstemp50 ='n.  oe2'
jesstemp51 ='n.  oe1'
jesstemp52 ='jessatom0 x. %s'%(9.302100+(d*0.300000))
jesstemp53 ='jessatom1 x. %s'%(7.989100+(d*0.300000))
jesstemp54 ='jessatom2 x. %s'%(7.029600+(d*0.300000))
jesstemp55 ='jessatom3 x. %s'%(5.039900+(d*0.300000))
jesstemp56 ='jessatom4 x. %s'%(4.767200+(d*0.300000))
jesstemp57 ='jessatom5 x. %s'%(2.828000+(d*0.300000))
jesstemp58 ='br. jessatom6'
jesstemp59 ='jessatom7 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp48+')|('+jesstemp49+'))&('+jesstemp28+'))|((('+jesstemp50+')|('+jesstemp51+'))&('+jesstemp29+')))&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp46+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.302100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.989100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.039900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.767200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(2.828000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('Jfa_1djq', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
