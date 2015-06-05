'''
FUNC:Jab_1afr
PDB:1afr
EC:1.14.19.2
PFAM:PF03405
RESI:trp,his,thr,asp
LOCI:a-62,146,199,228;
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
jesstemp6 ='r. his'
jesstemp7 ='jessatom0 x. %s'%(10.554500+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(10.049500+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(10.554500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.049500+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(11.322100+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(10.776700+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.322100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.776700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp13 ='r. thr'
jesstemp14 ='r. ser'
jesstemp15 ='jessatom0 x. %s'%(18.523400+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(17.523500+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(11.261500+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(9.887900+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp13+'))|(('+jesstemp0+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(18.523400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(17.523500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(11.261500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(9.887900+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(17.624500+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(16.725600+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(10.120200+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(8.675900+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp13+'))|(('+jesstemp2+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(17.624500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(16.725600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(10.120200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp25 ='r. asp'
jesstemp26 ='r. glu'
jesstemp27 ='jessatom0 x. %s'%(10.150500+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(9.433400+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(9.231400+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(8.443600+(d*0.300000))
jesstemp31 ='jessatom4 x. %s'%(10.039400+(d*0.300000))
jesstemp32 ='jessatom5 x. %s'%(9.251600+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp25+'))|(('+jesstemp0+')&('+jesstemp26+')))&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.150500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.433400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.231400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.443600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.039400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.251600+(d*0.300000)))
jesstemp33 ='jessatom0 x. %s'%(9.362700+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(8.706200+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(7.807300+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(7.090200+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(10.130300+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(9.180900+(d*0.300000))
jesstemp39 ='jessatom6 x. %s'%(1.555400+(d*0.300000))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp25+'))|(('+jesstemp2+')&('+jesstemp26+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.362700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.807300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(10.130300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.180900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1afr', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
