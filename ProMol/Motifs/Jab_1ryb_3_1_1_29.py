'''
FUNC:Jab_1ryb_3_1_1_29
PDB:1ryb
EC:3.1.1.29
RESI:asn,his,asp
LOCI:a-11,21,93;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. asn'
xxxtemp2 ='r. gln'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.521520)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.521520))
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*7.597590)
xxxtemp8 ='jessatom1 x. %s'%(d*7.307300)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*7.597590))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*7.307300))
xxxtemp9 ='jessatom0 x. %s'%(d*6.946940)
xxxtemp10 ='jessatom1 x. %s'%(d*6.426420)
xxxtemp11 ='jessatom2 x. %s'%(d*1.551550)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*6.946940))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.426420))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.551550))
xxxtemp13 ='r. asp'
xxxtemp14 ='r. glu'
xxxtemp15 ='jessatom0 x. %s'%(d*12.092080)
xxxtemp16 ='jessatom1 x. %s'%(d*12.272260)
xxxtemp17 ='jessatom2 x. %s'%(d*5.795790)
xxxtemp18 ='jessatom3 x. %s'%(d*6.936930)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp13+'))|(('+xxxtemp0+')&('+xxxtemp14+')))&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*12.092080))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*12.272260))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*5.795790))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*6.936930))
xxxtemp19 ='jessatom0 x. %s'%(d*11.231220)
xxxtemp20 ='jessatom1 x. %s'%(d*11.271260)
xxxtemp21 ='jessatom2 x. %s'%(d*4.434430)
xxxtemp22 ='jessatom3 x. %s'%(d*5.585580)
xxxtemp23 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp3+')&('+xxxtemp13+'))|(('+xxxtemp3+')&('+xxxtemp14+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*11.231220))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*11.271260))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*4.434430))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*5.585580))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1ryb_3_1_1_29', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
