'''
FUNC:Jab_1f61
PDB:1f61
EC:4.1.3.1
PFAM:PF00463,PF13714
RESI:his,cys,arg
LOCI:a-180,191,228;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.565500+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.565500+(d*0.300000)))
jesstemp6 ='r. cys'
jesstemp7 ='jessatom0 x. %s'%(25.149000+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(24.623800+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(25.149000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(24.623800+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(25.755000+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(25.239900+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(25.755000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(25.239900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp13 ='r. arg'
jesstemp14 ='jessatom0 x. %s'%(6.696300+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(6.060000+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(22.119000+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(23.048200+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(22.119000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(23.048200+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(6.100400+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(5.292400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(21.321100+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(22.179600+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.100400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.292400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(21.321100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(22.179600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1f61', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
