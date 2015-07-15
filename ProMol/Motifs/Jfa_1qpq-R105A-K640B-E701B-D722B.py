'''
FUNC:Jfa_1qpq-R105A-K640B-E701B-D722B
PDB:1qpq
EC:2.4.2.19
PFAM:PF02749,PF01729
RESI:arg,lys,glu,asp
LOCI:a-105;b-640,701,722;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. lys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  ce '
jesstemp3 ='r. lys'
jesstemp4 ='jessatom0 x. %s'%(1.504900+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.504900+(d*0.300000)))
jesstemp6 ='n.  nz '
jesstemp7 ='jessatom0 x. %s'%(2.424000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.474600+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.424000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.474600+(d*0.300000)))
jesstemp10 ='r. glu'
jesstemp11 ='r. asp'
jesstemp12 ='jessatom0 x. %s'%(11.180700+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(9.696000+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(9.504100+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp10+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.180700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.696000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.504100+(d*0.300000)))
jesstemp15 ='n.  oe1'
jesstemp16 ='n.  oe2'
jesstemp17 ='n.  od1'
jesstemp18 ='n.  od2'
jesstemp19 ='jessatom0 x. %s'%(10.100000+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(8.635500+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(8.554700+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.272600+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+'))|((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.100000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.635500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.554700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.272600+(d*0.300000)))
jesstemp24 ='n.  oe2'
jesstemp25 ='n.  oe1'
jesstemp26 ='n.  od2'
jesstemp27 ='n.  od1'
jesstemp28 ='jessatom0 x. %s'%(11.685700+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(10.201000+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(9.857600+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+'))|((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.685700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.201000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.857600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.242200+(d*0.300000)))
jesstemp34 ='n.  cg '
jesstemp35 ='jessatom0 x. %s'%(11.120100+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(9.675800+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(8.958700+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(4.555100+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(5.070200+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(4.393500+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp34+')&('+jesstemp11+'))|(('+jesstemp34+')&('+jesstemp10+')))&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.120100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.675800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.958700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.555100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.070200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.393500+(d*0.300000)))
jesstemp41 ='jessatom0 x. %s'%(10.019200+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(8.595100+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(7.847700+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(5.019700+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(5.231800+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(5.019700+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+'))|((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.019200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.595100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.847700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp49 ='jessatom0 x. %s'%(11.695800+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(10.251500+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(9.453600+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(4.726800+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(5.373200+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(4.221800+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+'))|((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(11.695800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(10.251500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.453600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.726800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.373200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.221800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.211900+(d*0.300000)))
jesstemp58 ='n.  ne '
jesstemp59 ='r. arg'
jesstemp60 ='jessatom0 x. %s'%(5.120700+(d*0.300000))
jesstemp61 ='jessatom1 x. %s'%(5.100500+(d*0.300000))
jesstemp62 ='jessatom2 x. %s'%(5.797400+(d*0.300000))
jesstemp63 ='jessatom3 x. %s'%(10.726200+(d*0.300000))
jesstemp64 ='jessatom4 x. %s'%(9.544500+(d*0.300000))
jesstemp65 ='jessatom5 x. %s'%(11.089800+(d*0.300000))
jesstemp66 ='jessatom6 x. %s'%(12.402800+(d*0.300000))
jesstemp67 ='jessatom7 x. %s'%(11.655400+(d*0.300000))
jesstemp68 ='jessatom8 x. %s'%(12.665400+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.120700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.100500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(5.797400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(10.726200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.544500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(11.089800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(12.402800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(11.655400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(12.665400+(d*0.300000)))
jesstemp69 ='n.  nh1'
jesstemp70 ='n.  nh2'
jesstemp71 ='jessatom0 x. %s'%(4.484400+(d*0.300000))
jesstemp72 ='jessatom1 x. %s'%(4.736900+(d*0.300000))
jesstemp73 ='jessatom2 x. %s'%(4.979300+(d*0.300000))
jesstemp74 ='jessatom3 x. %s'%(11.534200+(d*0.300000))
jesstemp75 ='jessatom4 x. %s'%(10.453500+(d*0.300000))
jesstemp76 ='jessatom5 x. %s'%(11.746300+(d*0.300000))
jesstemp77 ='jessatom6 x. %s'%(12.433100+(d*0.300000))
jesstemp78 ='jessatom7 x. %s'%(11.584700+(d*0.300000))
jesstemp79 ='jessatom8 x. %s'%(12.614900+(d*0.300000))
jesstemp80 ='jessatom9 x. %s'%(2.353300+(d*0.300000))
jesstemp81 ='br. jessatom9'
cmd.select('jessatom10', '((('+jesstemp69+')|('+jesstemp70+'))&('+jesstemp59+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(4.484400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(4.736900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(4.979300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(11.534200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(10.453500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(11.746300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(12.433100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(11.584700+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(12.614900+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(2.353300+(d*0.300000)))
jesstemp82 ='n.  nh2'
jesstemp83 ='n.  nh1'
jesstemp84 ='jessatom0 x. %s'%(4.666200+(d*0.300000))
jesstemp85 ='jessatom1 x. %s'%(4.161200+(d*0.300000))
jesstemp86 ='jessatom2 x. %s'%(4.343000+(d*0.300000))
jesstemp87 ='jessatom3 x. %s'%(9.221300+(d*0.300000))
jesstemp88 ='jessatom4 x. %s'%(8.140600+(d*0.300000))
jesstemp89 ='jessatom5 x. %s'%(9.443500+(d*0.300000))
jesstemp90 ='jessatom6 x. %s'%(10.433300+(d*0.300000))
jesstemp91 ='jessatom7 x. %s'%(9.685900+(d*0.300000))
jesstemp92 ='jessatom8 x. %s'%(10.615100+(d*0.300000))
jesstemp93 ='jessatom9 x. %s'%(2.302800+(d*0.300000))
jesstemp94 ='br. jessatom9'
jesstemp95 ='jessatom10 x. %s'%(2.333100+(d*0.300000))
cmd.select('jessatom11', '((('+jesstemp82+')|('+jesstemp83+'))&('+jesstemp59+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(4.666200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(4.161200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.343000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(9.221300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(8.140600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(9.443500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(10.433300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(9.685900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(10.615100+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.302800+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.333100+(d*0.300000)))
cmd.select('Jfa_1qpq-R105A-K640B-E701B-D722B', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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