'''
FUNC:Jfa_1mbb
PDB:1mbb
EC:1.1.1.158
PFAM:PF01565,PF02873
RESI:arg,ser,glu
LOCI:a-159,229,325;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.373500+(d*0.300000))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.373500+(d*0.300000)))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='jessatom0 x. %s'%(2.302800+(d*0.300000))
jesstemp10 ='br. jessatom0'
jesstemp11 ='jessatom1 x. %s'%(2.312900+(d*0.300000))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.302800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.312900+(d*0.300000)))
jesstemp12 ='n.  ca '
jesstemp13 ='r. ser'
jesstemp14 ='r. thr'
jesstemp15 ='jessatom0 x. %s'%(7.554800+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(9.281900+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(7.322500+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp12+')&('+jesstemp13+'))|(('+jesstemp12+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.554800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.281900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.322500+(d*0.300000)))
jesstemp18 ='n.  cb '
jesstemp19 ='jessatom0 x. %s'%(6.423600+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(7.989100+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(6.070100+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(1.535200+(d*0.300000))
jesstemp23 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp18+')&('+jesstemp13+'))|(('+jesstemp18+')&('+jesstemp14+')))&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.423600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.989100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.070100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.535200+(d*0.300000)))
jesstemp24 ='n.  og '
jesstemp25 ='jessatom0 x. %s'%(6.686200+(d*0.300000))
jesstemp26 ='jessatom1 x. %s'%(7.898200+(d*0.300000))
jesstemp27 ='jessatom2 x. %s'%(5.827700+(d*0.300000))
jesstemp28 ='jessatom3 x. %s'%(2.464400+(d*0.300000))
jesstemp29 ='br. jessatom3'
jesstemp30 ='jessatom4 x. %s'%(1.434200+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp24+')&('+jesstemp13+'))|(('+jesstemp24+')&('+jesstemp14+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.686200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.898200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.827700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.464400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.434200+(d*0.300000)))
jesstemp31 ='n.  cd '
jesstemp32 ='r. glu'
jesstemp33 ='r. asp'
jesstemp34 ='jessatom0 x. %s'%(3.615800+(d*0.300000))
jesstemp35 ='jessatom1 x. %s'%(5.928700+(d*0.300000))
jesstemp36 ='jessatom2 x. %s'%(4.989400+(d*0.300000))
jesstemp37 ='jessatom3 x. %s'%(5.171200+(d*0.300000))
jesstemp38 ='jessatom4 x. %s'%(4.534900+(d*0.300000))
jesstemp39 ='jessatom5 x. %s'%(5.514600+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp31+')&('+jesstemp32+'))|(('+jesstemp31+')&('+jesstemp33+')))&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(3.615800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.928700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.534900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.514600+(d*0.300000)))
jesstemp40 ='n.  oe1'
jesstemp41 ='n.  oe2'
jesstemp42 ='n.  od1'
jesstemp43 ='n.  od2'
jesstemp44 ='jessatom0 x. %s'%(3.434000+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(5.524700+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(4.413700+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(4.706600+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(3.767300+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(4.635900+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp40+')|('+jesstemp41+'))&('+jesstemp32+'))|((('+jesstemp42+')|('+jesstemp43+'))&('+jesstemp33+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(3.434000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.524700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.413700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.706600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.767300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.635900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp52 ='n.  oe2'
jesstemp53 ='n.  oe1'
jesstemp54 ='n.  od2'
jesstemp55 ='n.  od1'
jesstemp56 ='jessatom0 x. %s'%(3.726900+(d*0.300000))
jesstemp57 ='jessatom1 x. %s'%(6.060000+(d*0.300000))
jesstemp58 ='jessatom2 x. %s'%(4.949000+(d*0.300000))
jesstemp59 ='jessatom3 x. %s'%(5.241900+(d*0.300000))
jesstemp60 ='jessatom4 x. %s'%(4.787400+(d*0.300000))
jesstemp61 ='jessatom5 x. %s'%(5.676200+(d*0.300000))
jesstemp62 ='jessatom6 x. %s'%(1.252400+(d*0.300000))
jesstemp63 ='br. jessatom6'
jesstemp64 ='jessatom7 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp52+')|('+jesstemp53+'))&('+jesstemp32+'))|((('+jesstemp54+')|('+jesstemp55+'))&('+jesstemp33+')))&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(3.726900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(6.060000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.949000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.241900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.787400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.181600+(d*0.300000)))
cmd.select('Jfa_1mbb', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
