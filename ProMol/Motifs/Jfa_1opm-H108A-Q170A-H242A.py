'''
FUNC:Jfa_1opm-H108A-Q170A-H242A
PDB:1opm
EC:1.14.17.3
PFAM:PF01082,PF03712
RESI:his,gln,his
LOCI:a-108,170,242;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.383700+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.383700+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.211900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. gln'
jesstemp12 ='r. asn'
jesstemp13 ='jessatom0 x. %s'%(6.575100+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(6.211500+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(4.454100+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.211500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.454100+(d*0.300000)))
jesstemp16 ='n.  oe1'
jesstemp17 ='jessatom0 x. %s'%(5.686300+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(5.302500+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(3.494600+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp16+')&('+jesstemp11+'))|(('+jesstemp16+')&('+jesstemp12+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.302500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.494600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp22 ='jessatom0 x. %s'%(7.857800+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(7.433600+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(5.716600+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.343300+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp6+')&('+jesstemp11+'))|(('+jesstemp6+')&('+jesstemp12+')))&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.433600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.716600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.272500+(d*0.300000)))
jesstemp28 ='jessatom0 x. %s'%(9.645500+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(9.372800+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(8.756700+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(9.877800+(d*0.300000))
jesstemp32 ='jessatom4 x. %s'%(8.797100+(d*0.300000))
jesstemp33 ='jessatom5 x. %s'%(10.089900+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.372800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.756700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.877800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.797100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(10.089900+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(8.544600+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(8.170900+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(7.756800+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(9.180900+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(8.039600+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(9.504100+(d*0.300000))
jesstemp40 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.170900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.756800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.180900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.039600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.504100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp42 ='jessatom0 x. %s'%(9.867700+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(9.312200+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(8.716300+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(9.130400+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(8.140600+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(9.150600+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(2.252300+(d*0.300000))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.867700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.312200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.716300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.140600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.150600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.252300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('Jfa_1opm-H108A-Q170A-H242A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
