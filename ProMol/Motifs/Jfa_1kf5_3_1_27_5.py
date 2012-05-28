'''
FUNC:Jfa_1kf5_3_1_27_5
PDB:1kf5
EC:3.1.27.5
RESI:his,lys,his,phe
LOCI:a-12,41,119,120;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.371370+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.368631-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.371370+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.368631-(d*0.050000))))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.222220+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.217782-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.182180+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,2.177822-(d*0.050000)))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222220+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.217782-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.182180+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.177822-(d*0.050000))))
jesstemp10 ='n.  cd '
jesstemp11 ='r. lys'
jesstemp12 ='jessatom0 x. %s'%(8.178170+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom0 x. %s)'%(max(0.05,8.161838-(d*0.050000)))
jesstemp13 ='jessatom1 x. %s'%(7.307300+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom1 x. %s)'%(max(0.05,7.292707-(d*0.050000)))
jesstemp14 ='jessatom2 x. %s'%(6.936930+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom2 x. %s)'%(max(0.05,6.923077-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.178170+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,8.161838-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.307300+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,7.292707-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.936930+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,6.923077-(d*0.050000))))
jesstemp15 ='n.  ce '
jesstemp16 ='jessatom0 x. %s'%(7.537530+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,7.522478-(d*0.050000)))
jesstemp17 ='jessatom1 x. %s'%(6.666660+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom1 x. %s)'%(max(0.05,6.653347-(d*0.050000)))
jesstemp18 ='jessatom2 x. %s'%(5.995990+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom2 x. %s)'%(max(0.05,5.984016-(d*0.050000)))
jesstemp19 ='jessatom3 x. %s'%(1.531530+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom3 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.537530+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,7.522478-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.666660+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,6.653347-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.995990+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,5.984016-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp21 ='n.  nz '
jesstemp22 ='jessatom0 x. %s'%(6.056050+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom0 x. %s)'%(max(0.05,6.043956-(d*0.050000)))
jesstemp23 ='jessatom1 x. %s'%(5.225220+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom1 x. %s)'%(max(0.05,5.214785-(d*0.050000)))
jesstemp24 ='jessatom2 x. %s'%(4.544540+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom2 x. %s)'%(max(0.05,4.535465-(d*0.050000)))
jesstemp25 ='jessatom3 x. %s'%(2.502500+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom3 x. %s)'%(max(0.05,2.497502-(d*0.050000)))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.481480+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom4 x. %s)'%(max(0.05,1.478521-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.056050+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,6.043956-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.225220+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,5.214785-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.544540+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,4.535465-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.502500+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.497502-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.481480+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.478521-(d*0.050000))))
jesstemp28 ='jessatom0 x. %s'%(8.378370+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom0 x. %s)'%(max(0.05,8.361638-(d*0.050000)))
jesstemp29 ='jessatom1 x. %s'%(8.498490+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom1 x. %s)'%(max(0.05,8.481518-(d*0.050000)))
jesstemp30 ='jessatom2 x. %s'%(6.766760+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom2 x. %s)'%(max(0.05,6.753247-(d*0.050000)))
jesstemp31 ='jessatom3 x. %s'%(11.371360+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom3 x. %s)'%(max(0.05,11.348651-(d*0.050000)))
jesstemp32 ='jessatom4 x. %s'%(9.899890+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom4 x. %s)'%(max(0.05,9.880120-(d*0.050000)))
jesstemp33 ='jessatom5 x. %s'%(9.079070+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom5 x. %s)'%(max(0.05,9.060939-(d*0.050000)))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.378370+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,8.361638-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.498490+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,8.481518-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.766760+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,6.753247-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.371360+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,11.348651-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.899890+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,9.880120-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.079070+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,9.060939-(d*0.050000))))
jesstemp34 ='jessatom0 x. %s'%(8.308300+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom0 x. %s)'%(max(0.05,8.291708-(d*0.050000)))
jesstemp35 ='jessatom1 x. %s'%(8.268260+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom1 x. %s)'%(max(0.05,8.251748-(d*0.050000)))
jesstemp36 ='jessatom2 x. %s'%(6.466460+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom2 x. %s)'%(max(0.05,6.453546-(d*0.050000)))
jesstemp37 ='jessatom3 x. %s'%(10.320310+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom3 x. %s)'%(max(0.05,10.299700-(d*0.050000)))
jesstemp38 ='jessatom4 x. %s'%(8.828820+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom4 x. %s)'%(max(0.05,8.811189-(d*0.050000)))
jesstemp39 ='jessatom5 x. %s'%(8.128120+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom5 x. %s)'%(max(0.05,8.111888-(d*0.050000)))
jesstemp40 ='jessatom6 x. %s'%(1.341340+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom6 x. %s)'%(max(0.05,1.338661-(d*0.050000)))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.308300+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,8.291708-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.268260+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,8.251748-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.466460+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,6.453546-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.320310+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,10.299700-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.828820+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,8.811189-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.128120+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,8.111888-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.341340+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.338661-(d*0.050000))))
jesstemp42 ='jessatom0 x. %s'%(9.349340+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom0 x. %s)'%(max(0.05,9.330669-(d*0.050000)))
jesstemp43 ='jessatom1 x. %s'%(9.179170+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom1 x. %s)'%(max(0.05,9.160839-(d*0.050000)))
jesstemp44 ='jessatom2 x. %s'%(7.717710+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom2 x. %s)'%(max(0.05,7.702298-(d*0.050000)))
jesstemp45 ='jessatom3 x. %s'%(11.611600+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom3 x. %s)'%(max(0.05,11.588412-(d*0.050000)))
jesstemp46 ='jessatom4 x. %s'%(10.090080+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom4 x. %s)'%(max(0.05,10.069930-(d*0.050000)))
jesstemp47 ='jessatom5 x. %s'%(9.439430+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom5 x. %s)'%(max(0.05,9.420579-(d*0.050000)))
jesstemp48 ='jessatom6 x. %s'%(2.192190+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom6 x. %s)'%(max(0.05,2.187812-(d*0.050000)))
jesstemp49 ='br. jessatom6'
jesstemp50 ='jessatom7 x. %s'%(2.132130+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom7 x. %s)'%(max(0.05,2.127872-(d*0.050000)))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.349340+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,9.330669-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.179170+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,9.160839-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(7.717710+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,7.702298-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(11.611600+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,11.588412-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(10.090080+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,10.069930-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.439430+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,9.420579-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.192190+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.187812-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.132130+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.127872-(d*0.050000))))
jesstemp51 ='n.  n  '
jesstemp52 ='jessatom0 x. %s'%(5.365360+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom0 x. %s)'%(max(0.05,5.354645-(d*0.050000)))
jesstemp53 ='jessatom1 x. %s'%(5.565560+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom1 x. %s)'%(max(0.05,5.554446-(d*0.050000)))
jesstemp54 ='jessatom2 x. %s'%(4.244240+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom2 x. %s)'%(max(0.05,4.235764-(d*0.050000)))
jesstemp55 ='jessatom3 x. %s'%(10.240230+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom3 x. %s)'%(max(0.05,10.219780-(d*0.050000)))
jesstemp56 ='jessatom4 x. %s'%(8.938930+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom4 x. %s)'%(max(0.05,8.921079-(d*0.050000)))
jesstemp57 ='jessatom5 x. %s'%(7.757750+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom5 x. %s)'%(max(0.05,7.742258-(d*0.050000)))
jesstemp58 ='jessatom6 x. %s'%(3.323320+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom6 x. %s)'%(max(0.05,3.316683-(d*0.050000)))
jesstemp59 ='jessatom7 x. %s'%(3.723720+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom7 x. %s)'%(max(0.05,3.716284-(d*0.050000)))
jesstemp60 ='jessatom8 x. %s'%(4.344340+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom8 x. %s)'%(max(0.05,4.335664-(d*0.050000)))
cmd.select('jessatom9', '(('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.365360+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom9 x. %s)'%(max(0.05,5.354645-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(5.565560+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom9 x. %s)'%(max(0.05,5.554446-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(4.244240+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom9 x. %s)'%(max(0.05,4.235764-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(10.240230+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom9 x. %s)'%(max(0.05,10.219780-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(8.938930+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom9 x. %s)'%(max(0.05,8.921079-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.757750+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom9 x. %s)'%(max(0.05,7.742258-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(3.323320+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom9 x. %s)'%(max(0.05,3.316683-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(3.723720+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom9 x. %s)'%(max(0.05,3.716284-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(4.344340+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom9 x. %s)'%(max(0.05,4.335664-(d*0.050000))))
jesstemp61 ='n.  ca '
jesstemp62 ='jessatom0 x. %s'%(5.325320+(d*0.050000))
jesstemp62 = '('+jesstemp62+') and not (jessatom0 x. %s)'%(max(0.05,5.314685-(d*0.050000)))
jesstemp63 ='jessatom1 x. %s'%(5.325320+(d*0.050000))
jesstemp63 = '('+jesstemp63+') and not (jessatom1 x. %s)'%(max(0.05,5.314685-(d*0.050000)))
jesstemp64 ='jessatom3 x. %s'%(10.480470+(d*0.050000))
jesstemp64 = '('+jesstemp64+') and not (jessatom3 x. %s)'%(max(0.05,10.459540-(d*0.050000)))
jesstemp65 ='jessatom4 x. %s'%(9.199190+(d*0.050000))
jesstemp65 = '('+jesstemp65+') and not (jessatom4 x. %s)'%(max(0.05,9.180819-(d*0.050000)))
jesstemp66 ='jessatom5 x. %s'%(8.008000+(d*0.050000))
jesstemp66 = '('+jesstemp66+') and not (jessatom5 x. %s)'%(max(0.05,7.992008-(d*0.050000)))
jesstemp67 ='jessatom6 x. %s'%(4.324320+(d*0.050000))
jesstemp67 = '('+jesstemp67+') and not (jessatom6 x. %s)'%(max(0.05,4.315684-(d*0.050000)))
jesstemp68 ='jessatom7 x. %s'%(4.664660+(d*0.050000))
jesstemp68 = '('+jesstemp68+') and not (jessatom7 x. %s)'%(max(0.05,4.655345-(d*0.050000)))
jesstemp69 ='jessatom8 x. %s'%(4.724720+(d*0.050000))
jesstemp69 = '('+jesstemp69+') and not (jessatom8 x. %s)'%(max(0.05,4.715285-(d*0.050000)))
jesstemp70 ='jessatom9 x. %s'%(1.481480+(d*0.050000))
jesstemp70 = '('+jesstemp70+') and not (jessatom9 x. %s)'%(max(0.05,1.478521-(d*0.050000)))
jesstemp71 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp24+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(5.325320+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom10 x. %s)'%(max(0.05,5.314685-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(5.325320+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom10 x. %s)'%(max(0.05,5.314685-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(4.544540+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom10 x. %s)'%(max(0.05,4.535465-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(10.480470+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom10 x. %s)'%(max(0.05,10.459540-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(9.199190+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom10 x. %s)'%(max(0.05,9.180819-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(8.008000+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom10 x. %s)'%(max(0.05,7.992008-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(4.324320+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom10 x. %s)'%(max(0.05,4.315684-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(4.664660+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom10 x. %s)'%(max(0.05,4.655345-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(4.724720+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom10 x. %s)'%(max(0.05,4.715285-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.481480+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom10 x. %s)'%(max(0.05,1.478521-(d*0.050000))))
jesstemp72 ='n.  c  '
jesstemp73 ='jessatom0 x. %s'%(6.506500+(d*0.050000))
jesstemp73 = '('+jesstemp73+') and not (jessatom0 x. %s)'%(max(0.05,6.493506-(d*0.050000)))
jesstemp74 ='jessatom1 x. %s'%(6.256250+(d*0.050000))
jesstemp74 = '('+jesstemp74+') and not (jessatom1 x. %s)'%(max(0.05,6.243756-(d*0.050000)))
jesstemp75 ='jessatom2 x. %s'%(5.475470+(d*0.050000))
jesstemp75 = '('+jesstemp75+') and not (jessatom2 x. %s)'%(max(0.05,5.464535-(d*0.050000)))
jesstemp76 ='jessatom3 x. %s'%(10.580570+(d*0.050000))
jesstemp76 = '('+jesstemp76+') and not (jessatom3 x. %s)'%(max(0.05,10.559441-(d*0.050000)))
jesstemp77 ='jessatom4 x. %s'%(9.229220+(d*0.050000))
jesstemp77 = '('+jesstemp77+') and not (jessatom4 x. %s)'%(max(0.05,9.210789-(d*0.050000)))
jesstemp78 ='jessatom5 x. %s'%(8.198190+(d*0.050000))
jesstemp78 = '('+jesstemp78+') and not (jessatom5 x. %s)'%(max(0.05,8.181818-(d*0.050000)))
jesstemp79 ='jessatom6 x. %s'%(4.084080+(d*0.050000))
jesstemp79 = '('+jesstemp79+') and not (jessatom6 x. %s)'%(max(0.05,4.075924-(d*0.050000)))
jesstemp80 ='jessatom7 x. %s'%(4.244240+(d*0.050000))
jesstemp80 = '('+jesstemp80+') and not (jessatom7 x. %s)'%(max(0.05,4.235764-(d*0.050000)))
jesstemp81 ='jessatom8 x. %s'%(3.763760+(d*0.050000))
jesstemp81 = '('+jesstemp81+') and not (jessatom8 x. %s)'%(max(0.05,3.756244-(d*0.050000)))
jesstemp82 ='jessatom9 x. %s'%(2.422420+(d*0.050000))
jesstemp82 = '('+jesstemp82+') and not (jessatom9 x. %s)'%(max(0.05,2.417582-(d*0.050000)))
jesstemp83 ='br. jessatom9'
jesstemp84 ='jessatom10 x. %s'%(1.521520+(d*0.050000))
jesstemp84 = '('+jesstemp84+') and not (jessatom10 x. %s)'%(max(0.05,1.518482-(d*0.050000)))
cmd.select('jessatom11', '(('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(6.506500+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom11 x. %s)'%(max(0.05,6.493506-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(6.256250+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom11 x. %s)'%(max(0.05,6.243756-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(5.475470+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom11 x. %s)'%(max(0.05,5.464535-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(10.580570+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom11 x. %s)'%(max(0.05,10.559441-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(9.229220+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom11 x. %s)'%(max(0.05,9.210789-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(8.198190+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom11 x. %s)'%(max(0.05,8.181818-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.084080+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom11 x. %s)'%(max(0.05,4.075924-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(4.244240+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom11 x. %s)'%(max(0.05,4.235764-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(3.763760+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom11 x. %s)'%(max(0.05,3.756244-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.422420+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom11 x. %s)'%(max(0.05,2.417582-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.521520+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom11 x. %s)'%(max(0.05,1.518482-(d*0.050000))))
cmd.select('Jfa_1kf5_3_1_27_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
