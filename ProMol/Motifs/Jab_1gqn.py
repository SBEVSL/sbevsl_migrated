'''
FUNC:Jab_1gqn
PDB:1gqn
EC:4.2.1.10
PFAM:PF01487
RESI:glu,his,lys
LOCI:a-86,143,170;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.575600+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.575600+(d*0.300000)))
jesstemp6 ='r. his'
jesstemp7 ='jessatom0 x. %s'%(5.555000+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(4.938900+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.555000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.938900+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(4.635900+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(4.090500+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.595800+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.635900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.090500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.595800+(d*0.300000)))
jesstemp13 ='r. lys'
jesstemp14 ='jessatom0 x. %s'%(12.827000+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(11.524100+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(8.524400+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(9.009200+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.827000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.524100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.524400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(9.009200+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(12.301800+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(10.978700+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(8.463800+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(8.675900+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.585700+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.301800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.978700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.463800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.585700+(d*0.300000)))
cmd.select('Jab_1gqn', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
