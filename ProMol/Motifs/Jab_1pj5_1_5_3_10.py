'''
FUNC:Jab_1pj5_1_5_3_10
PDB:1pj5
EC:1.5.3.10
RESI:his,tyr,asp
LOCI:a-225,259,552;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. his'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. his'
xxxtemp4 ='jessatom0 x. %s'%(d*1.551550)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.551550))
xxxtemp6 ='r. tyr'
xxxtemp7 ='jessatom0 x. %s'%(d*11.951940)
xxxtemp8 ='jessatom1 x. %s'%(d*11.301290)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*11.951940))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*11.301290))
xxxtemp9 ='jessatom0 x. %s'%(d*11.541530)
xxxtemp10 ='jessatom1 x. %s'%(d*10.720710)
xxxtemp11 ='jessatom2 x. %s'%(d*1.551550)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*11.541530))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*10.720710))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.551550))
xxxtemp13 ='r. asp'
xxxtemp14 ='r. glu'
xxxtemp15 ='jessatom0 x. %s'%(d*40.570530)
xxxtemp16 ='jessatom1 x. %s'%(d*39.339300)
xxxtemp17 ='jessatom2 x. %s'%(d*41.631590)
xxxtemp18 ='jessatom3 x. %s'%(d*40.330290)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp13+'))|(('+xxxtemp0+')&('+xxxtemp14+')))&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*40.570530))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*39.339300))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*41.631590))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*40.330290))
xxxtemp19 ='jessatom0 x. %s'%(d*41.000960)
xxxtemp20 ='jessatom1 x. %s'%(d*39.759720)
xxxtemp21 ='jessatom2 x. %s'%(d*41.671630)
xxxtemp22 ='jessatom3 x. %s'%(d*40.390350)
xxxtemp23 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp13+'))|(('+xxxtemp2+')&('+xxxtemp14+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*41.000960))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*39.759720))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*41.671630))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*40.390350))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1pj5_1_5_3_10', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('temp0')
cmd.delete('temp1')
cmd.delete('temp2')
cmd.delete('temp3')
cmd.delete('temp4')
cmd.delete('temp5')
cmd.delete('temp6')
cmd.delete('temp7')
cmd.delete('temp8')
cmd.delete('temp9')
cmd.delete('temp10')
cmd.delete('temp11')
cmd.delete('temp12')
cmd.delete('temp13')
cmd.delete('temp14')
cmd.delete('temp15')
cmd.delete('temp16')
cmd.delete('temp17')
cmd.delete('temp18')
cmd.delete('temp19')
cmd.delete('temp20')
cmd.delete('temp21')
cmd.delete('temp22')
cmd.delete('temp23')
cmd.delete('temp24')
