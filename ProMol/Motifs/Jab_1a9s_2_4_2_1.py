'''
FUNC:Jab_1a9s_2_4_2_1
PDB:1a9s
EC:2.4.2.1
RESI:his,glu,asn
LOCI:a-86,89,243;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 a. %s'%(d*1.545300)
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom1 a. %s)'%(d*1.545300))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
jesstemp6 ='r. glu'
jesstemp7 ='r. asp'
jesstemp8 ='jessatom0 a. %s'%(d*5.716600)
jesstemp9 ='jessatom1 a. %s'%(d*5.575200)
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom2 a. %s)'%(d*5.716600))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom2 a. %s)'%(d*5.575200))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
jesstemp10 ='jessatom0 a. %s'%(d*5.090400)
jesstemp11 ='jessatom1 a. %s'%(d*5.100500)
jesstemp12 ='jessatom2 a. %s'%(d*1.545300)
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom3 a. %s)'%(d*5.090400))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom3 a. %s)'%(d*5.100500))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
cmd.select('tempjessatom2', 'jessatom2 & (jessatom3 a. %s)'%(d*1.545300))
cmd.select('jessatom2', 'tempjessatom2')
cmd.delete('tempjessatom2')
jesstemp14 ='r. asn'
jesstemp15 ='r. gln'
jesstemp16 ='jessatom0 a. %s'%(d*19.937400)
jesstemp17 ='jessatom1 a. %s'%(d*18.614300)
jesstemp18 ='jessatom2 a. %s'%(d*22.290700)
jesstemp19 ='jessatom3 a. %s'%(d*22.300800)
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom4 a. %s)'%(d*19.937400))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom4 a. %s)'%(d*18.614300))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
cmd.select('tempjessatom2', 'jessatom2 & (jessatom4 a. %s)'%(d*22.290700))
cmd.select('jessatom2', 'tempjessatom2')
cmd.delete('tempjessatom2')
cmd.select('tempjessatom3', 'jessatom3 & (jessatom4 a. %s)'%(d*22.300800))
cmd.select('jessatom3', 'tempjessatom3')
cmd.delete('tempjessatom3')
jesstemp20 ='jessatom0 a. %s'%(d*19.351600)
jesstemp21 ='jessatom1 a. %s'%(d*17.967900)
jesstemp22 ='jessatom2 a. %s'%(d*21.351400)
jesstemp23 ='jessatom3 a. %s'%(d*21.422100)
jesstemp24 ='jessatom4 a. %s'%(d*1.555400)
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('tempjessatom0', 'jessatom0 & (jessatom5 a. %s)'%(d*19.351600))
cmd.select('jessatom0', 'tempjessatom0')
cmd.delete('tempjessatom0')
cmd.select('tempjessatom1', 'jessatom1 & (jessatom5 a. %s)'%(d*17.967900))
cmd.select('jessatom1', 'tempjessatom1')
cmd.delete('tempjessatom1')
cmd.select('tempjessatom2', 'jessatom2 & (jessatom5 a. %s)'%(d*21.351400))
cmd.select('jessatom2', 'tempjessatom2')
cmd.delete('tempjessatom2')
cmd.select('tempjessatom3', 'jessatom3 & (jessatom5 a. %s)'%(d*21.422100))
cmd.select('jessatom3', 'tempjessatom3')
cmd.delete('tempjessatom3')
cmd.select('tempjessatom4', 'jessatom4 & (jessatom5 a. %s)'%(d*1.555400))
cmd.select('jessatom4', 'tempjessatom4')
cmd.delete('tempjessatom4')
cmd.select('Jab_1a9s_2_4_2_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
