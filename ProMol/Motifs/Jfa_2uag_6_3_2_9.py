'''
FUNC:Jfa_2uag_6_3_2_9
PDB:2uag
EC:6.3.2.9
RESI:lys,asn,his
LOCI:a-115,138,183;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. lys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  ce '
jesstemp3 ='r. lys'
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='n.  nz '
jesstemp7 ='jessatom0 x. %s'%(2.504800+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.504900+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.504800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.504900+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. asn'
jesstemp12 ='r. gln'
jesstemp13 ='jessatom0 x. %s'%(5.959000+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(5.050000+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(6.090300+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.050000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.090300+(d*0.300000)))
jesstemp16 ='n.  od1'
jesstemp17 ='jessatom0 x. %s'%(6.918500+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(5.938800+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(6.857900+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp16+')&('+jesstemp11+'))|(('+jesstemp16+')&('+jesstemp12+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp22 ='n.  nd2'
jesstemp23 ='jessatom0 x. %s'%(5.161100+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(4.050100+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(4.959100+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(1.343300+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp22+')&('+jesstemp11+'))|(('+jesstemp22+')&('+jesstemp12+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.161100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.050100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.959100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.272500+(d*0.300000)))
jesstemp29 ='r. his'
jesstemp30 ='jessatom0 x. %s'%(9.766700+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(8.797100+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(8.100200+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(9.716200+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(9.302100+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(9.231400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.766700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.797100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.100200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.716200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.302100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.231400+(d*0.300000)))
jesstemp36 ='n.  nd1'
jesstemp37 ='jessatom0 x. %s'%(10.110100+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(8.978900+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(8.352700+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(9.302100+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(8.787000+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(8.857700+(d*0.300000))
jesstemp43 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp36+')&('+jesstemp29+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.110100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.352700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.302100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.787000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.857700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp45 ='n.  ne2'
jesstemp46 ='jessatom0 x. %s'%(7.999200+(d*0.300000))
jesstemp47 ='jessatom1 x. %s'%(6.857900+(d*0.300000))
jesstemp48 ='jessatom2 x. %s'%(6.150900+(d*0.300000))
jesstemp49 ='jessatom3 x. %s'%(7.878000+(d*0.300000))
jesstemp50 ='jessatom4 x. %s'%(7.605300+(d*0.300000))
jesstemp51 ='jessatom5 x. %s'%(7.221500+(d*0.300000))
jesstemp52 ='jessatom6 x. %s'%(2.272500+(d*0.300000))
jesstemp53 ='br. jessatom6'
jesstemp54 ='jessatom7 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp45+')&('+jesstemp29+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.999200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.150900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.878000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.605300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.221500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.272500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('Jfa_2uag_6_3_2_9', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
