'''
FUNC:Jab_1h17
PDB:1h17
EC:2.3.1.54
PFAM:PF01228,PF02901
RESI:trp,cys,cys,gly
LOCI:a-333,418,419,734;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. trp'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. trp'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. cys'
jesstemp7 ='jessatom0 x. %s'%(5.140900+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(3.878400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.140900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(3.878400+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(6.130700+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(4.686400+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.130700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.686400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(7.272000+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(6.383200+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(3.848100+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(4.191500+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.272000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.383200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.848100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(4.191500+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(7.979000+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(7.029600+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(4.797500+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(4.726800+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.979000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.726800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp23 ='r. gly'
jesstemp24 ='jessatom0 x. %s'%(9.261700+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(8.776900+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(7.847700+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(8.019400+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(4.575300+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(3.646100+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.261700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.776900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.847700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.019400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.575300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.646100+(d*0.300000)))
jesstemp30 ='n.  c  '
jesstemp31 ='jessatom0 x. %s'%(7.888100+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(7.554800+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(7.090200+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(7.484100+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(4.252100+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(3.696600+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp30+')&('+jesstemp23+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.888100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.554800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.484100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.252100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.696600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1h17', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
