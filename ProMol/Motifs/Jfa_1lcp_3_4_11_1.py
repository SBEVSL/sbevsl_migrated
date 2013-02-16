'''
FUNC:Jfa_1lcp_3_4_11_1
PDB:1lcp
EC:3.4.11.1
RESI:asp,lys,arg
LOCI:a-255,262,336;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.272600+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.272600+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.222000+(d*0.300000)))
jesstemp16 ='n.  cd '
jesstemp17 ='r. lys'
jesstemp18 ='jessatom0 x. %s'%(4.858100+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(5.070200+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(4.878300+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.858100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.070200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.878300+(d*0.300000)))
jesstemp21 ='n.  ce '
jesstemp22 ='jessatom0 x. %s'%(3.666300+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(4.080400+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(3.444100+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp21+')&('+jesstemp17+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.666300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.080400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.444100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp27 ='n.  nz '
jesstemp28 ='jessatom0 x. %s'%(4.373300+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(4.807600+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(3.757200+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(2.535100+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(1.504900+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp27+')&('+jesstemp17+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.373300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.807600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.535100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.504900+(d*0.300000)))
jesstemp34 ='n.  ne '
jesstemp35 ='r. arg'
jesstemp36 ='jessatom0 x. %s'%(11.140300+(d*0.300000))
jesstemp37 ='jessatom1 x. %s'%(11.241300+(d*0.300000))
jesstemp38 ='jessatom2 x. %s'%(10.201000+(d*0.300000))
jesstemp39 ='jessatom3 x. %s'%(13.564300+(d*0.300000))
jesstemp40 ='jessatom4 x. %s'%(12.231100+(d*0.300000))
jesstemp41 ='jessatom5 x. %s'%(11.211000+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(11.140300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.241300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.201000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(13.564300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(12.231100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(11.211000+(d*0.300000)))
jesstemp42 ='n.  nh1'
jesstemp43 ='n.  nh2'
jesstemp44 ='jessatom0 x. %s'%(12.948200+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(13.059300+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(11.948300+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(14.786400+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(13.554200+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(12.372500+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(2.343200+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '((('+jesstemp42+')|('+jesstemp43+'))&('+jesstemp35+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(12.948200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(13.059300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(11.948300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(14.786400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(13.554200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(12.372500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.343200+(d*0.300000)))
jesstemp52 ='n.  nh2'
jesstemp53 ='n.  nh1'
jesstemp54 ='jessatom0 x. %s'%(11.049400+(d*0.300000))
jesstemp55 ='jessatom1 x. %s'%(11.271600+(d*0.300000))
jesstemp56 ='jessatom2 x. %s'%(9.968700+(d*0.300000))
jesstemp57 ='jessatom3 x. %s'%(12.726000+(d*0.300000))
jesstemp58 ='jessatom4 x. %s'%(11.463500+(d*0.300000))
jesstemp59 ='jessatom5 x. %s'%(10.251500+(d*0.300000))
jesstemp60 ='jessatom6 x. %s'%(2.312900+(d*0.300000))
jesstemp61 ='br. jessatom6'
jesstemp62 ='jessatom7 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom8', '((('+jesstemp52+')|('+jesstemp53+'))&('+jesstemp35+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(11.049400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(11.271600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.968700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(12.726000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(10.251500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.312900+(d*0.300000)))
cmd.select('Jfa_1lcp_3_4_11_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
