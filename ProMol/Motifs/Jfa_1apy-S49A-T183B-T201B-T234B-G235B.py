'''
FUNC:Jfa_1apy-S49A-T183B-T201B-T234B-G235B
PDB:1apy
EC:3.5.1.26
PFAM:PF01112
RESI:ser,thr,thr,thr,gly
LOCI:a-49;b-183,201,234,235;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. thr'
jesstemp2 ='r. ser'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.585700+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.585700+(d*0.300000)))
jesstemp6 ='n.  og1'
jesstemp7 ='jessatom0 x. %s'%(2.494700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.444300+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.494700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.444300+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(4.393500+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(4.918700+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(4.524800+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.393500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.918700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.524800+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(3.858200+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(3.908700+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(3.242100+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(1.565500+(d*0.300000))
jesstemp17 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.858200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.908700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.242100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.565500+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(3.716800+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(3.747100+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(2.767400+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(2.464400+(d*0.300000))
jesstemp22 ='br. jessatom3'
jesstemp23 ='jessatom4 x. %s'%(1.444300+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.716800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.747100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.767400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.464400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.444300+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(6.312500+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(5.019700+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(5.534800+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(9.746500+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(8.484000+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(8.282000+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.312500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.534800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.746500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.484000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.282000+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(5.585300+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(4.595500+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(5.443900+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(9.483900+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(8.393100+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(8.181000+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.575600+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.443900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.483900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.393100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.181000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.575600+(d*0.300000)))
jesstemp38 ='jessatom0 x. %s'%(4.625800+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(3.757200+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(4.534900+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(8.665800+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(7.605300+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(7.211400+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(2.474500+(d*0.300000))
jesstemp45 ='br. jessatom6'
jesstemp46 ='jessatom7 x. %s'%(1.444300+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.534900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.665800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.605300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.211400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.444300+(d*0.300000)))
jesstemp47 ='n.  n  '
jesstemp48 ='jessatom0 x. %s'%(6.797300+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(5.504500+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(5.514600+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(10.039400+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(8.675900+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(8.100200+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(2.454300+(d*0.300000))
jesstemp55 ='jessatom7 x. %s'%(3.262300+(d*0.300000))
jesstemp56 ='jessatom8 x. %s'%(3.110800+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(6.797300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.504500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(5.514600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(10.039400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(8.100200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(3.262300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(3.110800+(d*0.300000)))
jesstemp57 ='jessatom0 x. %s'%(7.908300+(d*0.300000))
jesstemp58 ='jessatom1 x. %s'%(6.686200+(d*0.300000))
jesstemp59 ='jessatom2 x. %s'%(6.514500+(d*0.300000))
jesstemp60 ='jessatom3 x. %s'%(11.019100+(d*0.300000))
jesstemp61 ='jessatom4 x. %s'%(9.645500+(d*0.300000))
jesstemp62 ='jessatom5 x. %s'%(8.908200+(d*0.300000))
jesstemp63 ='jessatom6 x. %s'%(3.827900+(d*0.300000))
jesstemp64 ='jessatom7 x. %s'%(4.585400+(d*0.300000))
jesstemp65 ='jessatom8 x. %s'%(4.322800+(d*0.300000))
jesstemp66 ='jessatom9 x. %s'%(1.464500+(d*0.300000))
jesstemp67 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp0+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(6.686200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(6.514500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(11.019100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(8.908200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(3.827900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(4.585400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.322800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.464500+(d*0.300000)))
jesstemp68 ='n.  c  '
jesstemp69 ='jessatom0 x. %s'%(8.160800+(d*0.300000))
jesstemp70 ='jessatom1 x. %s'%(6.888200+(d*0.300000))
jesstemp71 ='jessatom2 x. %s'%(6.403400+(d*0.300000))
jesstemp72 ='jessatom3 x. %s'%(10.746400+(d*0.300000))
jesstemp73 ='jessatom4 x. %s'%(9.312200+(d*0.300000))
jesstemp74 ='jessatom5 x. %s'%(8.494100+(d*0.300000))
jesstemp75 ='jessatom6 x. %s'%(4.817700+(d*0.300000))
jesstemp76 ='jessatom7 x. %s'%(5.706500+(d*0.300000))
jesstemp77 ='jessatom8 x. %s'%(5.302500+(d*0.300000))
jesstemp78 ='jessatom9 x. %s'%(2.464400+(d*0.300000))
jesstemp79 ='br. jessatom9'
jesstemp80 ='jessatom10 x. %s'%(1.535200+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(6.888200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(6.403400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(10.746400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(9.312200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.817700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(5.706500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(5.302500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.464400+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jfa_1apy-S49A-T183B-T201B-T234B-G235B', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
