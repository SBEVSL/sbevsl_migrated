'''
FUNC:Jfa_1q2o
PDB:1q2o
EC:1.14.13.39
PFAM:PF02898
RESI:cys,arg,trp,glu
LOCI:a-186,189,358,363;
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
jesstemp7 ='jessatom0 x. %s'%(2.787600+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.848300+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.787600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.848300+(d*0.300000)))
jesstemp10 ='n.  ne '
jesstemp11 ='r. arg'
jesstemp12 ='jessatom0 x. %s'%(4.363200+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(4.171300+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(5.120700+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.363200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.171300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.120700+(d*0.300000)))
jesstemp15 ='n.  nh1'
jesstemp16 ='n.  nh2'
jesstemp17 ='jessatom0 x. %s'%(6.221600+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(6.039800+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(7.241700+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(2.323000+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp11+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.221600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.039800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.241700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.323000+(d*0.300000)))
jesstemp22 ='n.  nh2'
jesstemp23 ='n.  nh1'
jesstemp24 ='jessatom0 x. %s'%(5.151000+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(5.544900+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(6.807400+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.333100+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.323000+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp22+')|('+jesstemp23+'))&('+jesstemp11+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.151000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.807400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.333100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(11.857400+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(11.433200+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(9.766700+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(14.594500+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(16.826600+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(16.291300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.857400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.433200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.766700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(14.594500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(16.826600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(16.291300+(d*0.300000)))
jesstemp36 ='n.  c  '
jesstemp37 ='jessatom0 x. %s'%(11.069600+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(10.827200+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(9.231400+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(14.079400+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(16.341800+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(15.604500+(d*0.300000))
jesstemp43 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(11.069600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(10.827200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.231400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(14.079400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(16.341800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(15.604500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
jesstemp45 ='n.  o  '
jesstemp46 ='jessatom0 x. %s'%(9.847500+(d*0.300000))
jesstemp47 ='jessatom1 x. %s'%(9.635400+(d*0.300000))
jesstemp48 ='jessatom2 x. %s'%(8.059800+(d*0.300000))
jesstemp49 ='jessatom3 x. %s'%(12.877500+(d*0.300000))
jesstemp50 ='jessatom4 x. %s'%(15.150000+(d*0.300000))
jesstemp51 ='jessatom5 x. %s'%(14.382400+(d*0.300000))
jesstemp52 ='jessatom6 x. %s'%(2.424000+(d*0.300000))
jesstemp53 ='br. jessatom6'
jesstemp54 ='jessatom7 x. %s'%(1.242300+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.847500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.059800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(12.877500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(15.150000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(14.382400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.424000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.242300+(d*0.300000)))
jesstemp55 ='n.  cd '
jesstemp56 ='r. glu'
jesstemp57 ='r. asp'
jesstemp58 ='jessatom0 x. %s'%(9.130400+(d*0.300000))
jesstemp59 ='jessatom1 x. %s'%(9.625300+(d*0.300000))
jesstemp60 ='jessatom2 x. %s'%(8.908200+(d*0.300000))
jesstemp61 ='jessatom3 x. %s'%(13.261300+(d*0.300000))
jesstemp62 ='jessatom4 x. %s'%(15.321700+(d*0.300000))
jesstemp63 ='jessatom5 x. %s'%(13.988500+(d*0.300000))
jesstemp64 ='jessatom6 x. %s'%(7.665900+(d*0.300000))
jesstemp65 ='jessatom7 x. %s'%(6.251900+(d*0.300000))
jesstemp66 ='jessatom8 x. %s'%(5.656000+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp55+')&('+jesstemp56+'))|(('+jesstemp55+')&('+jesstemp57+')))&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(9.625300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(8.908200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(13.261300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(15.321700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(13.988500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(6.251900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(5.656000+(d*0.300000)))
jesstemp67 ='n.  oe1'
jesstemp68 ='n.  oe2'
jesstemp69 ='n.  od1'
jesstemp70 ='n.  od2'
jesstemp71 ='jessatom0 x. %s'%(9.029400+(d*0.300000))
jesstemp72 ='jessatom1 x. %s'%(9.423300+(d*0.300000))
jesstemp73 ='jessatom2 x. %s'%(8.484000+(d*0.300000))
jesstemp74 ='jessatom3 x. %s'%(12.968400+(d*0.300000))
jesstemp75 ='jessatom4 x. %s'%(15.119700+(d*0.300000))
jesstemp76 ='jessatom5 x. %s'%(13.847100+(d*0.300000))
jesstemp77 ='jessatom6 x. %s'%(6.575100+(d*0.300000))
jesstemp78 ='jessatom7 x. %s'%(5.110600+(d*0.300000))
jesstemp79 ='jessatom8 x. %s'%(4.484400+(d*0.300000))
jesstemp80 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp81 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp67+')|('+jesstemp68+'))&('+jesstemp56+'))|((('+jesstemp69+')|('+jesstemp70+'))&('+jesstemp57+')))&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(9.029400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(9.423300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(8.484000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(12.968400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(15.119700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(13.847100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(5.110600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.484400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp82 ='n.  oe2'
jesstemp83 ='n.  oe1'
jesstemp84 ='n.  od2'
jesstemp85 ='n.  od1'
jesstemp86 ='jessatom0 x. %s'%(8.968800+(d*0.300000))
jesstemp87 ='jessatom1 x. %s'%(9.382900+(d*0.300000))
jesstemp88 ='jessatom2 x. %s'%(8.776900+(d*0.300000))
jesstemp89 ='jessatom3 x. %s'%(13.200700+(d*0.300000))
jesstemp90 ='jessatom4 x. %s'%(15.180300+(d*0.300000))
jesstemp91 ='jessatom5 x. %s'%(13.948100+(d*0.300000))
jesstemp92 ='jessatom6 x. %s'%(7.989100+(d*0.300000))
jesstemp93 ='jessatom7 x. %s'%(6.686200+(d*0.300000))
jesstemp94 ='jessatom8 x. %s'%(6.090300+(d*0.300000))
jesstemp95 ='br. jessatom9'
jesstemp96 ='jessatom10 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp82+')|('+jesstemp83+'))&('+jesstemp56+'))|((('+jesstemp84+')|('+jesstemp85+'))&('+jesstemp57+')))&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp80+')&('+jesstemp95+')&('+jesstemp96+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(8.968800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(9.382900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(8.776900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(13.200700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(15.180300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(13.948100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.989100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(6.686200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.090300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1q2o', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
