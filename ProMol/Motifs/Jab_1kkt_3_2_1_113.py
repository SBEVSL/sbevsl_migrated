'''
FUNC:Jab_1kkt_3_2_1_113
PDB:1kkt
EC:3.2.1.113
RESI:glu,arg,asp,glu
LOCI:a-122,126,267,409;
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
jesstemp6 ='r. arg'
jesstemp7 ='jessatom0 x. %s'%(6.110500+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(6.878100+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(6.110500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(6.878100+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(5.625700+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(6.060000+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.555400+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp3+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.555400+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(14.321800+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(14.927800+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(16.685200+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(16.947800+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(14.321800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(14.927800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(16.685200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(16.947800+(d*0.300000)))
jesstemp17 ='jessatom0 x. %s'%(13.756200+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(14.271300+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(15.947900+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(16.129700+(d*0.300000))
jesstemp21 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp22 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(13.756200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(14.271300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(15.947900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(16.129700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp23 ='jessatom0 x. %s'%(16.644800+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(16.917500+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(15.766100+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(15.806500+(d*0.300000))
jesstemp27 ='jessatom4 x. %s'%(11.200900+(d*0.300000))
jesstemp28 ='jessatom5 x. %s'%(9.857600+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(16.644800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(16.917500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(15.766100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(15.806500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(11.200900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.857600+(d*0.300000)))
jesstemp29 ='jessatom0 x. %s'%(16.240800+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(16.473100+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(15.927700+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(15.927700+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(9.958600+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(8.585000+(d*0.300000))
jesstemp35 ='jessatom6 x. %s'%(1.555400+(d*0.300000))
jesstemp36 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(16.240800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(16.473100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(15.927700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(15.927700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.958600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.585000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1kkt_3_2_1_113', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
