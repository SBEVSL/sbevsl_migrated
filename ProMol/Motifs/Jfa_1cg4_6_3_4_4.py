'''
FUNC:Jfa_1cg4_6_3_4_4
PDB:1cg4
EC:6.3.4.4
RESI:asp,his,gln
LOCI:a-13,41,224;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.251250+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom0 x. %s)'%(max(0.05,1.248751-(d*0.050000)))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='jessatom0 x. %s'%(1.231230+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom0 x. %s)'%(max(0.05,1.228771-(d*0.050000)))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.142140+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom1 x. %s)'%(max(0.05,2.137862-(d*0.050000)))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.231230+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,1.228771-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.142140+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.137862-(d*0.050000))))
jesstemp16 ='r. his'
jesstemp17 ='jessatom0 x. %s'%(8.638630+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom0 x. %s)'%(max(0.05,8.621379-(d*0.050000)))
jesstemp18 ='jessatom1 x. %s'%(7.617610+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom1 x. %s)'%(max(0.05,7.602398-(d*0.050000)))
jesstemp19 ='jessatom2 x. %s'%(9.649640+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom2 x. %s)'%(max(0.05,9.630370-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(8.638630+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,8.621379-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(7.617610+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,7.602398-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(9.649640+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,9.630370-(d*0.050000))))
jesstemp20 ='n.  nd1'
jesstemp21 ='jessatom0 x. %s'%(8.308300+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom0 x. %s)'%(max(0.05,8.291708-(d*0.050000)))
jesstemp22 ='jessatom1 x. %s'%(7.337330+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom1 x. %s)'%(max(0.05,7.322677-(d*0.050000)))
jesstemp23 ='jessatom2 x. %s'%(9.409400+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom2 x. %s)'%(max(0.05,9.390609-(d*0.050000)))
jesstemp24 ='jessatom3 x. %s'%(1.371370+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom3 x. %s)'%(max(0.05,1.368631-(d*0.050000)))
jesstemp25 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp20+')&('+jesstemp16+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.308300+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,8.291708-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.337330+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,7.322677-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(9.409400+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,9.390609-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.371370+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.368631-(d*0.050000))))
jesstemp26 ='n.  ne2'
jesstemp27 ='jessatom0 x. %s'%(8.788780+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom0 x. %s)'%(max(0.05,8.771229-(d*0.050000)))
jesstemp28 ='jessatom1 x. %s'%(7.657650+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom1 x. %s)'%(max(0.05,7.642358-(d*0.050000)))
jesstemp29 ='jessatom2 x. %s'%(9.779770+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom2 x. %s)'%(max(0.05,9.760240-(d*0.050000)))
jesstemp30 ='jessatom3 x. %s'%(2.182180+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom3 x. %s)'%(max(0.05,2.177822-(d*0.050000)))
jesstemp31 ='br. jessatom3'
jesstemp32 ='jessatom4 x. %s'%(2.142140+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom4 x. %s)'%(max(0.05,2.137862-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp26+')&('+jesstemp16+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.788780+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,8.771229-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.657650+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,7.642358-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.779770+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,9.760240-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.182180+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.177822-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.142140+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,2.137862-(d*0.050000))))
jesstemp33 ='n.  cd '
jesstemp34 ='r. gln'
jesstemp35 ='r. asn'
jesstemp36 ='jessatom0 x. %s'%(8.768760+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom0 x. %s)'%(max(0.05,8.751249-(d*0.050000)))
jesstemp37 ='jessatom1 x. %s'%(7.797790+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom1 x. %s)'%(max(0.05,7.782218-(d*0.050000)))
jesstemp38 ='jessatom2 x. %s'%(9.229220+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom2 x. %s)'%(max(0.05,9.210789-(d*0.050000)))
jesstemp39 ='jessatom3 x. %s'%(9.049040+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom3 x. %s)'%(max(0.05,9.030969-(d*0.050000)))
jesstemp40 ='jessatom4 x. %s'%(8.658650+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom4 x. %s)'%(max(0.05,8.641359-(d*0.050000)))
jesstemp41 ='jessatom5 x. %s'%(7.197190+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom5 x. %s)'%(max(0.05,7.182817-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp33+')&('+jesstemp34+'))|(('+jesstemp33+')&('+jesstemp35+')))&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(8.768760+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,8.751249-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(7.797790+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,7.782218-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.229220+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,9.210789-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.049040+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,9.030969-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.658650+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,8.641359-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.197190+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,7.182817-(d*0.050000))))
jesstemp42 ='jessatom0 x. %s'%(9.929920+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom0 x. %s)'%(max(0.05,9.910090-(d*0.050000)))
jesstemp43 ='jessatom1 x. %s'%(8.938930+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom1 x. %s)'%(max(0.05,8.921079-(d*0.050000)))
jesstemp44 ='jessatom2 x. %s'%(10.430420+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom2 x. %s)'%(max(0.05,10.409590-(d*0.050000)))
jesstemp45 ='jessatom3 x. %s'%(9.479470+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom3 x. %s)'%(max(0.05,9.460539-(d*0.050000)))
jesstemp46 ='jessatom4 x. %s'%(9.079070+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom4 x. %s)'%(max(0.05,9.060939-(d*0.050000)))
jesstemp47 ='jessatom5 x. %s'%(7.477470+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom5 x. %s)'%(max(0.05,7.462537-(d*0.050000)))
jesstemp48 ='jessatom6 x. %s'%(1.231230+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom6 x. %s)'%(max(0.05,1.228771-(d*0.050000)))
jesstemp49 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp5+')&('+jesstemp34+'))|(('+jesstemp5+')&('+jesstemp35+')))&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.929920+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,9.910090-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.938930+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,8.921079-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(10.430420+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,10.409590-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.479470+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,9.460539-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.079070+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,9.060939-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.477470+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,7.462537-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.231230+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.228771-(d*0.050000))))
jesstemp50 ='jessatom0 x. %s'%(8.158150+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom0 x. %s)'%(max(0.05,8.141858-(d*0.050000)))
jesstemp51 ='jessatom1 x. %s'%(7.097090+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom1 x. %s)'%(max(0.05,7.082917-(d*0.050000)))
jesstemp52 ='jessatom2 x. %s'%(8.608600+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom2 x. %s)'%(max(0.05,8.591409-(d*0.050000)))
jesstemp53 ='jessatom3 x. %s'%(8.178170+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom3 x. %s)'%(max(0.05,8.161838-(d*0.050000)))
jesstemp54 ='jessatom4 x. %s'%(7.947940+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom4 x. %s)'%(max(0.05,7.932068-(d*0.050000)))
jesstemp55 ='jessatom5 x. %s'%(6.426420+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom5 x. %s)'%(max(0.05,6.413586-(d*0.050000)))
jesstemp56 ='jessatom6 x. %s'%(1.341340+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom6 x. %s)'%(max(0.05,1.338661-(d*0.050000)))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.252250+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom7 x. %s)'%(max(0.05,2.247752-(d*0.050000)))
cmd.select('jessatom8', '(((('+jesstemp26+')&('+jesstemp34+'))|(('+jesstemp26+')&('+jesstemp35+')))&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(8.158150+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,8.141858-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.097090+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,7.082917-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(8.608600+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,8.591409-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.178170+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,8.161838-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.947940+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,7.932068-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(6.426420+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,6.413586-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.341340+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,1.338661-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.252250+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.247752-(d*0.050000))))
cmd.select('Jfa_1cg4_6_3_4_4', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
