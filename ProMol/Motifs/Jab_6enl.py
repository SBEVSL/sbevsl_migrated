'''
FUNC:Jab_6enl
PDB:6enl
EC:4.2.1.11
PFAM:PF03952,PF00113
RESI:glu,glu,his,lys
LOCI:a-168,211,373,396;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(10.009100+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(9.372800+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(10.009100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(9.372800+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(8.645600+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(7.908300+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.575600+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.645600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.575600+(d*0.300000)))
jesstemp12 ='r. his'
jesstemp13 ='jessatom0 x. %s'%(13.614800+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(12.140200+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(9.352600+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(8.716300+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(13.614800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.140200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.352600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(8.716300+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(13.008800+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(11.594800+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(8.049700+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(7.494200+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp12+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(13.008800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.594800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.049700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(7.494200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp23 ='r. lys'
jesstemp24 ='jessatom0 x. %s'%(11.170600+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(9.786900+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(10.493900+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(9.393000+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(6.464000+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(6.090300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.170600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.786900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.493900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.393000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.464000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.090300+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(10.180800+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(8.746600+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(10.605000+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(9.352600+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(6.686200+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(6.494300+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.515000+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp3+')&('+jesstemp23+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.180800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.746600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.605000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.352600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.686200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.494300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.515000+(d*0.300000)))
cmd.select('Jab_6enl', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
