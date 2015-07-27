'''
FUNC:Jfa_1diz-Y222A-D238A-W272A
PDB:1diz
EC:3.2.2.21
PFAM:PF06029,PF00730
RESI:tyr,asp,trp
LOCI:a-222,238,272;
'''
jesstemp0 ='n.  ce1'
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cz '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.414000+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.414000+(d*0.300000)))
jesstemp6 ='n.  oh '
jesstemp7 ='jessatom0 x. %s'%(2.434100+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.383700+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.434100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.383700+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. asp'
jesstemp12 ='r. glu'
jesstemp13 ='jessatom0 x. %s'%(7.746700+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(8.312300+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(8.888000+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(7.746700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.312300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(8.888000+(d*0.300000)))
jesstemp16 ='n.  od1'
jesstemp17 ='n.  od2'
jesstemp18 ='n.  oe1'
jesstemp19 ='n.  oe2'
jesstemp20 ='jessatom0 x. %s'%(6.918500+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(7.342700+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(7.938600+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.262500+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.342700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.262500+(d*0.300000)))
jesstemp25 ='n.  od2'
jesstemp26 ='n.  od1'
jesstemp27 ='n.  oe2'
jesstemp28 ='n.  oe1'
jesstemp29 ='jessatom0 x. %s'%(8.282000+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(8.847600+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(9.271800+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.211900+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.282000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.847600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.211900+(d*0.300000)))
jesstemp35 ='n.  ne1'
jesstemp36 ='r. trp'
jesstemp37 ='jessatom0 x. %s'%(7.837600+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(8.605200+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(8.807200+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(3.757200+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(4.383400+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(2.908800+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.837600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.605200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.807200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(3.757200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.383400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(2.908800+(d*0.300000)))
jesstemp43 ='n.  cz2'
jesstemp44 ='jessatom0 x. %s'%(5.373200+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(6.251900+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(6.635700+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(3.726900+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(3.737000+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(3.676400+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(2.535100+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp43+')&('+jesstemp36+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.373200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(6.251900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.635700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.726900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.737000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.676400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(2.535100+(d*0.300000)))
jesstemp52 ='n.  ch2'
jesstemp53 ='jessatom0 x. %s'%(4.242000+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(5.211600+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(5.575200+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(4.938900+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(4.716700+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(5.009600+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(3.737000+(d*0.300000))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(1.383700+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp52+')&('+jesstemp36+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.242000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.211600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.575200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.716700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(5.009600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(3.737000+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.383700+(d*0.300000)))
cmd.select('Jfa_1diz-Y222A-D238A-W272A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
