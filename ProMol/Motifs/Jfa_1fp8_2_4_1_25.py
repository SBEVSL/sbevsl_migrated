'''
FUNC:Jfa_1fp8_2_4_1_25
PDB:1fp8
EC:2.4.1.25
RESI:asp,glu,asp
LOCI:a-293,340,395;
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
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*1.237624))
cmd.select('temp13', 'byres jessatom0')
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*2.222000))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom1))'%((1./d)*2.178218))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp7 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*1.237624))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*2.178218))
cmd.select('temp15', 'name  cd ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*5.443900))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom0))'%((1./d)*5.336634))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*6.585200))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom1))'%((1./d)*6.455446))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*4.403600))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom2))'%((1./d)*4.316832))
cmd.select('jessatom3', '(((temp15 and temp2) or (temp15 and temp1)) and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*5.443900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*5.336634))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.585200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*6.455446))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.403600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*4.316832))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*4.555100))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom0))'%((1./d)*4.465347))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*5.656000))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom1))'%((1./d)*5.544554))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*3.444100))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom2))'%((1./d)*3.376238))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*1.262500))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom3))'%((1./d)*1.237624))
cmd.select('temp23', 'byres jessatom3')
cmd.select('jessatom4', '((((temp5 or temp6) and temp2) or ((temp3 or temp4) and temp1)) and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.555100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*4.465347))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*5.656000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*5.544554))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.444100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*3.376238))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.262500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.237624))
cmd.select('temp24', 'all within %s of (jessatom0)'%(d*6.575100))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom0))'%((1./d)*6.445545))
cmd.select('temp25', 'all within %s of (jessatom1)'%(d*7.655800))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom1))'%((1./d)*7.504950))
cmd.select('temp26', 'all within %s of (jessatom2)'%(d*5.454000))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom2))'%((1./d)*5.346535))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom3))'%((1./d)*1.237624))
cmd.select('temp27', 'byres jessatom3')
cmd.select('temp28', 'all within %s of (jessatom4)'%(d*2.211900))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom4))'%((1./d)*2.168317))
cmd.select('jessatom5', '((((temp11 or temp12) and temp2) or ((temp9 or temp10) and temp1)) and temp24 and temp25 and temp26 and temp22 and temp27 and temp28)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*6.575100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*6.445545))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.655800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*7.504950))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*5.454000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*5.346535))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.262500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*1.237624))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.211900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*2.168317))
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*8.221400))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom0))'%((1./d)*8.059406))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*8.282000))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom1))'%((1./d)*8.118812))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*7.888100))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom2))'%((1./d)*7.732673))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*8.504200))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom3))'%((1./d)*8.336634))
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*8.675900))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom4))'%((1./d)*8.504950))
cmd.select('temp34', 'all within %s of (jessatom5)'%(d*8.696100))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom5))'%((1./d)*8.524752))
cmd.select('jessatom6', '(((temp0 and temp1) or (temp0 and temp2)) and temp29 and temp30 and temp31 and temp32 and temp33 and temp34)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.221400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*8.059406))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*8.282000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*8.118812))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*7.888100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*7.732673))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*8.504200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*8.336634))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*8.675900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*8.504950))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.696100))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*8.524752))
cmd.select('temp35', 'all within %s of (jessatom0)'%(d*8.484000))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom0))'%((1./d)*8.316832))
cmd.select('temp36', 'all within %s of (jessatom1)'%(d*8.362800))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom1))'%((1./d)*8.198020))
cmd.select('temp37', 'all within %s of (jessatom2)'%(d*8.302200))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom2))'%((1./d)*8.138614))
cmd.select('temp38', 'all within %s of (jessatom3)'%(d*9.443500))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom3))'%((1./d)*9.257426))
cmd.select('temp39', 'all within %s of (jessatom4)'%(d*9.504100))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom4))'%((1./d)*9.316832))
cmd.select('temp40', 'all within %s of (jessatom5)'%(d*9.726300))
cmd.select('temp40', 'temp40 and not (all within %s of (jessatom5))'%((1./d)*9.534653))
cmd.select('temp41', 'all within %s of (jessatom6)'%(d*1.262500))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom6))'%((1./d)*1.237624))
cmd.select('temp42', 'byres jessatom6')
cmd.select('jessatom7', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41 and temp42)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.484000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*8.316832))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.362800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*8.198020))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*8.302200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*8.138614))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*9.443500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*9.257426))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*9.504100))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*9.316832))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*9.726300))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*9.534653))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.237624))
cmd.select('temp43', 'all within %s of (jessatom0)'%(d*7.120500))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom0))'%((1./d)*6.980198))
cmd.select('temp44', 'all within %s of (jessatom1)'%(d*7.302300))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom1))'%((1./d)*7.158416))
cmd.select('temp45', 'all within %s of (jessatom2)'%(d*6.756900))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom2))'%((1./d)*6.623762))
cmd.select('temp46', 'all within %s of (jessatom3)'%(d*7.302300))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom3))'%((1./d)*7.158416))
cmd.select('temp47', 'all within %s of (jessatom4)'%(d*7.474000))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom4))'%((1./d)*7.326733))
cmd.select('temp48', 'all within %s of (jessatom5)'%(d*7.585100))
cmd.select('temp48', 'temp48 and not (all within %s of (jessatom5))'%((1./d)*7.435644))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom6))'%((1./d)*1.237624))
cmd.select('temp49', 'byres jessatom6')
cmd.select('temp50', 'all within %s of (jessatom7)'%(d*2.211900))
cmd.select('temp50', 'temp50 and not (all within %s of (jessatom7))'%((1./d)*2.168317))
cmd.select('jessatom8', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp41 and temp49 and temp50)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*7.120500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*6.980198))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.302300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*7.158416))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*6.756900))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*6.623762))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.302300))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*7.158416))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*7.474000))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*7.326733))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*7.585100))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*7.435644))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*1.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.211900))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.168317))
cmd.select('Jfa_1fp8_2_4_1_25', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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