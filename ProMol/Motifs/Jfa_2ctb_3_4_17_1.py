'''
FUNC:Jfa_2ctb_3_4_17_1
PDB:2ctb
EC:3.4.17.1
RESI:arg,arg,glu
LOCI:a-71,127,270;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.332330+(d*0.050000))
jesstemp5 = '('+jesstemp5+') and not (jessatom0 x. %s)'%(max(0.05,2.327672-(d*0.050000)))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.332330+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,2.327672-(d*0.050000))))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='jessatom0 x. %s'%(2.272270+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom0 x. %s)'%(max(0.05,2.267732-(d*0.050000)))
jesstemp10 ='br. jessatom0'
jesstemp11 ='jessatom1 x. %s'%(2.342340+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,2.337662-(d*0.050000)))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.272270+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.267732-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.342340+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,2.337662-(d*0.050000))))
jesstemp12 ='jessatom0 x. %s'%(4.274270+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom0 x. %s)'%(max(0.05,4.265734-(d*0.050000)))
jesstemp13 ='jessatom1 x. %s'%(4.884880+(d*0.050000))
jesstemp13 = '('+jesstemp13+') and not (jessatom1 x. %s)'%(max(0.05,4.875125-(d*0.050000)))
jesstemp14 ='jessatom2 x. %s'%(3.583580+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom2 x. %s)'%(max(0.05,3.576424-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp4+')&('+jesstemp12+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.274270+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,4.265734-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(4.884880+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,4.875125-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(3.583580+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,3.576424-(d*0.050000))))
jesstemp15 ='jessatom0 x. %s'%(6.546540+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom0 x. %s)'%(max(0.05,6.533467-(d*0.050000)))
jesstemp16 ='jessatom1 x. %s'%(7.017010+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom1 x. %s)'%(max(0.05,7.002997-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(5.615610+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,5.604396-(d*0.050000)))
jesstemp18 ='jessatom3 x. %s'%(2.282280+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom3 x. %s)'%(max(0.05,2.277722-(d*0.050000)))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.546540+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,6.533467-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.017010+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,7.002997-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(5.615610+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,5.604396-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(2.282280+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,2.277722-(d*0.050000))))
jesstemp20 ='jessatom0 x. %s'%(5.635630+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom0 x. %s)'%(max(0.05,5.624376-(d*0.050000)))
jesstemp21 ='jessatom1 x. %s'%(6.726720+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom1 x. %s)'%(max(0.05,6.713287-(d*0.050000)))
jesstemp22 ='jessatom2 x. %s'%(4.874870+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom2 x. %s)'%(max(0.05,4.865135-(d*0.050000)))
jesstemp23 ='jessatom3 x. %s'%(2.312310+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom3 x. %s)'%(max(0.05,2.307692-(d*0.050000)))
jesstemp24 ='br. jessatom3'
jesstemp25 ='jessatom4 x. %s'%(2.292290+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom4 x. %s)'%(max(0.05,2.287712-(d*0.050000)))
cmd.select('jessatom5', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(5.635630+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,5.624376-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.726720+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,6.713287-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.874870+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,4.865135-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.312310+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.307692-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.292290+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,2.287712-(d*0.050000))))
jesstemp26 ='n.  cd '
jesstemp27 ='r. glu'
jesstemp28 ='r. asp'
jesstemp29 ='jessatom0 x. %s'%(9.929920+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom0 x. %s)'%(max(0.05,9.910090-(d*0.050000)))
jesstemp30 ='jessatom1 x. %s'%(11.911900+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom1 x. %s)'%(max(0.05,11.888112-(d*0.050000)))
jesstemp31 ='jessatom2 x. %s'%(9.969960+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom2 x. %s)'%(max(0.05,9.950050-(d*0.050000)))
jesstemp32 ='jessatom3 x. %s'%(9.709700+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom3 x. %s)'%(max(0.05,9.690310-(d*0.050000)))
jesstemp33 ='jessatom4 x. %s'%(10.140130+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom4 x. %s)'%(max(0.05,10.119880-(d*0.050000)))
jesstemp34 ='jessatom5 x. %s'%(7.917910+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom5 x. %s)'%(max(0.05,7.902098-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp26+')&('+jesstemp27+'))|(('+jesstemp26+')&('+jesstemp28+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.929920+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,9.910090-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(11.911900+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,11.888112-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(9.969960+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,9.950050-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(9.709700+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,9.690310-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.140130+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,10.119880-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(7.917910+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,7.902098-(d*0.050000))))
jesstemp35 ='n.  oe1'
jesstemp36 ='n.  oe2'
jesstemp37 ='n.  od1'
jesstemp38 ='n.  od2'
jesstemp39 ='jessatom0 x. %s'%(9.179170+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom0 x. %s)'%(max(0.05,9.160839-(d*0.050000)))
jesstemp40 ='jessatom1 x. %s'%(11.221210+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom1 x. %s)'%(max(0.05,11.198801-(d*0.050000)))
jesstemp41 ='jessatom2 x. %s'%(9.409400+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom2 x. %s)'%(max(0.05,9.390609-(d*0.050000)))
jesstemp42 ='jessatom3 x. %s'%(9.479470+(d*0.050000))
jesstemp42 = '('+jesstemp42+') and not (jessatom3 x. %s)'%(max(0.05,9.460539-(d*0.050000)))
jesstemp43 ='jessatom4 x. %s'%(10.180170+(d*0.050000))
jesstemp43 = '('+jesstemp43+') and not (jessatom4 x. %s)'%(max(0.05,10.159840-(d*0.050000)))
jesstemp44 ='jessatom5 x. %s'%(7.917910+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom5 x. %s)'%(max(0.05,7.902098-(d*0.050000)))
jesstemp45 ='jessatom6 x. %s'%(1.251250+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom6 x. %s)'%(max(0.05,1.248751-(d*0.050000)))
jesstemp46 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp35+')|('+jesstemp36+'))&('+jesstemp27+'))|((('+jesstemp37+')|('+jesstemp38+'))&('+jesstemp28+')))&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.179170+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,9.160839-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(11.221210+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,11.198801-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(9.409400+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,9.390609-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(9.479470+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,9.460539-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(10.180170+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,10.159840-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.917910+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,7.902098-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
jesstemp47 ='n.  oe2'
jesstemp48 ='n.  oe1'
jesstemp49 ='n.  od2'
jesstemp50 ='n.  od1'
jesstemp51 ='jessatom0 x. %s'%(9.719710+(d*0.050000))
jesstemp51 = '('+jesstemp51+') and not (jessatom0 x. %s)'%(max(0.05,9.700300-(d*0.050000)))
jesstemp52 ='jessatom1 x. %s'%(11.661650+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom1 x. %s)'%(max(0.05,11.638362-(d*0.050000)))
jesstemp53 ='jessatom2 x. %s'%(9.659650+(d*0.050000))
jesstemp53 = '('+jesstemp53+') and not (jessatom2 x. %s)'%(max(0.05,9.640360-(d*0.050000)))
jesstemp54 ='jessatom3 x. %s'%(8.998990+(d*0.050000))
jesstemp54 = '('+jesstemp54+') and not (jessatom3 x. %s)'%(max(0.05,8.981019-(d*0.050000)))
jesstemp55 ='jessatom4 x. %s'%(9.209200+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom4 x. %s)'%(max(0.05,9.190809-(d*0.050000)))
jesstemp56 ='jessatom5 x. %s'%(7.057050+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom5 x. %s)'%(max(0.05,7.042957-(d*0.050000)))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.232230+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom7 x. %s)'%(max(0.05,2.227772-(d*0.050000)))
cmd.select('jessatom8', '((((('+jesstemp47+')|('+jesstemp48+'))&('+jesstemp27+'))|((('+jesstemp49+')|('+jesstemp50+'))&('+jesstemp28+')))&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp45+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.719710+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,9.700300-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(11.661650+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,11.638362-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(9.659650+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,9.640360-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(8.998990+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,8.981019-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(9.209200+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,9.190809-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(7.057050+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,7.042957-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.232230+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.227772-(d*0.050000))))
cmd.select('Jfa_2ctb_3_4_17_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
