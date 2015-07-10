'''
FUNC:Jfa_1brl-H4A-H45A-F261A
PDB:1brl
EC:1.14.14.3
PFAM:PF00296
RESI:his,his,phe
LOCI:a-4,45,261;
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
jesstemp7 ='jessatom0 x. %s'%(2.191700+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.191700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.191700+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(6.039800+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(5.999400+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(6.908400+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.039800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.999400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.908400+(d*0.300000)))
jesstemp13 ='jessatom0 x. %s'%(6.878100+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(7.059900+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(7.857800+(d*0.300000))
jesstemp16 ='jessatom3 x. %s'%(1.414000+(d*0.300000))
jesstemp17 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.878100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.059900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.414000+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(7.080100+(d*0.300000))
jesstemp19 ='jessatom2 x. %s'%(8.403200+(d*0.300000))
jesstemp20 ='jessatom3 x. %s'%(2.222000+(d*0.300000))
jesstemp21 ='br. jessatom3'
jesstemp22 ='jessatom4 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp18+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.080100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.059900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(8.403200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.201800+(d*0.300000)))
jesstemp23 ='n.  ce1'
jesstemp24 ='n.  ce2'
jesstemp25 ='r. phe'
jesstemp26 ='jessatom0 x. %s'%(14.180400+(d*0.300000))
jesstemp27 ='jessatom1 x. %s'%(12.958300+(d*0.300000))
jesstemp28 ='jessatom2 x. %s'%(12.746200+(d*0.300000))
jesstemp29 ='jessatom3 x. %s'%(15.008600+(d*0.300000))
jesstemp30 ='jessatom4 x. %s'%(16.331700+(d*0.300000))
jesstemp31 ='jessatom5 x. %s'%(16.351900+(d*0.300000))
cmd.select('jessatom6', '((('+jesstemp23+')|('+jesstemp24+'))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(14.180400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(12.958300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(12.746200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(15.008600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(16.331700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(16.351900+(d*0.300000)))
jesstemp32 ='n.  ce2'
jesstemp33 ='n.  ce1'
jesstemp34 ='jessatom0 x. %s'%(16.149900+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(14.937900+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(14.655100+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(17.372000+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(18.705200+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(18.715300+(d*0.300000))
jesstemp40 ='jessatom6 x. %s'%(2.454300+(d*0.300000))
jesstemp41 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp32+')|('+jesstemp33+'))&('+jesstemp25+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(16.149900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(14.937900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(14.655100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(17.372000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(18.705200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(18.715300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.454300+(d*0.300000)))
jesstemp42 ='n.  cz '
jesstemp43 ='jessatom0 x. %s'%(14.958100+(d*0.300000))
jesstemp44 ='jessatom1 x. %s'%(13.705700+(d*0.300000))
jesstemp45 ='jessatom2 x. %s'%(13.534000+(d*0.300000))
jesstemp46 ='jessatom3 x. %s'%(16.099400+(d*0.300000))
jesstemp47 ='jessatom4 x. %s'%(17.442700+(d*0.300000))
jesstemp48 ='jessatom5 x. %s'%(17.382100+(d*0.300000))
jesstemp49 ='jessatom6 x. %s'%(1.414000+(d*0.300000))
jesstemp50 ='br. jessatom6'
jesstemp51 ='jessatom7 x. %s'%(1.414000+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp42+')&('+jesstemp25+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(14.958100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(13.705700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(13.534000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(16.099400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(17.442700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(17.382100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.414000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.414000+(d*0.300000)))
cmd.select('Jfa_1brl-H4A-H45A-F261A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
