'''
FUNC:Jfa_1a9t-H86A-E89A-N243A
PDB:1a9t
EC:2.4.2.1
PFAM:PF01048
RESI:his,glu,asn
LOCI:a-86,89,243;
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
jesstemp10 ='n.  cd '
jesstemp11 ='r. glu'
jesstemp12 ='r. asp'
jesstemp13 ='jessatom0 x. %s'%(4.726800+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(3.959200+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(6.080200+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.726800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.959200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.080200+(d*0.300000)))
jesstemp16 ='n.  oe1'
jesstemp17 ='n.  oe2'
jesstemp18 ='n.  od1'
jesstemp19 ='n.  od2'
jesstemp20 ='jessatom0 x. %s'%(5.837800+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(4.918700+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(6.979100+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(5.837800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.918700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.979100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp25 ='n.  oe2'
jesstemp26 ='n.  oe1'
jesstemp27 ='n.  od2'
jesstemp28 ='n.  od1'
jesstemp29 ='jessatom0 x. %s'%(3.737000+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(2.918900+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(5.060100+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp23+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.737000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(2.918900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.060100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.191700+(d*0.300000)))
jesstemp34 ='r. asn'
jesstemp35 ='r. gln'
jesstemp36 ='jessatom0 x. %s'%(15.685300+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(16.069100+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(14.372300+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(19.089000+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(19.917200+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(18.584000+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp34+'))|(('+jesstemp0+')&('+jesstemp35+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(15.685300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(16.069100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(14.372300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(19.089000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(19.917200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(18.584000+(d*0.300000)))
jesstemp42 ='jessatom0 x. %s'%(14.634900+(d*0.300000))
jesstemp43 ='jessatom1 x. %s'%(15.008600+(d*0.300000))
jesstemp44 ='jessatom2 x. %s'%(13.251200+(d*0.300000))
jesstemp45 ='jessatom3 x. %s'%(18.119400+(d*0.300000))
jesstemp46 ='jessatom4 x. %s'%(18.947600+(d*0.300000))
jesstemp47 ='jessatom5 x. %s'%(17.563900+(d*0.300000))
jesstemp48 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp49 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp18+')&('+jesstemp34+'))|(('+jesstemp18+')&('+jesstemp35+')))&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(14.634900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(15.008600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(13.251200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(18.119400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(18.947600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(17.563900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp50 ='n.  nd2'
jesstemp51 ='jessatom0 x. %s'%(15.887300+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(16.351900+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(14.735900+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(19.291000+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(20.159600+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(18.816300+(d*0.300000))
jesstemp57 ='jessatom6 x. %s'%(1.343300+(d*0.300000))
jesstemp58 ='br. jessatom6'
jesstemp59 ='jessatom7 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp50+')&('+jesstemp34+'))|(('+jesstemp50+')&('+jesstemp35+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(15.887300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(16.351900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(14.735900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(19.291000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(20.159600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(18.816300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.343300+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.262400+(d*0.300000)))
cmd.select('Jfa_1a9t-H86A-E89A-N243A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
