'''
FUNC:Jfa_1c1h_4_99_1_1
PDB:1c1h
EC:4.99.1.1
RESI:his,his,glu
LOCI:a-183,262,264;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nd1')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.393800))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.366337))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.393800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.366337))
cmd.select('temp6', 'name  ne2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.222000))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*2.178218))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.161400))
cmd.select('temp9', 'temp9 and not within %s of (jessatom1)'%((1./d)*2.118812))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*2.178218))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.161400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*2.118812))
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*10.938300))
cmd.select('temp10', 'temp10 and not within %s of (jessatom0)'%((1./d)*10.722772))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*12.079600))
cmd.select('temp11', 'temp11 and not within %s of (jessatom1)'%((1./d)*11.841584))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*10.584800))
cmd.select('temp12', 'temp12 and not within %s of (jessatom2)'%((1./d)*10.376238))
cmd.select('jessatom3', '(temp0 and temp3 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.938300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*10.722772))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*12.079600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*11.841584))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*10.584800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*10.376238))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*12.332100))
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*12.089109))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*13.453200))
cmd.select('temp14', 'temp14 and not within %s of (jessatom1)'%((1./d)*13.188119))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*11.918000))
cmd.select('temp15', 'temp15 and not within %s of (jessatom2)'%((1./d)*11.683168))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*1.393800))
cmd.select('temp16', 'temp16 and not within %s of (jessatom3)'%((1./d)*1.366337))
cmd.select('temp17', 'byres jessatom3')
cmd.select('jessatom4', '(temp2 and temp3 and temp13 and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*12.332100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*12.089109))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*13.453200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*13.188119))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*11.918000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*11.683168))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.393800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.366337))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*11.897800))
cmd.select('temp18', 'temp18 and not within %s of (jessatom0)'%((1./d)*11.663366))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*13.039100))
cmd.select('temp19', 'temp19 and not within %s of (jessatom1)'%((1./d)*12.782178))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*11.705900))
cmd.select('temp20', 'temp20 and not within %s of (jessatom2)'%((1./d)*11.475248))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*2.222000))
cmd.select('temp21', 'temp21 and not within %s of (jessatom3)'%((1./d)*2.178218))
cmd.select('temp22', 'byres jessatom3')
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*2.161400))
cmd.select('temp23', 'temp23 and not within %s of (jessatom4)'%((1./d)*2.118812))
cmd.select('jessatom5', '(temp6 and temp3 and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.897800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*11.663366))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*13.039100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*12.782178))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*11.705900))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*11.475248))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.222000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.178218))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.161400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.118812))
cmd.select('temp24', 'name  cd ')
cmd.select('temp25', 'resn glu')
cmd.select('temp26', 'resn asp')
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*5.918600))
cmd.select('temp27', 'temp27 and not within %s of (jessatom0)'%((1./d)*5.801980))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*6.807400))
cmd.select('temp28', 'temp28 and not within %s of (jessatom1)'%((1./d)*6.673267))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*4.999500))
cmd.select('temp29', 'temp29 and not within %s of (jessatom2)'%((1./d)*4.900990))
cmd.select('temp30', 'all within %s of (jessatom3)'%(d*5.999400))
cmd.select('temp30', 'temp30 and not within %s of (jessatom3)'%((1./d)*5.881188))
cmd.select('temp31', 'all within %s of (jessatom4)'%(d*7.272000))
cmd.select('temp31', 'temp31 and not within %s of (jessatom4)'%((1./d)*7.128713))
cmd.select('temp32', 'all within %s of (jessatom5)'%(d*7.595200))
cmd.select('temp32', 'temp32 and not within %s of (jessatom5)'%((1./d)*7.445545))
cmd.select('jessatom6', '(((temp24 and temp25) or (temp24 and temp26)) and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*5.918600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*5.801980))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*6.807400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*6.673267))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*4.999500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*4.900990))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*5.999400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*5.881188))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*7.272000))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*7.128713))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.595200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*7.445545))
cmd.select('temp33', 'name  oe1')
cmd.select('temp34', 'name  oe2')
cmd.select('temp35', 'name  od1')
cmd.select('temp36', 'name  od2')
cmd.select('temp37', 'all within %s of (jessatom0)'%(d*6.080200))
cmd.select('temp37', 'temp37 and not within %s of (jessatom0)'%((1./d)*5.960396))
cmd.select('temp38', 'all within %s of (jessatom1)'%(d*6.767000))
cmd.select('temp38', 'temp38 and not within %s of (jessatom1)'%((1./d)*6.633663))
cmd.select('temp39', 'all within %s of (jessatom2)'%(d*4.777300))
cmd.select('temp39', 'temp39 and not within %s of (jessatom2)'%((1./d)*4.683168))
cmd.select('temp40', 'all within %s of (jessatom3)'%(d*6.464000))
cmd.select('temp40', 'temp40 and not within %s of (jessatom3)'%((1./d)*6.336634))
cmd.select('temp41', 'all within %s of (jessatom4)'%(d*7.665900))
cmd.select('temp41', 'temp41 and not within %s of (jessatom4)'%((1./d)*7.514851))
cmd.select('temp42', 'all within %s of (jessatom5)'%(d*7.938600))
cmd.select('temp42', 'temp42 and not within %s of (jessatom5)'%((1./d)*7.782178))
cmd.select('temp43', 'all within %s of (jessatom6)'%(d*1.262500))
cmd.select('temp43', 'temp43 and not within %s of (jessatom6)'%((1./d)*1.237624))
cmd.select('temp44', 'byres jessatom6')
cmd.select('jessatom7', '((((temp33 or temp34) and temp25) or ((temp35 or temp36) and temp26)) and temp37 and temp38 and temp39 and temp40 and temp41 and temp42 and temp43 and temp44)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*6.080200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*5.960396))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*6.767000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*6.633663))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*4.777300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*4.683168))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.464000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*6.336634))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*7.665900))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*7.514851))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.938600))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*7.782178))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.237624))
cmd.select('temp45', 'name  oe2')
cmd.select('temp46', 'name  oe1')
cmd.select('temp47', 'name  od2')
cmd.select('temp48', 'name  od1')
cmd.select('temp49', 'all within %s of (jessatom0)'%(d*6.706400))
cmd.select('temp49', 'temp49 and not within %s of (jessatom0)'%((1./d)*6.574257))
cmd.select('temp50', 'all within %s of (jessatom1)'%(d*7.726500))
cmd.select('temp50', 'temp50 and not within %s of (jessatom1)'%((1./d)*7.574257))
cmd.select('temp51', 'all within %s of (jessatom2)'%(d*6.060000))
cmd.select('temp51', 'temp51 and not within %s of (jessatom2)'%((1./d)*5.940594))
cmd.select('temp52', 'all within %s of (jessatom3)'%(d*4.807600))
cmd.select('temp52', 'temp52 and not within %s of (jessatom3)'%((1./d)*4.712871))
cmd.select('temp53', 'all within %s of (jessatom4)'%(d*6.100400))
cmd.select('temp53', 'temp53 and not within %s of (jessatom4)'%((1./d)*5.980198))
cmd.select('temp54', 'all within %s of (jessatom5)'%(d*6.453900))
cmd.select('temp54', 'temp54 and not within %s of (jessatom5)'%((1./d)*6.326733))
cmd.select('temp43', 'temp43 and not within %s of (jessatom6)'%((1./d)*1.237624))
cmd.select('temp55', 'byres jessatom6')
cmd.select('temp56', 'all within %s of (jessatom7)'%(d*2.222000))
cmd.select('temp56', 'temp56 and not within %s of (jessatom7)'%((1./d)*2.178218))
cmd.select('jessatom8', '((((temp45 or temp46) and temp25) or ((temp47 or temp48) and temp26)) and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp43 and temp55 and temp56)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.706400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*6.574257))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.726500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*7.574257))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*6.060000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*5.940594))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*4.807600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*4.712871))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*6.100400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*5.980198))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*6.453900))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*6.326733))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*1.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.222000))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.178218))
cmd.select('Jfa_1c1h_4_99_1_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
