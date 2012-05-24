'''
FUNC:Jab_1dd8_2_3_1_41
PDB:1dd8
EC:2.3.1.41
RESI:cys,his,lys,his,phe,phe
LOCI:a-163,298,328,333,390,392;
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
xxxtemp6 ='r. his'
xxxtemp7 ='jessatom0 x. %s'%(d*8.968960)
xxxtemp8 ='jessatom1 x. %s'%(d*7.907900)
cmd.select('jessatom2', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp7+')&('+xxxtemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*8.968960))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*7.907900))
xxxtemp9 ='jessatom0 x. %s'%(d*8.368360)
xxxtemp10 ='jessatom1 x. %s'%(d*7.237230)
xxxtemp11 ='jessatom2 x. %s'%(d*1.521520)
xxxtemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp9+')&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*8.368360))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*7.237230))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.521520))
xxxtemp13 ='jessatom0 x. %s'%(d*8.438430)
xxxtemp14 ='jessatom1 x. %s'%(d*7.937930)
xxxtemp15 ='jessatom2 x. %s'%(d*9.299290)
xxxtemp16 ='jessatom3 x. %s'%(d*9.869860)
cmd.select('jessatom4', '(('+xxxtemp0+')&('+xxxtemp6+')&('+xxxtemp13+')&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*8.438430))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*7.937930))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*9.299290))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*9.869860))
xxxtemp17 ='jessatom0 x. %s'%(d*7.947940)
xxxtemp18 ='jessatom1 x. %s'%(d*7.257250)
xxxtemp19 ='jessatom2 x. %s'%(d*8.968960)
xxxtemp20 ='jessatom3 x. %s'%(d*9.359350)
xxxtemp21 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+xxxtemp2+')&('+xxxtemp6+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*7.947940))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*7.257250))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*8.968960))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*9.359350))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
xxxtemp23 ='n.  n  '
xxxtemp24 ='jessatom0 x. %s'%(d*5.395390)
xxxtemp25 ='jessatom1 x. %s'%(d*4.914910)
xxxtemp26 ='jessatom2 x. %s'%(d*11.041030)
xxxtemp27 ='jessatom3 x. %s'%(d*9.869860)
xxxtemp28 ='jessatom4 x. %s'%(d*12.022010)
xxxtemp29 ='jessatom5 x. %s'%(d*10.960950)
cmd.select('jessatom6', '(('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+')&('+xxxtemp26+')&('+xxxtemp27+')&('+xxxtemp28+')&('+xxxtemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(d*5.395390))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(d*4.914910))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(d*11.041030))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(d*9.869860))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(d*12.022010))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(d*10.960950))
xxxtemp30 ='jessatom0 x. %s'%(d*6.746740)
xxxtemp31 ='jessatom1 x. %s'%(d*6.296290)
xxxtemp32 ='jessatom2 x. %s'%(d*12.282270)
xxxtemp33 ='jessatom3 x. %s'%(d*11.071060)
xxxtemp34 ='jessatom4 x. %s'%(d*13.063050)
xxxtemp35 ='jessatom5 x. %s'%(d*11.921910)
xxxtemp36 ='jessatom6 x. %s'%(d*1.461460)
xxxtemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+xxxtemp0+')&('+xxxtemp30+')&('+xxxtemp31+')&('+xxxtemp32+')&('+xxxtemp33+')&('+xxxtemp34+')&('+xxxtemp35+')&('+xxxtemp36+')&('+xxxtemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(d*6.746740))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(d*6.296290))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(d*12.282270))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(d*11.071060))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(d*13.063050))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(d*11.921910))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(d*1.461460))
cmd.select('Jab_1dd8_2_3_1_41', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
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
