'''
FUNC:Jab_1a2f_1_11_1_5
PDB:1a2f
EC:1.11.1.5
RESI:arg,his,trp
LOCI:a-48,52,191;
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
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*6.196190)
xxxtemp8 ='jessatom1 x. %s'%(d*6.876870)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*6.196190))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*6.876870))
xxxtemp9 ='jessatom0 x. %s'%(d*5.825820)
xxxtemp10 ='jessatom1 x. %s'%(d*6.226220)
xxxtemp11 ='jessatom2 x. %s'%(d*1.491490)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*5.825820))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.226220))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.491490))
xxxtemp13 ='r. asn'
xxxtemp14 ='r. gln'
xxxtemp15 ='jessatom0 x. %s'%(d*9.309300)
xxxtemp16 ='jessatom1 x. %s'%(d*8.648640)
xxxtemp17 ='jessatom2 x. %s'%(d*7.337330)
xxxtemp18 ='jessatom3 x. %s'%(d*5.955950)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp13+'))|(('+xxxtemp0+')&('+xxxtemp14+')))&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*9.309300))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*8.648640))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*7.337330))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*5.955950))
xxxtemp19 ='jessatom0 x. %s'%(d*9.759750)
xxxtemp20 ='jessatom1 x. %s'%(d*9.299290)
xxxtemp21 ='jessatom2 x. %s'%(d*7.157150)
xxxtemp22 ='jessatom3 x. %s'%(d*5.835830)
xxxtemp23 ='jessatom4 x. %s'%(d*1.541540)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp13+'))|(('+xxxtemp2+')&('+xxxtemp14+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*9.759750))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*9.299290))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*7.157150))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*5.835830))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.541540))
cmd.select('Jab_1a2f_1_11_1_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
