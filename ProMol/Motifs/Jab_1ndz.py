'''
FUNC:Jab_1ndz
PDB:1ndz
EC:3.5.4.4
PFAM:PF00962
RESI:glu,his,tyr,asp
LOCI:a-217,238,240,295;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. his'
jesstemp7 ='jessatom0 x. %s'%(5.433800+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(5.262100+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.433800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(5.262100+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(4.040000+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(3.767300+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.525100+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.040000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.767300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.525100+(d*0.300000)))
jesstemp13 ='r. tyr'
jesstemp14 ='jessatom0 x. %s'%(5.726700+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(6.908400+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(5.666100+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(5.565100+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.908400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.666100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(5.565100+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(5.171200+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(6.332700+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(5.797400+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(5.403500+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.332700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.797400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(5.403500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(12.170500+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(10.857500+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(9.968700+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(9.797000+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(14.836900+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(14.200600+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.170500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.857500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.968700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.797000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(14.836900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(14.200600+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(10.807000+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(9.524300+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(9.049600+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(8.706200+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(13.624900+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(12.887600+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.636200+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.807000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.524300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.049600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(13.624900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(12.887600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.636200+(d*0.300000)))
cmd.select('Jab_1ndz', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
