'''
FUNC:Jfa_1dcp_4_2_1_96
PDB:1dcp
EC:4.2.1.96
RESI:his,his,his,asp
LOCI:a-62,63,80,89;
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
jesstemp7 ='jessatom0 x. %s'%(2.232100+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(6.544800+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(7.171000+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(7.878000+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.544800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.171000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.878000+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(6.100400+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(6.554900+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(7.635600+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(1.403900+(d*0.300000))
jesstemp17 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.100400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.554900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.403900+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(7.625500+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(8.312300+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(9.342500+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(2.232100+(d*0.300000))
jesstemp22 ='br. jessatom3'
jesstemp23 ='jessatom4 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.625500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.312300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.342500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.232100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.242200+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(8.524400+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(7.575000+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(8.090100+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(9.211200+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(8.686000+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(10.877700+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.524400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.575000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.090100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.211200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.686000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(10.877700+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(7.433600+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.625600+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(7.039700+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(7.979000+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(7.544700+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(9.746500+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.414000+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.433600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.625600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.979000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.544700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.746500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.414000+(d*0.300000)))
jesstemp38 ='jessatom0 x. %s'%(9.231400+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(8.484000+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(8.484000+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(9.362700+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(9.170800+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(11.291800+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(2.242200+(d*0.300000))
jesstemp45 ='br. jessatom6'
jesstemp46 ='jessatom7 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.231400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.484000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.484000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.362700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.170800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(11.291800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.242200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.201800+(d*0.300000)))
jesstemp47 ='r. asp'
jesstemp48 ='r. glu'
jesstemp49 ='jessatom0 x. %s'%(5.555000+(d*0.300000))
jesstemp50 ='jessatom1 x. %s'%(5.151000+(d*0.300000))
jesstemp51 ='jessatom2 x. %s'%(3.393600+(d*0.300000))
jesstemp52 ='jessatom3 x. %s'%(10.988800+(d*0.300000))
jesstemp53 ='jessatom4 x. %s'%(10.827200+(d*0.300000))
jesstemp54 ='jessatom5 x. %s'%(12.625000+(d*0.300000))
jesstemp55 ='jessatom6 x. %s'%(8.928400+(d*0.300000))
jesstemp56 ='jessatom7 x. %s'%(8.181000+(d*0.300000))
jesstemp57 ='jessatom8 x. %s'%(9.049600+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp47+'))|(('+jesstemp0+')&('+jesstemp48+')))&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.555000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.151000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(3.393600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(10.988800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(10.827200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(12.625000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(8.928400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(8.181000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(9.049600+(d*0.300000)))
jesstemp58 ='n.  od1'
jesstemp59 ='n.  od2'
jesstemp60 ='n.  oe1'
jesstemp61 ='n.  oe2'
jesstemp62 ='jessatom0 x. %s'%(4.757100+(d*0.300000))
jesstemp63 ='jessatom1 x. %s'%(4.423800+(d*0.300000))
jesstemp64 ='jessatom2 x. %s'%(2.525000+(d*0.300000))
jesstemp65 ='jessatom3 x. %s'%(9.827300+(d*0.300000))
jesstemp66 ='jessatom4 x. %s'%(9.716200+(d*0.300000))
jesstemp67 ='jessatom5 x. %s'%(11.524100+(d*0.300000))
jesstemp68 ='jessatom6 x. %s'%(8.150700+(d*0.300000))
jesstemp69 ='jessatom7 x. %s'%(7.282100+(d*0.300000))
jesstemp70 ='jessatom8 x. %s'%(8.201200+(d*0.300000))
jesstemp71 ='jessatom9 x. %s'%(1.222100+(d*0.300000))
jesstemp72 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp58+')|('+jesstemp59+'))&('+jesstemp47+'))|((('+jesstemp60+')|('+jesstemp61+'))&('+jesstemp48+')))&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(4.757100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(4.423800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(2.525000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(9.827300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(9.716200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(11.524100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(8.150700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(7.282100+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.222100+(d*0.300000)))
jesstemp73 ='n.  od2'
jesstemp74 ='n.  od1'
jesstemp75 ='n.  oe2'
jesstemp76 ='n.  oe1'
jesstemp77 ='jessatom0 x. %s'%(6.302400+(d*0.300000))
jesstemp78 ='jessatom1 x. %s'%(5.645900+(d*0.300000))
jesstemp79 ='jessatom2 x. %s'%(4.262200+(d*0.300000))
jesstemp80 ='jessatom3 x. %s'%(11.806900+(d*0.300000))
jesstemp81 ='jessatom4 x. %s'%(11.544300+(d*0.300000))
jesstemp82 ='jessatom5 x. %s'%(13.433000+(d*0.300000))
jesstemp83 ='jessatom6 x. %s'%(8.706200+(d*0.300000))
jesstemp84 ='jessatom7 x. %s'%(8.160800+(d*0.300000))
jesstemp85 ='jessatom8 x. %s'%(8.968800+(d*0.300000))
jesstemp86 ='jessatom9 x. %s'%(1.313000+(d*0.300000))
jesstemp87 ='br. jessatom9'
jesstemp88 ='jessatom10 x. %s'%(2.242200+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp73+')|('+jesstemp74+'))&('+jesstemp47+'))|((('+jesstemp75+')|('+jesstemp76+'))&('+jesstemp48+')))&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(6.302400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(5.645900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.262200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(11.806900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(11.544300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(13.433000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(8.160800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(8.968800+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.313000+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.242200+(d*0.300000)))
cmd.select('Jfa_1dcp_4_2_1_96', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
