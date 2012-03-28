'''
FUNC:Jfa_1dd8_2_3_1_41
PDB:1dd8
EC:2.3.1.41
RESI:cys,his,lys,his,phe,phe
LOCI:a-163,298,328,333,390,392;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn cys')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn cys')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.514851))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.514851))
cmd.select('temp6', 'name  sg ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.838100))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*2.782178))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.807900))
cmd.select('temp9', 'temp9 and not within %s of (jessatom1)'%((1./d)*1.772277))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.838100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*2.782178))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.807900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*1.772277))
cmd.select('temp10', 'name  cg ')
cmd.select('temp11', 'resn his')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*7.181100))
cmd.select('temp12', 'temp12 and not within %s of (jessatom0)'%((1./d)*7.039604))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*5.938800))
cmd.select('temp13', 'temp13 and not within %s of (jessatom1)'%((1./d)*5.821782))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*6.645800))
cmd.select('temp14', 'temp14 and not within %s of (jessatom2)'%((1./d)*6.514851))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*7.181100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*7.039604))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.938800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*5.821782))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*6.645800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*6.514851))
cmd.select('temp15', 'name  nd1')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*5.989300))
cmd.select('temp16', 'temp16 and not within %s of (jessatom0)'%((1./d)*5.871287))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*4.848000))
cmd.select('temp17', 'temp17 and not within %s of (jessatom1)'%((1./d)*4.752475))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*5.767100))
cmd.select('temp18', 'temp18 and not within %s of (jessatom2)'%((1./d)*5.653465))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.393800))
cmd.select('temp19', 'temp19 and not within %s of (jessatom3)'%((1./d)*1.366337))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*5.989300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*5.871287))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.848000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*4.752475))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*5.767100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*5.653465))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.393800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.366337))
cmd.select('temp21', 'name  ne2')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*5.908500))
cmd.select('temp22', 'temp22 and not within %s of (jessatom0)'%((1./d)*5.792079))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*4.444000))
cmd.select('temp23', 'temp23 and not within %s of (jessatom1)'%((1./d)*4.356436))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*4.706600))
cmd.select('temp24', 'temp24 and not within %s of (jessatom2)'%((1./d)*4.613861))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.211900))
cmd.select('temp25', 'temp25 and not within %s of (jessatom3)'%((1./d)*2.168317))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*2.161400))
cmd.select('temp27', 'temp27 and not within %s of (jessatom4)'%((1./d)*2.118812))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*5.908500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*5.792079))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*4.444000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*4.356436))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.706600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*4.613861))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.211900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.168317))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.161400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.118812))
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*6.565000))
cmd.select('temp28', 'temp28 and not within %s of (jessatom0)'%((1./d)*6.435644))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*5.817600))
cmd.select('temp29', 'temp29 and not within %s of (jessatom1)'%((1./d)*5.702970))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*5.464100))
cmd.select('temp30', 'temp30 and not within %s of (jessatom2)'%((1./d)*5.356436))
cmd.select('temp31', 'all within %s of (jessatom3)'%(d*7.393200))
cmd.select('temp31', 'temp31 and not within %s of (jessatom3)'%((1./d)*7.247525))
cmd.select('temp32', 'all within %s of (jessatom4)'%(d*6.554900))
cmd.select('temp32', 'temp32 and not within %s of (jessatom4)'%((1./d)*6.425743))
cmd.select('temp33', 'all within %s of (jessatom5)'%(d*6.211500))
cmd.select('temp33', 'temp33 and not within %s of (jessatom5)'%((1./d)*6.089109))
cmd.select('jessatom6', '(temp10 and temp11 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*6.565000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*6.435644))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*5.817600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*5.702970))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*5.464100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*5.356436))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*7.393200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*7.247525))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.554900))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*6.425743))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*6.211500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*6.089109))
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*5.615600))
cmd.select('temp34', 'temp34 and not within %s of (jessatom0)'%((1./d)*5.504950))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*5.080300))
cmd.select('temp35', 'temp35 and not within %s of (jessatom1)'%((1./d)*4.980198))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*5.110600))
cmd.select('temp36', 'temp36 and not within %s of (jessatom2)'%((1./d)*5.009901))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*7.181100))
cmd.select('temp37', 'temp37 and not within %s of (jessatom3)'%((1./d)*7.039604))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*6.140800))
cmd.select('temp38', 'temp38 and not within %s of (jessatom4)'%((1./d)*6.019802))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*6.140800))
cmd.select('temp39', 'temp39 and not within %s of (jessatom5)'%((1./d)*6.019802))
cmd.select('temp40', 'all within %s of (jessatom6)'%(d*1.393800))
cmd.select('temp40', 'temp40 and not within %s of (jessatom6)'%((1./d)*1.366337))
cmd.select('temp41', 'byres jessatom6')
cmd.select('jessatom7', '(temp15 and temp11 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*5.615600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*5.504950))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*5.080300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*4.980198))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*5.110600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*5.009901))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.181100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*7.039604))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*6.140800))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*6.019802))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*6.140800))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*6.019802))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.393800))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.366337))
cmd.select('temp42', 'all within %s of (jessatom0)'%(d*4.716700))
cmd.select('temp42', 'temp42 and not within %s of (jessatom0)'%((1./d)*4.623762))
cmd.select('temp43', 'all within %s of (jessatom1)'%(d*3.757200))
cmd.select('temp43', 'temp43 and not within %s of (jessatom1)'%((1./d)*3.683168))
cmd.select('temp44', 'all within %s of (jessatom2)'%(d*3.292600))
cmd.select('temp44', 'temp44 and not within %s of (jessatom2)'%((1./d)*3.227723))
cmd.select('temp45', 'all within %s of (jessatom3)'%(d*6.282200))
cmd.select('temp45', 'temp45 and not within %s of (jessatom3)'%((1./d)*6.158416))
cmd.select('temp46', 'all within %s of (jessatom4)'%(d*5.383300))
cmd.select('temp46', 'temp46 and not within %s of (jessatom4)'%((1./d)*5.277228))
cmd.select('temp47', 'all within %s of (jessatom5)'%(d*4.716700))
cmd.select('temp47', 'temp47 and not within %s of (jessatom5)'%((1./d)*4.623762))
cmd.select('temp48', 'all within %s of (jessatom6)'%(d*2.211900))
cmd.select('temp48', 'temp48 and not within %s of (jessatom6)'%((1./d)*2.168317))
cmd.select('temp49', 'byres jessatom6')
cmd.select('temp50', 'all within %s of (jessatom7)'%(d*2.151300))
cmd.select('temp50', 'temp50 and not within %s of (jessatom7)'%((1./d)*2.108911))
cmd.select('jessatom8', '(temp21 and temp11 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*4.716700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*4.623762))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*3.757200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*3.683168))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*3.292600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*3.227723))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*6.282200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*6.158416))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*5.383300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*5.277228))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*4.716700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*4.623762))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.211900))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*2.168317))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.151300))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.108911))
cmd.select('temp51', 'name  n  ')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*5.443900))
cmd.select('temp52', 'temp52 and not within %s of (jessatom0)'%((1./d)*5.336634))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*4.959100))
cmd.select('temp53', 'temp53 and not within %s of (jessatom1)'%((1./d)*4.861386))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*4.282400))
cmd.select('temp54', 'temp54 and not within %s of (jessatom2)'%((1./d)*4.198020))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*8.625400))
cmd.select('temp55', 'temp55 and not within %s of (jessatom3)'%((1./d)*8.455446))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*8.181000))
cmd.select('temp56', 'temp56 and not within %s of (jessatom4)'%((1./d)*8.019802))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*6.817500))
cmd.select('temp57', 'temp57 and not within %s of (jessatom5)'%((1./d)*6.683168))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*9.635400))
cmd.select('temp58', 'temp58 and not within %s of (jessatom6)'%((1./d)*9.445545))
cmd.select('temp59', 'all within %s of (jessatom7)'%(d*9.372800))
cmd.select('temp59', 'temp59 and not within %s of (jessatom7)'%((1./d)*9.188119))
cmd.select('temp60', 'all within %s of (jessatom8)'%(d*7.453800))
cmd.select('temp60', 'temp60 and not within %s of (jessatom8)'%((1./d)*7.306931))
cmd.select('jessatom9', '(temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*5.443900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom9)'%((1./d)*5.336634))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*4.959100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom9)'%((1./d)*4.861386))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*4.282400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom9)'%((1./d)*4.198020))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*8.625400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom9)'%((1./d)*8.455446))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*8.181000))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom9)'%((1./d)*8.019802))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*6.817500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom9)'%((1./d)*6.683168))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*9.635400))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom9)'%((1./d)*9.445545))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*9.372800))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom9)'%((1./d)*9.188119))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*7.453800))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom9)'%((1./d)*7.306931))
cmd.select('temp61', 'all within %s of (jessatom0)'%(d*6.807400))
cmd.select('temp61', 'temp61 and not within %s of (jessatom0)'%((1./d)*6.673267))
cmd.select('temp62', 'all within %s of (jessatom1)'%(d*6.352900))
cmd.select('temp62', 'temp62 and not within %s of (jessatom1)'%((1./d)*6.227723))
cmd.select('temp63', 'all within %s of (jessatom2)'%(d*5.454000))
cmd.select('temp63', 'temp63 and not within %s of (jessatom2)'%((1./d)*5.346535))
cmd.select('temp64', 'all within %s of (jessatom3)'%(d*9.847500))
cmd.select('temp64', 'temp64 and not within %s of (jessatom3)'%((1./d)*9.653465))
cmd.select('temp65', 'all within %s of (jessatom4)'%(d*9.504100))
cmd.select('temp65', 'temp65 and not within %s of (jessatom4)'%((1./d)*9.316832))
cmd.select('temp66', 'all within %s of (jessatom5)'%(d*7.979000))
cmd.select('temp66', 'temp66 and not within %s of (jessatom5)'%((1./d)*7.821782))
cmd.select('temp67', 'all within %s of (jessatom6)'%(d*10.655500))
cmd.select('temp67', 'temp67 and not within %s of (jessatom6)'%((1./d)*10.445545))
cmd.select('temp68', 'all within %s of (jessatom7)'%(d*10.514100))
cmd.select('temp68', 'temp68 and not within %s of (jessatom7)'%((1./d)*10.306931))
cmd.select('temp69', 'all within %s of (jessatom8)'%(d*8.534500))
cmd.select('temp69', 'temp69 and not within %s of (jessatom8)'%((1./d)*8.366337))
cmd.select('temp70', 'all within %s of (jessatom9)'%(d*1.474600))
cmd.select('temp70', 'temp70 and not within %s of (jessatom9)'%((1./d)*1.445545))
cmd.select('temp71', 'byres jessatom9')
cmd.select('jessatom10', '(temp0 and temp61 and temp62 and temp63 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69 and temp70 and temp71)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*6.807400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom10)'%((1./d)*6.673267))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*6.352900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom10)'%((1./d)*6.227723))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*5.454000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom10)'%((1./d)*5.346535))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*9.847500))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom10)'%((1./d)*9.653465))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*9.504100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom10)'%((1./d)*9.316832))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*7.979000))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom10)'%((1./d)*7.821782))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*10.655500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom10)'%((1./d)*10.445545))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*10.514100))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom10)'%((1./d)*10.306931))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*8.534500))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom10)'%((1./d)*8.366337))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.474600))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom10)'%((1./d)*1.445545))
cmd.select('temp72', 'name  c  ')
cmd.select('temp73', 'all within %s of (jessatom0)'%(d*7.504300))
cmd.select('temp73', 'temp73 and not within %s of (jessatom0)'%((1./d)*7.356436))
cmd.select('temp74', 'all within %s of (jessatom1)'%(d*7.282100))
cmd.select('temp74', 'temp74 and not within %s of (jessatom1)'%((1./d)*7.138614))
cmd.select('temp75', 'all within %s of (jessatom2)'%(d*6.625600))
cmd.select('temp75', 'temp75 and not within %s of (jessatom2)'%((1./d)*6.495050))
cmd.select('temp76', 'all within %s of (jessatom3)'%(d*10.827200))
cmd.select('temp76', 'temp76 and not within %s of (jessatom3)'%((1./d)*10.613861))
cmd.select('temp77', 'all within %s of (jessatom4)'%(d*10.473700))
cmd.select('temp77', 'temp77 and not within %s of (jessatom4)'%((1./d)*10.267327))
cmd.select('temp78', 'all within %s of (jessatom5)'%(d*9.120300))
cmd.select('temp78', 'temp78 and not within %s of (jessatom5)'%((1./d)*8.940594))
cmd.select('temp79', 'all within %s of (jessatom6)'%(d*11.968500))
cmd.select('temp79', 'temp79 and not within %s of (jessatom6)'%((1./d)*11.732673))
cmd.select('temp80', 'all within %s of (jessatom7)'%(d*11.726100))
cmd.select('temp80', 'temp80 and not within %s of (jessatom7)'%((1./d)*11.495050))
cmd.select('temp81', 'all within %s of (jessatom8)'%(d*9.817200))
cmd.select('temp81', 'temp81 and not within %s of (jessatom8)'%((1./d)*9.623762))
cmd.select('temp82', 'all within %s of (jessatom9)'%(d*2.444200))
cmd.select('temp82', 'temp82 and not within %s of (jessatom9)'%((1./d)*2.396040))
cmd.select('temp83', 'byres jessatom9')
cmd.select('temp84', 'all within %s of (jessatom10)'%(d*1.515000))
cmd.select('temp84', 'temp84 and not within %s of (jessatom10)'%((1./d)*1.485149))
cmd.select('jessatom11', '(temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80 and temp81 and temp82 and temp83 and temp84)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*7.504300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom11)'%((1./d)*7.356436))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*7.282100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom11)'%((1./d)*7.138614))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*6.625600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom11)'%((1./d)*6.495050))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*10.827200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom11)'%((1./d)*10.613861))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*10.473700))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom11)'%((1./d)*10.267327))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*9.120300))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom11)'%((1./d)*8.940594))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*11.968500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom11)'%((1./d)*11.732673))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*11.726100))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom11)'%((1./d)*11.495050))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*9.817200))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom11)'%((1./d)*9.623762))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.444200))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom11)'%((1./d)*2.396040))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*1.515000))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom11)'%((1./d)*1.485149))
cmd.select('Jfa_1dd8_2_3_1_41', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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
cmd.delete('temp0')
cmd.delete('temp1')
cmd.delete('temp2')
cmd.delete('temp3')
cmd.delete('temp4')
cmd.delete('temp5')
cmd.delete('temp6')
cmd.delete('temp7')
cmd.delete('temp8')
cmd.delete('temp9')
cmd.delete('temp10')
cmd.delete('temp11')
cmd.delete('temp12')
cmd.delete('temp13')
cmd.delete('temp14')
cmd.delete('temp15')
cmd.delete('temp16')
cmd.delete('temp17')
cmd.delete('temp18')
cmd.delete('temp19')
cmd.delete('temp20')
cmd.delete('temp21')
cmd.delete('temp22')
cmd.delete('temp23')
cmd.delete('temp24')
cmd.delete('temp25')
cmd.delete('temp26')
cmd.delete('temp27')
cmd.delete('temp28')
cmd.delete('temp29')
cmd.delete('temp30')
cmd.delete('temp31')
cmd.delete('temp32')
cmd.delete('temp33')
cmd.delete('temp34')
cmd.delete('temp35')
cmd.delete('temp36')
cmd.delete('temp37')
cmd.delete('temp38')
cmd.delete('temp39')
cmd.delete('temp40')
cmd.delete('temp41')
cmd.delete('temp42')
cmd.delete('temp43')
cmd.delete('temp44')
cmd.delete('temp45')
cmd.delete('temp46')
cmd.delete('temp47')
cmd.delete('temp48')
cmd.delete('temp49')
cmd.delete('temp50')
cmd.delete('temp51')
cmd.delete('temp52')
cmd.delete('temp53')
cmd.delete('temp54')
cmd.delete('temp55')
cmd.delete('temp56')
cmd.delete('temp57')
cmd.delete('temp58')
cmd.delete('temp59')
cmd.delete('temp60')
cmd.delete('temp61')
cmd.delete('temp62')
cmd.delete('temp63')
cmd.delete('temp64')
cmd.delete('temp65')
cmd.delete('temp66')
cmd.delete('temp67')
cmd.delete('temp68')
cmd.delete('temp69')
cmd.delete('temp70')
cmd.delete('temp71')
cmd.delete('temp72')
cmd.delete('temp73')
cmd.delete('temp74')
cmd.delete('temp75')
cmd.delete('temp76')
cmd.delete('temp77')
cmd.delete('temp78')
cmd.delete('temp79')
cmd.delete('temp80')
cmd.delete('temp81')
cmd.delete('temp82')
cmd.delete('temp83')
cmd.delete('temp84')
