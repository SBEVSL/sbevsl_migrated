'''
FUNC:Jab_1cy8-E9A-D111A-Y319A-H365A
PDB:1cy8
EC:5.99.1.2
PFAM:PF01131,PF01751
RESI:glu,asp,tyr,his
LOCI:a-9,111,319,365;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.565500+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.565500+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(8.150700+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(7.272000+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(8.150700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.272000+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(8.160800+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(7.120500+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.120500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp12 ='r. tyr'
jesstemp13 ='jessatom0 x. %s'%(14.362200+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(13.624900+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(8.221400+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(7.575000+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(14.362200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.624900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.221400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(7.575000+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(14.079400+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(13.281500+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(7.272000+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(6.756900+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp12+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(14.079400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.281500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.272000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(6.756900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp23 ='r. his'
jesstemp24 ='jessatom0 x. %s'%(20.412100+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(19.563700+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(12.372500+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(12.524000+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(8.938500+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(7.928500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(20.412100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(19.563700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(12.372500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(12.524000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.938500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.928500+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(20.321200+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(19.381900+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(12.251300+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(12.281600+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(8.968800+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(7.908300+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp3+')&('+jesstemp23+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(20.321200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(19.381900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(12.251300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(12.281600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.968800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1cy8-E9A-D111A-Y319A-H365A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
