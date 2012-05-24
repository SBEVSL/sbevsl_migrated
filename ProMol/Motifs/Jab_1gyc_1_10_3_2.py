'''
FUNC:Jab_1gyc_1_10_3_2
PDB:1gyc
EC:1.10.3.2
RESI:his,cys,his
LOCI:a-452,453,454;
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
xxxtemp6 ='r. cys'
xxxtemp7 ='jessatom0 x. %s'%(d*3.773770)
xxxtemp8 ='jessatom1 x. %s'%(d*4.294290)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*3.773770))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*4.294290))
xxxtemp9 ='jessatom0 x. %s'%(d*4.834830)
xxxtemp10 ='jessatom1 x. %s'%(d*5.265260)
xxxtemp11 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*4.834830))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*5.265260))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp13 ='jessatom0 x. %s'%(d*6.186180)
xxxtemp14 ='jessatom1 x. %s'%(d*6.076070)
xxxtemp15 ='jessatom2 x. %s'%(d*3.803800)
xxxtemp16 ='jessatom3 x. %s'%(d*4.654650)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*6.186180))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*6.076070))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*3.803800))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*4.654650))
xxxtemp17 ='jessatom0 x. %s'%(d*6.846840)
xxxtemp18 ='jessatom1 x. %s'%(d*6.856850)
xxxtemp19 ='jessatom2 x. %s'%(d*4.834830)
xxxtemp20 ='jessatom3 x. %s'%(d*5.865860)
xxxtemp21 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*6.846840))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*6.856850))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*4.834830))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*5.865860))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1gyc_1_10_3_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
