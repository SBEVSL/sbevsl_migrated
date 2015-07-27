'''
FUNC:Jab_2nac-N146A-R284A-Q313A-H332A
PDB:2nac
EC:1.2.1.2
PFAM:PF02826,PF00389
RESI:asn,arg,gln,his
LOCI:a-146,284,313,332;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.515000+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.515000+(d*0.300000)))
jesstemp6 ='r. arg'
jesstemp7 ='jessatom0 x. %s'%(15.463100+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(14.756100+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(15.463100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(14.756100+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(16.038800+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(15.372200+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.575600+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(16.038800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(15.372200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.575600+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(19.725300+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(18.412300+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(10.332300+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(10.766600+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(19.725300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(18.412300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.332300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(10.766600+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(18.230500+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(16.917500+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(9.362700+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(9.827300+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.525100+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(18.230500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(16.917500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.362700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(9.827300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.525100+(d*0.300000)))
jesstemp23 ='r. his'
jesstemp24 ='jessatom0 x. %s'%(12.998700+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(11.695800+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(10.019200+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(11.211000+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(8.433500+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(7.302300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.998700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.695800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.019200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.211000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.433500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.302300+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(13.321900+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(11.998800+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(9.231400+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(10.281800+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(7.201300+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(5.959000+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.565500+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp3+')&('+jesstemp23+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(13.321900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.998800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.231400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.281800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.201300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.565500+(d*0.300000)))
cmd.select('Jab_2nac-N146A-R284A-Q313A-H332A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
