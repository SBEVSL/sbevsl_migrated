'''
FUNC:Jab_1gxz_2_4_2_31
PDB:1gxz
EC:2.4.2.31
RESI:ser,glu,arg,glu
LOCI:a-147,159,184,189;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.531530+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp6 ='r. glu'
jesstemp7 ='r. asp'
jesstemp8 ='jessatom0 x. %s'%(12.992980+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom0 x. %s)'%(max(0.05,12.967033-(d*0.050000)))
jesstemp9 ='jessatom1 x. %s'%(11.841830+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,11.818182-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.992980+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,12.967033-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(11.841830+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,11.818182-(d*0.050000))))
jesstemp10 ='jessatom0 x. %s'%(12.442430+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom0 x. %s)'%(max(0.05,12.417582-(d*0.050000)))
jesstemp11 ='jessatom1 x. %s'%(11.241230+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,11.218781-(d*0.050000)))
jesstemp12 ='jessatom2 x. %s'%(1.531530+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom2 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp6+'))|(('+jesstemp3+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(12.442430+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,12.417582-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(11.241230+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,11.218781-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp14 ='r. arg'
jesstemp15 ='jessatom0 x. %s'%(12.272260+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom0 x. %s)'%(max(0.05,12.247752-(d*0.050000)))
jesstemp16 ='jessatom1 x. %s'%(11.141130+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom1 x. %s)'%(max(0.05,11.118881-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(12.492480+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,12.467532-(d*0.050000)))
jesstemp18 ='jessatom3 x. %s'%(11.000990+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom3 x. %s)'%(max(0.05,10.979021-(d*0.050000)))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(12.272260+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,12.247752-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(11.141130+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,11.118881-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(12.492480+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,12.467532-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(11.000990+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,10.979021-(d*0.050000))))
jesstemp19 ='jessatom0 x. %s'%(11.451440+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom0 x. %s)'%(max(0.05,11.428571-(d*0.050000)))
jesstemp20 ='jessatom1 x. %s'%(10.240230+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom1 x. %s)'%(max(0.05,10.219780-(d*0.050000)))
jesstemp21 ='jessatom2 x. %s'%(11.000990+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom2 x. %s)'%(max(0.05,10.979021-(d*0.050000)))
jesstemp22 ='jessatom3 x. %s'%(9.519510+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom3 x. %s)'%(max(0.05,9.500500-(d*0.050000)))
jesstemp23 ='jessatom4 x. %s'%(1.531530+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom4 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(11.451440+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,11.428571-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(10.240230+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,10.219780-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(11.000990+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,10.979021-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(9.519510+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,9.500500-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp25 ='jessatom0 x. %s'%(6.546540+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom0 x. %s)'%(max(0.05,6.533467-(d*0.050000)))
jesstemp26 ='jessatom1 x. %s'%(6.466460+(d*0.050000))
jesstemp26 = '('+jesstemp26+') and not (jessatom1 x. %s)'%(max(0.05,6.453546-(d*0.050000)))
jesstemp27 ='jessatom2 x. %s'%(13.733720+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom2 x. %s)'%(max(0.05,13.706294-(d*0.050000)))
jesstemp28 ='jessatom3 x. %s'%(12.632620+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom3 x. %s)'%(max(0.05,12.607393-(d*0.050000)))
jesstemp29 ='jessatom4 x. %s'%(8.528520+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom4 x. %s)'%(max(0.05,8.511489-(d*0.050000)))
jesstemp30 ='jessatom5 x. %s'%(8.278270+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom5 x. %s)'%(max(0.05,8.261738-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp25+')&('+jesstemp26+')&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.546540+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,6.533467-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.466460+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,6.453546-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(13.733720+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,13.706294-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(12.632620+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,12.607393-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(8.528520+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,8.511489-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(8.278270+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,8.261738-(d*0.050000))))
jesstemp31 ='jessatom0 x. %s'%(5.935930+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom0 x. %s)'%(max(0.05,5.924076-(d*0.050000)))
jesstemp32 ='jessatom1 x. %s'%(5.605600+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom1 x. %s)'%(max(0.05,5.594406-(d*0.050000)))
jesstemp33 ='jessatom2 x. %s'%(13.293280+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom2 x. %s)'%(max(0.05,13.266733-(d*0.050000)))
jesstemp34 ='jessatom3 x. %s'%(12.172160+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom3 x. %s)'%(max(0.05,12.147852-(d*0.050000)))
jesstemp35 ='jessatom4 x. %s'%(7.747740+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom4 x. %s)'%(max(0.05,7.732268-(d*0.050000)))
jesstemp36 ='jessatom5 x. %s'%(7.437430+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom5 x. %s)'%(max(0.05,7.422577-(d*0.050000)))
jesstemp37 ='jessatom6 x. %s'%(1.531530+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom6 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp38 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp6+'))|(('+jesstemp3+')&('+jesstemp7+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(5.935930+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,5.924076-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.605600+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,5.594406-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(13.293280+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,13.266733-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(12.172160+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,12.147852-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(7.747740+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,7.732268-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(7.437430+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,7.422577-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
cmd.select('Jab_1gxz_2_4_2_31', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
