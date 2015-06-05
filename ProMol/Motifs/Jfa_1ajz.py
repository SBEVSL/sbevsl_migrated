'''
FUNC:Jfa_1ajz
PDB:1ajz
EC:2.5.1.15
PFAM:PF00809
RESI:asn,arg,arg
LOCI:a-22,63,255;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='jessatom0 x. %s'%(1.252400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.252400+(d*0.300000)))
jesstemp6 ='n.  nd2'
jesstemp7 ='jessatom0 x. %s'%(1.353400+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.302800+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.302800+(d*0.300000)))
jesstemp10 ='n.  ne '
jesstemp11 ='r. arg'
jesstemp12 ='jessatom0 x. %s'%(7.171000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(7.746700+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(6.100400+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.171000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.746700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.100400+(d*0.300000)))
jesstemp15 ='n.  nh1'
jesstemp16 ='n.  nh2'
jesstemp17 ='jessatom0 x. %s'%(8.231500+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(9.069800+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(7.090200+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(2.363400+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp11+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.231500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.069800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.363400+(d*0.300000)))
jesstemp22 ='n.  nh2'
jesstemp23 ='n.  nh1'
jesstemp24 ='jessatom0 x. %s'%(6.393300+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(7.221500+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(5.130800+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.312900+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp22+')|('+jesstemp23+'))&('+jesstemp11+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.393300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.221500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.130800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.312900+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(7.352800+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.746800+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(10.029300+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(11.685700+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(9.534400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp19+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.352800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.746800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.029300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(11.685700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.534400+(d*0.300000)))
jesstemp35 ='jessatom0 x. %s'%(7.019500+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(6.696300+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(6.383200+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(8.069900+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(9.696000+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(7.635600+(d*0.300000))
jesstemp41 ='jessatom6 x. %s'%(2.333100+(d*0.300000))
jesstemp42 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp11+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.019500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.383200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.069900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.696000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.333100+(d*0.300000)))
jesstemp43 ='jessatom0 x. %s'%(5.191400+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(4.635900+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(4.898500+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(8.150700+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(9.827300+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(7.696200+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(2.302800+(d*0.300000))
jesstemp50 ='br. jessatom6'
jesstemp51 ='jessatom7 x. %s'%(2.323000+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp22+')|('+jesstemp23+'))&('+jesstemp11+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.191400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.635900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.898500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.150700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.827300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.696200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.302800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('Jfa_1ajz', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
