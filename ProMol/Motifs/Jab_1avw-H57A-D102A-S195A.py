'''
FUNC:Jab_1avw-H57A-D102A-S195A
PDB:1avw
EC:3.4.21.4
PFAM:PF00197,PF00089
RESI:his,asp,ser
LOCI:a-57,102,195;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. asp'
jesstemp7 ='r. glu'
jesstemp8 ='jessatom0 x. %s'%(6.595300+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(6.544800+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(6.595300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(6.544800+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(6.302400+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(5.908500+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.302400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.908500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp14 ='r. ser'
jesstemp15 ='r. thr'
jesstemp16 ='jessatom0 x. %s'%(8.453700+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(7.948700+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(10.322200+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(9.352600+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.453700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.948700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.322200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(9.352600+(d*0.300000)))
jesstemp20 ='jessatom0 x. %s'%(7.261900+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(6.716500+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(9.958600+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(8.968800+(d*0.300000))
jesstemp24 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.261900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.716500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.958600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(8.968800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1avw-H57A-D102A-S195A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
