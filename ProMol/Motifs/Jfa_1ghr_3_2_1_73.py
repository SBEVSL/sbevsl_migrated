'''
FUNC:Jfa_1ghr_3_2_1_73
PDB:1ghr
EC:3.2.1.73
RESI:glu,glu,lys,glu
LOCI:a-232,280,283,288;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  oe1'
jesstemp4 ='n.  oe2'
jesstemp5 ='n.  od1'
jesstemp6 ='n.  od2'
jesstemp7 ='jessatom0 x. %s'%(1.241240+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,1.238761-(d*0.050000)))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
jesstemp9 ='n.  oe2'
jesstemp10 ='n.  oe1'
jesstemp11 ='n.  od2'
jesstemp12 ='n.  od1'
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.172170+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom1 x. %s)'%(max(0.05,2.167832-(d*0.050000)))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.172170+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.167832-(d*0.050000))))
jesstemp15 ='jessatom0 x. %s'%(9.929920+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom0 x. %s)'%(max(0.05,9.910090-(d*0.050000)))
jesstemp16 ='jessatom1 x. %s'%(10.230220+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom1 x. %s)'%(max(0.05,10.209790-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(9.489480+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,9.470529-(d*0.050000)))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.929920+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,9.910090-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.230220+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,10.209790-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.489480+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,9.470529-(d*0.050000))))
jesstemp18 ='jessatom0 x. %s'%(8.938930+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom0 x. %s)'%(max(0.05,8.921079-(d*0.050000)))
jesstemp19 ='jessatom1 x. %s'%(9.189180+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom1 x. %s)'%(max(0.05,9.170829-(d*0.050000)))
jesstemp20 ='jessatom2 x. %s'%(8.608600+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom2 x. %s)'%(max(0.05,8.591409-(d*0.050000)))
jesstemp21 ='jessatom3 x. %s'%(1.241240+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom3 x. %s)'%(max(0.05,1.238761-(d*0.050000)))
jesstemp22 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.938930+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,8.921079-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.189180+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,9.170829-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.608600+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,8.591409-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
jesstemp23 ='jessatom0 x. %s'%(9.949940+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom0 x. %s)'%(max(0.05,9.930070-(d*0.050000)))
jesstemp24 ='jessatom1 x. %s'%(10.330320+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom1 x. %s)'%(max(0.05,10.309690-(d*0.050000)))
jesstemp25 ='jessatom2 x. %s'%(9.369360+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom2 x. %s)'%(max(0.05,9.350649-(d*0.050000)))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(2.172170+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom4 x. %s)'%(max(0.05,2.167832-(d*0.050000)))
cmd.select('jessatom5', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp21+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.949940+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,9.930070-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.330320+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,10.309690-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.369360+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,9.350649-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.172170+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,2.167832-(d*0.050000))))
jesstemp28 ='r. lys'
jesstemp29 ='jessatom0 x. %s'%(10.090080+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom0 x. %s)'%(max(0.05,10.069930-(d*0.050000)))
jesstemp30 ='jessatom1 x. %s'%(9.849840+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom1 x. %s)'%(max(0.05,9.830170-(d*0.050000)))
jesstemp31 ='jessatom2 x. %s'%(9.829820+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom2 x. %s)'%(max(0.05,9.810190-(d*0.050000)))
jesstemp32 ='jessatom3 x. %s'%(4.594590+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom3 x. %s)'%(max(0.05,4.585415-(d*0.050000)))
jesstemp33 ='jessatom4 x. %s'%(4.374370+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom4 x. %s)'%(max(0.05,4.365634-(d*0.050000)))
jesstemp34 ='jessatom5 x. %s'%(5.065060+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom5 x. %s)'%(max(0.05,5.054945-(d*0.050000)))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.090080+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,10.069930-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.849840+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,9.830170-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.829820+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,9.810190-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.594590+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,4.585415-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.374370+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,4.365634-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.065060+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,5.054945-(d*0.050000))))
jesstemp35 ='n.  ce '
jesstemp36 ='jessatom0 x. %s'%(8.868860+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom0 x. %s)'%(max(0.05,8.851149-(d*0.050000)))
jesstemp37 ='jessatom1 x. %s'%(8.758750+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom1 x. %s)'%(max(0.05,8.741259-(d*0.050000)))
jesstemp38 ='jessatom2 x. %s'%(8.518510+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom2 x. %s)'%(max(0.05,8.501499-(d*0.050000)))
jesstemp39 ='jessatom3 x. %s'%(3.773770+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom3 x. %s)'%(max(0.05,3.766234-(d*0.050000)))
jesstemp40 ='jessatom4 x. %s'%(3.423420+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom4 x. %s)'%(max(0.05,3.416583-(d*0.050000)))
jesstemp41 ='jessatom5 x. %s'%(4.074070+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom5 x. %s)'%(max(0.05,4.065934-(d*0.050000)))
jesstemp42 ='jessatom6 x. %s'%(1.531530+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom6 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp35+')&('+jesstemp28+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.868860+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,8.851149-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.758750+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,8.741259-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.518510+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,8.501499-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.773770+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,3.766234-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.423420+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,3.416583-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.074070+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,4.065934-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp44 ='n.  nz '
jesstemp45 ='jessatom0 x. %s'%(8.698690+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom0 x. %s)'%(max(0.05,8.681319-(d*0.050000)))
jesstemp46 ='jessatom1 x. %s'%(8.608600+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom1 x. %s)'%(max(0.05,8.591409-(d*0.050000)))
jesstemp47 ='jessatom2 x. %s'%(8.178170+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom2 x. %s)'%(max(0.05,8.161838-(d*0.050000)))
jesstemp48 ='jessatom3 x. %s'%(4.524520+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom3 x. %s)'%(max(0.05,4.515485-(d*0.050000)))
jesstemp49 ='jessatom4 x. %s'%(4.344340+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom4 x. %s)'%(max(0.05,4.335664-(d*0.050000)))
jesstemp50 ='jessatom5 x. %s'%(4.424420+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom5 x. %s)'%(max(0.05,4.415584-(d*0.050000)))
jesstemp51 ='jessatom6 x. %s'%(2.552550+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom6 x. %s)'%(max(0.05,2.547453-(d*0.050000)))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(1.501500+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom7 x. %s)'%(max(0.05,1.498501-(d*0.050000)))
cmd.select('jessatom8', '(('+jesstemp44+')&('+jesstemp28+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.698690+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,8.681319-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.608600+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,8.591409-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.178170+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,8.161838-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.524520+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,4.515485-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.344340+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,4.335664-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.424420+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,4.415584-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.552550+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.547453-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.501500+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,1.498501-(d*0.050000))))
jesstemp54 ='jessatom0 x. %s'%(9.789780+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom0 x. %s)'%(max(0.05,9.770230-(d*0.050000)))
jesstemp55 ='jessatom1 x. %s'%(9.009000+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom1 x. %s)'%(max(0.05,8.991009-(d*0.050000)))
jesstemp56 ='jessatom2 x. %s'%(9.909900+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom2 x. %s)'%(max(0.05,9.890110-(d*0.050000)))
jesstemp57 ='jessatom3 x. %s'%(8.898890+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom3 x. %s)'%(max(0.05,8.881119-(d*0.050000)))
jesstemp58 ='jessatom4 x. %s'%(8.228220+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom4 x. %s)'%(max(0.05,8.211788-(d*0.050000)))
jesstemp59 ='jessatom5 x. %s'%(9.399390+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom5 x. %s)'%(max(0.05,9.380619-(d*0.050000)))
jesstemp60 ='jessatom6 x. %s'%(4.754750+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom6 x. %s)'%(max(0.05,4.745255-(d*0.050000)))
jesstemp61 ='jessatom7 x. %s'%(5.365360+(d*0.050000))
jesstemp61 = '('+jesstemp61+') and not (jessatom7 x. %s)'%(max(0.05,5.354645-(d*0.050000)))
jesstemp62 ='jessatom8 x. %s'%(5.685680+(d*0.050000))
jesstemp62 = '('+jesstemp62+') and not (jessatom8 x. %s)'%(max(0.05,5.674326-(d*0.050000)))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(9.789780+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom9 x. %s)'%(max(0.05,9.770230-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(9.009000+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom9 x. %s)'%(max(0.05,8.991009-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(9.909900+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom9 x. %s)'%(max(0.05,9.890110-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(8.898890+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom9 x. %s)'%(max(0.05,8.881119-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(8.228220+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom9 x. %s)'%(max(0.05,8.211788-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(9.399390+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom9 x. %s)'%(max(0.05,9.380619-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(4.754750+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom9 x. %s)'%(max(0.05,4.745255-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(5.365360+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom9 x. %s)'%(max(0.05,5.354645-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(5.685680+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom9 x. %s)'%(max(0.05,5.674326-(d*0.050000))))
jesstemp63 ='jessatom0 x. %s'%(9.069060+(d*0.050000))
jesstemp63 = '('+jesstemp63+') and not (jessatom0 x. %s)'%(max(0.05,9.050949-(d*0.050000)))
jesstemp64 ='jessatom1 x. %s'%(8.358350+(d*0.050000))
jesstemp64 = '('+jesstemp64+') and not (jessatom1 x. %s)'%(max(0.05,8.341658-(d*0.050000)))
jesstemp65 ='jessatom2 x. %s'%(9.059050+(d*0.050000))
jesstemp65 = '('+jesstemp65+') and not (jessatom2 x. %s)'%(max(0.05,9.040959-(d*0.050000)))
jesstemp66 ='jessatom3 x. %s'%(8.208200+(d*0.050000))
jesstemp66 = '('+jesstemp66+') and not (jessatom3 x. %s)'%(max(0.05,8.191808-(d*0.050000)))
jesstemp67 ='jessatom4 x. %s'%(7.577570+(d*0.050000))
jesstemp67 = '('+jesstemp67+') and not (jessatom4 x. %s)'%(max(0.05,7.562438-(d*0.050000)))
jesstemp68 ='jessatom5 x. %s'%(8.588580+(d*0.050000))
jesstemp68 = '('+jesstemp68+') and not (jessatom5 x. %s)'%(max(0.05,8.571429-(d*0.050000)))
jesstemp69 ='jessatom6 x. %s'%(4.184180+(d*0.050000))
jesstemp69 = '('+jesstemp69+') and not (jessatom6 x. %s)'%(max(0.05,4.175824-(d*0.050000)))
jesstemp70 ='jessatom7 x. %s'%(4.544540+(d*0.050000))
jesstemp70 = '('+jesstemp70+') and not (jessatom7 x. %s)'%(max(0.05,4.535465-(d*0.050000)))
jesstemp71 ='jessatom8 x. %s'%(4.644640+(d*0.050000))
jesstemp71 = '('+jesstemp71+') and not (jessatom8 x. %s)'%(max(0.05,4.635365-(d*0.050000)))
jesstemp72 ='jessatom9 x. %s'%(1.241240+(d*0.050000))
jesstemp72 = '('+jesstemp72+') and not (jessatom9 x. %s)'%(max(0.05,1.238761-(d*0.050000)))
jesstemp73 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(9.069060+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom10 x. %s)'%(max(0.05,9.050949-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(8.358350+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom10 x. %s)'%(max(0.05,8.341658-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(9.059050+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom10 x. %s)'%(max(0.05,9.040959-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(8.208200+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom10 x. %s)'%(max(0.05,8.191808-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(7.577570+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom10 x. %s)'%(max(0.05,7.562438-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(8.588580+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom10 x. %s)'%(max(0.05,8.571429-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(4.184180+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom10 x. %s)'%(max(0.05,4.175824-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(4.544540+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom10 x. %s)'%(max(0.05,4.535465-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.644640+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom10 x. %s)'%(max(0.05,4.635365-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom10 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
jesstemp74 ='jessatom0 x. %s'%(9.489480+(d*0.050000))
jesstemp74 = '('+jesstemp74+') and not (jessatom0 x. %s)'%(max(0.05,9.470529-(d*0.050000)))
jesstemp75 ='jessatom2 x. %s'%(9.759750+(d*0.050000))
jesstemp75 = '('+jesstemp75+') and not (jessatom2 x. %s)'%(max(0.05,9.740260-(d*0.050000)))
jesstemp76 ='jessatom3 x. %s'%(9.539530+(d*0.050000))
jesstemp76 = '('+jesstemp76+') and not (jessatom3 x. %s)'%(max(0.05,9.520480-(d*0.050000)))
jesstemp77 ='jessatom4 x. %s'%(8.738730+(d*0.050000))
jesstemp77 = '('+jesstemp77+') and not (jessatom4 x. %s)'%(max(0.05,8.721279-(d*0.050000)))
jesstemp78 ='jessatom5 x. %s'%(10.110100+(d*0.050000))
jesstemp78 = '('+jesstemp78+') and not (jessatom5 x. %s)'%(max(0.05,10.089910-(d*0.050000)))
jesstemp79 ='jessatom6 x. %s'%(5.685680+(d*0.050000))
jesstemp79 = '('+jesstemp79+') and not (jessatom6 x. %s)'%(max(0.05,5.674326-(d*0.050000)))
jesstemp80 ='jessatom7 x. %s'%(6.166160+(d*0.050000))
jesstemp80 = '('+jesstemp80+') and not (jessatom7 x. %s)'%(max(0.05,6.153846-(d*0.050000)))
jesstemp81 ='jessatom8 x. %s'%(6.586580+(d*0.050000))
jesstemp81 = '('+jesstemp81+') and not (jessatom8 x. %s)'%(max(0.05,6.573427-(d*0.050000)))
jesstemp82 ='jessatom9 x. %s'%(1.261260+(d*0.050000))
jesstemp82 = '('+jesstemp82+') and not (jessatom9 x. %s)'%(max(0.05,1.258741-(d*0.050000)))
jesstemp83 ='br. jessatom9'
jesstemp84 ='jessatom10 x. %s'%(2.182180+(d*0.050000))
jesstemp84 = '('+jesstemp84+') and not (jessatom10 x. %s)'%(max(0.05,2.177822-(d*0.050000)))
cmd.select('jessatom11', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp74+')&('+jesstemp46+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(9.489480+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom11 x. %s)'%(max(0.05,9.470529-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(8.608600+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom11 x. %s)'%(max(0.05,8.591409-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(9.759750+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom11 x. %s)'%(max(0.05,9.740260-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(9.539530+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom11 x. %s)'%(max(0.05,9.520480-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(8.738730+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom11 x. %s)'%(max(0.05,8.721279-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(10.110100+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom11 x. %s)'%(max(0.05,10.089910-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(5.685680+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom11 x. %s)'%(max(0.05,5.674326-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(6.166160+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom11 x. %s)'%(max(0.05,6.153846-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.586580+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom11 x. %s)'%(max(0.05,6.573427-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.261260+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom11 x. %s)'%(max(0.05,1.258741-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.182180+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom11 x. %s)'%(max(0.05,2.177822-(d*0.050000))))
cmd.select('Jfa_1ghr_3_2_1_73', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
