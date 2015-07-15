'''
FUNC:Jfa_1n7n-N349A-H399A-Y408A
PDB:1n7n
EC:4.2.2.1
PFAM:PF02278,PF08124,PF02884
RESI:asn,his,tyr
LOCI:a-349,399,408;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.383700+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.383700+(d*0.300000)))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.222000+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.171500+(d*0.300000)))
jesstemp10 ='n.  ce1'
jesstemp11 ='r. tyr'
jesstemp12 ='jessatom0 x. %s'%(5.686300+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(5.363100+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.050100+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.050100+(d*0.300000)))
jesstemp15 ='n.  cz '
jesstemp16 ='jessatom0 x. %s'%(4.979300+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(4.383400+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(3.474400+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.383700+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.979300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.383400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.474400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.383700+(d*0.300000)))
jesstemp21 ='n.  oh '
jesstemp22 ='jessatom0 x. %s'%(5.019700+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(4.201600+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(3.272400+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.403800+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.383700+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.201600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.272400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.403800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.383700+(d*0.300000)))
jesstemp28 ='n.  ne '
jesstemp29 ='r. arg'
jesstemp30 ='jessatom0 x. %s'%(7.787100+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.413500+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(7.039700+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(7.453800+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(6.201400+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(5.241900+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.787100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.413500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(7.039700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.453800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.241900+(d*0.300000)))
jesstemp36 ='n.  nh1'
jesstemp37 ='n.  nh2'
jesstemp38 ='jessatom0 x. %s'%(5.726700+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(4.403600+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(4.827800+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(5.302500+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(3.989500+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(3.070400+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(2.343200+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp36+')|('+jesstemp37+'))&('+jesstemp29+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.403600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.827800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.302500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.989500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.070400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.343200+(d*0.300000)))
jesstemp46 ='n.  nh2'
jesstemp47 ='n.  nh1'
jesstemp48 ='jessatom0 x. %s'%(7.595200+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(6.363000+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(6.241800+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(6.039800+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(5.019700+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(3.858200+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(2.323000+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.292700+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp46+')|('+jesstemp47+'))&('+jesstemp29+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.595200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.363000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.039800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.019700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.858200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.323000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.292700+(d*0.300000)))
cmd.select('Jfa_1n7n-N349A-H399A-Y408A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
