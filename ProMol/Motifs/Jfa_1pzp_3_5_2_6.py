'''
FUNC:Jfa_1pzp_3_5_2_6
PDB:1pzp
EC:3.5.2.6
RESI:ser,lys,ser,glu
LOCI:a-70,73,130,166;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.531530+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.392390+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.387612-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.421420+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,1.418581-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.392390+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.387612-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.421420+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,1.418581-(d*0.050000))))
jesstemp10 ='n.  cd '
jesstemp11 ='r. lys'
jesstemp12 ='jessatom0 x. %s'%(4.204200+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom0 x. %s)'%(max(0.05,4.195804-(d*0.050000)))
jesstemp13 ='jessatom1 x. %s'%(3.953950+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom1 x. %s)'%(max(0.05,3.946054-(d*0.050000)))
jesstemp14 ='jessatom2 x. %s'%(3.933930+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom2 x. %s)'%(max(0.05,3.926074-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.204200+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,4.195804-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.953950+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,3.946054-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.933930+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,3.926074-(d*0.050000))))
jesstemp15 ='n.  ce '
jesstemp16 ='jessatom0 x. %s'%(4.184180+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,4.175824-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(3.413410+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,3.406593-(d*0.050000)))
jesstemp18 ='jessatom3 x. %s'%(1.561560+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom3 x. %s)'%(max(0.05,1.558442-(d*0.050000)))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp13+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.184180+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,4.175824-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.953950+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,3.946054-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.413410+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,3.406593-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.561560+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.558442-(d*0.050000))))
jesstemp20 ='n.  nz '
jesstemp21 ='jessatom0 x. %s'%(4.254250+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom0 x. %s)'%(max(0.05,4.245754-(d*0.050000)))
jesstemp22 ='jessatom1 x. %s'%(3.583580+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom1 x. %s)'%(max(0.05,3.576424-(d*0.050000)))
jesstemp23 ='jessatom2 x. %s'%(2.662660+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom2 x. %s)'%(max(0.05,2.657343-(d*0.050000)))
jesstemp24 ='jessatom3 x. %s'%(2.542540+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom3 x. %s)'%(max(0.05,2.537463-(d*0.050000)))
jesstemp25 ='br. jessatom3'
jesstemp26 ='jessatom4 x. %s'%(1.471470+(d*0.050000))
jesstemp26 = '('+jesstemp26+') and not (jessatom4 x. %s)'%(max(0.05,1.468531-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp20+')&('+jesstemp11+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.254250+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,4.245754-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.583580+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,3.576424-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(2.662660+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,2.657343-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.542540+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.537463-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.471470+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.468531-(d*0.050000))))
jesstemp27 ='jessatom0 x. %s'%(6.566560+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom0 x. %s)'%(max(0.05,6.553447-(d*0.050000)))
jesstemp28 ='jessatom1 x. %s'%(5.275270+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom1 x. %s)'%(max(0.05,5.264735-(d*0.050000)))
jesstemp29 ='jessatom2 x. %s'%(5.005000+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom2 x. %s)'%(max(0.05,4.995005-(d*0.050000)))
jesstemp30 ='jessatom3 x. %s'%(4.434430+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom3 x. %s)'%(max(0.05,4.425574-(d*0.050000)))
jesstemp31 ='jessatom4 x. %s'%(4.764760+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom4 x. %s)'%(max(0.05,4.755245-(d*0.050000)))
jesstemp32 ='jessatom5 x. %s'%(3.983980+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom5 x. %s)'%(max(0.05,3.976024-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.566560+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,6.553447-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.275270+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,5.264735-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.005000+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,4.995005-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.434430+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,4.425574-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.764760+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,4.755245-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.983980+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,3.976024-(d*0.050000))))
jesstemp33 ='jessatom0 x. %s'%(6.046040+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom0 x. %s)'%(max(0.05,6.033966-(d*0.050000)))
jesstemp34 ='jessatom1 x. %s'%(4.584580+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom1 x. %s)'%(max(0.05,4.575425-(d*0.050000)))
jesstemp35 ='jessatom2 x. %s'%(4.354350+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom2 x. %s)'%(max(0.05,4.345654-(d*0.050000)))
jesstemp36 ='jessatom3 x. %s'%(5.005000+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom3 x. %s)'%(max(0.05,4.995005-(d*0.050000)))
jesstemp37 ='jessatom4 x. %s'%(5.205200+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom4 x. %s)'%(max(0.05,5.194805-(d*0.050000)))
jesstemp38 ='jessatom5 x. %s'%(4.174170+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom5 x. %s)'%(max(0.05,4.165834-(d*0.050000)))
jesstemp39 ='jessatom6 x. %s'%(1.541540+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom6 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.046040+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,6.033966-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.584580+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,4.575425-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.354350+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,4.345654-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.005000+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,4.995005-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.205200+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,5.194805-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.174170+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,4.165834-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp41 ='jessatom0 x. %s'%(4.634630+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom0 x. %s)'%(max(0.05,4.625375-(d*0.050000)))
jesstemp42 ='jessatom1 x. %s'%(3.173170+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom1 x. %s)'%(max(0.05,3.166833-(d*0.050000)))
jesstemp43 ='jessatom2 x. %s'%(3.033030+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom2 x. %s)'%(max(0.05,3.026973-(d*0.050000)))
jesstemp44 ='jessatom3 x. %s'%(4.194190+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom3 x. %s)'%(max(0.05,4.185814-(d*0.050000)))
jesstemp45 ='jessatom4 x. %s'%(4.354350+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom4 x. %s)'%(max(0.05,4.345654-(d*0.050000)))
jesstemp46 ='jessatom5 x. %s'%(3.383380+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom5 x. %s)'%(max(0.05,3.376623-(d*0.050000)))
jesstemp47 ='jessatom6 x. %s'%(2.402400+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom6 x. %s)'%(max(0.05,2.397602-(d*0.050000)))
jesstemp48 ='br. jessatom6'
jesstemp49 ='jessatom7 x. %s'%(1.421420+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom7 x. %s)'%(max(0.05,1.418581-(d*0.050000)))
cmd.select('jessatom8', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.634630+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,4.625375-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(3.173170+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,3.166833-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(3.033030+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,3.026973-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.194190+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,4.185814-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.354350+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,4.345654-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.383380+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,3.376623-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.402400+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.397602-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.421420+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,1.418581-(d*0.050000))))
jesstemp50 ='r. glu'
jesstemp51 ='r. asp'
jesstemp52 ='jessatom0 x. %s'%(5.895890+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom0 x. %s)'%(max(0.05,5.884116-(d*0.050000)))
jesstemp53 ='jessatom1 x. %s'%(6.066060+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom1 x. %s)'%(max(0.05,6.053946-(d*0.050000)))
jesstemp54 ='jessatom2 x. %s'%(4.944940+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom2 x. %s)'%(max(0.05,4.935065-(d*0.050000)))
jesstemp55 ='jessatom3 x. %s'%(5.665660+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom3 x. %s)'%(max(0.05,5.654346-(d*0.050000)))
jesstemp56 ='jessatom4 x. %s'%(4.154150+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom4 x. %s)'%(max(0.05,4.145854-(d*0.050000)))
jesstemp57 ='jessatom5 x. %s'%(4.114110+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom5 x. %s)'%(max(0.05,4.105894-(d*0.050000)))
jesstemp58 ='jessatom6 x. %s'%(7.977970+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom6 x. %s)'%(max(0.05,7.962038-(d*0.050000)))
jesstemp59 ='jessatom7 x. %s'%(8.018010+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom7 x. %s)'%(max(0.05,8.001998-(d*0.050000)))
jesstemp60 ='jessatom8 x. %s'%(7.157150+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom8 x. %s)'%(max(0.05,7.142857-(d*0.050000)))
cmd.select('jessatom9', '(((('+jesstemp10+')&('+jesstemp50+'))|(('+jesstemp10+')&('+jesstemp51+')))&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.895890+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom9 x. %s)'%(max(0.05,5.884116-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(6.066060+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom9 x. %s)'%(max(0.05,6.053946-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(4.944940+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom9 x. %s)'%(max(0.05,4.935065-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(5.665660+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom9 x. %s)'%(max(0.05,5.654346-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(4.154150+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom9 x. %s)'%(max(0.05,4.145854-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(4.114110+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom9 x. %s)'%(max(0.05,4.105894-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(7.977970+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom9 x. %s)'%(max(0.05,7.962038-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(8.018010+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom9 x. %s)'%(max(0.05,8.001998-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(7.157150+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom9 x. %s)'%(max(0.05,7.142857-(d*0.050000))))
jesstemp61 ='n.  oe1'
jesstemp62 ='n.  oe2'
jesstemp63 ='n.  od1'
jesstemp64 ='n.  od2'
jesstemp65 ='jessatom0 x. %s'%(6.326320+(d*0.050000))
jesstemp65 = '('+jesstemp65+') and not (jessatom0 x. %s)'%(max(0.05,6.313686-(d*0.050000)))
jesstemp66 ='jessatom1 x. %s'%(6.436430+(d*0.050000))
jesstemp66 = '('+jesstemp66+') and not (jessatom1 x. %s)'%(max(0.05,6.423576-(d*0.050000)))
jesstemp67 ='jessatom2 x. %s'%(5.225220+(d*0.050000))
jesstemp67 = '('+jesstemp67+') and not (jessatom2 x. %s)'%(max(0.05,5.214785-(d*0.050000)))
jesstemp68 ='jessatom3 x. %s'%(6.636630+(d*0.050000))
jesstemp68 = '('+jesstemp68+') and not (jessatom3 x. %s)'%(max(0.05,6.623377-(d*0.050000)))
jesstemp69 ='jessatom4 x. %s'%(5.125120+(d*0.050000))
jesstemp69 = '('+jesstemp69+') and not (jessatom4 x. %s)'%(max(0.05,5.114885-(d*0.050000)))
jesstemp70 ='jessatom5 x. %s'%(4.804800+(d*0.050000))
jesstemp70 = '('+jesstemp70+') and not (jessatom5 x. %s)'%(max(0.05,4.795205-(d*0.050000)))
jesstemp71 ='jessatom6 x. %s'%(8.518510+(d*0.050000))
jesstemp71 = '('+jesstemp71+') and not (jessatom6 x. %s)'%(max(0.05,8.501499-(d*0.050000)))
jesstemp72 ='jessatom7 x. %s'%(8.378370+(d*0.050000))
jesstemp72 = '('+jesstemp72+') and not (jessatom7 x. %s)'%(max(0.05,8.361638-(d*0.050000)))
jesstemp73 ='jessatom8 x. %s'%(7.527520+(d*0.050000))
jesstemp73 = '('+jesstemp73+') and not (jessatom8 x. %s)'%(max(0.05,7.512488-(d*0.050000)))
jesstemp74 ='jessatom9 x. %s'%(1.241240+(d*0.050000))
jesstemp74 = '('+jesstemp74+') and not (jessatom9 x. %s)'%(max(0.05,1.238761-(d*0.050000)))
jesstemp75 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp61+')|('+jesstemp62+'))&('+jesstemp50+'))|((('+jesstemp63+')|('+jesstemp64+'))&('+jesstemp51+')))&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(6.326320+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom10 x. %s)'%(max(0.05,6.313686-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(6.436430+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom10 x. %s)'%(max(0.05,6.423576-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(5.225220+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom10 x. %s)'%(max(0.05,5.214785-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(6.636630+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom10 x. %s)'%(max(0.05,6.623377-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(5.125120+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom10 x. %s)'%(max(0.05,5.114885-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(4.804800+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom10 x. %s)'%(max(0.05,4.795205-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(8.518510+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom10 x. %s)'%(max(0.05,8.501499-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(8.378370+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom10 x. %s)'%(max(0.05,8.361638-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(7.527520+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom10 x. %s)'%(max(0.05,7.512488-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom10 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
jesstemp76 ='n.  oe2'
jesstemp77 ='n.  oe1'
jesstemp78 ='n.  od2'
jesstemp79 ='n.  od1'
jesstemp80 ='jessatom0 x. %s'%(4.714710+(d*0.050000))
jesstemp80 = '('+jesstemp80+') and not (jessatom0 x. %s)'%(max(0.05,4.705295-(d*0.050000)))
jesstemp81 ='jessatom1 x. %s'%(4.974970+(d*0.050000))
jesstemp81 = '('+jesstemp81+') and not (jessatom1 x. %s)'%(max(0.05,4.965035-(d*0.050000)))
jesstemp82 ='jessatom2 x. %s'%(3.983980+(d*0.050000))
jesstemp82 = '('+jesstemp82+') and not (jessatom2 x. %s)'%(max(0.05,3.976024-(d*0.050000)))
jesstemp83 ='jessatom3 x. %s'%(4.664660+(d*0.050000))
jesstemp83 = '('+jesstemp83+') and not (jessatom3 x. %s)'%(max(0.05,4.655345-(d*0.050000)))
jesstemp84 ='jessatom4 x. %s'%(3.233230+(d*0.050000))
jesstemp84 = '('+jesstemp84+') and not (jessatom4 x. %s)'%(max(0.05,3.226773-(d*0.050000)))
jesstemp85 ='jessatom5 x. %s'%(3.353350+(d*0.050000))
jesstemp85 = '('+jesstemp85+') and not (jessatom5 x. %s)'%(max(0.05,3.346653-(d*0.050000)))
jesstemp86 ='jessatom6 x. %s'%(7.317310+(d*0.050000))
jesstemp86 = '('+jesstemp86+') and not (jessatom6 x. %s)'%(max(0.05,7.302697-(d*0.050000)))
jesstemp87 ='jessatom7 x. %s'%(7.327320+(d*0.050000))
jesstemp87 = '('+jesstemp87+') and not (jessatom7 x. %s)'%(max(0.05,7.312687-(d*0.050000)))
jesstemp88 ='jessatom8 x. %s'%(6.336330+(d*0.050000))
jesstemp88 = '('+jesstemp88+') and not (jessatom8 x. %s)'%(max(0.05,6.323676-(d*0.050000)))
jesstemp89 ='br. jessatom9'
jesstemp90 ='jessatom10 x. %s'%(2.162160+(d*0.050000))
jesstemp90 = '('+jesstemp90+') and not (jessatom10 x. %s)'%(max(0.05,2.157842-(d*0.050000)))
cmd.select('jessatom11', '((((('+jesstemp76+')|('+jesstemp77+'))&('+jesstemp50+'))|((('+jesstemp78+')|('+jesstemp79+'))&('+jesstemp51+')))&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp74+')&('+jesstemp89+')&('+jesstemp90+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(4.714710+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom11 x. %s)'%(max(0.05,4.705295-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(4.974970+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom11 x. %s)'%(max(0.05,4.965035-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(3.983980+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom11 x. %s)'%(max(0.05,3.976024-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(4.664660+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom11 x. %s)'%(max(0.05,4.655345-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(3.233230+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom11 x. %s)'%(max(0.05,3.226773-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(3.353350+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom11 x. %s)'%(max(0.05,3.346653-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.317310+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom11 x. %s)'%(max(0.05,7.302697-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.327320+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom11 x. %s)'%(max(0.05,7.312687-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(6.336330+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom11 x. %s)'%(max(0.05,6.323676-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom11 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.162160+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom11 x. %s)'%(max(0.05,2.157842-(d*0.050000))))
cmd.select('Jfa_1pzp_3_5_2_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
