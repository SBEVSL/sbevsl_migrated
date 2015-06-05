'''
FUNC:Jfa_1uou
PDB:1uou
EC:2.4.2.4
PFAM:PF07831,PF00591,PF02885
RESI:his,arg,lys
LOCI:a-116,202,221;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.393800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.393800+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.211900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.211900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.161400+(d*0.300000)))
jesstemp10 ='n.  ne '
jesstemp11 ='r. arg'
jesstemp12 ='jessatom0 x. %s'%(13.231000+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(13.150200+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(11.493800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(13.231000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(13.150200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(11.493800+(d*0.300000)))
jesstemp15 ='n.  nh1'
jesstemp16 ='n.  nh2'
jesstemp17 ='jessatom0 x. %s'%(11.503900+(d*0.300000))
jesstemp18 ='jessatom1 x. %s'%(11.615000+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(9.867700+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(2.312900+(d*0.300000))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp15+')|('+jesstemp16+'))&('+jesstemp11+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(11.503900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.615000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.867700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.312900+(d*0.300000)))
jesstemp22 ='n.  nh2'
jesstemp23 ='n.  nh1'
jesstemp24 ='jessatom0 x. %s'%(11.079700+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(10.918100+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(9.342500+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.343200+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.323000+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp22+')|('+jesstemp23+'))&('+jesstemp11+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.079700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.918100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.342500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.343200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.323000+(d*0.300000)))
jesstemp30 ='n.  cd '
jesstemp31 ='r. lys'
jesstemp32 ='jessatom0 x. %s'%(6.130700+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(4.908600+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(5.231800+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(11.453400+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(10.716100+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(9.120300+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.130700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.908600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.453400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.716100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.120300+(d*0.300000)))
jesstemp38 ='n.  ce '
jesstemp39 ='jessatom0 x. %s'%(6.666000+(d*0.300000))
jesstemp40 ='jessatom1 x. %s'%(5.595400+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(5.312600+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(10.120200+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(9.504100+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(7.817400+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.515000+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp38+')&('+jesstemp31+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.666000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.595400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.312600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.120200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.504100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.515000+(d*0.300000)))
jesstemp47 ='n.  nz '
jesstemp48 ='jessatom0 x. %s'%(6.605400+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(5.746900+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(5.241900+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(9.019300+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(8.312300+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(6.686200+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(2.454300+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(1.474600+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp47+')&('+jesstemp31+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.605400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.746900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.241900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.019300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.312300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.686200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.454300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.474600+(d*0.300000)))
cmd.select('Jfa_1uou', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
