'''
FUNC:Jfa_1xic-H54A-D57A-E181A-K183A
PDB:1xic
EC:5.3.1.5
PFAM:PF01261
RESI:his,asp,glu,lys
LOCI:a-54,57,181,183;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.424100+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.424100+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.191700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.181600+(d*0.300000)))
jesstemp10 ='r. asp'
jesstemp11 ='r. glu'
jesstemp12 ='jessatom0 x. %s'%(4.201600+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(3.595600+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(5.736800+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp10+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.201600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.595600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.736800+(d*0.300000)))
jesstemp15 ='n.  od1'
jesstemp16 ='n.  od2'
jesstemp17 ='n.  oe1'
jesstemp18 ='n.  oe2'
jesstemp19 ='jessatom0 x. %s'%(4.373300+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(3.787500+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(5.746900+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.282700+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+'))|((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.373300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.787500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.746900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.282700+(d*0.300000)))
jesstemp24 ='n.  od2'
jesstemp25 ='n.  od1'
jesstemp26 ='n.  oe2'
jesstemp27 ='n.  oe1'
jesstemp28 ='jessatom0 x. %s'%(3.504700+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(2.737100+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(4.908600+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(1.242300+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+'))|((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.504700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(2.737100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.908600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
jesstemp34 ='n.  cd '
jesstemp35 ='jessatom0 x. %s'%(10.110100+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(9.887900+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(8.100200+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(13.301700+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(13.443100+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(12.231100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp34+')&('+jesstemp11+'))|(('+jesstemp34+')&('+jesstemp10+')))&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.110100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.887900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.100200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(13.301700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(13.443100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(12.231100+(d*0.300000)))
jesstemp41 ='jessatom0 x. %s'%(9.201100+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(9.019300+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(7.292200+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(12.423000+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(12.655300+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(11.322100+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp17+')|('+jesstemp18+'))&('+jesstemp11+'))|((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp10+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.019300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.292200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(12.423000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(12.655300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(11.322100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp49 ='jessatom0 x. %s'%(10.382800+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(10.019200+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(8.292100+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(13.342100+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(13.422900+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(12.311900+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp56 ='br. jessatom6'
jesstemp57 ='jessatom7 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp26+')|('+jesstemp27+'))&('+jesstemp11+'))|((('+jesstemp24+')|('+jesstemp25+'))&('+jesstemp10+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(10.382800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(10.019200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.292100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(13.342100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(13.422900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(12.311900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.242200+(d*0.300000)))
jesstemp58 ='r. lys'
jesstemp59 ='jessatom0 x. %s'%(13.433000+(d*0.300000))
jesstemp60 ='jessatom1 x. %s'%(13.160300+(d*0.300000))
jesstemp61 ='jessatom2 x. %s'%(11.301900+(d*0.300000))
jesstemp62 ='jessatom3 x. %s'%(16.240800+(d*0.300000))
jesstemp63 ='jessatom4 x. %s'%(15.796400+(d*0.300000))
jesstemp64 ='jessatom5 x. %s'%(15.574200+(d*0.300000))
jesstemp65 ='jessatom6 x. %s'%(7.362900+(d*0.300000))
jesstemp66 ='jessatom7 x. %s'%(8.342600+(d*0.300000))
jesstemp67 ='jessatom8 x. %s'%(6.575100+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp34+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(13.433000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(13.160300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(11.301900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(16.240800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(15.796400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(15.574200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(7.362900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(8.342600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(6.575100+(d*0.300000)))
jesstemp68 ='n.  ce '
jesstemp69 ='jessatom0 x. %s'%(13.897600+(d*0.300000))
jesstemp70 ='jessatom1 x. %s'%(13.483500+(d*0.300000))
jesstemp71 ='jessatom2 x. %s'%(11.786700+(d*0.300000))
jesstemp72 ='jessatom3 x. %s'%(16.372100+(d*0.300000))
jesstemp73 ='jessatom4 x. %s'%(15.877200+(d*0.300000))
jesstemp74 ='jessatom5 x. %s'%(15.766100+(d*0.300000))
jesstemp75 ='jessatom6 x. %s'%(8.231500+(d*0.300000))
jesstemp76 ='jessatom7 x. %s'%(9.201100+(d*0.300000))
jesstemp77 ='jessatom8 x. %s'%(7.282100+(d*0.300000))
jesstemp78 ='jessatom9 x. %s'%(1.545300+(d*0.300000))
jesstemp79 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp68+')&('+jesstemp58+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(13.897600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(13.483500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(11.786700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(16.372100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(15.877200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(15.766100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(8.231500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(7.282100+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.545300+(d*0.300000)))
jesstemp80 ='n.  nz '
jesstemp81 ='jessatom0 x. %s'%(12.948200+(d*0.300000))
jesstemp82 ='jessatom1 x. %s'%(12.513900+(d*0.300000))
jesstemp83 ='jessatom2 x. %s'%(10.908000+(d*0.300000))
jesstemp84 ='jessatom3 x. %s'%(15.251000+(d*0.300000))
jesstemp85 ='jessatom4 x. %s'%(14.685400+(d*0.300000))
jesstemp86 ='jessatom5 x. %s'%(14.715700+(d*0.300000))
jesstemp87 ='jessatom6 x. %s'%(8.494100+(d*0.300000))
jesstemp88 ='jessatom7 x. %s'%(9.312200+(d*0.300000))
jesstemp89 ='jessatom8 x. %s'%(7.554800+(d*0.300000))
jesstemp90 ='jessatom9 x. %s'%(2.464400+(d*0.300000))
jesstemp91 ='br. jessatom9'
jesstemp92 ='jessatom10 x. %s'%(1.525100+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp80+')&('+jesstemp58+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(12.948200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(12.513900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(10.908000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(15.251000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(14.685400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(14.715700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(9.312200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(7.554800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.464400+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.525100+(d*0.300000)))
cmd.select('Jfa_1xic-H54A-D57A-E181A-K183A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
