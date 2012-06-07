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
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. ser'
jesstemp7 ='r. thr'
jesstemp8 ='jessatom0 x. %s'%(11.120100+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(9.776800+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(11.120100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(9.776800+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(10.069700+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(8.726400+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.069700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.726400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp14 ='r. glu'
jesstemp15 ='r. asp'
jesstemp16 ='jessatom0 x. %s'%(7.504300+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(6.140800+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(6.928600+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(6.756900+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(7.504300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.928600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(6.756900+(d*0.300000)))
jesstemp20 ='jessatom0 x. %s'%(6.948800+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(5.514600+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(5.807500+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(5.433800+(d*0.300000))
jesstemp24 ='jessatom4 x. %s'%(1.525100+(d*0.300000))
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.514600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(5.433800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.525100+(d*0.300000)))
cmd.select('Jab_1mbb_1_1_1_158', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
