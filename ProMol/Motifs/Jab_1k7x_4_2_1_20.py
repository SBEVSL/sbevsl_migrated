'''
FUNC:Jab_1k7x_4_2_1_20
PDB:1k7x
EC:4.2.1.20
RESI:his,lys,lys,asp
LOCI:b-86,87,167,305;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.646300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.646300+(d*0.300000)))
jesstemp6 ='r. lys'
jesstemp7 ='jessatom0 x. %s'%(3.918800+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(4.635900+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.918800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.635900+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(4.999500+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(5.736800+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.565500+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.736800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.565500+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(21.563500+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(21.351400+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(18.533500+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(17.402300+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(21.563500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(21.351400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(18.533500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(17.402300+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(22.482600+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(22.179600+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(19.594000+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(18.503200+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.585700+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(22.482600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(22.179600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(19.594000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(18.503200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.585700+(d*0.300000)))
jesstemp23 ='r. asp'
jesstemp24 ='r. glu'
jesstemp25 ='jessatom0 x. %s'%(16.665000+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(16.200400+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(15.018700+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(13.958200+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(9.150600+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(9.170800+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp23+'))|(('+jesstemp0+')&('+jesstemp24+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(16.665000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(16.200400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(15.018700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(13.958200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(9.150600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.170800+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(16.988200+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(16.675100+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(15.170200+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(13.998600+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(8.756700+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(8.928400+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.636200+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp23+'))|(('+jesstemp2+')&('+jesstemp24+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(16.988200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(16.675100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(15.170200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(13.998600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.756700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.928400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.636200+(d*0.300000)))
cmd.select('Jab_1k7x_4_2_1_20', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
