'''
FUNC:Jfa_1chd_3_1_1_61
PDB:1chd
EC:3.1.1.61
RESI:ser,thr,his,met,asp
LOCI:a-164,165,190,283,286;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn ser')
cmd.select('temp2', 'resn thr')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.535200))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.504950))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.535200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.504950))
cmd.select('temp6', 'name  og ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.403800))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*2.356436))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.424100))
cmd.select('temp9', 'temp9 and not within %s of (jessatom1)'%((1./d)*1.396040))
cmd.select('jessatom2', '(((temp6 and temp1) or (temp6 and temp2)) and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.403800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*2.356436))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.424100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*1.396040))
cmd.select('temp10', 'name  n  ')
cmd.select('temp11', 'all within %s of (jessatom0)'%(d*2.484600))
cmd.select('temp11', 'temp11 and not within %s of (jessatom0)'%((1./d)*2.435644))
cmd.select('temp12', 'all within %s of (jessatom1)'%(d*2.888600))
cmd.select('temp12', 'temp12 and not within %s of (jessatom1)'%((1./d)*2.831683))
cmd.select('temp13', 'all within %s of (jessatom2)'%(d*2.646200))
cmd.select('temp13', 'temp13 and not within %s of (jessatom2)'%((1./d)*2.594059))
cmd.select('jessatom3', '(((temp10) or (temp10)) and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*2.484600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*2.435644))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*2.888600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*2.831683))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*2.646200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*2.594059))
cmd.select('temp14', 'name  ca ')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*3.878400))
cmd.select('temp15', 'temp15 and not within %s of (jessatom0)'%((1./d)*3.801980))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*4.343000))
cmd.select('temp16', 'temp16 and not within %s of (jessatom1)'%((1./d)*4.257426))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*3.928900))
cmd.select('temp17', 'temp17 and not within %s of (jessatom2)'%((1./d)*3.851485))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*1.464500))
cmd.select('temp18', 'temp18 and not within %s of (jessatom3)'%((1./d)*1.435644))
cmd.select('temp19', 'byres jessatom3')
cmd.select('jessatom4', '(((temp14) or (temp14)) and temp15 and temp16 and temp17 and temp18 and temp19)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*3.878400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*3.801980))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.343000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*4.257426))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.928900))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*3.851485))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.464500))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.435644))
cmd.select('temp20', 'name  c  ')
cmd.select('temp21', 'all within %s of (jessatom0)'%(d*4.534900))
cmd.select('temp21', 'temp21 and not within %s of (jessatom0)'%((1./d)*4.445545))
cmd.select('temp22', 'all within %s of (jessatom1)'%(d*5.211600))
cmd.select('temp22', 'temp22 and not within %s of (jessatom1)'%((1./d)*5.108911))
cmd.select('temp23', 'all within %s of (jessatom2)'%(d*5.140900))
cmd.select('temp23', 'temp23 and not within %s of (jessatom2)'%((1./d)*5.039604))
cmd.select('temp24', 'all within %s of (jessatom3)'%(d*2.525000))
cmd.select('temp24', 'temp24 and not within %s of (jessatom3)'%((1./d)*2.475248))
cmd.select('temp25', 'byres jessatom3')
cmd.select('temp26', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp26', 'temp26 and not within %s of (jessatom4)'%((1./d)*1.514851))
cmd.select('jessatom5', '(((temp20) or (temp20)) and temp21 and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*4.534900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*4.445545))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*5.211600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*5.108911))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*5.140900))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*5.039604))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.525000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.475248))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.514851))
cmd.select('temp27', 'name  cg ')
cmd.select('temp28', 'resn his')
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*4.454100))
cmd.select('temp29', 'temp29 and not within %s of (jessatom0)'%((1./d)*4.366337))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*4.009700))
cmd.select('temp30', 'temp30 and not within %s of (jessatom1)'%((1./d)*3.930693))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*4.181400))
cmd.select('temp31', 'temp31 and not within %s of (jessatom2)'%((1./d)*4.099010))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*6.292300))
cmd.select('temp32', 'temp32 and not within %s of (jessatom3)'%((1./d)*6.168317))
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*7.635600))
cmd.select('temp33', 'temp33 and not within %s of (jessatom4)'%((1./d)*7.485149))
cmd.select('temp34', 'all within %s of (jessatom5)'%(d*8.716300))
cmd.select('temp34', 'temp34 and not within %s of (jessatom5)'%((1./d)*8.544554))
cmd.select('jessatom6', '(temp27 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33 and temp34)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*4.454100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*4.366337))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*4.009700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*3.930693))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*4.181400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*4.099010))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*6.292300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*6.168317))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*7.635600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*7.485149))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.716300))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*8.544554))
cmd.select('temp35', 'name  nd1')
cmd.select('temp36', 'all within %s of (jessatom0)'%(d*4.383400))
cmd.select('temp36', 'temp36 and not within %s of (jessatom0)'%((1./d)*4.297030))
cmd.select('temp37', 'all within %s of (jessatom1)'%(d*3.474400))
cmd.select('temp37', 'temp37 and not within %s of (jessatom1)'%((1./d)*3.405941))
cmd.select('temp38', 'all within %s of (jessatom2)'%(d*3.535000))
cmd.select('temp38', 'temp38 and not within %s of (jessatom2)'%((1./d)*3.465347))
cmd.select('temp39', 'all within %s of (jessatom3)'%(d*5.969100))
cmd.select('temp39', 'temp39 and not within %s of (jessatom3)'%((1./d)*5.851485))
cmd.select('temp40', 'all within %s of (jessatom4)'%(d*7.332600))
cmd.select('temp40', 'temp40 and not within %s of (jessatom4)'%((1./d)*7.188119))
cmd.select('temp41', 'all within %s of (jessatom5)'%(d*8.463800))
cmd.select('temp41', 'temp41 and not within %s of (jessatom5)'%((1./d)*8.297030))
cmd.select('temp42', 'all within %s of (jessatom6)'%(d*1.393800))
cmd.select('temp42', 'temp42 and not within %s of (jessatom6)'%((1./d)*1.366337))
cmd.select('temp43', 'byres jessatom6')
cmd.select('jessatom7', '(temp35 and temp28 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41 and temp42 and temp43)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*4.383400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*4.297030))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*3.474400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*3.405941))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*3.535000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*3.465347))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*5.969100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*5.851485))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*7.332600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*7.188119))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*8.463800))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*8.297030))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.393800))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.366337))
cmd.select('temp44', 'name  ne2')
cmd.select('temp45', 'all within %s of (jessatom0)'%(d*5.827700))
cmd.select('temp45', 'temp45 and not within %s of (jessatom0)'%((1./d)*5.712871))
cmd.select('temp46', 'all within %s of (jessatom1)'%(d*5.090400))
cmd.select('temp46', 'temp46 and not within %s of (jessatom1)'%((1./d)*4.990099))
cmd.select('temp47', 'all within %s of (jessatom2)'%(d*5.524700))
cmd.select('temp47', 'temp47 and not within %s of (jessatom2)'%((1./d)*5.415842))
cmd.select('temp48', 'all within %s of (jessatom3)'%(d*7.807300))
cmd.select('temp48', 'temp48 and not within %s of (jessatom3)'%((1./d)*7.653465))
cmd.select('temp49', 'all within %s of (jessatom4)'%(d*9.231400))
cmd.select('temp49', 'temp49 and not within %s of (jessatom4)'%((1./d)*9.049505))
cmd.select('temp50', 'all within %s of (jessatom5)'%(d*10.221200))
cmd.select('temp50', 'temp50 and not within %s of (jessatom5)'%((1./d)*10.019802))
cmd.select('temp51', 'all within %s of (jessatom6)'%(d*2.222000))
cmd.select('temp51', 'temp51 and not within %s of (jessatom6)'%((1./d)*2.178218))
cmd.select('temp52', 'byres jessatom6')
cmd.select('temp53', 'all within %s of (jessatom7)'%(d*2.171500))
cmd.select('temp53', 'temp53 and not within %s of (jessatom7)'%((1./d)*2.128713))
cmd.select('jessatom8', '(temp44 and temp28 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*5.827700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*5.712871))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*5.090400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*4.990099))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.524700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*5.415842))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.807300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*7.653465))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*9.231400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*9.049505))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*10.221200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*10.019802))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.222000))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*2.178218))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.171500))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.128713))
cmd.select('temp54', 'name  n  ')
cmd.select('temp55', 'all within %s of (jessatom0)'%(d*5.110600))
cmd.select('temp55', 'temp55 and not within %s of (jessatom0)'%((1./d)*5.009901))
cmd.select('temp56', 'all within %s of (jessatom1)'%(d*3.949100))
cmd.select('temp56', 'temp56 and not within %s of (jessatom1)'%((1./d)*3.871287))
cmd.select('temp57', 'all within %s of (jessatom2)'%(d*3.747100))
cmd.select('temp57', 'temp57 and not within %s of (jessatom2)'%((1./d)*3.673267))
cmd.select('temp58', 'all within %s of (jessatom3)'%(d*4.474300))
cmd.select('temp58', 'temp58 and not within %s of (jessatom3)'%((1./d)*4.386139))
cmd.select('temp59', 'all within %s of (jessatom4)'%(d*5.191400))
cmd.select('temp59', 'temp59 and not within %s of (jessatom4)'%((1./d)*5.089109))
cmd.select('temp60', 'all within %s of (jessatom5)'%(d*5.878200))
cmd.select('temp60', 'temp60 and not within %s of (jessatom5)'%((1./d)*5.762376))
cmd.select('temp61', 'all within %s of (jessatom6)'%(d*7.231600))
cmd.select('temp61', 'temp61 and not within %s of (jessatom6)'%((1./d)*7.089109))
cmd.select('temp62', 'all within %s of (jessatom7)'%(d*6.120600))
cmd.select('temp62', 'temp62 and not within %s of (jessatom7)'%((1./d)*6.000000))
cmd.select('temp63', 'all within %s of (jessatom8)'%(d*7.676000))
cmd.select('temp63', 'temp63 and not within %s of (jessatom8)'%((1./d)*7.524752))
cmd.select('jessatom9', '(temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61 and temp62 and temp63)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*5.110600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom9)'%((1./d)*5.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*3.949100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom9)'%((1./d)*3.871287))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*3.747100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom9)'%((1./d)*3.673267))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*4.474300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom9)'%((1./d)*4.386139))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*5.191400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom9)'%((1./d)*5.089109))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*5.878200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom9)'%((1./d)*5.762376))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*7.231600))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom9)'%((1./d)*7.089109))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*6.120600))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom9)'%((1./d)*6.000000))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*7.676000))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom9)'%((1./d)*7.524752))
cmd.select('temp64', 'all within %s of (jessatom0)'%(d*6.393300))
cmd.select('temp64', 'temp64 and not within %s of (jessatom0)'%((1./d)*6.267327))
cmd.select('temp65', 'all within %s of (jessatom1)'%(d*5.110600))
cmd.select('temp65', 'temp65 and not within %s of (jessatom1)'%((1./d)*5.009901))
cmd.select('temp66', 'all within %s of (jessatom2)'%(d*4.696500))
cmd.select('temp66', 'temp66 and not within %s of (jessatom2)'%((1./d)*4.603960))
cmd.select('temp67', 'all within %s of (jessatom3)'%(d*5.726700))
cmd.select('temp67', 'temp67 and not within %s of (jessatom3)'%((1./d)*5.613861))
cmd.select('temp68', 'all within %s of (jessatom4)'%(d*6.332700))
cmd.select('temp68', 'temp68 and not within %s of (jessatom4)'%((1./d)*6.207921))
cmd.select('temp69', 'all within %s of (jessatom5)'%(d*7.120500))
cmd.select('temp69', 'temp69 and not within %s of (jessatom5)'%((1./d)*6.980198))
cmd.select('temp70', 'all within %s of (jessatom6)'%(d*7.888100))
cmd.select('temp70', 'temp70 and not within %s of (jessatom6)'%((1./d)*7.732673))
cmd.select('temp71', 'all within %s of (jessatom7)'%(d*6.645800))
cmd.select('temp71', 'temp71 and not within %s of (jessatom7)'%((1./d)*6.514851))
cmd.select('temp72', 'all within %s of (jessatom8)'%(d*8.150700))
cmd.select('temp72', 'temp72 and not within %s of (jessatom8)'%((1./d)*7.990099))
cmd.select('temp73', 'all within %s of (jessatom9)'%(d*1.464500))
cmd.select('temp73', 'temp73 and not within %s of (jessatom9)'%((1./d)*1.435644))
cmd.select('temp74', 'byres jessatom9')
cmd.select('jessatom10', '(temp0 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69 and temp70 and temp71 and temp72 and temp73 and temp74)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*6.393300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom10)'%((1./d)*6.267327))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*5.110600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom10)'%((1./d)*5.009901))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*4.696500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom10)'%((1./d)*4.603960))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*5.726700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom10)'%((1./d)*5.613861))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*6.332700))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom10)'%((1./d)*6.207921))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*7.120500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom10)'%((1./d)*6.980198))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*7.888100))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom10)'%((1./d)*7.732673))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*6.645800))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom10)'%((1./d)*6.514851))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*8.150700))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom10)'%((1./d)*7.990099))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.464500))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom10)'%((1./d)*1.435644))
cmd.select('temp75', 'name  c  ')
cmd.select('temp76', 'all within %s of (jessatom0)'%(d*6.767000))
cmd.select('temp76', 'temp76 and not within %s of (jessatom0)'%((1./d)*6.633663))
cmd.select('temp77', 'all within %s of (jessatom1)'%(d*5.312600))
cmd.select('temp77', 'temp77 and not within %s of (jessatom1)'%((1./d)*5.207921))
cmd.select('temp78', 'all within %s of (jessatom2)'%(d*5.029800))
cmd.select('temp78', 'temp78 and not within %s of (jessatom2)'%((1./d)*4.930693))
cmd.select('temp79', 'all within %s of (jessatom3)'%(d*6.605400))
cmd.select('temp79', 'temp79 and not within %s of (jessatom3)'%((1./d)*6.475248))
cmd.select('temp80', 'all within %s of (jessatom4)'%(d*7.433600))
cmd.select('temp80', 'temp80 and not within %s of (jessatom4)'%((1./d)*7.287129))
cmd.select('temp81', 'all within %s of (jessatom5)'%(d*8.292100))
cmd.select('temp81', 'temp81 and not within %s of (jessatom5)'%((1./d)*8.128713))
cmd.select('temp82', 'all within %s of (jessatom6)'%(d*7.443700))
cmd.select('temp82', 'temp82 and not within %s of (jessatom6)'%((1./d)*7.297030))
cmd.select('temp83', 'all within %s of (jessatom7)'%(d*6.110500))
cmd.select('temp83', 'temp83 and not within %s of (jessatom7)'%((1./d)*5.990099))
cmd.select('temp84', 'all within %s of (jessatom8)'%(d*7.342700))
cmd.select('temp84', 'temp84 and not within %s of (jessatom8)'%((1./d)*7.198020))
cmd.select('temp85', 'all within %s of (jessatom9)'%(d*2.474500))
cmd.select('temp85', 'temp85 and not within %s of (jessatom9)'%((1./d)*2.425743))
cmd.select('temp86', 'byres jessatom9')
cmd.select('temp87', 'all within %s of (jessatom10)'%(d*1.535200))
cmd.select('temp87', 'temp87 and not within %s of (jessatom10)'%((1./d)*1.504950))
cmd.select('jessatom11', '(temp75 and temp76 and temp77 and temp78 and temp79 and temp80 and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*6.767000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom11)'%((1./d)*6.633663))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*5.312600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom11)'%((1./d)*5.207921))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*5.029800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom11)'%((1./d)*4.930693))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*6.605400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom11)'%((1./d)*6.475248))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*7.433600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom11)'%((1./d)*7.287129))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*8.292100))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom11)'%((1./d)*8.128713))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*7.443700))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom11)'%((1./d)*7.297030))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*6.110500))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom11)'%((1./d)*5.990099))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*7.342700))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom11)'%((1./d)*7.198020))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.474500))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom11)'%((1./d)*2.425743))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*1.535200))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom11)'%((1./d)*1.504950))
cmd.select('temp88', 'resn asp')
cmd.select('temp89', 'resn glu')
cmd.select('temp90', 'all within %s of (jessatom0)'%(d*8.888000))
cmd.select('temp90', 'temp90 and not within %s of (jessatom0)'%((1./d)*8.712871))
cmd.select('temp91', 'all within %s of (jessatom1)'%(d*7.918400))
cmd.select('temp91', 'temp91 and not within %s of (jessatom1)'%((1./d)*7.762376))
cmd.select('temp92', 'all within %s of (jessatom2)'%(d*8.463800))
cmd.select('temp92', 'temp92 and not within %s of (jessatom2)'%((1./d)*8.297030))
cmd.select('temp93', 'all within %s of (jessatom3)'%(d*10.786800))
cmd.select('temp93', 'temp93 and not within %s of (jessatom3)'%((1./d)*10.574257))
cmd.select('temp94', 'all within %s of (jessatom4)'%(d*12.221000))
cmd.select('temp94', 'temp94 and not within %s of (jessatom4)'%((1./d)*11.980198))
cmd.select('temp95', 'all within %s of (jessatom5)'%(d*13.089600))
cmd.select('temp95', 'temp95 and not within %s of (jessatom5)'%((1./d)*12.831683))
cmd.select('temp96', 'all within %s of (jessatom6)'%(d*5.948900))
cmd.select('temp96', 'temp96 and not within %s of (jessatom6)'%((1./d)*5.831683))
cmd.select('temp97', 'all within %s of (jessatom7)'%(d*5.494400))
cmd.select('temp97', 'temp97 and not within %s of (jessatom7)'%((1./d)*5.386139))
cmd.select('temp98', 'all within %s of (jessatom8)'%(d*3.737000))
cmd.select('temp98', 'temp98 and not within %s of (jessatom8)'%((1./d)*3.663366))
cmd.select('temp99', 'all within %s of (jessatom9)'%(d*9.302100))
cmd.select('temp99', 'temp99 and not within %s of (jessatom9)'%((1./d)*9.118812))
cmd.select('temp100', 'all within %s of (jessatom10)'%(d*9.433400))
cmd.select('temp100', 'temp100 and not within %s of (jessatom10)'%((1./d)*9.247525))
cmd.select('temp101', 'all within %s of (jessatom11)'%(d*8.181000))
cmd.select('temp101', 'temp101 and not within %s of (jessatom11)'%((1./d)*8.019802))
cmd.select('jessatom12', '(((temp27 and temp88) or (temp27 and temp89)) and temp90 and temp91 and temp92 and temp93 and temp94 and temp95 and temp96 and temp97 and temp98 and temp99 and temp100 and temp101)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom12)'%(d*8.888000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom12)'%((1./d)*8.712871))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom12)'%(d*7.918400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom12)'%((1./d)*7.762376))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom12)'%(d*8.463800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom12)'%((1./d)*8.297030))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom12)'%(d*10.786800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom12)'%((1./d)*10.574257))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom12)'%(d*12.221000))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom12)'%((1./d)*11.980198))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom12)'%(d*13.089600))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom12)'%((1./d)*12.831683))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom12)'%(d*5.948900))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom12)'%((1./d)*5.831683))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom12)'%(d*5.494400))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom12)'%((1./d)*5.386139))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom12)'%(d*3.737000))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom12)'%((1./d)*3.663366))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom12)'%(d*9.302100))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom12)'%((1./d)*9.118812))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom12)'%(d*9.433400))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom12)'%((1./d)*9.247525))
cmd.select('jessatom11', 'jessatom11 within %s of (jessatom12)'%(d*8.181000))
cmd.select('jessatom11', 'jessatom11 and not within %s of (jessatom12)'%((1./d)*8.019802))
cmd.select('temp102', 'name  od1')
cmd.select('temp103', 'name  od2')
cmd.select('temp104', 'name  oe1')
cmd.select('temp105', 'name  oe2')
cmd.select('temp106', 'all within %s of (jessatom0)'%(d*10.069700))
cmd.select('temp106', 'temp106 and not within %s of (jessatom0)'%((1./d)*9.871287))
cmd.select('temp107', 'all within %s of (jessatom1)'%(d*9.130400))
cmd.select('temp107', 'temp107 and not within %s of (jessatom1)'%((1./d)*8.950495))
cmd.select('temp108', 'all within %s of (jessatom2)'%(d*9.716200))
cmd.select('temp108', 'temp108 and not within %s of (jessatom2)'%((1./d)*9.524752))
cmd.select('temp109', 'all within %s of (jessatom3)'%(d*12.008900))
cmd.select('temp109', 'temp109 and not within %s of (jessatom3)'%((1./d)*11.772277))
cmd.select('temp110', 'all within %s of (jessatom4)'%(d*13.453200))
cmd.select('temp110', 'temp110 and not within %s of (jessatom4)'%((1./d)*13.188119))
cmd.select('temp111', 'all within %s of (jessatom5)'%(d*14.281400))
cmd.select('temp111', 'temp111 and not within %s of (jessatom5)'%((1./d)*14.000000))
cmd.select('temp112', 'all within %s of (jessatom6)'%(d*7.120500))
cmd.select('temp112', 'temp112 and not within %s of (jessatom6)'%((1./d)*6.980198))
cmd.select('temp113', 'all within %s of (jessatom7)'%(d*6.736700))
cmd.select('temp113', 'temp113 and not within %s of (jessatom7)'%((1./d)*6.603960))
cmd.select('temp114', 'all within %s of (jessatom8)'%(d*4.898500))
cmd.select('temp114', 'temp114 and not within %s of (jessatom8)'%((1./d)*4.801980))
cmd.select('temp115', 'all within %s of (jessatom9)'%(d*10.423200))
cmd.select('temp115', 'temp115 and not within %s of (jessatom9)'%((1./d)*10.217822))
cmd.select('temp116', 'all within %s of (jessatom10)'%(d*10.514100))
cmd.select('temp116', 'temp116 and not within %s of (jessatom10)'%((1./d)*10.306931))
cmd.select('temp117', 'all within %s of (jessatom11)'%(d*9.201100))
cmd.select('temp117', 'temp117 and not within %s of (jessatom11)'%((1./d)*9.019802))
cmd.select('temp118', 'all within %s of (jessatom12)'%(d*1.262500))
cmd.select('temp118', 'temp118 and not within %s of (jessatom12)'%((1./d)*1.237624))
cmd.select('temp119', 'byres jessatom12')
cmd.select('jessatom13', '((((temp102 or temp103) and temp88) or ((temp104 or temp105) and temp89)) and temp106 and temp107 and temp108 and temp109 and temp110 and temp111 and temp112 and temp113 and temp114 and temp115 and temp116 and temp117 and temp118 and temp119)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom13)'%(d*10.069700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom13)'%((1./d)*9.871287))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom13)'%(d*9.130400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom13)'%((1./d)*8.950495))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom13)'%(d*9.716200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom13)'%((1./d)*9.524752))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom13)'%(d*12.008900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom13)'%((1./d)*11.772277))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom13)'%(d*13.453200))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom13)'%((1./d)*13.188119))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom13)'%(d*14.281400))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom13)'%((1./d)*14.000000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom13)'%(d*7.120500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom13)'%((1./d)*6.980198))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom13)'%(d*6.736700))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom13)'%((1./d)*6.603960))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom13)'%(d*4.898500))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom13)'%((1./d)*4.801980))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom13)'%(d*10.423200))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom13)'%((1./d)*10.217822))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom13)'%(d*10.514100))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom13)'%((1./d)*10.306931))
cmd.select('jessatom11', 'jessatom11 within %s of (jessatom13)'%(d*9.201100))
cmd.select('jessatom11', 'jessatom11 and not within %s of (jessatom13)'%((1./d)*9.019802))
cmd.select('jessatom12', 'jessatom12 within %s of (jessatom13)'%(d*1.262500))
cmd.select('jessatom12', 'jessatom12 and not within %s of (jessatom13)'%((1./d)*1.237624))
cmd.select('temp120', 'name  od2')
cmd.select('temp121', 'name  od1')
cmd.select('temp122', 'name  oe2')
cmd.select('temp123', 'name  oe1')
cmd.select('temp124', 'all within %s of (jessatom0)'%(d*8.271900))
cmd.select('temp124', 'temp124 and not within %s of (jessatom0)'%((1./d)*8.108911))
cmd.select('temp125', 'all within %s of (jessatom1)'%(d*7.423500))
cmd.select('temp125', 'temp125 and not within %s of (jessatom1)'%((1./d)*7.277228))
cmd.select('temp126', 'all within %s of (jessatom2)'%(d*7.968900))
cmd.select('temp126', 'temp126 and not within %s of (jessatom2)'%((1./d)*7.811881))
cmd.select('temp127', 'all within %s of (jessatom3)'%(d*10.281800))
cmd.select('temp127', 'temp127 and not within %s of (jessatom3)'%((1./d)*10.079208))
cmd.select('temp128', 'all within %s of (jessatom4)'%(d*11.726100))
cmd.select('temp128', 'temp128 and not within %s of (jessatom4)'%((1./d)*11.495050))
cmd.select('temp129', 'all within %s of (jessatom5)'%(d*12.625000))
cmd.select('temp129', 'temp129 and not within %s of (jessatom5)'%((1./d)*12.376238))
cmd.select('temp130', 'all within %s of (jessatom6)'%(d*4.979300))
cmd.select('temp130', 'temp130 and not within %s of (jessatom6)'%((1./d)*4.881188))
cmd.select('temp131', 'all within %s of (jessatom7)'%(d*4.767200))
cmd.select('temp131', 'temp131 and not within %s of (jessatom7)'%((1./d)*4.673267))
cmd.select('temp132', 'all within %s of (jessatom8)'%(d*2.777500))
cmd.select('temp132', 'temp132 and not within %s of (jessatom8)'%((1./d)*2.722772))
cmd.select('temp133', 'all within %s of (jessatom9)'%(d*9.312200))
cmd.select('temp133', 'temp133 and not within %s of (jessatom9)'%((1./d)*9.128713))
cmd.select('temp134', 'all within %s of (jessatom10)'%(d*9.564700))
cmd.select('temp134', 'temp134 and not within %s of (jessatom10)'%((1./d)*9.376238))
cmd.select('temp135', 'all within %s of (jessatom11)'%(d*8.423400))
cmd.select('temp135', 'temp135 and not within %s of (jessatom11)'%((1./d)*8.257426))
cmd.select('temp118', 'temp118 and not within %s of (jessatom12)'%((1./d)*1.237624))
cmd.select('temp136', 'byres jessatom12')
cmd.select('temp137', 'all within %s of (jessatom13)'%(d*2.191700))
cmd.select('temp137', 'temp137 and not within %s of (jessatom13)'%((1./d)*2.148515))
cmd.select('jessatom14', '((((temp120 or temp121) and temp88) or ((temp122 or temp123) and temp89)) and temp124 and temp125 and temp126 and temp127 and temp128 and temp129 and temp130 and temp131 and temp132 and temp133 and temp134 and temp135 and temp118 and temp136 and temp137)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom14)'%(d*8.271900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom14)'%((1./d)*8.108911))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom14)'%(d*7.423500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom14)'%((1./d)*7.277228))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom14)'%(d*7.968900))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom14)'%((1./d)*7.811881))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom14)'%(d*10.281800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom14)'%((1./d)*10.079208))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom14)'%(d*11.726100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom14)'%((1./d)*11.495050))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom14)'%(d*12.625000))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom14)'%((1./d)*12.376238))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom14)'%(d*4.979300))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom14)'%((1./d)*4.881188))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom14)'%(d*4.767200))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom14)'%((1./d)*4.673267))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom14)'%(d*2.777500))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom14)'%((1./d)*2.722772))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom14)'%(d*9.312200))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom14)'%((1./d)*9.128713))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom14)'%(d*9.564700))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom14)'%((1./d)*9.376238))
cmd.select('jessatom11', 'jessatom11 within %s of (jessatom14)'%(d*8.423400))
cmd.select('jessatom11', 'jessatom11 and not within %s of (jessatom14)'%((1./d)*8.257426))
cmd.select('jessatom12', 'jessatom12 within %s of (jessatom14)'%(d*1.262500))
cmd.select('jessatom12', 'jessatom12 and not within %s of (jessatom14)'%((1./d)*1.237624))
cmd.select('jessatom13', 'jessatom13 within %s of (jessatom14)'%(d*2.191700))
cmd.select('jessatom13', 'jessatom13 and not within %s of (jessatom14)'%((1./d)*2.148515))
cmd.select('Jfa_1chd_3_1_1_61', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11|byres jessatom12|byres jessatom13|byres jessatom14')
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
cmd.delete('jessatom12')
cmd.delete('jessatom13')
cmd.delete('jessatom14')
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
cmd.delete('temp85')
cmd.delete('temp86')
cmd.delete('temp87')
cmd.delete('temp88')
cmd.delete('temp89')
cmd.delete('temp90')
cmd.delete('temp91')
cmd.delete('temp92')
cmd.delete('temp93')
cmd.delete('temp94')
cmd.delete('temp95')
cmd.delete('temp96')
cmd.delete('temp97')
cmd.delete('temp98')
cmd.delete('temp99')
cmd.delete('temp100')
cmd.delete('temp101')
cmd.delete('temp102')
cmd.delete('temp103')
cmd.delete('temp104')
cmd.delete('temp105')
cmd.delete('temp106')
cmd.delete('temp107')
cmd.delete('temp108')
cmd.delete('temp109')
cmd.delete('temp110')
cmd.delete('temp111')
cmd.delete('temp112')
cmd.delete('temp113')
cmd.delete('temp114')
cmd.delete('temp115')
cmd.delete('temp116')
cmd.delete('temp117')
cmd.delete('temp118')
cmd.delete('temp119')
cmd.delete('temp120')
cmd.delete('temp121')
cmd.delete('temp122')
cmd.delete('temp123')
cmd.delete('temp124')
cmd.delete('temp125')
cmd.delete('temp126')
cmd.delete('temp127')
cmd.delete('temp128')
cmd.delete('temp129')
cmd.delete('temp130')
cmd.delete('temp131')
cmd.delete('temp132')
cmd.delete('temp133')
cmd.delete('temp134')
cmd.delete('temp135')
cmd.delete('temp136')
cmd.delete('temp137')
