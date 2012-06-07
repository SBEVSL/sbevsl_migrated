'''
FUNC:Jab_3nse_1_14_13_39
PDB:3nse
EC:1.14.13.39
RESI:cys,arg,trp,glu
LOCI:a-186,189,358,363;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. cys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. cys'
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. arg'
jesstemp7 ='jessatom0 x. %s'%(6.201400+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(5.494400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(5.494400+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(5.787300+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(5.140900+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.787300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.140900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(11.938200+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(11.453400+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(11.887700+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(13.119900+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.938200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.453400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(11.887700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(13.119900+(d*0.300000)))
jesstemp17 ='n.  c  '
jesstemp18 ='jessatom0 x. %s'%(11.130200+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(10.827200+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(11.625100+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(12.796700+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.130200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.827200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.625100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(12.796700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp24 ='r. glu'
jesstemp25 ='r. asp'
jesstemp26 ='jessatom0 x. %s'%(12.190700+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(12.928000+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(16.099400+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(16.634700+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(10.554500+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(9.100100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp24+'))|(('+jesstemp0+')&('+jesstemp25+')))&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.190700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(12.928000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(16.099400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(16.634700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.554500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.100100+(d*0.300000)))
jesstemp32 ='jessatom0 x. %s'%(11.241300+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(11.837200+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(15.008600+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(15.594400+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(9.211200+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(7.777000+(d*0.300000))
jesstemp38 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp39 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp24+'))|(('+jesstemp2+')&('+jesstemp25+')))&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(11.241300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.837200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(15.008600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(15.594400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.211200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.777000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_3nse_1_14_13_39', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
