'''
FUNC:Jfa_1diz_3_2_2_21
PDB:1diz
EC:3.2.2.21
RESI:tyr,asp,trp
LOCI:a-222,238,272;
'''
xxxtemp0 ='n.  ce1'
xxxtemp1 ='r. tyr'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cz '
xxxtemp3 ='r. tyr'
xxxtemp4 ='jessatom0 x. %s'%(d*1.401400)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.401400))
xxxtemp6 ='n.  oh '
xxxtemp7 ='jessatom0 x. %s'%(d*2.412410)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*1.371370)
cmd.select('jessatom2', '(('+xxxtemp6+')&('+xxxtemp3+')&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*2.412410))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*1.371370))
xxxtemp10 ='n.  cg '
xxxtemp11 ='r. asp'
xxxtemp12 ='r. glu'
xxxtemp13 ='jessatom0 x. %s'%(d*7.677670)
xxxtemp14 ='jessatom1 x. %s'%(d*8.238230)
xxxtemp15 ='jessatom2 x. %s'%(d*8.808800)
cmd.select('jessatom3', '(((('+xxxtemp10+')&('+xxxtemp11+'))|(('+xxxtemp10+')&('+xxxtemp12+')))&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*7.677670))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*8.238230))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*8.808800))
xxxtemp16 ='n.  od1'
xxxtemp17 ='n.  od2'
xxxtemp18 ='n.  oe1'
xxxtemp19 ='n.  oe2'
xxxtemp20 ='jessatom0 x. %s'%(d*6.856850)
xxxtemp21 ='jessatom1 x. %s'%(d*7.277270)
xxxtemp22 ='jessatom2 x. %s'%(d*7.867860)
xxxtemp23 ='jessatom3 x. %s'%(d*1.251250)
xxxtemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+xxxtemp16+')|('+xxxtemp17+'))&('+xxxtemp11+'))|((('+xxxtemp18+')|('+xxxtemp19+'))&('+xxxtemp12+')))&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*6.856850))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*7.277270))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*7.867860))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.251250))
xxxtemp25 ='n.  od2'
xxxtemp26 ='n.  od1'
xxxtemp27 ='n.  oe2'
xxxtemp28 ='n.  oe1'
xxxtemp29 ='jessatom0 x. %s'%(d*8.208200)
xxxtemp30 ='jessatom1 x. %s'%(d*8.768760)
xxxtemp31 ='jessatom2 x. %s'%(d*9.189180)
xxxtemp32 ='jessatom3 x. %s'%(d*1.241240)
xxxtemp33 ='br. jessatom3'
xxxtemp34 ='jessatom4 x. %s'%(d*2.192190)
cmd.select('jessatom5', '((((('+xxxtemp25+')|('+xxxtemp26+'))&('+xxxtemp11+'))|((('+xxxtemp27+')|('+xxxtemp28+'))&('+xxxtemp12+')))&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*8.208200))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*8.768760))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*9.189180))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*1.241240))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*2.192190))
xxxtemp35 ='n.  ne1'
xxxtemp36 ='r. trp'
xxxtemp37 ='jessatom0 x. %s'%(d*7.767760)
xxxtemp38 ='jessatom1 x. %s'%(d*8.528520)
xxxtemp39 ='jessatom2 x. %s'%(d*8.728720)
xxxtemp40 ='jessatom3 x. %s'%(d*3.723720)
xxxtemp41 ='jessatom4 x. %s'%(d*4.344340)
xxxtemp42 ='jessatom5 x. %s'%(d*2.882880)
cmd.select('jessatom6', '(('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*7.767760))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*8.528520))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*8.728720))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*3.723720))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*4.344340))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*2.882880))
xxxtemp43 ='n.  cz2'
xxxtemp44 ='jessatom0 x. %s'%(d*5.325320)
xxxtemp45 ='jessatom1 x. %s'%(d*6.196190)
xxxtemp46 ='jessatom2 x. %s'%(d*6.576570)
xxxtemp47 ='jessatom3 x. %s'%(d*3.693690)
xxxtemp48 ='jessatom4 x. %s'%(d*3.703700)
xxxtemp49 ='jessatom5 x. %s'%(d*3.643640)
xxxtemp50 ='jessatom6 x. %s'%(d*2.512510)
xxxtemp51 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp43+')&('+xxxtemp36+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+')&('+xxxtemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*5.325320))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*6.196190))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*6.576570))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*3.693690))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*3.703700))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*3.643640))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*2.512510))
xxxtemp52 ='n.  ch2'
xxxtemp53 ='jessatom0 x. %s'%(d*4.204200)
xxxtemp54 ='jessatom1 x. %s'%(d*5.165160)
xxxtemp55 ='jessatom2 x. %s'%(d*5.525520)
xxxtemp56 ='jessatom3 x. %s'%(d*4.894890)
xxxtemp57 ='jessatom4 x. %s'%(d*4.674670)
xxxtemp58 ='jessatom5 x. %s'%(d*4.964960)
xxxtemp59 ='jessatom6 x. %s'%(d*3.703700)
xxxtemp60 ='br. jessatom6'
xxxtemp61 ='jessatom7 x. %s'%(d*1.371370)
cmd.select('jessatom8', '(('+xxxtemp52+')&('+xxxtemp36+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*4.204200))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*5.165160))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*5.525520))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*4.894890))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*4.674670))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*4.964960))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*3.703700))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*1.371370))
cmd.select('Jfa_1diz_3_2_2_21', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
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
cmd.delete('temp61')
