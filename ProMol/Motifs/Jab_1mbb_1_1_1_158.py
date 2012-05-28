'''
FUNC:Jab_1mbb_1_1_1_158
PDB:1mbb
EC:1.1.1.158
RESI:arg,ser,glu
LOCI:a-159,229,325;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. arg'
jesstemp4 ='jessatom0 x. %s'%(1.541540+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp6 ='r. ser'
jesstemp7 ='r. thr'
jesstemp8 ='jessatom0 x. %s'%(11.021010+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom0 x. %s)'%(max(0.05,10.999001-(d*0.050000)))
jesstemp9 ='jessatom1 x. %s'%(9.689680+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,9.670330-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(11.021010+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,10.999001-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(9.689680+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,9.670330-(d*0.050000))))
jesstemp10 ='jessatom0 x. %s'%(9.979970+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom0 x. %s)'%(max(0.05,9.960040-(d*0.050000)))
jesstemp11 ='jessatom1 x. %s'%(8.648640+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,8.631369-(d*0.050000)))
jesstemp12 ='jessatom2 x. %s'%(1.521520+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom2 x. %s)'%(max(0.05,1.518482-(d*0.050000)))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.979970+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,9.960040-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.648640+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,8.631369-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.521520+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.518482-(d*0.050000))))
jesstemp14 ='r. glu'
jesstemp15 ='r. asp'
jesstemp16 ='jessatom0 x. %s'%(7.437430+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,7.422577-(d*0.050000)))
jesstemp17 ='jessatom1 x. %s'%(6.086080+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom1 x. %s)'%(max(0.05,6.073926-(d*0.050000)))
jesstemp18 ='jessatom2 x. %s'%(6.866860+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom2 x. %s)'%(max(0.05,6.853147-(d*0.050000)))
jesstemp19 ='jessatom3 x. %s'%(6.696690+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom3 x. %s)'%(max(0.05,6.683317-(d*0.050000)))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.437430+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,7.422577-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.086080+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,6.073926-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.866860+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,6.853147-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(6.696690+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,6.683317-(d*0.050000))))
jesstemp20 ='jessatom0 x. %s'%(6.886880+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom0 x. %s)'%(max(0.05,6.873127-(d*0.050000)))
jesstemp21 ='jessatom1 x. %s'%(5.465460+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom1 x. %s)'%(max(0.05,5.454545-(d*0.050000)))
jesstemp22 ='jessatom2 x. %s'%(5.755750+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom2 x. %s)'%(max(0.05,5.744256-(d*0.050000)))
jesstemp23 ='jessatom3 x. %s'%(5.385380+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom3 x. %s)'%(max(0.05,5.374625-(d*0.050000)))
jesstemp24 ='jessatom4 x. %s'%(1.511510+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom4 x. %s)'%(max(0.05,1.508492-(d*0.050000)))
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.886880+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,6.873127-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.465460+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,5.454545-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.755750+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,5.744256-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(5.385380+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,5.374625-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.511510+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.508492-(d*0.050000))))
cmd.select('Jab_1mbb_1_1_1_158', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
