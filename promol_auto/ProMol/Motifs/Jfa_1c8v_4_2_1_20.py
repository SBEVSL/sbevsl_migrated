'''
FUNC:Jfa_1c8v_4_2_1_20
PDB:1c8v
EC:4.2.1.20
RESI:his,lys,lys,asp
LOCI:b-86,87,167,305;
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
jesstemp9 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. lys'
jesstemp12 ='jessatom0 x. %s'%(6.241800+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(5.666100+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(5.373200+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.666100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.373200+(d*0.300000)))
jesstemp15 ='n.  ce '
jesstemp16 ='jessatom0 x. %s'%(6.878100+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(6.140800+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(5.585300+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.555400+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.878100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.555400+(d*0.300000)))
jesstemp21 ='n.  nz '
jesstemp22 ='jessatom0 x. %s'%(6.292300+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(5.433800+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(4.757100+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.615900+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.474600+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.292300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.433800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.757100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.615900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.474600+(d*0.300000)))
jesstemp28 ='jessatom0 x. %s'%(23.048200+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(22.270500+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(20.927200+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(19.159700+(d*0.300000))
jesstemp32 ='jessatom4 x. %s'%(17.685100+(d*0.300000))
jesstemp33 ='jessatom5 x. %s'%(17.432600+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(23.048200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(22.270500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(20.927200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(19.159700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(17.685100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(17.432600+(d*0.300000)))
jesstemp34 ='jessatom0 x. %s'%(24.007700+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(23.189600+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(21.927100+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(19.886900+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(18.422400+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(18.230500+(d*0.300000))
jesstemp40 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(24.007700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(23.189600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(21.927100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(19.886900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(18.422400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(18.230500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
jesstemp42 ='jessatom0 x. %s'%(25.179300+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(24.391500+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(23.088600+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(20.927200+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(19.493000+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(19.381900+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(2.585600+(d*0.300000))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(1.504900+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(25.179300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(24.391500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(23.088600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(20.927200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(19.493000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(19.381900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.585600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.504900+(d*0.300000)))
jesstemp51 ='r. asp'
jesstemp52 ='r. glu'
jesstemp53 ='jessatom0 x. %s'%(16.493300+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(15.311600+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(14.847000+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(13.513800+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(12.069500+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(11.382700+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(10.897900+(d*0.300000))
jesstemp60 ='jessatom7 x. %s'%(11.200900+(d*0.300000))
jesstemp61 ='jessatom8 x. %s'%(12.655300+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp51+'))|(('+jesstemp0+')&('+jesstemp52+')))&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(16.493300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(15.311600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(14.847000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(13.513800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(12.069500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(11.382700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(10.897900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(11.200900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(12.655300+(d*0.300000)))
jesstemp62 ='n.  od1'
jesstemp63 ='n.  od2'
jesstemp64 ='n.  oe1'
jesstemp65 ='n.  oe2'
jesstemp66 ='jessatom0 x. %s'%(17.341700+(d*0.300000))
jesstemp67 ='jessatom1 x. %s'%(16.129700+(d*0.300000))
jesstemp68 ='jessatom2 x. %s'%(15.756000+(d*0.300000))
jesstemp69 ='jessatom3 x. %s'%(14.109700+(d*0.300000))
jesstemp70 ='jessatom4 x. %s'%(12.695700+(d*0.300000))
jesstemp71 ='jessatom5 x. %s'%(12.120000+(d*0.300000))
jesstemp72 ='jessatom6 x. %s'%(11.059500+(d*0.300000))
jesstemp73 ='jessatom7 x. %s'%(11.190800+(d*0.300000))
jesstemp74 ='jessatom8 x. %s'%(12.604800+(d*0.300000))
jesstemp75 ='jessatom9 x. %s'%(1.272600+(d*0.300000))
jesstemp76 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp62+')|('+jesstemp63+'))&('+jesstemp51+'))|((('+jesstemp64+')|('+jesstemp65+'))&('+jesstemp52+')))&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(17.341700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(16.129700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(15.756000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(14.109700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(12.695700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(12.120000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(11.059500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(11.190800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(12.604800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.272600+(d*0.300000)))
jesstemp77 ='n.  od2'
jesstemp78 ='n.  od1'
jesstemp79 ='n.  oe2'
jesstemp80 ='n.  oe1'
jesstemp81 ='jessatom0 x. %s'%(16.402400+(d*0.300000))
jesstemp82 ='jessatom1 x. %s'%(15.200500+(d*0.300000))
jesstemp83 ='jessatom2 x. %s'%(14.776300+(d*0.300000))
jesstemp84 ='jessatom3 x. %s'%(13.877400+(d*0.300000))
jesstemp85 ='jessatom4 x. %s'%(12.453300+(d*0.300000))
jesstemp86 ='jessatom5 x. %s'%(11.635200+(d*0.300000))
jesstemp87 ='jessatom6 x. %s'%(11.544300+(d*0.300000))
jesstemp88 ='jessatom7 x. %s'%(11.928100+(d*0.300000))
jesstemp89 ='jessatom8 x. %s'%(13.402700+(d*0.300000))
jesstemp90 ='br. jessatom9'
jesstemp91 ='jessatom10 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp77+')|('+jesstemp78+'))&('+jesstemp51+'))|((('+jesstemp79+')|('+jesstemp80+'))&('+jesstemp52+')))&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp75+')&('+jesstemp90+')&('+jesstemp91+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(16.402400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(15.200500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(14.776300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(13.877400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(12.453300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(11.635200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(11.544300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(11.928100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(13.402700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('Jfa_1c8v_4_2_1_20', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
