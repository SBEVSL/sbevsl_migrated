'''
FUNC:Jab_1raf
PDB:1raf
EC:2.1.3.2
PFAM:PF02748,PF00185,PF01948,PF02729
RESI:arg,thr,arg,his
LOCI:a-54,55,105,134;
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
jesstemp6 ='r. thr'
jesstemp7 ='r. ser'
jesstemp8 ='jessatom0 x. %s'%(3.898600+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(4.494500+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.898600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.494500+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(4.949000+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(5.312600+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(12.372500+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(12.968400+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(9.251600+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(8.049700+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.372500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.968400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.251600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(8.049700+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(10.867600+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(11.463500+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(7.878000+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(6.676100+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.867600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(7.878000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(6.676100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp24 ='r. his'
jesstemp25 ='jessatom0 x. %s'%(13.715800+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(13.392600+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(10.514100+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(9.251600+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(9.029400+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(8.958700+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(13.715800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(13.392600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.514100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.251600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.029400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.958700+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(12.756300+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(12.332100+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(9.817200+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(8.514300+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(9.069800+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(8.766800+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.525100+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp24+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(12.756300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(12.332100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.817200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.514300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.069800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.766800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.525100+(d*0.300000)))
cmd.select('Jab_1raf', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
