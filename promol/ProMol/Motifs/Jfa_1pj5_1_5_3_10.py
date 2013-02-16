'''
FUNC:Jfa_1pj5_1_5_3_10
PDB:1pj5
EC:1.5.3.10
RESI:his,tyr,asp
LOCI:a-225,259,552;
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
jesstemp7 ='jessatom0 x. %s'%(2.222000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.171500+(d*0.300000)))
jesstemp10 ='n.  ce1'
jesstemp11 ='r. tyr'
jesstemp12 ='jessatom0 x. %s'%(7.070000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(6.696300+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.878300+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.070000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.878300+(d*0.300000)))
jesstemp15 ='n.  cz '
jesstemp16 ='jessatom0 x. %s'%(5.777200+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(5.454000+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(3.565300+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.434200+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.777200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.454000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.565300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.434200+(d*0.300000)))
jesstemp21 ='n.  oh '
jesstemp22 ='jessatom0 x. %s'%(4.938900+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(4.908600+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(2.817900+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.444200+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.383700+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.908600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.817900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.383700+(d*0.300000)))
jesstemp28 ='r. asp'
jesstemp29 ='r. glu'
jesstemp30 ='jessatom0 x. %s'%(39.430400+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(39.844500+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(39.390000+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(40.602000+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(39.753600+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(39.773800+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp28+'))|(('+jesstemp0+')&('+jesstemp29+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(39.430400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(39.844500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(39.390000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(40.602000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(39.753600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(39.773800+(d*0.300000)))
jesstemp36 ='n.  od1'
jesstemp37 ='n.  od2'
jesstemp38 ='n.  oe1'
jesstemp39 ='n.  oe2'
jesstemp40 ='jessatom0 x. %s'%(38.268900+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(38.672900+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(38.248700+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(39.541500+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(38.672900+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(38.672900+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.272600+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp36+')|('+jesstemp37+'))&('+jesstemp28+'))|((('+jesstemp38+')|('+jesstemp39+'))&('+jesstemp29+')))&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(38.268900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(38.672900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(38.248700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(39.541500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(38.672900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(38.672900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.272600+(d*0.300000)))
jesstemp48 ='n.  od2'
jesstemp49 ='n.  od1'
jesstemp50 ='n.  oe2'
jesstemp51 ='n.  oe1'
jesstemp52 ='jessatom0 x. %s'%(40.016200+(d*0.300000))
jesstemp53 ='jessatom1 x. %s'%(40.379800+(d*0.300000))
jesstemp54 ='jessatom2 x. %s'%(39.945500+(d*0.300000))
jesstemp55 ='jessatom3 x. %s'%(41.096900+(d*0.300000))
jesstemp56 ='jessatom4 x. %s'%(40.268700+(d*0.300000))
jesstemp57 ='jessatom5 x. %s'%(40.319200+(d*0.300000))
jesstemp58 ='jessatom6 x. %s'%(1.282700+(d*0.300000))
jesstemp59 ='br. jessatom6'
jesstemp60 ='jessatom7 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp48+')|('+jesstemp49+'))&('+jesstemp28+'))|((('+jesstemp50+')|('+jesstemp51+'))&('+jesstemp29+')))&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(40.016200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(40.379800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(39.945500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(41.096900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(40.268700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(40.319200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.282700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('Jfa_1pj5_1_5_3_10', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
