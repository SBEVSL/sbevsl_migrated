'''
FUNC:Jab_1gqn_4_2_1_10
PDB:1gqn
EC:4.2.1.10
RESI:glu,his,lys
LOCI:a-86,143,170;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.561560+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.558442-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.561560+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.558442-(d*0.050000))))
jesstemp6 ='r. his'
jesstemp7 ='jessatom0 x. %s'%(5.505500+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,5.494505-(d*0.050000)))
jesstemp8 ='jessatom1 x. %s'%(4.894890+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom1 x. %s)'%(max(0.05,4.885115-(d*0.050000)))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.505500+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,5.494505-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.894890+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,4.885115-(d*0.050000))))
jesstemp9 ='jessatom0 x. %s'%(4.594590+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom0 x. %s)'%(max(0.05,4.585415-(d*0.050000)))
jesstemp10 ='jessatom1 x. %s'%(4.054050+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom1 x. %s)'%(max(0.05,4.045954-(d*0.050000)))
jesstemp11 ='jessatom2 x. %s'%(1.581580+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom2 x. %s)'%(max(0.05,1.578422-(d*0.050000)))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.594590+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,4.585415-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.054050+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,4.045954-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.581580+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.578422-(d*0.050000))))
jesstemp13 ='r. lys'
jesstemp14 ='jessatom0 x. %s'%(12.712700+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom0 x. %s)'%(max(0.05,12.687313-(d*0.050000)))
jesstemp15 ='jessatom1 x. %s'%(11.421410+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom1 x. %s)'%(max(0.05,11.398601-(d*0.050000)))
jesstemp16 ='jessatom2 x. %s'%(8.448440+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom2 x. %s)'%(max(0.05,8.431568-(d*0.050000)))
jesstemp17 ='jessatom3 x. %s'%(8.928920+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom3 x. %s)'%(max(0.05,8.911089-(d*0.050000)))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.712700+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,12.687313-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.421410+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,11.398601-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.448440+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,8.431568-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(8.928920+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,8.911089-(d*0.050000))))
jesstemp18 ='jessatom0 x. %s'%(12.192180+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom0 x. %s)'%(max(0.05,12.167832-(d*0.050000)))
jesstemp19 ='jessatom1 x. %s'%(10.880870+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom1 x. %s)'%(max(0.05,10.859141-(d*0.050000)))
jesstemp20 ='jessatom2 x. %s'%(8.388380+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom2 x. %s)'%(max(0.05,8.371628-(d*0.050000)))
jesstemp21 ='jessatom3 x. %s'%(8.598590+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom3 x. %s)'%(max(0.05,8.581419-(d*0.050000)))
jesstemp22 ='jessatom4 x. %s'%(1.571570+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom4 x. %s)'%(max(0.05,1.568432-(d*0.050000)))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.192180+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,12.167832-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.880870+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,10.859141-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.388380+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,8.371628-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(8.598590+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,8.581419-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.571570+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.568432-(d*0.050000))))
cmd.select('Jab_1gqn_4_2_1_10', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
