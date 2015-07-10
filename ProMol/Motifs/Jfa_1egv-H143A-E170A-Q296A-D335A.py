'''
FUNC:Jfa_1egv-H143A-E170A-Q296A-D335A
PDB:1egv
EC:4.2.1.28
PFAM:PF02288,PF02287,PF02286
RESI:his,glu,gln,asp
LOCI:a-143,170,296,335;
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
jesstemp7 ='jessatom0 x. %s'%(2.201800+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. glu'
jesstemp12 ='r. asp'
jesstemp13 ='jessatom0 x. %s'%(5.191400+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(6.009500+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(4.332900+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.191400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.009500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.332900+(d*0.300000)))
jesstemp16 ='n.  oe2'
jesstemp17 ='n.  oe1'
jesstemp18 ='n.  od2'
jesstemp19 ='n.  od1'
jesstemp20 ='jessatom0 x. %s'%(4.575300+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(5.342900+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(3.484500+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.575300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.342900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.484500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp25 ='n.  oe1'
jesstemp26 ='n.  oe2'
jesstemp27 ='n.  od1'
jesstemp28 ='n.  od2'
jesstemp29 ='jessatom0 x. %s'%(6.100400+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(6.746800+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(5.019700+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(1.272600+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.100400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.746800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.232100+(d*0.300000)))
jesstemp35 ='r. gln'
jesstemp36 ='r. asn'
jesstemp37 ='jessatom0 x. %s'%(8.787000+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(8.817300+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(6.726600+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(6.201400+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(5.544900+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(5.959000+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp10+')&('+jesstemp35+'))|(('+jesstemp10+')&('+jesstemp36+')))&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.787000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.817300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.726600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.959000+(d*0.300000)))
jesstemp43 ='jessatom0 x. %s'%(7.635600+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(7.686100+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(5.605500+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(5.504500+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(4.676300+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(5.474200+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp50 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp25+')&('+jesstemp35+'))|(('+jesstemp25+')&('+jesstemp36+')))&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.635600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.686100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.605500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.504500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.676300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.474200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.252400+(d*0.300000)))
jesstemp51 ='jessatom0 x. %s'%(9.120300+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(9.211200+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(7.080100+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(5.888300+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(5.504500+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(5.393400+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(1.353400+(d*0.300000))
jesstemp58 ='br. jessatom6'
jesstemp59 ='jessatom7 x. %s'%(2.252300+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp6+')&('+jesstemp35+'))|(('+jesstemp6+')&('+jesstemp36+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.120300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.211200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.080100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.888300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.504500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.393400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.353400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.252300+(d*0.300000)))
jesstemp60 ='jessatom0 x. %s'%(6.676100+(d*0.300000))
jesstemp61 ='jessatom1 x. %s'%(5.969100+(d*0.300000))
jesstemp62 ='jessatom2 x. %s'%(4.807600+(d*0.300000))
jesstemp63 ='jessatom3 x. %s'%(7.716400+(d*0.300000))
jesstemp64 ='jessatom4 x. %s'%(6.676100+(d*0.300000))
jesstemp65 ='jessatom5 x. %s'%(7.958800+(d*0.300000))
jesstemp66 ='jessatom6 x. %s'%(5.282300+(d*0.300000))
jesstemp67 ='jessatom7 x. %s'%(4.464200+(d*0.300000))
jesstemp68 ='jessatom8 x. %s'%(6.201400+(d*0.300000))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp12+'))|(('+jesstemp0+')&('+jesstemp11+')))&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(6.676100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.969100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(4.807600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(7.716400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(6.676100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.958800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(5.282300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.464200+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(6.201400+(d*0.300000)))
jesstemp69 ='jessatom0 x. %s'%(7.787100+(d*0.300000))
jesstemp70 ='jessatom1 x. %s'%(6.969000+(d*0.300000))
jesstemp71 ='jessatom2 x. %s'%(5.979200+(d*0.300000))
jesstemp72 ='jessatom3 x. %s'%(8.918300+(d*0.300000))
jesstemp73 ='jessatom4 x. %s'%(7.908300+(d*0.300000))
jesstemp74 ='jessatom5 x. %s'%(9.090000+(d*0.300000))
jesstemp75 ='jessatom6 x. %s'%(5.928700+(d*0.300000))
jesstemp76 ='jessatom7 x. %s'%(5.292400+(d*0.300000))
jesstemp77 ='jessatom8 x. %s'%(6.868000+(d*0.300000))
jesstemp78 ='jessatom9 x. %s'%(1.262500+(d*0.300000))
jesstemp79 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+'))|((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+')))&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(7.787100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(6.969000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(8.918300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(9.090000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(5.928700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(5.292400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(6.868000+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.262500+(d*0.300000)))
jesstemp80 ='jessatom0 x. %s'%(6.585200+(d*0.300000))
jesstemp81 ='jessatom1 x. %s'%(6.039800+(d*0.300000))
jesstemp82 ='jessatom2 x. %s'%(4.504600+(d*0.300000))
jesstemp83 ='jessatom3 x. %s'%(6.807400+(d*0.300000))
jesstemp84 ='jessatom4 x. %s'%(5.827700+(d*0.300000))
jesstemp85 ='jessatom5 x. %s'%(6.928600+(d*0.300000))
jesstemp86 ='jessatom6 x. %s'%(4.171300+(d*0.300000))
jesstemp87 ='jessatom7 x. %s'%(3.383500+(d*0.300000))
jesstemp88 ='jessatom8 x. %s'%(4.999500+(d*0.300000))
jesstemp89 ='jessatom9 x. %s'%(1.252400+(d*0.300000))
jesstemp90 ='br. jessatom9'
jesstemp91 ='jessatom10 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom11', '((((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+'))|((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+')))&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(6.585200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(6.039800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.504600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(6.807400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(6.928600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.171300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(3.383500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.201800+(d*0.300000)))
cmd.select('Jfa_1egv-H143A-E170A-Q296A-D335A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
