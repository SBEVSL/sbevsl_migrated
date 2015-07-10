'''
FUNC:Jfa_1kdn-K19A-N119A
PDB:1kdn
EC:2.7.4.6
PFAM:PF00334
RESI:lys,asn
LOCI:a-19,119;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. lys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  ce '
jesstemp3 ='r. lys'
jesstemp4 ='jessatom0 x. %s'%(1.515000+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.515000+(d*0.300000)))
jesstemp6 ='n.  nz '
jesstemp7 ='jessatom0 x. %s'%(2.494700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.484700+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.494700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.484700+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. asn'
jesstemp12 ='r. gln'
jesstemp13 ='jessatom0 x. %s'%(4.858100+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(4.484400+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(3.676400+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.484400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.676400+(d*0.300000)))
jesstemp16 ='n.  od1'
jesstemp17 ='jessatom0 x. %s'%(3.646100+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(3.393600+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(2.676500+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp16+')&('+jesstemp11+'))|(('+jesstemp16+')&('+jesstemp12+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.646100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.393600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.676500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp22 ='n.  nd2'
jesstemp23 ='jessatom0 x. %s'%(5.686300+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(4.999500+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(3.979400+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(1.343300+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.282600+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp22+')&('+jesstemp11+'))|(('+jesstemp22+')&('+jesstemp12+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.979400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.282600+(d*0.300000)))
jesstemp29 ='r. his'
jesstemp30 ='jessatom0 x. %s'%(6.393300+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(5.231800+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(5.938800+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(8.544600+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(7.908300+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(8.443600+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.393300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.443600+(d*0.300000)))
jesstemp36 ='n.  nd1'
jesstemp37 ='jessatom0 x. %s'%(6.888200+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(5.544900+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(5.918600+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(8.413300+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(8.100200+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.383700+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp36+')&('+jesstemp29+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp34+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.888200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.413300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.100200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.383700+(d*0.300000)))
jesstemp44 ='n.  ne2'
jesstemp45 ='jessatom0 x. %s'%(8.574900+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(7.373000+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(7.938600+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(10.453500+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(9.928300+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(10.180800+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(2.211900+(d*0.300000))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(2.151300+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp44+')&('+jesstemp29+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.574900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.373000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(10.453500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.928300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(10.180800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.151300+(d*0.300000)))
cmd.select('Jfa_1kdn-K19A-N119A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
