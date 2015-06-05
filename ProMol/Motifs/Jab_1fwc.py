'''
FUNC:Jab_1fwc
PDB:1fwc
EC:3.5.1.5
PFAM:PF00699,PF01979,PF00449,PF00547,PF07969,PF13594
RESI:his,asp,his,arg
LOCI:c-219,221,320,336;
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
jesstemp8 ='jessatom0 x. %s'%(5.504500+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(5.171200+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.504500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(5.171200+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(5.807500+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(5.090400+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.090400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(11.382700+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(10.504000+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(8.009300+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(6.857900+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.382700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(10.504000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.009300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(6.857900+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(10.807000+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(10.100000+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(7.544700+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(6.585200+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.807000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.100000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.544700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(6.585200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp24 ='r. arg'
jesstemp25 ='jessatom0 x. %s'%(15.412600+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(15.725700+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(14.756100+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(14.705600+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(12.392700+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(11.009000+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(15.412600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(15.725700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(14.756100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(14.705600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(12.392700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(11.009000+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(14.271300+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(14.483400+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(13.453200+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(13.321900+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(10.887800+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(9.504100+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp24+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(14.271300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(14.483400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(13.453200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(13.321900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(10.887800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.504100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1fwc', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
