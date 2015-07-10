'''
FUNC:Jfa_1ga8-D130A-N153A-Q189A
PDB:1ga8
EC:2.4.1.44
PFAM:PF01501
RESI:asp,asn,gln
LOCI:a-130,153,189;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.272600+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.272600+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.242300+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp16 ='r. asn'
jesstemp17 ='r. gln'
jesstemp18 ='jessatom0 x. %s'%(4.747000+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(5.746900+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(3.797600+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp16+'))|(('+jesstemp0+')&('+jesstemp17+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.746900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.797600+(d*0.300000)))
jesstemp21 ='jessatom0 x. %s'%(5.979200+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(6.938700+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(5.019700+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(1.242300+(d*0.300000))
jesstemp25 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp3+')&('+jesstemp16+'))|(('+jesstemp3+')&('+jesstemp17+')))&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.938700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.242300+(d*0.300000)))
jesstemp26 ='n.  nd2'
jesstemp27 ='jessatom0 x. %s'%(4.191500+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(5.050000+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(3.070400+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(1.343300+(d*0.300000))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp26+')&('+jesstemp16+'))|(('+jesstemp26+')&('+jesstemp17+')))&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.191500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.050000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.070400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.262400+(d*0.300000)))
jesstemp33 ='n.  cd '
jesstemp34 ='jessatom0 x. %s'%(5.272200+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(6.221600+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(4.282400+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(4.706600+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(5.443900+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(4.171300+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp33+')&('+jesstemp17+'))|(('+jesstemp33+')&('+jesstemp16+')))&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.272200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.221600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.282400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.706600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.443900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.171300+(d*0.300000)))
jesstemp40 ='jessatom0 x. %s'%(5.120700+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(6.130700+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(3.999600+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(3.585500+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(4.231900+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(3.110800+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp5+')&('+jesstemp17+'))|(('+jesstemp5+')&('+jesstemp16+')))&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.120700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.130700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.585500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.231900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.110800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp48 ='n.  ne2'
jesstemp49 ='jessatom0 x. %s'%(4.888400+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(5.635800+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(4.009700+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(5.403500+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(6.272100+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(4.595500+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(1.353400+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(2.282600+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp48+')&('+jesstemp17+'))|(('+jesstemp48+')&('+jesstemp16+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.888400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.635800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.009700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.403500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.272100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.282600+(d*0.300000)))
cmd.select('Jfa_1ga8-D130A-N153A-Q189A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
