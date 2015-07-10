'''
FUNC:Jfa_1foh-D54A-R281A-Y289A
PDB:1foh
EC:1.14.13.7
PFAM:PF01946,PF07976,PF01494
RESI:asp,arg,tyr
LOCI:a-54,281,289;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.272600+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.201800+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.272600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.201800+(d*0.300000)))
jesstemp16 ='n.  ne '
jesstemp17 ='r. arg'
jesstemp18 ='jessatom0 x. %s'%(4.565200+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(5.726700+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(4.060200+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.565200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.726700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.060200+(d*0.300000)))
jesstemp21 ='n.  nh1'
jesstemp22 ='n.  nh2'
jesstemp23 ='jessatom0 x. %s'%(3.777400+(d*0.300000))
jesstemp24 ='jessatom1 x. %s'%(4.999500+(d*0.300000))
jesstemp25 ='jessatom2 x. %s'%(2.939100+(d*0.300000))
jesstemp26 ='jessatom3 x. %s'%(2.292700+(d*0.300000))
jesstemp27 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp21+')|('+jesstemp22+'))&('+jesstemp17+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.777400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.939100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.292700+(d*0.300000)))
jesstemp28 ='n.  nh2'
jesstemp29 ='n.  nh1'
jesstemp30 ='jessatom0 x. %s'%(5.585300+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(6.847800+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(5.060100+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(2.353300+(d*0.300000))
jesstemp34 ='br. jessatom3'
jesstemp35 ='jessatom4 x. %s'%(2.353300+(d*0.300000))
cmd.select('jessatom5', '((('+jesstemp28+')|('+jesstemp29+'))&('+jesstemp17+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.585300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.847800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.060100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.353300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.353300+(d*0.300000)))
jesstemp36 ='n.  ce1'
jesstemp37 ='r. tyr'
jesstemp38 ='jessatom0 x. %s'%(5.858000+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(5.363100+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(5.413600+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(9.150600+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(7.585100+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(9.908100+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.858000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.363100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.150600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.585100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.908100+(d*0.300000)))
jesstemp44 ='n.  cz '
jesstemp45 ='jessatom0 x. %s'%(5.746900+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(5.201500+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(5.514600+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(9.423300+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(7.736600+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(9.978800+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(1.383700+(d*0.300000))
jesstemp52 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp44+')&('+jesstemp37+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.746900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.201500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.514600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.423300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.736600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.978800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.383700+(d*0.300000)))
jesstemp53 ='n.  oh '
jesstemp54 ='jessatom0 x. %s'%(4.706600+(d*0.300000))
jesstemp55 ='jessatom1 x. %s'%(4.080400+(d*0.300000))
jesstemp56 ='jessatom2 x. %s'%(4.716700+(d*0.300000))
jesstemp57 ='jessatom3 x. %s'%(8.736500+(d*0.300000))
jesstemp58 ='jessatom4 x. %s'%(7.130600+(d*0.300000))
jesstemp59 ='jessatom5 x. %s'%(9.302100+(d*0.300000))
jesstemp60 ='jessatom6 x. %s'%(2.413900+(d*0.300000))
jesstemp61 ='br. jessatom6'
jesstemp62 ='jessatom7 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp53+')&('+jesstemp37+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.706600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.080400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.716700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.736500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.130600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.302100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.413900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.393800+(d*0.300000)))
cmd.select('Jfa_1foh-D54A-R281A-Y289A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
