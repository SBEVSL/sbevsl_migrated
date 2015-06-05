'''
FUNC:Jab_2npx
PDB:2npx
EC:1.11.1.1
PFAM:PF07992,PF00070,PF02852,PF13738
RESI:his,ser,arg
LOCI:a-10,41,303;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.504900+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.504900+(d*0.300000)))
jesstemp6 ='n.  n  '
jesstemp7 ='jessatom0 x. %s'%(9.140500+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(8.706200+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+'))|(('+jesstemp6+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(9.140500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(8.706200+(d*0.300000)))
jesstemp9 ='n.  ca '
jesstemp10 ='jessatom0 x. %s'%(10.231300+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(9.675800+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.454400+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp9+'))|(('+jesstemp9+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.231300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.675800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.454400+(d*0.300000)))
jesstemp14 ='r. cys'
jesstemp15 ='jessatom0 x. %s'%(10.625200+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(9.645500+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(4.272300+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(3.898600+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.625200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.645500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.272300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(3.898600+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(9.756600+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(8.696100+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(4.928800+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(4.938900+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.756600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.696100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
jesstemp25 ='r. arg'
jesstemp26 ='jessatom0 x. %s'%(5.544900+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(5.221700+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(13.675400+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(14.604600+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(13.725900+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(12.463400+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp0+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.221700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(13.675400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(14.604600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(13.725900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(12.463400+(d*0.300000)))
jesstemp32 ='jessatom0 x. %s'%(5.676200+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(5.171200+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(13.099700+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(14.049100+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(12.877500+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(11.534200+(d*0.300000))
jesstemp38 ='jessatom6 x. %s'%(1.595800+(d*0.300000))
jesstemp39 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp2+')&('+jesstemp25+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(13.099700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(14.049100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(12.877500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(11.534200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.595800+(d*0.300000)))
cmd.select('Jab_2npx', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
