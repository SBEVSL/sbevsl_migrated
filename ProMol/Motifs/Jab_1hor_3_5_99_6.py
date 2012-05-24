'''
FUNC:Jab_1hor_3_5_99_6
PDB:1hor
EC:3.5.99.6
RESI:asp,asp,his,glu
LOCI:a-72,141,143,148;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. asp'
xxxtemp2 ='r. glu'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.541540)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.541540))
xxxtemp6 ='jessatom0 x. %s'%(d*16.886870)
xxxtemp7 ='jessatom1 x. %s'%(d*15.405390)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+')))&('+xxxtemp6+')&('+xxxtemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*16.886870))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*15.405390))
xxxtemp8 ='jessatom0 x. %s'%(d*16.506490)
xxxtemp9 ='jessatom1 x. %s'%(d*14.994980)
xxxtemp10 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp8+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*16.506490))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*14.994980))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp12 ='r. his'
xxxtemp13 ='jessatom0 x. %s'%(d*12.332320)
xxxtemp14 ='jessatom1 x. %s'%(d*10.970960)
xxxtemp15 ='jessatom2 x. %s'%(d*5.665660)
xxxtemp16 ='jessatom3 x. %s'%(d*5.805800)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp12+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*12.332320))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*10.970960))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*5.665660))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*5.805800))
xxxtemp17 ='jessatom0 x. %s'%(d*11.641630)
xxxtemp18 ='jessatom1 x. %s'%(d*10.200190)
xxxtemp19 ='jessatom2 x. %s'%(d*5.735730)
xxxtemp20 ='jessatom3 x. %s'%(d*5.495490)
xxxtemp21 ='jessatom4 x. %s'%(d*1.561560)
xxxtemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp12+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*11.641630))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*10.200190))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*5.735730))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*5.495490))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.561560))
xxxtemp23 ='jessatom0 x. %s'%(d*12.472460)
xxxtemp24 ='jessatom1 x. %s'%(d*11.041030)
xxxtemp25 ='jessatom2 x. %s'%(d*7.707700)
xxxtemp26 ='jessatom3 x. %s'%(d*6.716710)
xxxtemp27 ='jessatom4 x. %s'%(d*5.295290)
xxxtemp28 ='jessatom5 x. %s'%(d*4.184180)
cmd.select('jessatom6', '(((('+xxxtemp0+')&('+xxxtemp2+'))|(('+xxxtemp0+')&('+xxxtemp1+')))&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+')&('+xxxtemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*12.472460))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*11.041030))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*7.707700))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*6.716710))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*5.295290))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*4.184180))
xxxtemp29 ='jessatom0 x. %s'%(d*12.622610)
xxxtemp30 ='jessatom1 x. %s'%(d*11.181170)
xxxtemp31 ='jessatom2 x. %s'%(d*8.248240)
xxxtemp32 ='jessatom3 x. %s'%(d*7.057050)
xxxtemp33 ='jessatom4 x. %s'%(d*6.526520)
xxxtemp34 ='jessatom5 x. %s'%(d*5.245240)
xxxtemp35 ='jessatom6 x. %s'%(d*1.541540)
xxxtemp36 ='br. jessatom6'
cmd.select('jessatom7', '(((('+xxxtemp3+')&('+xxxtemp2+'))|(('+xxxtemp3+')&('+xxxtemp1+')))&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*12.622610))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*11.181170))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*8.248240))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*7.057050))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*6.526520))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*5.245240))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.541540))
cmd.select('Jab_1hor_3_5_99_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
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
