'''
FUNC:Jfa_1cg4
PDB:1cg4
EC:6.3.4.4
PFAM:PF00709
RESI:asp,his,gln
LOCI:a-13,41,224;
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
jesstemp13 ='jessatom0 x. %s'%(1.242300+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp16 ='r. his'
jesstemp17 ='jessatom0 x. %s'%(8.716300+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(7.686100+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(9.736400+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.716300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.686100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.736400+(d*0.300000)))
jesstemp20 ='n.  nd1'
jesstemp21 ='jessatom0 x. %s'%(8.383000+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(7.403300+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(9.494000+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(1.383700+(d*0.300000))
jesstemp25 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp20+')&('+jesstemp16+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.383000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.494000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.383700+(d*0.300000)))
jesstemp26 ='n.  ne2'
jesstemp27 ='jessatom0 x. %s'%(8.867800+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(7.726500+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(9.867700+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(2.201800+(d*0.300000))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp26+')&('+jesstemp16+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.867800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.726500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.867700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.161400+(d*0.300000)))
jesstemp33 ='n.  cd '
jesstemp34 ='r. gln'
jesstemp35 ='r. asn'
jesstemp36 ='jessatom0 x. %s'%(8.847600+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(7.867900+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(9.312200+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(9.130400+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(8.736500+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(7.261900+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp33+')&('+jesstemp34+'))|(('+jesstemp33+')&('+jesstemp35+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.847600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.867900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.312200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.736500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.261900+(d*0.300000)))
jesstemp42 ='jessatom0 x. %s'%(10.019200+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(9.019300+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(10.524200+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(9.564700+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(9.160700+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(7.544700+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp49 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp5+')&('+jesstemp34+'))|(('+jesstemp5+')&('+jesstemp35+')))&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.019200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.019300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.524200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.564700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.160700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.544700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp50 ='jessatom0 x. %s'%(8.231500+(d*0.300000))
jesstemp51 ='jessatom1 x. %s'%(7.160900+(d*0.300000))
jesstemp52 ='jessatom2 x. %s'%(8.686000+(d*0.300000))
jesstemp53 ='jessatom3 x. %s'%(8.251700+(d*0.300000))
jesstemp54 ='jessatom4 x. %s'%(8.019400+(d*0.300000))
jesstemp55 ='jessatom5 x. %s'%(6.484200+(d*0.300000))
jesstemp56 ='jessatom6 x. %s'%(1.353400+(d*0.300000))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp26+')&('+jesstemp34+'))|(('+jesstemp26+')&('+jesstemp35+')))&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.231500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.160900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.686000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.251700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.019400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.484200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.272500+(d*0.300000)))
cmd.select('Jfa_1cg4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
