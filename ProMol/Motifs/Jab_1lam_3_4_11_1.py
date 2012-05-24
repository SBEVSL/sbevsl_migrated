'''
FUNC:Jab_1lam_3_4_11_1
PDB:1lam
EC:3.4.11.1
RESI:asp,lys,arg
LOCI:a-255,262,336;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. asp'
xxxtemp2 ='r. glu'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.541540)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.541540))
xxxtemp6 ='r. lys'
xxxtemp7 ='jessatom0 x. %s'%(d*8.448440)
xxxtemp8 ='jessatom1 x. %s'%(d*8.518510)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*8.448440))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*8.518510))
xxxtemp9 ='jessatom0 x. %s'%(d*7.287280)
xxxtemp10 ='jessatom1 x. %s'%(d*7.317310)
xxxtemp11 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*7.287280))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*7.317310))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp13 ='r. arg'
xxxtemp14 ='jessatom0 x. %s'%(d*12.932920)
xxxtemp15 ='jessatom1 x. %s'%(d*11.801790)
xxxtemp16 ='jessatom2 x. %s'%(d*16.916900)
xxxtemp17 ='jessatom3 x. %s'%(d*16.356340)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*12.932920))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*11.801790))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*16.916900))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*16.356340))
xxxtemp18 ='jessatom0 x. %s'%(d*13.653640)
xxxtemp19 ='jessatom1 x. %s'%(d*12.462450)
xxxtemp20 ='jessatom2 x. %s'%(d*16.876860)
xxxtemp21 ='jessatom3 x. %s'%(d*16.406390)
xxxtemp22 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*13.653640))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*12.462450))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*16.876860))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*16.406390))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1lam_3_4_11_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
