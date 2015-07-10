'''
FUNC:Jfa_1cns-E67A-E89A-S120A
PDB:1cns
EC:3.2.1.14
PFAM:PF00182
RESI:glu,glu,ser
LOCI:a-67,89,120;
'''
jesstemp0 ='n.  cd '
jesstemp1 ='r. glu'
jesstemp2 ='r. asp'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  oe1'
jesstemp4 ='n.  oe2'
jesstemp5 ='n.  od1'
jesstemp6 ='n.  od2'
jesstemp7 ='jessatom0 x. %s'%(1.262500+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.262500+(d*0.300000)))
jesstemp9 ='n.  oe2'
jesstemp10 ='n.  oe1'
jesstemp11 ='n.  od2'
jesstemp12 ='n.  od1'
jesstemp13 ='jessatom0 x. %s'%(1.242300+(d*0.300000))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.242300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.181600+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(10.372700+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(9.160700+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(11.261500+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.372700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.160700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(11.261500+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(9.938400+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(8.756700+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(10.817100+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.938400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.756700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.817100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.252400+(d*0.300000)))
jesstemp24 ='jessatom0 x. %s'%(10.867600+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(9.625300+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(11.665500+(d*0.300000))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(2.191700+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp22+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.867600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.625300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.665500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.191700+(d*0.300000)))
jesstemp29 ='n.  ca '
jesstemp30 ='r. ser'
jesstemp31 ='r. thr'
jesstemp32 ='jessatom0 x. %s'%(10.231300+(d*0.300000))
jesstemp33 ='jessatom1 x. %s'%(9.514200+(d*0.300000))
jesstemp34 ='jessatom2 x. %s'%(10.857500+(d*0.300000))
jesstemp35 ='jessatom3 x. %s'%(7.484100+(d*0.300000))
jesstemp36 ='jessatom4 x. %s'%(6.241800+(d*0.300000))
jesstemp37 ='jessatom5 x. %s'%(8.150700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp29+')&('+jesstemp30+'))|(('+jesstemp29+')&('+jesstemp31+')))&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.231300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(9.514200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(10.857500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(7.484100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.150700+(d*0.300000)))
jesstemp38 ='n.  cb '
jesstemp39 ='jessatom0 x. %s'%(9.473800+(d*0.300000))
jesstemp40 ='jessatom1 x. %s'%(8.655700+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(10.049500+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(6.625600+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(5.413600+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(7.150800+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.535200+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp38+')&('+jesstemp30+'))|(('+jesstemp38+')&('+jesstemp31+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.473800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.655700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.049500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(6.625600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.150800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.535200+(d*0.300000)))
jesstemp47 ='n.  og '
jesstemp48 ='jessatom0 x. %s'%(9.241500+(d*0.300000))
jesstemp49 ='jessatom1 x. %s'%(8.312300+(d*0.300000))
jesstemp50 ='jessatom2 x. %s'%(9.938400+(d*0.300000))
jesstemp51 ='jessatom3 x. %s'%(5.231800+(d*0.300000))
jesstemp52 ='jessatom4 x. %s'%(3.999600+(d*0.300000))
jesstemp53 ='jessatom5 x. %s'%(5.827700+(d*0.300000))
jesstemp54 ='jessatom6 x. %s'%(2.434100+(d*0.300000))
jesstemp55 ='br. jessatom6'
jesstemp56 ='jessatom7 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom8', '(((('+jesstemp47+')&('+jesstemp30+'))|(('+jesstemp47+')&('+jesstemp31+')))&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(8.312300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.938400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.231800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(3.999600+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.434100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.424100+(d*0.300000)))
cmd.select('Jfa_1cns-E67A-E89A-S120A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
