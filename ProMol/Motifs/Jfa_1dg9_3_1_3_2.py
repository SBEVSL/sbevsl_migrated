'''
FUNC:Jfa_1dg9_3_1_3_2
PDB:1dg9
EC:3.1.3.2
RESI:cys,cys,arg,asp
LOCI:a-12,17,18,129;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. cys'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. cys'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='n.  sg '
xxxtemp7 ='jessatom0 x. %s'%(d*2.772770)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*1.821820)
cmd.select('jessatom2', '(('+xxxtemp6+')&('+xxxtemp3+')&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*2.772770))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*1.821820))
xxxtemp10 ='jessatom0 x. %s'%(d*8.088080)
xxxtemp11 ='jessatom1 x. %s'%(d*6.706700)
xxxtemp12 ='jessatom2 x. %s'%(d*5.445440)
cmd.select('jessatom3', '(('+xxxtemp0+')&('+xxxtemp3+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*8.088080))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.706700))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*5.445440))
xxxtemp13 ='jessatom0 x. %s'%(d*8.428420)
xxxtemp14 ='jessatom1 x. %s'%(d*6.996990)
xxxtemp15 ='jessatom2 x. %s'%(d*5.995990)
xxxtemp16 ='jessatom3 x. %s'%(d*1.531530)
xxxtemp17 ='br. jessatom3'
cmd.select('jessatom4', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.428420))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*6.996990))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*5.995990))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.531530))
xxxtemp18 ='jessatom0 x. %s'%(d*9.539530)
xxxtemp19 ='jessatom1 x. %s'%(d*8.208200)
xxxtemp20 ='jessatom2 x. %s'%(d*7.117110)
xxxtemp21 ='jessatom3 x. %s'%(d*2.792790)
xxxtemp22 ='br. jessatom3'
xxxtemp23 ='jessatom4 x. %s'%(d*1.811810)
cmd.select('jessatom5', '(('+xxxtemp6+')&('+xxxtemp3+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*9.539530))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*8.208200))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*7.117110))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.792790))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.811810))
xxxtemp24 ='n.  ne '
xxxtemp25 ='r. arg'
xxxtemp26 ='jessatom0 x. %s'%(d*5.265260)
xxxtemp27 ='jessatom1 x. %s'%(d*3.963960)
xxxtemp28 ='jessatom2 x. %s'%(d*4.694690)
xxxtemp29 ='jessatom3 x. %s'%(d*6.046040)
xxxtemp30 ='jessatom4 x. %s'%(d*5.515510)
xxxtemp31 ='jessatom5 x. %s'%(d*6.756750)
cmd.select('jessatom6', '(('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+')&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*5.265260))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*3.963960))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*4.694690))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*6.046040))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*5.515510))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*6.756750))
xxxtemp32 ='n.  nh1'
xxxtemp33 ='n.  nh2'
xxxtemp34 ='jessatom0 x. %s'%(d*5.865860)
xxxtemp35 ='jessatom1 x. %s'%(d*5.035030)
xxxtemp36 ='jessatom2 x. %s'%(d*6.306300)
xxxtemp37 ='jessatom3 x. %s'%(d*8.358350)
xxxtemp38 ='jessatom4 x. %s'%(d*7.727720)
xxxtemp39 ='jessatom5 x. %s'%(d*8.808800)
xxxtemp40 ='jessatom6 x. %s'%(d*2.332330)
xxxtemp41 ='br. jessatom6'
cmd.select('jessatom7', '((('+xxxtemp32+')|('+xxxtemp33+'))&('+xxxtemp25+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*5.865860))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*5.035030))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*6.306300))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*8.358350))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*7.727720))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*8.808800))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*2.332330))
xxxtemp42 ='n.  nh2'
xxxtemp43 ='n.  nh1'
xxxtemp44 ='jessatom0 x. %s'%(d*4.564560)
xxxtemp45 ='jessatom1 x. %s'%(d*3.763760)
xxxtemp46 ='jessatom2 x. %s'%(d*4.784780)
xxxtemp47 ='jessatom3 x. %s'%(d*7.367360)
xxxtemp48 ='jessatom4 x. %s'%(d*6.826820)
xxxtemp49 ='jessatom5 x. %s'%(d*7.687680)
xxxtemp50 ='br. jessatom6'
xxxtemp51 ='jessatom7 x. %s'%(d*2.342340)
cmd.select('jessatom8', '((('+xxxtemp42+')|('+xxxtemp43+'))&('+xxxtemp25+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp40+')&('+xxxtemp50+')&('+xxxtemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*4.564560))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*3.763760))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*4.784780))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*7.367360))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*6.826820))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*7.687680))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*2.332330))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.342340))
xxxtemp52 ='n.  cg '
xxxtemp53 ='r. asp'
xxxtemp54 ='r. glu'
xxxtemp55 ='jessatom0 x. %s'%(d*8.538530)
xxxtemp56 ='jessatom1 x. %s'%(d*7.487480)
xxxtemp57 ='jessatom2 x. %s'%(d*7.767760)
xxxtemp58 ='jessatom3 x. %s'%(d*7.407400)
xxxtemp59 ='jessatom4 x. %s'%(d*6.146140)
xxxtemp60 ='jessatom5 x. %s'%(d*6.236230)
xxxtemp61 ='jessatom6 x. %s'%(d*4.494490)
xxxtemp62 ='jessatom7 x. %s'%(d*4.814810)
xxxtemp63 ='jessatom8 x. %s'%(d*4.244240)
cmd.select('jessatom9', '(((('+xxxtemp52+')&('+xxxtemp53+'))|(('+xxxtemp52+')&('+xxxtemp54+')))&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+')&('+xxxtemp62+')&('+xxxtemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(d*8.538530))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(d*7.487480))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(d*7.767760))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(d*7.407400))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(d*6.146140))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(d*6.236230))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(d*4.494490))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(d*4.814810))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(d*4.244240))
xxxtemp64 ='n.  od1'
xxxtemp65 ='n.  od2'
xxxtemp66 ='n.  oe1'
xxxtemp67 ='n.  oe2'
xxxtemp68 ='jessatom0 x. %s'%(d*8.388380)
xxxtemp69 ='jessatom2 x. %s'%(d*7.757750)
xxxtemp70 ='jessatom3 x. %s'%(d*7.877870)
xxxtemp71 ='jessatom4 x. %s'%(d*6.706700)
xxxtemp72 ='jessatom5 x. %s'%(d*6.636630)
xxxtemp73 ='jessatom6 x. %s'%(d*5.035030)
xxxtemp74 ='jessatom7 x. %s'%(d*5.225220)
xxxtemp75 ='jessatom8 x. %s'%(d*4.224220)
xxxtemp76 ='jessatom9 x. %s'%(d*1.211210)
xxxtemp77 ='br. jessatom9'
cmd.select('jessatom10', '((((('+xxxtemp64+')|('+xxxtemp65+'))&('+xxxtemp53+'))|((('+xxxtemp66+')|('+xxxtemp67+'))&('+xxxtemp54+')))&('+xxxtemp68+')&('+xxxtemp56+')&('+xxxtemp69+')&('+xxxtemp70+')&('+xxxtemp71+')&('+xxxtemp72+')&('+xxxtemp73+')&('+xxxtemp74+')&('+xxxtemp75+')&('+xxxtemp76+')&('+xxxtemp77+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(d*8.388380))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(d*7.487480))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(d*7.757750))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(d*7.877870))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(d*6.706700))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(d*6.636630))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(d*5.035030))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(d*5.225220))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(d*4.224220))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(d*1.211210))
xxxtemp78 ='n.  od2'
xxxtemp79 ='n.  od1'
xxxtemp80 ='n.  oe2'
xxxtemp81 ='n.  oe1'
xxxtemp82 ='jessatom0 x. %s'%(d*8.868860)
xxxtemp83 ='jessatom1 x. %s'%(d*7.667660)
xxxtemp84 ='jessatom2 x. %s'%(d*7.687680)
xxxtemp85 ='jessatom3 x. %s'%(d*6.456450)
xxxtemp86 ='jessatom4 x. %s'%(d*5.085080)
xxxtemp87 ='jessatom5 x. %s'%(d*5.095090)
xxxtemp88 ='jessatom6 x. %s'%(d*4.604600)
xxxtemp89 ='jessatom7 x. %s'%(d*5.455450)
xxxtemp90 ='jessatom8 x. %s'%(d*4.884880)
xxxtemp91 ='jessatom9 x. %s'%(d*1.321320)
xxxtemp92 ='br. jessatom9'
xxxtemp93 ='jessatom10 x. %s'%(d*2.252250)
cmd.select('jessatom11', '((((('+xxxtemp78+')|('+xxxtemp79+'))&('+xxxtemp53+'))|((('+xxxtemp80+')|('+xxxtemp81+'))&('+xxxtemp54+')))&('+xxxtemp82+')&('+xxxtemp83+')&('+xxxtemp84+')&('+xxxtemp85+')&('+xxxtemp86+')&('+xxxtemp87+')&('+xxxtemp88+')&('+xxxtemp89+')&('+xxxtemp90+')&('+xxxtemp91+')&('+xxxtemp92+')&('+xxxtemp93+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(d*8.868860))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(d*7.667660))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(d*7.687680))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(d*6.456450))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(d*5.085080))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(d*5.095090))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(d*4.604600))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(d*5.455450))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(d*4.884880))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(d*1.321320))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(d*2.252250))
cmd.select('Jfa_1dg9_3_1_3_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
cmd.delete('temp90')
cmd.delete('temp91')
cmd.delete('temp92')
cmd.delete('temp93')
