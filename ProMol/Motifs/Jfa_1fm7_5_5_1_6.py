'''
FUNC:Jfa_1fm7_5_5_1_6
PDB:1fm7
EC:5.5.1.6
RESI:thr,tyr,asn,thr
LOCI:a-48,106,113,190;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. thr'
xxxtemp2 ='r. ser'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.551550)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.551550))
xxxtemp6 ='n.  og1'
xxxtemp7 ='jessatom0 x. %s'%(d*2.432430)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*1.421420)
cmd.select('jessatom2', '(((('+xxxtemp6+')&('+xxxtemp1+'))|(('+xxxtemp6+')&('+xxxtemp2+')))&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*2.432430))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*1.421420))
xxxtemp10 ='n.  ce1'
xxxtemp11 ='r. tyr'
xxxtemp12 ='jessatom0 x. %s'%(d*6.566560)
xxxtemp13 ='jessatom1 x. %s'%(d*5.075070)
xxxtemp14 ='jessatom2 x. %s'%(d*4.984980)
cmd.select('jessatom3', '(('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+')&('+xxxtemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*6.566560))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*5.075070))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*4.984980))
xxxtemp15 ='n.  cz '
xxxtemp16 ='jessatom0 x. %s'%(d*7.667660)
xxxtemp17 ='jessatom1 x. %s'%(d*6.146140)
xxxtemp18 ='jessatom2 x. %s'%(d*6.036030)
xxxtemp19 ='jessatom3 x. %s'%(d*1.391390)
xxxtemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+xxxtemp15+')&('+xxxtemp11+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*7.667660))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*6.146140))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*6.036030))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.391390))
xxxtemp21 ='n.  oh '
xxxtemp22 ='jessatom0 x. %s'%(d*7.867860)
xxxtemp23 ='jessatom1 x. %s'%(d*6.326320)
xxxtemp24 ='jessatom2 x. %s'%(d*6.066060)
xxxtemp25 ='jessatom3 x. %s'%(d*2.402400)
xxxtemp26 ='br. jessatom3'
xxxtemp27 ='jessatom4 x. %s'%(d*1.371370)
cmd.select('jessatom5', '(('+xxxtemp21+')&('+xxxtemp11+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*7.867860))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*6.326320))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*6.066060))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.402400))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.371370))
xxxtemp28 ='n.  cg '
xxxtemp29 ='r. asn'
xxxtemp30 ='r. gln'
xxxtemp31 ='jessatom0 x. %s'%(d*13.823810)
xxxtemp32 ='jessatom1 x. %s'%(d*12.712700)
xxxtemp33 ='jessatom2 x. %s'%(d*11.521510)
xxxtemp34 ='jessatom3 x. %s'%(d*10.190180)
xxxtemp35 ='jessatom4 x. %s'%(d*10.180170)
xxxtemp36 ='jessatom5 x. %s'%(d*9.989980)
cmd.select('jessatom6', '(((('+xxxtemp28+')&('+xxxtemp29+'))|(('+xxxtemp28+')&('+xxxtemp30+')))&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*13.823810))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*12.712700))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*11.521510))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*10.190180))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*10.180170))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*9.989980))
xxxtemp37 ='n.  od1'
xxxtemp38 ='jessatom0 x. %s'%(d*14.524510)
xxxtemp39 ='jessatom1 x. %s'%(d*13.473460)
xxxtemp40 ='jessatom2 x. %s'%(d*12.282270)
xxxtemp41 ='jessatom3 x. %s'%(d*11.000990)
xxxtemp42 ='jessatom4 x. %s'%(d*11.071060)
xxxtemp43 ='jessatom5 x. %s'%(d*10.980970)
xxxtemp44 ='jessatom6 x. %s'%(d*1.231230)
xxxtemp45 ='br. jessatom6'
cmd.select('jessatom7', '(((('+xxxtemp37+')&('+xxxtemp29+'))|(('+xxxtemp37+')&('+xxxtemp30+')))&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*14.524510))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*13.473460))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*12.282270))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*11.000990))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*11.071060))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*10.980970))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.231230))
xxxtemp46 ='n.  nd2'
xxxtemp47 ='jessatom0 x. %s'%(d*12.562550)
xxxtemp48 ='jessatom1 x. %s'%(d*11.471460)
xxxtemp49 ='jessatom2 x. %s'%(d*10.250240)
xxxtemp50 ='jessatom3 x. %s'%(d*9.239230)
xxxtemp51 ='jessatom4 x. %s'%(d*9.319310)
xxxtemp52 ='jessatom5 x. %s'%(d*9.119110)
xxxtemp53 ='jessatom6 x. %s'%(d*1.331330)
xxxtemp54 ='br. jessatom6'
xxxtemp55 ='jessatom7 x. %s'%(d*2.252250)
cmd.select('jessatom8', '(((('+xxxtemp46+')&('+xxxtemp29+'))|(('+xxxtemp46+')&('+xxxtemp30+')))&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+')&('+xxxtemp50+')&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*12.562550))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*11.471460))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*10.250240))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*9.239230))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*9.319310))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*9.119110))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*1.331330))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.252250))
xxxtemp56 ='jessatom0 x. %s'%(d*14.834820)
xxxtemp57 ='jessatom1 x. %s'%(d*13.703690)
xxxtemp58 ='jessatom2 x. %s'%(d*12.452440)
xxxtemp59 ='jessatom3 x. %s'%(d*11.831820)
xxxtemp60 ='jessatom4 x. %s'%(d*11.421410)
xxxtemp61 ='jessatom5 x. %s'%(d*10.510500)
xxxtemp62 ='jessatom6 x. %s'%(d*6.206200)
xxxtemp63 ='jessatom7 x. %s'%(d*7.207200)
xxxtemp64 ='jessatom8 x. %s'%(d*6.066060)
cmd.select('jessatom9', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+')))&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+')&('+xxxtemp62+')&('+xxxtemp63+')&('+xxxtemp64+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(d*14.834820))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(d*13.703690))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(d*12.452440))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(d*11.831820))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(d*11.421410))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(d*10.510500))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(d*6.206200))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(d*7.207200))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(d*6.066060))
xxxtemp65 ='jessatom0 x. %s'%(d*14.314300)
xxxtemp66 ='jessatom1 x. %s'%(d*13.113100)
xxxtemp67 ='jessatom2 x. %s'%(d*11.891880)
xxxtemp68 ='jessatom3 x. %s'%(d*10.830820)
xxxtemp69 ='jessatom4 x. %s'%(d*10.410400)
xxxtemp70 ='jessatom5 x. %s'%(d*9.609600)
xxxtemp71 ='jessatom6 x. %s'%(d*4.924920)
xxxtemp72 ='jessatom7 x. %s'%(d*5.995990)
xxxtemp73 ='jessatom8 x. %s'%(d*4.844840)
xxxtemp74 ='jessatom9 x. %s'%(d*1.551550)
xxxtemp75 ='br. jessatom9'
cmd.select('jessatom10', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp65+')&('+xxxtemp66+')&('+xxxtemp67+')&('+xxxtemp68+')&('+xxxtemp69+')&('+xxxtemp70+')&('+xxxtemp71+')&('+xxxtemp72+')&('+xxxtemp73+')&('+xxxtemp74+')&('+xxxtemp75+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(d*14.314300))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(d*13.113100))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(d*11.891880))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(d*10.830820))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(d*10.410400))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(d*9.609600))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(d*4.924920))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(d*5.995990))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(d*4.844840))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(d*1.551550))
xxxtemp76 ='jessatom0 x. %s'%(d*13.293280)
xxxtemp77 ='jessatom1 x. %s'%(d*12.042030)
xxxtemp78 ='jessatom2 x. %s'%(d*10.880870)
xxxtemp79 ='jessatom3 x. %s'%(d*9.609600)
xxxtemp80 ='jessatom4 x. %s'%(d*9.119110)
xxxtemp81 ='jessatom5 x. %s'%(d*8.258250)
xxxtemp82 ='jessatom6 x. %s'%(d*5.295290)
xxxtemp83 ='jessatom7 x. %s'%(d*6.486480)
xxxtemp84 ='jessatom8 x. %s'%(d*4.994990)
xxxtemp85 ='jessatom9 x. %s'%(d*2.442440)
xxxtemp86 ='br. jessatom9'
xxxtemp87 ='jessatom10 x. %s'%(d*1.431430)
cmd.select('jessatom11', '(((('+xxxtemp6+')&('+xxxtemp1+'))|(('+xxxtemp6+')&('+xxxtemp2+')))&('+xxxtemp76+')&('+xxxtemp77+')&('+xxxtemp78+')&('+xxxtemp79+')&('+xxxtemp80+')&('+xxxtemp81+')&('+xxxtemp82+')&('+xxxtemp83+')&('+xxxtemp84+')&('+xxxtemp85+')&('+xxxtemp86+')&('+xxxtemp87+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(d*13.293280))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(d*12.042030))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(d*10.880870))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(d*9.609600))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(d*9.119110))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(d*8.258250))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(d*5.295290))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(d*6.486480))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(d*4.994990))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(d*2.442440))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(d*1.431430))
cmd.select('Jfa_1fm7_5_5_1_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
