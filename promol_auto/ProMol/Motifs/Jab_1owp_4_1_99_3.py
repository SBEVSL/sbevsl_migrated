'''
FUNC:Jab_1owp_4_1_99_3
PDB:1owp
EC:4.1.99.3
RESI:trp,trp,trp
LOCI:a-314,367,390;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. trp'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. trp'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(9.039500+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(7.827500+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.039500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.827500+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(9.706100+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(8.605200+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.565500+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.706100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.605200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.565500+(d*0.300000)))
jesstemp12 ='jessatom0 x. %s'%(14.786400+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(13.766300+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(6.565000+(d*0.300000))
jesstemp15 ='jessatom3 x. %s'%(5.312600+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(14.786400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.766300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.565000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(5.312600+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(14.291500+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(13.160300+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(5.676200+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(4.666200+(d*0.300000))
jesstemp20 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp21 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(14.291500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.160300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.666200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1owp_4_1_99_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
