'''
FUNC:Jab_1cns_3_2_1_14
PDB:1cns
EC:3.2.1.14
RESI:glu,glu,ser
LOCI:a-67,89,120;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. glu'
xxxtemp2 ='r. asp'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.521520)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.521520))
xxxtemp6 ='jessatom0 x. %s'%(d*9.479470)
xxxtemp7 ='jessatom1 x. %s'%(d*9.479470)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+')))&('+xxxtemp6+')&('+xxxtemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*9.479470))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*9.479470))
xxxtemp8 ='jessatom0 x. %s'%(d*9.619610)
xxxtemp9 ='jessatom1 x. %s'%(d*9.489480)
xxxtemp10 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp8+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*9.619610))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*9.489480))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp12 ='r. ser'
xxxtemp13 ='r. thr'
xxxtemp14 ='jessatom0 x. %s'%(d*11.581570)
xxxtemp15 ='jessatom1 x. %s'%(d*10.520510)
xxxtemp16 ='jessatom2 x. %s'%(d*9.169160)
xxxtemp17 ='jessatom3 x. %s'%(d*7.927920)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp12+'))|(('+xxxtemp0+')&('+xxxtemp13+')))&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*11.581570))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*10.520510))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*9.169160))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*7.927920))
xxxtemp18 ='jessatom0 x. %s'%(d*10.950940)
xxxtemp19 ='jessatom1 x. %s'%(d*10.010000)
xxxtemp20 ='jessatom2 x. %s'%(d*8.778770)
xxxtemp21 ='jessatom3 x. %s'%(d*7.437430)
xxxtemp22 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp3+')&('+xxxtemp12+'))|(('+xxxtemp3+')&('+xxxtemp13+')))&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*10.950940))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*10.010000))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*8.778770))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*7.437430))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_1cns_3_2_1_14', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
