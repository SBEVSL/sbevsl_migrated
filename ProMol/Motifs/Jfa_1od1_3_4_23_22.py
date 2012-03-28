'''
FUNC:Jfa_1od1_3_4_23_22
PDB:1od1
EC:3.4.23.22
RESI:asp,thr,asp,thr
LOCI:a-35,36,219,222;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  od1')
cmd.select('temp4', 'name  od2')
cmd.select('temp5', 'name  oe1')
cmd.select('temp6', 'name  oe2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.262500))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*1.237624))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.237624))
cmd.select('temp9', 'name  od2')
cmd.select('temp10', 'name  od1')
cmd.select('temp11', 'name  oe2')
cmd.select('temp12', 'name  oe1')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*1.272600))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom0))'%((1./d)*1.247525))
cmd.select('temp14', 'byres jessatom0')
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*2.252300))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom1))'%((1./d)*2.207921))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.272600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*1.247525))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.252300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*2.207921))
cmd.select('temp16', 'name  ca ')
cmd.select('temp17', 'resn ser')
cmd.select('temp18', 'resn thr')
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*4.585400))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom0))'%((1./d)*4.495050))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*4.989400))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom1))'%((1./d)*4.891089))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*4.090500))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom2))'%((1./d)*4.009901))
cmd.select('jessatom3', '(((temp16 and temp17) or (temp16 and temp18)) and temp19 and temp20 and temp21)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.585400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*4.495050))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.989400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*4.891089))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.090500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*4.009901))
cmd.select('temp22', 'name  cb ')
cmd.select('temp23', 'all within %s of (jessatom0)'%(d*4.181400))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom0))'%((1./d)*4.099010))
cmd.select('temp24', 'all within %s of (jessatom1)'%(d*4.848000))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom1))'%((1./d)*4.752475))
cmd.select('temp25', 'all within %s of (jessatom2)'%(d*3.302700))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom2))'%((1./d)*3.237624))
cmd.select('temp26', 'all within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom3))'%((1./d)*1.524752))
cmd.select('temp27', 'byres jessatom3')
cmd.select('jessatom4', '(((temp22 and temp17) or (temp22 and temp18)) and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.181400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*4.099010))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.848000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*4.752475))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.302700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*3.237624))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.555400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.524752))
cmd.select('temp28', 'name  og ')
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*3.413800))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom0))'%((1./d)*3.346535))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*4.373300))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom1))'%((1./d)*4.287129))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*2.575500))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom2))'%((1./d)*2.524752))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*2.494700))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom3))'%((1./d)*2.445545))
cmd.select('temp33', 'byres jessatom3')
cmd.select('temp34', 'all within %s of (jessatom4)'%(d*1.444300))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom4))'%((1./d)*1.415842))
cmd.select('jessatom5', '(((temp28 and temp17) or (temp28 and temp18)) and temp29 and temp30 and temp31 and temp32 and temp33 and temp34)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*3.413800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*3.346535))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*4.373300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*4.287129))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*2.575500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*2.524752))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.494700))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*2.445545))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.444300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.415842))
cmd.select('temp35', 'all within %s of (jessatom0)'%(d*5.302500))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom0))'%((1./d)*5.198020))
cmd.select('temp36', 'all within %s of (jessatom1)'%(d*4.070300))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom1))'%((1./d)*3.990099))
cmd.select('temp37', 'all within %s of (jessatom2)'%(d*5.918600))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom2))'%((1./d)*5.801980))
cmd.select('temp38', 'all within %s of (jessatom3)'%(d*7.393200))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom3))'%((1./d)*7.247525))
cmd.select('temp39', 'all within %s of (jessatom4)'%(d*7.665900))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom4))'%((1./d)*7.514851))
cmd.select('temp40', 'all within %s of (jessatom5)'%(d*7.807300))
cmd.select('temp40', 'temp40 and not (all within %s of (jessatom5))'%((1./d)*7.653465))
cmd.select('jessatom6', '(((temp0 and temp1) or (temp0 and temp2)) and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*5.302500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*5.198020))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*4.070300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*3.990099))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*5.918600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*5.801980))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*7.393200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*7.247525))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*7.665900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*7.514851))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.807300))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*7.653465))
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*4.292500))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom0))'%((1./d)*4.207921))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*3.040100))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom1))'%((1./d)*2.980198))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*5.090400))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom2))'%((1./d)*4.990099))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*6.847800))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom3))'%((1./d)*6.712871))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*7.090200))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom4))'%((1./d)*6.950495))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*7.049800))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom5))'%((1./d)*6.910891))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*1.252400))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom6))'%((1./d)*1.227723))
cmd.select('temp48', 'byres jessatom6')
cmd.select('jessatom7', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*4.292500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*4.207921))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*3.040100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*2.980198))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*5.090400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*4.990099))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.847800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*6.712871))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*7.090200))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*6.950495))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.049800))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*6.910891))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.252400))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.227723))
cmd.select('temp49', 'all within %s of (jessatom0)'%(d*5.565100))
cmd.select('temp49', 'temp49 and not (all within %s of (jessatom0))'%((1./d)*5.455446))
cmd.select('temp50', 'all within %s of (jessatom1)'%(d*4.454100))
cmd.select('temp50', 'temp50 and not (all within %s of (jessatom1))'%((1./d)*4.366337))
cmd.select('temp51', 'all within %s of (jessatom2)'%(d*5.928700))
cmd.select('temp51', 'temp51 and not (all within %s of (jessatom2))'%((1./d)*5.811881))
cmd.select('temp52', 'all within %s of (jessatom3)'%(d*7.383100))
cmd.select('temp52', 'temp52 and not (all within %s of (jessatom3))'%((1./d)*7.237624))
cmd.select('temp53', 'all within %s of (jessatom4)'%(d*7.514400))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom4))'%((1./d)*7.366337))
cmd.select('temp54', 'all within %s of (jessatom5)'%(d*7.797200))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom5))'%((1./d)*7.643564))
cmd.select('temp55', 'all within %s of (jessatom6)'%(d*1.262500))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom6))'%((1./d)*1.237624))
cmd.select('temp56', 'byres jessatom6')
cmd.select('temp57', 'all within %s of (jessatom7)'%(d*2.242200))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom7))'%((1./d)*2.198020))
cmd.select('jessatom8', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*5.565100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*5.455446))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*4.454100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*4.366337))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.928700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*5.811881))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.383100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*7.237624))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*7.514400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*7.366337))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*7.797200))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*7.643564))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*1.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.242200))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.198020))
cmd.select('Jfa_1od1_3_4_23_22', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
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