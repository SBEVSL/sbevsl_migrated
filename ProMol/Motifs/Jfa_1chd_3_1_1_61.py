'''
FUNC:Jfa_1chd_3_1_1_61
PDB:1chd
EC:3.1.1.61
RESI:ser,thr,his,met,asp
LOCI:a-164,165,190,283,286;
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
jesstemp7 ='jessatom0 x. %s'%(2.382380+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.377622-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.411410+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,1.408591-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.382380+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.377622-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.411410+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,1.408591-(d*0.050000))))
jesstemp10 ='n.  n  '
jesstemp11 ='jessatom0 x. %s'%(2.462460+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom0 x. %s)'%(max(0.05,2.457542-(d*0.050000)))
jesstemp12 ='jessatom1 x. %s'%(2.862860+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom1 x. %s)'%(max(0.05,2.857143-(d*0.050000)))
jesstemp13 ='jessatom2 x. %s'%(2.622620+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom2 x. %s)'%(max(0.05,2.617383-(d*0.050000)))
cmd.select('jessatom3', '(((('+jesstemp10+'))|(('+jesstemp10+')))&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(2.462460+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,2.457542-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(2.862860+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,2.857143-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(2.622620+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,2.617383-(d*0.050000))))
jesstemp14 ='n.  ca '
jesstemp15 ='jessatom0 x. %s'%(3.843840+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom0 x. %s)'%(max(0.05,3.836164-(d*0.050000)))
jesstemp16 ='jessatom1 x. %s'%(4.304300+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom1 x. %s)'%(max(0.05,4.295704-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(3.893890+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,3.886114-(d*0.050000)))
jesstemp18 ='jessatom3 x. %s'%(1.451450+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom3 x. %s)'%(max(0.05,1.448551-(d*0.050000)))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp14+'))|(('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.843840+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,3.836164-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.304300+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,4.295704-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.893890+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,3.886114-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.451450+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.448551-(d*0.050000))))
jesstemp20 ='n.  c  '
jesstemp21 ='jessatom0 x. %s'%(4.494490+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom0 x. %s)'%(max(0.05,4.485514-(d*0.050000)))
jesstemp22 ='jessatom1 x. %s'%(5.165160+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom1 x. %s)'%(max(0.05,5.154845-(d*0.050000)))
jesstemp23 ='jessatom2 x. %s'%(5.095090+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom2 x. %s)'%(max(0.05,5.084915-(d*0.050000)))
jesstemp24 ='jessatom3 x. %s'%(2.502500+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom3 x. %s)'%(max(0.05,2.497502-(d*0.050000)))
jesstemp25 ='br. jessatom3'
jesstemp26 ='jessatom4 x. %s'%(1.531530+(d*0.050000))
jesstemp26 = '('+jesstemp26+') and not (jessatom4 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
cmd.select('jessatom5', '(((('+jesstemp20+'))|(('+jesstemp20+')))&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.494490+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,4.485514-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.165160+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,5.154845-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.095090+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,5.084915-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.502500+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.497502-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp27 ='n.  cg '
jesstemp28 ='r. his'
jesstemp29 ='jessatom0 x. %s'%(4.414410+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom0 x. %s)'%(max(0.05,4.405594-(d*0.050000)))
jesstemp30 ='jessatom1 x. %s'%(3.973970+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom1 x. %s)'%(max(0.05,3.966034-(d*0.050000)))
jesstemp31 ='jessatom2 x. %s'%(4.144140+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom2 x. %s)'%(max(0.05,4.135864-(d*0.050000)))
jesstemp32 ='jessatom3 x. %s'%(6.236230+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom3 x. %s)'%(max(0.05,6.223776-(d*0.050000)))
jesstemp33 ='jessatom4 x. %s'%(7.567560+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom4 x. %s)'%(max(0.05,7.552448-(d*0.050000)))
jesstemp34 ='jessatom5 x. %s'%(8.638630+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom5 x. %s)'%(max(0.05,8.621379-(d*0.050000)))
cmd.select('jessatom6', '(('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(4.414410+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,4.405594-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(3.973970+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,3.966034-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.144140+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,4.135864-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.236230+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,6.223776-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.567560+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,7.552448-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.638630+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,8.621379-(d*0.050000))))
jesstemp35 ='n.  nd1'
jesstemp36 ='jessatom0 x. %s'%(4.344340+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom0 x. %s)'%(max(0.05,4.335664-(d*0.050000)))
jesstemp37 ='jessatom1 x. %s'%(3.443440+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom1 x. %s)'%(max(0.05,3.436563-(d*0.050000)))
jesstemp38 ='jessatom2 x. %s'%(3.503500+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom2 x. %s)'%(max(0.05,3.496503-(d*0.050000)))
jesstemp39 ='jessatom3 x. %s'%(5.915910+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom3 x. %s)'%(max(0.05,5.904096-(d*0.050000)))
jesstemp40 ='jessatom4 x. %s'%(7.267260+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom4 x. %s)'%(max(0.05,7.252747-(d*0.050000)))
jesstemp41 ='jessatom5 x. %s'%(8.388380+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom5 x. %s)'%(max(0.05,8.371628-(d*0.050000)))
jesstemp42 ='jessatom6 x. %s'%(1.381380+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom6 x. %s)'%(max(0.05,1.378621-(d*0.050000)))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp35+')&('+jesstemp28+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.344340+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,4.335664-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(3.443440+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,3.436563-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.503500+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,3.496503-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.915910+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,5.904096-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.267260+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,7.252747-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.388380+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,8.371628-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.381380+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.378621-(d*0.050000))))
jesstemp44 ='n.  ne2'
jesstemp45 ='jessatom0 x. %s'%(5.775770+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom0 x. %s)'%(max(0.05,5.764236-(d*0.050000)))
jesstemp46 ='jessatom1 x. %s'%(5.045040+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom1 x. %s)'%(max(0.05,5.034965-(d*0.050000)))
jesstemp47 ='jessatom2 x. %s'%(5.475470+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom2 x. %s)'%(max(0.05,5.464535-(d*0.050000)))
jesstemp48 ='jessatom3 x. %s'%(7.737730+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom3 x. %s)'%(max(0.05,7.722278-(d*0.050000)))
jesstemp49 ='jessatom4 x. %s'%(9.149140+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom4 x. %s)'%(max(0.05,9.130869-(d*0.050000)))
jesstemp50 ='jessatom5 x. %s'%(10.130120+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom5 x. %s)'%(max(0.05,10.109890-(d*0.050000)))
jesstemp51 ='jessatom6 x. %s'%(2.202200+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom6 x. %s)'%(max(0.05,2.197802-(d*0.050000)))
jesstemp52 ='br. jessatom6'
jesstemp53 ='jessatom7 x. %s'%(2.152150+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom7 x. %s)'%(max(0.05,2.147852-(d*0.050000)))
cmd.select('jessatom8', '(('+jesstemp44+')&('+jesstemp28+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.775770+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,5.764236-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.045040+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,5.034965-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.475470+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,5.464535-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.737730+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,7.722278-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.149140+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,9.130869-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(10.130120+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,10.109890-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.202200+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.197802-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.152150+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.147852-(d*0.050000))))
jesstemp54 ='n.  n  '
jesstemp55 ='jessatom0 x. %s'%(5.065060+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom0 x. %s)'%(max(0.05,5.054945-(d*0.050000)))
jesstemp56 ='jessatom1 x. %s'%(3.913910+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom1 x. %s)'%(max(0.05,3.906094-(d*0.050000)))
jesstemp57 ='jessatom2 x. %s'%(3.713710+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom2 x. %s)'%(max(0.05,3.706294-(d*0.050000)))
jesstemp58 ='jessatom3 x. %s'%(4.434430+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom3 x. %s)'%(max(0.05,4.425574-(d*0.050000)))
jesstemp59 ='jessatom4 x. %s'%(5.145140+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom4 x. %s)'%(max(0.05,5.134865-(d*0.050000)))
jesstemp60 ='jessatom5 x. %s'%(5.825820+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom5 x. %s)'%(max(0.05,5.814186-(d*0.050000)))
jesstemp61 ='jessatom6 x. %s'%(7.167160+(d*0.050000))
jesstemp61 = '('+jesstemp61+') and not (jessatom6 x. %s)'%(max(0.05,7.152847-(d*0.050000)))
jesstemp62 ='jessatom7 x. %s'%(6.066060+(d*0.050000))
jesstemp62 = '('+jesstemp62+') and not (jessatom7 x. %s)'%(max(0.05,6.053946-(d*0.050000)))
jesstemp63 ='jessatom8 x. %s'%(7.607600+(d*0.050000))
jesstemp63 = '('+jesstemp63+') and not (jessatom8 x. %s)'%(max(0.05,7.592408-(d*0.050000)))
cmd.select('jessatom9', '(('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(5.065060+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom9 x. %s)'%(max(0.05,5.054945-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(3.913910+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom9 x. %s)'%(max(0.05,3.906094-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(3.713710+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom9 x. %s)'%(max(0.05,3.706294-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(4.434430+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom9 x. %s)'%(max(0.05,4.425574-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(5.145140+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom9 x. %s)'%(max(0.05,5.134865-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(5.825820+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom9 x. %s)'%(max(0.05,5.814186-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(7.167160+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom9 x. %s)'%(max(0.05,7.152847-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(6.066060+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom9 x. %s)'%(max(0.05,6.053946-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(7.607600+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom9 x. %s)'%(max(0.05,7.592408-(d*0.050000))))
jesstemp64 ='jessatom0 x. %s'%(6.336330+(d*0.050000))
jesstemp64 = '('+jesstemp64+') and not (jessatom0 x. %s)'%(max(0.05,6.323676-(d*0.050000)))
jesstemp65 ='jessatom1 x. %s'%(5.065060+(d*0.050000))
jesstemp65 = '('+jesstemp65+') and not (jessatom1 x. %s)'%(max(0.05,5.054945-(d*0.050000)))
jesstemp66 ='jessatom2 x. %s'%(4.654650+(d*0.050000))
jesstemp66 = '('+jesstemp66+') and not (jessatom2 x. %s)'%(max(0.05,4.645355-(d*0.050000)))
jesstemp67 ='jessatom3 x. %s'%(5.675670+(d*0.050000))
jesstemp67 = '('+jesstemp67+') and not (jessatom3 x. %s)'%(max(0.05,5.664336-(d*0.050000)))
jesstemp68 ='jessatom4 x. %s'%(6.276270+(d*0.050000))
jesstemp68 = '('+jesstemp68+') and not (jessatom4 x. %s)'%(max(0.05,6.263736-(d*0.050000)))
jesstemp69 ='jessatom5 x. %s'%(7.057050+(d*0.050000))
jesstemp69 = '('+jesstemp69+') and not (jessatom5 x. %s)'%(max(0.05,7.042957-(d*0.050000)))
jesstemp70 ='jessatom6 x. %s'%(7.817810+(d*0.050000))
jesstemp70 = '('+jesstemp70+') and not (jessatom6 x. %s)'%(max(0.05,7.802198-(d*0.050000)))
jesstemp71 ='jessatom7 x. %s'%(6.586580+(d*0.050000))
jesstemp71 = '('+jesstemp71+') and not (jessatom7 x. %s)'%(max(0.05,6.573427-(d*0.050000)))
jesstemp72 ='jessatom8 x. %s'%(8.078070+(d*0.050000))
jesstemp72 = '('+jesstemp72+') and not (jessatom8 x. %s)'%(max(0.05,8.061938-(d*0.050000)))
jesstemp73 ='jessatom9 x. %s'%(1.451450+(d*0.050000))
jesstemp73 = '('+jesstemp73+') and not (jessatom9 x. %s)'%(max(0.05,1.448551-(d*0.050000)))
jesstemp74 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp0+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(6.336330+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom10 x. %s)'%(max(0.05,6.323676-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(5.065060+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom10 x. %s)'%(max(0.05,5.054945-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(4.654650+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom10 x. %s)'%(max(0.05,4.645355-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(5.675670+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom10 x. %s)'%(max(0.05,5.664336-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(6.276270+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom10 x. %s)'%(max(0.05,6.263736-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(7.057050+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom10 x. %s)'%(max(0.05,7.042957-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(7.817810+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom10 x. %s)'%(max(0.05,7.802198-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(6.586580+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom10 x. %s)'%(max(0.05,6.573427-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(8.078070+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom10 x. %s)'%(max(0.05,8.061938-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.451450+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom10 x. %s)'%(max(0.05,1.448551-(d*0.050000))))
jesstemp75 ='n.  c  '
jesstemp76 ='jessatom0 x. %s'%(6.706700+(d*0.050000))
jesstemp76 = '('+jesstemp76+') and not (jessatom0 x. %s)'%(max(0.05,6.693307-(d*0.050000)))
jesstemp77 ='jessatom1 x. %s'%(5.265260+(d*0.050000))
jesstemp77 = '('+jesstemp77+') and not (jessatom1 x. %s)'%(max(0.05,5.254745-(d*0.050000)))
jesstemp78 ='jessatom2 x. %s'%(4.984980+(d*0.050000))
jesstemp78 = '('+jesstemp78+') and not (jessatom2 x. %s)'%(max(0.05,4.975025-(d*0.050000)))
jesstemp79 ='jessatom3 x. %s'%(6.546540+(d*0.050000))
jesstemp79 = '('+jesstemp79+') and not (jessatom3 x. %s)'%(max(0.05,6.533467-(d*0.050000)))
jesstemp80 ='jessatom4 x. %s'%(7.367360+(d*0.050000))
jesstemp80 = '('+jesstemp80+') and not (jessatom4 x. %s)'%(max(0.05,7.352647-(d*0.050000)))
jesstemp81 ='jessatom5 x. %s'%(8.218210+(d*0.050000))
jesstemp81 = '('+jesstemp81+') and not (jessatom5 x. %s)'%(max(0.05,8.201798-(d*0.050000)))
jesstemp82 ='jessatom6 x. %s'%(7.377370+(d*0.050000))
jesstemp82 = '('+jesstemp82+') and not (jessatom6 x. %s)'%(max(0.05,7.362637-(d*0.050000)))
jesstemp83 ='jessatom7 x. %s'%(6.056050+(d*0.050000))
jesstemp83 = '('+jesstemp83+') and not (jessatom7 x. %s)'%(max(0.05,6.043956-(d*0.050000)))
jesstemp84 ='jessatom8 x. %s'%(7.277270+(d*0.050000))
jesstemp84 = '('+jesstemp84+') and not (jessatom8 x. %s)'%(max(0.05,7.262737-(d*0.050000)))
jesstemp85 ='jessatom9 x. %s'%(2.452450+(d*0.050000))
jesstemp85 = '('+jesstemp85+') and not (jessatom9 x. %s)'%(max(0.05,2.447552-(d*0.050000)))
jesstemp86 ='br. jessatom9'
jesstemp87 ='jessatom10 x. %s'%(1.521520+(d*0.050000))
jesstemp87 = '('+jesstemp87+') and not (jessatom10 x. %s)'%(max(0.05,1.518482-(d*0.050000)))
cmd.select('jessatom11', '(('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(6.706700+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom11 x. %s)'%(max(0.05,6.693307-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(5.265260+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom11 x. %s)'%(max(0.05,5.254745-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(4.984980+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom11 x. %s)'%(max(0.05,4.975025-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(6.546540+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom11 x. %s)'%(max(0.05,6.533467-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(7.367360+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom11 x. %s)'%(max(0.05,7.352647-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(8.218210+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom11 x. %s)'%(max(0.05,8.201798-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.377370+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom11 x. %s)'%(max(0.05,7.362637-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(6.056050+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom11 x. %s)'%(max(0.05,6.043956-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(7.277270+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom11 x. %s)'%(max(0.05,7.262737-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.452450+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom11 x. %s)'%(max(0.05,2.447552-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.521520+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom11 x. %s)'%(max(0.05,1.518482-(d*0.050000))))
jesstemp88 ='r. asp'
jesstemp89 ='r. glu'
jesstemp90 ='jessatom0 x. %s'%(8.808800+(d*0.050000))
jesstemp90 = '('+jesstemp90+') and not (jessatom0 x. %s)'%(max(0.05,8.791209-(d*0.050000)))
jesstemp91 ='jessatom1 x. %s'%(7.847840+(d*0.050000))
jesstemp91 = '('+jesstemp91+') and not (jessatom1 x. %s)'%(max(0.05,7.832168-(d*0.050000)))
jesstemp92 ='jessatom2 x. %s'%(8.388380+(d*0.050000))
jesstemp92 = '('+jesstemp92+') and not (jessatom2 x. %s)'%(max(0.05,8.371628-(d*0.050000)))
jesstemp93 ='jessatom3 x. %s'%(10.690680+(d*0.050000))
jesstemp93 = '('+jesstemp93+') and not (jessatom3 x. %s)'%(max(0.05,10.669331-(d*0.050000)))
jesstemp94 ='jessatom4 x. %s'%(12.112100+(d*0.050000))
jesstemp94 = '('+jesstemp94+') and not (jessatom4 x. %s)'%(max(0.05,12.087912-(d*0.050000)))
jesstemp95 ='jessatom5 x. %s'%(12.972960+(d*0.050000))
jesstemp95 = '('+jesstemp95+') and not (jessatom5 x. %s)'%(max(0.05,12.947053-(d*0.050000)))
jesstemp96 ='jessatom6 x. %s'%(5.895890+(d*0.050000))
jesstemp96 = '('+jesstemp96+') and not (jessatom6 x. %s)'%(max(0.05,5.884116-(d*0.050000)))
jesstemp97 ='jessatom7 x. %s'%(5.445440+(d*0.050000))
jesstemp97 = '('+jesstemp97+') and not (jessatom7 x. %s)'%(max(0.05,5.434565-(d*0.050000)))
jesstemp98 ='jessatom8 x. %s'%(3.703700+(d*0.050000))
jesstemp98 = '('+jesstemp98+') and not (jessatom8 x. %s)'%(max(0.05,3.696304-(d*0.050000)))
jesstemp99 ='jessatom9 x. %s'%(9.219210+(d*0.050000))
jesstemp99 = '('+jesstemp99+') and not (jessatom9 x. %s)'%(max(0.05,9.200799-(d*0.050000)))
jesstemp100 ='jessatom10 x. %s'%(9.349340+(d*0.050000))
jesstemp100 = '('+jesstemp100+') and not (jessatom10 x. %s)'%(max(0.05,9.330669-(d*0.050000)))
jesstemp101 ='jessatom11 x. %s'%(8.108100+(d*0.050000))
jesstemp101 = '('+jesstemp101+') and not (jessatom11 x. %s)'%(max(0.05,8.091908-(d*0.050000)))
cmd.select('jessatom12', '(((('+jesstemp27+')&('+jesstemp88+'))|(('+jesstemp27+')&('+jesstemp89+')))&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+')&('+jesstemp95+')&('+jesstemp96+')&('+jesstemp97+')&('+jesstemp98+')&('+jesstemp99+')&('+jesstemp100+')&('+jesstemp101+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom12 x. %s)'%(8.808800+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom12 x. %s)'%(max(0.05,8.791209-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom12 x. %s)'%(7.847840+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom12 x. %s)'%(max(0.05,7.832168-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom12 x. %s)'%(8.388380+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom12 x. %s)'%(max(0.05,8.371628-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom12 x. %s)'%(10.690680+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom12 x. %s)'%(max(0.05,10.669331-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom12 x. %s)'%(12.112100+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom12 x. %s)'%(max(0.05,12.087912-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom12 x. %s)'%(12.972960+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom12 x. %s)'%(max(0.05,12.947053-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom12 x. %s)'%(5.895890+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom12 x. %s)'%(max(0.05,5.884116-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom12 x. %s)'%(5.445440+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom12 x. %s)'%(max(0.05,5.434565-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom12 x. %s)'%(3.703700+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom12 x. %s)'%(max(0.05,3.696304-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom12 x. %s)'%(9.219210+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom12 x. %s)'%(max(0.05,9.200799-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom12 x. %s)'%(9.349340+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom12 x. %s)'%(max(0.05,9.330669-(d*0.050000))))
cmd.select('jessatom11', 'jessatom11 & (jessatom12 x. %s)'%(8.108100+(d*0.050000)))
cmd.select('jessatom11', 'jessatom11 & not (jessatom12 x. %s)'%(max(0.05,8.091908-(d*0.050000))))
jesstemp102 ='n.  od1'
jesstemp103 ='n.  od2'
jesstemp104 ='n.  oe1'
jesstemp105 ='n.  oe2'
jesstemp106 ='jessatom0 x. %s'%(9.979970+(d*0.050000))
jesstemp106 = '('+jesstemp106+') and not (jessatom0 x. %s)'%(max(0.05,9.960040-(d*0.050000)))
jesstemp107 ='jessatom1 x. %s'%(9.049040+(d*0.050000))
jesstemp107 = '('+jesstemp107+') and not (jessatom1 x. %s)'%(max(0.05,9.030969-(d*0.050000)))
jesstemp108 ='jessatom2 x. %s'%(9.629620+(d*0.050000))
jesstemp108 = '('+jesstemp108+') and not (jessatom2 x. %s)'%(max(0.05,9.610390-(d*0.050000)))
jesstemp109 ='jessatom3 x. %s'%(11.901890+(d*0.050000))
jesstemp109 = '('+jesstemp109+') and not (jessatom3 x. %s)'%(max(0.05,11.878122-(d*0.050000)))
jesstemp110 ='jessatom4 x. %s'%(13.333320+(d*0.050000))
jesstemp110 = '('+jesstemp110+') and not (jessatom4 x. %s)'%(max(0.05,13.306693-(d*0.050000)))
jesstemp111 ='jessatom5 x. %s'%(14.154140+(d*0.050000))
jesstemp111 = '('+jesstemp111+') and not (jessatom5 x. %s)'%(max(0.05,14.125874-(d*0.050000)))
jesstemp112 ='jessatom6 x. %s'%(7.057050+(d*0.050000))
jesstemp112 = '('+jesstemp112+') and not (jessatom6 x. %s)'%(max(0.05,7.042957-(d*0.050000)))
jesstemp113 ='jessatom7 x. %s'%(6.676670+(d*0.050000))
jesstemp113 = '('+jesstemp113+') and not (jessatom7 x. %s)'%(max(0.05,6.663337-(d*0.050000)))
jesstemp114 ='jessatom8 x. %s'%(4.854850+(d*0.050000))
jesstemp114 = '('+jesstemp114+') and not (jessatom8 x. %s)'%(max(0.05,4.845155-(d*0.050000)))
jesstemp115 ='jessatom9 x. %s'%(10.330320+(d*0.050000))
jesstemp115 = '('+jesstemp115+') and not (jessatom9 x. %s)'%(max(0.05,10.309690-(d*0.050000)))
jesstemp116 ='jessatom10 x. %s'%(10.420410+(d*0.050000))
jesstemp116 = '('+jesstemp116+') and not (jessatom10 x. %s)'%(max(0.05,10.399600-(d*0.050000)))
jesstemp117 ='jessatom11 x. %s'%(9.119110+(d*0.050000))
jesstemp117 = '('+jesstemp117+') and not (jessatom11 x. %s)'%(max(0.05,9.100899-(d*0.050000)))
jesstemp118 ='jessatom12 x. %s'%(1.251250+(d*0.050000))
jesstemp118 = '('+jesstemp118+') and not (jessatom12 x. %s)'%(max(0.05,1.248751-(d*0.050000)))
jesstemp119 ='br. jessatom12'
cmd.select('jessatom13', '((((('+jesstemp102+')|('+jesstemp103+'))&('+jesstemp88+'))|((('+jesstemp104+')|('+jesstemp105+'))&('+jesstemp89+')))&('+jesstemp106+')&('+jesstemp107+')&('+jesstemp108+')&('+jesstemp109+')&('+jesstemp110+')&('+jesstemp111+')&('+jesstemp112+')&('+jesstemp113+')&('+jesstemp114+')&('+jesstemp115+')&('+jesstemp116+')&('+jesstemp117+')&('+jesstemp118+')&('+jesstemp119+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom13 x. %s)'%(9.979970+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom13 x. %s)'%(max(0.05,9.960040-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom13 x. %s)'%(9.049040+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom13 x. %s)'%(max(0.05,9.030969-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom13 x. %s)'%(9.629620+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom13 x. %s)'%(max(0.05,9.610390-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom13 x. %s)'%(11.901890+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom13 x. %s)'%(max(0.05,11.878122-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom13 x. %s)'%(13.333320+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom13 x. %s)'%(max(0.05,13.306693-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom13 x. %s)'%(14.154140+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom13 x. %s)'%(max(0.05,14.125874-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom13 x. %s)'%(7.057050+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom13 x. %s)'%(max(0.05,7.042957-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom13 x. %s)'%(6.676670+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom13 x. %s)'%(max(0.05,6.663337-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom13 x. %s)'%(4.854850+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom13 x. %s)'%(max(0.05,4.845155-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom13 x. %s)'%(10.330320+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom13 x. %s)'%(max(0.05,10.309690-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom13 x. %s)'%(10.420410+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom13 x. %s)'%(max(0.05,10.399600-(d*0.050000))))
cmd.select('jessatom11', 'jessatom11 & (jessatom13 x. %s)'%(9.119110+(d*0.050000)))
cmd.select('jessatom11', 'jessatom11 & not (jessatom13 x. %s)'%(max(0.05,9.100899-(d*0.050000))))
cmd.select('jessatom12', 'jessatom12 & (jessatom13 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom12', 'jessatom12 & not (jessatom13 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
jesstemp120 ='n.  od2'
jesstemp121 ='n.  od1'
jesstemp122 ='n.  oe2'
jesstemp123 ='n.  oe1'
jesstemp124 ='jessatom0 x. %s'%(8.198190+(d*0.050000))
jesstemp124 = '('+jesstemp124+') and not (jessatom0 x. %s)'%(max(0.05,8.181818-(d*0.050000)))
jesstemp125 ='jessatom1 x. %s'%(7.357350+(d*0.050000))
jesstemp125 = '('+jesstemp125+') and not (jessatom1 x. %s)'%(max(0.05,7.342657-(d*0.050000)))
jesstemp126 ='jessatom2 x. %s'%(7.897890+(d*0.050000))
jesstemp126 = '('+jesstemp126+') and not (jessatom2 x. %s)'%(max(0.05,7.882118-(d*0.050000)))
jesstemp127 ='jessatom3 x. %s'%(10.190180+(d*0.050000))
jesstemp127 = '('+jesstemp127+') and not (jessatom3 x. %s)'%(max(0.05,10.169830-(d*0.050000)))
jesstemp128 ='jessatom4 x. %s'%(11.621610+(d*0.050000))
jesstemp128 = '('+jesstemp128+') and not (jessatom4 x. %s)'%(max(0.05,11.598402-(d*0.050000)))
jesstemp129 ='jessatom5 x. %s'%(12.512500+(d*0.050000))
jesstemp129 = '('+jesstemp129+') and not (jessatom5 x. %s)'%(max(0.05,12.487512-(d*0.050000)))
jesstemp130 ='jessatom6 x. %s'%(4.934930+(d*0.050000))
jesstemp130 = '('+jesstemp130+') and not (jessatom6 x. %s)'%(max(0.05,4.925075-(d*0.050000)))
jesstemp131 ='jessatom7 x. %s'%(4.724720+(d*0.050000))
jesstemp131 = '('+jesstemp131+') and not (jessatom7 x. %s)'%(max(0.05,4.715285-(d*0.050000)))
jesstemp132 ='jessatom8 x. %s'%(2.752750+(d*0.050000))
jesstemp132 = '('+jesstemp132+') and not (jessatom8 x. %s)'%(max(0.05,2.747253-(d*0.050000)))
jesstemp133 ='jessatom9 x. %s'%(9.229220+(d*0.050000))
jesstemp133 = '('+jesstemp133+') and not (jessatom9 x. %s)'%(max(0.05,9.210789-(d*0.050000)))
jesstemp134 ='jessatom10 x. %s'%(9.479470+(d*0.050000))
jesstemp134 = '('+jesstemp134+') and not (jessatom10 x. %s)'%(max(0.05,9.460539-(d*0.050000)))
jesstemp135 ='jessatom11 x. %s'%(8.348340+(d*0.050000))
jesstemp135 = '('+jesstemp135+') and not (jessatom11 x. %s)'%(max(0.05,8.331668-(d*0.050000)))
jesstemp136 ='br. jessatom12'
jesstemp137 ='jessatom13 x. %s'%(2.172170+(d*0.050000))
jesstemp137 = '('+jesstemp137+') and not (jessatom13 x. %s)'%(max(0.05,2.167832-(d*0.050000)))
cmd.select('jessatom14', '((((('+jesstemp120+')|('+jesstemp121+'))&('+jesstemp88+'))|((('+jesstemp122+')|('+jesstemp123+'))&('+jesstemp89+')))&('+jesstemp124+')&('+jesstemp125+')&('+jesstemp126+')&('+jesstemp127+')&('+jesstemp128+')&('+jesstemp129+')&('+jesstemp130+')&('+jesstemp131+')&('+jesstemp132+')&('+jesstemp133+')&('+jesstemp134+')&('+jesstemp135+')&('+jesstemp118+')&('+jesstemp136+')&('+jesstemp137+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom14 x. %s)'%(8.198190+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom14 x. %s)'%(max(0.05,8.181818-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom14 x. %s)'%(7.357350+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom14 x. %s)'%(max(0.05,7.342657-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom14 x. %s)'%(7.897890+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom14 x. %s)'%(max(0.05,7.882118-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom14 x. %s)'%(10.190180+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom14 x. %s)'%(max(0.05,10.169830-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom14 x. %s)'%(11.621610+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom14 x. %s)'%(max(0.05,11.598402-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom14 x. %s)'%(12.512500+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom14 x. %s)'%(max(0.05,12.487512-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom14 x. %s)'%(4.934930+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom14 x. %s)'%(max(0.05,4.925075-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom14 x. %s)'%(4.724720+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom14 x. %s)'%(max(0.05,4.715285-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom14 x. %s)'%(2.752750+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom14 x. %s)'%(max(0.05,2.747253-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom14 x. %s)'%(9.229220+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom14 x. %s)'%(max(0.05,9.210789-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom14 x. %s)'%(9.479470+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom14 x. %s)'%(max(0.05,9.460539-(d*0.050000))))
cmd.select('jessatom11', 'jessatom11 & (jessatom14 x. %s)'%(8.348340+(d*0.050000)))
cmd.select('jessatom11', 'jessatom11 & not (jessatom14 x. %s)'%(max(0.05,8.331668-(d*0.050000))))
cmd.select('jessatom12', 'jessatom12 & (jessatom14 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom12', 'jessatom12 & not (jessatom14 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
cmd.select('jessatom13', 'jessatom13 & (jessatom14 x. %s)'%(2.172170+(d*0.050000)))
cmd.select('jessatom13', 'jessatom13 & not (jessatom14 x. %s)'%(max(0.05,2.167832-(d*0.050000))))
cmd.select('Jfa_1chd_3_1_1_61', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
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
cmd.delete('jessatom12')
cmd.delete('jessatom13')
cmd.delete('jessatom14')
