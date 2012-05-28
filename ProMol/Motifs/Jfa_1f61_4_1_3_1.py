'''
FUNC:Jfa_1f61_4_1_3_1
PDB:1f61
EC:4.1.3.1
RESI:his,cys,arg
LOCI:a-180,191,228;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.381380+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.378621-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.381380+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.378621-(d*0.050000))))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.212210+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.207792-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.142140+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,2.137862-(d*0.050000)))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.212210+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.207792-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.142140+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.137862-(d*0.050000))))
jesstemp10 ='n.  ca '
jesstemp11 ='r. cys'
jesstemp12 ='jessatom0 x. %s'%(23.523500+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom0 x. %s)'%(max(0.05,23.476523-(d*0.050000)))
jesstemp13 ='jessatom1 x. %s'%(22.172150+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom1 x. %s)'%(max(0.05,22.127872-(d*0.050000)))
jesstemp14 ='jessatom2 x. %s'%(22.652630+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom2 x. %s)'%(max(0.05,22.607393-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(23.523500+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,23.476523-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(22.172150+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,22.127872-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(22.652630+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,22.607393-(d*0.050000))))
jesstemp15 ='n.  cb '
jesstemp16 ='jessatom0 x. %s'%(24.074050+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,24.025974-(d*0.050000)))
jesstemp17 ='jessatom1 x. %s'%(22.722700+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom1 x. %s)'%(max(0.05,22.677323-(d*0.050000)))
jesstemp18 ='jessatom2 x. %s'%(23.113090+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom2 x. %s)'%(max(0.05,23.066933-(d*0.050000)))
jesstemp19 ='jessatom3 x. %s'%(1.541540+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom3 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(24.074050+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,24.025974-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(22.722700+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,22.677323-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(23.113090+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,23.066933-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp21 ='n.  sg '
jesstemp22 ='jessatom0 x. %s'%(23.063040+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom0 x. %s)'%(max(0.05,23.016983-(d*0.050000)))
jesstemp23 ='jessatom1 x. %s'%(21.701680+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom1 x. %s)'%(max(0.05,21.658342-(d*0.050000)))
jesstemp24 ='jessatom2 x. %s'%(22.072050+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom2 x. %s)'%(max(0.05,22.027972-(d*0.050000)))
jesstemp25 ='jessatom3 x. %s'%(2.792790+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom3 x. %s)'%(max(0.05,2.787213-(d*0.050000)))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.781780+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom4 x. %s)'%(max(0.05,1.778222-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(23.063040+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,23.016983-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(21.701680+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,21.658342-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(22.072050+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,22.027972-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.792790+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.787213-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.781780+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.778222-(d*0.050000))))
jesstemp28 ='n.  ne '
jesstemp29 ='r. arg'
jesstemp30 ='jessatom0 x. %s'%(6.986980+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom0 x. %s)'%(max(0.05,6.973027-(d*0.050000)))
jesstemp31 ='jessatom1 x. %s'%(5.955950+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom1 x. %s)'%(max(0.05,5.944056-(d*0.050000)))
jesstemp32 ='jessatom2 x. %s'%(6.886880+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom2 x. %s)'%(max(0.05,6.873127-(d*0.050000)))
jesstemp33 ='jessatom3 x. %s'%(17.627610+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom3 x. %s)'%(max(0.05,17.592408-(d*0.050000)))
jesstemp34 ='jessatom4 x. %s'%(18.428410+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom4 x. %s)'%(max(0.05,18.391608-(d*0.050000)))
jesstemp35 ='jessatom5 x. %s'%(17.737720+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom5 x. %s)'%(max(0.05,17.702298-(d*0.050000)))
cmd.select('jessatom6', '(('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.986980+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,6.973027-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.955950+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,5.944056-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.886880+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,6.873127-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(17.627610+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,17.592408-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(18.428410+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,18.391608-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(17.737720+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,17.702298-(d*0.050000))))
jesstemp36 ='n.  nh1'
jesstemp37 ='n.  nh2'
jesstemp38 ='jessatom0 x. %s'%(6.576570+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom0 x. %s)'%(max(0.05,6.563437-(d*0.050000)))
jesstemp39 ='jessatom1 x. %s'%(5.515510+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom1 x. %s)'%(max(0.05,5.504496-(d*0.050000)))
jesstemp40 ='jessatom2 x. %s'%(5.755750+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom2 x. %s)'%(max(0.05,5.744256-(d*0.050000)))
jesstemp41 ='jessatom3 x. %s'%(17.667650+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom3 x. %s)'%(max(0.05,17.632368-(d*0.050000)))
jesstemp42 ='jessatom4 x. %s'%(18.308290+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom4 x. %s)'%(max(0.05,18.271728-(d*0.050000)))
jesstemp43 ='jessatom5 x. %s'%(17.527510+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom5 x. %s)'%(max(0.05,17.492507-(d*0.050000)))
jesstemp44 ='jessatom6 x. %s'%(2.322320+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom6 x. %s)'%(max(0.05,2.317682-(d*0.050000)))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp36+')|('+jesstemp37+'))&('+jesstemp29+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.576570+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,6.563437-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.515510+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,5.504496-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.755750+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,5.744256-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(17.667650+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,17.632368-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(18.308290+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,18.271728-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(17.527510+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,17.492507-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.322320+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,2.317682-(d*0.050000))))
jesstemp46 ='n.  nh2'
jesstemp47 ='n.  nh1'
jesstemp48 ='jessatom0 x. %s'%(8.518510+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom0 x. %s)'%(max(0.05,8.501499-(d*0.050000)))
jesstemp49 ='jessatom1 x. %s'%(7.347340+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom1 x. %s)'%(max(0.05,7.332667-(d*0.050000)))
jesstemp50 ='jessatom2 x. %s'%(7.907900+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom2 x. %s)'%(max(0.05,7.892108-(d*0.050000)))
jesstemp51 ='jessatom3 x. %s'%(15.605590+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom3 x. %s)'%(max(0.05,15.574426-(d*0.050000)))
jesstemp52 ='jessatom4 x. %s'%(16.336320+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom4 x. %s)'%(max(0.05,16.303696-(d*0.050000)))
jesstemp53 ='jessatom5 x. %s'%(15.645630+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom5 x. %s)'%(max(0.05,15.614386-(d*0.050000)))
jesstemp54 ='br. jessatom6'
jesstemp55 ='jessatom7 x. %s'%(2.322320+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom7 x. %s)'%(max(0.05,2.317682-(d*0.050000)))
cmd.select('jessatom8', '((('+jesstemp46+')|('+jesstemp47+'))&('+jesstemp29+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp44+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.518510+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,8.501499-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.347340+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,7.332667-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.907900+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,7.892108-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(15.605590+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,15.574426-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(16.336320+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,16.303696-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(15.645630+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,15.614386-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.322320+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.317682-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.322320+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.317682-(d*0.050000))))
cmd.select('Jfa_1f61_4_1_3_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
