'''
FUNC:Jfa_1gk2-A142A-S143A-G144A-Y280A-E414A
PDB:1gk2
EC:4.3.1.3
PFAM:PF00221
RESI:ala,ser,gly,tyr,glu
LOCI:a-142,143,144,280,414;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ala'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  c  '
jesstemp3 ='r. ala'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='n.  cb '
jesstemp7 ='jessatom0 x. %s'%(1.525100+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.535100+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.525100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.535100+(d*0.300000)))
jesstemp10 ='r. ser'
jesstemp11 ='r. thr'
jesstemp12 ='jessatom0 x. %s'%(3.848100+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(2.514900+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.848000+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp10+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(3.848100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(2.514900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.848000+(d*0.300000)))
jesstemp15 ='jessatom0 x. %s'%(4.534900+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(3.009800+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(5.312600+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(1.535200+(d*0.300000))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp6+')&('+jesstemp10+'))|(('+jesstemp6+')&('+jesstemp11+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.534900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.009800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.535200+(d*0.300000)))
jesstemp20 ='n.  og '
jesstemp21 ='jessatom0 x. %s'%(5.928700+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(4.413700+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(6.726600+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(2.444200+(d*0.300000))
jesstemp25 ='br. jessatom3'
jesstemp26 ='jessatom4 x. %s'%(1.434200+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp20+')&('+jesstemp10+'))|(('+jesstemp20+')&('+jesstemp11+')))&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.928700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.413700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.726600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.434200+(d*0.300000)))
jesstemp27 ='n.  n  '
jesstemp28 ='r. gly'
jesstemp29 ='jessatom0 x. %s'%(3.918800+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(5.342900+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(2.413900+(d*0.300000))
jesstemp32 ='jessatom4 x. %s'%(3.191600+(d*0.300000))
jesstemp33 ='jessatom5 x. %s'%(3.939000+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp16+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(3.918800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(3.009800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.342900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(2.413900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.191600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.939000+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(4.716700+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(4.151100+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(6.211500+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(3.817800+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(4.595500+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(5.191400+(d*0.300000))
jesstemp40 ='jessatom6 x. %s'%(1.444300+(d*0.300000))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp0+')&('+jesstemp28+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.716700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.151100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.211500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.817800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.191400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.444300+(d*0.300000)))
jesstemp42 ='jessatom0 x. %s'%(4.989400+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(4.565200+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(6.403400+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(4.827800+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(5.282300+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(5.969100+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(2.474500+(d*0.300000))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(1.535200+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp2+')&('+jesstemp28+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.565200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.403400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.827800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.282300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.969100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.474500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.535200+(d*0.300000)))
jesstemp51 ='n.  ce1'
jesstemp52 ='r. tyr'
jesstemp53 ='jessatom0 x. %s'%(44.581400+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(46.106500+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(44.248100+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(48.126500+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(49.075900+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(50.419200+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(47.086200+(d*0.300000))
jesstemp60 ='jessatom7 x. %s'%(46.540800+(d*0.300000))
jesstemp61 ='jessatom8 x. %s'%(46.076200+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(44.581400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(46.106500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(44.248100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(48.126500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(49.075900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(50.419200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(47.086200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(46.540800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(46.076200+(d*0.300000)))
jesstemp62 ='n.  cz '
jesstemp63 ='jessatom0 x. %s'%(44.096600+(d*0.300000))
jesstemp64 ='jessatom1 x. %s'%(45.621700+(d*0.300000))
jesstemp65 ='jessatom2 x. %s'%(43.712800+(d*0.300000))
jesstemp66 ='jessatom3 x. %s'%(47.672000+(d*0.300000))
jesstemp67 ='jessatom4 x. %s'%(48.611300+(d*0.300000))
jesstemp68 ='jessatom5 x. %s'%(49.954600+(d*0.300000))
jesstemp69 ='jessatom6 x. %s'%(46.692300+(d*0.300000))
jesstemp70 ='jessatom7 x. %s'%(46.187300+(d*0.300000))
jesstemp71 ='jessatom8 x. %s'%(45.722700+(d*0.300000))
jesstemp72 ='jessatom9 x. %s'%(1.393800+(d*0.300000))
jesstemp73 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp62+')&('+jesstemp52+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(44.096600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(45.621700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(43.712800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(47.672000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(48.611300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(49.954600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(46.692300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(46.187300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(45.722700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.393800+(d*0.300000)))
jesstemp74 ='n.  oh '
jesstemp75 ='jessatom0 x. %s'%(44.884400+(d*0.300000))
jesstemp76 ='jessatom1 x. %s'%(46.409500+(d*0.300000))
jesstemp77 ='jessatom2 x. %s'%(44.470300+(d*0.300000))
jesstemp78 ='jessatom3 x. %s'%(48.459800+(d*0.300000))
jesstemp79 ='jessatom4 x. %s'%(49.399100+(d*0.300000))
jesstemp80 ='jessatom5 x. %s'%(50.752500+(d*0.300000))
jesstemp81 ='jessatom6 x. %s'%(47.530600+(d*0.300000))
jesstemp82 ='jessatom7 x. %s'%(47.045800+(d*0.300000))
jesstemp83 ='jessatom8 x. %s'%(46.621600+(d*0.300000))
jesstemp84 ='jessatom9 x. %s'%(2.393700+(d*0.300000))
jesstemp85 ='br. jessatom9'
jesstemp86 ='jessatom10 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp74+')&('+jesstemp52+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(44.884400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(46.409500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(44.470300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(48.459800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(49.399100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(50.752500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(47.530600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(47.045800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(46.621600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.393700+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.393800+(d*0.300000)))
jesstemp87 ='n.  cd '
jesstemp88 ='r. glu'
jesstemp89 ='r. asp'
jesstemp90 ='jessatom0 x. %s'%(5.837800+(d*0.300000))
jesstemp91 ='jessatom1 x. %s'%(4.696500+(d*0.300000))
jesstemp92 ='jessatom2 x. %s'%(5.656000+(d*0.300000))
jesstemp93 ='jessatom3 x. %s'%(4.979300+(d*0.300000))
jesstemp94 ='jessatom4 x. %s'%(3.767300+(d*0.300000))
jesstemp95 ='jessatom5 x. %s'%(4.383400+(d*0.300000))
jesstemp96 ='jessatom6 x. %s'%(6.464000+(d*0.300000))
jesstemp97 ='jessatom7 x. %s'%(7.777000+(d*0.300000))
jesstemp98 ='jessatom8 x. %s'%(7.938600+(d*0.300000))
jesstemp99 ='jessatom9 x. %s'%(49.540500+(d*0.300000))
jesstemp100 ='jessatom10 x. %s'%(48.995100+(d*0.300000))
jesstemp101 ='jessatom11 x. %s'%(49.752600+(d*0.300000))
cmd.select('jessatom12', '(((('+jesstemp87+')&('+jesstemp88+'))|(('+jesstemp87+')&('+jesstemp89+')))&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+')&('+jesstemp98+')&('+jesstemp99+')&('+jesstemp100+')&('+jesstemp101+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom12 x. %s)'%(5.837800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom12 x. %s)'%(4.696500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom12 x. %s)'%(5.656000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom12 x. %s)'%(4.979300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom12 x. %s)'%(3.767300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom12 x. %s)'%(4.383400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom12 x. %s)'%(6.464000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom12 x. %s)'%(7.777000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom12 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom12 x. %s)'%(49.540500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom12 x. %s)'%(48.995100+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom12 x. %s)'%(49.752600+(d*0.300000)))
jesstemp102 ='n.  oe1'
jesstemp103 ='n.  oe2'
jesstemp104 ='n.  od1'
jesstemp105 ='n.  od2'
jesstemp106 ='jessatom0 x. %s'%(5.070200+(d*0.300000))
jesstemp107 ='jessatom1 x. %s'%(4.120800+(d*0.300000))
jesstemp108 ='jessatom2 x. %s'%(4.807600+(d*0.300000))
jesstemp109 ='jessatom3 x. %s'%(5.029800+(d*0.300000))
jesstemp110 ='jessatom4 x. %s'%(3.999600+(d*0.300000))
jesstemp111 ='jessatom5 x. %s'%(4.928800+(d*0.300000))
jesstemp112 ='jessatom6 x. %s'%(6.181200+(d*0.300000))
jesstemp113 ='jessatom7 x. %s'%(7.403300+(d*0.300000))
jesstemp114 ='jessatom8 x. %s'%(7.413400+(d*0.300000))
jesstemp115 ='jessatom9 x. %s'%(48.399200+(d*0.300000))
jesstemp116 ='jessatom10 x. %s'%(47.853800+(d*0.300000))
jesstemp117 ='jessatom11 x. %s'%(48.611300+(d*0.300000))
jesstemp118 ='jessatom12 x. %s'%(1.262500+(d*0.300000))
jesstemp119 ='br. jessatom12'
cmd.select('jessatom13', '((((('+jesstemp102+')|('+jesstemp103+'))&('+jesstemp88+'))|((('+jesstemp104+')|('+jesstemp105+'))&('+jesstemp89+')))&('+jesstemp106+')&('+jesstemp107+')&('+jesstemp108+')&('+jesstemp109+')&('+jesstemp110+')&('+jesstemp111+')&('+jesstemp112+')&('+jesstemp113+')&('+jesstemp114+')&('+jesstemp115+')&('+jesstemp116+')&('+jesstemp117+')&('+jesstemp118+')&('+jesstemp119+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom13 x. %s)'%(5.070200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom13 x. %s)'%(4.120800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom13 x. %s)'%(4.807600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom13 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom13 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom13 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom13 x. %s)'%(6.181200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom13 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom13 x. %s)'%(7.413400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom13 x. %s)'%(48.399200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom13 x. %s)'%(47.853800+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom13 x. %s)'%(48.611300+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom13 x. %s)'%(1.262500+(d*0.300000)))
jesstemp120 ='n.  oe2'
jesstemp121 ='n.  oe1'
jesstemp122 ='n.  od2'
jesstemp123 ='n.  od1'
jesstemp124 ='jessatom0 x. %s'%(6.171100+(d*0.300000))
jesstemp125 ='jessatom1 x. %s'%(4.817700+(d*0.300000))
jesstemp126 ='jessatom2 x. %s'%(6.282200+(d*0.300000))
jesstemp127 ='jessatom3 x. %s'%(4.524800+(d*0.300000))
jesstemp128 ='jessatom4 x. %s'%(3.100700+(d*0.300000))
jesstemp129 ='jessatom5 x. %s'%(3.403700+(d*0.300000))
jesstemp130 ='jessatom6 x. %s'%(5.989300+(d*0.300000))
jesstemp131 ='jessatom7 x. %s'%(7.292200+(d*0.300000))
jesstemp132 ='jessatom8 x. %s'%(7.534600+(d*0.300000))
jesstemp133 ='jessatom9 x. %s'%(50.298000+(d*0.300000))
jesstemp134 ='jessatom10 x. %s'%(49.772800+(d*0.300000))
jesstemp135 ='jessatom11 x. %s'%(50.550500+(d*0.300000))
jesstemp136 ='br. jessatom12'
jesstemp137 ='jessatom13 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom14', '((((('+jesstemp120+')|('+jesstemp121+'))&('+jesstemp88+'))|((('+jesstemp122+')|('+jesstemp123+'))&('+jesstemp89+')))&('+jesstemp124+')&('+jesstemp125+')&('+jesstemp126+')&('+jesstemp127+')&('+jesstemp128+')&('+jesstemp129+')&('+jesstemp130+')&('+jesstemp131+')&('+jesstemp132+')&('+jesstemp133+')&('+jesstemp134+')&('+jesstemp135+')&('+jesstemp118+')&('+jesstemp136+')&('+jesstemp137+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom14 x. %s)'%(6.171100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom14 x. %s)'%(4.817700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom14 x. %s)'%(6.282200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom14 x. %s)'%(4.524800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom14 x. %s)'%(3.100700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom14 x. %s)'%(3.403700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom14 x. %s)'%(5.989300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom14 x. %s)'%(7.292200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom14 x. %s)'%(7.534600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom14 x. %s)'%(50.298000+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom14 x. %s)'%(49.772800+(d*0.300000)))
cmd.select('jessatom11', 'jessatom11 & (jessatom14 x. %s)'%(50.550500+(d*0.300000)))
cmd.select('jessatom12', 'jessatom12 & (jessatom14 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom13', 'jessatom13 & (jessatom14 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('Jfa_1gk2-A142A-S143A-G144A-Y280A-E414A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
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
cmd.delete('jessatom12')
cmd.delete('jessatom13')
cmd.delete('jessatom14')
