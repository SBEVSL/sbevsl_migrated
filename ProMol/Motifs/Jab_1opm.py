'''
FUNC:Jab_1opm
PDB:1opm
EC:1.14.17.3
PFAM:PF01082,PF03712
RESI:his,gln,his
LOCI:a-108,170,242;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.575600+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.575600+(d*0.300000)))
jesstemp6 ='r. gln'
jesstemp7 ='r. asn'
jesstemp8 ='jessatom0 x. %s'%(8.544600+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(8.857700+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(8.857700+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(8.595100+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(8.635500+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.595100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.635500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(12.988600+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(11.463500+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(15.291400+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(13.998600+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.988600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(15.291400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(13.998600+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(12.463400+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(10.978700+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(14.039000+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(12.705800+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.463400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.978700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(14.039000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(12.705800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1opm', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
