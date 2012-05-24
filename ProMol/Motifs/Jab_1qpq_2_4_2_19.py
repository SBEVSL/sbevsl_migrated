'''
FUNC:Jab_1qpq_2_4_2_19
PDB:1qpq
EC:2.4.2.19
RESI:arg,lys,glu,asp
LOCI:a-105;b-640,701,722;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. lys'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. lys'
xxxtemp4 ='jessatom0 x. %s'%(d*1.501500)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.501500))
xxxtemp6 ='r. glu'
xxxtemp7 ='r. asp'
xxxtemp8 ='jessatom0 x. %s'%(d*15.965950)
xxxtemp9 ='jessatom1 x. %s'%(d*15.495480)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*15.965950))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*15.495480))
xxxtemp10 ='jessatom0 x. %s'%(d*14.654640)
xxxtemp11 ='jessatom1 x. %s'%(d*14.194180)
xxxtemp12 ='jessatom2 x. %s'%(d*1.521520)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*14.654640))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*14.194180))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.521520))
xxxtemp14 ='jessatom0 x. %s'%(d*15.245230)
xxxtemp15 ='jessatom1 x. %s'%(d*14.224210)
xxxtemp16 ='jessatom2 x. %s'%(d*6.596590)
xxxtemp17 ='jessatom3 x. %s'%(d*6.386380)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp7+'))|(('+xxxtemp0+')&('+xxxtemp6+')))&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*15.245230))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*14.224210))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*6.596590))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*6.386380))
xxxtemp18 ='jessatom0 x. %s'%(d*14.984970)
xxxtemp19 ='jessatom1 x. %s'%(d*14.024010)
xxxtemp20 ='jessatom2 x. %s'%(d*5.845840)
xxxtemp21 ='jessatom3 x. %s'%(d*5.445440)
xxxtemp22 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp7+'))|(('+xxxtemp2+')&('+xxxtemp6+')))&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*14.984970))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*14.024010))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*5.845840))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*5.445440))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
xxxtemp24 ='r. arg'
xxxtemp25 ='jessatom0 x. %s'%(d*7.097090)
xxxtemp26 ='jessatom1 x. %s'%(d*7.727720)
xxxtemp27 ='jessatom2 x. %s'%(d*15.585570)
xxxtemp28 ='jessatom3 x. %s'%(d*14.124110)
xxxtemp29 ='jessatom4 x. %s'%(d*16.606590)
xxxtemp30 ='jessatom5 x. %s'%(d*15.715700)
cmd.select('jessatom6', '(('+xxxtemp0+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+')&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*7.097090))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*7.727720))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*15.585570))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*14.124110))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*16.606590))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*15.715700))
xxxtemp31 ='jessatom0 x. %s'%(d*6.576570)
xxxtemp32 ='jessatom1 x. %s'%(d*7.337330)
xxxtemp33 ='jessatom2 x. %s'%(d*14.824810)
xxxtemp34 ='jessatom3 x. %s'%(d*13.403390)
xxxtemp35 ='jessatom4 x. %s'%(d*16.156140)
xxxtemp36 ='jessatom5 x. %s'%(d*15.315300)
xxxtemp37 ='jessatom6 x. %s'%(d*1.521520)
xxxtemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp2+')&('+xxxtemp24+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*6.576570))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*7.337330))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*14.824810))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*13.403390))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*16.156140))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*15.315300))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.521520))
cmd.select('Jab_1qpq_2_4_2_19', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
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
cmd.delete('temp37')
cmd.delete('temp38')
