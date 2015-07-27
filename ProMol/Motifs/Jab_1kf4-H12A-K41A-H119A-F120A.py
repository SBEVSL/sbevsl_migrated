'''
FUNC:Jab_1kf4-H12A-K41A-H119A-F120A
PDB:1kf4
EC:3.1.27.5
PFAM:PF00074
RESI:his,lys,his,phe
LOCI:a-12,41,119,120;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. lys'
jesstemp7 ='jessatom0 x. %s'%(12.887600+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(13.231000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.887600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(13.231000+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(11.453400+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(11.817000+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.453400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(11.817000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(9.079900+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(7.716400+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(14.927800+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(13.756200+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.079900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.716400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(14.927800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(13.756200+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(10.504000+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(9.160700+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(15.230800+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(14.160200+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.504000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.160700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(15.230800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(14.160200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
jesstemp23 ='n.  n  '
jesstemp24 ='jessatom0 x. %s'%(7.807300+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(6.373100+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(13.948100+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(12.806800+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(2.444200+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(3.383500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.807300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.373100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(13.948100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(12.806800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.383500+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(7.696200+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.241800+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(14.099600+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(12.998700+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(3.827900+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(4.646000+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.464500+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp0+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.696200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(14.099600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(12.998700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.827900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.646000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.464500+(d*0.300000)))
cmd.select('Jab_1kf4-H12A-K41A-H119A-F120A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
