'''
FUNC:Jab_1hmp_2_4_2_8
PDB:1hmp
EC:2.4.2.8
RESI:glu,asp,asp,lys,arg
LOCI:a-133,134,137,165,169;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.565500+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.565500+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(3.706700+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(4.312700+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.706700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.312700+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(4.706600+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(5.383300+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.535200+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.706600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.383300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.535200+(d*0.300000)))
jesstemp12 ='jessatom0 x. %s'%(10.827200+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(9.595000+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(9.958600+(d*0.300000))
jesstemp15 ='jessatom3 x. %s'%(10.554500+(d*0.300000))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp2+'))|(('+jesstemp0+')&('+jesstemp1+')))&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.827200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.595000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.958600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(10.554500+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(11.099900+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(9.908100+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(10.059600+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(10.433300+(d*0.300000))
jesstemp20 ='jessatom4 x. %s'%(1.555400+(d*0.300000))
jesstemp21 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp3+')&('+jesstemp2+'))|(('+jesstemp3+')&('+jesstemp1+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.099900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.908100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(10.059600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(10.433300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.555400+(d*0.300000)))
jesstemp22 ='r. lys'
jesstemp23 ='jessatom0 x. %s'%(12.988600+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(12.170500+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(11.261500+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(12.029100+(d*0.300000))
jesstemp27 ='jessatom4 x. %s'%(5.807500+(d*0.300000))
jesstemp28 ='jessatom5 x. %s'%(6.837700+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(12.988600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(12.170500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(11.261500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(12.029100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.807500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(6.837700+(d*0.300000)))
jesstemp29 ='jessatom0 x. %s'%(13.079500+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(12.200800+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(11.312000+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(11.948300+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(4.817700+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(5.666100+(d*0.300000))
jesstemp35 ='jessatom6 x. %s'%(1.515000+(d*0.300000))
jesstemp36 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp3+')&('+jesstemp22+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(13.079500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(12.200800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(11.312000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(11.948300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.817700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.666100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.515000+(d*0.300000)))
jesstemp37 ='r. arg'
jesstemp38 ='jessatom0 x. %s'%(18.250700+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(16.856900+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(17.786100+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(18.412300+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(7.857800+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(8.201200+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(9.857600+(d*0.300000))
jesstemp45 ='jessatom7 x. %s'%(8.938500+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp0+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(18.250700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(16.856900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(17.786100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(18.412300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.201200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(9.857600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(8.938500+(d*0.300000)))
jesstemp46 ='jessatom0 x. %s'%(17.887100+(d*0.300000))
jesstemp47 ='jessatom1 x. %s'%(16.523600+(d*0.300000))
jesstemp48 ='jessatom2 x. %s'%(17.230600+(d*0.300000))
jesstemp49 ='jessatom3 x. %s'%(17.745700+(d*0.300000))
jesstemp50 ='jessatom4 x. %s'%(7.282100+(d*0.300000))
jesstemp51 ='jessatom5 x. %s'%(7.373000+(d*0.300000))
jesstemp52 ='jessatom6 x. %s'%(9.655600+(d*0.300000))
jesstemp53 ='jessatom7 x. %s'%(8.544600+(d*0.300000))
jesstemp54 ='jessatom8 x. %s'%(1.525100+(d*0.300000))
jesstemp55 ='br. jessatom8'
cmd.select('jessatom9', '(('+jesstemp3+')&('+jesstemp37+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(17.887100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(16.523600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(17.230600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(17.745700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(7.282100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.373000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(9.655600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(8.544600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(1.525100+(d*0.300000)))
cmd.select('Jab_1hmp_2_4_2_8', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
