'''
FUNC:Jfa_1ajo
PDB:1ajo
EC:3.2.1.73
PFAM:PF00722
RESI:glu,asp,glu
LOCI:a-193,195,197;
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
jesstemp13 ='jessatom0 x. %s'%(1.282700+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.282700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp16 ='n.  cg '
jesstemp17 ='jessatom0 x. %s'%(3.979400+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(5.161100+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(3.312800+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp16+')&('+jesstemp2+'))|(('+jesstemp16+')&('+jesstemp1+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(3.979400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.161100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.312800+(d*0.300000)))
jesstemp20 ='jessatom0 x. %s'%(3.191600+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(4.423800+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(2.454300+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+'))|((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.191600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.423800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp25 ='jessatom0 x. %s'%(3.908700+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(4.949000+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(3.403700+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(1.242300+(d*0.300000))
jesstemp29 ='br. jessatom3'
jesstemp30 ='jessatom4 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+'))|((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.908700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.403700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.181600+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(7.080100+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(7.958800+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(5.888300+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(4.373300+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(4.807600+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(4.646000+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.080100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.958800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.888300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.373300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.807600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.646000+(d*0.300000)))
jesstemp37 ='jessatom0 x. %s'%(7.171000+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(8.039600+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(6.090300+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(4.242000+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(4.959100+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(4.231900+(d*0.300000))
jesstemp43 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.171000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.039600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.090300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.242000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.959100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.231900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp45 ='jessatom0 x. %s'%(6.837700+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(7.564900+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(5.585300+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(4.837900+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(5.009600+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(5.070200+(d*0.300000))
jesstemp51 ='br. jessatom6'
jesstemp52 ='jessatom7 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp43+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.837700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.564900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.837900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.009600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.070200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1ajo', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
