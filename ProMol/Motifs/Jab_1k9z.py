'''
FUNC:Jab_1k9z
PDB:1k9z
EC:3.1.3.7
PFAM:PF00459
RESI:asp,thr,asp
LOCI:a-49,147,294;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. thr'
jesstemp7 ='r. ser'
jesstemp8 ='jessatom0 x. %s'%(7.766900+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(7.049800+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(7.766900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.049800+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(7.110400+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(6.140800+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp6+'))|(('+jesstemp3+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.110400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.140800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(14.008700+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(13.402700+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(11.766500+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(11.756400+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(14.008700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.402700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(11.766500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(11.756400+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(14.402600+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(13.655200+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(11.524100+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(11.463500+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(14.402600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.655200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.524100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1k9z', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
