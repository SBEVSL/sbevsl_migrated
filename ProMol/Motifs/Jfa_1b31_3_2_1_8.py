'''
FUNC:Jfa_1b31_3_2_1_8
PDB:1b31
EC:3.2.1.8
RESI:glu,his,glu,asp
LOCI:a-132,210,238,240;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  oe1')
cmd.select('temp4', 'name  oe2')
cmd.select('temp5', 'name  od1')
cmd.select('temp6', 'name  od2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.262500))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*1.237624))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.237624))
cmd.select('temp9', 'name  oe2')
cmd.select('temp10', 'name  oe1')
cmd.select('temp11', 'name  od2')
cmd.select('temp12', 'name  od1')
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*1.237624))
cmd.select('temp13', 'byres jessatom0')
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*2.211900))
cmd.select('temp14', 'temp14 and not within %s of (jessatom1)'%((1./d)*2.168317))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp7 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*1.237624))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.211900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*2.168317))
cmd.select('temp15', 'name  cg ')
cmd.select('temp16', 'resn his')
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*8.817300))
cmd.select('temp17', 'temp17 and not within %s of (jessatom0)'%((1./d)*8.643564))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*9.625300))
cmd.select('temp18', 'temp18 and not within %s of (jessatom1)'%((1./d)*9.435644))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*7.676000))
cmd.select('temp19', 'temp19 and not within %s of (jessatom2)'%((1./d)*7.524752))
cmd.select('jessatom3', '(temp15 and temp16 and temp17 and temp18 and temp19)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.817300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*8.643564))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*9.625300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*9.435644))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*7.676000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*7.524752))
cmd.select('temp20', 'name  nd1')
cmd.select('temp21', 'all within %s of (jessatom0)'%(d*9.574800))
cmd.select('temp21', 'temp21 and not within %s of (jessatom0)'%((1./d)*9.386139))
cmd.select('temp22', 'all within %s of (jessatom1)'%(d*10.372700))
cmd.select('temp22', 'temp22 and not within %s of (jessatom1)'%((1./d)*10.168317))
cmd.select('temp23', 'all within %s of (jessatom2)'%(d*8.362800))
cmd.select('temp23', 'temp23 and not within %s of (jessatom2)'%((1./d)*8.198020))
cmd.select('temp24', 'all within %s of (jessatom3)'%(d*1.393800))
cmd.select('temp24', 'temp24 and not within %s of (jessatom3)'%((1./d)*1.366337))
cmd.select('temp25', 'byres jessatom3')
cmd.select('jessatom4', '(temp20 and temp16 and temp21 and temp22 and temp23 and temp24 and temp25)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*9.574800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*9.386139))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*10.372700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*10.168317))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*8.362800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*8.198020))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.393800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.366337))
cmd.select('temp26', 'name  ne2')
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*7.665900))
cmd.select('temp27', 'temp27 and not within %s of (jessatom0)'%((1./d)*7.514851))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*8.534500))
cmd.select('temp28', 'temp28 and not within %s of (jessatom1)'%((1./d)*8.366337))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*6.443800))
cmd.select('temp29', 'temp29 and not within %s of (jessatom2)'%((1./d)*6.316832))
cmd.select('temp30', 'all within %s of (jessatom3)'%(d*2.211900))
cmd.select('temp30', 'temp30 and not within %s of (jessatom3)'%((1./d)*2.168317))
cmd.select('temp31', 'byres jessatom3')
cmd.select('temp32', 'all within %s of (jessatom4)'%(d*2.161400))
cmd.select('temp32', 'temp32 and not within %s of (jessatom4)'%((1./d)*2.118812))
cmd.select('jessatom5', '(temp26 and temp16 and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.665900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*7.514851))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*8.534500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*8.366337))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*6.443800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*6.316832))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.211900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.168317))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.161400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.118812))
cmd.select('temp33', 'all within %s of (jessatom0)'%(d*7.080100))
cmd.select('temp33', 'temp33 and not within %s of (jessatom0)'%((1./d)*6.940594))
cmd.select('temp34', 'all within %s of (jessatom1)'%(d*8.130500))
cmd.select('temp34', 'temp34 and not within %s of (jessatom1)'%((1./d)*7.970297))
cmd.select('temp35', 'all within %s of (jessatom2)'%(d*6.009500))
cmd.select('temp35', 'temp35 and not within %s of (jessatom2)'%((1./d)*5.891089))
cmd.select('temp36', 'all within %s of (jessatom3)'%(d*5.938800))
cmd.select('temp36', 'temp36 and not within %s of (jessatom3)'%((1./d)*5.821782))
cmd.select('temp37', 'all within %s of (jessatom4)'%(d*5.787300))
cmd.select('temp37', 'temp37 and not within %s of (jessatom4)'%((1./d)*5.673267))
cmd.select('temp38', 'all within %s of (jessatom5)'%(d*3.878400))
cmd.select('temp38', 'temp38 and not within %s of (jessatom5)'%((1./d)*3.801980))
cmd.select('jessatom6', '(((temp0 and temp1) or (temp0 and temp2)) and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*7.080100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*6.940594))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*8.130500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*7.970297))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*6.009500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*5.891089))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*5.938800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*5.821782))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*5.787300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*5.673267))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*3.878400))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*3.801980))
cmd.select('temp39', 'all within %s of (jessatom0)'%(d*6.686200))
cmd.select('temp39', 'temp39 and not within %s of (jessatom0)'%((1./d)*6.554455))
cmd.select('temp40', 'all within %s of (jessatom1)'%(d*7.655800))
cmd.select('temp40', 'temp40 and not within %s of (jessatom1)'%((1./d)*7.504950))
cmd.select('temp41', 'all within %s of (jessatom2)'%(d*5.514600))
cmd.select('temp41', 'temp41 and not within %s of (jessatom2)'%((1./d)*5.405941))
cmd.select('temp42', 'all within %s of (jessatom3)'%(d*5.090400))
cmd.select('temp42', 'temp42 and not within %s of (jessatom3)'%((1./d)*4.990099))
cmd.select('temp43', 'all within %s of (jessatom4)'%(d*4.928800))
cmd.select('temp43', 'temp43 and not within %s of (jessatom4)'%((1./d)*4.831683))
cmd.select('temp44', 'all within %s of (jessatom5)'%(d*2.918900))
cmd.select('temp44', 'temp44 and not within %s of (jessatom5)'%((1./d)*2.861386))
cmd.select('temp45', 'all within %s of (jessatom6)'%(d*1.262500))
cmd.select('temp45', 'temp45 and not within %s of (jessatom6)'%((1./d)*1.237624))
cmd.select('temp46', 'byres jessatom6')
cmd.select('jessatom7', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp39 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*6.686200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*6.554455))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*7.655800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*7.504950))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*5.514600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*5.405941))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*5.090400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*4.990099))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*4.928800))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*4.831683))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*2.918900))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*2.861386))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.237624))
cmd.select('temp47', 'all within %s of (jessatom0)'%(d*6.585200))
cmd.select('temp47', 'temp47 and not within %s of (jessatom0)'%((1./d)*6.455446))
cmd.select('temp40', 'temp40 and not within %s of (jessatom1)'%((1./d)*7.504950))
cmd.select('temp48', 'all within %s of (jessatom2)'%(d*5.666100))
cmd.select('temp48', 'temp48 and not within %s of (jessatom2)'%((1./d)*5.554455))
cmd.select('temp49', 'all within %s of (jessatom3)'%(d*7.009400))
cmd.select('temp49', 'temp49 and not within %s of (jessatom3)'%((1./d)*6.871287))
cmd.select('temp50', 'all within %s of (jessatom4)'%(d*6.969000))
cmd.select('temp50', 'temp50 and not within %s of (jessatom4)'%((1./d)*6.831683))
cmd.select('temp51', 'all within %s of (jessatom5)'%(d*4.969200))
cmd.select('temp51', 'temp51 and not within %s of (jessatom5)'%((1./d)*4.871287))
cmd.select('temp45', 'temp45 and not within %s of (jessatom6)'%((1./d)*1.237624))
cmd.select('temp52', 'byres jessatom6')
cmd.select('temp53', 'all within %s of (jessatom7)'%(d*2.211900))
cmd.select('temp53', 'temp53 and not within %s of (jessatom7)'%((1./d)*2.168317))
cmd.select('jessatom8', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp47 and temp40 and temp48 and temp49 and temp50 and temp51 and temp45 and temp52 and temp53)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.585200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*6.455446))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.655800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*7.504950))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.666100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*5.554455))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.009400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*6.871287))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*6.969000))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*6.831683))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*4.969200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*4.871287))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*1.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.211900))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.168317))
cmd.select('temp54', 'all within %s of (jessatom0)'%(d*12.806800))
cmd.select('temp54', 'temp54 and not within %s of (jessatom0)'%((1./d)*12.554455))
cmd.select('temp55', 'all within %s of (jessatom1)'%(d*13.554200))
cmd.select('temp55', 'temp55 and not within %s of (jessatom1)'%((1./d)*13.287129))
cmd.select('temp56', 'all within %s of (jessatom2)'%(d*11.574600))
cmd.select('temp56', 'temp56 and not within %s of (jessatom2)'%((1./d)*11.346535))
cmd.select('temp57', 'all within %s of (jessatom3)'%(d*4.423800))
cmd.select('temp57', 'temp57 and not within %s of (jessatom3)'%((1./d)*4.336634))
cmd.select('temp58', 'all within %s of (jessatom4)'%(d*3.292600))
cmd.select('temp58', 'temp58 and not within %s of (jessatom4)'%((1./d)*3.227723))
cmd.select('temp59', 'all within %s of (jessatom5)'%(d*5.252000))
cmd.select('temp59', 'temp59 and not within %s of (jessatom5)'%((1./d)*5.148515))
cmd.select('temp60', 'all within %s of (jessatom6)'%(d*8.251700))
cmd.select('temp60', 'temp60 and not within %s of (jessatom6)'%((1./d)*8.089109))
cmd.select('temp61', 'all within %s of (jessatom7)'%(d*7.554800))
cmd.select('temp61', 'temp61 and not within %s of (jessatom7)'%((1./d)*7.405941))
cmd.select('temp62', 'all within %s of (jessatom8)'%(d*9.504100))
cmd.select('temp62', 'temp62 and not within %s of (jessatom8)'%((1./d)*9.316832))
cmd.select('jessatom9', '(((temp15 and temp2) or (temp15 and temp1)) and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61 and temp62)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*12.806800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom9)'%((1./d)*12.554455))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*13.554200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom9)'%((1./d)*13.287129))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*11.574600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom9)'%((1./d)*11.346535))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*4.423800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom9)'%((1./d)*4.336634))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*3.292600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom9)'%((1./d)*3.227723))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*5.252000))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom9)'%((1./d)*5.148515))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*8.251700))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom9)'%((1./d)*8.089109))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*7.554800))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom9)'%((1./d)*7.405941))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*9.504100))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom9)'%((1./d)*9.316832))
cmd.select('temp63', 'all within %s of (jessatom0)'%(d*12.342200))
cmd.select('temp63', 'temp63 and not within %s of (jessatom0)'%((1./d)*12.099010))
cmd.select('temp64', 'all within %s of (jessatom1)'%(d*13.099700))
cmd.select('temp64', 'temp64 and not within %s of (jessatom1)'%((1./d)*12.841584))
cmd.select('temp65', 'all within %s of (jessatom2)'%(d*11.150400))
cmd.select('temp65', 'temp65 and not within %s of (jessatom2)'%((1./d)*10.930693))
cmd.select('temp66', 'all within %s of (jessatom3)'%(d*3.656200))
cmd.select('temp66', 'temp66 and not within %s of (jessatom3)'%((1./d)*3.584158))
cmd.select('temp67', 'all within %s of (jessatom4)'%(d*2.838100))
cmd.select('temp67', 'temp67 and not within %s of (jessatom4)'%((1./d)*2.782178))
cmd.select('temp51', 'temp51 and not within %s of (jessatom5)'%((1./d)*4.871287))
cmd.select('temp68', 'all within %s of (jessatom6)'%(d*8.302200))
cmd.select('temp68', 'temp68 and not within %s of (jessatom6)'%((1./d)*8.138614))
cmd.select('temp69', 'all within %s of (jessatom7)'%(d*7.564900))
cmd.select('temp69', 'temp69 and not within %s of (jessatom7)'%((1./d)*7.415842))
cmd.select('temp70', 'all within %s of (jessatom8)'%(d*9.534400))
cmd.select('temp70', 'temp70 and not within %s of (jessatom8)'%((1./d)*9.346535))
cmd.select('temp71', 'all within %s of (jessatom9)'%(d*1.262500))
cmd.select('temp71', 'temp71 and not within %s of (jessatom9)'%((1./d)*1.237624))
cmd.select('temp72', 'byres jessatom9')
cmd.select('jessatom10', '((((temp5 or temp6) and temp2) or ((temp3 or temp4) and temp1)) and temp63 and temp64 and temp65 and temp66 and temp67 and temp51 and temp68 and temp69 and temp70 and temp71 and temp72)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*12.342200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom10)'%((1./d)*12.099010))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*13.099700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom10)'%((1./d)*12.841584))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*11.150400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom10)'%((1./d)*10.930693))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*3.656200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom10)'%((1./d)*3.584158))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*2.838100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom10)'%((1./d)*2.782178))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*4.969200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom10)'%((1./d)*4.871287))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*8.302200))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom10)'%((1./d)*8.138614))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*7.564900))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom10)'%((1./d)*7.415842))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*9.534400))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom10)'%((1./d)*9.346535))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.262500))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom10)'%((1./d)*1.237624))
cmd.select('temp73', 'all within %s of (jessatom0)'%(d*12.271500))
cmd.select('temp73', 'temp73 and not within %s of (jessatom0)'%((1./d)*12.029703))
cmd.select('temp74', 'all within %s of (jessatom1)'%(d*12.978500))
cmd.select('temp74', 'temp74 and not within %s of (jessatom1)'%((1./d)*12.722772))
cmd.select('temp75', 'all within %s of (jessatom2)'%(d*11.019100))
cmd.select('temp75', 'temp75 and not within %s of (jessatom2)'%((1./d)*10.801980))
cmd.select('temp76', 'all within %s of (jessatom3)'%(d*4.444000))
cmd.select('temp76', 'temp76 and not within %s of (jessatom3)'%((1./d)*4.356436))
cmd.select('temp77', 'all within %s of (jessatom4)'%(d*3.141100))
cmd.select('temp77', 'temp77 and not within %s of (jessatom4)'%((1./d)*3.079208))
cmd.select('temp78', 'all within %s of (jessatom5)'%(d*4.817700))
cmd.select('temp78', 'temp78 and not within %s of (jessatom5)'%((1./d)*4.722772))
cmd.select('temp79', 'all within %s of (jessatom6)'%(d*7.665900))
cmd.select('temp79', 'temp79 and not within %s of (jessatom6)'%((1./d)*7.514851))
cmd.select('temp80', 'all within %s of (jessatom7)'%(d*6.898300))
cmd.select('temp80', 'temp80 and not within %s of (jessatom7)'%((1./d)*6.762376))
cmd.select('temp81', 'all within %s of (jessatom8)'%(d*8.908200))
cmd.select('temp81', 'temp81 and not within %s of (jessatom8)'%((1./d)*8.732673))
cmd.select('temp71', 'temp71 and not within %s of (jessatom9)'%((1./d)*1.237624))
cmd.select('temp82', 'byres jessatom9')
cmd.select('temp83', 'all within %s of (jessatom10)'%(d*2.211900))
cmd.select('temp83', 'temp83 and not within %s of (jessatom10)'%((1./d)*2.168317))
cmd.select('jessatom11', '((((temp11 or temp12) and temp2) or ((temp9 or temp10) and temp1)) and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80 and temp81 and temp71 and temp82 and temp83)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*12.271500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom11)'%((1./d)*12.029703))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*12.978500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom11)'%((1./d)*12.722772))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*11.019100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom11)'%((1./d)*10.801980))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*4.444000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom11)'%((1./d)*4.356436))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*3.141100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom11)'%((1./d)*3.079208))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*4.817700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom11)'%((1./d)*4.722772))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*7.665900))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom11)'%((1./d)*7.514851))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*6.898300))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom11)'%((1./d)*6.762376))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*8.908200))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom11)'%((1./d)*8.732673))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*1.262500))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom11)'%((1./d)*1.237624))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.211900))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom11)'%((1./d)*2.168317))
cmd.select('Jfa_1b31_3_2_1_8', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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
