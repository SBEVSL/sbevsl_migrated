'''
FUNC:Jab_1dd8
PDB:1dd8
EC:2.3.1.41
PFAM:PF02801,PF00108,PF00109
RESI:cys,his,lys,his,phe,phe
LOCI:a-163,298,328,333,390,392;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. cys'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. cys'
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. his'
jesstemp7 ='jessatom0 x. %s'%(9.049600+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(7.979000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.049600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(7.979000+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(8.443600+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(7.302300+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.443600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.302300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(8.514300+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(8.009300+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(9.382900+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(9.958600+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.514300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.009300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.382900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(9.958600+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(8.019400+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(7.322500+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(9.049600+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(9.443500+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.019400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.322500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.049600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(9.443500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp23 ='n.  n  '
jesstemp24 ='jessatom0 x. %s'%(5.443900+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(4.959100+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(11.140300+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(9.958600+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(12.130100+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(11.059500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.443900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.959100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(11.140300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.958600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(12.130100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(11.059500+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(6.807400+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.352900+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(12.392700+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(11.170600+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(13.180500+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(12.029100+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.474600+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp0+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.807400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.352900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(12.392700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(11.170600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(13.180500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(12.029100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.474600+(d*0.300000)))
cmd.select('Jab_1dd8', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
