'''
FUNC:Jfa_1ahy
PDB:1ahy
EC:2.6.1.1
PFAM:PF00155
RESI:trp,asp,lys
LOCI:a-140,222,258;
'''
jesstemp0 ='n.  ne1'
jesstemp1 ='r. trp'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cz2'
jesstemp3 ='r. trp'
jesstemp4 ='jessatom0 x. %s'%(2.525000+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.525000+(d*0.300000)))
jesstemp6 ='n.  ch2'
jesstemp7 ='jessatom0 x. %s'%(3.726900+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(1.403900+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.726900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.403900+(d*0.300000)))
jesstemp10 ='n.  cg '
jesstemp11 ='r. asp'
jesstemp12 ='r. glu'
jesstemp13 ='jessatom0 x. %s'%(8.049700+(d*0.300000))
jesstemp14 ='jessatom1 x. %s'%(7.575000+(d*0.300000))
jesstemp15 ='jessatom2 x. %s'%(7.029600+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.049700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.575000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(7.029600+(d*0.300000)))
jesstemp16 ='n.  od1'
jesstemp17 ='n.  od2'
jesstemp18 ='n.  oe1'
jesstemp19 ='n.  oe2'
jesstemp20 ='jessatom0 x. %s'%(8.383000+(d*0.300000))
jesstemp21 ='jessatom1 x. %s'%(7.706300+(d*0.300000))
jesstemp22 ='jessatom2 x. %s'%(7.150800+(d*0.300000))
jesstemp23 ='jessatom3 x. %s'%(1.212000+(d*0.300000))
jesstemp24 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp16+')|('+jesstemp17+'))&('+jesstemp11+'))|((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp12+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.383000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.706300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(7.150800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.212000+(d*0.300000)))
jesstemp25 ='n.  od2'
jesstemp26 ='n.  od1'
jesstemp27 ='n.  oe2'
jesstemp28 ='n.  oe1'
jesstemp29 ='jessatom0 x. %s'%(6.878100+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(6.474100+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(5.979200+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(1.323100+(d*0.300000))
jesstemp33 ='br. jessatom3'
jesstemp34 ='jessatom4 x. %s'%(2.232100+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp25+')|('+jesstemp26+'))&('+jesstemp11+'))|((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp12+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.878100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.474100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.979200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.323100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.232100+(d*0.300000)))
jesstemp35 ='n.  cd '
jesstemp36 ='r. lys'
jesstemp37 ='jessatom0 x. %s'%(8.423400+(d*0.300000))
jesstemp38 ='jessatom1 x. %s'%(8.372900+(d*0.300000))
jesstemp39 ='jessatom2 x. %s'%(8.989000+(d*0.300000))
jesstemp40 ='jessatom3 x. %s'%(9.433400+(d*0.300000))
jesstemp41 ='jessatom4 x. %s'%(8.756700+(d*0.300000))
jesstemp42 ='jessatom5 x. %s'%(9.342500+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.423400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.372900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.989000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.433400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.756700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.342500+(d*0.300000)))
jesstemp43 ='n.  ce '
jesstemp44 ='jessatom0 x. %s'%(7.120500+(d*0.300000))
jesstemp45 ='jessatom1 x. %s'%(7.059900+(d*0.300000))
jesstemp46 ='jessatom2 x. %s'%(7.787100+(d*0.300000))
jesstemp47 ='jessatom3 x. %s'%(9.271800+(d*0.300000))
jesstemp48 ='jessatom4 x. %s'%(8.706200+(d*0.300000))
jesstemp49 ='jessatom5 x. %s'%(8.978900+(d*0.300000))
jesstemp50 ='jessatom6 x. %s'%(1.565500+(d*0.300000))
jesstemp51 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp43+')&('+jesstemp36+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(7.120500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.059900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(7.787100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(8.706200+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.565500+(d*0.300000)))
jesstemp52 ='n.  nz '
jesstemp53 ='jessatom0 x. %s'%(5.928700+(d*0.300000))
jesstemp54 ='jessatom1 x. %s'%(5.888300+(d*0.300000))
jesstemp55 ='jessatom2 x. %s'%(6.575100+(d*0.300000))
jesstemp56 ='jessatom3 x. %s'%(7.878000+(d*0.300000))
jesstemp57 ='jessatom4 x. %s'%(7.403300+(d*0.300000))
jesstemp58 ='jessatom5 x. %s'%(7.504300+(d*0.300000))
jesstemp59 ='jessatom6 x. %s'%(2.545200+(d*0.300000))
jesstemp60 ='br. jessatom6'
jesstemp61 ='jessatom7 x. %s'%(1.535200+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp52+')&('+jesstemp36+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.928700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.888300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(7.878000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.403300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.504300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.545200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jfa_1ahy', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
