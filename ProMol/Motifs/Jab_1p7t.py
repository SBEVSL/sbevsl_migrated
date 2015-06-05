'''
FUNC:Jab_1p7t
PDB:1p7t
EC:2.3.3.9
PFAM:PF01274
RESI:asp,glu,arg,asp
LOCI:a-270,272,338,631;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.595800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.595800+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(5.534800+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(5.272200+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.534800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(5.272200+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(5.878200+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(5.645900+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.645900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp12 ='r. arg'
jesstemp13 ='jessatom0 x. %s'%(4.696500+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(5.676200+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(6.383200+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(5.736800+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.696500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.383200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(5.736800+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(4.353100+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(4.938900+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(5.797400+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(4.999500+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.504900+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp12+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.353100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.797400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.504900+(d*0.300000)))
jesstemp23 ='jessatom0 x. %s'%(11.776600+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(10.281800+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(9.645500+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(9.988900+(d*0.300000))
jesstemp27 ='jessatom4 x. %s'%(14.402600+(d*0.300000))
jesstemp28 ='jessatom5 x. %s'%(13.140100+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.776600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.281800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.988900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(14.402600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(13.140100+(d*0.300000)))
jesstemp29 ='jessatom0 x. %s'%(10.352500+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(8.837500+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(8.645600+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(8.948600+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(13.029000+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(11.756400+(d*0.300000))
jesstemp35 ='jessatom6 x. %s'%(1.565500+(d*0.300000))
jesstemp36 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(10.352500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.837500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(8.645600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(8.948600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(13.029000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(11.756400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.565500+(d*0.300000)))
cmd.select('Jab_1p7t', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
