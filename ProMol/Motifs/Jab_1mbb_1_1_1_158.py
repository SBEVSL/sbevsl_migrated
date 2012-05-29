'''
FUNC:Jab_1mbb_1_1_1_158
PDB:1mbb
EC:1.1.1.158
RESI:arg,ser,glu
LOCI:a-159,229,325;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. arg'
jesstemp4 ='jessatom0 a. %s'%(d*1.555400)
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom1 a. %s)'%(d*1.555400))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
jesstemp6 ='r. ser'
jesstemp7 ='r. thr'
jesstemp8 ='jessatom0 a. %s'%(d*11.120100)
jesstemp9 ='jessatom1 a. %s'%(d*9.776800)
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom2 a. %s)'%(d*11.120100))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom2 a. %s)'%(d*9.776800))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
jesstemp10 ='jessatom0 a. %s'%(d*10.069700)
jesstemp11 ='jessatom1 a. %s'%(d*8.726400)
jesstemp12 ='jessatom2 a. %s'%(d*1.535200)
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom3 a. %s)'%(d*10.069700))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom3 a. %s)'%(d*8.726400))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
cmd.select('tempjessatom2', 'jessatom2 & (jessatom3 a. %s)'%(d*1.535200))
cmd.select('jessatom2', 'tempjessatom2')
cmd.delete('tempjessatom2')
jesstemp14 ='r. glu'
jesstemp15 ='r. asp'
jesstemp16 ='jessatom0 a. %s'%(d*7.504300)
jesstemp17 ='jessatom1 a. %s'%(d*6.140800)
jesstemp18 ='jessatom2 a. %s'%(d*6.928600)
jesstemp19 ='jessatom3 a. %s'%(d*6.756900)
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom4 a. %s)'%(d*7.504300))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom4 a. %s)'%(d*6.140800))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
cmd.select('tempjessatom2', 'jessatom2 & (jessatom4 a. %s)'%(d*6.928600))
cmd.select('jessatom2', 'tempjessatom2')
cmd.delete('tempjessatom2')
cmd.select('tempjessatom3', 'jessatom3 & (jessatom4 a. %s)'%(d*6.756900))
cmd.select('jessatom3', 'tempjessatom3')
cmd.delete('tempjessatom3')
jesstemp20 ='jessatom0 a. %s'%(d*6.948800)
jesstemp21 ='jessatom1 a. %s'%(d*5.514600)
jesstemp22 ='jessatom2 a. %s'%(d*5.807500)
jesstemp23 ='jessatom3 a. %s'%(d*5.433800)
jesstemp24 ='jessatom4 a. %s'%(d*1.525100)
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom5 a. %s)'%(d*6.948800))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom5 a. %s)'%(d*5.514600))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
cmd.select('tempjessatom2', 'jessatom2 & (jessatom5 a. %s)'%(d*5.807500))
cmd.select('jessatom2', 'tempjessatom2')
cmd.delete('tempjessatom2')
cmd.select('tempjessatom3', 'jessatom3 & (jessatom5 a. %s)'%(d*5.433800))
cmd.select('jessatom3', 'tempjessatom3')
cmd.delete('tempjessatom3')
cmd.select('tempjessatom4', 'jessatom4 & (jessatom5 a. %s)'%(d*1.525100))
cmd.select('jessatom4', 'tempjessatom4')
cmd.delete('tempjessatom4')
cmd.select('Jab_1mbb_1_1_1_158', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
