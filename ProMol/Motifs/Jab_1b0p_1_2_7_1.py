'''
FUNC:Jab_1b0p_1_2_7_1
PDB:1b0p
EC:1.2.7.1
RESI:thr,glu,arg,asn
LOCI:a-31,64,114,996;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. thr'
jesstemp2 ='r. ser'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.561560+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.558442-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.561560+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.558442-(d*0.050000))))
jesstemp6 ='r. glu'
jesstemp7 ='r. asp'
jesstemp8 ='jessatom0 x. %s'%(12.652640+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom0 x. %s)'%(max(0.05,12.627373-(d*0.050000)))
jesstemp9 ='jessatom1 x. %s'%(13.763750+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,13.736264-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(12.652640+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,12.627373-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(13.763750+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,13.736264-(d*0.050000))))
jesstemp10 ='jessatom0 x. %s'%(11.501490+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom0 x. %s)'%(max(0.05,11.478521-(d*0.050000)))
jesstemp11 ='jessatom1 x. %s'%(12.642630+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,12.617383-(d*0.050000)))
jesstemp12 ='jessatom2 x. %s'%(1.531530+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom2 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp6+'))|(('+jesstemp3+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(11.501490+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,11.478521-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(12.642630+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,12.617383-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp14 ='r. arg'
jesstemp15 ='jessatom0 x. %s'%(8.358350+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom0 x. %s)'%(max(0.05,8.341658-(d*0.050000)))
jesstemp16 ='jessatom1 x. %s'%(8.818810+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom1 x. %s)'%(max(0.05,8.801199-(d*0.050000)))
jesstemp17 ='jessatom2 x. %s'%(14.914900+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom2 x. %s)'%(max(0.05,14.885115-(d*0.050000)))
jesstemp18 ='jessatom3 x. %s'%(13.393380+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom3 x. %s)'%(max(0.05,13.366633-(d*0.050000)))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.358350+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,8.341658-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(8.818810+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,8.801199-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(14.914900+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,14.885115-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(13.393380+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,13.366633-(d*0.050000))))
jesstemp19 ='jessatom0 x. %s'%(6.886880+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom0 x. %s)'%(max(0.05,6.873127-(d*0.050000)))
jesstemp20 ='jessatom1 x. %s'%(7.387380+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom1 x. %s)'%(max(0.05,7.372627-(d*0.050000)))
jesstemp21 ='jessatom2 x. %s'%(13.893880+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom2 x. %s)'%(max(0.05,13.866134-(d*0.050000)))
jesstemp22 ='jessatom3 x. %s'%(12.392380+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom3 x. %s)'%(max(0.05,12.367632-(d*0.050000)))
jesstemp23 ='jessatom4 x. %s'%(1.531530+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom4 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(6.886880+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,6.873127-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.387380+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,7.372627-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(13.893880+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,13.866134-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(12.392380+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,12.367632-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp25 ='r. asn'
jesstemp26 ='r. gln'
jesstemp27 ='jessatom0 x. %s'%(9.679670+(d*0.050000))
jesstemp27 = '('+jesstemp27+') and not (jessatom0 x. %s)'%(max(0.05,9.660340-(d*0.050000)))
jesstemp28 ='jessatom1 x. %s'%(8.688680+(d*0.050000))
jesstemp28 = '('+jesstemp28+') and not (jessatom1 x. %s)'%(max(0.05,8.671329-(d*0.050000)))
jesstemp29 ='jessatom2 x. %s'%(17.137120+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom2 x. %s)'%(max(0.05,17.102897-(d*0.050000)))
jesstemp30 ='jessatom3 x. %s'%(16.666650+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom3 x. %s)'%(max(0.05,16.633367-(d*0.050000)))
jesstemp31 ='jessatom4 x. %s'%(17.047030+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom4 x. %s)'%(max(0.05,17.012987-(d*0.050000)))
jesstemp32 ='jessatom5 x. %s'%(15.625610+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom5 x. %s)'%(max(0.05,15.594406-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp25+'))|(('+jesstemp0+')&('+jesstemp26+')))&('+jesstemp27+')&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(9.679670+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,9.660340-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(8.688680+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,8.671329-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(17.137120+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,17.102897-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(16.666650+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,16.633367-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(17.047030+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,17.012987-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(15.625610+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,15.594406-(d*0.050000))))
jesstemp33 ='jessatom0 x. %s'%(9.619610+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom0 x. %s)'%(max(0.05,9.600400-(d*0.050000)))
jesstemp34 ='jessatom1 x. %s'%(8.538530+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom1 x. %s)'%(max(0.05,8.521479-(d*0.050000)))
jesstemp35 ='jessatom2 x. %s'%(16.966950+(d*0.050000))
jesstemp35 = '('+jesstemp35+') and not (jessatom2 x. %s)'%(max(0.05,16.933067-(d*0.050000)))
jesstemp36 ='jessatom3 x. %s'%(16.456440+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom3 x. %s)'%(max(0.05,16.423576-(d*0.050000)))
jesstemp37 ='jessatom4 x. %s'%(16.486470+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom4 x. %s)'%(max(0.05,16.453546-(d*0.050000)))
jesstemp38 ='jessatom5 x. %s'%(15.095080+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom5 x. %s)'%(max(0.05,15.064935-(d*0.050000)))
jesstemp39 ='jessatom6 x. %s'%(1.541540+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom6 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp40 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp3+')&('+jesstemp25+'))|(('+jesstemp3+')&('+jesstemp26+')))&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.619610+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,9.600400-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(8.538530+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,8.521479-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(16.966950+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,16.933067-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(16.456440+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,16.423576-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(16.486470+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,16.453546-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(15.095080+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,15.064935-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
cmd.select('Jab_1b0p_1_2_7_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
