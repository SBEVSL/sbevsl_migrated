'''
FUNC:Jab_1ah3_1_1_1_21
PDB:1ah3
EC:1.1.1.21
RESI:asp,tyr,lys,his
LOCI:a-43,48,77,110;
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
jesstemp6 ='r. tyr'
jesstemp7 ='jessatom0 x. %s'%(10.554500+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(10.766600+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(10.554500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.766600+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(9.120300+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(9.342500+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.120300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.342500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='r. lys'
jesstemp14 ='jessatom0 x. %s'%(8.918300+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(9.241500+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(9.857600+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(9.504100+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.918300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.857600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(9.504100+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(8.544600+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(8.625400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(9.281900+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(8.888000+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.565500+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.625400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.281900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(8.888000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.565500+(d*0.300000)))
jesstemp24 ='r. his'
jesstemp25 ='jessatom0 x. %s'%(11.857400+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(11.503900+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(11.483700+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(11.413000+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(5.171200+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(4.191500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.857400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.503900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(11.483700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.413000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.191500+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(11.665500+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(11.402900+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(10.140400+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(10.190900+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(4.817700+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(3.797600+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp3+')&('+jesstemp24+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(11.665500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.402900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.140400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.190900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.817700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.797600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_1ah3_1_1_1_21', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
