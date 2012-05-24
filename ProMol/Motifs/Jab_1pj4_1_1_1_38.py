'''
FUNC:Jab_1pj4_1_1_1_38
PDB:1pj4
EC:1.1.1.38
RESI:tyr,lys,asp
LOCI:a-112,183,278;
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
xxxtemp6 ='r. lys'
xxxtemp7 ='jessatom0 x. %s'%(d*7.777770)
xxxtemp8 ='jessatom1 x. %s'%(d*7.407400)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*7.777770))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*7.407400))
xxxtemp9 ='jessatom0 x. %s'%(d*8.808800)
xxxtemp10 ='jessatom1 x. %s'%(d*8.478470)
xxxtemp11 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*8.808800))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*8.478470))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp13 ='r. asp'
xxxtemp14 ='r. glu'
xxxtemp15 ='jessatom0 x. %s'%(d*14.864850)
xxxtemp16 ='jessatom1 x. %s'%(d*14.224210)
xxxtemp17 ='jessatom2 x. %s'%(d*10.140130)
xxxtemp18 ='jessatom3 x. %s'%(d*8.908900)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp13+'))|(('+xxxtemp0+')&('+xxxtemp14+')))&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*14.864850))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*14.224210))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*10.140130))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*8.908900))
xxxtemp19 ='jessatom0 x. %s'%(d*13.543530)
xxxtemp20 ='jessatom1 x. %s'%(d*12.942930)
xxxtemp21 ='jessatom2 x. %s'%(d*8.618610)
xxxtemp22 ='jessatom3 x. %s'%(d*7.377370)
xxxtemp23 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp13+'))|(('+xxxtemp2+')&('+xxxtemp14+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*13.543530))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*12.942930))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*8.618610))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*7.377370))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
cmd.select('Jab_1pj4_1_1_1_38', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
