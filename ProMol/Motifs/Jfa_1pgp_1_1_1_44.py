'''
FUNC:Jfa_1pgp_1_1_1_44
PDB:1pgp
EC:1.1.1.44
RESI:gly,lys,asn,glu
LOCI:a-130,183,187,190;
'''
jesstemp0 ='n.  n  '
cmd.select('jessatom0', '(('+jesstemp0+'))')
jesstemp1 ='n.  ca '
jesstemp2 ='jessatom0 x. %s'%(1.461460+(d*0.050000))
jesstemp2 = '('+jesstemp2+') and not (jessatom0 x. %s)'%(max(0.05,1.458541-(d*0.050000)))
jesstemp3 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp1+')&('+jesstemp2+')&('+jesstemp3+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.461460+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.458541-(d*0.050000))))
jesstemp4 ='n.  c  '
jesstemp5 ='jessatom0 x. %s'%(2.472470+(d*0.050000))
jesstemp5 = '('+jesstemp5+') and not (jessatom0 x. %s)'%(max(0.05,2.467532-(d*0.050000)))
jesstemp6 ='br. jessatom0'
jesstemp7 ='jessatom1 x. %s'%(1.511510+(d*0.050000))
jesstemp7 = '('+jesstemp7+') and not (jessatom1 x. %s)'%(max(0.05,1.508492-(d*0.050000)))
cmd.select('jessatom2', '(('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+')&('+jesstemp7+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.472470+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,2.467532-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(1.511510+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,1.508492-(d*0.050000))))
jesstemp8 ='n.  cd '
jesstemp9 ='r. lys'
jesstemp10 ='jessatom0 x. %s'%(9.179170+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom0 x. %s)'%(max(0.05,9.160839-(d*0.050000)))
jesstemp11 ='jessatom1 x. %s'%(10.230220+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,10.209790-(d*0.050000)))
jesstemp12 ='jessatom2 x. %s'%(11.321310+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom2 x. %s)'%(max(0.05,11.298701-(d*0.050000)))
cmd.select('jessatom3', '(('+jesstemp8+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.179170+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,9.160839-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.230220+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,10.209790-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(11.321310+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,11.298701-(d*0.050000))))
jesstemp13 ='n.  ce '
jesstemp14 ='jessatom0 x. %s'%(8.238230+(d*0.050000))
jesstemp14 = '('+jesstemp14+') and not (jessatom0 x. %s)'%(max(0.05,8.221778-(d*0.050000)))
jesstemp15 ='jessatom1 x. %s'%(9.219210+(d*0.050000))
jesstemp15 = '('+jesstemp15+') and not (jessatom1 x. %s)'%(max(0.05,9.200799-(d*0.050000)))
jesstemp16 ='jessatom2 x. %s'%(10.420410+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom2 x. %s)'%(max(0.05,10.399600-(d*0.050000)))
jesstemp17 ='jessatom3 x. %s'%(1.501500+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom3 x. %s)'%(max(0.05,1.498501-(d*0.050000)))
jesstemp18 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp13+')&('+jesstemp9+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.238230+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,8.221778-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.219210+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,9.200799-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(10.420410+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,10.399600-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.501500+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,1.498501-(d*0.050000))))
jesstemp19 ='n.  nz '
jesstemp20 ='jessatom0 x. %s'%(7.717710+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom0 x. %s)'%(max(0.05,7.702298-(d*0.050000)))
jesstemp21 ='jessatom1 x. %s'%(8.538530+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom1 x. %s)'%(max(0.05,8.521479-(d*0.050000)))
jesstemp22 ='jessatom2 x. %s'%(9.709700+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom2 x. %s)'%(max(0.05,9.690310-(d*0.050000)))
jesstemp23 ='jessatom3 x. %s'%(2.482480+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom3 x. %s)'%(max(0.05,2.477522-(d*0.050000)))
jesstemp24 ='br. jessatom3'
jesstemp25 ='jessatom4 x. %s'%(1.491490+(d*0.050000))
jesstemp25 = '('+jesstemp25+') and not (jessatom4 x. %s)'%(max(0.05,1.488511-(d*0.050000)))
cmd.select('jessatom5', '(('+jesstemp19+')&('+jesstemp9+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.717710+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,7.702298-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.538530+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,8.521479-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.709700+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,9.690310-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.482480+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,2.477522-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.491490+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.488511-(d*0.050000))))
jesstemp26 ='n.  cg '
jesstemp27 ='r. asn'
jesstemp28 ='r. gln'
jesstemp29 ='jessatom0 x. %s'%(10.060050+(d*0.050000))
jesstemp29 = '('+jesstemp29+') and not (jessatom0 x. %s)'%(max(0.05,10.039960-(d*0.050000)))
jesstemp30 ='jessatom1 x. %s'%(10.740730+(d*0.050000))
jesstemp30 = '('+jesstemp30+') and not (jessatom1 x. %s)'%(max(0.05,10.719281-(d*0.050000)))
jesstemp31 ='jessatom2 x. %s'%(12.182170+(d*0.050000))
jesstemp31 = '('+jesstemp31+') and not (jessatom2 x. %s)'%(max(0.05,12.157842-(d*0.050000)))
jesstemp32 ='jessatom3 x. %s'%(5.225220+(d*0.050000))
jesstemp32 = '('+jesstemp32+') and not (jessatom3 x. %s)'%(max(0.05,5.214785-(d*0.050000)))
jesstemp33 ='jessatom4 x. %s'%(4.114110+(d*0.050000))
jesstemp33 = '('+jesstemp33+') and not (jessatom4 x. %s)'%(max(0.05,4.105894-(d*0.050000)))
jesstemp34 ='jessatom5 x. %s'%(4.434430+(d*0.050000))
jesstemp34 = '('+jesstemp34+') and not (jessatom5 x. %s)'%(max(0.05,4.425574-(d*0.050000)))
cmd.select('jessatom6', '(((('+jesstemp26+')&('+jesstemp27+'))|(('+jesstemp26+')&('+jesstemp28+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(10.060050+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom6 x. %s)'%(max(0.05,10.039960-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(10.740730+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom6 x. %s)'%(max(0.05,10.719281-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(12.182170+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom6 x. %s)'%(max(0.05,12.157842-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(5.225220+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom6 x. %s)'%(max(0.05,5.214785-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(4.114110+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom6 x. %s)'%(max(0.05,4.105894-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.434430+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom6 x. %s)'%(max(0.05,4.425574-(d*0.050000))))
jesstemp35 ='n.  od1'
jesstemp36 ='jessatom1 x. %s'%(9.969960+(d*0.050000))
jesstemp36 = '('+jesstemp36+') and not (jessatom1 x. %s)'%(max(0.05,9.950050-(d*0.050000)))
jesstemp37 ='jessatom2 x. %s'%(11.401390+(d*0.050000))
jesstemp37 = '('+jesstemp37+') and not (jessatom2 x. %s)'%(max(0.05,11.378621-(d*0.050000)))
jesstemp38 ='jessatom3 x. %s'%(4.474470+(d*0.050000))
jesstemp38 = '('+jesstemp38+') and not (jessatom3 x. %s)'%(max(0.05,4.465534-(d*0.050000)))
jesstemp39 ='jessatom4 x. %s'%(3.273270+(d*0.050000))
jesstemp39 = '('+jesstemp39+') and not (jessatom4 x. %s)'%(max(0.05,3.266733-(d*0.050000)))
jesstemp40 ='jessatom5 x. %s'%(3.823820+(d*0.050000))
jesstemp40 = '('+jesstemp40+') and not (jessatom5 x. %s)'%(max(0.05,3.816184-(d*0.050000)))
jesstemp41 ='jessatom6 x. %s'%(1.231230+(d*0.050000))
jesstemp41 = '('+jesstemp41+') and not (jessatom6 x. %s)'%(max(0.05,1.228771-(d*0.050000)))
jesstemp42 ='br. jessatom6'
cmd.select('jessatom7', '(((('+jesstemp35+')&('+jesstemp27+'))|(('+jesstemp35+')&('+jesstemp28+')))&('+jesstemp10+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(9.179170+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom7 x. %s)'%(max(0.05,9.160839-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(9.969960+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom7 x. %s)'%(max(0.05,9.950050-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(11.401390+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom7 x. %s)'%(max(0.05,11.378621-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(4.474470+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom7 x. %s)'%(max(0.05,4.465534-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.273270+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom7 x. %s)'%(max(0.05,3.266733-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(3.823820+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom7 x. %s)'%(max(0.05,3.816184-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.231230+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom7 x. %s)'%(max(0.05,1.228771-(d*0.050000))))
jesstemp43 ='n.  nd2'
jesstemp44 ='jessatom0 x. %s'%(9.919910+(d*0.050000))
jesstemp44 = '('+jesstemp44+') and not (jessatom0 x. %s)'%(max(0.05,9.900100-(d*0.050000)))
jesstemp45 ='jessatom1 x. %s'%(10.440430+(d*0.050000))
jesstemp45 = '('+jesstemp45+') and not (jessatom1 x. %s)'%(max(0.05,10.419580-(d*0.050000)))
jesstemp46 ='jessatom2 x. %s'%(11.871860+(d*0.050000))
jesstemp46 = '('+jesstemp46+') and not (jessatom2 x. %s)'%(max(0.05,11.848152-(d*0.050000)))
jesstemp47 ='jessatom3 x. %s'%(5.685680+(d*0.050000))
jesstemp47 = '('+jesstemp47+') and not (jessatom3 x. %s)'%(max(0.05,5.674326-(d*0.050000)))
jesstemp48 ='jessatom4 x. %s'%(4.494490+(d*0.050000))
jesstemp48 = '('+jesstemp48+') and not (jessatom4 x. %s)'%(max(0.05,4.485514-(d*0.050000)))
jesstemp49 ='jessatom5 x. %s'%(4.384380+(d*0.050000))
jesstemp49 = '('+jesstemp49+') and not (jessatom5 x. %s)'%(max(0.05,4.375624-(d*0.050000)))
jesstemp50 ='jessatom6 x. %s'%(1.301300+(d*0.050000))
jesstemp50 = '('+jesstemp50+') and not (jessatom6 x. %s)'%(max(0.05,1.298701-(d*0.050000)))
jesstemp51 ='br. jessatom6'
jesstemp52 ='jessatom7 x. %s'%(2.192190+(d*0.050000))
jesstemp52 = '('+jesstemp52+') and not (jessatom7 x. %s)'%(max(0.05,2.187812-(d*0.050000)))
cmd.select('jessatom8', '(((('+jesstemp43+')&('+jesstemp27+'))|(('+jesstemp43+')&('+jesstemp28+')))&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(9.919910+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom8 x. %s)'%(max(0.05,9.900100-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(10.440430+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom8 x. %s)'%(max(0.05,10.419580-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(11.871860+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom8 x. %s)'%(max(0.05,11.848152-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.685680+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom8 x. %s)'%(max(0.05,5.674326-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.494490+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom8 x. %s)'%(max(0.05,4.485514-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.384380+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom8 x. %s)'%(max(0.05,4.375624-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.301300+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom8 x. %s)'%(max(0.05,1.298701-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.192190+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom8 x. %s)'%(max(0.05,2.187812-(d*0.050000))))
jesstemp53 ='r. glu'
jesstemp54 ='r. asp'
jesstemp55 ='jessatom0 x. %s'%(9.299290+(d*0.050000))
jesstemp55 = '('+jesstemp55+') and not (jessatom0 x. %s)'%(max(0.05,9.280719-(d*0.050000)))
jesstemp56 ='jessatom1 x. %s'%(9.829820+(d*0.050000))
jesstemp56 = '('+jesstemp56+') and not (jessatom1 x. %s)'%(max(0.05,9.810190-(d*0.050000)))
jesstemp57 ='jessatom2 x. %s'%(11.331320+(d*0.050000))
jesstemp57 = '('+jesstemp57+') and not (jessatom2 x. %s)'%(max(0.05,11.308691-(d*0.050000)))
jesstemp58 ='jessatom3 x. %s'%(8.638630+(d*0.050000))
jesstemp58 = '('+jesstemp58+') and not (jessatom3 x. %s)'%(max(0.05,8.621379-(d*0.050000)))
jesstemp59 ='jessatom4 x. %s'%(7.297290+(d*0.050000))
jesstemp59 = '('+jesstemp59+') and not (jessatom4 x. %s)'%(max(0.05,7.282717-(d*0.050000)))
jesstemp60 ='jessatom5 x. %s'%(7.637630+(d*0.050000))
jesstemp60 = '('+jesstemp60+') and not (jessatom5 x. %s)'%(max(0.05,7.622378-(d*0.050000)))
jesstemp61 ='jessatom6 x. %s'%(4.714710+(d*0.050000))
jesstemp61 = '('+jesstemp61+') and not (jessatom6 x. %s)'%(max(0.05,4.705295-(d*0.050000)))
jesstemp62 ='jessatom7 x. %s'%(4.534530+(d*0.050000))
jesstemp62 = '('+jesstemp62+') and not (jessatom7 x. %s)'%(max(0.05,4.525475-(d*0.050000)))
jesstemp63 ='jessatom8 x. %s'%(5.105100+(d*0.050000))
jesstemp63 = '('+jesstemp63+') and not (jessatom8 x. %s)'%(max(0.05,5.094905-(d*0.050000)))
cmd.select('jessatom9', '(((('+jesstemp8+')&('+jesstemp53+'))|(('+jesstemp8+')&('+jesstemp54+')))&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(9.299290+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom9 x. %s)'%(max(0.05,9.280719-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(9.829820+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom9 x. %s)'%(max(0.05,9.810190-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(11.331320+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom9 x. %s)'%(max(0.05,11.308691-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(8.638630+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom9 x. %s)'%(max(0.05,8.621379-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(7.297290+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom9 x. %s)'%(max(0.05,7.282717-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(7.637630+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom9 x. %s)'%(max(0.05,7.622378-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(4.714710+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom9 x. %s)'%(max(0.05,4.705295-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.534530+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom9 x. %s)'%(max(0.05,4.525475-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(5.105100+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom9 x. %s)'%(max(0.05,5.094905-(d*0.050000))))
jesstemp64 ='n.  oe1'
jesstemp65 ='n.  oe2'
jesstemp66 ='n.  od2'
jesstemp67 ='jessatom0 x. %s'%(8.258250+(d*0.050000))
jesstemp67 = '('+jesstemp67+') and not (jessatom0 x. %s)'%(max(0.05,8.241758-(d*0.050000)))
jesstemp68 ='jessatom1 x. %s'%(8.898890+(d*0.050000))
jesstemp68 = '('+jesstemp68+') and not (jessatom1 x. %s)'%(max(0.05,8.881119-(d*0.050000)))
jesstemp69 ='jessatom2 x. %s'%(10.380370+(d*0.050000))
jesstemp69 = '('+jesstemp69+') and not (jessatom2 x. %s)'%(max(0.05,10.359640-(d*0.050000)))
jesstemp70 ='jessatom3 x. %s'%(7.837830+(d*0.050000))
jesstemp70 = '('+jesstemp70+') and not (jessatom3 x. %s)'%(max(0.05,7.822178-(d*0.050000)))
jesstemp71 ='jessatom4 x. %s'%(6.506500+(d*0.050000))
jesstemp71 = '('+jesstemp71+') and not (jessatom4 x. %s)'%(max(0.05,6.493506-(d*0.050000)))
jesstemp72 ='jessatom5 x. %s'%(6.886880+(d*0.050000))
jesstemp72 = '('+jesstemp72+') and not (jessatom5 x. %s)'%(max(0.05,6.873127-(d*0.050000)))
jesstemp73 ='jessatom6 x. %s'%(4.614610+(d*0.050000))
jesstemp73 = '('+jesstemp73+') and not (jessatom6 x. %s)'%(max(0.05,4.605395-(d*0.050000)))
jesstemp74 ='jessatom7 x. %s'%(4.124120+(d*0.050000))
jesstemp74 = '('+jesstemp74+') and not (jessatom7 x. %s)'%(max(0.05,4.115884-(d*0.050000)))
jesstemp75 ='jessatom8 x. %s'%(5.085080+(d*0.050000))
jesstemp75 = '('+jesstemp75+') and not (jessatom8 x. %s)'%(max(0.05,5.074925-(d*0.050000)))
jesstemp76 ='jessatom9 x. %s'%(1.241240+(d*0.050000))
jesstemp76 = '('+jesstemp76+') and not (jessatom9 x. %s)'%(max(0.05,1.238761-(d*0.050000)))
jesstemp77 ='br. jessatom9'
cmd.select('jessatom10', '((((('+jesstemp64+')|('+jesstemp65+'))&('+jesstemp53+'))|((('+jesstemp35+')|('+jesstemp66+'))&('+jesstemp54+')))&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(8.258250+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom10 x. %s)'%(max(0.05,8.241758-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(8.898890+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom10 x. %s)'%(max(0.05,8.881119-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(10.380370+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom10 x. %s)'%(max(0.05,10.359640-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(7.837830+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom10 x. %s)'%(max(0.05,7.822178-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(6.506500+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom10 x. %s)'%(max(0.05,6.493506-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(6.886880+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom10 x. %s)'%(max(0.05,6.873127-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(4.614610+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom10 x. %s)'%(max(0.05,4.605395-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(4.124120+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom10 x. %s)'%(max(0.05,4.115884-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(5.085080+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom10 x. %s)'%(max(0.05,5.074925-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.241240+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom10 x. %s)'%(max(0.05,1.238761-(d*0.050000))))
jesstemp78 ='n.  oe2'
jesstemp79 ='n.  oe1'
jesstemp80 ='n.  od2'
jesstemp81 ='n.  od1'
jesstemp82 ='jessatom0 x. %s'%(9.559550+(d*0.050000))
jesstemp82 = '('+jesstemp82+') and not (jessatom0 x. %s)'%(max(0.05,9.540460-(d*0.050000)))
jesstemp83 ='jessatom1 x. %s'%(9.949940+(d*0.050000))
jesstemp83 = '('+jesstemp83+') and not (jessatom1 x. %s)'%(max(0.05,9.930070-(d*0.050000)))
jesstemp84 ='jessatom2 x. %s'%(11.451440+(d*0.050000))
jesstemp84 = '('+jesstemp84+') and not (jessatom2 x. %s)'%(max(0.05,11.428571-(d*0.050000)))
jesstemp85 ='jessatom3 x. %s'%(8.848840+(d*0.050000))
jesstemp85 = '('+jesstemp85+') and not (jessatom3 x. %s)'%(max(0.05,8.831169-(d*0.050000)))
jesstemp86 ='jessatom4 x. %s'%(7.457450+(d*0.050000))
jesstemp86 = '('+jesstemp86+') and not (jessatom4 x. %s)'%(max(0.05,7.442557-(d*0.050000)))
jesstemp87 ='jessatom5 x. %s'%(7.597590+(d*0.050000))
jesstemp87 = '('+jesstemp87+') and not (jessatom5 x. %s)'%(max(0.05,7.582418-(d*0.050000)))
jesstemp88 ='jessatom6 x. %s'%(4.474470+(d*0.050000))
jesstemp88 = '('+jesstemp88+') and not (jessatom6 x. %s)'%(max(0.05,4.465534-(d*0.050000)))
jesstemp89 ='jessatom7 x. %s'%(4.564560+(d*0.050000))
jesstemp89 = '('+jesstemp89+') and not (jessatom7 x. %s)'%(max(0.05,4.555445-(d*0.050000)))
jesstemp90 ='jessatom8 x. %s'%(4.574570+(d*0.050000))
jesstemp90 = '('+jesstemp90+') and not (jessatom8 x. %s)'%(max(0.05,4.565435-(d*0.050000)))
jesstemp91 ='jessatom9 x. %s'%(1.251250+(d*0.050000))
jesstemp91 = '('+jesstemp91+') and not (jessatom9 x. %s)'%(max(0.05,1.248751-(d*0.050000)))
jesstemp92 ='br. jessatom9'
jesstemp93 ='jessatom10 x. %s'%(2.192190+(d*0.050000))
jesstemp93 = '('+jesstemp93+') and not (jessatom10 x. %s)'%(max(0.05,2.187812-(d*0.050000)))
cmd.select('jessatom11', '((((('+jesstemp78+')|('+jesstemp79+'))&('+jesstemp53+'))|((('+jesstemp80+')|('+jesstemp81+'))&('+jesstemp54+')))&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(9.559550+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom11 x. %s)'%(max(0.05,9.540460-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(9.949940+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom11 x. %s)'%(max(0.05,9.930070-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(11.451440+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom11 x. %s)'%(max(0.05,11.428571-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(8.848840+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom11 x. %s)'%(max(0.05,8.831169-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(7.457450+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom11 x. %s)'%(max(0.05,7.442557-(d*0.050000))))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(7.597590+(d*0.050000)))
cmd.select('jessatom5', 'jessatom5 & not (jessatom11 x. %s)'%(max(0.05,7.582418-(d*0.050000))))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.474470+(d*0.050000)))
cmd.select('jessatom6', 'jessatom6 & not (jessatom11 x. %s)'%(max(0.05,4.465534-(d*0.050000))))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(4.564560+(d*0.050000)))
cmd.select('jessatom7', 'jessatom7 & not (jessatom11 x. %s)'%(max(0.05,4.555445-(d*0.050000))))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(4.574570+(d*0.050000)))
cmd.select('jessatom8', 'jessatom8 & not (jessatom11 x. %s)'%(max(0.05,4.565435-(d*0.050000))))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(1.251250+(d*0.050000)))
cmd.select('jessatom9', 'jessatom9 & not (jessatom11 x. %s)'%(max(0.05,1.248751-(d*0.050000))))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.192190+(d*0.050000)))
cmd.select('jessatom10', 'jessatom10 & not (jessatom11 x. %s)'%(max(0.05,2.187812-(d*0.050000))))
cmd.select('Jfa_1pgp_1_1_1_44', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
