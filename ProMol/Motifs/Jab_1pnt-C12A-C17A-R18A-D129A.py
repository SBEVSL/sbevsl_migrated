'''
FUNC:Jab_1pnt-C12A-C17A-R18A-D129A
PDB:1pnt
EC:3.1.3.2
PFAM:PF01451
RESI:cys,cys,arg,asp
LOCI:a-12,17,18,129;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. cys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. cys'
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(8.181000+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(6.767000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(8.181000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(6.767000+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(8.544600+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(7.090200+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.090200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp12 ='r. arg'
jesstemp13 ='jessatom0 x. %s'%(6.322600+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(4.858100+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(3.868300+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(4.383400+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.322600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.868300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(4.383400+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(5.656000+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(4.181400+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(4.868200+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(4.989400+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.565500+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp12+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.656000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.181400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.868200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.565500+(d*0.300000)))
jesstemp23 ='r. asp'
jesstemp24 ='r. glu'
jesstemp25 ='jessatom0 x. %s'%(8.978900+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(7.817400+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(7.797200+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(6.575100+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(7.251800+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(6.201400+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp23+'))|(('+jesstemp0+')&('+jesstemp24+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.797200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.251800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.201400+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(8.888000+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(7.888100+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(8.292100+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(7.059900+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(8.090100+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(7.039700+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp23+'))|(('+jesstemp2+')&('+jesstemp24+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.888000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.888100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.292100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.059900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.090100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1pnt-C12A-C17A-R18A-D129A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
