'''
FUNC:Jab_1csc_2_3_3_1
PDB:1csc
EC:2.3.3.1
RESI:ser,his,his,asp
LOCI:a-244,274,320,375;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. his'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. his'
xxxtemp4 ='jessatom0 x. %s'%(d*1.561560)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.561560))
xxxtemp6 ='jessatom0 x. %s'%(d*9.709700)
xxxtemp7 ='jessatom1 x. %s'%(d*10.550540)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*9.709700))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*10.550540))
xxxtemp8 ='jessatom0 x. %s'%(d*10.330320)
xxxtemp9 ='jessatom1 x. %s'%(d*11.141130)
xxxtemp10 ='jessatom2 x. %s'%(d*1.551550)
xxxtemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp8+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*10.330320))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*11.141130))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.551550))
xxxtemp12 ='r. asp'
xxxtemp13 ='r. glu'
xxxtemp14 ='jessatom0 x. %s'%(d*9.089080)
xxxtemp15 ='jessatom1 x. %s'%(d*10.360350)
xxxtemp16 ='jessatom2 x. %s'%(d*10.530520)
xxxtemp17 ='jessatom3 x. %s'%(d*10.190180)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp12+'))|(('+xxxtemp0+')&('+xxxtemp13+')))&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*9.089080))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*10.360350))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*10.530520))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*10.190180))
xxxtemp18 ='jessatom0 x. %s'%(d*7.717710)
xxxtemp19 ='jessatom1 x. %s'%(d*9.049040)
xxxtemp20 ='jessatom2 x. %s'%(d*10.040030)
xxxtemp21 ='jessatom3 x. %s'%(d*9.899890)
xxxtemp22 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp12+'))|(('+xxxtemp2+')&('+xxxtemp13+')))&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*7.717710))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*9.049040))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*10.040030))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*9.899890))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
cmd.select('Jab_1csc_2_3_3_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
