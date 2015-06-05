'''
FUNC:Jab_1pgn
PDB:1pgn
EC:1.1.1.44
PFAM:PF00393,PF03446
RESI:gly,lys,asn,glu
LOCI:a-130,183,187,190;
'''
jesstemp0 ='n.  n  '
cmd.select('jessatom0', '(('+jesstemp0+'))')
jesstemp1 ='n.  ca '
jesstemp2 ='jessatom0 x. %s'%(1.464500+(d*0.300000))
jesstemp3 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp1+')&('+jesstemp2+')&('+jesstemp3+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.464500+(d*0.300000)))
jesstemp4 ='r. lys'
jesstemp5 ='jessatom0 x. %s'%(12.180600+(d*0.300000))
jesstemp6 ='jessatom1 x. %s'%(13.231000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp1+')&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.180600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(13.231000+(d*0.300000)))
jesstemp7 ='n.  cb '
jesstemp8 ='jessatom0 x. %s'%(11.766500+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(12.746200+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp7+')&('+jesstemp4+')&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.766500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.746200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp12 ='r. asn'
jesstemp13 ='r. gln'
jesstemp14 ='jessatom0 x. %s'%(11.534200+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(12.281600+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(6.575100+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(7.433600+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp1+')&('+jesstemp12+'))|(('+jesstemp1+')&('+jesstemp13+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.534200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.281600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(7.433600+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(11.392800+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(12.019000+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(6.433700+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(7.039700+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.525100+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp7+')&('+jesstemp12+'))|(('+jesstemp7+')&('+jesstemp13+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.392800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(12.019000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.433700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.525100+(d*0.300000)))
jesstemp24 ='r. glu'
jesstemp25 ='r. asp'
jesstemp26 ='jessatom0 x. %s'%(12.513900+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(13.210800+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(10.584800+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(11.615000+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(4.686400+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(5.928700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp1+')&('+jesstemp24+'))|(('+jesstemp1+')&('+jesstemp25+')))&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.513900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(13.210800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.584800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.615000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.686400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.928700+(d*0.300000)))
jesstemp32 ='jessatom0 x. %s'%(11.160500+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(11.837200+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(9.716200+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(10.605000+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(3.807700+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(4.918700+(d*0.300000))
jesstemp38 ='jessatom6 x. %s'%(1.515000+(d*0.300000))
jesstemp39 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp7+')&('+jesstemp24+'))|(('+jesstemp7+')&('+jesstemp25+')))&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(11.160500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.837200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.716200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.605000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.807700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.918700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.515000+(d*0.300000)))
cmd.select('Jab_1pgn', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
