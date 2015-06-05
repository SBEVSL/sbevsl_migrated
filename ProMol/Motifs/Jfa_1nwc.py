'''
FUNC:Jfa_1nwc
PDB:1nwc
EC:1.2.1.11
PFAM:PF01118,PF02774
RESI:cys,gln,his
LOCI:a-136,163,277;
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
jesstemp6 ='n.  sg '
jesstemp7 ='jessatom0 x. %s'%(2.848200+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.818000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.848200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.818000+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. gln'
jesstemp12 ='r. asn'
jesstemp13 ='jessatom0 x. %s'%(7.655800+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(7.130600+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(5.827700+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.655800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.130600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.827700+(d*0.300000)))
jesstemp16 ='n.  oe1'
jesstemp17 ='jessatom0 x. %s'%(6.918500+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(6.292300+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(4.827800+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp16+')&('+jesstemp11+'))|(('+jesstemp16+')&('+jesstemp12+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.292300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.827800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp22 ='n.  ne2'
jesstemp23 ='jessatom0 x. %s'%(8.312300+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(7.999200+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(6.726600+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(1.333200+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp22+')&('+jesstemp11+'))|(('+jesstemp22+')&('+jesstemp12+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.312300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.999200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.726600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.272500+(d*0.300000)))
jesstemp29 ='n.  cg '
jesstemp30 ='r. his'
jesstemp31 ='jessatom0 x. %s'%(6.090300+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(5.191400+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(4.898500+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(4.615700+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(4.555100+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(5.746900+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.090300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.191400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.898500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.615700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.555100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.746900+(d*0.300000)))
jesstemp37 ='n.  nd1'
jesstemp38 ='jessatom0 x. %s'%(7.029600+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(5.938800+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(5.353000+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(4.595500+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(4.484400+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(5.837800+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp37+')&('+jesstemp30+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.353000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.484400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.837800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp46 ='jessatom0 x. %s'%(5.342900+(d*0.300000))
jesstemp47 ='jessatom1 x. %s'%(4.161200+(d*0.300000))
jesstemp48 ='jessatom2 x. %s'%(3.262300+(d*0.300000))
jesstemp49 ='jessatom3 x. %s'%(4.211700+(d*0.300000))
jesstemp50 ='jessatom4 x. %s'%(3.565300+(d*0.300000))
jesstemp51 ='jessatom5 x. %s'%(5.474200+(d*0.300000))
jesstemp52 ='jessatom6 x. %s'%(2.211900+(d*0.300000))
jesstemp53 ='br. jessatom6'
jesstemp54 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp22+')&('+jesstemp30+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.342900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.161200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(3.262300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.211700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(3.565300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.474200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_1nwc', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
