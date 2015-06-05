'''
FUNC:Jfa_1naw
PDB:1naw
EC:2.5.1.7
PFAM:PF00275
RESI:asn,cys,asp,arg
LOCI:a-23,115,305,397;
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
jesstemp7 ='jessatom0 x. %s'%(1.353400+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.272500+(d*0.300000)))
jesstemp10 ='n.  ca '
jesstemp11 ='r. cys'
jesstemp12 ='jessatom0 x. %s'%(26.371100+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(25.674200+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(26.431700+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(26.371100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(25.674200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(26.431700+(d*0.300000)))
jesstemp15 ='n.  cb '
jesstemp16 ='jessatom0 x. %s'%(27.259900+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(26.563000+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(27.270000+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.555400+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(27.259900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(26.563000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(27.270000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.555400+(d*0.300000)))
jesstemp21 ='n.  sg '
jesstemp22 ='jessatom0 x. %s'%(26.542800+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(25.886300+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(26.472100+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.858300+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.838200+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(26.542800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(25.886300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(26.472100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.858300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.838200+(d*0.300000)))
jesstemp28 ='r. asp'
jesstemp29 ='r. glu'
jesstemp30 ='jessatom0 x. %s'%(7.766900+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(8.494100+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(6.453900+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(26.502400+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(27.108400+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(25.967100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp28+'))|(('+jesstemp0+')&('+jesstemp29+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.766900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.453900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(26.502400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(27.108400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(25.967100+(d*0.300000)))
jesstemp36 ='n.  od2'
jesstemp37 ='n.  oe1'
jesstemp38 ='n.  oe2'
jesstemp39 ='jessatom0 x. %s'%(8.302200+(d*0.300000))
jesstemp40 ='jessatom1 x. %s'%(8.898100+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(7.029600+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(25.522700+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(26.088300+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(24.906600+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp36+'))&('+jesstemp28+'))|((('+jesstemp37+')|('+jesstemp38+'))&('+jesstemp29+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.898100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(25.522700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(26.088300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(24.906600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp47 ='n.  od2'
jesstemp48 ='n.  od1'
jesstemp49 ='n.  oe2'
jesstemp50 ='n.  oe1'
jesstemp51 ='jessatom0 x. %s'%(6.827600+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(7.635600+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(5.544900+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(26.492300+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(27.169000+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(26.088300+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp58 ='br. jessatom6'
jesstemp59 ='jessatom7 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp47+')|('+jesstemp48+'))&('+jesstemp28+'))|((('+jesstemp49+')|('+jesstemp50+'))&('+jesstemp29+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.827600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(26.492300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(27.169000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(26.088300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.242200+(d*0.300000)))
jesstemp60 ='n.  ne '
jesstemp61 ='r. arg'
jesstemp62 ='jessatom0 x. %s'%(13.867300+(d*0.300000))
jesstemp63 ='jessatom1 x. %s'%(12.887600+(d*0.300000))
jesstemp64 ='jessatom2 x. %s'%(13.917800+(d*0.300000))
jesstemp65 ='jessatom3 x. %s'%(23.977400+(d*0.300000))
jesstemp66 ='jessatom4 x. %s'%(24.320800+(d*0.300000))
jesstemp67 ='jessatom5 x. %s'%(23.543100+(d*0.300000))
jesstemp68 ='jessatom6 x. %s'%(16.341800+(d*0.300000))
jesstemp69 ='jessatom7 x. %s'%(15.867100+(d*0.300000))
jesstemp70 ='jessatom8 x. %s'%(16.483200+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(13.867300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(12.887600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(13.917800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(23.977400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(24.320800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(23.543100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(16.341800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(15.867100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(16.483200+(d*0.300000)))
jesstemp71 ='n.  nh1'
jesstemp72 ='n.  nh2'
jesstemp73 ='jessatom0 x. %s'%(13.624900+(d*0.300000))
jesstemp74 ='jessatom1 x. %s'%(12.635100+(d*0.300000))
jesstemp75 ='jessatom2 x. %s'%(13.635000+(d*0.300000))
jesstemp76 ='jessatom3 x. %s'%(21.684700+(d*0.300000))
jesstemp77 ='jessatom4 x. %s'%(22.007900+(d*0.300000))
jesstemp78 ='jessatom5 x. %s'%(21.210000+(d*0.300000))
jesstemp79 ='jessatom6 x. %s'%(15.685300+(d*0.300000))
jesstemp80 ='jessatom7 x. %s'%(15.079300+(d*0.300000))
jesstemp81 ='jessatom8 x. %s'%(15.846900+(d*0.300000))
jesstemp82 ='jessatom9 x. %s'%(2.373500+(d*0.300000))
jesstemp83 ='br. jessatom9'
cmd.select('jessatom10', '((('+jesstemp71+')|('+jesstemp72+'))&('+jesstemp61+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(13.624900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(12.635100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(13.635000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(21.684700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(22.007900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(21.210000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(15.685300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(15.079300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(15.846900+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(2.373500+(d*0.300000)))
jesstemp84 ='n.  nh2'
jesstemp85 ='n.  nh1'
jesstemp86 ='jessatom0 x. %s'%(15.614600+(d*0.300000))
jesstemp87 ='jessatom1 x. %s'%(14.594500+(d*0.300000))
jesstemp88 ='jessatom2 x. %s'%(15.695400+(d*0.300000))
jesstemp89 ='jessatom3 x. %s'%(22.674500+(d*0.300000))
jesstemp90 ='jessatom4 x. %s'%(22.937100+(d*0.300000))
jesstemp91 ='jessatom5 x. %s'%(22.199800+(d*0.300000))
jesstemp92 ='jessatom6 x. %s'%(17.917400+(d*0.300000))
jesstemp93 ='jessatom7 x. %s'%(17.331600+(d*0.300000))
jesstemp94 ='jessatom8 x. %s'%(18.089100+(d*0.300000))
jesstemp95 ='jessatom9 x. %s'%(2.312900+(d*0.300000))
jesstemp96 ='br. jessatom9'
jesstemp97 ='jessatom10 x. %s'%(2.363400+(d*0.300000))
cmd.select('jessatom11', '((('+jesstemp84+')|('+jesstemp85+'))&('+jesstemp61+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(15.614600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(14.594500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(15.695400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(22.674500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(22.937100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(22.199800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(17.917400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(17.331600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(18.089100+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.363400+(d*0.300000)))
cmd.select('Jfa_1naw', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
