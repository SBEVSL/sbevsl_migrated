'''
FUNC:Jab_1bd4_2_4_2_9
PDB:1bd4
EC:2.4.2.9
RESI:arg,thr,asp
LOCI:a-137,141,235;
'''
xxxtemp0 ='n.  ca '
xxxtemp1 ='r. arg'
cmd.select('jessatom0', '(('+xxxtemp0+')&('+xxxtemp1+'))')
xxxtemp2 ='n.  cb '
xxxtemp3 ='r. arg'
xxxtemp4 ='jessatom0 x. %s'%(d*1.531530)
xxxtemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+xxxtemp2+')&('+xxxtemp3+')&('+xxxtemp4+')&('+xxxtemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(d*1.531530))
xxxtemp6 ='r. thr'
xxxtemp7 ='r. ser'
xxxtemp8 ='jessatom0 x. %s'%(d*7.947940)
xxxtemp9 ='jessatom1 x. %s'%(d*8.008000)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*7.947940))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*8.008000))
xxxtemp10 ='jessatom0 x. %s'%(d*7.897890)
xxxtemp11 ='jessatom1 x. %s'%(d*8.168160)
xxxtemp12 ='jessatom2 x. %s'%(d*1.541540)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp2+')&('+xxxtemp6+'))|(('+xxxtemp2+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*7.897890))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*8.168160))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.541540))
xxxtemp14 ='r. asp'
xxxtemp15 ='r. glu'
xxxtemp16 ='jessatom0 x. %s'%(d*15.625610)
xxxtemp17 ='jessatom1 x. %s'%(d*14.504490)
xxxtemp18 ='jessatom2 x. %s'%(d*21.271250)
xxxtemp19 ='jessatom3 x. %s'%(d*21.951930)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp14+'))|(('+xxxtemp0+')&('+xxxtemp15+')))&('+xxxtemp16+')&('+xxxtemp17+')&('+xxxtemp18+')&('+xxxtemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*15.625610))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*14.504490))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*21.271250))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*21.951930))
xxxtemp20 ='jessatom0 x. %s'%(d*15.065050)
xxxtemp21 ='jessatom1 x. %s'%(d*13.973960)
xxxtemp22 ='jessatom2 x. %s'%(d*20.670650)
xxxtemp23 ='jessatom3 x. %s'%(d*21.391370)
xxxtemp24 ='jessatom4 x. %s'%(d*1.531530)
xxxtemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp2+')&('+xxxtemp14+'))|(('+xxxtemp2+')&('+xxxtemp15+')))&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+')&('+xxxtemp24+')&('+xxxtemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*15.065050))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*13.973960))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*20.670650))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*21.391370))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.531530))
cmd.select('Jab_1bd4_2_4_2_9', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
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
