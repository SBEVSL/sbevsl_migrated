'''
FUNC:Jab_1dcp-H62A-H63A-H80A-D89A
PDB:1dcp
EC:4.2.1.96
PFAM:PF01329
RESI:his,his,his,asp
LOCI:a-62,63,80,89;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.565500+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.565500+(d*0.300000)))
jesstemp6 ='jessatom0 x. %s'%(3.767300+(d*0.300000))
jesstemp7 ='jessatom1 x. %s'%(4.848000+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(3.767300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(4.848000+(d*0.300000)))
jesstemp8 ='jessatom0 x. %s'%(4.716700+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(6.029700+(d*0.300000))
jesstemp10 ='jessatom2 x. %s'%(1.565500+(d*0.300000))
jesstemp11 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.716700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.029700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.565500+(d*0.300000)))
jesstemp12 ='jessatom0 x. %s'%(9.241500+(d*0.300000))
jesstemp13 ='jessatom1 x. %s'%(9.322300+(d*0.300000))
jesstemp14 ='jessatom2 x. %s'%(9.675800+(d*0.300000))
jesstemp15 ='jessatom3 x. %s'%(10.029300+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp3+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(9.241500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.322300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.675800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(10.029300+(d*0.300000)))
jesstemp16 ='jessatom0 x. %s'%(9.069800+(d*0.300000))
jesstemp17 ='jessatom1 x. %s'%(9.413200+(d*0.300000))
jesstemp18 ='jessatom2 x. %s'%(9.150600+(d*0.300000))
jesstemp19 ='jessatom3 x. %s'%(9.271800+(d*0.300000))
jesstemp20 ='jessatom4 x. %s'%(1.565500+(d*0.300000))
jesstemp21 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(9.069800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.413200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.150600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(9.271800+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.565500+(d*0.300000)))
jesstemp22 ='r. asp'
jesstemp23 ='r. glu'
jesstemp24 ='jessatom0 x. %s'%(7.938600+(d*0.300000))
jesstemp25 ='jessatom1 x. %s'%(6.696300+(d*0.300000))
jesstemp26 ='jessatom2 x. %s'%(8.978900+(d*0.300000))
jesstemp27 ='jessatom3 x. %s'%(10.514100+(d*0.300000))
jesstemp28 ='jessatom4 x. %s'%(10.574700+(d*0.300000))
jesstemp29 ='jessatom5 x. %s'%(11.382700+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp22+'))|(('+jesstemp0+')&('+jesstemp23+')))&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(7.938600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(10.514100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.574700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(11.382700+(d*0.300000)))
jesstemp30 ='jessatom0 x. %s'%(8.736500+(d*0.300000))
jesstemp31 ='jessatom1 x. %s'%(7.595200+(d*0.300000))
jesstemp32 ='jessatom2 x. %s'%(9.504100+(d*0.300000))
jesstemp33 ='jessatom3 x. %s'%(10.978700+(d*0.300000))
jesstemp34 ='jessatom4 x. %s'%(9.887900+(d*0.300000))
jesstemp35 ='jessatom5 x. %s'%(10.807000+(d*0.300000))
jesstemp36 ='jessatom6 x. %s'%(1.555400+(d*0.300000))
jesstemp37 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp2+')&('+jesstemp22+'))|(('+jesstemp2+')&('+jesstemp23+')))&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(8.736500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(7.595200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.504100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.978700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.887900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(10.807000+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.555400+(d*0.300000)))
cmd.select('Jab_1dcp-H62A-H63A-H80A-D89A', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
