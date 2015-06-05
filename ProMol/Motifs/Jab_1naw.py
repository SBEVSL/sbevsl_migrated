'''
FUNC:Jab_1naw
PDB:1naw
EC:2.5.1.7
PFAM:PF00275
RESI:asn,cys,asp,arg
LOCI:a-23,115,305,397;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='r. cys'
jesstemp7 ='jessatom0 x. %s'%(27.835600+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(27.290200+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(27.835600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(27.290200+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(28.805200+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(28.239600+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(28.805200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(28.239600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp13 ='r. asp'
jesstemp14 ='r. glu'
jesstemp15 ='jessatom0 x. %s'%(12.200800+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(10.776700+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(27.956800+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(28.461800+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp13+'))|(('+jesstemp0+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.200800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(10.776700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(27.956800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(28.461800+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(10.675700+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(9.261700+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(27.926500+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(28.502200+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp3+')&('+jesstemp13+'))|(('+jesstemp3+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.675700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.261700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(27.926500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(28.502200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp25 ='r. arg'
jesstemp26 ='jessatom0 x. %s'%(11.887700+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(11.998800+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(27.068000+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(27.532600+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(14.786400+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(13.948100+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.887700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.998800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(27.068000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(27.532600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(14.786400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(13.948100+(d*0.300000)))
jesstemp32 ='jessatom0 x. %s'%(12.099800+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(12.130100+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(25.573200+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(26.017600+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(14.695500+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(13.907700+(d*0.300000))
jesstemp38 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp39 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp3+')&('+jesstemp25+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(12.099800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(12.130100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(25.573200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(26.017600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(14.695500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(13.907700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1naw', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
