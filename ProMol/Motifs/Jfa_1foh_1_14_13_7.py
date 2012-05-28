'''
FUNC:Jfa_1foh_1_14_13_7
PDB:1foh
EC:1.14.13.7
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
jesstemp13 ='jessatom0 x. %s'%(1.261260+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom0 x. %s)'%(max(0.05,1.258741-(d*0.050000)))
jesstemp14 ='br. jessatom0'
jesstemp15 ='jessatom1 x. %s'%(2.182180+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom1 x. %s)'%(max(0.05,2.177822-(d*0.050000)))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.261260+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,1.258741-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.182180+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.177822-(d*0.050000))))
jesstemp16 ='n.  ne '
jesstemp17 ='r. arg'
jesstemp18 ='jessatom0 x. %s'%(4.524520+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom0 x. %s)'%(max(0.05,4.515485-(d*0.050000)))
jesstemp19 ='jessatom1 x. %s'%(5.675670+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom1 x. %s)'%(max(0.05,5.664336-(d*0.050000)))
jesstemp20 ='jessatom2 x. %s'%(4.024020+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom2 x. %s)'%(max(0.05,4.015984-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.524520+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,4.515485-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(5.675670+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,5.664336-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.024020+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,4.015984-(d*0.050000))))
jesstemp21 ='n.  nh1'
jesstemp22 ='n.  nh2'
jesstemp23 ='jessatom0 x. %s'%(3.743740+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom0 x. %s)'%(max(0.05,3.736264-(d*0.050000)))
jesstemp24 ='jessatom1 x. %s'%(4.954950+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom1 x. %s)'%(max(0.05,4.945055-(d*0.050000)))
jesstemp25 ='jessatom2 x. %s'%(2.912910+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom2 x. %s)'%(max(0.05,2.907093-(d*0.050000)))
jesstemp26 ='jessatom3 x. %s'%(2.272270+(d*0.050000))
jesstemp26 = '('+jesstemp26+') and not (jessatom3 x. %s)'%(max(0.05,2.267732-(d*0.050000)))
jesstemp27 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp21+')|('+jesstemp22+'))&('+jesstemp17+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(3.743740+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,3.736264-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(4.954950+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,4.945055-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(2.912910+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,2.907093-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.272270+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,2.267732-(d*0.050000))))
jesstemp28 ='n.  nh2'
jesstemp29 ='n.  nh1'
jesstemp30 ='jessatom0 x. %s'%(5.535530+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom0 x. %s)'%(max(0.05,5.524476-(d*0.050000)))
jesstemp31 ='jessatom1 x. %s'%(6.786780+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom1 x. %s)'%(max(0.05,6.773227-(d*0.050000)))
jesstemp32 ='jessatom2 x. %s'%(5.015010+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom2 x. %s)'%(max(0.05,5.004995-(d*0.050000)))
jesstemp33 ='jessatom3 x. %s'%(2.332330+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom3 x. %s)'%(max(0.05,2.327672-(d*0.050000)))
jesstemp34 ='br. jessatom3'
jesstemp35 ='jessatom4 x. %s'%(2.332330+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom4 x. %s)'%(max(0.05,2.327672-(d*0.050000)))
cmd.select('jessatom5', '((('+jesstemp28+')|('+jesstemp29+'))&('+jesstemp17+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.535530+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,5.524476-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.786780+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,6.773227-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.015010+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,5.004995-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.332330+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.327672-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.332330+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,2.327672-(d*0.050000))))
jesstemp36 ='n.  ce1'
jesstemp37 ='r. tyr'
jesstemp38 ='jessatom0 x. %s'%(5.805800+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom0 x. %s)'%(max(0.05,5.794206-(d*0.050000)))
jesstemp39 ='jessatom1 x. %s'%(5.315310+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom1 x. %s)'%(max(0.05,5.304695-(d*0.050000)))
jesstemp40 ='jessatom2 x. %s'%(5.365360+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom2 x. %s)'%(max(0.05,5.354645-(d*0.050000)))
jesstemp41 ='jessatom3 x. %s'%(9.069060+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom3 x. %s)'%(max(0.05,9.050949-(d*0.050000)))
jesstemp42 ='jessatom4 x. %s'%(7.517510+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom4 x. %s)'%(max(0.05,7.502498-(d*0.050000)))
jesstemp43 ='jessatom5 x. %s'%(9.819810+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom5 x. %s)'%(max(0.05,9.800200-(d*0.050000)))
cmd.select('jessatom6', '(('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(5.805800+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,5.794206-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.315310+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,5.304695-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.365360+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,5.354645-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.069060+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,9.050949-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(7.517510+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,7.502498-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(9.819810+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,9.800200-(d*0.050000))))
jesstemp44 ='n.  cz '
jesstemp45 ='jessatom0 x. %s'%(5.695690+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom0 x. %s)'%(max(0.05,5.684316-(d*0.050000)))
jesstemp46 ='jessatom1 x. %s'%(5.155150+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom1 x. %s)'%(max(0.05,5.144855-(d*0.050000)))
jesstemp47 ='jessatom2 x. %s'%(5.465460+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom2 x. %s)'%(max(0.05,5.454545-(d*0.050000)))
jesstemp48 ='jessatom3 x. %s'%(9.339330+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom3 x. %s)'%(max(0.05,9.320679-(d*0.050000)))
jesstemp49 ='jessatom4 x. %s'%(7.667660+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom4 x. %s)'%(max(0.05,7.652348-(d*0.050000)))
jesstemp50 ='jessatom5 x. %s'%(9.889880+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom5 x. %s)'%(max(0.05,9.870130-(d*0.050000)))
jesstemp51 ='jessatom6 x. %s'%(1.371370+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom6 x. %s)'%(max(0.05,1.368631-(d*0.050000)))
jesstemp52 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp44+')&('+jesstemp37+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.695690+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,5.684316-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.155150+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,5.144855-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.465460+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,5.454545-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.339330+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,9.320679-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.667660+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,7.652348-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(9.889880+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,9.870130-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.371370+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.368631-(d*0.050000))))
jesstemp53 ='n.  oh '
jesstemp54 ='jessatom0 x. %s'%(4.664660+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom0 x. %s)'%(max(0.05,4.655345-(d*0.050000)))
jesstemp55 ='jessatom1 x. %s'%(4.044040+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom1 x. %s)'%(max(0.05,4.035964-(d*0.050000)))
jesstemp56 ='jessatom2 x. %s'%(4.674670+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom2 x. %s)'%(max(0.05,4.665335-(d*0.050000)))
jesstemp57 ='jessatom3 x. %s'%(8.658650+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom3 x. %s)'%(max(0.05,8.641359-(d*0.050000)))
jesstemp58 ='jessatom4 x. %s'%(7.067060+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom4 x. %s)'%(max(0.05,7.052947-(d*0.050000)))
jesstemp59 ='jessatom5 x. %s'%(9.219210+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom5 x. %s)'%(max(0.05,9.200799-(d*0.050000)))
jesstemp60 ='jessatom6 x. %s'%(2.392390+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom6 x. %s)'%(max(0.05,2.387612-(d*0.050000)))
jesstemp61 ='br. jessatom6'
jesstemp62 ='jessatom7 x. %s'%(1.381380+(d*0.050000))
jesstemp62 = '('+jesstemp62+') and not (jessatom7 x. %s)'%(max(0.05,1.378621-(d*0.050000)))
cmd.select('jessatom8', '(('+jesstemp53+')&('+jesstemp37+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(4.664660+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,4.655345-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.044040+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,4.035964-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(4.674670+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,4.665335-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.658650+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,8.641359-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(7.067060+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,7.052947-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(9.219210+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,9.200799-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.392390+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,2.387612-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.381380+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,1.378621-(d*0.050000))))
cmd.select('Jfa_1foh_1_14_13_7', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
