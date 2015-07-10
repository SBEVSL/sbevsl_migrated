'''
FUNC:Jab_1s2i-Y11A-D75A-D95A-E101A
PDB:1s2i
EC:2.4.2.6
PFAM:PF05014
RESI:tyr,asp,asp,glu
LOCI:a-11,75,95,101;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='r. asp'
jesstemp7 ='r. glu'
jesstemp8 ='jessatom0 x. %s'%(8.706200+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(7.958800+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.958800+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(9.130400+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(8.352700+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.352700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(16.038800+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(15.584300+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(15.352000+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(13.958200+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(16.038800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(15.584300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(15.352000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(13.958200+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(14.816700+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(14.453100+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(14.432900+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(13.079500+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(14.816700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(14.453100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(14.432900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(13.079500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(9.847500+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(8.574900+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(8.867800+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(8.009300+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(10.362600+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(9.968700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp7+'))|(('+jesstemp0+')&('+jesstemp6+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.847500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.574900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.867800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.009300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.362600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.968700+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(8.726400+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(7.554800+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(7.938600+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(7.049800+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(9.968700+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(9.362700+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp7+'))|(('+jesstemp2+')&('+jesstemp6+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.726400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.554800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.049800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.968700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.362700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1s2i-Y11A-D75A-D95A-E101A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
