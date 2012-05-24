'''
FUNC:Jab_1gqn_4_2_1_10
PDB:1gqn
EC:4.2.1.10
RESI:glu,his,lys
LOCI:a-86,143,170;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. glu'
xxxtemp2 ='r. asp'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.561560)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.561560))
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*5.505500)
xxxtemp8 ='jessatom1 x. %s'%(d*4.894890)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*5.505500))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*4.894890))
xxxtemp9 ='jessatom0 x. %s'%(d*4.594590)
xxxtemp10 ='jessatom1 x. %s'%(d*4.054050)
xxxtemp11 ='jessatom2 x. %s'%(d*1.581580)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*4.594590))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*4.054050))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.581580))
xxxtemp13 ='r. lys'
xxxtemp14 ='jessatom0 x. %s'%(d*12.712700)
xxxtemp15 ='jessatom1 x. %s'%(d*11.421410)
xxxtemp16 ='jessatom2 x. %s'%(d*8.448440)
xxxtemp17 ='jessatom3 x. %s'%(d*8.928920)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*12.712700))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*11.421410))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*8.448440))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*8.928920))
xxxtemp18 ='jessatom0 x. %s'%(d*12.192180)
xxxtemp19 ='jessatom1 x. %s'%(d*10.880870)
xxxtemp20 ='jessatom2 x. %s'%(d*8.388380)
xxxtemp21 ='jessatom3 x. %s'%(d*8.598590)
xxxtemp22 ='jessatom4 x. %s'%(d*1.571570)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*12.192180))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*10.880870))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*8.388380))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*8.598590))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.571570))
cmd.select('Jab_1gqn_4_2_1_10', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
