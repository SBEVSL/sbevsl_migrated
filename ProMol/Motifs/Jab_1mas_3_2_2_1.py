'''
FUNC:Jab_1mas_3_2_2_1
PDB:1mas
EC:3.2.2.1
RESI:asp,asn,his
LOCI:a-10,168,241;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. asp'
xxxtemp2 ='r. glu'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.511510)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.511510))
xxxtemp6 ='r. asn'
xxxtemp7 ='r. gln'
xxxtemp8 ='jessatom0 x. %s'%(d*12.622610)
xxxtemp9 ='jessatom1 x. %s'%(d*11.381370)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*12.622610))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*11.381370))
xxxtemp10 ='jessatom0 x. %s'%(d*11.751740)
xxxtemp11 ='jessatom1 x. %s'%(d*10.500490)
xxxtemp12 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp6+'))|(('+xxxtemp3+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*11.751740))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*10.500490))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp14 ='r. his'
xxxtemp15 ='jessatom0 x. %s'%(d*6.016010)
xxxtemp16 ='jessatom1 x. %s'%(d*4.844840)
xxxtemp17 ='jessatom2 x. %s'%(d*11.421410)
xxxtemp18 ='jessatom3 x. %s'%(d*10.350340)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*6.016010))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*4.844840))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*11.421410))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*10.350340))
xxxtemp19 ='jessatom0 x. %s'%(d*6.276270)
xxxtemp20 ='jessatom1 x. %s'%(d*4.884880)
xxxtemp21 ='jessatom2 x. %s'%(d*10.100090)
xxxtemp22 ='jessatom3 x. %s'%(d*9.099090)
xxxtemp23 ='jessatom4 x. %s'%(d*1.511510)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp14+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*6.276270))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*4.884880))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*10.100090))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*9.099090))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.511510))
cmd.select('Jab_1mas_3_2_2_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
