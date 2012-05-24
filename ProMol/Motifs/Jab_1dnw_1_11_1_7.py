'''
FUNC:Jab_1dnw_1_11_1_7
PDB:1dnw
EC:1.11.1.7
RESI:gln,his,arg
LOCI:a-95,95;c-239;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. gln'
xxxtemp2 ='r. asn'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*6.286280)
xxxtemp8 ='jessatom1 x. %s'%(d*7.087080)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*6.286280))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*7.087080))
xxxtemp9 ='jessatom0 x. %s'%(d*5.975970)
xxxtemp10 ='jessatom1 x. %s'%(d*6.496490)
xxxtemp11 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*5.975970))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.496490))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp13 ='r. arg'
xxxtemp14 ='jessatom0 x. %s'%(d*10.010000)
xxxtemp15 ='jessatom1 x. %s'%(d*9.469460)
xxxtemp16 ='jessatom2 x. %s'%(d*7.677670)
xxxtemp17 ='jessatom3 x. %s'%(d*6.496490)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*10.010000))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*9.469460))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*7.677670))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*6.496490))
xxxtemp18 ='jessatom0 x. %s'%(d*8.918910)
xxxtemp19 ='jessatom1 x. %s'%(d*8.438430)
xxxtemp20 ='jessatom2 x. %s'%(d*6.766760)
xxxtemp21 ='jessatom3 x. %s'%(d*5.695690)
xxxtemp22 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*8.918910))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*8.438430))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*6.766760))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*5.695690))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
cmd.select('Jab_1dnw_1_11_1_7', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
