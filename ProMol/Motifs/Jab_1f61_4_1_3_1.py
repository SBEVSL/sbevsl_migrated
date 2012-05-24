'''
FUNC:Jab_1f61_4_1_3_1
PDB:1f61
EC:4.1.3.1
RESI:his,cys,arg
LOCI:a-180,191,228;
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
xxxtemp6 ='r. cys'
xxxtemp7 ='jessatom0 x. %s'%(d*24.924900)
xxxtemp8 ='jessatom1 x. %s'%(d*24.404380)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*24.924900))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*24.404380))
xxxtemp9 ='jessatom0 x. %s'%(d*25.525500)
xxxtemp10 ='jessatom1 x. %s'%(d*25.014990)
xxxtemp11 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*25.525500))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*25.014990))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp13 ='r. arg'
xxxtemp14 ='jessatom0 x. %s'%(d*6.636630)
xxxtemp15 ='jessatom1 x. %s'%(d*6.006000)
xxxtemp16 ='jessatom2 x. %s'%(d*21.921900)
xxxtemp17 ='jessatom3 x. %s'%(d*22.842820)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*6.636630))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*6.006000))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*21.921900))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*22.842820))
xxxtemp18 ='jessatom0 x. %s'%(d*6.046040)
xxxtemp19 ='jessatom1 x. %s'%(d*5.245240)
xxxtemp20 ='jessatom2 x. %s'%(d*21.131110)
xxxtemp21 ='jessatom3 x. %s'%(d*21.981960)
xxxtemp22 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*6.046040))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*5.245240))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*21.131110))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*21.981960))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1f61_4_1_3_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
