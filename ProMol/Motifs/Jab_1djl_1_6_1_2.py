'''
FUNC:Jab_1djl_1_6_1_2
PDB:1djl
EC:1.6.1.2
RESI:tyr,arg,tyr
LOCI:a-890,925,1006;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. tyr'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. tyr'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. arg'
xxxtemp7 ='jessatom0 x. %s'%(d*6.566560)
xxxtemp8 ='jessatom1 x. %s'%(d*6.066060)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*6.566560))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*6.066060))
xxxtemp9 ='jessatom0 x. %s'%(d*6.636630)
xxxtemp10 ='jessatom1 x. %s'%(d*6.026020)
xxxtemp11 ='jessatom2 x. %s'%(d*1.521520)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*6.636630))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.026020))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.521520))
xxxtemp13 ='jessatom0 x. %s'%(d*9.049040)
xxxtemp14 ='jessatom1 x. %s'%(d*7.597590)
xxxtemp15 ='jessatom2 x. %s'%(d*9.269260)
xxxtemp16 ='jessatom3 x. %s'%(d*9.239230)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*9.049040))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*7.597590))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*9.269260))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*9.239230))
xxxtemp17 ='jessatom0 x. %s'%(d*8.398390)
xxxtemp18 ='jessatom1 x. %s'%(d*6.956950)
xxxtemp19 ='jessatom2 x. %s'%(d*7.897890)
xxxtemp20 ='jessatom3 x. %s'%(d*7.977970)
xxxtemp21 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*8.398390))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*6.956950))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*7.897890))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*7.977970))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_1djl_1_6_1_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
