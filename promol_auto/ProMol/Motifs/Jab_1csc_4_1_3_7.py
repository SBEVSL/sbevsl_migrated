'''
FUNC:Jab_1csc_4_1_3_7
PDB:1csc
EC:4.1.3.7
RESI:his,his,asp
LOCI:a-274,320,375;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.575600+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.575600+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(9.797000+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(10.645400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.797000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.645400+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(10.423200+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(11.241300+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.565500+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.423200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(11.241300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.565500+(d*0.300000)))
jesstemp12 ='r. asp'
jesstemp13 ='r. glu'
jesstemp14 ='jessatom0 x. %s'%(9.170800+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(10.453500+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(10.625200+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(10.281800+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp12+'))|(('+jesstemp0+')&('+jesstemp13+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.170800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(10.453500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.625200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(10.281800+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(7.787100+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(9.130400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(10.130300+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(9.988900+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp12+'))|(('+jesstemp2+')&('+jesstemp13+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.787100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(10.130300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(9.988900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1csc_4_1_3_7', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
