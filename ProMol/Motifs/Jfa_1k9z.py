'''
FUNC:Jfa_1k9z
PDB:1k9z
EC:3.1.3.7
PFAM:PF00459
RESI:asp,thr,asp
LOCI:a-49,147,294;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.252400+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.171500+(d*0.300000)))
jesstemp16 ='n.  ca '
jesstemp17 ='r. thr'
jesstemp18 ='r. ser'
jesstemp19 ='jessatom0 x. %s'%(5.555000+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(5.373200+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(4.747000+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp16+')&('+jesstemp17+'))|(('+jesstemp16+')&('+jesstemp18+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.555000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.373200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.747000+(d*0.300000)))
jesstemp22 ='n.  cb '
jesstemp23 ='jessatom0 x. %s'%(4.666200+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(4.565200+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(3.848100+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp27 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp22+')&('+jesstemp17+'))|(('+jesstemp22+')&('+jesstemp18+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.666200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.565200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.848100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp28 ='n.  og1'
jesstemp29 ='jessatom0 x. %s'%(3.797600+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(4.060200+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(2.737100+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(2.434100+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(1.464500+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp28+')&('+jesstemp17+'))|(('+jesstemp28+')&('+jesstemp18+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.797600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.060200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.737100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.434100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.464500+(d*0.300000)))
jesstemp35 ='jessatom0 x. %s'%(11.918000+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(12.847200+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(10.726200+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(10.372700+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(10.190900+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(9.423300+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.918000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(12.847200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.726200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.372700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.190900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.423300+(d*0.300000)))
jesstemp41 ='jessatom0 x. %s'%(10.776700+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(11.716000+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(9.584900+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(9.423300+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(9.241500+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(8.393100+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.776700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.716000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.584900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.423300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.393100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp49 ='jessatom0 x. %s'%(12.130100+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(13.018900+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(10.938300+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(10.504000+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(10.211100+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(9.534400+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(12.130100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(13.018900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(10.938300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(10.504000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(10.211100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.534400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.171500+(d*0.300000)))
cmd.select('Jfa_1k9z', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
