'''
FUNC:Jfa_1kkt_3_2_1_113
PDB:1kkt
EC:3.2.1.113
RESI:glu,arg,asp,glu
LOCI:a-122,126,267,409;
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
xxxtemp13 ='jessatom0 x. %s'%(d*1.241240)
xxxtemp14 ='br. jessatom0'
xxxtemp15 ='jessatom1 x. %s'%(d*2.172170)
cmd.select('jessatom2', '((((('+xxxtemp9+')|('+xxxtemp10+'))&('+xxxtemp1+'))|((('+xxxtemp11+')|('+xxxtemp12+'))&('+xxxtemp2+')))&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*1.241240))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*2.172170))
xxxtemp16 ='n.  ne '
xxxtemp17 ='r. arg'
xxxtemp18 ='jessatom0 x. %s'%(d*3.983980)
xxxtemp19 ='jessatom1 x. %s'%(d*4.694690)
xxxtemp20 ='jessatom2 x. %s'%(d*2.842840)
cmd.select('jessatom3', '(('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*3.983980))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*4.694690))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*2.842840))
xxxtemp21 ='n.  nh1'
xxxtemp22 ='n.  nh2'
xxxtemp23 ='jessatom0 x. %s'%(d*5.495490)
xxxtemp24 ='jessatom1 x. %s'%(d*5.865860)
xxxtemp25 ='jessatom2 x. %s'%(d*4.614610)
xxxtemp26 ='jessatom3 x. %s'%(d*2.312310)
xxxtemp27 ='br. jessatom3'
cmd.select('jessatom4', '((('+xxxtemp21+')|('+xxxtemp22+'))&('+xxxtemp17+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*5.495490))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*5.865860))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*4.614610))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*2.312310))
xxxtemp28 ='n.  nh2'
xxxtemp29 ='n.  nh1'
xxxtemp30 ='jessatom0 x. %s'%(d*3.523520)
xxxtemp31 ='jessatom1 x. %s'%(d*3.653650)
xxxtemp32 ='jessatom2 x. %s'%(d*2.892890)
xxxtemp33 ='jessatom3 x. %s'%(d*2.302300)
xxxtemp34 ='br. jessatom3'
xxxtemp35 ='jessatom4 x. %s'%(d*2.292290)
cmd.select('jessatom5', '((('+xxxtemp28+')|('+xxxtemp29+'))&('+xxxtemp17+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*3.523520))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*3.653650))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*2.892890))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.302300))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*2.292290))
xxxtemp36 ='n.  cg '
xxxtemp37 ='jessatom0 x. %s'%(d*10.830820)
xxxtemp38 ='jessatom1 x. %s'%(d*10.050040)
xxxtemp39 ='jessatom2 x. %s'%(d*11.101090)
xxxtemp40 ='jessatom3 x. %s'%(d*12.872860)
xxxtemp41 ='jessatom4 x. %s'%(d*13.853840)
xxxtemp42 ='jessatom5 x. %s'%(d*12.042030)
cmd.select('jessatom6', '(((('+xxxtemp36+')&('+xxxtemp2+'))|(('+xxxtemp36+')&('+xxxtemp1+')))&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*10.830820))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*10.050040))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*11.101090))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*12.872860))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*13.853840))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*12.042030))
xxxtemp43 ='jessatom0 x. %s'%(d*10.230220)
xxxtemp44 ='jessatom1 x. %s'%(d*9.389380)
xxxtemp45 ='jessatom2 x. %s'%(d*10.480470)
xxxtemp46 ='jessatom3 x. %s'%(d*12.142130)
xxxtemp47 ='jessatom4 x. %s'%(d*12.962950)
xxxtemp48 ='jessatom5 x. %s'%(d*11.181170)
xxxtemp49 ='jessatom6 x. %s'%(d*1.251250)
xxxtemp50 ='br. jessatom6'
cmd.select('jessatom7', '((((('+xxxtemp5+')|('+xxxtemp6+'))&('+xxxtemp2+'))|((('+xxxtemp3+')|('+xxxtemp4+'))&('+xxxtemp1+')))&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*10.230220))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*9.389380))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*10.480470))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*12.142130))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*12.962950))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*11.181170))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.251250))
xxxtemp51 ='jessatom0 x. %s'%(d*10.390380)
xxxtemp52 ='jessatom1 x. %s'%(d*9.669660)
xxxtemp53 ='jessatom2 x. %s'%(d*10.730720)
xxxtemp54 ='jessatom3 x. %s'%(d*12.692680)
xxxtemp55 ='jessatom4 x. %s'%(d*13.843830)
xxxtemp56 ='jessatom5 x. %s'%(d*11.951940)
xxxtemp57 ='br. jessatom6'
xxxtemp58 ='jessatom7 x. %s'%(d*2.182180)
cmd.select('jessatom8', '((((('+xxxtemp11+')|('+xxxtemp12+'))&('+xxxtemp2+'))|((('+xxxtemp9+')|('+xxxtemp10+'))&('+xxxtemp1+')))&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp49+')&('+xxxtemp57+')&('+xxxtemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*10.390380))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*9.669660))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*10.730720))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*12.692680))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*13.843830))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*11.951940))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*1.251250))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.182180))
xxxtemp59 ='jessatom0 x. %s'%(d*11.741730)
xxxtemp60 ='jessatom1 x. %s'%(d*11.011000)
xxxtemp61 ='jessatom2 x. %s'%(d*11.431420)
xxxtemp62 ='jessatom3 x. %s'%(d*11.541530)
xxxtemp63 ='jessatom4 x. %s'%(d*11.301290)
xxxtemp64 ='jessatom5 x. %s'%(d*10.500490)
xxxtemp65 ='jessatom6 x. %s'%(d*7.867860)
xxxtemp66 ='jessatom7 x. %s'%(d*6.836830)
xxxtemp67 ='jessatom8 x. %s'%(d*8.868860)
cmd.select('jessatom9', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+')))&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+')&('+xxxtemp62+')&('+xxxtemp63+')&('+xxxtemp64+')&('+xxxtemp65+')&('+xxxtemp66+')&('+xxxtemp67+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(d*11.741730))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(d*11.011000))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(d*11.431420))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(d*11.541530))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(d*11.301290))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(d*10.500490))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(d*7.867860))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(d*6.836830))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(d*8.868860))
xxxtemp68 ='jessatom0 x. %s'%(d*10.500490)
xxxtemp69 ='jessatom1 x. %s'%(d*9.789780)
xxxtemp70 ='jessatom2 x. %s'%(d*10.180170)
xxxtemp71 ='jessatom3 x. %s'%(d*10.360350)
xxxtemp72 ='jessatom4 x. %s'%(d*10.220210)
xxxtemp73 ='jessatom5 x. %s'%(d*9.339330)
xxxtemp74 ='jessatom6 x. %s'%(d*7.367360)
xxxtemp75 ='jessatom7 x. %s'%(d*6.296290)
xxxtemp76 ='jessatom8 x. %s'%(d*8.258250)
xxxtemp77 ='jessatom9 x. %s'%(d*1.251250)
xxxtemp78 ='br. jessatom9'
cmd.select('jessatom10', '((((('+xxxtemp3+')|('+xxxtemp4+'))&('+xxxtemp1+'))|((('+xxxtemp5+')|('+xxxtemp6+'))&('+xxxtemp2+')))&('+xxxtemp68+')&('+xxxtemp69+')&('+xxxtemp70+')&('+xxxtemp71+')&('+xxxtemp72+')&('+xxxtemp73+')&('+xxxtemp74+')&('+xxxtemp75+')&('+xxxtemp76+')&('+xxxtemp77+')&('+xxxtemp78+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(d*10.500490))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(d*9.789780))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(d*10.180170))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(d*10.360350))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(d*10.220210))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(d*9.339330))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(d*7.367360))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(d*6.296290))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(d*8.258250))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(d*1.251250))
xxxtemp79 ='jessatom0 x. %s'%(d*12.372360)
xxxtemp80 ='jessatom1 x. %s'%(d*11.601590)
xxxtemp81 ='jessatom2 x. %s'%(d*12.072060)
xxxtemp82 ='jessatom3 x. %s'%(d*12.072060)
xxxtemp83 ='jessatom4 x. %s'%(d*11.611600)
xxxtemp84 ='jessatom5 x. %s'%(d*10.890880)
xxxtemp85 ='jessatom6 x. %s'%(d*8.828820)
xxxtemp86 ='jessatom7 x. %s'%(d*7.757750)
xxxtemp87 ='jessatom8 x. %s'%(d*9.859850)
xxxtemp88 ='br. jessatom9'
xxxtemp89 ='jessatom10 x. %s'%(d*2.202200)
cmd.select('jessatom11', '((((('+xxxtemp9+')|('+xxxtemp10+'))&('+xxxtemp1+'))|((('+xxxtemp11+')|('+xxxtemp12+'))&('+xxxtemp2+')))&('+xxxtemp79+')&('+xxxtemp80+')&('+xxxtemp81+')&('+xxxtemp82+')&('+xxxtemp83+')&('+xxxtemp84+')&('+xxxtemp85+')&('+xxxtemp86+')&('+xxxtemp87+')&('+xxxtemp77+')&('+xxxtemp88+')&('+xxxtemp89+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(d*12.372360))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(d*11.601590))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(d*12.072060))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(d*12.072060))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(d*11.611600))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(d*10.890880))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(d*8.828820))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(d*7.757750))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(d*9.859850))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(d*1.251250))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(d*2.202200))
cmd.select('Jfa_1kkt_3_2_1_113', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
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
cmd.delete('temp62')
cmd.delete('temp63')
cmd.delete('temp64')
cmd.delete('temp65')
cmd.delete('temp66')
cmd.delete('temp67')
cmd.delete('temp68')
cmd.delete('temp69')
cmd.delete('temp70')
cmd.delete('temp71')
cmd.delete('temp72')
cmd.delete('temp73')
cmd.delete('temp74')
cmd.delete('temp75')
cmd.delete('temp76')
cmd.delete('temp77')
cmd.delete('temp78')
cmd.delete('temp79')
cmd.delete('temp80')
cmd.delete('temp81')
cmd.delete('temp82')
cmd.delete('temp83')
cmd.delete('temp84')
cmd.delete('temp85')
cmd.delete('temp86')
cmd.delete('temp87')
cmd.delete('temp88')
cmd.delete('temp89')
