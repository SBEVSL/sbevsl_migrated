'''
FUNC:Jab_1b0p_1_2_7_1
PDB:1b0p
EC:1.2.7.1
RESI:thr,glu,arg,asn
LOCI:a-31,64,114,996;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. thr'
xxxtemp2 ='r. ser'
cmd.select('jessatom0', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+'))))')
xxxtemp3 ='n.  cb '
xxxtemp4 ='jessatom0 x. %s'%(d*1.561560)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.561560))
xxxtemp6 ='r. glu'
xxxtemp7 ='r. asp'
xxxtemp8 ='jessatom0 x. %s'%(d*12.652640)
xxxtemp9 ='jessatom1 x. %s'%(d*13.763750)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*12.652640))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*13.763750))
xxxtemp10 ='jessatom0 x. %s'%(d*11.501490)
xxxtemp11 ='jessatom1 x. %s'%(d*12.642630)
xxxtemp12 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp6+'))|(('+xxxtemp3+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*11.501490))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*12.642630))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp14 ='r. arg'
xxxtemp15 ='jessatom0 x. %s'%(d*8.358350)
xxxtemp16 ='jessatom1 x. %s'%(d*8.818810)
xxxtemp17 ='jessatom2 x. %s'%(d*14.914900)
xxxtemp18 ='jessatom3 x. %s'%(d*13.393380)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.358350))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*8.818810))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*14.914900))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*13.393380))
xxxtemp19 ='jessatom0 x. %s'%(d*6.886880)
xxxtemp20 ='jessatom1 x. %s'%(d*7.387380)
xxxtemp21 ='jessatom2 x. %s'%(d*13.893880)
xxxtemp22 ='jessatom3 x. %s'%(d*12.392380)
xxxtemp23 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp3+')&('+xxxtemp14+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*6.886880))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*7.387380))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*13.893880))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*12.392380))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
xxxtemp25 ='r. asn'
xxxtemp26 ='r. gln'
xxxtemp27 ='jessatom0 x. %s'%(d*9.679670)
xxxtemp28 ='jessatom1 x. %s'%(d*8.688680)
xxxtemp29 ='jessatom2 x. %s'%(d*17.137120)
xxxtemp30 ='jessatom3 x. %s'%(d*16.666650)
xxxtemp31 ='jessatom4 x. %s'%(d*17.047030)
xxxtemp32 ='jessatom5 x. %s'%(d*15.625610)
cmd.select('jessatom6', '(((('+xxxtemp0+')&('+xxxtemp25+'))|(('+xxxtemp0+')&('+xxxtemp26+')))&('+xxxtemp27+')&('+xxxtemp28+')&('+xxxtemp29+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*9.679670))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*8.688680))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*17.137120))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*16.666650))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*17.047030))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*15.625610))
xxxtemp33 ='jessatom0 x. %s'%(d*9.619610)
xxxtemp34 ='jessatom1 x. %s'%(d*8.538530)
xxxtemp35 ='jessatom2 x. %s'%(d*16.966950)
xxxtemp36 ='jessatom3 x. %s'%(d*16.456440)
xxxtemp37 ='jessatom4 x. %s'%(d*16.486470)
xxxtemp38 ='jessatom5 x. %s'%(d*15.095080)
xxxtemp39 ='jessatom6 x. %s'%(d*1.541540)
xxxtemp40 ='br. jessatom6'
cmd.select('jessatom7', '(((('+xxxtemp3+')&('+xxxtemp25+'))|(('+xxxtemp3+')&('+xxxtemp26+')))&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+')&('+xxxtemp38+')&('+xxxtemp39+')&('+xxxtemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*9.619610))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*8.538530))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*16.966950))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*16.456440))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*16.486470))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*15.095080))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.541540))
cmd.select('Jab_1b0p_1_2_7_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
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
cmd.delete('temp39')
cmd.delete('temp40')
