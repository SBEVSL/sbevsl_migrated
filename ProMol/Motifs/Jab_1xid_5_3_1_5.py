'''
FUNC:Jab_1xid_5_3_1_5
PDB:1xid
EC:5.3.1.5
RESI:his,asp,glu,lys
LOCI:a-54,57,181,183;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='r. asp'
jesstemp7 ='r. glu'
jesstemp8 ='jessatom0 x. %s'%(5.211600+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(5.019700+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.211600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(5.019700+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(4.565200+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(4.555100+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.565200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.555100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(13.978400+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(13.806700+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(18.493100+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(17.513400+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp7+'))|(('+jesstemp0+')&('+jesstemp6+')))&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(13.978400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.806700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(18.493100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(17.513400+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(12.594700+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(12.412900+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(17.018500+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(16.018600+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp7+'))|(('+jesstemp2+')&('+jesstemp6+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.594700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(12.412900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(17.018500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(16.018600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp24 ='r. lys'
jesstemp25 ='jessatom0 x. %s'%(17.574000+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(16.856900+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(21.018100+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(20.200000+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(6.807400+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(7.120500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(17.574000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(16.856900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(21.018100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(20.200000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.807400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.120500+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(16.331700+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(15.554000+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(19.614200+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(18.826400+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(6.827600+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(6.807400+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.565500+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp24+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(16.331700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(15.554000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(19.614200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(18.826400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.827600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.807400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.565500+(d*0.300000)))
cmd.select('Jab_1xid_5_3_1_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
