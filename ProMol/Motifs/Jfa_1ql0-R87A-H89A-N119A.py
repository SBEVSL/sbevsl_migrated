'''
FUNC:Jfa_1ql0-R87A-H89A-N119A
PDB:1ql0
EC:3.1.30.2
PFAM:PF01223
RESI:arg,his,asn
LOCI:a-87,89,119;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.353300+(d*0.300000))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.353300+(d*0.300000)))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='jessatom0 x. %s'%(2.312900+(d*0.300000))
jesstemp10 ='br. jessatom0'
jesstemp11 ='jessatom1 x. %s'%(2.292700+(d*0.300000))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.292700+(d*0.300000)))
jesstemp12 ='n.  cg '
jesstemp13 ='r. his'
jesstemp14 ='jessatom0 x. %s'%(10.766600+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(11.574600+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(12.988600+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.766600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(11.574600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(12.988600+(d*0.300000)))
jesstemp17 ='n.  nd1'
jesstemp18 ='jessatom0 x. %s'%(10.150500+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(10.746400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(12.291700+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(1.383700+(d*0.300000))
jesstemp22 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp17+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.150500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(10.746400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(12.291700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.383700+(d*0.300000)))
jesstemp23 ='n.  ne2'
jesstemp24 ='jessatom0 x. %s'%(9.999000+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(10.938300+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(12.180600+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(2.222000+(d*0.300000))
jesstemp28 ='br. jessatom3'
jesstemp29 ='jessatom4 x. %s'%(2.161400+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp23+')&('+jesstemp13+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.999000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.938300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(12.180600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.161400+(d*0.300000)))
jesstemp30 ='r. asn'
jesstemp31 ='r. gln'
jesstemp32 ='jessatom0 x. %s'%(11.110000+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(10.463600+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(12.604800+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(7.595200+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(6.817500+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(8.857700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp12+')&('+jesstemp30+'))|(('+jesstemp12+')&('+jesstemp31+')))&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.110000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.463600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(12.604800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.595200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.817500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.857700+(d*0.300000)))
jesstemp38 ='n.  od1'
jesstemp39 ='jessatom0 x. %s'%(11.402900+(d*0.300000))
jesstemp40 ='jessatom1 x. %s'%(10.978700+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(13.049200+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(6.625600+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(5.948900+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(8.059800+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.222100+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp38+')&('+jesstemp30+'))|(('+jesstemp38+')&('+jesstemp31+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(11.402900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(10.978700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(13.049200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.625600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.948900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.059800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.222100+(d*0.300000)))
jesstemp47 ='n.  nd2'
jesstemp48 ='jessatom0 x. %s'%(10.322200+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(9.534400+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(11.736200+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(7.665900+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(6.696300+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(8.615300+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(1.333200+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp47+')&('+jesstemp30+'))|(('+jesstemp47+')&('+jesstemp31+')))&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(10.322200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(9.534400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(11.736200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.665900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.615300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.181600+(d*0.300000)))
cmd.select('Jfa_1ql0-R87A-H89A-N119A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
