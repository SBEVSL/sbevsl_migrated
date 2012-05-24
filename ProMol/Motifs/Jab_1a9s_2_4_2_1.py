'''
FUNC:Jab_1a9s_2_4_2_1
PDB:1a9s
EC:2.4.2.1
RESI:his,glu,asn
LOCI:a-86,89,243;
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
xxxtemp6 ='r. glu'
xxxtemp7 ='r. asp'
xxxtemp8 ='jessatom0 x. %s'%(d*5.665660)
xxxtemp9 ='jessatom1 x. %s'%(d*5.525520)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*5.665660))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*5.525520))
xxxtemp10 ='jessatom0 x. %s'%(d*5.045040)
xxxtemp11 ='jessatom1 x. %s'%(d*5.055050)
xxxtemp12 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*5.045040))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*5.055050))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp14 ='r. asn'
xxxtemp15 ='r. gln'
xxxtemp16 ='jessatom0 x. %s'%(d*19.759740)
xxxtemp17 ='jessatom1 x. %s'%(d*18.448430)
xxxtemp18 ='jessatom2 x. %s'%(d*22.092070)
xxxtemp19 ='jessatom3 x. %s'%(d*22.102080)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp14+'))|(('+xxxtemp0+')&('+xxxtemp15+')))&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*19.759740))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*18.448430))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*22.092070))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*22.102080))
xxxtemp20 ='jessatom0 x. %s'%(d*19.179160)
xxxtemp21 ='jessatom1 x. %s'%(d*17.807790)
xxxtemp22 ='jessatom2 x. %s'%(d*21.161140)
xxxtemp23 ='jessatom3 x. %s'%(d*21.231210)
xxxtemp24 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp14+'))|(('+xxxtemp2+')&('+xxxtemp15+')))&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*19.179160))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*17.807790))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*21.161140))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*21.231210))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1a9s_2_4_2_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
cmd.delete('temp25')
