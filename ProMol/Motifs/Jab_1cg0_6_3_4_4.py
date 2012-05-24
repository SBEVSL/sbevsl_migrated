'''
FUNC:Jab_1cg0_6_3_4_4
PDB:1cg0
EC:6.3.4.4
RESI:asp,his,gln
LOCI:a-13,41,224;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. asp'
xxxtemp2 ='r. glu'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.521520)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.521520))
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*7.617610)
xxxtemp8 ='jessatom1 x. %s'%(d*8.178170)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*7.617610))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*8.178170))
xxxtemp9 ='jessatom0 x. %s'%(d*8.268260)
xxxtemp10 ='jessatom1 x. %s'%(d*9.029020)
xxxtemp11 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*8.268260))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*9.029020))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp13 ='r. gln'
xxxtemp14 ='r. asn'
xxxtemp15 ='jessatom0 x. %s'%(d*6.946940)
xxxtemp16 ='jessatom1 x. %s'%(d*7.677670)
xxxtemp17 ='jessatom2 x. %s'%(d*9.869860)
xxxtemp18 ='jessatom3 x. %s'%(d*9.629620)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp13+'))|(('+xxxtemp0+')&('+xxxtemp14+')))&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*6.946940))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*7.677670))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*9.869860))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*9.629620))
xxxtemp19 ='jessatom0 x. %s'%(d*8.238230)
xxxtemp20 ='jessatom1 x. %s'%(d*8.818810)
xxxtemp21 ='jessatom2 x. %s'%(d*11.051040)
xxxtemp22 ='jessatom3 x. %s'%(d*10.800790)
xxxtemp23 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp3+')&('+xxxtemp13+'))|(('+xxxtemp3+')&('+xxxtemp14+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*8.238230))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*8.818810))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*11.051040))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*10.800790))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_1cg0_6_3_4_4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
