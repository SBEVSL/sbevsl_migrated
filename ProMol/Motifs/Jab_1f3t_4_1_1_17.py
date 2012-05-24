'''
FUNC:Jab_1f3t_4_1_1_17
PDB:1f3t
EC:4.1.1.17
RESI:lys,his,glu
LOCI:a-69,197,272;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. lys'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. lys'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*14.724710)
xxxtemp8 ='jessatom1 x. %s'%(d*13.623610)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*14.724710))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*13.623610))
xxxtemp9 ='jessatom0 x. %s'%(d*13.423410)
xxxtemp10 ='jessatom1 x. %s'%(d*12.272260)
xxxtemp11 ='jessatom2 x. %s'%(d*1.521520)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*13.423410))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*12.272260))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.521520))
xxxtemp13 ='r. glu'
xxxtemp14 ='r. asp'
xxxtemp15 ='jessatom0 x. %s'%(d*10.650640)
xxxtemp16 ='jessatom1 x. %s'%(d*10.320310)
xxxtemp17 ='jessatom2 x. %s'%(d*8.528520)
xxxtemp18 ='jessatom3 x. %s'%(d*8.158150)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp13+'))|(('+xxxtemp0+')&('+xxxtemp14+')))&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*10.650640))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*10.320310))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*8.528520))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*8.158150))
xxxtemp19 ='jessatom0 x. %s'%(d*10.200190)
xxxtemp20 ='jessatom1 x. %s'%(d*9.679670)
xxxtemp21 ='jessatom2 x. %s'%(d*7.687680)
xxxtemp22 ='jessatom3 x. %s'%(d*7.137130)
xxxtemp23 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp13+'))|(('+xxxtemp2+')&('+xxxtemp14+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*10.200190))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*9.679670))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*7.687680))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*7.137130))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
cmd.select('Jab_1f3t_4_1_1_17', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
