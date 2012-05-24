'''
FUNC:Jfa_3lip_3_1_1_3
PDB:3lip
EC:3.1.1.3
RESI:ser,asp,his
LOCI:a-87,264,286;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. ser'
xxxtemp2 ='r. thr'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.541540)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.541540))
xxxtemp6 ='n.  og '
xxxtemp7 ='jessatom0 x. %s'%(d*2.472470)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*1.421420)
cmd.select('jessatom2', '(((('+xxxtemp6+')&('+xxxtemp1+'))|(('+xxxtemp6+')&('+xxxtemp2+')))&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*2.472470))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*1.421420))
xxxtemp10 ='n.  cg '
xxxtemp11 ='r. asp'
xxxtemp12 ='r. glu'
xxxtemp13 ='jessatom0 x. %s'%(d*8.258250)
xxxtemp14 ='jessatom1 x. %s'%(d*8.318310)
xxxtemp15 ='jessatom2 x. %s'%(d*7.837830)
cmd.select('jessatom3', '(((('+xxxtemp10+')&('+xxxtemp11+'))|(('+xxxtemp10+')&('+xxxtemp12+')))&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*8.258250))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*8.318310))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*7.837830))
xxxtemp16 ='n.  od1'
xxxtemp17 ='n.  od2'
xxxtemp18 ='n.  oe1'
xxxtemp19 ='n.  oe2'
xxxtemp20 ='jessatom0 x. %s'%(d*8.328320)
xxxtemp21 ='jessatom1 x. %s'%(d*8.298290)
xxxtemp22 ='jessatom2 x. %s'%(d*7.617610)
xxxtemp23 ='jessatom3 x. %s'%(d*1.241240)
xxxtemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+xxxtemp16+')|('+xxxtemp17+'))&('+xxxtemp11+'))|((('+xxxtemp18+')|('+xxxtemp19+'))&('+xxxtemp12+')))&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.328320))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*8.298290))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*7.617610))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.241240))
xxxtemp25 ='n.  od2'
xxxtemp26 ='n.  od1'
xxxtemp27 ='n.  oe2'
xxxtemp28 ='n.  oe1'
xxxtemp29 ='jessatom0 x. %s'%(d*7.237230)
xxxtemp30 ='jessatom1 x. %s'%(d*7.417410)
xxxtemp31 ='jessatom2 x. %s'%(d*7.097090)
xxxtemp32 ='jessatom3 x. %s'%(d*1.251250)
xxxtemp33 ='br. jessatom3'
xxxtemp34 ='jessatom4 x. %s'%(d*2.152150)
cmd.select('jessatom5', '((((('+xxxtemp25+')|('+xxxtemp26+'))&('+xxxtemp11+'))|((('+xxxtemp27+')|('+xxxtemp28+'))&('+xxxtemp12+')))&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*7.237230))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*7.417410))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*7.097090))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*1.251250))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*2.152150))
xxxtemp35 ='r. his'
xxxtemp36 ='jessatom0 x. %s'%(d*6.156150)
xxxtemp37 ='jessatom1 x. %s'%(d*5.525520)
xxxtemp38 ='jessatom2 x. %s'%(d*4.974970)
xxxtemp39 ='jessatom3 x. %s'%(d*4.074070)
xxxtemp40 ='jessatom4 x. %s'%(d*4.024020)
xxxtemp41 ='jessatom5 x. %s'%(d*3.823820)
cmd.select('jessatom6', '(('+xxxtemp10+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*6.156150))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*5.525520))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*4.974970))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*4.074070))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*4.024020))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*3.823820))
xxxtemp42 ='n.  nd1'
xxxtemp43 ='jessatom0 x. %s'%(d*5.365360)
xxxtemp44 ='jessatom1 x. %s'%(d*5.055050)
xxxtemp45 ='jessatom2 x. %s'%(d*4.614610)
xxxtemp46 ='jessatom3 x. %s'%(d*3.493490)
xxxtemp47 ='jessatom4 x. %s'%(d*3.573570)
xxxtemp48 ='jessatom5 x. %s'%(d*2.902900)
xxxtemp49 ='jessatom6 x. %s'%(d*1.391390)
xxxtemp50 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp42+')&('+xxxtemp35+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*5.365360))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*5.055050))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*4.614610))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*3.493490))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*3.573570))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*2.902900))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.391390))
xxxtemp51 ='n.  ne2'
xxxtemp52 ='jessatom0 x. %s'%(d*4.244240)
xxxtemp53 ='jessatom1 x. %s'%(d*3.443440)
xxxtemp54 ='jessatom2 x. %s'%(d*2.782780)
xxxtemp55 ='jessatom3 x. %s'%(d*5.545540)
xxxtemp56 ='jessatom4 x. %s'%(d*5.385380)
xxxtemp57 ='jessatom5 x. %s'%(d*4.974970)
xxxtemp58 ='jessatom6 x. %s'%(d*2.192190)
xxxtemp59 ='br. jessatom6'
xxxtemp60 ='jessatom7 x. %s'%(d*2.132130)
cmd.select('jessatom8', '(('+xxxtemp51+')&('+xxxtemp35+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*4.244240))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*3.443440))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*2.782780))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*5.545540))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*5.385380))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*4.974970))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*2.192190))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.132130))
cmd.select('Jfa_3lip_3_1_1_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
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
cmd.delete('temp56')
cmd.delete('temp57')
cmd.delete('temp58')
cmd.delete('temp59')
cmd.delete('temp60')
