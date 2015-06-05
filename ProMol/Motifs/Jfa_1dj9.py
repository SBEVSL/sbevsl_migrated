'''
FUNC:Jfa_1dj9
PDB:1dj9
EC:2.3.1.47
PFAM:PF01212,PF00155
RESI:his,glu,asp,lys
LOCI:a-133,175,204,236;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.393800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.393800+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.222000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.171500+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. glu'
jesstemp12 ='r. asp'
jesstemp13 ='jessatom0 x. %s'%(5.494400+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(6.635700+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(7.302300+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.494400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.302300+(d*0.300000)))
jesstemp16 ='n.  oe1'
jesstemp17 ='n.  oe2'
jesstemp18 ='n.  od1'
jesstemp19 ='n.  od2'
jesstemp20 ='jessatom0 x. %s'%(5.959000+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(7.181100+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(7.494200+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.181100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.494200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp25 ='n.  oe2'
jesstemp26 ='n.  oe1'
jesstemp27 ='n.  od2'
jesstemp28 ='n.  od1'
jesstemp29 ='jessatom0 x. %s'%(4.545000+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(5.726700+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(6.453900+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp23+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.545000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.453900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.191700+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(5.918600+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(6.120600+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(7.241700+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(5.171200+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(5.585300+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(5.474200+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp12+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.918600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.120600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.241700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.474200+(d*0.300000)))
jesstemp40 ='jessatom0 x. %s'%(6.423600+(d*0.300000))
jesstemp41 ='jessatom1 x. %s'%(6.676100+(d*0.300000))
jesstemp42 ='jessatom2 x. %s'%(7.463900+(d*0.300000))
jesstemp43 ='jessatom3 x. %s'%(5.605500+(d*0.300000))
jesstemp44 ='jessatom4 x. %s'%(5.746900+(d*0.300000))
jesstemp45 ='jessatom5 x. %s'%(6.029700+(d*0.300000))
jesstemp46 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp47 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+'))|((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+')))&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.423600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.676100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.463900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.605500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.746900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.029700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp48 ='jessatom0 x. %s'%(4.777300+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(4.888400+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(6.140800+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(5.090400+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(5.625700+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(5.090400+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(1.272600+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+'))|((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+')))&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.888400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.090400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.090400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.181600+(d*0.300000)))
jesstemp57 ='r. lys'
jesstemp58 ='jessatom0 x. %s'%(8.968800+(d*0.300000))
jesstemp59 ='jessatom1 x. %s'%(9.281900+(d*0.300000))
jesstemp60 ='jessatom2 x. %s'%(8.191100+(d*0.300000))
jesstemp61 ='jessatom3 x. %s'%(9.766700+(d*0.300000))
jesstemp62 ='jessatom4 x. %s'%(9.069800+(d*0.300000))
jesstemp63 ='jessatom5 x. %s'%(10.039400+(d*0.300000))
jesstemp64 ='jessatom6 x. %s'%(8.191100+(d*0.300000))
jesstemp65 ='jessatom7 x. %s'%(7.150800+(d*0.300000))
jesstemp66 ='jessatom8 x. %s'%(8.261800+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp10+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(8.968800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(9.281900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(8.191100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(9.766700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.069800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(10.039400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(8.191100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(7.150800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(8.261800+(d*0.300000)))
jesstemp67 ='n.  ce '
jesstemp68 ='jessatom0 x. %s'%(7.665900+(d*0.300000))
jesstemp69 ='jessatom1 x. %s'%(7.979000+(d*0.300000))
jesstemp70 ='jessatom2 x. %s'%(6.736700+(d*0.300000))
jesstemp71 ='jessatom3 x. %s'%(9.079900+(d*0.300000))
jesstemp72 ='jessatom4 x. %s'%(8.463800+(d*0.300000))
jesstemp73 ='jessatom5 x. %s'%(9.180900+(d*0.300000))
jesstemp74 ='jessatom6 x. %s'%(7.797200+(d*0.300000))
jesstemp75 ='jessatom7 x. %s'%(6.918500+(d*0.300000))
jesstemp76 ='jessatom8 x. %s'%(7.635600+(d*0.300000))
jesstemp77 ='jessatom9 x. %s'%(1.545300+(d*0.300000))
jesstemp78 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp67+')&('+jesstemp57+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(7.979000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(6.736700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(9.079900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(8.463800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(9.180900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(7.797200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.545300+(d*0.300000)))
jesstemp79 ='n.  nz '
jesstemp80 ='jessatom0 x. %s'%(7.807300+(d*0.300000))
jesstemp81 ='jessatom1 x. %s'%(7.878000+(d*0.300000))
jesstemp82 ='jessatom2 x. %s'%(6.534700+(d*0.300000))
jesstemp83 ='jessatom3 x. %s'%(10.049500+(d*0.300000))
jesstemp84 ='jessatom4 x. %s'%(9.544500+(d*0.300000))
jesstemp85 ='jessatom5 x. %s'%(9.999000+(d*0.300000))
jesstemp86 ='jessatom6 x. %s'%(8.403200+(d*0.300000))
jesstemp87 ='jessatom7 x. %s'%(7.605300+(d*0.300000))
jesstemp88 ='jessatom8 x. %s'%(8.090100+(d*0.300000))
jesstemp89 ='jessatom9 x. %s'%(2.525000+(d*0.300000))
jesstemp90 ='br. jessatom9'
jesstemp91 ='jessatom10 x. %s'%(1.504900+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp79+')&('+jesstemp57+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(7.807300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(7.878000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(6.534700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(10.049500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(9.544500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(9.999000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(8.403200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.605300+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(8.090100+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.525000+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.504900+(d*0.300000)))
cmd.select('Jfa_1dj9', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
