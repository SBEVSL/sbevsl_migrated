'''
FUNC:Jfa_1mqf_1_11_1_6
PDB:1mqf
EC:1.11.1.6
RESI:his,ser,asn
LOCI:a-54,93,127;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nd1'
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.381380+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.378621-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.381380+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.378621-(d*0.050000))))
jesstemp6 ='n.  ne2'
jesstemp7 ='jessatom0 x. %s'%(2.202200+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,2.197802-(d*0.050000)))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.142140+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,2.137862-(d*0.050000)))
cmd.select('jessatom2', '(('+jesstemp6+')&('+jesstemp3+')&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.202200+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.197802-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.142140+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.137862-(d*0.050000))))
jesstemp10 ='n.  ca '
jesstemp11 ='r. ser'
jesstemp12 ='r. thr'
jesstemp13 ='jessatom0 x. %s'%(5.605600+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom0 x. %s)'%(max(0.05,5.594406-(d*0.050000)))
jesstemp14 ='jessatom1 x. %s'%(4.864860+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom1 x. %s)'%(max(0.05,4.855145-(d*0.050000)))
jesstemp15 ='jessatom2 x. %s'%(6.976970+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom2 x. %s)'%(max(0.05,6.963037-(d*0.050000)))
cmd.select('jessatom3', '(((('+jesstemp10+')&('+jesstemp11+'))|(('+jesstemp10+')&('+jesstemp12+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(5.605600+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,5.594406-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.864860+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,4.855145-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(6.976970+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,6.963037-(d*0.050000))))
jesstemp16 ='n.  cb '
jesstemp17 ='jessatom0 x. %s'%(4.444440+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom0 x. %s)'%(max(0.05,4.435564-(d*0.050000)))
jesstemp18 ='jessatom1 x. %s'%(3.973970+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom1 x. %s)'%(max(0.05,3.966034-(d*0.050000)))
jesstemp19 ='jessatom2 x. %s'%(6.106100+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom2 x. %s)'%(max(0.05,6.093906-(d*0.050000)))
jesstemp20 ='jessatom3 x. %s'%(1.541540+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom3 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp21 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp16+')&('+jesstemp11+'))|(('+jesstemp16+')&('+jesstemp12+')))&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.444440+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,4.435564-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.973970+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,3.966034-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.106100+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,6.093906-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp22 ='n.  og '
jesstemp23 ='jessatom0 x. %s'%(3.503500+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom0 x. %s)'%(max(0.05,3.496503-(d*0.050000)))
jesstemp24 ='jessatom1 x. %s'%(2.822820+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom1 x. %s)'%(max(0.05,2.817183-(d*0.050000)))
jesstemp25 ='jessatom2 x. %s'%(4.944940+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom2 x. %s)'%(max(0.05,4.935065-(d*0.050000)))
jesstemp26 ='jessatom3 x. %s'%(2.442440+(d*0.050000))
jesstemp26 = '('+jesstemp26+') and not (jessatom3 x. %s)'%(max(0.05,2.437562-(d*0.050000)))
jesstemp27 ='br. jessatom3'
jesstemp28 ='jessatom4 x. %s'%(1.421420+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom4 x. %s)'%(max(0.05,1.418581-(d*0.050000)))
cmd.select('jessatom5', '(((('+jesstemp22+')&('+jesstemp11+'))|(('+jesstemp22+')&('+jesstemp12+')))&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(3.503500+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,3.496503-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(2.822820+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,2.817183-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.944940+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,4.935065-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.442440+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.437562-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.421420+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.418581-(d*0.050000))))
jesstemp29 ='r. asn'
jesstemp30 ='r. gln'
jesstemp31 ='jessatom0 x. %s'%(6.616610+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom0 x. %s)'%(max(0.05,6.603397-(d*0.050000)))
jesstemp32 ='jessatom1 x. %s'%(5.625620+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom1 x. %s)'%(max(0.05,5.614386-(d*0.050000)))
jesstemp33 ='jessatom2 x. %s'%(4.874870+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom2 x. %s)'%(max(0.05,4.865135-(d*0.050000)))
jesstemp34 ='jessatom3 x. %s'%(8.778770+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom3 x. %s)'%(max(0.05,8.761239-(d*0.050000)))
jesstemp35 ='jessatom4 x. %s'%(8.618610+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom4 x. %s)'%(max(0.05,8.601399-(d*0.050000)))
jesstemp36 ='jessatom5 x. %s'%(7.337330+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom5 x. %s)'%(max(0.05,7.322677-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp29+'))|(('+jesstemp0+')&('+jesstemp30+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.616610+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,6.603397-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.625620+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,5.614386-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(4.874870+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,4.865135-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(8.778770+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,8.761239-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.618610+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,8.601399-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.337330+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,7.322677-(d*0.050000))))
jesstemp37 ='n.  od1'
jesstemp38 ='jessatom1 x. %s'%(4.544540+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom1 x. %s)'%(max(0.05,4.535465-(d*0.050000)))
jesstemp39 ='jessatom2 x. %s'%(4.094090+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom2 x. %s)'%(max(0.05,4.085914-(d*0.050000)))
jesstemp40 ='jessatom3 x. %s'%(7.677670+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom3 x. %s)'%(max(0.05,7.662338-(d*0.050000)))
jesstemp41 ='jessatom4 x. %s'%(7.447440+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom4 x. %s)'%(max(0.05,7.432567-(d*0.050000)))
jesstemp42 ='jessatom5 x. %s'%(6.136130+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom5 x. %s)'%(max(0.05,6.123876-(d*0.050000)))
jesstemp43 ='jessatom6 x. %s'%(1.231230+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom6 x. %s)'%(max(0.05,1.228771-(d*0.050000)))
jesstemp44 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp37+')&('+jesstemp29+'))|(('+jesstemp37+')&('+jesstemp30+')))&('+jesstemp13+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.605600+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,5.594406-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(4.544540+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,4.535465-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(4.094090+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,4.085914-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(7.677670+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,7.662338-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.447440+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,7.432567-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(6.136130+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,6.123876-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.231230+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.228771-(d*0.050000))))
jesstemp45 ='n.  nd2'
jesstemp46 ='jessatom0 x. %s'%(6.786780+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom0 x. %s)'%(max(0.05,6.773227-(d*0.050000)))
jesstemp47 ='jessatom1 x. %s'%(5.995990+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom1 x. %s)'%(max(0.05,5.984016-(d*0.050000)))
jesstemp48 ='jessatom2 x. %s'%(4.784780+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom2 x. %s)'%(max(0.05,4.775225-(d*0.050000)))
jesstemp49 ='jessatom3 x. %s'%(9.619610+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom3 x. %s)'%(max(0.05,9.600400-(d*0.050000)))
jesstemp50 ='jessatom4 x. %s'%(9.359350+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom4 x. %s)'%(max(0.05,9.340659-(d*0.050000)))
jesstemp51 ='jessatom5 x. %s'%(8.078070+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom5 x. %s)'%(max(0.05,8.061938-(d*0.050000)))
jesstemp52 ='jessatom6 x. %s'%(1.331330+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom6 x. %s)'%(max(0.05,1.328671-(d*0.050000)))
jesstemp53 ='br. jessatom6'
jesstemp54 ='jessatom7 x. %s'%(2.242240+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom7 x. %s)'%(max(0.05,2.237762-(d*0.050000)))
cmd.select('jessatom8', '(((('+jesstemp45+')&('+jesstemp29+'))|(('+jesstemp45+')&('+jesstemp30+')))&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.786780+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,6.773227-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.995990+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,5.984016-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.784780+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,4.775225-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.619610+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,9.600400-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.359350+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,9.340659-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(8.078070+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,8.061938-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.331330+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,1.328671-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.242240+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.237762-(d*0.050000))))
cmd.select('Jfa_1mqf_1_11_1_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
