'''
FUNC:Jfa_1fwa_3_5_1_5
PDB:1fwa
EC:3.5.1.5
RESI:his,asp,his,arg
LOCI:c-219,221,320,336;
'''
xxxtemp0 ='n.  cg '
xxxtemp1 ='r. his'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  nd1'
xxxtemp3 ='r. his'
xxxtemp4 ='jessatom0 x. %s'%(d*1.381380)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.381380))
xxxtemp6 ='n.  ne2'
xxxtemp7 ='jessatom0 x. %s'%(d*2.202200)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*2.142140)
cmd.select('jessatom2', '(('+xxxtemp6+')&('+xxxtemp3+')&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*2.202200))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*2.142140))
xxxtemp10 ='r. asp'
xxxtemp11 ='r. glu'
xxxtemp12 ='jessatom0 x. %s'%(d*4.764760)
xxxtemp13 ='jessatom1 x. %s'%(d*3.473470)
xxxtemp14 ='jessatom2 x. %s'%(d*4.564560)
cmd.select('jessatom3', '(((('+xxxtemp0+')&('+xxxtemp10+'))|(('+xxxtemp0+')&('+xxxtemp11+')))&('+xxxtemp12+')&('+xxxtemp13+')&('+xxxtemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*4.764760))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*3.473470))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*4.564560))
xxxtemp15 ='n.  od1'
xxxtemp16 ='n.  od2'
xxxtemp17 ='n.  oe1'
xxxtemp18 ='n.  oe2'
xxxtemp19 ='jessatom0 x. %s'%(d*5.025020)
xxxtemp20 ='jessatom1 x. %s'%(d*3.653650)
xxxtemp21 ='jessatom2 x. %s'%(d*4.794790)
xxxtemp22 ='jessatom3 x. %s'%(d*1.251250)
xxxtemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+xxxtemp15+')|('+xxxtemp16+'))&('+xxxtemp10+'))|((('+xxxtemp17+')|('+xxxtemp18+'))&('+xxxtemp11+')))&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*5.025020))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*3.653650))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*4.794790))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.251250))
xxxtemp24 ='n.  od2'
xxxtemp25 ='n.  od1'
xxxtemp26 ='n.  oe2'
xxxtemp27 ='n.  oe1'
xxxtemp28 ='jessatom0 x. %s'%(d*5.185180)
xxxtemp29 ='jessatom1 x. %s'%(d*3.993990)
xxxtemp30 ='jessatom2 x. %s'%(d*4.524520)
xxxtemp31 ='br. jessatom3'
xxxtemp32 ='jessatom4 x. %s'%(d*2.192190)
cmd.select('jessatom5', '((((('+xxxtemp24+')|('+xxxtemp25+'))&('+xxxtemp10+'))|((('+xxxtemp26+')|('+xxxtemp27+'))&('+xxxtemp11+')))&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp22+')&('+xxxtemp31+')&('+xxxtemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*5.185180))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*3.993990))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*4.524520))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*1.251250))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*2.192190))
xxxtemp33 ='jessatom0 x. %s'%(d*7.807800)
xxxtemp34 ='jessatom1 x. %s'%(d*6.716710)
xxxtemp35 ='jessatom2 x. %s'%(d*6.136130)
xxxtemp36 ='jessatom3 x. %s'%(d*4.924920)
xxxtemp37 ='jessatom4 x. %s'%(d*4.784780)
xxxtemp38 ='jessatom5 x. %s'%(d*4.144140)
cmd.select('jessatom6', '(('+xxxtemp0+')&('+xxxtemp3+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*7.807800))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*6.716710))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*6.136130))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*4.924920))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*4.784780))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*4.144140))
xxxtemp39 ='jessatom0 x. %s'%(d*6.476470)
xxxtemp40 ='jessatom1 x. %s'%(d*5.445440)
xxxtemp41 ='jessatom2 x. %s'%(d*4.784780)
xxxtemp42 ='jessatom3 x. %s'%(d*4.064060)
xxxtemp43 ='jessatom4 x. %s'%(d*4.054050)
xxxtemp44 ='jessatom5 x. %s'%(d*3.273270)
xxxtemp45 ='jessatom6 x. %s'%(d*1.381380)
xxxtemp46 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*6.476470))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*5.445440))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*4.784780))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*4.064060))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*4.054050))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*3.273270))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.381380))
xxxtemp47 ='jessatom0 x. %s'%(d*7.467460)
xxxtemp48 ='jessatom1 x. %s'%(d*6.616610)
xxxtemp49 ='jessatom2 x. %s'%(d*5.515510)
xxxtemp50 ='jessatom3 x. %s'%(d*5.965960)
xxxtemp51 ='jessatom4 x. %s'%(d*5.695690)
xxxtemp52 ='jessatom5 x. %s'%(d*5.335330)
xxxtemp53 ='jessatom6 x. %s'%(d*2.202200)
xxxtemp54 ='br. jessatom6'
xxxtemp55 ='jessatom7 x. %s'%(d*2.142140)
cmd.select('jessatom8', '(('+xxxtemp6+')&('+xxxtemp3+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+')&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*7.467460))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*6.616610))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*5.515510))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*5.965960))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*5.695690))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*5.335330))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*2.202200))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.142140))
xxxtemp56 ='n.  ne '
xxxtemp57 ='r. arg'
xxxtemp58 ='jessatom0 x. %s'%(d*10.320310)
xxxtemp59 ='jessatom1 x. %s'%(d*9.449440)
xxxtemp60 ='jessatom2 x. %s'%(d*8.828820)
xxxtemp61 ='jessatom3 x. %s'%(d*9.049040)
xxxtemp62 ='jessatom4 x. %s'%(d*8.158150)
xxxtemp63 ='jessatom5 x. %s'%(d*8.978970)
xxxtemp64 ='jessatom6 x. %s'%(d*6.046040)
xxxtemp65 ='jessatom7 x. %s'%(d*6.466460)
xxxtemp66 ='jessatom8 x. %s'%(d*4.924920)
cmd.select('jessatom9', '(('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+')&('+xxxtemp62+')&('+xxxtemp63+')&('+xxxtemp64+')&('+xxxtemp65+')&('+xxxtemp66+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(d*10.320310))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(d*9.449440))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(d*8.828820))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(d*9.049040))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(d*8.158150))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(d*8.978970))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(d*6.046040))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(d*6.466460))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(d*4.924920))
xxxtemp67 ='n.  nh1'
xxxtemp68 ='n.  nh2'
xxxtemp69 ='jessatom0 x. %s'%(d*8.568560)
xxxtemp70 ='jessatom1 x. %s'%(d*7.547540)
xxxtemp71 ='jessatom2 x. %s'%(d*7.147140)
xxxtemp72 ='jessatom3 x. %s'%(d*6.786780)
xxxtemp73 ='jessatom4 x. %s'%(d*5.905900)
xxxtemp74 ='jessatom5 x. %s'%(d*6.716710)
xxxtemp75 ='jessatom6 x. %s'%(d*4.134130)
xxxtemp76 ='jessatom7 x. %s'%(d*4.464460)
xxxtemp77 ='jessatom8 x. %s'%(d*3.453450)
xxxtemp78 ='jessatom9 x. %s'%(d*2.302300)
xxxtemp79 ='br. jessatom9'
cmd.select('jessatom10', '((('+xxxtemp67+')|('+xxxtemp68+'))&('+xxxtemp57+')&('+xxxtemp69+')&('+xxxtemp70+')&('+xxxtemp71+')&('+xxxtemp72+')&('+xxxtemp73+')&('+xxxtemp74+')&('+xxxtemp75+')&('+xxxtemp76+')&('+xxxtemp77+')&('+xxxtemp78+')&('+xxxtemp79+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(d*8.568560))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(d*7.547540))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(d*7.147140))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(d*6.786780))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(d*5.905900))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(d*6.716710))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(d*4.134130))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(d*4.464460))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(d*3.453450))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(d*2.302300))
xxxtemp80 ='n.  nh2'
xxxtemp81 ='n.  nh1'
xxxtemp82 ='jessatom0 x. %s'%(d*8.918910)
xxxtemp83 ='jessatom1 x. %s'%(d*8.148140)
xxxtemp84 ='jessatom2 x. %s'%(d*7.137130)
xxxtemp85 ='jessatom3 x. %s'%(d*7.977970)
xxxtemp86 ='jessatom4 x. %s'%(d*7.327320)
xxxtemp87 ='jessatom5 x. %s'%(d*7.687680)
xxxtemp88 ='jessatom6 x. %s'%(d*4.634630)
xxxtemp89 ='jessatom7 x. %s'%(d*4.834830)
xxxtemp90 ='jessatom8 x. %s'%(d*2.952950)
xxxtemp91 ='br. jessatom9'
xxxtemp92 ='jessatom10 x. %s'%(d*2.282280)
cmd.select('jessatom11', '((('+xxxtemp80+')|('+xxxtemp81+'))&('+xxxtemp57+')&('+xxxtemp82+')&('+xxxtemp83+')&('+xxxtemp84+')&('+xxxtemp85+')&('+xxxtemp86+')&('+xxxtemp87+')&('+xxxtemp88+')&('+xxxtemp89+')&('+xxxtemp90+')&('+xxxtemp78+')&('+xxxtemp91+')&('+xxxtemp92+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(d*8.918910))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(d*8.148140))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(d*7.137130))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(d*7.977970))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(d*7.327320))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(d*7.687680))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(d*4.634630))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(d*4.834830))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(d*2.952950))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(d*2.302300))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(d*2.282280))
cmd.select('Jfa_1fwa_3_5_1_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
