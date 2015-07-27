'''
FUNC:Jfa_1pow-R264A-F479A-E483A
PDB:1pow
EC:1.2.3.3
PFAM:PF02775,PF00205,PF02776
RESI:arg,phe,glu
LOCI:a-264,479,483;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.353300+(d*0.300000))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.353300+(d*0.300000)))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='jessatom0 x. %s'%(2.323000+(d*0.300000))
jesstemp10 ='br. jessatom0'
jesstemp11 ='jessatom1 x. %s'%(2.333100+(d*0.300000))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.333100+(d*0.300000)))
jesstemp12 ='n.  ce1'
jesstemp13 ='n.  ce2'
jesstemp14 ='r. phe'
jesstemp15 ='jessatom0 x. %s'%(3.797600+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(3.848100+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(3.696600+(d*0.300000))
cmd.select('jessatom3', '((('+jesstemp12+')|('+jesstemp13+'))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(3.797600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.848100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.696600+(d*0.300000)))
jesstemp18 ='n.  ce2'
jesstemp19 ='n.  ce1'
jesstemp20 ='jessatom0 x. %s'%(4.716700+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(3.514800+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(4.524800+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(2.403800+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp14+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.716700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.514800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.524800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.403800+(d*0.300000)))
jesstemp25 ='n.  cz '
jesstemp26 ='jessatom0 x. %s'%(3.969300+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(4.211700+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp29 ='br. jessatom3'
jesstemp30 ='jessatom4 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp25+')&('+jesstemp14+')&('+jesstemp26+')&('+jesstemp21+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.969300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.514800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.211700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.393800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.393800+(d*0.300000)))
jesstemp31 ='n.  cd '
jesstemp32 ='r. glu'
jesstemp33 ='r. asp'
jesstemp34 ='jessatom0 x. %s'%(5.999400+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(3.747100+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(4.918700+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(6.595300+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(5.221700+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(6.110500+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp31+')&('+jesstemp32+'))|(('+jesstemp31+')&('+jesstemp33+')))&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.999400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(3.747100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.918700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.595300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.221700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.110500+(d*0.300000)))
jesstemp40 ='n.  oe1'
jesstemp41 ='n.  oe2'
jesstemp42 ='n.  od1'
jesstemp43 ='n.  od2'
jesstemp44 ='jessatom0 x. %s'%(7.211400+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(4.959100+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(5.989300+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(7.524500+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(6.009500+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(7.039700+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp40+')|('+jesstemp41+'))&('+jesstemp32+'))|((('+jesstemp42+')|('+jesstemp43+'))&('+jesstemp33+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.211400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.959100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.989300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.524500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.009500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp52 ='n.  oe2'
jesstemp53 ='n.  oe1'
jesstemp54 ='n.  od2'
jesstemp55 ='n.  od1'
jesstemp56 ='jessatom0 x. %s'%(5.494400+(d*0.300000))
jesstemp57 ='jessatom1 x. %s'%(3.141100+(d*0.300000))
jesstemp58 ='jessatom2 x. %s'%(4.757100+(d*0.300000))
jesstemp59 ='jessatom3 x. %s'%(5.847900+(d*0.300000))
jesstemp60 ='jessatom4 x. %s'%(4.242000+(d*0.300000))
jesstemp61 ='jessatom5 x. %s'%(5.171200+(d*0.300000))
jesstemp62 ='jessatom6 x. %s'%(1.232200+(d*0.300000))
jesstemp63 ='br. jessatom6'
jesstemp64 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp52+')|('+jesstemp53+'))&('+jesstemp32+'))|((('+jesstemp54+')|('+jesstemp55+'))&('+jesstemp33+')))&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.494400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.141100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.757100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.847900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.242000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.232200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_1pow-R264A-F479A-E483A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
