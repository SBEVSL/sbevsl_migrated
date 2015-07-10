'''
FUNC:Jfa_1dg9-C12A-C17A-R18A-D129A
PDB:1dg9
EC:3.1.3.2
PFAM:PF01451
RESI:cys,cys,arg,asp
LOCI:a-12,17,18,129;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. cys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. cys'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='n.  sg '
jesstemp7 ='jessatom0 x. %s'%(2.797700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.838200+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.797700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.838200+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(8.160800+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(6.767000+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(5.494400+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.767000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.494400+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(8.504200+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(7.059900+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(6.049900+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp17 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.504200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.059900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.049900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(9.625300+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(8.282000+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(7.181100+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(2.817900+(d*0.300000))
jesstemp22 ='br. jessatom3'
jesstemp23 ='jessatom4 x. %s'%(1.828100+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.625300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.282000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.181100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.817900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.828100+(d*0.300000)))
jesstemp24 ='n.  ne '
jesstemp25 ='r. arg'
jesstemp26 ='jessatom0 x. %s'%(5.312600+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(3.999600+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(4.736900+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(6.100400+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(5.565100+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(6.817500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.736900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.100400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.565100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.817500+(d*0.300000)))
jesstemp32 ='n.  nh1'
jesstemp33 ='n.  nh2'
jesstemp34 ='jessatom0 x. %s'%(5.918600+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(5.080300+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(6.363000+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(8.433500+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(7.797200+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(8.888000+(d*0.300000))
jesstemp40 ='jessatom6 x. %s'%(2.353300+(d*0.300000))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp32+')|('+jesstemp33+'))&('+jesstemp25+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.080300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.363000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.433500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.797200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.888000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.353300+(d*0.300000)))
jesstemp42 ='n.  nh2'
jesstemp43 ='n.  nh1'
jesstemp44 ='jessatom0 x. %s'%(4.605600+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(3.797600+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(4.827800+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(7.433600+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(6.888200+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(7.756800+(d*0.300000))
jesstemp50 ='br. jessatom6'
jesstemp51 ='jessatom7 x. %s'%(2.363400+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp42+')|('+jesstemp43+'))&('+jesstemp25+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp40+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.605600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.797600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.827800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.433600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.888200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.756800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.353300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.363400+(d*0.300000)))
jesstemp52 ='n.  cg '
jesstemp53 ='r. asp'
jesstemp54 ='r. glu'
jesstemp55 ='jessatom0 x. %s'%(8.615300+(d*0.300000))
jesstemp56 ='jessatom1 x. %s'%(7.554800+(d*0.300000))
jesstemp57 ='jessatom2 x. %s'%(7.837600+(d*0.300000))
jesstemp58 ='jessatom3 x. %s'%(7.474000+(d*0.300000))
jesstemp59 ='jessatom4 x. %s'%(6.201400+(d*0.300000))
jesstemp60 ='jessatom5 x. %s'%(6.292300+(d*0.300000))
jesstemp61 ='jessatom6 x. %s'%(4.534900+(d*0.300000))
jesstemp62 ='jessatom7 x. %s'%(4.858100+(d*0.300000))
jesstemp63 ='jessatom8 x. %s'%(4.282400+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp52+')&('+jesstemp53+'))|(('+jesstemp52+')&('+jesstemp54+')))&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(8.615300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(7.554800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(7.837600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(7.474000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(6.292300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(4.534900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(4.282400+(d*0.300000)))
jesstemp64 ='n.  od1'
jesstemp65 ='n.  od2'
jesstemp66 ='n.  oe1'
jesstemp67 ='n.  oe2'
jesstemp68 ='jessatom0 x. %s'%(8.463800+(d*0.300000))
jesstemp69 ='jessatom2 x. %s'%(7.827500+(d*0.300000))
jesstemp70 ='jessatom3 x. %s'%(7.948700+(d*0.300000))
jesstemp71 ='jessatom4 x. %s'%(6.767000+(d*0.300000))
jesstemp72 ='jessatom5 x. %s'%(6.696300+(d*0.300000))
jesstemp73 ='jessatom6 x. %s'%(5.080300+(d*0.300000))
jesstemp74 ='jessatom7 x. %s'%(5.272200+(d*0.300000))
jesstemp75 ='jessatom8 x. %s'%(4.262200+(d*0.300000))
jesstemp76 ='jessatom9 x. %s'%(1.222100+(d*0.300000))
jesstemp77 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp64+')|('+jesstemp65+'))&('+jesstemp53+'))|((('+jesstemp66+')|('+jesstemp67+'))&('+jesstemp54+')))&('+jesstemp68+')&('+jesstemp56+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(8.463800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(7.554800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(7.827500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(7.948700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(6.767000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(5.080300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(5.272200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.262200+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.222100+(d*0.300000)))
jesstemp78 ='n.  od2'
jesstemp79 ='n.  od1'
jesstemp80 ='n.  oe2'
jesstemp81 ='n.  oe1'
jesstemp82 ='jessatom0 x. %s'%(8.948600+(d*0.300000))
jesstemp83 ='jessatom1 x. %s'%(7.736600+(d*0.300000))
jesstemp84 ='jessatom2 x. %s'%(7.756800+(d*0.300000))
jesstemp85 ='jessatom3 x. %s'%(6.514500+(d*0.300000))
jesstemp86 ='jessatom4 x. %s'%(5.130800+(d*0.300000))
jesstemp87 ='jessatom5 x. %s'%(5.140900+(d*0.300000))
jesstemp88 ='jessatom6 x. %s'%(4.646000+(d*0.300000))
jesstemp89 ='jessatom7 x. %s'%(5.504500+(d*0.300000))
jesstemp90 ='jessatom8 x. %s'%(4.928800+(d*0.300000))
jesstemp91 ='jessatom9 x. %s'%(1.333200+(d*0.300000))
jesstemp92 ='br. jessatom9'
jesstemp93 ='jessatom10 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp78+')|('+jesstemp79+'))&('+jesstemp53+'))|((('+jesstemp80+')|('+jesstemp81+'))&('+jesstemp54+')))&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(8.948600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(7.736600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(7.756800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(6.514500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(5.130800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(5.140900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.646000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(5.504500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.272500+(d*0.300000)))
cmd.select('Jfa_1dg9-C12A-C17A-R18A-D129A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
