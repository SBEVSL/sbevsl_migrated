'''
FUNC:Jfa_1qq5-D8A-T12A-R39A-N115A-K147A-S171A-N173A-F175A-D176A
PDB:1qq5
EC:3.8.1.2
PFAM:PF00702,PF13419
RESI:asp,thr,arg,asn,lys,ser,asn,phe,asp
LOCI:a-8,12,39,115,147,171,173,175,176;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp15 ='n.  ne '
jesstemp16 ='r. arg'
jesstemp17 ='jessatom0 x. %s'%(8.585000+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(8.403200+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(7.756800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.585000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.403200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.756800+(d*0.300000)))
jesstemp20 ='n.  nh1'
jesstemp21 ='n.  nh2'
jesstemp22 ='jessatom0 x. %s'%(7.665900+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(7.201300+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(7.120500+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.323000+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp16+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.201300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.120500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.323000+(d*0.300000)))
jesstemp27 ='n.  nh2'
jesstemp28 ='n.  nh1'
jesstemp29 ='jessatom0 x. %s'%(6.342800+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(6.140800+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(5.575200+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.323000+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp16+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp25+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.342800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.575200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
jesstemp34 ='n.  ca '
jesstemp35 ='r. ser'
jesstemp36 ='r. thr'
jesstemp37 ='jessatom0 x. %s'%(6.322600+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(5.332800+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(7.352800+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(11.574600+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(9.564700+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(9.746500+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp34+')&('+jesstemp35+'))|(('+jesstemp34+')&('+jesstemp36+')))&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.322600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.332800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.352800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.574600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.564700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.746500+(d*0.300000)))
jesstemp43 ='n.  cb '
jesstemp44 ='jessatom0 x. %s'%(6.474100+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(5.625700+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(7.362900+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(11.301900+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(9.281900+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(9.615200+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp43+')&('+jesstemp35+'))|(('+jesstemp43+')&('+jesstemp36+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.474100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.362900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(11.301900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.281900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.615200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
jesstemp52 ='n.  og '
jesstemp53 ='jessatom0 x. %s'%(6.635700+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(5.726700+(d*0.300000))
jesstemp55 ='jessatom3 x. %s'%(10.271700+(d*0.300000))
jesstemp56 ='jessatom4 x. %s'%(8.160800+(d*0.300000))
jesstemp57 ='jessatom5 x. %s'%(8.746600+(d*0.300000))
jesstemp58 ='jessatom6 x. %s'%(2.454300+(d*0.300000))
jesstemp59 ='br. jessatom6'
jesstemp60 ='jessatom7 x. %s'%(1.434200+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp52+')&('+jesstemp35+'))|(('+jesstemp52+')&('+jesstemp36+')))&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp39+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.352800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(10.271700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.746600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.434200+(d*0.300000)))
jesstemp61 ='jessatom0 x. %s'%(4.343000+(d*0.300000))
jesstemp62 ='jessatom1 x. %s'%(4.141000+(d*0.300000))
jesstemp63 ='jessatom2 x. %s'%(4.989400+(d*0.300000))
jesstemp64 ='jessatom3 x. %s'%(10.584800+(d*0.300000))
jesstemp65 ='jessatom4 x. %s'%(9.776800+(d*0.300000))
jesstemp66 ='jessatom5 x. %s'%(8.322400+(d*0.300000))
jesstemp67 ='jessatom6 x. %s'%(7.716400+(d*0.300000))
jesstemp68 ='jessatom7 x. %s'%(8.655700+(d*0.300000))
jesstemp69 ='jessatom8 x. %s'%(8.999100+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(4.343000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(4.141000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(10.584800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.776800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(8.322400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(7.716400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(8.655700+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(8.999100+(d*0.300000)))
jesstemp70 ='jessatom0 x. %s'%(5.292400+(d*0.300000))
jesstemp71 ='jessatom1 x. %s'%(4.898500+(d*0.300000))
jesstemp72 ='jessatom2 x. %s'%(6.080200+(d*0.300000))
jesstemp73 ='jessatom3 x. %s'%(11.443300+(d*0.300000))
jesstemp74 ='jessatom4 x. %s'%(10.493900+(d*0.300000))
jesstemp75 ='jessatom5 x. %s'%(9.211200+(d*0.300000))
jesstemp76 ='jessatom6 x. %s'%(7.575000+(d*0.300000))
jesstemp77 ='jessatom7 x. %s'%(8.696100+(d*0.300000))
jesstemp78 ='jessatom8 x. %s'%(9.120300+(d*0.300000))
jesstemp79 ='jessatom9 x. %s'%(1.272600+(d*0.300000))
jesstemp80 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(5.292400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(4.898500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(6.080200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(11.443300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(10.493900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(9.211200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(7.575000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(8.696100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(9.120300+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.272600+(d*0.300000)))
jesstemp81 ='jessatom0 x. %s'%(3.252200+(d*0.300000))
jesstemp82 ='jessatom1 x. %s'%(3.221900+(d*0.300000))
jesstemp83 ='jessatom2 x. %s'%(4.019800+(d*0.300000))
jesstemp84 ='jessatom3 x. %s'%(10.382800+(d*0.300000))
jesstemp85 ='jessatom4 x. %s'%(9.524300+(d*0.300000))
jesstemp86 ='jessatom5 x. %s'%(8.069900+(d*0.300000))
jesstemp87 ='jessatom6 x. %s'%(7.140700+(d*0.300000))
jesstemp88 ='jessatom7 x. %s'%(7.938600+(d*0.300000))
jesstemp89 ='jessatom8 x. %s'%(8.332500+(d*0.300000))
jesstemp90 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp91 ='br. jessatom9'
jesstemp92 ='jessatom10 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(3.252200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(3.221900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.019800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(10.382800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(9.524300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(8.069900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.140700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(8.332500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('Jfa_1qq5-D8A-T12A-R39A-N115A-K147A-S171A-N173A-F175A-D176A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
