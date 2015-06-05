'''
FUNC:Jab_1d8h
PDB:1d8h
EC:3.1.3.33
PFAM:PF02940
RESI:arg,glu,lys,arg
LOCI:a-393,433,456,458;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. arg'
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. glu'
jesstemp7 ='r. asp'
jesstemp8 ='jessatom0 x. %s'%(9.625300+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(8.716300+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.625300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(8.716300+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(9.786900+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(8.776900+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.786900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.776900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp14 ='r. lys'
jesstemp15 ='jessatom0 x. %s'%(13.382500+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(12.524000+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(17.624500+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(16.675100+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(13.382500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(12.524000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(17.624500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(16.675100+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(12.372500+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(11.423100+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(16.099400+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(15.129800+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.585700+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(12.372500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(11.423100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(16.099400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(15.129800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.585700+(d*0.300000)))
jesstemp25 ='jessatom0 x. %s'%(17.654800+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(16.564000+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(19.139500+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(17.856800+(d*0.300000))
jesstemp29 ='jessatom4 x. %s'%(6.100400+(d*0.300000))
jesstemp30 ='jessatom5 x. %s'%(6.009500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(17.654800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(16.564000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(19.139500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(17.856800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.100400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.009500+(d*0.300000)))
jesstemp31 ='jessatom0 x. %s'%(16.351900+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(15.230800+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(17.553800+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(16.271100+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(5.787300+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(5.292400+(d*0.300000))
jesstemp37 ='jessatom6 x. %s'%(1.585700+(d*0.300000))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(16.351900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(15.230800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(17.553800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(16.271100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.787300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.292400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.585700+(d*0.300000)))
cmd.select('Jab_1d8h', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
