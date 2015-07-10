'''
FUNC:Jfa_1cnz-K195A-D227A-Y145B
PDB:1cnz
EC:1.1.1.85
PFAM:PF00180
RESI:lys,asp,tyr
LOCI:a-195,227;b-145;
'''
jesstemp0 ='n.  ce1'
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cz '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.393800+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.393800+(d*0.300000)))
jesstemp6 ='n.  oh '
jesstemp7 ='jessatom0 x. %s'%(2.413900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.393800+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.413900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.393800+(d*0.300000)))
jesstemp10 ='n.  cd '
jesstemp11 ='r. lys'
jesstemp12 ='jessatom0 x. %s'%(6.009500+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(5.171200+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(4.393500+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.009500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.171200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.393500+(d*0.300000)))
jesstemp15 ='n.  ce '
jesstemp16 ='jessatom0 x. %s'%(4.878300+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(4.262200+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(3.444100+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(1.545300+(d*0.300000))
jesstemp20 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp15+')&('+jesstemp11+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.878300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.262200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(3.444100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.545300+(d*0.300000)))
jesstemp21 ='n.  nz '
jesstemp22 ='jessatom0 x. %s'%(5.464100+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(4.959100+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(3.878400+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(2.535100+(d*0.300000))
jesstemp26 ='br. jessatom3'
jesstemp27 ='jessatom4 x. %s'%(1.504900+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp21+')&('+jesstemp11+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.464100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.959100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(3.878400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.535100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.504900+(d*0.300000)))
jesstemp28 ='n.  cg '
jesstemp29 ='r. asp'
jesstemp30 ='r. glu'
jesstemp31 ='jessatom0 x. %s'%(8.302200+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(7.585100+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(6.231700+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(4.868200+(d*0.300000))
jesstemp35 ='jessatom4 x. %s'%(4.736900+(d*0.300000))
jesstemp36 ='jessatom5 x. %s'%(3.514800+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp28+')&('+jesstemp29+'))|(('+jesstemp28+')&('+jesstemp30+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.302200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.585100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.231700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.868200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.736900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(3.514800+(d*0.300000)))
jesstemp37 ='n.  od1'
jesstemp38 ='n.  od2'
jesstemp39 ='n.  oe1'
jesstemp40 ='n.  oe2'
jesstemp41 ='jessatom0 x. %s'%(8.645600+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(7.908300+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(6.615500+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(4.353100+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(4.494500+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(3.444100+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.242300+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp37+')|('+jesstemp38+'))&('+jesstemp29+'))|((('+jesstemp39+')|('+jesstemp40+'))&('+jesstemp30+')))&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.645600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.908300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.615500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.353100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(4.494500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.444100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.242300+(d*0.300000)))
jesstemp49 ='n.  od2'
jesstemp50 ='n.  od1'
jesstemp51 ='n.  oe2'
jesstemp52 ='n.  oe1'
jesstemp53 ='jessatom0 x. %s'%(7.817400+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(7.272000+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(5.938800+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(5.181300+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(4.676300+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(3.252200+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(1.222100+(d*0.300000))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(2.151300+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp49+')|('+jesstemp50+'))&('+jesstemp29+'))|((('+jesstemp51+')|('+jesstemp52+'))&('+jesstemp30+')))&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(7.817400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.272000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.181300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.676300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.252200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.222100+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.151300+(d*0.300000)))
cmd.select('Jfa_1cnz-K195A-D227A-Y145B', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
