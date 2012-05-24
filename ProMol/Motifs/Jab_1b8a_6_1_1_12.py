'''
FUNC:Jab_1b8a_6_1_1_12
PDB:1b8a
EC:6.1.1.12
RESI:arg,asp,arg
LOCI:a-214,231,412;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. arg'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. arg'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. asp'
xxxtemp7 ='r. glu'
xxxtemp8 ='jessatom0 x. %s'%(d*15.805790)
xxxtemp9 ='jessatom1 x. %s'%(d*15.045030)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*15.805790))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*15.045030))
xxxtemp10 ='jessatom0 x. %s'%(d*14.944930)
xxxtemp11 ='jessatom1 x. %s'%(d*14.284270)
xxxtemp12 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*14.944930))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*14.284270))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp14 ='jessatom0 x. %s'%(d*14.554540)
xxxtemp15 ='jessatom1 x. %s'%(d*13.423410)
xxxtemp16 ='jessatom2 x. %s'%(d*13.323310)
xxxtemp17 ='jessatom3 x. %s'%(d*14.003990)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp3+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*14.554540))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*13.423410))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*13.323310))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*14.003990))
xxxtemp18 ='jessatom0 x. %s'%(d*13.923910)
xxxtemp19 ='jessatom1 x. %s'%(d*12.702690)
xxxtemp20 ='jessatom2 x. %s'%(d*12.552540)
xxxtemp21 ='jessatom3 x. %s'%(d*13.203190)
xxxtemp22 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*13.923910))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*12.702690))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*12.552540))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*13.203190))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_1b8a_6_1_1_12', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
