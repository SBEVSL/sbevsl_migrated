'''
FUNC:Jfa_3fit
PDB:3fit
EC:3.6.1.29
PFAM:PF11969,PF01230
RESI:gln,his,his
LOCI:a-83,94,96;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. gln'
jesstemp2 ='r. asn'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  oe1'
jesstemp4 ='jessatom0 x. %s'%(1.242300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.242300+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(1.333200+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.252300+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.252300+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. his'
jesstemp12 ='jessatom0 x. %s'%(13.433000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(14.665200+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(12.685600+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(13.433000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(14.665200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(12.685600+(d*0.300000)))
jesstemp15 ='n.  nd1'
jesstemp16 ='jessatom0 x. %s'%(14.685400+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(15.917600+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(13.887500+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(14.685400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(15.917600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(13.887500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp21 ='jessatom0 x. %s'%(14.836900+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(16.079200+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(14.180400+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(2.222000+(d*0.300000))
jesstemp25 ='br. jessatom3'
jesstemp26 ='jessatom4 x. %s'%(2.151300+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp6+')&('+jesstemp11+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(14.836900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(16.079200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(14.180400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.151300+(d*0.300000)))
jesstemp27 ='jessatom0 x. %s'%(8.201200+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(9.403100+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(7.544700+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(6.211500+(d*0.300000))
jesstemp31 ='jessatom4 x. %s'%(7.352800+(d*0.300000))
jesstemp32 ='jessatom5 x. %s'%(7.100300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.403100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.544700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.211500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.352800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.100300+(d*0.300000)))
jesstemp33 ='jessatom0 x. %s'%(8.039600+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(9.271800+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(7.302300+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(5.635800+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(6.837700+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(6.918500+(d*0.300000))
jesstemp39 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.039600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.302300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.635800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.837700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp41 ='jessatom0 x. %s'%(6.635700+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(7.817400+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(5.757000+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(7.585100+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(8.675900+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(8.857700+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(2.222000+(d*0.300000))
jesstemp48 ='br. jessatom6'
jesstemp49 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp11+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.757000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.585100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.857700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_3fit', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
