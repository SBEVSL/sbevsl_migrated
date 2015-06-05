'''
FUNC:Jab_1pow
PDB:1pow
EC:1.2.3.3
PFAM:PF02775,PF00205,PF02776
RESI:arg,phe,glu
LOCI:a-264,479,483;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. arg'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. phe'
jesstemp7 ='jessatom0 x. %s'%(10.544400+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(9.443500+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(10.544400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(9.443500+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(10.291900+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(9.201100+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.291900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.201100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='r. glu'
jesstemp14 ='r. asp'
jesstemp15 ='jessatom0 x. %s'%(11.049400+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(9.685900+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(6.615500+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(7.534600+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp13+'))|(('+jesstemp0+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.049400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.685900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.615500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(7.534600+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(11.069600+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(9.615200+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(6.332700+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(6.999300+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.504900+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp13+'))|(('+jesstemp2+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.069600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.615200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.332700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(6.999300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.504900+(d*0.300000)))
cmd.select('Jab_1pow', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
