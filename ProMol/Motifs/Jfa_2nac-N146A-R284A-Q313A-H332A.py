'''
FUNC:Jfa_2nac-N146A-R284A-Q313A-H332A
PDB:2nac
EC:1.2.1.2
PFAM:PF02826,PF00389
RESI:asn,arg,gln,his
LOCI:a-146,284,313,332;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='jessatom0 x. %s'%(1.232200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.232200+(d*0.300000)))
jesstemp6 ='n.  nd2'
jesstemp7 ='jessatom0 x. %s'%(1.292800+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.252300+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.292800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.252300+(d*0.300000)))
jesstemp10 ='n.  ne '
jesstemp11 ='r. arg'
jesstemp12 ='jessatom0 x. %s'%(11.655400+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(11.150400+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(11.271600+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.655400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(11.150400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(11.271600+(d*0.300000)))
jesstemp15 ='n.  nh1'
jesstemp16 ='n.  nh2'
jesstemp17 ='jessatom0 x. %s'%(9.605100+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(9.180900+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(9.241500+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(2.343200+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp11+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.605100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.180900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.343200+(d*0.300000)))
jesstemp22 ='n.  nh2'
jesstemp23 ='n.  nh1'
jesstemp24 ='jessatom0 x. %s'%(9.766700+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(9.281900+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(9.322300+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.403800+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.292700+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp22+')|('+jesstemp23+'))&('+jesstemp11+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.766700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.281900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.322300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.403800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.292700+(d*0.300000)))
jesstemp30 ='n.  cd '
jesstemp31 ='jessatom0 x. %s'%(13.806700+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(13.938000+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(13.029000+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(7.403300+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(6.958900+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(8.170900+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp30+')&('+jesstemp2+'))|(('+jesstemp30+')&('+jesstemp1+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(13.806700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(13.938000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(13.029000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.958900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.170900+(d*0.300000)))
jesstemp37 ='n.  oe1'
jesstemp38 ='jessatom0 x. %s'%(13.554200+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(13.624900+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(12.877500+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(7.039700+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(6.484200+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(7.989100+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp37+')&('+jesstemp2+'))|(('+jesstemp37+')&('+jesstemp1+')))&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(13.554200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(13.624900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(12.877500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.484200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.989100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp46 ='n.  ne2'
jesstemp47 ='jessatom0 x. %s'%(12.938100+(d*0.300000))
jesstemp48 ='jessatom1 x. %s'%(13.140100+(d*0.300000))
jesstemp49 ='jessatom2 x. %s'%(12.079600+(d*0.300000))
jesstemp50 ='jessatom3 x. %s'%(7.373000+(d*0.300000))
jesstemp51 ='jessatom4 x. %s'%(6.726600+(d*0.300000))
jesstemp52 ='jessatom5 x. %s'%(7.746700+(d*0.300000))
jesstemp53 ='jessatom6 x. %s'%(1.353400+(d*0.300000))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(2.282600+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp46+')&('+jesstemp2+'))|(('+jesstemp46+')&('+jesstemp1+')))&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(12.938100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(13.140100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(12.079600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.373000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.726600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.746700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.282600+(d*0.300000)))
jesstemp56 ='r. his'
jesstemp57 ='jessatom0 x. %s'%(10.079800+(d*0.300000))
jesstemp58 ='jessatom1 x. %s'%(10.382800+(d*0.300000))
jesstemp59 ='jessatom2 x. %s'%(9.312200+(d*0.300000))
jesstemp60 ='jessatom3 x. %s'%(7.837600+(d*0.300000))
jesstemp61 ='jessatom4 x. %s'%(6.181200+(d*0.300000))
jesstemp62 ='jessatom5 x. %s'%(7.625500+(d*0.300000))
jesstemp63 ='jessatom6 x. %s'%(4.211700+(d*0.300000))
jesstemp64 ='jessatom7 x. %s'%(4.080400+(d*0.300000))
jesstemp65 ='jessatom8 x. %s'%(3.535000+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp0+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(10.079800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(10.382800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(9.312200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(7.837600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(6.181200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.625500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(4.211700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.080400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(3.535000+(d*0.300000)))
jesstemp66 ='n.  nd1'
jesstemp67 ='jessatom0 x. %s'%(10.069700+(d*0.300000))
jesstemp68 ='jessatom1 x. %s'%(10.322200+(d*0.300000))
jesstemp69 ='jessatom3 x. %s'%(6.938700+(d*0.300000))
jesstemp70 ='jessatom4 x. %s'%(5.454000+(d*0.300000))
jesstemp71 ='jessatom5 x. %s'%(6.605400+(d*0.300000))
jesstemp72 ='jessatom6 x. %s'%(3.848100+(d*0.300000))
jesstemp73 ='jessatom7 x. %s'%(3.959200+(d*0.300000))
jesstemp74 ='jessatom8 x. %s'%(2.908800+(d*0.300000))
jesstemp75 ='jessatom9 x. %s'%(1.424100+(d*0.300000))
jesstemp76 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp66+')&('+jesstemp56+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp19+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(10.069700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(10.322200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(6.938700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(5.454000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(6.605400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(3.848100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(3.959200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(2.908800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.424100+(d*0.300000)))
jesstemp77 ='jessatom0 x. %s'%(8.403200+(d*0.300000))
jesstemp78 ='jessatom1 x. %s'%(8.534500+(d*0.300000))
jesstemp79 ='jessatom2 x. %s'%(7.756800+(d*0.300000))
jesstemp80 ='jessatom3 x. %s'%(6.524600+(d*0.300000))
jesstemp81 ='jessatom4 x. %s'%(4.504600+(d*0.300000))
jesstemp82 ='jessatom5 x. %s'%(5.999400+(d*0.300000))
jesstemp83 ='jessatom6 x. %s'%(5.514600+(d*0.300000))
jesstemp84 ='jessatom7 x. %s'%(5.171200+(d*0.300000))
jesstemp85 ='jessatom8 x. %s'%(4.888400+(d*0.300000))
jesstemp86 ='jessatom9 x. %s'%(2.191700+(d*0.300000))
jesstemp87 ='br. jessatom9'
jesstemp88 ='jessatom10 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp46+')&('+jesstemp56+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(8.403200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(8.534500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(7.756800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(6.524600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(4.504600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(5.999400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(5.514600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(4.888400+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_2nac-N146A-R284A-Q313A-H332A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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