'''
FUNC:Jab_1iov_6_3_2_4
PDB:1iov
EC:6.3.2.4
RESI:glu,ser,tyr,arg,gly
LOCI:a-15,150,216,255,276;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. glu'
xxxtemp2 ='r. asp'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.541540)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.541540))
xxxtemp6 ='r. ser'
xxxtemp7 ='r. thr'
xxxtemp8 ='jessatom0 x. %s'%(d*6.906900)
xxxtemp9 ='jessatom1 x. %s'%(d*6.206200)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*6.906900))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*6.206200))
xxxtemp10 ='jessatom0 x. %s'%(d*5.655650)
xxxtemp11 ='jessatom1 x. %s'%(d*5.135130)
xxxtemp12 ='jessatom2 x. %s'%(d*1.511510)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp6+'))|(('+xxxtemp3+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*5.655650))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*5.135130))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.511510))
xxxtemp14 ='r. tyr'
xxxtemp15 ='jessatom0 x. %s'%(d*11.401390)
xxxtemp16 ='jessatom1 x. %s'%(d*11.571560)
xxxtemp17 ='jessatom2 x. %s'%(d*8.898890)
xxxtemp18 ='jessatom3 x. %s'%(d*8.288280)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*11.401390))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*11.571560))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*8.898890))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*8.288280))
xxxtemp19 ='jessatom0 x. %s'%(d*9.989980)
xxxtemp20 ='jessatom1 x. %s'%(d*10.260250)
xxxtemp21 ='jessatom2 x. %s'%(d*8.238230)
xxxtemp22 ='jessatom3 x. %s'%(d*7.407400)
xxxtemp23 ='jessatom4 x. %s'%(d*1.561560)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp14+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*9.989980))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*10.260250))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*8.238230))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*7.407400))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.561560))
xxxtemp25 ='r. arg'
xxxtemp26 ='jessatom0 x. %s'%(d*16.406390)
xxxtemp27 ='jessatom1 x. %s'%(d*14.984970)
xxxtemp28 ='jessatom2 x. %s'%(d*12.712700)
xxxtemp29 ='jessatom3 x. %s'%(d*13.463450)
xxxtemp30 ='jessatom4 x. %s'%(d*16.876860)
xxxtemp31 ='jessatom5 x. %s'%(d*16.896880)
cmd.select('jessatom6', '(('+xxxtemp0+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+')&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*16.406390))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*14.984970))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*12.712700))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*13.463450))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*16.876860))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*16.896880))
xxxtemp32 ='jessatom0 x. %s'%(d*15.485470)
xxxtemp33 ='jessatom1 x. %s'%(d*14.104090)
xxxtemp34 ='jessatom2 x. %s'%(d*11.731720)
xxxtemp35 ='jessatom3 x. %s'%(d*12.412400)
xxxtemp36 ='jessatom4 x. %s'%(d*15.395380)
xxxtemp37 ='jessatom5 x. %s'%(d*15.445430)
xxxtemp38 ='jessatom6 x. %s'%(d*1.561560)
xxxtemp39 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp3+')&('+xxxtemp25+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*15.485470))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*14.104090))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*11.731720))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*12.412400))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*15.395380))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*15.445430))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.561560))
xxxtemp40 ='n.  n  '
xxxtemp41 ='jessatom0 x. %s'%(d*10.050040)
xxxtemp42 ='jessatom1 x. %s'%(d*8.928920)
xxxtemp43 ='jessatom2 x. %s'%(d*8.718710)
xxxtemp44 ='jessatom3 x. %s'%(d*8.538530)
xxxtemp45 ='jessatom4 x. %s'%(d*11.121110)
xxxtemp46 ='jessatom5 x. %s'%(d*10.650640)
xxxtemp47 ='jessatom6 x. %s'%(d*8.138130)
xxxtemp48 ='jessatom7 x. %s'%(d*6.886880)
cmd.select('jessatom8', '(('+xxxtemp40+')&('+xxxtemp41+')&('+xxxtemp42+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*10.050040))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*8.928920))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*8.718710))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*8.538530))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*11.121110))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*10.650640))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*8.138130))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*6.886880))
xxxtemp49 ='jessatom0 x. %s'%(d*9.719710)
xxxtemp50 ='jessatom1 x. %s'%(d*8.778770)
xxxtemp51 ='jessatom2 x. %s'%(d*8.858850)
xxxtemp52 ='jessatom3 x. %s'%(d*8.458450)
xxxtemp53 ='jessatom4 x. %s'%(d*10.190180)
xxxtemp54 ='jessatom5 x. %s'%(d*9.669660)
xxxtemp55 ='jessatom6 x. %s'%(d*9.469460)
xxxtemp56 ='jessatom7 x. %s'%(d*8.158150)
xxxtemp57 ='jessatom8 x. %s'%(d*1.471470)
xxxtemp58 ='br. jessatom8'
cmd.select('jessatom9', '(('+xxxtemp0+')&('+xxxtemp49+')&('+xxxtemp50+')&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(d*9.719710))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(d*8.778770))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(d*8.858850))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(d*8.458450))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(d*10.190180))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(d*9.669660))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(d*9.469460))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(d*8.158150))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(d*1.471470))
cmd.select('Jab_1iov_6_3_2_4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9')
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
