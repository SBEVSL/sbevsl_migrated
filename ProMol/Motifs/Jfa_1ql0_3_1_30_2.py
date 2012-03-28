'''
FUNC:Jfa_1ql0_3_1_30_2
PDB:1ql0
EC:3.1.30.2
RESI:arg,his,asn
LOCI:a-87,89,119;
'''
cmd.select('temp0', 'name  ne ')
cmd.select('temp1', 'resn arg')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nh1')
cmd.select('temp3', 'name  nh2')
cmd.select('temp4', 'resn arg')
cmd.select('temp5', 'all within %s of (jessatom0)'%(d*2.353300))
cmd.select('temp5', 'temp5 and not (all within %s of (jessatom0))'%((1./d)*2.306931))
cmd.select('temp6', 'byres jessatom0')
cmd.select('jessatom1', '((temp2 or temp3) and temp4 and temp5 and temp6)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*2.353300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*2.306931))
cmd.select('temp7', 'name  nh2')
cmd.select('temp8', 'name  nh1')
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*2.312900))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom0))'%((1./d)*2.267327))
cmd.select('temp10', 'byres jessatom0')
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*2.292700))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom1))'%((1./d)*2.247525))
cmd.select('jessatom2', '((temp7 or temp8) and temp4 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.312900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*2.267327))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.292700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*2.247525))
cmd.select('temp12', 'name  cg ')
cmd.select('temp13', 'resn his')
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*10.766600))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom0))'%((1./d)*10.554455))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*11.574600))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom1))'%((1./d)*11.346535))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*12.988600))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom2))'%((1./d)*12.732673))
cmd.select('jessatom3', '(temp12 and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.766600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*10.554455))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*11.574600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*11.346535))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*12.988600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*12.732673))
cmd.select('temp17', 'name  nd1')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*10.150500))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom0))'%((1./d)*9.950495))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*10.746400))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom1))'%((1./d)*10.534653))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*12.291700))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom2))'%((1./d)*12.049505))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*1.383700))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom3))'%((1./d)*1.356436))
cmd.select('temp22', 'byres jessatom3')
cmd.select('jessatom4', '(temp17 and temp13 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*10.150500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*9.950495))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*10.746400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*10.534653))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*12.291700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*12.049505))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.383700))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.356436))
cmd.select('temp23', 'name  ne2')
cmd.select('temp24', 'all within %s of (jessatom0)'%(d*9.999000))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom0))'%((1./d)*9.801980))
cmd.select('temp25', 'all within %s of (jessatom1)'%(d*10.938300))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom1))'%((1./d)*10.722772))
cmd.select('temp26', 'all within %s of (jessatom2)'%(d*12.180600))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom2))'%((1./d)*11.940594))
cmd.select('temp27', 'all within %s of (jessatom3)'%(d*2.222000))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom3))'%((1./d)*2.178218))
cmd.select('temp28', 'byres jessatom3')
cmd.select('temp29', 'all within %s of (jessatom4)'%(d*2.161400))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom4))'%((1./d)*2.118812))
cmd.select('jessatom5', '(temp23 and temp13 and temp24 and temp25 and temp26 and temp27 and temp28 and temp29)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*9.999000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*9.801980))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*10.938300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*10.722772))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*12.180600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*11.940594))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.222000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*2.178218))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.161400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*2.118812))
cmd.select('temp30', 'resn asn')
cmd.select('temp31', 'resn gln')
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*11.110000))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom0))'%((1./d)*10.891089))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*10.463600))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom1))'%((1./d)*10.257426))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*12.604800))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom2))'%((1./d)*12.356436))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*7.595200))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom3))'%((1./d)*7.445545))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*6.817500))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom4))'%((1./d)*6.683168))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*8.857700))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom5))'%((1./d)*8.683168))
cmd.select('jessatom6', '(((temp12 and temp30) or (temp12 and temp31)) and temp32 and temp33 and temp34 and temp35 and temp36 and temp37)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*11.110000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*10.891089))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*10.463600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*10.257426))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*12.604800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*12.356436))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*7.595200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*7.445545))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.817500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*6.683168))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.857700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*8.683168))
cmd.select('temp38', 'name  od1')
cmd.select('temp39', 'all within %s of (jessatom0)'%(d*11.402900))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom0))'%((1./d)*11.178218))
cmd.select('temp40', 'all within %s of (jessatom1)'%(d*10.978700))
cmd.select('temp40', 'temp40 and not (all within %s of (jessatom1))'%((1./d)*10.762376))
cmd.select('temp41', 'all within %s of (jessatom2)'%(d*13.049200))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom2))'%((1./d)*12.792079))
cmd.select('temp42', 'all within %s of (jessatom3)'%(d*6.625600))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom3))'%((1./d)*6.495050))
cmd.select('temp43', 'all within %s of (jessatom4)'%(d*5.948900))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom4))'%((1./d)*5.831683))
cmd.select('temp44', 'all within %s of (jessatom5)'%(d*8.059800))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom5))'%((1./d)*7.900990))
cmd.select('temp45', 'all within %s of (jessatom6)'%(d*1.222100))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom6))'%((1./d)*1.198020))
cmd.select('temp46', 'byres jessatom6')
cmd.select('jessatom7', '(((temp38 and temp30) or (temp38 and temp31)) and temp39 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*11.402900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*11.178218))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*10.978700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*10.762376))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*13.049200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*12.792079))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.625600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*6.495050))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.948900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*5.831683))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*8.059800))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*7.900990))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.222100))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.198020))
cmd.select('temp47', 'name  nd2')
cmd.select('temp48', 'all within %s of (jessatom0)'%(d*10.322200))
cmd.select('temp48', 'temp48 and not (all within %s of (jessatom0))'%((1./d)*10.118812))
cmd.select('temp49', 'all within %s of (jessatom1)'%(d*9.534400))
cmd.select('temp49', 'temp49 and not (all within %s of (jessatom1))'%((1./d)*9.346535))
cmd.select('temp50', 'all within %s of (jessatom2)'%(d*11.736200))
cmd.select('temp50', 'temp50 and not (all within %s of (jessatom2))'%((1./d)*11.504950))
cmd.select('temp51', 'all within %s of (jessatom3)'%(d*7.665900))
cmd.select('temp51', 'temp51 and not (all within %s of (jessatom3))'%((1./d)*7.514851))
cmd.select('temp52', 'all within %s of (jessatom4)'%(d*6.696300))
cmd.select('temp52', 'temp52 and not (all within %s of (jessatom4))'%((1./d)*6.564356))
cmd.select('temp53', 'all within %s of (jessatom5)'%(d*8.615300))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom5))'%((1./d)*8.445545))
cmd.select('temp54', 'all within %s of (jessatom6)'%(d*1.333200))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom6))'%((1./d)*1.306931))
cmd.select('temp55', 'byres jessatom6')
cmd.select('temp56', 'all within %s of (jessatom7)'%(d*2.181600))
cmd.select('temp56', 'temp56 and not (all within %s of (jessatom7))'%((1./d)*2.138614))
cmd.select('jessatom8', '(((temp47 and temp30) or (temp47 and temp31)) and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*10.322200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*10.118812))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*9.534400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*9.346535))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*11.736200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*11.504950))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.665900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*7.514851))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*6.696300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*6.564356))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*8.615300))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*8.445545))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.333200))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*1.306931))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.181600))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.138614))
cmd.select('Jfa_1ql0_3_1_30_2', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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