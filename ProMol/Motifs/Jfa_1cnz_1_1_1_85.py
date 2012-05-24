'''
FUNC:Jfa_1cnz_1_1_1_85
PDB:1cnz
EC:1.1.1.85
RESI:lys,asp,tyr
LOCI:a-195,227;b-145;
'''
xxxtemp0 ='n.  ce1'
xxxtemp1 ='r. tyr'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cz '
xxxtemp3 ='r. tyr'
xxxtemp4 ='jessatom0 x. %s'%(d*1.381380)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.381380))
xxxtemp6 ='n.  oh '
xxxtemp7 ='jessatom0 x. %s'%(d*2.392390)
xxxtemp8 ='br. jessatom0'
xxxtemp9 ='jessatom1 x. %s'%(d*1.381380)
cmd.select('jessatom2', '(('+xxxtemp6+')&('+xxxtemp3+')&('+xxxtemp7+')&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*2.392390))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*1.381380))
xxxtemp10 ='n.  cd '
xxxtemp11 ='r. lys'
xxxtemp12 ='jessatom0 x. %s'%(d*5.955950)
xxxtemp13 ='jessatom1 x. %s'%(d*5.125120)
xxxtemp14 ='jessatom2 x. %s'%(d*4.354350)
cmd.select('jessatom3', '(('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+')&('+xxxtemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*5.955950))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*5.125120))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*4.354350))
xxxtemp15 ='n.  ce '
xxxtemp16 ='jessatom0 x. %s'%(d*4.834830)
xxxtemp17 ='jessatom1 x. %s'%(d*4.224220)
xxxtemp18 ='jessatom2 x. %s'%(d*3.413410)
xxxtemp19 ='jessatom3 x. %s'%(d*1.531530)
xxxtemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+xxxtemp15+')&('+xxxtemp11+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*4.834830))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*4.224220))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*3.413410))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*1.531530))
xxxtemp21 ='n.  nz '
xxxtemp22 ='jessatom0 x. %s'%(d*5.415410)
xxxtemp23 ='jessatom1 x. %s'%(d*4.914910)
xxxtemp24 ='jessatom2 x. %s'%(d*3.843840)
xxxtemp25 ='jessatom3 x. %s'%(d*2.512510)
xxxtemp26 ='br. jessatom3'
xxxtemp27 ='jessatom4 x. %s'%(d*1.491490)
cmd.select('jessatom5', '(('+xxxtemp21+')&('+xxxtemp11+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*5.415410))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*4.914910))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*3.843840))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.512510))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.491490))
xxxtemp28 ='n.  cg '
xxxtemp29 ='r. asp'
xxxtemp30 ='r. glu'
xxxtemp31 ='jessatom0 x. %s'%(d*8.228220)
xxxtemp32 ='jessatom1 x. %s'%(d*7.517510)
xxxtemp33 ='jessatom2 x. %s'%(d*6.176170)
xxxtemp34 ='jessatom3 x. %s'%(d*4.824820)
xxxtemp35 ='jessatom4 x. %s'%(d*4.694690)
xxxtemp36 ='jessatom5 x. %s'%(d*3.483480)
cmd.select('jessatom6', '(((('+xxxtemp28+')&('+xxxtemp29+'))|(('+xxxtemp28+')&('+xxxtemp30+')))&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*8.228220))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*7.517510))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*6.176170))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*4.824820))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*4.694690))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*3.483480))
xxxtemp37 ='n.  od1'
xxxtemp38 ='n.  od2'
xxxtemp39 ='n.  oe1'
xxxtemp40 ='n.  oe2'
xxxtemp41 ='jessatom0 x. %s'%(d*8.568560)
xxxtemp42 ='jessatom1 x. %s'%(d*7.837830)
xxxtemp43 ='jessatom2 x. %s'%(d*6.556550)
xxxtemp44 ='jessatom3 x. %s'%(d*4.314310)
xxxtemp45 ='jessatom4 x. %s'%(d*4.454450)
xxxtemp46 ='jessatom5 x. %s'%(d*3.413410)
xxxtemp47 ='jessatom6 x. %s'%(d*1.231230)
xxxtemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+xxxtemp37+')|('+xxxtemp38+'))&('+xxxtemp29+'))|((('+xxxtemp39+')|('+xxxtemp40+'))&('+xxxtemp30+')))&('+xxxtemp41+')&('+xxxtemp42+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*8.568560))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*7.837830))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*6.556550))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*4.314310))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*4.454450))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*3.413410))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.231230))
xxxtemp49 ='n.  od2'
xxxtemp50 ='n.  od1'
xxxtemp51 ='n.  oe2'
xxxtemp52 ='n.  oe1'
xxxtemp53 ='jessatom0 x. %s'%(d*7.747740)
xxxtemp54 ='jessatom1 x. %s'%(d*7.207200)
xxxtemp55 ='jessatom2 x. %s'%(d*5.885880)
xxxtemp56 ='jessatom3 x. %s'%(d*5.135130)
xxxtemp57 ='jessatom4 x. %s'%(d*4.634630)
xxxtemp58 ='jessatom5 x. %s'%(d*3.223220)
xxxtemp59 ='jessatom6 x. %s'%(d*1.211210)
xxxtemp60 ='br. jessatom6'
xxxtemp61 ='jessatom7 x. %s'%(d*2.132130)
cmd.select('jessatom8', '((((('+xxxtemp49+')|('+xxxtemp50+'))&('+xxxtemp29+'))|((('+xxxtemp51+')|('+xxxtemp52+'))&('+xxxtemp30+')))&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+')&('+xxxtemp60+')&('+xxxtemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*7.747740))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*7.207200))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*5.885880))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*5.135130))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*4.634630))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*3.223220))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*1.211210))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*2.132130))
cmd.select('Jfa_1cnz_1_1_1_85', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
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
