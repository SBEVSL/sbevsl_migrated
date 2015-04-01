'''
FUNC:Jab_5csm_5_4_99_5
PDB:5csm
EC:5.4.99.5
RESI:arg,arg,lys,glu
LOCI:a-16,157,168,246;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. arg'
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(11.463500+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(12.887600+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(12.887600+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(11.493800+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(12.847200+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.493800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.847200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp12 ='r. lys'
jesstemp13 ='jessatom0 x. %s'%(13.534000+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(13.766300+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(17.473000+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(18.371900+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(13.534000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(13.766300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(17.473000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(18.371900+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(13.392600+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(13.645100+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(16.856900+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(17.695200+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp12+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(13.392600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(13.645100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(16.856900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(17.695200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
jesstemp23 ='r. glu'
jesstemp24 ='r. asp'
jesstemp25 ='jessatom0 x. %s'%(15.796400+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(16.705400+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(12.311900+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(13.241100+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(10.190900+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(9.110200+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp23+'))|(('+jesstemp0+')&('+jesstemp24+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(15.796400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(16.705400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(12.311900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(13.241100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.190900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.110200+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(14.735900+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(15.554000+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(12.130100+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(12.958300+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(9.443500+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(8.241600+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp23+'))|(('+jesstemp2+')&('+jesstemp24+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(14.735900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(15.554000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(12.130100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(12.958300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.443500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.241600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_5csm_5_4_99_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
