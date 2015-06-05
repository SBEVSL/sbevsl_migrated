'''
FUNC:Jfa_1que
PDB:1que
EC:1.18.1.2
PFAM:PF00175,PF00970
RESI:ser,cys,glu
LOCI:a-80,261,301;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.535200+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.535200+(d*0.300000)))
jesstemp6 ='n.  og '
jesstemp7 ='jessatom0 x. %s'%(2.444200+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.424100+(d*0.300000)))
jesstemp10 ='r. cys'
jesstemp11 ='jessatom0 x. %s'%(9.625300+(d*0.300000))
jesstemp12 ='jessatom1 x. %s'%(8.231500+(d*0.300000))
jesstemp13 ='jessatom2 x. %s'%(7.251800+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.625300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(8.231500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.251800+(d*0.300000)))
jesstemp14 ='jessatom0 x. %s'%(8.413300+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(6.979100+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(6.120600+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp18 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp3+')&('+jesstemp10+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.413300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.979100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.120600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp19 ='n.  sg '
jesstemp20 ='jessatom0 x. %s'%(6.797300+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(5.413600+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(4.423800+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(2.828000+(d*0.300000))
jesstemp24 ='br. jessatom3'
jesstemp25 ='jessatom4 x. %s'%(1.828100+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp19+')&('+jesstemp10+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.797300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(5.413600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.423800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.828000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.828100+(d*0.300000)))
jesstemp26 ='n.  cd '
jesstemp27 ='r. glu'
jesstemp28 ='r. asp'
jesstemp29 ='jessatom0 x. %s'%(5.767100+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(5.221700+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(4.110700+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(6.464000+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(5.757000+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(4.514700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp26+')&('+jesstemp27+'))|(('+jesstemp26+')&('+jesstemp28+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.767100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.221700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.110700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.464000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(5.757000+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.514700+(d*0.300000)))
jesstemp35 ='n.  oe1'
jesstemp36 ='n.  oe2'
jesstemp37 ='n.  od1'
jesstemp38 ='n.  od2'
jesstemp39 ='jessatom0 x. %s'%(5.979200+(d*0.300000))
jesstemp40 ='jessatom1 x. %s'%(5.625700+(d*0.300000))
jesstemp41 ='jessatom2 x. %s'%(4.747000+(d*0.300000))
jesstemp42 ='jessatom3 x. %s'%(7.423500+(d*0.300000))
jesstemp43 ='jessatom4 x. %s'%(6.645800+(d*0.300000))
jesstemp44 ='jessatom5 x. %s'%(5.544900+(d*0.300000))
jesstemp45 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp35+')|('+jesstemp36+'))&('+jesstemp27+'))|((('+jesstemp37+')|('+jesstemp38+'))&('+jesstemp28+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.625700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.747000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.423500+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(6.645800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(5.544900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.262500+(d*0.300000)))
jesstemp47 ='n.  oe2'
jesstemp48 ='n.  oe1'
jesstemp49 ='n.  od2'
jesstemp50 ='n.  od1'
jesstemp51 ='jessatom0 x. %s'%(4.736900+(d*0.300000))
jesstemp52 ='jessatom1 x. %s'%(4.060200+(d*0.300000))
jesstemp53 ='jessatom2 x. %s'%(2.878500+(d*0.300000))
jesstemp54 ='jessatom3 x. %s'%(6.251900+(d*0.300000))
jesstemp55 ='jessatom4 x. %s'%(5.393400+(d*0.300000))
jesstemp56 ='jessatom5 x. %s'%(3.898600+(d*0.300000))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.222000+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp47+')|('+jesstemp48+'))&('+jesstemp27+'))|((('+jesstemp49+')|('+jesstemp50+'))&('+jesstemp28+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp45+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.736900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.060200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(2.878500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(6.251900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(5.393400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.898600+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('Jfa_1que', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
