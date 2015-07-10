'''
FUNC:Jfa_1qnt-N137A-C145A-H146A-E172A
PDB:1qnt
EC:2.1.1.63
PFAM:PF01035,PF02870
RESI:asn,cys,his,glu
LOCI:a-137,145,146,172;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='jessatom0 x. %s'%(1.242300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.242300+(d*0.300000)))
jesstemp6 ='n.  nd2'
jesstemp7 ='jessatom0 x. %s'%(1.333200+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.262400+(d*0.300000)))
jesstemp10 ='n.  ca '
jesstemp11 ='r. cys'
jesstemp12 ='jessatom0 x. %s'%(5.868100+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(6.857900+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.837900+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.868100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.837900+(d*0.300000)))
jesstemp15 ='n.  cb '
jesstemp16 ='jessatom0 x. %s'%(4.858100+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(5.979200+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(3.969300+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.555400+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.969300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.555400+(d*0.300000)))
jesstemp21 ='n.  sg '
jesstemp22 ='jessatom0 x. %s'%(4.393500+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(5.544900+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(3.353200+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.858300+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.818000+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.393500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.353200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.858300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.818000+(d*0.300000)))
jesstemp28 ='r. his'
jesstemp29 ='jessatom0 x. %s'%(9.524300+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(10.362600+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(8.201200+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(5.231800+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(6.181200+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(5.898400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.524300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.362600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.181200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.898400+(d*0.300000)))
jesstemp35 ='n.  nd1'
jesstemp36 ='jessatom0 x. %s'%(8.514300+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(9.261700+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(7.181100+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(4.797500+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(5.706500+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(5.312600+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.393800+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp35+')&('+jesstemp28+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.514300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.261700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.181100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.797500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.706500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.393800+(d*0.300000)))
jesstemp44 ='n.  ne2'
jesstemp45 ='jessatom0 x. %s'%(10.463600+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(11.110000+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(9.130400+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(6.595300+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(7.706300+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(7.463900+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(2.222000+(d*0.300000))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp44+')&('+jesstemp28+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(10.463600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(11.110000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.595300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.706300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.161400+(d*0.300000)))
jesstemp54 ='n.  cd '
jesstemp55 ='r. glu'
jesstemp56 ='r. asp'
jesstemp57 ='jessatom0 x. %s'%(13.978400+(d*0.300000))
jesstemp58 ='jessatom1 x. %s'%(14.513700+(d*0.300000))
jesstemp59 ='jessatom2 x. %s'%(12.675500+(d*0.300000))
jesstemp60 ='jessatom3 x. %s'%(9.958600+(d*0.300000))
jesstemp61 ='jessatom4 x. %s'%(11.241300+(d*0.300000))
jesstemp62 ='jessatom5 x. %s'%(11.180700+(d*0.300000))
jesstemp63 ='jessatom6 x. %s'%(5.666100+(d*0.300000))
jesstemp64 ='jessatom7 x. %s'%(5.918600+(d*0.300000))
jesstemp65 ='jessatom8 x. %s'%(3.767300+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp54+')&('+jesstemp55+'))|(('+jesstemp54+')&('+jesstemp56+')))&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(13.978400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(14.513700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(12.675500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(9.958600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(11.241300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(11.180700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(5.666100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(3.767300+(d*0.300000)))
jesstemp66 ='n.  oe1'
jesstemp67 ='n.  oe2'
jesstemp68 ='n.  od2'
jesstemp69 ='jessatom0 x. %s'%(14.049100+(d*0.300000))
jesstemp70 ='jessatom1 x. %s'%(14.604600+(d*0.300000))
jesstemp71 ='jessatom2 x. %s'%(12.766400+(d*0.300000))
jesstemp72 ='jessatom3 x. %s'%(9.726300+(d*0.300000))
jesstemp73 ='jessatom4 x. %s'%(11.099900+(d*0.300000))
jesstemp74 ='jessatom5 x. %s'%(11.251400+(d*0.300000))
jesstemp75 ='jessatom6 x. %s'%(5.868100+(d*0.300000))
jesstemp76 ='jessatom7 x. %s'%(6.161000+(d*0.300000))
jesstemp77 ='jessatom8 x. %s'%(4.110700+(d*0.300000))
jesstemp78 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp79 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp66+')|('+jesstemp67+'))&('+jesstemp55+'))|((('+jesstemp3+')|('+jesstemp68+'))&('+jesstemp56+')))&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(14.049100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(14.604600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(12.766400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(9.726300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(11.099900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(11.251400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(5.868100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.161000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.110700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp80 ='n.  oe2'
jesstemp81 ='n.  oe1'
jesstemp82 ='n.  od2'
jesstemp83 ='n.  od1'
jesstemp84 ='jessatom0 x. %s'%(12.948200+(d*0.300000))
jesstemp85 ='jessatom1 x. %s'%(13.463300+(d*0.300000))
jesstemp86 ='jessatom2 x. %s'%(11.635200+(d*0.300000))
jesstemp87 ='jessatom3 x. %s'%(9.241500+(d*0.300000))
jesstemp88 ='jessatom4 x. %s'%(10.443400+(d*0.300000))
jesstemp89 ='jessatom5 x. %s'%(10.251500+(d*0.300000))
jesstemp90 ='jessatom6 x. %s'%(4.898500+(d*0.300000))
jesstemp91 ='jessatom7 x. %s'%(4.969200+(d*0.300000))
jesstemp92 ='jessatom8 x. %s'%(2.817900+(d*0.300000))
jesstemp93 ='br. jessatom9'
jesstemp94 ='jessatom10 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp80+')|('+jesstemp81+'))&('+jesstemp55+'))|((('+jesstemp82+')|('+jesstemp83+'))&('+jesstemp56+')))&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp78+')&('+jesstemp93+')&('+jesstemp94+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(12.948200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(13.463300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(11.635200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(10.443400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(10.251500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.898500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(4.969200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(2.817900+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1qnt-N137A-C145A-H146A-E172A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
