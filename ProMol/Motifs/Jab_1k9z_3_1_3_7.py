'''
FUNC:Jab_1k9z_3_1_3_7
PDB:1k9z
EC:3.1.3.7
RESI:asp,thr,asp
LOCI:a-49,147,294;
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
xxxtemp6 ='r. thr'
xxxtemp7 ='r. ser'
xxxtemp8 ='jessatom0 x. %s'%(d*7.697690)
xxxtemp9 ='jessatom1 x. %s'%(d*6.986980)
cmd.select('jessatom2', '(((('+xxxtemp0+')&('+xxxtemp6+'))|(('+xxxtemp0+')&('+xxxtemp7+')))&('+xxxtemp8+')&('+xxxtemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(d*7.697690))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(d*6.986980))
xxxtemp10 ='jessatom0 x. %s'%(d*7.047040)
xxxtemp11 ='jessatom1 x. %s'%(d*6.086080)
xxxtemp12 ='jessatom2 x. %s'%(d*1.531530)
xxxtemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+xxxtemp3+')&('+xxxtemp6+'))|(('+xxxtemp3+')&('+xxxtemp7+')))&('+xxxtemp10+')&('+xxxtemp11+')&('+xxxtemp12+')&('+xxxtemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(d*7.047040))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(d*6.086080))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(d*1.531530))
xxxtemp14 ='jessatom0 x. %s'%(d*13.883870)
xxxtemp15 ='jessatom1 x. %s'%(d*13.283270)
xxxtemp16 ='jessatom2 x. %s'%(d*11.661650)
xxxtemp17 ='jessatom3 x. %s'%(d*11.651640)
cmd.select('jessatom4', '(((('+xxxtemp0+')&('+xxxtemp1+'))|(('+xxxtemp0+')&('+xxxtemp2+')))&('+xxxtemp14+')&('+xxxtemp15+')&('+xxxtemp16+')&('+xxxtemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(d*13.883870))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(d*13.283270))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(d*11.661650))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(d*11.651640))
xxxtemp18 ='jessatom0 x. %s'%(d*14.274260)
xxxtemp19 ='jessatom1 x. %s'%(d*13.533520)
xxxtemp20 ='jessatom2 x. %s'%(d*11.421410)
xxxtemp21 ='jessatom3 x. %s'%(d*11.361350)
xxxtemp22 ='jessatom4 x. %s'%(d*1.521520)
xxxtemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+xxxtemp3+')&('+xxxtemp1+'))|(('+xxxtemp3+')&('+xxxtemp2+')))&('+xxxtemp18+')&('+xxxtemp19+')&('+xxxtemp20+')&('+xxxtemp21+')&('+xxxtemp22+')&('+xxxtemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(d*14.274260))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(d*13.533520))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(d*11.421410))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(d*11.361350))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(d*1.521520))
cmd.select('Jab_1k9z_3_1_3_7', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
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
