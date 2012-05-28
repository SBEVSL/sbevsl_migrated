'''
FUNC:Jfa_12as_6_3_1_1
PDB:12as
EC:6.3.1.1
RESI:asp,arg,gln
LOCI:a-46,100,116;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.251250+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,1.248751-(d*0.050000)))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.192190+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom1 x. %s)'%(max(0.05,2.187812-(d*0.050000)))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.192190+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.187812-(d*0.050000))))
jesstemp15 ='n.  ne '
jesstemp16 ='r. arg'
jesstemp17 ='jessatom0 x. %s'%(7.357350+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom0 x. %s)'%(max(0.05,7.342657-(d*0.050000)))
jesstemp18 ='jessatom1 x. %s'%(7.887880+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom1 x. %s)'%(max(0.05,7.872128-(d*0.050000)))
jesstemp19 ='jessatom2 x. %s'%(6.606600+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom2 x. %s)'%(max(0.05,6.593407-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.357350+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,7.342657-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.887880+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,7.872128-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.606600+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,6.593407-(d*0.050000))))
jesstemp20 ='n.  nh1'
jesstemp21 ='n.  nh2'
jesstemp22 ='jessatom0 x. %s'%(6.376370+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom0 x. %s)'%(max(0.05,6.363636-(d*0.050000)))
jesstemp23 ='jessatom1 x. %s'%(6.686680+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom1 x. %s)'%(max(0.05,6.673327-(d*0.050000)))
jesstemp24 ='jessatom2 x. %s'%(5.555550+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom2 x. %s)'%(max(0.05,5.544456-(d*0.050000)))
jesstemp25 ='jessatom3 x. %s'%(2.252250+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom3 x. %s)'%(max(0.05,2.247752-(d*0.050000)))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp16+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.376370+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,6.363636-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.686680+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,6.673327-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.555550+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,5.544456-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.252250+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,2.247752-(d*0.050000))))
jesstemp27 ='n.  nh2'
jesstemp28 ='n.  nh1'
jesstemp29 ='jessatom0 x. %s'%(5.775770+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom0 x. %s)'%(max(0.05,5.764236-(d*0.050000)))
jesstemp30 ='jessatom1 x. %s'%(6.486480+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom1 x. %s)'%(max(0.05,6.473526-(d*0.050000)))
jesstemp31 ='jessatom2 x. %s'%(4.814810+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom2 x. %s)'%(max(0.05,4.805195-(d*0.050000)))
jesstemp32 ='jessatom3 x. %s'%(2.302300+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom3 x. %s)'%(max(0.05,2.297702-(d*0.050000)))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.252250+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom4 x. %s)'%(max(0.05,2.247752-(d*0.050000)))
cmd.select('jessatom5', '((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp16+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.775770+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,5.764236-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.486480+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,6.473526-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.814810+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,4.805195-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.302300+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.297702-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.252250+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,2.247752-(d*0.050000))))
jesstemp35 ='n.  cd '
jesstemp36 ='r. gln'
jesstemp37 ='r. asn'
jesstemp38 ='jessatom0 x. %s'%(8.348340+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom0 x. %s)'%(max(0.05,8.331668-(d*0.050000)))
jesstemp39 ='jessatom1 x. %s'%(9.299290+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom1 x. %s)'%(max(0.05,9.280719-(d*0.050000)))
jesstemp40 ='jessatom2 x. %s'%(7.147140+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom2 x. %s)'%(max(0.05,7.132867-(d*0.050000)))
jesstemp41 ='jessatom3 x. %s'%(6.466460+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom3 x. %s)'%(max(0.05,6.453546-(d*0.050000)))
jesstemp42 ='jessatom4 x. %s'%(6.406400+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom4 x. %s)'%(max(0.05,6.393606-(d*0.050000)))
jesstemp43 ='jessatom5 x. %s'%(4.754750+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom5 x. %s)'%(max(0.05,4.745255-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp35+')&('+jesstemp36+'))|(('+jesstemp35+')&('+jesstemp37+')))&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.348340+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,8.331668-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.299290+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,9.280719-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.147140+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,7.132867-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.466460+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,6.453546-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.406400+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,6.393606-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.754750+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,4.745255-(d*0.050000))))
jesstemp44 ='jessatom0 x. %s'%(7.697690+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom0 x. %s)'%(max(0.05,7.682318-(d*0.050000)))
jesstemp45 ='jessatom1 x. %s'%(8.588580+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom1 x. %s)'%(max(0.05,8.571429-(d*0.050000)))
jesstemp46 ='jessatom2 x. %s'%(6.496490+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom2 x. %s)'%(max(0.05,6.483516-(d*0.050000)))
jesstemp47 ='jessatom3 x. %s'%(5.315310+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom3 x. %s)'%(max(0.05,5.304695-(d*0.050000)))
jesstemp48 ='jessatom4 x. %s'%(5.185180+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom4 x. %s)'%(max(0.05,5.174825-(d*0.050000)))
jesstemp49 ='jessatom5 x. %s'%(3.603600+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom5 x. %s)'%(max(0.05,3.596404-(d*0.050000)))
jesstemp50 ='jessatom6 x. %s'%(1.231230+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom6 x. %s)'%(max(0.05,1.228771-(d*0.050000)))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp5+')&('+jesstemp36+'))|(('+jesstemp5+')&('+jesstemp37+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.697690+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,7.682318-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.588580+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,8.571429-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.496490+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,6.483516-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.315310+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,5.304695-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.185180+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,5.174825-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.603600+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,3.596404-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.231230+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.228771-(d*0.050000))))
jesstemp52 ='n.  ne2'
jesstemp53 ='jessatom0 x. %s'%(7.957950+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom0 x. %s)'%(max(0.05,7.942058-(d*0.050000)))
jesstemp54 ='jessatom1 x. %s'%(8.958950+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom1 x. %s)'%(max(0.05,8.941059-(d*0.050000)))
jesstemp55 ='jessatom2 x. %s'%(6.796790+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom2 x. %s)'%(max(0.05,6.783217-(d*0.050000)))
jesstemp56 ='jessatom3 x. %s'%(7.317310+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom3 x. %s)'%(max(0.05,7.302697-(d*0.050000)))
jesstemp57 ='jessatom4 x. %s'%(7.107100+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom4 x. %s)'%(max(0.05,7.092907-(d*0.050000)))
jesstemp58 ='jessatom5 x. %s'%(5.355350+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom5 x. %s)'%(max(0.05,5.344655-(d*0.050000)))
jesstemp59 ='jessatom6 x. %s'%(1.331330+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom6 x. %s)'%(max(0.05,1.328671-(d*0.050000)))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(2.242240+(d*0.050000))
jesstemp61 = '('+jesstemp61+') and not (jessatom7 x. %s)'%(max(0.05,2.237762-(d*0.050000)))
cmd.select('jessatom8', '(((('+jesstemp52+')&('+jesstemp36+'))|(('+jesstemp52+')&('+jesstemp37+')))&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.957950+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,7.942058-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.958950+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,8.941059-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.796790+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,6.783217-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.317310+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,7.302697-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.107100+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,7.092907-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.355350+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,5.344655-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.331330+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,1.328671-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.242240+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.237762-(d*0.050000))))
cmd.select('Jfa_12as_6_3_1_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
