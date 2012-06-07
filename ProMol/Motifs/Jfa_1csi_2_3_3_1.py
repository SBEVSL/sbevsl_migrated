'''
FUNC:Jfa_1csi_2_3_3_1
PDB:1csi
EC:2.3.3.1
RESI:ser,his,his,asp
LOCI:a-244,274,320,375;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.403900+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.403900+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.222000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.191700+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(10.180800+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(9.059700+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(10.443400+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.180800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.059700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(10.443400+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(10.251500+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(9.160700+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(10.281800+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(1.403900+(d*0.300000))
jesstemp17 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.251500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.160700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.281800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.403900+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(8.736500+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(7.514400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(8.675900+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(2.242200+(d*0.300000))
jesstemp22 ='br. jessatom3'
jesstemp23 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.736500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.514400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.242200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp24 ='r. asp'
jesstemp25 ='r. glu'
jesstemp26 ='jessatom0 x. %s'%(8.009300+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(7.140700+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(8.888000+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(9.524300+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(10.453500+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(8.574900+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp24+'))|(('+jesstemp0+')&('+jesstemp25+')))&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.009300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.140700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.888000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.524300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.453500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.574900+(d*0.300000)))
jesstemp32 ='n.  od1'
jesstemp33 ='n.  od2'
jesstemp34 ='n.  oe1'
jesstemp35 ='n.  oe2'
jesstemp36 ='jessatom0 x. %s'%(8.160800+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(7.282100+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(8.807200+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(10.291900+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(11.130200+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(9.130400+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.323100+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp32+')|('+jesstemp33+'))&('+jesstemp24+'))|((('+jesstemp34+')|('+jesstemp35+'))&('+jesstemp25+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.282100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.807200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.291900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(11.130200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.323100+(d*0.300000)))
jesstemp44 ='n.  od2'
jesstemp45 ='n.  od1'
jesstemp46 ='n.  oe2'
jesstemp47 ='n.  oe1'
jesstemp48 ='jessatom0 x. %s'%(7.100300+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(6.191300+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(8.069900+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(8.585000+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(9.483900+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(7.645700+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(1.212000+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp44+')|('+jesstemp45+'))&('+jesstemp24+'))|((('+jesstemp46+')|('+jesstemp47+'))&('+jesstemp25+')))&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.100300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.191300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.069900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.585000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.483900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.645700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.212000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('Jfa_1csi_2_3_3_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
