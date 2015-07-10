'''
FUNC:Jab_1b0p-T31A-E64A-R114A-N996A
PDB:1b0p
EC:1.2.7.1
PFAM:PF01558,PF02775,PF01855,PF00037,PF13237,PF12838,PF12837,PF10371
RESI:thr,glu,arg,asn
LOCI:a-31,64,114,996;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. thr'
jesstemp2 ='r. ser'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.575600+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.575600+(d*0.300000)))
jesstemp6 ='r. glu'
jesstemp7 ='r. asp'
jesstemp8 ='jessatom0 x. %s'%(12.766400+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(13.887500+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.766400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(13.887500+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(11.604900+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(12.756300+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp6+'))|(('+jesstemp3+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.604900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.756300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp14 ='r. arg'
jesstemp15 ='jessatom0 x. %s'%(8.433500+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(8.898100+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(15.049000+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(13.513800+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.433500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.898100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(15.049000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(13.513800+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(6.948800+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(7.453800+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(14.018800+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(12.503800+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.453800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(14.018800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(12.503800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp25 ='r. asn'
jesstemp26 ='r. gln'
jesstemp27 ='jessatom0 x. %s'%(9.766700+(d*0.300000))
jesstemp28 ='jessatom1 x. %s'%(8.766800+(d*0.300000))
jesstemp29 ='jessatom2 x. %s'%(17.291200+(d*0.300000))
jesstemp30 ='jessatom3 x. %s'%(16.816500+(d*0.300000))
jesstemp31 ='jessatom4 x. %s'%(17.200300+(d*0.300000))
jesstemp32 ='jessatom5 x. %s'%(15.766100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp25+'))|(('+jesstemp0+')&('+jesstemp26+')))&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.766700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.766800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(17.291200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(16.816500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(17.200300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(15.766100+(d*0.300000)))
jesstemp33 ='jessatom0 x. %s'%(9.706100+(d*0.300000))
jesstemp34 ='jessatom1 x. %s'%(8.615300+(d*0.300000))
jesstemp35 ='jessatom2 x. %s'%(17.119500+(d*0.300000))
jesstemp36 ='jessatom3 x. %s'%(16.604400+(d*0.300000))
jesstemp37 ='jessatom4 x. %s'%(16.634700+(d*0.300000))
jesstemp38 ='jessatom5 x. %s'%(15.230800+(d*0.300000))
jesstemp39 ='jessatom6 x. %s'%(1.555400+(d*0.300000))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp25+'))|(('+jesstemp3+')&('+jesstemp26+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.706100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.615300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(17.119500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(16.604400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(16.634700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(15.230800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1b0p-T31A-E64A-R114A-N996A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
