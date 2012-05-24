'''
FUNC:Jab_1n7n_4_2_2_1
PDB:1n7n
EC:4.2.2.1
RESI:asn,his,tyr
LOCI:a-349,399,408;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. his'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. his'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. tyr'
xxxtemp7 ='jessatom0 x. %s'%(d*9.249240)
xxxtemp8 ='jessatom1 x. %s'%(d*9.029020)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*9.249240))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*9.029020))
xxxtemp9 ='jessatom0 x. %s'%(d*7.737730)
xxxtemp10 ='jessatom1 x. %s'%(d*7.607600)
xxxtemp11 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*7.737730))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*7.607600))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp13 ='r. arg'
xxxtemp14 ='jessatom0 x. %s'%(d*11.531520)
xxxtemp15 ='jessatom1 x. %s'%(d*10.110100)
xxxtemp16 ='jessatom2 x. %s'%(d*10.560550)
xxxtemp17 ='jessatom3 x. %s'%(d*10.460450)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*11.531520))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*10.110100))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*10.560550))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*10.460450))
xxxtemp18 ='jessatom0 x. %s'%(d*10.950940)
xxxtemp19 ='jessatom1 x. %s'%(d*9.469460)
xxxtemp20 ='jessatom2 x. %s'%(d*10.780770)
xxxtemp21 ='jessatom3 x. %s'%(d*10.550540)
xxxtemp22 ='jessatom4 x. %s'%(d*1.551550)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*10.950940))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*9.469460))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*10.780770))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*10.550540))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.551550))
cmd.select('Jab_1n7n_4_2_2_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
