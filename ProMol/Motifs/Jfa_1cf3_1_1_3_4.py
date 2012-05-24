'''
FUNC:Jfa_1cf3_1_1_3_4
PDB:1cf3
EC:1.1.3.4
RESI:glu,his,his
LOCI:a-412,516,559;
'''
xxxtemp0 ='n.  cd '
xxxtemp1 ='r. glu'
xxxtemp2 ='r. asp'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  oe1'
xxxtemp4 ='n.  oe2'
xxxtemp5 ='n.  od1'
xxxtemp6 ='n.  od2'
xxxtemp7 ='jessatom0 x. %s'%(d*1.251250)
xxxtemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+xxxtemp3+')|('+xxxtemp4+'))&('+xxxtemp1+'))|((('+xxxtemp5+')|('+xxxtemp6+'))&('+xxxtemp2+')))&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.251250))
xxxtemp9 ='n.  oe2'
xxxtemp10 ='n.  oe1'
xxxtemp11 ='n.  od2'
xxxtemp12 ='n.  od1'
xxxtemp13 ='jessatom0 x. %s'%(d*1.261260)
xxxtemp14 ='br. jessatom0'
xxxtemp15 ='jessatom1 x. %s'%(d*2.212210)
cmd.select('jessatom2', '((((('+xxxtemp9+')|('+xxxtemp10+'))&('+xxxtemp1+'))|((('+xxxtemp11+')|('+xxxtemp12+'))&('+xxxtemp2+')))&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*1.261260))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*2.212210))
xxxtemp16 ='n.  cg '
xxxtemp17 ='r. his'
xxxtemp18 ='jessatom0 x. %s'%(d*9.309300)
xxxtemp19 ='jessatom1 x. %s'%(d*8.268260)
xxxtemp20 ='jessatom2 x. %s'%(d*9.629620)
cmd.select('jessatom3', '(('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*9.309300))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*8.268260))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*9.629620))
xxxtemp21 ='n.  nd1'
xxxtemp22 ='jessatom0 x. %s'%(d*8.058050)
xxxtemp23 ='jessatom1 x. %s'%(d*6.976970)
xxxtemp24 ='jessatom2 x. %s'%(d*8.458450)
xxxtemp25 ='jessatom3 x. %s'%(d*1.391390)
xxxtemp26 ='br. jessatom3'
cmd.select('jessatom4', '(('+xxxtemp21+')&('+xxxtemp17+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.058050))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*6.976970))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*8.458450))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.391390))
xxxtemp27 ='n.  ne2'
xxxtemp28 ='jessatom0 x. %s'%(d*8.408400)
xxxtemp29 ='jessatom1 x. %s'%(d*7.467460)
xxxtemp30 ='jessatom2 x. %s'%(d*8.478470)
xxxtemp31 ='jessatom3 x. %s'%(d*2.192190)
xxxtemp32 ='br. jessatom3'
xxxtemp33 ='jessatom4 x. %s'%(d*2.162160)
cmd.select('jessatom5', '(('+xxxtemp27+')&('+xxxtemp17+')&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*8.408400))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*7.467460))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*8.478470))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.192190))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*2.162160))
xxxtemp34 ='jessatom0 x. %s'%(d*5.215210)
xxxtemp35 ='jessatom1 x. %s'%(d*4.754750)
xxxtemp36 ='jessatom2 x. %s'%(d*4.734730)
xxxtemp37 ='jessatom3 x. %s'%(d*7.207200)
xxxtemp38 ='jessatom4 x. %s'%(d*6.246240)
xxxtemp39 ='jessatom5 x. %s'%(d*5.345340)
cmd.select('jessatom6', '(('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*5.215210))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*4.754750))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*4.734730))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*7.207200))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*6.246240))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*5.345340))
xxxtemp40 ='jessatom1 x. %s'%(d*4.814810)
xxxtemp41 ='jessatom2 x. %s'%(d*4.684680)
xxxtemp42 ='jessatom3 x. %s'%(d*6.666660)
xxxtemp43 ='jessatom4 x. %s'%(d*5.825820)
xxxtemp44 ='jessatom5 x. %s'%(d*4.794790)
xxxtemp45 ='jessatom6 x. %s'%(d*1.381380)
xxxtemp46 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp21+')&('+xxxtemp17+')&('+xxxtemp34+')&('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*5.215210))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*4.814810))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*4.684680))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*6.666660))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*5.825820))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*4.794790))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.381380))
xxxtemp47 ='jessatom0 x. %s'%(d*3.363360)
xxxtemp48 ='jessatom1 x. %s'%(d*3.303300)
xxxtemp49 ='jessatom2 x. %s'%(d*2.642640)
xxxtemp50 ='jessatom3 x. %s'%(d*8.128120)
xxxtemp51 ='jessatom4 x. %s'%(d*7.067060)
xxxtemp52 ='jessatom5 x. %s'%(d*6.546540)
xxxtemp53 ='jessatom6 x. %s'%(d*2.202200)
xxxtemp54 ='br. jessatom6'
xxxtemp55 ='jessatom7 x. %s'%(d*2.152150)
cmd.select('jessatom8', '(('+xxxtemp27+')&('+xxxtemp17+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+')&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*3.363360))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*3.303300))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*2.642640))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*8.128120))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*7.067060))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*6.546540))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*2.202200))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.152150))
cmd.select('Jfa_1cf3_1_1_3_4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
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
cmd.delete('temp26')
cmd.delete('temp27')
cmd.delete('temp28')
cmd.delete('temp29')
cmd.delete('temp30')
cmd.delete('temp31')
cmd.delete('temp32')
cmd.delete('temp33')
cmd.delete('temp34')
cmd.delete('temp35')
cmd.delete('temp36')
cmd.delete('temp37')
cmd.delete('temp38')
cmd.delete('temp39')
cmd.delete('temp40')
cmd.delete('temp41')
cmd.delete('temp42')
cmd.delete('temp43')
cmd.delete('temp44')
cmd.delete('temp45')
cmd.delete('temp46')
cmd.delete('temp47')
cmd.delete('temp48')
cmd.delete('temp49')
cmd.delete('temp50')
cmd.delete('temp51')
cmd.delete('temp52')
cmd.delete('temp53')
cmd.delete('temp54')
cmd.delete('temp55')
