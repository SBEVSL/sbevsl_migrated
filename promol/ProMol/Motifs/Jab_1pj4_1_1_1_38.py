'''
FUNC:Jab_1pj4_1_1_1_38
PDB:1pj4
EC:1.1.1.38
RESI:tyr,lys,asp
LOCI:a-112,183,278;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. lys'
jesstemp7 ='jessatom0 x. %s'%(7.847700+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(7.474000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(7.847700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.474000+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(8.888000+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(8.554700+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.888000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.554700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='r. asp'
jesstemp14 ='r. glu'
jesstemp15 ='jessatom0 x. %s'%(14.998500+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(14.352100+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(10.231300+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(8.989000+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp13+'))|(('+jesstemp0+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(14.998500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(14.352100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.231300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(8.989000+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(13.665300+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(13.059300+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(8.696100+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(7.443700+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp13+'))|(('+jesstemp2+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(13.665300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.059300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.696100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(7.443700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1pj4_1_1_1_38', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
