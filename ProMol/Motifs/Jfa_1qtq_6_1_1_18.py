'''
FUNC:Jfa_1qtq_6_1_1_18
PDB:1qtq
EC:6.1.1.18
RESI:glu,arg,lys
LOCI:a-34,260,270;
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
xxxtemp13 ='br. jessatom0'
xxxtemp14 ='jessatom1 x. %s'%(d*2.202200)
cmd.select('jessatom2', '((((('+xxxtemp9+')|('+xxxtemp10+'))&('+xxxtemp1+'))|((('+xxxtemp11+')|('+xxxtemp12+'))&('+xxxtemp2+')))&('+xxxtemp7+')&('+xxxtemp13+')&('+xxxtemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*1.251250))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*2.202200))
xxxtemp15 ='n.  ne '
xxxtemp16 ='r. arg'
xxxtemp17 ='jessatom0 x. %s'%(d*14.494480)
xxxtemp18 ='jessatom1 x. %s'%(d*13.343330)
xxxtemp19 ='jessatom2 x. %s'%(d*15.475460)
cmd.select('jessatom3', '(('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*14.494480))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*13.343330))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*15.475460))
xxxtemp20 ='n.  nh1'
xxxtemp21 ='n.  nh2'
xxxtemp22 ='jessatom0 x. %s'%(d*12.362350)
xxxtemp23 ='jessatom1 x. %s'%(d*11.201190)
xxxtemp24 ='jessatom2 x. %s'%(d*13.363350)
xxxtemp25 ='jessatom3 x. %s'%(d*2.302300)
xxxtemp26 ='br. jessatom3'
cmd.select('jessatom4', '((('+xxxtemp20+')|('+xxxtemp21+'))&('+xxxtemp16+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*12.362350))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*11.201190))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*13.363350))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*2.302300))
xxxtemp27 ='n.  nh2'
xxxtemp28 ='n.  nh1'
xxxtemp29 ='jessatom0 x. %s'%(d*12.822810)
xxxtemp30 ='jessatom1 x. %s'%(d*11.711700)
xxxtemp31 ='jessatom2 x. %s'%(d*13.773760)
xxxtemp32 ='br. jessatom3'
xxxtemp33 ='jessatom4 x. %s'%(d*2.302300)
cmd.select('jessatom5', '((('+xxxtemp27+')|('+xxxtemp28+'))&('+xxxtemp16+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp25+')&('+xxxtemp32+')&('+xxxtemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*12.822810))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*11.711700))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*13.773760))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*2.302300))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*2.302300))
xxxtemp34 ='r. lys'
xxxtemp35 ='jessatom0 x. %s'%(d*7.257250)
xxxtemp36 ='jessatom1 x. %s'%(d*6.806800)
xxxtemp37 ='jessatom2 x. %s'%(d*7.917910)
xxxtemp38 ='jessatom3 x. %s'%(d*11.101090)
xxxtemp39 ='jessatom4 x. %s'%(d*9.739730)
xxxtemp40 ='jessatom5 x. %s'%(d*8.858850)
cmd.select('jessatom6', '(('+xxxtemp0+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*7.257250))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*6.806800))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*7.917910))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*11.101090))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*9.739730))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*8.858850))
xxxtemp41 ='n.  ce '
xxxtemp42 ='jessatom0 x. %s'%(d*6.846840)
xxxtemp43 ='jessatom1 x. %s'%(d*6.416410)
xxxtemp44 ='jessatom2 x. %s'%(d*7.687680)
xxxtemp45 ='jessatom3 x. %s'%(d*10.910900)
xxxtemp46 ='jessatom4 x. %s'%(d*9.409400)
xxxtemp47 ='jessatom5 x. %s'%(d*8.768760)
xxxtemp48 ='jessatom6 x. %s'%(d*1.521520)
xxxtemp49 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp41+')&('+xxxtemp34+')&('+xxxtemp42+')&('+xxxtemp43+')&('+xxxtemp44+')&('+xxxtemp45+')&('+xxxtemp46+')&('+xxxtemp47+')&('+xxxtemp48+')&('+xxxtemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*6.846840))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*6.416410))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*7.687680))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*10.910900))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*9.409400))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*8.768760))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.521520))
xxxtemp50 ='n.  nz '
xxxtemp51 ='jessatom0 x. %s'%(d*5.925920)
xxxtemp52 ='jessatom1 x. %s'%(d*5.315310)
xxxtemp53 ='jessatom2 x. %s'%(d*6.876870)
xxxtemp54 ='jessatom3 x. %s'%(d*10.290280)
xxxtemp55 ='jessatom4 x. %s'%(d*8.568560)
xxxtemp56 ='jessatom5 x. %s'%(d*8.258250)
xxxtemp57 ='jessatom6 x. %s'%(d*2.482480)
xxxtemp58 ='br. jessatom6'
xxxtemp59 ='jessatom7 x. %s'%(d*1.491490)
cmd.select('jessatom8', '(('+xxxtemp50+')&('+xxxtemp34+')&('+xxxtemp51+')&('+xxxtemp52+')&('+xxxtemp53+')&('+xxxtemp54+')&('+xxxtemp55+')&('+xxxtemp56+')&('+xxxtemp57+')&('+xxxtemp58+')&('+xxxtemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(d*5.925920))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(d*5.315310))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(d*6.876870))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(d*10.290280))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(d*8.568560))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(d*8.258250))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(d*2.482480))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(d*1.491490))
cmd.select('Jfa_1qtq_6_1_1_18', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
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
