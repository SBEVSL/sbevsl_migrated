'''
FUNC:Jfa_1kfw_3_2_1_14
PDB:1kfw
EC:3.2.1.14
RESI:asp,glu,tyr
LOCI:a-190,192,271;
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
jesstemp14 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp15 ='n.  cd '
jesstemp16 ='jessatom0 x. %s'%(5.938800+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(6.989200+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(5.797400+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp15+')&('+jesstemp2+'))|(('+jesstemp15+')&('+jesstemp1+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.989200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.797400+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(7.090200+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(8.160800+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(6.817500+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+'))|((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.817500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(4.898500+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(6.019600+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(4.625800+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+'))|((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp22+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.898500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.019600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp29 ='n.  ce1'
jesstemp30 ='r. tyr'
jesstemp31 ='jessatom0 x. %s'%(9.504100+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(10.221200+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(8.494100+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(7.847700+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(7.524500+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(7.463900+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.504100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.221200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.847700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.524500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.463900+(d*0.300000)))
jesstemp37 ='n.  cz '
jesstemp38 ='jessatom0 x. %s'%(9.201100+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(9.797000+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(8.181000+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(8.453700+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(8.322400+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(7.918400+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp37+')&('+jesstemp30+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.797000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.181000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.453700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.322400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.918400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp46 ='n.  oh '
jesstemp47 ='jessatom0 x. %s'%(7.958800+(d*0.300000))
jesstemp48 ='jessatom1 x. %s'%(8.514300+(d*0.300000))
jesstemp49 ='jessatom2 x. %s'%(6.908400+(d*0.300000))
jesstemp50 ='jessatom3 x. %s'%(7.908300+(d*0.300000))
jesstemp51 ='jessatom4 x. %s'%(7.968900+(d*0.300000))
jesstemp52 ='jessatom5 x. %s'%(7.221500+(d*0.300000))
jesstemp53 ='jessatom6 x. %s'%(2.413900+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp46+')&('+jesstemp30+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.958800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.514300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.908400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.968900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.221500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.413900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.393800+(d*0.300000)))
cmd.select('Jfa_1kfw_3_2_1_14', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
