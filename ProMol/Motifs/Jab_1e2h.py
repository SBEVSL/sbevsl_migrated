'''
FUNC:Jab_1e2h
PDB:1e2h
EC:2.7.1.27
PFAM:PF00693
RESI:gly,glu,arg,arg
LOCI:a-59,83,163,222;
'''
jesstemp0 ='n.  n  '
cmd.select('jessatom0', '(('+jesstemp0+'))')
jesstemp1 ='n.  ca '
jesstemp2 ='jessatom0 x. %s'%(1.454400+(d*0.300000))
jesstemp3 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp1+')&('+jesstemp2+')&('+jesstemp3+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.454400+(d*0.300000)))
jesstemp4 ='r. glu'
jesstemp5 ='r. asp'
jesstemp6 ='jessatom0 x. %s'%(12.079600+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(13.180500+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp1+')&('+jesstemp4+'))|(('+jesstemp1+')&('+jesstemp5+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.079600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(13.180500+(d*0.300000)))
jesstemp8 ='n.  cb '
jesstemp9 ='jessatom0 x. %s'%(10.776700+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(11.827100+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp8+')&('+jesstemp4+'))|(('+jesstemp8+')&('+jesstemp5+')))&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.776700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(11.827100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='r. arg'
jesstemp14 ='jessatom0 x. %s'%(11.786700+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(13.109800+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(7.615400+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(8.029500+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp1+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.786700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.109800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.615400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(8.029500+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(11.170600+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(12.544200+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(7.070000+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(7.383100+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp8+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.170600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(12.544200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.070000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(7.383100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(9.271800+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(9.514200+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(11.443300+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(10.059600+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(15.877200+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(14.776300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp1+')&('+jesstemp13+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.514200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(11.443300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.059600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(15.877200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(14.776300+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(8.675900+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(9.140500+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(10.180800+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(8.817300+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(14.453100+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(13.301700+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.555400+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp8+')&('+jesstemp13+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.140500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.180800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.817300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(14.453100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(13.301700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1e2h', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
