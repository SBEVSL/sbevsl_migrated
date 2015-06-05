'''
FUNC:Jab_1onr
PDB:1onr
EC:2.2.1.2
PFAM:PF00923
RESI:asp,glu,lys
LOCI:a-17,96,132;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(12.786600+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(13.069400+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.786600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(13.069400+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(12.109900+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(12.261400+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(12.109900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.261400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp12 ='r. lys'
jesstemp13 ='jessatom0 x. %s'%(13.119900+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(13.200700+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(4.221800+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(4.696500+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(13.119900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.200700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.221800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(4.696500+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(11.726100+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(11.806900+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(3.595600+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(3.757200+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp12+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.726100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.806900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.595600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1onr', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
