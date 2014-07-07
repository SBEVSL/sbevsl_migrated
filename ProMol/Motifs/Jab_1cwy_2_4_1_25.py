'''
FUNC:Jab_1cwy_2_4_1_25
PDB:1cwy
EC:2.4.1.25
RESI:asp,glu,asp
LOCI:a-293,340,395;
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
jesstemp6 ='jessatom0 x. %s'%(5.201500+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(6.453900+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.201500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(6.453900+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(3.878400+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(4.999500+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(3.878400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp12 ='jessatom0 x. %s'%(11.978600+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(11.180700+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(12.534100+(d*0.300000))
jesstemp15 ='jessatom3 x. %s'%(11.514000+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.978600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.180700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(12.534100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(11.514000+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(10.847400+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(10.089900+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(11.453400+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(10.403000+(d*0.300000))
jesstemp20 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp21 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.847400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.089900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.453400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(10.403000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1cwy_2_4_1_25', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
