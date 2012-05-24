'''
FUNC:Jab_5yas_4_1_2_39
PDB:5yas
EC:4.1.2.39
RESI:thr,ser,asp,his
LOCI:a-11,80,207,235;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. ser'
xxxtemp2 ='r. thr'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. asp'
xxxtemp7 ='r. glu'
xxxtemp8 ='jessatom0 x. %s'%(d*10.690680)
xxxtemp9 ='jessatom1 x. %s'%(d*10.380370)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*10.690680))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*10.380370))
xxxtemp10 ='jessatom0 x. %s'%(d*9.549540)
xxxtemp11 ='jessatom1 x. %s'%(d*9.389380)
xxxtemp12 ='jessatom2 x. %s'%(d*1.501500)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp6+'))|(('+xxxtemp3+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*9.549540))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*9.389380))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.501500))
xxxtemp14 ='r. his'
xxxtemp15 ='jessatom0 x. %s'%(d*8.148140)
xxxtemp16 ='jessatom1 x. %s'%(d*7.497490)
xxxtemp17 ='jessatom2 x. %s'%(d*4.584580)
xxxtemp18 ='jessatom3 x. %s'%(d*4.504500)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.148140))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*7.497490))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*4.584580))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*4.504500))
xxxtemp19 ='jessatom0 x. %s'%(d*7.737730)
xxxtemp20 ='jessatom1 x. %s'%(d*6.906900)
xxxtemp21 ='jessatom2 x. %s'%(d*4.844840)
xxxtemp22 ='jessatom3 x. %s'%(d*4.774770)
xxxtemp23 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp14+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*7.737730))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*6.906900))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*4.844840))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*4.774770))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_5yas_4_1_2_39', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
