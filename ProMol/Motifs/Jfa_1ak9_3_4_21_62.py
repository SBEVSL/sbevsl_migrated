'''
FUNC:Jfa_1ak9_3_4_21_62
PDB:1ak9
EC:3.4.21.62
RESI:asp,his,ser
LOCI:a-32,64,221;
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
jesstemp13 ='jessatom0 x. %s'%(1.241240+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom0 x. %s)'%(max(0.05,1.238761-(d*0.050000)))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.222220+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom1 x. %s)'%(max(0.05,2.217782-(d*0.050000)))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222220+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.217782-(d*0.050000))))
jesstemp16 ='r. his'
jesstemp17 ='jessatom0 x. %s'%(4.414410+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom0 x. %s)'%(max(0.05,4.405594-(d*0.050000)))
jesstemp18 ='jessatom1 x. %s'%(3.603600+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom1 x. %s)'%(max(0.05,3.596404-(d*0.050000)))
jesstemp19 ='jessatom2 x. %s'%(4.444440+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom2 x. %s)'%(max(0.05,4.435564-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.414410+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,4.405594-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.603600+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,3.596404-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.444440+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,4.435564-(d*0.050000))))
jesstemp20 ='n.  nd1'
jesstemp21 ='jessatom0 x. %s'%(3.263260+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom0 x. %s)'%(max(0.05,3.256743-(d*0.050000)))
jesstemp22 ='jessatom1 x. %s'%(2.692690+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom1 x. %s)'%(max(0.05,2.687313-(d*0.050000)))
jesstemp23 ='jessatom2 x. %s'%(3.153150+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom2 x. %s)'%(max(0.05,3.146853-(d*0.050000)))
jesstemp24 ='jessatom3 x. %s'%(1.391390+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom3 x. %s)'%(max(0.05,1.388611-(d*0.050000)))
jesstemp25 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp20+')&('+jesstemp16+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.263260+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,3.256743-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(2.692690+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,2.687313-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.153150+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,3.146853-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.391390+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.388611-(d*0.050000))))
jesstemp26 ='n.  ne2'
jesstemp27 ='jessatom0 x. %s'%(5.195190+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom0 x. %s)'%(max(0.05,5.184815-(d*0.050000)))
jesstemp28 ='jessatom1 x. %s'%(4.784780+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom1 x. %s)'%(max(0.05,4.775225-(d*0.050000)))
jesstemp29 ='jessatom2 x. %s'%(4.754750+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom2 x. %s)'%(max(0.05,4.745255-(d*0.050000)))
jesstemp30 ='jessatom3 x. %s'%(2.202200+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom3 x. %s)'%(max(0.05,2.197802-(d*0.050000)))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(2.142140+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom4 x. %s)'%(max(0.05,2.137862-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp26+')&('+jesstemp16+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.195190+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,5.184815-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.784780+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,4.775225-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.754750+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,4.745255-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.202200+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.197802-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.142140+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,2.137862-(d*0.050000))))
jesstemp33 ='n.  ca '
jesstemp34 ='r. ser'
jesstemp35 ='r. thr'
jesstemp36 ='jessatom0 x. %s'%(7.847840+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom0 x. %s)'%(max(0.05,7.832168-(d*0.050000)))
jesstemp37 ='jessatom1 x. %s'%(8.158150+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom1 x. %s)'%(max(0.05,8.141858-(d*0.050000)))
jesstemp38 ='jessatom2 x. %s'%(6.766760+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom2 x. %s)'%(max(0.05,6.753247-(d*0.050000)))
jesstemp39 ='jessatom3 x. %s'%(6.676670+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom3 x. %s)'%(max(0.05,6.663337-(d*0.050000)))
jesstemp40 ='jessatom4 x. %s'%(6.136130+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom4 x. %s)'%(max(0.05,6.123876-(d*0.050000)))
jesstemp41 ='jessatom5 x. %s'%(4.744740+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom5 x. %s)'%(max(0.05,4.735265-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp33+')&('+jesstemp34+'))|(('+jesstemp33+')&('+jesstemp35+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.847840+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,7.832168-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.158150+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,8.141858-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.766760+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,6.753247-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.676670+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,6.663337-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.136130+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,6.123876-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.744740+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,4.735265-(d*0.050000))))
jesstemp42 ='n.  cb '
jesstemp43 ='jessatom0 x. %s'%(6.996990+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom0 x. %s)'%(max(0.05,6.983017-(d*0.050000)))
jesstemp44 ='jessatom1 x. %s'%(7.117110+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom1 x. %s)'%(max(0.05,7.102897-(d*0.050000)))
jesstemp45 ='jessatom2 x. %s'%(6.056050+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom2 x. %s)'%(max(0.05,6.043956-(d*0.050000)))
jesstemp46 ='jessatom3 x. %s'%(5.245240+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom3 x. %s)'%(max(0.05,5.234765-(d*0.050000)))
jesstemp47 ='jessatom4 x. %s'%(4.854850+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom4 x. %s)'%(max(0.05,4.845155-(d*0.050000)))
jesstemp48 ='jessatom5 x. %s'%(3.263260+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom5 x. %s)'%(max(0.05,3.256743-(d*0.050000)))
jesstemp49 ='jessatom6 x. %s'%(1.531530+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom6 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp50 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp42+')&('+jesstemp34+'))|(('+jesstemp42+')&('+jesstemp35+')))&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.996990+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,6.983017-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.117110+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,7.102897-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.056050+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,6.043956-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.245240+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,5.234765-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.854850+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,4.845155-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.263260+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,3.256743-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp51 ='n.  og '
jesstemp52 ='jessatom0 x. %s'%(6.736730+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom0 x. %s)'%(max(0.05,6.723277-(d*0.050000)))
jesstemp53 ='jessatom1 x. %s'%(6.796790+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom1 x. %s)'%(max(0.05,6.783217-(d*0.050000)))
jesstemp54 ='jessatom2 x. %s'%(5.875870+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom2 x. %s)'%(max(0.05,5.864136-(d*0.050000)))
jesstemp55 ='jessatom3 x. %s'%(5.125120+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom3 x. %s)'%(max(0.05,5.114885-(d*0.050000)))
jesstemp56 ='jessatom4 x. %s'%(4.614610+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom4 x. %s)'%(max(0.05,4.605395-(d*0.050000)))
jesstemp57 ='jessatom5 x. %s'%(2.972970+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom5 x. %s)'%(max(0.05,2.967033-(d*0.050000)))
jesstemp58 ='jessatom6 x. %s'%(2.372370+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom6 x. %s)'%(max(0.05,2.367632-(d*0.050000)))
jesstemp59 ='br. jessatom6'
jesstemp60 ='jessatom7 x. %s'%(1.391390+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom7 x. %s)'%(max(0.05,1.388611-(d*0.050000)))
cmd.select('jessatom8', '(((('+jesstemp51+')&('+jesstemp34+'))|(('+jesstemp51+')&('+jesstemp35+')))&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.736730+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,6.723277-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.796790+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,6.783217-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.875870+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,5.864136-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.125120+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,5.114885-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.614610+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,4.605395-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(2.972970+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,2.967033-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.372370+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.367632-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.391390+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,1.388611-(d*0.050000))))
cmd.select('Jfa_1ak9_3_4_21_62', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
