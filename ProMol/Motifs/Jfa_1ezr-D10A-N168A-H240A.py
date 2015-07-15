'''
FUNC:Jfa_1ezr-D10A-N168A-H240A
PDB:1ezr
EC:3.2.2.1
PFAM:PF01156
RESI:asp,asn,his
LOCI:a-10,168,240;
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
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp15 ='r. asn'
jesstemp16 ='r. gln'
jesstemp17 ='jessatom0 x. %s'%(9.140500+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(8.857700+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(9.938400+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp15+'))|(('+jesstemp0+')&('+jesstemp16+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.140500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.857700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.938400+(d*0.300000)))
jesstemp20 ='jessatom0 x. %s'%(8.827400+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(8.433500+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(9.736400+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.232200+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp3+')&('+jesstemp15+'))|(('+jesstemp3+')&('+jesstemp16+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.827400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.433500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.736400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.232200+(d*0.300000)))
jesstemp25 ='n.  nd2'
jesstemp26 ='jessatom0 x. %s'%(8.453700+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(8.332500+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(9.150600+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(1.343300+(d*0.300000))
jesstemp30 ='br. jessatom3'
jesstemp31 ='jessatom4 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp25+')&('+jesstemp15+'))|(('+jesstemp25+')&('+jesstemp16+')))&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.453700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.150600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.262400+(d*0.300000)))
jesstemp32 ='r. his'
jesstemp33 ='jessatom0 x. %s'%(4.474300+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(4.484400+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(4.110700+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(8.534500+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(8.665800+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(7.777000+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(4.474300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.484400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.110700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.534500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.665800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.777000+(d*0.300000)))
jesstemp39 ='n.  nd1'
jesstemp40 ='jessatom0 x. %s'%(3.676400+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(3.434000+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(3.434000+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(8.837500+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(8.766800+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(8.201200+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp39+')&('+jesstemp32+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(3.676400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(3.434000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.434000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.837500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.766800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp48 ='n.  ne2'
jesstemp49 ='jessatom0 x. %s'%(5.807500+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(5.454000+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(5.443900+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(9.726300+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(9.766700+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(9.191000+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(2.222000+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp48+')&('+jesstemp32+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.454000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.443900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.726300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.766700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.191000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_1ezr-D10A-N168A-H240A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
