'''
FUNC:Jfa_1qnt_2_1_1_63
PDB:1qnt
EC:2.1.1.63
RESI:asn,cys,his,glu
LOCI:a-137,145,146,172;
'''
xxxtemp0 ='n.  cg '
xxxtemp1 ='r. asn'
xxxtemp2 ='r. gln'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  od1'
xxxtemp4 ='jessatom0 x. %s'%(d*1.231230)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.231230))
xxxtemp6 ='n.  nd2'
xxxtemp7 ='jessatom0 x. %s'%(d*1.321320)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*2.242240)
cmd.select('jessatom2', '(((('+xxxtemp6+')&('+xxxtemp1+'))|(('+xxxtemp6+')&('+xxxtemp2+')))&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*1.321320))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*2.242240))
xxxtemp10 ='n.  ca '
xxxtemp11 ='r. cys'
xxxtemp12 ='jessatom0 x. %s'%(d*5.815810)
xxxtemp13 ='jessatom1 x. %s'%(d*6.796790)
xxxtemp14 ='jessatom2 x. %s'%(d*4.794790)
cmd.select('jessatom3', '(('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+')&('+xxxtemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*5.815810))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.796790))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*4.794790))
xxxtemp15 ='n.  cb '
xxxtemp16 ='jessatom0 x. %s'%(d*4.814810)
xxxtemp17 ='jessatom1 x. %s'%(d*5.925920)
xxxtemp18 ='jessatom2 x. %s'%(d*3.933930)
xxxtemp19 ='jessatom3 x. %s'%(d*1.541540)
xxxtemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+xxxtemp15+')&('+xxxtemp11+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*4.814810))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*5.925920))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*3.933930))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.541540))
xxxtemp21 ='n.  sg '
xxxtemp22 ='jessatom0 x. %s'%(d*4.354350)
xxxtemp23 ='jessatom1 x. %s'%(d*5.495490)
xxxtemp24 ='jessatom2 x. %s'%(d*3.323320)
xxxtemp25 ='jessatom3 x. %s'%(d*2.832830)
xxxtemp26 ='br. jessatom3'
xxxtemp27 ='jessatom4 x. %s'%(d*1.801800)
cmd.select('jessatom5', '(('+xxxtemp21+')&('+xxxtemp11+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*4.354350))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*5.495490))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*3.323320))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.832830))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.801800))
xxxtemp28 ='r. his'
xxxtemp29 ='jessatom0 x. %s'%(d*9.439430)
xxxtemp30 ='jessatom1 x. %s'%(d*10.270260)
xxxtemp31 ='jessatom2 x. %s'%(d*8.128120)
xxxtemp32 ='jessatom3 x. %s'%(d*5.185180)
xxxtemp33 ='jessatom4 x. %s'%(d*6.126120)
xxxtemp34 ='jessatom5 x. %s'%(d*5.845840)
cmd.select('jessatom6', '(('+xxxtemp0+')&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*9.439430))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*10.270260))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*8.128120))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*5.185180))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*6.126120))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*5.845840))
xxxtemp35 ='n.  nd1'
xxxtemp36 ='jessatom0 x. %s'%(d*8.438430)
xxxtemp37 ='jessatom1 x. %s'%(d*9.179170)
xxxtemp38 ='jessatom2 x. %s'%(d*7.117110)
xxxtemp39 ='jessatom3 x. %s'%(d*4.754750)
xxxtemp40 ='jessatom4 x. %s'%(d*5.655650)
xxxtemp41 ='jessatom5 x. %s'%(d*5.265260)
xxxtemp42 ='jessatom6 x. %s'%(d*1.381380)
xxxtemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp35+')&('+xxxtemp28+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+')&('+xxxtemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*8.438430))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*9.179170))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*7.117110))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*4.754750))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*5.655650))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*5.265260))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.381380))
xxxtemp44 ='n.  ne2'
xxxtemp45 ='jessatom0 x. %s'%(d*10.370360)
xxxtemp46 ='jessatom1 x. %s'%(d*11.011000)
xxxtemp47 ='jessatom2 x. %s'%(d*9.049040)
xxxtemp48 ='jessatom3 x. %s'%(d*6.536530)
xxxtemp49 ='jessatom4 x. %s'%(d*7.637630)
xxxtemp50 ='jessatom5 x. %s'%(d*7.397390)
xxxtemp51 ='jessatom6 x. %s'%(d*2.202200)
xxxtemp52 ='br. jessatom6'
xxxtemp53 ='jessatom7 x. %s'%(d*2.142140)
cmd.select('jessatom8', '(('+xxxtemp44+')&('+xxxtemp28+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+')&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*10.370360))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*11.011000))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*9.049040))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*6.536530))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*7.637630))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*7.397390))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*2.202200))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.142140))
xxxtemp54 ='n.  cd '
xxxtemp55 ='r. glu'
xxxtemp56 ='r. asp'
xxxtemp57 ='jessatom0 x. %s'%(d*13.853840)
xxxtemp58 ='jessatom1 x. %s'%(d*14.384370)
xxxtemp59 ='jessatom2 x. %s'%(d*12.562550)
xxxtemp60 ='jessatom3 x. %s'%(d*9.869860)
xxxtemp61 ='jessatom4 x. %s'%(d*11.141130)
xxxtemp62 ='jessatom5 x. %s'%(d*11.081070)
xxxtemp63 ='jessatom6 x. %s'%(d*5.615610)
xxxtemp64 ='jessatom7 x. %s'%(d*5.865860)
xxxtemp65 ='jessatom8 x. %s'%(d*3.733730)
cmd.select('jessatom9', '(((('+xxxtemp54+')&('+xxxtemp55+'))|(('+xxxtemp54+')&('+xxxtemp56+')))&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+')&('+xxxtemp62+')&('+xxxtemp63+')&('+xxxtemp64+')&('+xxxtemp65+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(d*13.853840))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(d*14.384370))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(d*12.562550))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(d*9.869860))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(d*11.141130))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(d*11.081070))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(d*5.615610))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(d*5.865860))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(d*3.733730))
xxxtemp66 ='n.  oe1'
xxxtemp67 ='n.  oe2'
xxxtemp68 ='n.  od2'
xxxtemp69 ='jessatom0 x. %s'%(d*13.923910)
xxxtemp70 ='jessatom1 x. %s'%(d*14.474460)
xxxtemp71 ='jessatom2 x. %s'%(d*12.652640)
xxxtemp72 ='jessatom3 x. %s'%(d*9.639630)
xxxtemp73 ='jessatom4 x. %s'%(d*11.000990)
xxxtemp74 ='jessatom5 x. %s'%(d*11.151140)
xxxtemp75 ='jessatom6 x. %s'%(d*5.815810)
xxxtemp76 ='jessatom7 x. %s'%(d*6.106100)
xxxtemp77 ='jessatom8 x. %s'%(d*4.074070)
xxxtemp78 ='jessatom9 x. %s'%(d*1.251250)
xxxtemp79 ='br. jessatom9'
cmd.select('jessatom10', '((((('+xxxtemp66+')|('+xxxtemp67+'))&('+xxxtemp55+'))|((('+xxxtemp3+')|('+xxxtemp68+'))&('+xxxtemp56+')))&('+xxxtemp69+')&('+xxxtemp70+')&('+xxxtemp71+')&('+xxxtemp72+')&('+xxxtemp73+')&('+xxxtemp74+')&('+xxxtemp75+')&('+xxxtemp76+')&('+xxxtemp77+')&('+xxxtemp78+')&('+xxxtemp79+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(d*13.923910))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(d*14.474460))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(d*12.652640))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(d*9.639630))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(d*11.000990))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(d*11.151140))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(d*5.815810))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(d*6.106100))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(d*4.074070))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(d*1.251250))
xxxtemp80 ='n.  oe2'
xxxtemp81 ='n.  oe1'
xxxtemp82 ='n.  od2'
xxxtemp83 ='n.  od1'
xxxtemp84 ='jessatom0 x. %s'%(d*12.832820)
xxxtemp85 ='jessatom1 x. %s'%(d*13.343330)
xxxtemp86 ='jessatom2 x. %s'%(d*11.531520)
xxxtemp87 ='jessatom3 x. %s'%(d*9.159150)
xxxtemp88 ='jessatom4 x. %s'%(d*10.350340)
xxxtemp89 ='jessatom5 x. %s'%(d*10.160150)
xxxtemp90 ='jessatom6 x. %s'%(d*4.854850)
xxxtemp91 ='jessatom7 x. %s'%(d*4.924920)
xxxtemp92 ='jessatom8 x. %s'%(d*2.792790)
xxxtemp93 ='br. jessatom9'
xxxtemp94 ='jessatom10 x. %s'%(d*2.202200)
cmd.select('jessatom11', '((((('+xxxtemp80+')|('+xxxtemp81+'))&('+xxxtemp55+'))|((('+xxxtemp82+')|('+xxxtemp83+'))&('+xxxtemp56+')))&('+xxxtemp84+')&('+xxxtemp85+')&('+xxxtemp86+')&('+xxxtemp87+')&('+xxxtemp88+')&('+xxxtemp89+')&('+xxxtemp90+')&('+xxxtemp91+')&('+xxxtemp92+')&('+xxxtemp78+')&('+xxxtemp93+')&('+xxxtemp94+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(d*12.832820))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(d*13.343330))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(d*11.531520))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(d*9.159150))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(d*10.350340))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(d*10.160150))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(d*4.854850))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(d*4.924920))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(d*2.792790))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(d*1.251250))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(d*2.202200))
cmd.select('Jfa_1qnt_2_1_1_63', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
cmd.delete('temp94')
