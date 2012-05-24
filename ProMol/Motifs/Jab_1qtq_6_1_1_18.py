'''
FUNC:Jab_1qtq_6_1_1_18
PDB:1qtq
EC:6.1.1.18
RESI:glu,arg,lys
LOCI:a-34,360,270;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. glu'
xxxtemp2 ='r. asp'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. arg'
xxxtemp7 ='jessatom0 x. %s'%(d*16.186170)
xxxtemp8 ='jessatom1 x. %s'%(d*15.955940)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*16.186170))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*15.955940))
xxxtemp9 ='jessatom0 x. %s'%(d*15.185170)
xxxtemp10 ='jessatom1 x. %s'%(d*14.854840)
xxxtemp11 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*15.185170))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*14.854840))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp13 ='r. lys'
xxxtemp14 ='jessatom0 x. %s'%(d*10.360350)
xxxtemp15 ='jessatom1 x. %s'%(d*9.849840)
xxxtemp16 ='jessatom2 x. %s'%(d*13.453440)
xxxtemp17 ='jessatom3 x. %s'%(d*12.182170)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*10.360350))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*9.849840))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*13.453440))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*12.182170))
xxxtemp18 ='jessatom0 x. %s'%(d*8.848840)
xxxtemp19 ='jessatom1 x. %s'%(d*8.348340)
xxxtemp20 ='jessatom2 x. %s'%(d*13.643630)
xxxtemp21 ='jessatom3 x. %s'%(d*12.362350)
xxxtemp22 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*8.848840))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*8.348340))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*13.643630))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*12.362350))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
cmd.select('Jab_1qtq_6_1_1_18', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
