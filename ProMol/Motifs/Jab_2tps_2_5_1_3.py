'''
FUNC:Jab_2tps_2_5_1_3
PDB:2tps
EC:2.5.1.3
RESI:arg,ser,lys
LOCI:a-59,130,159;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. arg'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. arg'
xxxtemp4 ='jessatom0 x. %s'%(d*1.541540)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.541540))
xxxtemp6 ='r. ser'
xxxtemp7 ='r. thr'
xxxtemp8 ='jessatom0 x. %s'%(d*13.663650)
xxxtemp9 ='jessatom1 x. %s'%(d*12.572560)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*13.663650))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*12.572560))
xxxtemp10 ='jessatom0 x. %s'%(d*12.772760)
xxxtemp11 ='jessatom1 x. %s'%(d*11.661650)
xxxtemp12 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*12.772760))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*11.661650))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp14 ='r. lys'
xxxtemp15 ='jessatom0 x. %s'%(d*10.800790)
xxxtemp16 ='jessatom1 x. %s'%(d*9.639630)
xxxtemp17 ='jessatom2 x. %s'%(d*12.902890)
xxxtemp18 ='jessatom3 x. %s'%(d*11.521510)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*10.800790))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*9.639630))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*12.902890))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*11.521510))
xxxtemp19 ='jessatom0 x. %s'%(d*10.380370)
xxxtemp20 ='jessatom1 x. %s'%(d*9.129120)
xxxtemp21 ='jessatom2 x. %s'%(d*11.381370)
xxxtemp22 ='jessatom3 x. %s'%(d*10.010000)
xxxtemp23 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp14+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*10.380370))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*9.129120))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*11.381370))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*10.010000))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_2tps_2_5_1_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
