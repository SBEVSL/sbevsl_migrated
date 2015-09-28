'''
FUNC:Jfa_1f61_4_1_3_1
PDB:1f61
EC:4.1.3.1
RESI:his,cys,arg
LOCI:a-180,191,228;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.393800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.393800+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.232100+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp10 ='n.  ca '
jesstemp11 ='r. cys'
jesstemp12 ='jessatom0 x. %s'%(23.735000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(22.371500+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(22.856300+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(23.735000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(22.371500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(22.856300+(d*0.300000)))
jesstemp15 ='n.  cb '
jesstemp16 ='jessatom0 x. %s'%(24.290500+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(22.927000+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(23.320900+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.555400+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(24.290500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(22.927000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(23.320900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.555400+(d*0.300000)))
jesstemp21 ='n.  sg '
jesstemp22 ='jessatom0 x. %s'%(23.270400+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(21.896800+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(22.270500+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.817900+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.797800+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(23.270400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(21.896800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(22.270500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.817900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.797800+(d*0.300000)))
jesstemp28 ='n.  ne '
jesstemp29 ='r. arg'
jesstemp30 ='jessatom0 x. %s'%(7.049800+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.009500+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(6.948800+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(17.786100+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(18.594100+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(17.897200+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.049800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.009500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(17.786100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(18.594100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(17.897200+(d*0.300000)))
jesstemp36 ='n.  nh1'
jesstemp37 ='n.  nh2'
jesstemp38 ='jessatom0 x. %s'%(6.635700+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(5.565100+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(5.807500+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(17.826500+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(18.472900+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(17.685100+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(2.343200+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp36+')|('+jesstemp37+'))&('+jesstemp29+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.565100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(17.826500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(18.472900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(17.685100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.343200+(d*0.300000)))
jesstemp46 ='n.  nh2'
jesstemp47 ='n.  nh1'
jesstemp48 ='jessatom0 x. %s'%(8.595100+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(7.413400+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(7.979000+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(15.745900+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(16.483200+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(15.786300+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(2.343200+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp46+')|('+jesstemp47+'))&('+jesstemp29+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp44+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.595100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.413400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.979000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(15.745900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(16.483200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(15.786300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.343200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.343200+(d*0.300000)))
cmd.select('Jfa_1f61_4_1_3_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
