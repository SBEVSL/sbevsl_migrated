'''
FUNC:Jfa_1f17_1_1_1_35
PDB:1f17
EC:1.1.1.35
RESI:ser,his,asn
LOCI:a-137,158,208;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.454300+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.424100+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. his'
jesstemp12 ='jessatom0 x. %s'%(5.272200+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(5.666100+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.918700+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.272200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.666100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.918700+(d*0.300000)))
jesstemp15 ='n.  nd1'
jesstemp16 ='jessatom0 x. %s'%(5.342900+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(5.555000+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(4.878300+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.342900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.555000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.878300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp21 ='n.  ne2'
jesstemp22 ='jessatom0 x. %s'%(3.838000+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(3.757200+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(2.828000+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.211900+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.838000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.828000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.161400+(d*0.300000)))
jesstemp28 ='n.  cd '
jesstemp29 ='r. glu'
jesstemp30 ='r. asp'
jesstemp31 ='jessatom0 x. %s'%(8.625400+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(8.938500+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(8.494100+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(4.797500+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(3.888500+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(5.989300+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp28+')&('+jesstemp29+'))|(('+jesstemp28+')&('+jesstemp30+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.625400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.938500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.888500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.989300+(d*0.300000)))
jesstemp37 ='n.  oe1'
jesstemp38 ='n.  oe2'
jesstemp39 ='n.  od1'
jesstemp40 ='n.  od2'
jesstemp41 ='jessatom0 x. %s'%(7.403300+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(7.696200+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(7.241700+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(3.696600+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(2.676500+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(4.747000+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp37+')|('+jesstemp38+'))&('+jesstemp29+'))|((('+jesstemp39+')|('+jesstemp40+'))&('+jesstemp30+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.696200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.241700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.696600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(2.676500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp49 ='n.  oe2'
jesstemp50 ='n.  oe1'
jesstemp51 ='n.  od2'
jesstemp52 ='n.  od1'
jesstemp53 ='jessatom0 x. %s'%(9.211200+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(9.494000+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(9.180900+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(5.888300+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(4.868200+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(6.868000+(d*0.300000))
jesstemp59 ='br. jessatom6'
jesstemp60 ='jessatom7 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp49+')|('+jesstemp50+'))&('+jesstemp29+'))|((('+jesstemp51+')|('+jesstemp52+'))&('+jesstemp30+')))&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp47+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.211200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.494000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.180900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.888300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.868200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.868000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
jesstemp61 ='r. asn'
jesstemp62 ='r. gln'
jesstemp63 ='jessatom0 x. %s'%(6.049900+(d*0.300000))
jesstemp64 ='jessatom1 x. %s'%(5.302500+(d*0.300000))
jesstemp65 ='jessatom2 x. %s'%(5.312600+(d*0.300000))
jesstemp66 ='jessatom3 x. %s'%(6.746800+(d*0.300000))
jesstemp67 ='jessatom4 x. %s'%(5.575200+(d*0.300000))
jesstemp68 ='jessatom5 x. %s'%(5.292400+(d*0.300000))
jesstemp69 ='jessatom6 x. %s'%(6.898300+(d*0.300000))
jesstemp70 ='jessatom7 x. %s'%(6.039800+(d*0.300000))
jesstemp71 ='jessatom8 x. %s'%(6.868000+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp10+')&('+jesstemp61+'))|(('+jesstemp10+')&('+jesstemp62+')))&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(6.049900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.302500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(6.746800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(5.575200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(5.292400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(6.898300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(6.039800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(6.868000+(d*0.300000)))
jesstemp72 ='jessatom0 x. %s'%(6.948800+(d*0.300000))
jesstemp73 ='jessatom1 x. %s'%(6.019600+(d*0.300000))
jesstemp74 ='jessatom2 x. %s'%(5.827700+(d*0.300000))
jesstemp75 ='jessatom3 x. %s'%(7.312400+(d*0.300000))
jesstemp76 ='jessatom4 x. %s'%(6.140800+(d*0.300000))
jesstemp77 ='jessatom5 x. %s'%(5.817600+(d*0.300000))
jesstemp78 ='jessatom6 x. %s'%(7.362900+(d*0.300000))
jesstemp79 ='jessatom7 x. %s'%(6.585200+(d*0.300000))
jesstemp80 ='jessatom8 x. %s'%(7.352800+(d*0.300000))
jesstemp81 ='jessatom9 x. %s'%(1.242300+(d*0.300000))
jesstemp82 ='br. jessatom9'
cmd.select('jessatom10', '(((('+jesstemp39+')&('+jesstemp61+'))|(('+jesstemp39+')&('+jesstemp62+')))&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(6.019600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(7.312400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(5.817600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(7.362900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.585200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(7.352800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.242300+(d*0.300000)))
jesstemp83 ='n.  nd2'
jesstemp84 ='jessatom0 x. %s'%(4.787400+(d*0.300000))
jesstemp85 ='jessatom1 x. %s'%(4.090500+(d*0.300000))
jesstemp86 ='jessatom2 x. %s'%(4.070300+(d*0.300000))
jesstemp87 ='jessatom3 x. %s'%(5.676200+(d*0.300000))
jesstemp88 ='jessatom4 x. %s'%(4.625800+(d*0.300000))
jesstemp89 ='jessatom5 x. %s'%(4.080400+(d*0.300000))
jesstemp90 ='jessatom6 x. %s'%(6.595300+(d*0.300000))
jesstemp91 ='jessatom7 x. %s'%(5.575200+(d*0.300000))
jesstemp92 ='jessatom8 x. %s'%(6.787200+(d*0.300000))
jesstemp93 ='jessatom9 x. %s'%(1.343300+(d*0.300000))
jesstemp94 ='br. jessatom9'
jesstemp95 ='jessatom10 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom11', '(((('+jesstemp83+')&('+jesstemp61+'))|(('+jesstemp83+')&('+jesstemp62+')))&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(4.787400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(4.090500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.070300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(4.080400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(6.595300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(5.575200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.787200+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.272500+(d*0.300000)))
cmd.select('Jfa_1f17_1_1_1_35', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
