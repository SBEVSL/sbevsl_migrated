'''
FUNC:Jab_1avw_3_4_21_4
PDB:1avw
EC:3.4.21.4
RESI:his,asp,ser
LOCI:a-57,102,195;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. his'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. his'
xxxtemp4 ='jessatom0 x. %s'%(d*1.541540)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.541540))
xxxtemp6 ='r. asp'
xxxtemp7 ='r. glu'
xxxtemp8 ='jessatom0 x. %s'%(d*6.536530)
xxxtemp9 ='jessatom1 x. %s'%(d*6.486480)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*6.536530))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*6.486480))
xxxtemp10 ='jessatom0 x. %s'%(d*6.246240)
xxxtemp11 ='jessatom1 x. %s'%(d*5.855850)
xxxtemp12 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*6.246240))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*5.855850))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp14 ='r. ser'
xxxtemp15 ='r. thr'
xxxtemp16 ='jessatom0 x. %s'%(d*8.378370)
xxxtemp17 ='jessatom1 x. %s'%(d*7.877870)
xxxtemp18 ='jessatom2 x. %s'%(d*10.230220)
xxxtemp19 ='jessatom3 x. %s'%(d*9.269260)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp14+'))|(('+xxxtemp0+')&('+xxxtemp15+')))&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.378370))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*7.877870))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*10.230220))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*9.269260))
xxxtemp20 ='jessatom0 x. %s'%(d*7.197190)
xxxtemp21 ='jessatom1 x. %s'%(d*6.656650)
xxxtemp22 ='jessatom2 x. %s'%(d*9.869860)
xxxtemp23 ='jessatom3 x. %s'%(d*8.888880)
xxxtemp24 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp14+'))|(('+xxxtemp2+')&('+xxxtemp15+')))&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*7.197190))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*6.656650))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*9.869860))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*8.888880))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_1avw_3_4_21_4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
