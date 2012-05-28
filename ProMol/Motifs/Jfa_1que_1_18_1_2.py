'''
FUNC:Jfa_1que_1_18_1_2
PDB:1que
EC:1.18.1.2
RESI:ser,cys,glu
LOCI:a-80,261,301;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.521520+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.518482-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.521520+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.518482-(d*0.050000))))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.422420+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.417582-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.411410+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,1.408591-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.422420+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.417582-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.411410+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,1.408591-(d*0.050000))))
jesstemp10 ='r. cys'
jesstemp11 ='jessatom0 x. %s'%(9.539530+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom0 x. %s)'%(max(0.05,9.520480-(d*0.050000)))
jesstemp12 ='jessatom1 x. %s'%(8.158150+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom1 x. %s)'%(max(0.05,8.141858-(d*0.050000)))
jesstemp13 ='jessatom2 x. %s'%(7.187180+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom2 x. %s)'%(max(0.05,7.172827-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.539530+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,9.520480-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.158150+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,8.141858-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.187180+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,7.172827-(d*0.050000))))
jesstemp14 ='jessatom0 x. %s'%(8.338330+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom0 x. %s)'%(max(0.05,8.321678-(d*0.050000)))
jesstemp15 ='jessatom1 x. %s'%(6.916910+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom1 x. %s)'%(max(0.05,6.903097-(d*0.050000)))
jesstemp16 ='jessatom2 x. %s'%(6.066060+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom2 x. %s)'%(max(0.05,6.053946-(d*0.050000)))
jesstemp17 ='jessatom3 x. %s'%(1.531530+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom3 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp18 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp3+')&('+jesstemp10+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.338330+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,8.321678-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.916910+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,6.903097-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.066060+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,6.053946-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp19 ='n.  sg '
jesstemp20 ='jessatom0 x. %s'%(6.736730+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom0 x. %s)'%(max(0.05,6.723277-(d*0.050000)))
jesstemp21 ='jessatom1 x. %s'%(5.365360+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom1 x. %s)'%(max(0.05,5.354645-(d*0.050000)))
jesstemp22 ='jessatom2 x. %s'%(4.384380+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom2 x. %s)'%(max(0.05,4.375624-(d*0.050000)))
jesstemp23 ='jessatom3 x. %s'%(2.802800+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom3 x. %s)'%(max(0.05,2.797203-(d*0.050000)))
jesstemp24 ='br. jessatom3'
jesstemp25 ='jessatom4 x. %s'%(1.811810+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom4 x. %s)'%(max(0.05,1.808192-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp19+')&('+jesstemp10+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.736730+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,6.723277-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.365360+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,5.354645-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.384380+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,4.375624-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.802800+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.797203-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.811810+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.808192-(d*0.050000))))
jesstemp26 ='n.  cd '
jesstemp27 ='r. glu'
jesstemp28 ='r. asp'
jesstemp29 ='jessatom0 x. %s'%(5.715710+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom0 x. %s)'%(max(0.05,5.704296-(d*0.050000)))
jesstemp30 ='jessatom1 x. %s'%(5.175170+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom1 x. %s)'%(max(0.05,5.164835-(d*0.050000)))
jesstemp31 ='jessatom2 x. %s'%(4.074070+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom2 x. %s)'%(max(0.05,4.065934-(d*0.050000)))
jesstemp32 ='jessatom3 x. %s'%(6.406400+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom3 x. %s)'%(max(0.05,6.393606-(d*0.050000)))
jesstemp33 ='jessatom4 x. %s'%(5.705700+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom4 x. %s)'%(max(0.05,5.694306-(d*0.050000)))
jesstemp34 ='jessatom5 x. %s'%(4.474470+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom5 x. %s)'%(max(0.05,4.465534-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp26+')&('+jesstemp27+'))|(('+jesstemp26+')&('+jesstemp28+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.715710+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,5.704296-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.175170+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,5.164835-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.074070+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,4.065934-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.406400+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,6.393606-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.705700+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,5.694306-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.474470+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,4.465534-(d*0.050000))))
jesstemp35 ='n.  oe1'
jesstemp36 ='n.  oe2'
jesstemp37 ='n.  od1'
jesstemp38 ='n.  od2'
jesstemp39 ='jessatom0 x. %s'%(5.925920+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom0 x. %s)'%(max(0.05,5.914086-(d*0.050000)))
jesstemp40 ='jessatom1 x. %s'%(5.575570+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom1 x. %s)'%(max(0.05,5.564436-(d*0.050000)))
jesstemp41 ='jessatom2 x. %s'%(4.704700+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom2 x. %s)'%(max(0.05,4.695305-(d*0.050000)))
jesstemp42 ='jessatom3 x. %s'%(7.357350+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom3 x. %s)'%(max(0.05,7.342657-(d*0.050000)))
jesstemp43 ='jessatom4 x. %s'%(6.586580+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom4 x. %s)'%(max(0.05,6.573427-(d*0.050000)))
jesstemp44 ='jessatom5 x. %s'%(5.495490+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom5 x. %s)'%(max(0.05,5.484515-(d*0.050000)))
jesstemp45 ='jessatom6 x. %s'%(1.251250+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom6 x. %s)'%(max(0.05,1.248751-(d*0.050000)))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp35+')|('+jesstemp36+'))&('+jesstemp27+'))|((('+jesstemp37+')|('+jesstemp38+'))&('+jesstemp28+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.925920+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,5.914086-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.575570+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,5.564436-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.704700+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,4.695305-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.357350+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,7.342657-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.586580+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,6.573427-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.495490+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,5.484515-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
jesstemp47 ='n.  oe2'
jesstemp48 ='n.  oe1'
jesstemp49 ='n.  od2'
jesstemp50 ='n.  od1'
jesstemp51 ='jessatom0 x. %s'%(4.694690+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom0 x. %s)'%(max(0.05,4.685315-(d*0.050000)))
jesstemp52 ='jessatom1 x. %s'%(4.024020+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom1 x. %s)'%(max(0.05,4.015984-(d*0.050000)))
jesstemp53 ='jessatom2 x. %s'%(2.852850+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom2 x. %s)'%(max(0.05,2.847153-(d*0.050000)))
jesstemp54 ='jessatom3 x. %s'%(6.196190+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom3 x. %s)'%(max(0.05,6.183816-(d*0.050000)))
jesstemp55 ='jessatom4 x. %s'%(5.345340+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom4 x. %s)'%(max(0.05,5.334665-(d*0.050000)))
jesstemp56 ='jessatom5 x. %s'%(3.863860+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom5 x. %s)'%(max(0.05,3.856144-(d*0.050000)))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.202200+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom7 x. %s)'%(max(0.05,2.197802-(d*0.050000)))
cmd.select('jessatom8', '((((('+jesstemp47+')|('+jesstemp48+'))&('+jesstemp27+'))|((('+jesstemp49+')|('+jesstemp50+'))&('+jesstemp28+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp45+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.694690+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,4.685315-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.024020+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,4.015984-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(2.852850+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,2.847153-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.196190+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,6.183816-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.345340+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,5.334665-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.863860+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,3.856144-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.202200+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.197802-(d*0.050000))))
cmd.select('Jfa_1que_1_18_1_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
