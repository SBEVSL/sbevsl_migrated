'''
FUNC:Jfa_1nv2
PDB:1nv2
EC:3.1.3.11
PFAM:PF00459,PF00316
RESI:asp,asp,glu
LOCI:a-1068,1074,1098;
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
jesstemp13 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(8.080000+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(9.261700+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(7.484100+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.080000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.261700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.484100+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(8.302200+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(9.483900+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(7.544700+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.483900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.544700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(7.221500+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(8.362800+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(6.746800+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp22+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.221500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.362800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.746800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.232100+(d*0.300000)))
jesstemp29 ='n.  cd '
jesstemp30 ='jessatom0 x. %s'%(7.777000+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(9.029400+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(7.312400+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(4.403600+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(4.706600+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(4.797500+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp29+')&('+jesstemp2+'))|(('+jesstemp29+')&('+jesstemp1+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.777000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.029400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.312400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.403600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.706600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.797500+(d*0.300000)))
jesstemp36 ='jessatom0 x. %s'%(7.463900+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(8.696100+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(7.191200+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(4.524800+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(5.130800+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(4.646000+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+'))|((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.696100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.191200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.524800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.130800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.646000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp44 ='jessatom0 x. %s'%(7.049800+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(8.302200+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(6.423600+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(4.151100+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(4.201600+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(4.514700+(d*0.300000))
jesstemp50 ='br. jessatom6'
jesstemp51 ='jessatom7 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+'))|((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp42+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.049800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.423600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.151100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.201600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.514700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('Jfa_1nv2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
