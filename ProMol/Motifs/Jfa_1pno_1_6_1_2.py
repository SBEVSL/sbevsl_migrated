'''
FUNC:Jfa_1pno_1_6_1_2
PDB:1pno
EC:1.6.1.2
RESI:tyr,arg,tyr
LOCI:a-316,351,432;
'''
jesstemp0 ='n.  ce1'
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cz '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.403900+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.403900+(d*0.300000)))
jesstemp6 ='n.  oh '
jesstemp7 ='jessatom0 x. %s'%(2.413900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.413900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.393800+(d*0.300000)))
jesstemp10 ='n.  ne '
jesstemp11 ='r. arg'
jesstemp12 ='jessatom0 x. %s'%(3.989500+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(4.343000+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.837900+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(3.989500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.343000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.837900+(d*0.300000)))
jesstemp15 ='n.  nh1'
jesstemp16 ='n.  nh2'
jesstemp17 ='jessatom0 x. %s'%(4.242000+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(4.605600+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(5.615600+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(2.333100+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp11+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.242000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.605600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.615600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.333100+(d*0.300000)))
jesstemp22 ='n.  nh2'
jesstemp23 ='n.  nh1'
jesstemp24 ='jessatom0 x. %s'%(4.120800+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(3.797600+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(4.393500+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.323000+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp22+')|('+jesstemp23+'))&('+jesstemp11+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.120800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.797600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.393500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.312900+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(8.403200+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(8.352700+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(8.494100+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(4.565200+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(5.625700+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(5.019700+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.403200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.352700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.565200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.019700+(d*0.300000)))
jesstemp36 ='jessatom0 x. %s'%(9.635400+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(9.665700+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(9.857600+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(5.706500+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(6.544800+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(6.241800+(d*0.300000))
jesstemp42 ='jessatom6 x. %s'%(1.403900+(d*0.300000))
jesstemp43 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.665700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.857600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.706500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.544800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.403900+(d*0.300000)))
jesstemp44 ='jessatom0 x. %s'%(10.564600+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(10.645400+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(10.746400+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(6.635700+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(7.716400+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(7.413400+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(2.444200+(d*0.300000))
jesstemp51 ='br. jessatom6'
jesstemp52 ='jessatom7 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(10.564600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(10.645400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(10.746400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.716400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.413400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.393800+(d*0.300000)))
cmd.select('Jfa_1pno_1_6_1_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
