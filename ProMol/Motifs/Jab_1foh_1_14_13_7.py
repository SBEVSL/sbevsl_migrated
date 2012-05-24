'''
FUNC:Jab_1foh_1_14_13_7
PDB:1foh
EC:1.14.13.7
RESI:asp,arg,tyr
LOCI:a-54,281,289;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. asp'
xxxtemp2 ='r. glu'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.521520)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.521520))
xxxtemp6 ='r. arg'
xxxtemp7 ='jessatom0 x. %s'%(d*8.558550)
xxxtemp8 ='jessatom1 x. %s'%(d*7.407400)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*8.558550))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*7.407400))
xxxtemp9 ='jessatom0 x. %s'%(d*7.857850)
xxxtemp10 ='jessatom1 x. %s'%(d*6.566560)
xxxtemp11 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp3+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*7.857850))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.566560))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp13 ='r. tyr'
xxxtemp14 ='jessatom0 x. %s'%(d*12.242230)
xxxtemp15 ='jessatom1 x. %s'%(d*11.231220)
xxxtemp16 ='jessatom2 x. %s'%(d*12.712700)
xxxtemp17 ='jessatom3 x. %s'%(d*11.931920)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*12.242230))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*11.231220))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*12.712700))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*11.931920))
xxxtemp18 ='jessatom0 x. %s'%(d*11.751740)
xxxtemp19 ='jessatom1 x. %s'%(d*10.880870)
xxxtemp20 ='jessatom2 x. %s'%(d*12.872860)
xxxtemp21 ='jessatom3 x. %s'%(d*12.172160)
xxxtemp22 ='jessatom4 x. %s'%(d*1.511510)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*11.751740))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*10.880870))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*12.872860))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*12.172160))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.511510))
cmd.select('Jab_1foh_1_14_13_7', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
