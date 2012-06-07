'''
FUNC:Jab_1qnt_2_1_1_63
PDB:1qnt
EC:2.1.1.63
RESI:asn,cys,his,glu
LOCI:a-137,145,146,172;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. cys'
jesstemp7 ='jessatom0 x. %s'%(7.605300+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(6.080200+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(7.605300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(6.080200+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(6.312500+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(4.807600+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.312500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.807600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp13 ='r. his'
jesstemp14 ='jessatom0 x. %s'%(10.756500+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(9.241500+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(3.848100+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(4.706600+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.756500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.848100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(4.706600+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(11.332200+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(9.837400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(4.928800+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(5.686300+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.332200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.837400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp24 ='r. glu'
jesstemp25 ='r. asp'
jesstemp26 ='jessatom0 x. %s'%(20.099000+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(18.614300+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(13.513800+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(14.766200+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(10.695900+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(9.776800+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp24+'))|(('+jesstemp0+')&('+jesstemp25+')))&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(20.099000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(18.614300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(13.513800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(14.766200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.695900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.776800+(d*0.300000)))
jesstemp32 ='jessatom0 x. %s'%(18.765800+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(17.271000+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(12.079600+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(13.362300+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(9.403100+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(8.564800+(d*0.300000))
jesstemp38 ='jessatom6 x. %s'%(1.545300+(d*0.300000))
jesstemp39 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp24+'))|(('+jesstemp3+')&('+jesstemp25+')))&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(18.765800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(17.271000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(12.079600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(13.362300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.403100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1qnt_2_1_1_63', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
