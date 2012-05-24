'''
FUNC:Jab_1diz_3_2_2_21
PDB:1diz
EC:3.2.2.21
RESI:tyr,asp,trp
LOCI:a-222,238,272;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. tyr'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. tyr'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. asp'
xxxtemp7 ='r. glu'
xxxtemp8 ='jessatom0 x. %s'%(d*9.319310)
xxxtemp9 ='jessatom1 x. %s'%(d*8.518510)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*9.319310))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*8.518510))
xxxtemp10 ='jessatom0 x. %s'%(d*8.638630)
xxxtemp11 ='jessatom1 x. %s'%(d*7.937930)
xxxtemp12 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*8.638630))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*7.937930))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp14 ='r. trp'
xxxtemp15 ='jessatom0 x. %s'%(d*13.293280)
xxxtemp16 ='jessatom1 x. %s'%(d*12.982970)
xxxtemp17 ='jessatom2 x. %s'%(d*10.080070)
xxxtemp18 ='jessatom3 x. %s'%(d*8.758750)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*13.293280))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*12.982970))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*10.080070))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*8.758750))
xxxtemp19 ='jessatom0 x. %s'%(d*12.042030)
xxxtemp20 ='jessatom1 x. %s'%(d*11.711700)
xxxtemp21 ='jessatom2 x. %s'%(d*9.659650)
xxxtemp22 ='jessatom3 x. %s'%(d*8.268260)
xxxtemp23 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp14+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*12.042030))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*11.711700))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*9.659650))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*8.268260))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1diz_3_2_2_21', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
