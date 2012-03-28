'''
FUNC:Jab_2dnj_3_1_21_1
PDB:2dnj
EC:3.1.21.1
RESI:glu,his,asp,his
LOCI:a-78,134,212,252;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.585700))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.554455))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.585700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.554455))
cmd.select('temp6', 'resn his')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*9.130400))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*8.950495))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*7.645700))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom1))'%((1./d)*7.495050))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*9.130400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*8.950495))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*7.645700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*7.495050))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*7.888100))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom0))'%((1./d)*7.732673))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*6.363000))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom1))'%((1./d)*6.237624))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.525100))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom2))'%((1./d)*1.495050))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*7.888100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*7.732673))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.363000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*6.237624))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.525100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.495050))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*16.947800))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom0))'%((1./d)*16.613861))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*15.453000))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom1))'%((1./d)*15.148515))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*9.009200))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom2))'%((1./d)*8.831683))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*9.544500))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom3))'%((1./d)*9.356436))
cmd.select('jessatom4', '(((temp0 and temp2) or (temp0 and temp1)) and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*16.947800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*16.613861))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*15.453000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*15.148515))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*9.009200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*8.831683))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*9.544500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*9.356436))
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*16.654900))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom0))'%((1./d)*16.326733))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*15.200500))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom1))'%((1./d)*14.900990))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*9.312200))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom2))'%((1./d)*9.128713))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*9.635400))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom3))'%((1./d)*9.445545))
cmd.select('temp21', 'all within %s of (jessatom4)'%(d*1.565500))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom4))'%((1./d)*1.534653))
cmd.select('temp22', 'byres jessatom4')
cmd.select('jessatom5', '(((temp3 and temp2) or (temp3 and temp1)) and temp17 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*16.654900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*16.326733))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*15.200500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*14.900990))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.312200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*9.128713))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*9.635400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*9.445545))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.565500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.534653))
cmd.select('temp23', 'all within %s of (jessatom0)'%(d*16.351900))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom0))'%((1./d)*16.029703))
cmd.select('temp24', 'all within %s of (jessatom1)'%(d*15.079300))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom1))'%((1./d)*14.782178))
cmd.select('temp25', 'all within %s of (jessatom2)'%(d*12.210900))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom2))'%((1./d)*11.970297))
cmd.select('temp26', 'all within %s of (jessatom3)'%(d*11.685700))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom3))'%((1./d)*11.455446))
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*8.029500))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom4))'%((1./d)*7.871287))
cmd.select('temp28', 'all within %s of (jessatom5)'%(d*6.857900))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom5))'%((1./d)*6.722772))
cmd.select('jessatom6', '(temp0 and temp6 and temp23 and temp24 and temp25 and temp26 and temp27 and temp28)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*16.351900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*16.029703))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*15.079300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*14.782178))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*12.210900))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*11.970297))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*11.685700))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*11.455446))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*8.029500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*7.871287))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*6.857900))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*6.722772))
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*15.119700))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom0))'%((1./d)*14.821782))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*13.796600))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom1))'%((1./d)*13.524752))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*10.675700))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom2))'%((1./d)*10.465347))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*10.160600))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom3))'%((1./d)*9.960396))
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*6.999300))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom4))'%((1./d)*6.861386))
cmd.select('temp34', 'all within %s of (jessatom5)'%(d*5.847900))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom5))'%((1./d)*5.732673))
cmd.select('temp35', 'all within %s of (jessatom6)'%(d*1.565500))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom6))'%((1./d)*1.534653))
cmd.select('temp36', 'byres jessatom6')
cmd.select('jessatom7', '(temp3 and temp6 and temp29 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*15.119700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*14.821782))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*13.796600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*13.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*10.675700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*10.465347))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*10.160600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*9.960396))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*6.999300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*6.861386))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*5.847900))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*5.732673))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.565500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.534653))
cmd.select('Jab_2dnj_3_1_21_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
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