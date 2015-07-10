'''
FUNC:Jfa_1b0p-T31A-E64A-R14A-N996A
PDB:1b0p
EC:1.2.7.1
PFAM:PF01558,PF02775,PF01855,PF00037,PF13237,PF12838,PF12837,PF10371
RESI:thr,glu,arg,asn
LOCI:a-31,64,14,996;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. thr'
jesstemp2 ='r. ser'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.575600+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.575600+(d*0.300000)))
jesstemp6 ='n.  og1'
jesstemp7 ='jessatom0 x. %s'%(2.454300+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.444300+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.444300+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. glu'
jesstemp12 ='r. asp'
jesstemp13 ='jessatom0 x. %s'%(9.898000+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(10.867600+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(10.887800+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.898000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.867600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(10.887800+(d*0.300000)))
jesstemp16 ='n.  oe1'
jesstemp17 ='n.  oe2'
jesstemp18 ='n.  od1'
jesstemp19 ='n.  od2'
jesstemp20 ='jessatom0 x. %s'%(8.776900+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(9.817200+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(9.867700+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.776900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.817200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.867700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp25 ='n.  oe2'
jesstemp26 ='n.  oe1'
jesstemp27 ='n.  od2'
jesstemp28 ='n.  od1'
jesstemp29 ='jessatom0 x. %s'%(10.291900+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(11.130200+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(11.029200+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.291900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.130200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.029200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.201800+(d*0.300000)))
jesstemp35 ='n.  ne '
jesstemp36 ='r. arg'
jesstemp37 ='jessatom0 x. %s'%(5.959000+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(5.938800+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(7.019500+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(10.190900+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(9.534400+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(10.554500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.019500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.190900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.534400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(10.554500+(d*0.300000)))
jesstemp43 ='n.  nh1'
jesstemp44 ='n.  nh2'
jesstemp45 ='jessatom0 x. %s'%(4.262200+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(4.171300+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(5.009600+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(9.100100+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(8.332500+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(9.342500+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(2.323000+(d*0.300000))
jesstemp52 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp43+')|('+jesstemp44+'))&('+jesstemp36+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.262200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.171300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.009600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.100100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.342500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.323000+(d*0.300000)))
jesstemp53 ='n.  nh2'
jesstemp54 ='n.  nh1'
jesstemp55 ='jessatom0 x. %s'%(6.524600+(d*0.300000))
jesstemp56 ='jessatom1 x. %s'%(6.181200+(d*0.300000))
jesstemp57 ='jessatom2 x. %s'%(6.878100+(d*0.300000))
jesstemp58 ='jessatom3 x. %s'%(9.877800+(d*0.300000))
jesstemp59 ='jessatom4 x. %s'%(9.362700+(d*0.300000))
jesstemp60 ='jessatom5 x. %s'%(9.968700+(d*0.300000))
jesstemp61 ='jessatom6 x. %s'%(2.302800+(d*0.300000))
jesstemp62 ='br. jessatom6'
jesstemp63 ='jessatom7 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp53+')|('+jesstemp54+'))&('+jesstemp36+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.524600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.181200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.878100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.877800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.362700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.968700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.302800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.312900+(d*0.300000)))
jesstemp64 ='n.  cg '
jesstemp65 ='r. asn'
jesstemp66 ='r. gln'
jesstemp67 ='jessatom0 x. %s'%(8.645600+(d*0.300000))
jesstemp68 ='jessatom1 x. %s'%(7.635600+(d*0.300000))
jesstemp69 ='jessatom2 x. %s'%(6.433700+(d*0.300000))
jesstemp70 ='jessatom3 x. %s'%(12.705800+(d*0.300000))
jesstemp71 ='jessatom4 x. %s'%(12.160400+(d*0.300000))
jesstemp72 ='jessatom5 x. %s'%(12.190700+(d*0.300000))
jesstemp73 ='jessatom6 x. %s'%(10.948400+(d*0.300000))
jesstemp74 ='jessatom7 x. %s'%(8.877900+(d*0.300000))
jesstemp75 ='jessatom8 x. %s'%(9.393000+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp64+')&('+jesstemp65+'))|(('+jesstemp64+')&('+jesstemp66+')))&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(8.645600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(6.433700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(12.705800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(12.160400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(12.190700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(10.948400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(8.877900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(9.393000+(d*0.300000)))
jesstemp76 ='jessatom0 x. %s'%(8.706200+(d*0.300000))
jesstemp77 ='jessatom1 x. %s'%(7.888100+(d*0.300000))
jesstemp78 ='jessatom2 x. %s'%(6.655900+(d*0.300000))
jesstemp79 ='jessatom3 x. %s'%(11.837200+(d*0.300000))
jesstemp80 ='jessatom4 x. %s'%(11.342300+(d*0.300000))
jesstemp81 ='jessatom5 x. %s'%(11.261500+(d*0.300000))
jesstemp82 ='jessatom6 x. %s'%(11.099900+(d*0.300000))
jesstemp83 ='jessatom7 x. %s'%(8.948600+(d*0.300000))
jesstemp84 ='jessatom8 x. %s'%(9.524300+(d*0.300000))
jesstemp85 ='jessatom9 x. %s'%(1.242300+(d*0.300000))
jesstemp86 ='br. jessatom9'
cmd.select('jessatom10', '(((('+jesstemp18+')&('+jesstemp65+'))|(('+jesstemp18+')&('+jesstemp66+')))&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(7.888100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(6.655900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(11.837200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(11.342300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(11.261500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(11.099900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(8.948600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(9.524300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.242300+(d*0.300000)))
jesstemp87 ='n.  nd2'
jesstemp88 ='jessatom0 x. %s'%(7.888100+(d*0.300000))
jesstemp89 ='jessatom1 x. %s'%(6.756900+(d*0.300000))
jesstemp90 ='jessatom2 x. %s'%(5.686300+(d*0.300000))
jesstemp91 ='jessatom3 x. %s'%(12.544200+(d*0.300000))
jesstemp92 ='jessatom4 x. %s'%(11.958400+(d*0.300000))
jesstemp93 ='jessatom5 x. %s'%(12.099800+(d*0.300000))
jesstemp94 ='jessatom6 x. %s'%(9.807100+(d*0.300000))
jesstemp95 ='jessatom7 x. %s'%(7.827500+(d*0.300000))
jesstemp96 ='jessatom8 x. %s'%(8.261800+(d*0.300000))
jesstemp97 ='jessatom9 x. %s'%(1.333200+(d*0.300000))
jesstemp98 ='br. jessatom9'
jesstemp99 ='jessatom10 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom11', '(((('+jesstemp87+')&('+jesstemp65+'))|(('+jesstemp87+')&('+jesstemp66+')))&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+')&('+jesstemp98+')&('+jesstemp99+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(7.888100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(6.756900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(12.544200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(11.958400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(12.099800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(9.807100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.827500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(8.261800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.262400+(d*0.300000)))
cmd.select('Jfa_1b0p-T31A-E64A-R14A-N996A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
