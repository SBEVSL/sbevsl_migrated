'''
FUNC:Jfa_1nhc
PDB:1nhc
EC:3.2.1.15
PFAM:PF00295
RESI:asp,asp,asp,his
LOCI:a-186,207,208,229;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.282700+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.282700+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.252400+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.191700+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(4.242000+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(4.797500+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(3.322900+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.242000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.322900+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(4.999500+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(5.474200+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(3.928900+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.282700+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.474200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.928900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.282700+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(4.019800+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(4.282400+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(3.403700+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(1.272600+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.019800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.282400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.403700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(5.423700+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(5.120700+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(5.706500+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(4.989400+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(5.989300+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(3.807700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.423700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.120700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.706500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.989300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.807700+(d*0.300000)))
jesstemp36 ='jessatom0 x. %s'%(5.221700+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(4.686400+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(5.484300+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(4.949000+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(5.767100+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(3.676400+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.221700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.686400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.484300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.767100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.676400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp44 ='jessatom0 x. %s'%(6.585200+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(6.352900+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(6.767000+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(5.544900+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(6.504400+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(4.433900+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp51 ='br. jessatom6'
jesstemp52 ='jessatom7 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.585200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.352900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.767000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.504400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.433900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.171500+(d*0.300000)))
jesstemp53 ='r. his'
jesstemp54 ='jessatom0 x. %s'%(7.979000+(d*0.300000))
jesstemp55 ='jessatom1 x. %s'%(8.322400+(d*0.300000))
jesstemp56 ='jessatom2 x. %s'%(7.413400+(d*0.300000))
jesstemp57 ='jessatom3 x. %s'%(4.403600+(d*0.300000))
jesstemp58 ='jessatom4 x. %s'%(4.858100+(d*0.300000))
jesstemp59 ='jessatom5 x. %s'%(4.252100+(d*0.300000))
jesstemp60 ='jessatom6 x. %s'%(5.201500+(d*0.300000))
jesstemp61 ='jessatom7 x. %s'%(5.706500+(d*0.300000))
jesstemp62 ='jessatom8 x. %s'%(4.676300+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp0+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(7.979000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(8.322400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(7.413400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(4.403600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(4.252100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(5.201500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(5.706500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(4.676300+(d*0.300000)))
jesstemp63 ='n.  nd1'
jesstemp64 ='jessatom0 x. %s'%(7.504300+(d*0.300000))
jesstemp65 ='jessatom1 x. %s'%(7.777000+(d*0.300000))
jesstemp66 ='jessatom2 x. %s'%(6.837700+(d*0.300000))
jesstemp67 ='jessatom3 x. %s'%(3.676400+(d*0.300000))
jesstemp68 ='jessatom4 x. %s'%(3.878400+(d*0.300000))
jesstemp69 ='jessatom5 x. %s'%(3.535000+(d*0.300000))
jesstemp70 ='jessatom6 x. %s'%(5.161100+(d*0.300000))
jesstemp71 ='jessatom7 x. %s'%(5.363100+(d*0.300000))
jesstemp72 ='jessatom8 x. %s'%(4.848000+(d*0.300000))
jesstemp73 ='jessatom9 x. %s'%(1.393800+(d*0.300000))
jesstemp74 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp63+')&('+jesstemp53+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(7.504300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(7.777000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(6.837700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(3.676400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(3.878400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(3.535000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(5.161100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.848000+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.393800+(d*0.300000)))
jesstemp75 ='n.  ne2'
jesstemp76 ='jessatom0 x. %s'%(8.908200+(d*0.300000))
jesstemp77 ='jessatom1 x. %s'%(9.393000+(d*0.300000))
jesstemp78 ='jessatom2 x. %s'%(8.080000+(d*0.300000))
jesstemp79 ='jessatom3 x. %s'%(4.797500+(d*0.300000))
jesstemp80 ='jessatom4 x. %s'%(4.747000+(d*0.300000))
jesstemp81 ='jessatom5 x. %s'%(5.140900+(d*0.300000))
jesstemp82 ='jessatom6 x. %s'%(7.150800+(d*0.300000))
jesstemp83 ='jessatom7 x. %s'%(7.463900+(d*0.300000))
jesstemp84 ='jessatom8 x. %s'%(6.777100+(d*0.300000))
jesstemp85 ='jessatom9 x. %s'%(2.222000+(d*0.300000))
jesstemp86 ='br. jessatom9'
jesstemp87 ='jessatom10 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp75+')&('+jesstemp53+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(8.908200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(9.393000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(8.080000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(5.140900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.150800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.777100+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.161400+(d*0.300000)))
cmd.select('Jfa_1nhc', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
