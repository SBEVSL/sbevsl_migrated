'''
FUNC:Jfa_1nkh_2_4_1_38
PDB:1nkh
EC:2.4.1.38
RESI:glu,asp,arg
LOCI:b-317,319,359;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  oe1'
jesstemp4 ='n.  oe2'
jesstemp5 ='n.  od1'
jesstemp6 ='n.  od2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  oe2'
jesstemp10 ='n.  oe1'
jesstemp11 ='n.  od2'
jesstemp12 ='n.  od1'
jesstemp13 ='jessatom0 x. %s'%(1.252400+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp16 ='n.  cg '
jesstemp17 ='jessatom0 x. %s'%(7.564900+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(7.857800+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(7.120500+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp16+')&('+jesstemp2+'))|(('+jesstemp16+')&('+jesstemp1+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.564900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.120500+(d*0.300000)))
jesstemp20 ='jessatom0 x. %s'%(8.181000+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(8.302200+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(7.837600+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.272600+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+'))|((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.181000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.837600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.272600+(d*0.300000)))
jesstemp25 ='jessatom0 x. %s'%(7.100300+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(7.463900+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(6.474100+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+'))|((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp23+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.100300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.474100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp30 ='n.  ne '
jesstemp31 ='r. arg'
jesstemp32 ='jessatom0 x. %s'%(9.534400+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(10.160600+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(8.302200+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(7.918400+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(8.675900+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(6.686200+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.534400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.160600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.918400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.686200+(d*0.300000)))
jesstemp38 ='n.  nh1'
jesstemp39 ='n.  nh2'
jesstemp40 ='jessatom0 x. %s'%(11.099900+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(11.786700+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(9.847500+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(10.190900+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(10.978700+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(8.958700+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(2.323000+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp38+')|('+jesstemp39+'))&('+jesstemp31+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(11.099900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.786700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.847500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.190900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(10.978700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.958700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.323000+(d*0.300000)))
jesstemp48 ='n.  nh2'
jesstemp49 ='n.  nh1'
jesstemp50 ='jessatom0 x. %s'%(11.503900+(d*0.300000))
jesstemp51 ='jessatom1 x. %s'%(12.008900+(d*0.300000))
jesstemp52 ='jessatom2 x. %s'%(10.291900+(d*0.300000))
jesstemp53 ='jessatom3 x. %s'%(9.605100+(d*0.300000))
jesstemp54 ='jessatom4 x. %s'%(10.170700+(d*0.300000))
jesstemp55 ='jessatom5 x. %s'%(8.413300+(d*0.300000))
jesstemp56 ='jessatom6 x. %s'%(2.312900+(d*0.300000))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp48+')|('+jesstemp49+'))&('+jesstemp31+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(11.503900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(12.008900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(10.291900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.605100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(10.170700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.413300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('Jfa_1nkh_2_4_1_38', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
