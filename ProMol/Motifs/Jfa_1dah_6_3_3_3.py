'''
FUNC:Jfa_1dah_6_3_3_3
PDB:1dah
EC:6.3.3.3
RESI:thr,lys,lys,ser
LOCI:a-11,15,37,41;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. thr'
jesstemp2 ='r. ser'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.581580+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.578422-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.581580+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.578422-(d*0.050000))))
jesstemp6 ='n.  og1'
jesstemp7 ='jessatom0 x. %s'%(2.452450+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.447552-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.451450+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,1.448551-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.452450+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.447552-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.451450+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,1.448551-(d*0.050000))))
jesstemp10 ='n.  cd '
jesstemp11 ='r. lys'
jesstemp12 ='jessatom0 x. %s'%(6.586580+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom0 x. %s)'%(max(0.05,6.573427-(d*0.050000)))
jesstemp13 ='jessatom1 x. %s'%(7.657650+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom1 x. %s)'%(max(0.05,7.642358-(d*0.050000)))
jesstemp14 ='jessatom2 x. %s'%(7.647640+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom2 x. %s)'%(max(0.05,7.632368-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.586580+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,6.573427-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.657650+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,7.642358-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.647640+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,7.632368-(d*0.050000))))
jesstemp15 ='n.  ce '
jesstemp16 ='jessatom0 x. %s'%(5.855850+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,5.844156-(d*0.050000)))
jesstemp17 ='jessatom1 x. %s'%(6.716710+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom1 x. %s)'%(max(0.05,6.703297-(d*0.050000)))
jesstemp18 ='jessatom2 x. %s'%(6.486480+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom2 x. %s)'%(max(0.05,6.473526-(d*0.050000)))
jesstemp19 ='jessatom3 x. %s'%(1.551550+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom3 x. %s)'%(max(0.05,1.548452-(d*0.050000)))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.855850+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,5.844156-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.716710+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,6.703297-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.486480+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,6.473526-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.551550+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.548452-(d*0.050000))))
jesstemp21 ='n.  nz '
jesstemp22 ='jessatom0 x. %s'%(4.404400+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom0 x. %s)'%(max(0.05,4.395604-(d*0.050000)))
jesstemp23 ='jessatom1 x. %s'%(5.335330+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom1 x. %s)'%(max(0.05,5.324675-(d*0.050000)))
jesstemp24 ='jessatom2 x. %s'%(5.195190+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom2 x. %s)'%(max(0.05,5.184815-(d*0.050000)))
jesstemp25 ='jessatom3 x. %s'%(2.472470+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom3 x. %s)'%(max(0.05,2.467532-(d*0.050000)))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.471470+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom4 x. %s)'%(max(0.05,1.468531-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.404400+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,4.395604-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.335330+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,5.324675-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.195190+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,5.184815-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.472470+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.467532-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.471470+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.468531-(d*0.050000))))
jesstemp28 ='jessatom0 x. %s'%(11.341330+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom0 x. %s)'%(max(0.05,11.318681-(d*0.050000)))
jesstemp29 ='jessatom1 x. %s'%(11.481470+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom1 x. %s)'%(max(0.05,11.458541-(d*0.050000)))
jesstemp30 ='jessatom2 x. %s'%(10.560550+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom2 x. %s)'%(max(0.05,10.539461-(d*0.050000)))
jesstemp31 ='jessatom3 x. %s'%(7.677670+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom3 x. %s)'%(max(0.05,7.662338-(d*0.050000)))
jesstemp32 ='jessatom4 x. %s'%(6.776770+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom4 x. %s)'%(max(0.05,6.763237-(d*0.050000)))
jesstemp33 ='jessatom5 x. %s'%(7.777770+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom5 x. %s)'%(max(0.05,7.762238-(d*0.050000)))
cmd.select('jessatom6', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.341330+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,11.318681-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.481470+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,11.458541-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.560550+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,10.539461-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.677670+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,7.662338-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.776770+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,6.763237-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.777770+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,7.762238-(d*0.050000))))
jesstemp34 ='jessatom0 x. %s'%(10.280270+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom0 x. %s)'%(max(0.05,10.259740-(d*0.050000)))
jesstemp35 ='jessatom1 x. %s'%(10.270260+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom1 x. %s)'%(max(0.05,10.249750-(d*0.050000)))
jesstemp36 ='jessatom2 x. %s'%(9.289280+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom2 x. %s)'%(max(0.05,9.270729-(d*0.050000)))
jesstemp37 ='jessatom3 x. %s'%(7.487480+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom3 x. %s)'%(max(0.05,7.472527-(d*0.050000)))
jesstemp38 ='jessatom4 x. %s'%(6.336330+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom4 x. %s)'%(max(0.05,6.323676-(d*0.050000)))
jesstemp39 ='jessatom5 x. %s'%(7.117110+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom5 x. %s)'%(max(0.05,7.102897-(d*0.050000)))
jesstemp40 ='jessatom6 x. %s'%(1.551550+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom6 x. %s)'%(max(0.05,1.548452-(d*0.050000)))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.280270+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,10.259740-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(10.270260+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,10.249750-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.289280+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,9.270729-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.487480+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,7.472527-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.336330+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,6.323676-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.117110+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,7.102897-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.551550+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.548452-(d*0.050000))))
jesstemp42 ='jessatom0 x. %s'%(8.938930+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom0 x. %s)'%(max(0.05,8.921079-(d*0.050000)))
jesstemp43 ='jessatom1 x. %s'%(9.029020+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom1 x. %s)'%(max(0.05,9.010989-(d*0.050000)))
jesstemp44 ='jessatom2 x. %s'%(8.118110+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom2 x. %s)'%(max(0.05,8.101898-(d*0.050000)))
jesstemp45 ='jessatom3 x. %s'%(6.136130+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom3 x. %s)'%(max(0.05,6.123876-(d*0.050000)))
jesstemp46 ='jessatom4 x. %s'%(4.924920+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom4 x. %s)'%(max(0.05,4.915085-(d*0.050000)))
jesstemp47 ='jessatom5 x. %s'%(5.665660+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom5 x. %s)'%(max(0.05,5.654346-(d*0.050000)))
jesstemp48 ='jessatom6 x. %s'%(2.452450+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom6 x. %s)'%(max(0.05,2.447552-(d*0.050000)))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(1.461460+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom7 x. %s)'%(max(0.05,1.458541-(d*0.050000)))
cmd.select('jessatom8', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.938930+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,8.921079-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.029020+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,9.010989-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.118110+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,8.101898-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.136130+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,6.123876-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.924920+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,4.915085-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.665660+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,5.654346-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.452450+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.447552-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.461460+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,1.458541-(d*0.050000))))
jesstemp51 ='jessatom0 x. %s'%(11.921910+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom0 x. %s)'%(max(0.05,11.898102-(d*0.050000)))
jesstemp52 ='jessatom1 x. %s'%(10.950940+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom1 x. %s)'%(max(0.05,10.929071-(d*0.050000)))
jesstemp53 ='jessatom2 x. %s'%(9.789780+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom2 x. %s)'%(max(0.05,9.770230-(d*0.050000)))
jesstemp54 ='jessatom3 x. %s'%(12.822810+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom3 x. %s)'%(max(0.05,12.797203-(d*0.050000)))
jesstemp55 ='jessatom4 x. %s'%(11.331320+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom4 x. %s)'%(max(0.05,11.308691-(d*0.050000)))
jesstemp56 ='jessatom5 x. %s'%(11.281270+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom5 x. %s)'%(max(0.05,11.258741-(d*0.050000)))
jesstemp57 ='jessatom6 x. %s'%(8.448440+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom6 x. %s)'%(max(0.05,8.431568-(d*0.050000)))
jesstemp58 ='jessatom7 x. %s'%(7.117110+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom7 x. %s)'%(max(0.05,7.102897-(d*0.050000)))
jesstemp59 ='jessatom8 x. %s'%(7.627620+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom8 x. %s)'%(max(0.05,7.612388-(d*0.050000)))
cmd.select('jessatom9', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(11.921910+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom9 x. %s)'%(max(0.05,11.898102-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(10.950940+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom9 x. %s)'%(max(0.05,10.929071-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(9.789780+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom9 x. %s)'%(max(0.05,9.770230-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(12.822810+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom9 x. %s)'%(max(0.05,12.797203-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(11.331320+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom9 x. %s)'%(max(0.05,11.308691-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(11.281270+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom9 x. %s)'%(max(0.05,11.258741-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(8.448440+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom9 x. %s)'%(max(0.05,8.431568-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(7.117110+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom9 x. %s)'%(max(0.05,7.102897-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(7.627620+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom9 x. %s)'%(max(0.05,7.612388-(d*0.050000))))
jesstemp60 ='jessatom0 x. %s'%(11.411400+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom0 x. %s)'%(max(0.05,11.388611-(d*0.050000)))
jesstemp61 ='jessatom1 x. %s'%(10.320310+(d*0.050000))
jesstemp61 = '('+jesstemp61+') and not (jessatom1 x. %s)'%(max(0.05,10.299700-(d*0.050000)))
jesstemp62 ='jessatom2 x. %s'%(9.279270+(d*0.050000))
jesstemp62 = '('+jesstemp62+') and not (jessatom2 x. %s)'%(max(0.05,9.260739-(d*0.050000)))
jesstemp63 ='jessatom3 x. %s'%(12.782770+(d*0.050000))
jesstemp63 = '('+jesstemp63+') and not (jessatom3 x. %s)'%(max(0.05,12.757243-(d*0.050000)))
jesstemp64 ='jessatom4 x. %s'%(11.311300+(d*0.050000))
jesstemp64 = '('+jesstemp64+') and not (jessatom4 x. %s)'%(max(0.05,11.288711-(d*0.050000)))
jesstemp65 ='jessatom5 x. %s'%(11.151140+(d*0.050000))
jesstemp65 = '('+jesstemp65+') and not (jessatom5 x. %s)'%(max(0.05,11.128871-(d*0.050000)))
jesstemp66 ='jessatom6 x. %s'%(9.179170+(d*0.050000))
jesstemp66 = '('+jesstemp66+') and not (jessatom6 x. %s)'%(max(0.05,9.160839-(d*0.050000)))
jesstemp67 ='jessatom7 x. %s'%(7.777770+(d*0.050000))
jesstemp67 = '('+jesstemp67+') and not (jessatom7 x. %s)'%(max(0.05,7.762238-(d*0.050000)))
jesstemp68 ='jessatom8 x. %s'%(8.098090+(d*0.050000))
jesstemp68 = '('+jesstemp68+') and not (jessatom8 x. %s)'%(max(0.05,8.081918-(d*0.050000)))
jesstemp69 ='jessatom9 x. %s'%(1.531530+(d*0.050000))
jesstemp69 = '('+jesstemp69+') and not (jessatom9 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp70 ='br. jessatom9'
cmd.select('jessatom10', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(11.411400+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom10 x. %s)'%(max(0.05,11.388611-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(10.320310+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom10 x. %s)'%(max(0.05,10.299700-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(9.279270+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom10 x. %s)'%(max(0.05,9.260739-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(12.782770+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom10 x. %s)'%(max(0.05,12.757243-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(11.311300+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom10 x. %s)'%(max(0.05,11.288711-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(11.151140+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom10 x. %s)'%(max(0.05,11.128871-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(9.179170+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom10 x. %s)'%(max(0.05,9.160839-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(7.777770+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom10 x. %s)'%(max(0.05,7.762238-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(8.098090+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom10 x. %s)'%(max(0.05,8.081918-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom10 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp71 ='n.  og '
jesstemp72 ='jessatom0 x. %s'%(9.989980+(d*0.050000))
jesstemp72 = '('+jesstemp72+') and not (jessatom0 x. %s)'%(max(0.05,9.970030-(d*0.050000)))
jesstemp73 ='jessatom1 x. %s'%(8.898890+(d*0.050000))
jesstemp73 = '('+jesstemp73+') and not (jessatom1 x. %s)'%(max(0.05,8.881119-(d*0.050000)))
jesstemp74 ='jessatom2 x. %s'%(7.877870+(d*0.050000))
jesstemp74 = '('+jesstemp74+') and not (jessatom2 x. %s)'%(max(0.05,7.862138-(d*0.050000)))
jesstemp75 ='jessatom3 x. %s'%(11.631620+(d*0.050000))
jesstemp75 = '('+jesstemp75+') and not (jessatom3 x. %s)'%(max(0.05,11.608392-(d*0.050000)))
jesstemp76 ='jessatom4 x. %s'%(10.150140+(d*0.050000))
jesstemp76 = '('+jesstemp76+') and not (jessatom4 x. %s)'%(max(0.05,10.129870-(d*0.050000)))
jesstemp77 ='jessatom5 x. %s'%(9.899890+(d*0.050000))
jesstemp77 = '('+jesstemp77+') and not (jessatom5 x. %s)'%(max(0.05,9.880120-(d*0.050000)))
jesstemp78 ='jessatom6 x. %s'%(8.818810+(d*0.050000))
jesstemp78 = '('+jesstemp78+') and not (jessatom6 x. %s)'%(max(0.05,8.801199-(d*0.050000)))
jesstemp79 ='jessatom7 x. %s'%(7.327320+(d*0.050000))
jesstemp79 = '('+jesstemp79+') and not (jessatom7 x. %s)'%(max(0.05,7.312687-(d*0.050000)))
jesstemp80 ='jessatom8 x. %s'%(7.397390+(d*0.050000))
jesstemp80 = '('+jesstemp80+') and not (jessatom8 x. %s)'%(max(0.05,7.382617-(d*0.050000)))
jesstemp81 ='jessatom9 x. %s'%(2.492490+(d*0.050000))
jesstemp81 = '('+jesstemp81+') and not (jessatom9 x. %s)'%(max(0.05,2.487512-(d*0.050000)))
jesstemp82 ='br. jessatom9'
jesstemp83 ='jessatom10 x. %s'%(1.431430+(d*0.050000))
jesstemp83 = '('+jesstemp83+') and not (jessatom10 x. %s)'%(max(0.05,1.428571-(d*0.050000)))
cmd.select('jessatom11', '(((('+jesstemp71+')&('+jesstemp2+'))|(('+jesstemp71+')&('+jesstemp1+')))&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(9.989980+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom11 x. %s)'%(max(0.05,9.970030-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(8.898890+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom11 x. %s)'%(max(0.05,8.881119-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(7.877870+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom11 x. %s)'%(max(0.05,7.862138-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(11.631620+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom11 x. %s)'%(max(0.05,11.608392-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(10.150140+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom11 x. %s)'%(max(0.05,10.129870-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(9.899890+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom11 x. %s)'%(max(0.05,9.880120-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(8.818810+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom11 x. %s)'%(max(0.05,8.801199-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.327320+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom11 x. %s)'%(max(0.05,7.312687-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(7.397390+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom11 x. %s)'%(max(0.05,7.382617-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.492490+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom11 x. %s)'%(max(0.05,2.487512-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.431430+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom11 x. %s)'%(max(0.05,1.428571-(d*0.050000))))
cmd.select('Jfa_1dah_6_3_3_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
