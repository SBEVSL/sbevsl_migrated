'''
FUNC:Jab_1ei9_3_1_2_22
PDB:1ei9
EC:3.1.2.22
RESI:met,ser,gln,asp,his
LOCI:a-41,115,116,233,289;
'''
cmd.select('temp0', 'name  n  ')
cmd.select('jessatom0', '(temp0)')
cmd.select('temp1', 'name  ca ')
cmd.select('temp2', 'all within %s of (jessatom0)'%(d*1.464500))
cmd.select('temp2', 'temp2 and not (all within %s of (jessatom0))'%((1./d)*1.435644))
cmd.select('temp3', 'byres jessatom0')
cmd.select('jessatom1', '(temp1 and temp2 and temp3)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.464500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.435644))
cmd.select('temp4', 'resn ser')
cmd.select('temp5', 'resn thr')
cmd.select('temp6', 'all within %s of (jessatom0)'%(d*6.019600))
cmd.select('temp6', 'temp6 and not (all within %s of (jessatom0))'%((1./d)*5.900990))
cmd.select('temp7', 'all within %s of (jessatom1)'%(d*7.322500))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom1))'%((1./d)*7.178218))
cmd.select('jessatom2', '(((temp1 and temp4) or (temp1 and temp5)) and temp6 and temp7)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*6.019600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*5.900990))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*7.322500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*7.178218))
cmd.select('temp8', 'name  cb ')
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*4.888400))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom0))'%((1./d)*4.792079))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*6.120600))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom1))'%((1./d)*6.000000))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom2))'%((1./d)*1.514851))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(((temp8 and temp4) or (temp8 and temp5)) and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.888400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*4.792079))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.120600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*6.000000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.514851))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*5.050000))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom0))'%((1./d)*4.950495))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*6.211500))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom1))'%((1./d)*6.089109))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*2.494700))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom2))'%((1./d)*2.445545))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*2.807800))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom3))'%((1./d)*2.752475))
cmd.select('jessatom4', '(((temp0) or (temp0)) and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*5.050000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*4.950495))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.211500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*6.089109))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*2.494700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*2.445545))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*2.807800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*2.752475))
cmd.select('temp17', 'name  ca ')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*5.575200))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom0))'%((1./d)*5.465347))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*6.585200))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom1))'%((1./d)*6.455446))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*3.868300))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom2))'%((1./d)*3.792079))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*4.282400))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom3))'%((1./d)*4.198020))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.484700))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom4))'%((1./d)*1.455446))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(((temp17) or (temp17)) and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*5.575200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*5.465347))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*6.585200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*6.455446))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*3.868300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*3.792079))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*4.282400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*4.198020))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.484700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.455446))
cmd.select('temp24', 'resn asp')
cmd.select('temp25', 'resn glu')
cmd.select('temp26', 'all within %s of (jessatom0)'%(d*15.240900))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom0))'%((1./d)*14.940594))
cmd.select('temp27', 'all within %s of (jessatom1)'%(d*15.836800))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom1))'%((1./d)*15.524752))
cmd.select('temp28', 'all within %s of (jessatom2)'%(d*11.574600))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom2))'%((1./d)*11.346535))
cmd.select('temp29', 'all within %s of (jessatom3)'%(d*11.433200))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom3))'%((1./d)*11.207921))
cmd.select('temp30', 'all within %s of (jessatom4)'%(d*13.150200))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom4))'%((1./d)*12.891089))
cmd.select('temp31', 'all within %s of (jessatom5)'%(d*14.281400))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom5))'%((1./d)*14.000000))
cmd.select('jessatom6', '(((temp1 and temp24) or (temp1 and temp25)) and temp26 and temp27 and temp28 and temp29 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*15.240900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*14.940594))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*15.836800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*15.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*11.574600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*11.346535))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*11.433200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*11.207921))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*13.150200))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*12.891089))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*14.281400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*14.000000))
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*14.483400))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom0))'%((1./d)*14.198020))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*15.150000))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom1))'%((1./d)*14.851485))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*10.463600))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom2))'%((1./d)*10.257426))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*10.463600))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom3))'%((1./d)*10.257426))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*11.998800))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom4))'%((1./d)*11.762376))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*13.079500))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom5))'%((1./d)*12.821782))
cmd.select('temp38', 'all within %s of (jessatom6)'%(d*1.555400))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom6))'%((1./d)*1.524752))
cmd.select('temp39', 'byres jessatom6')
cmd.select('jessatom7', '(((temp8 and temp24) or (temp8 and temp25)) and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*14.483400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*14.198020))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*15.150000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*14.851485))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*10.463600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*10.257426))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*10.463600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*10.257426))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*11.998800))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*11.762376))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*13.079500))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*12.821782))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.555400))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.524752))
cmd.select('temp40', 'resn his')
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*11.493800))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom0))'%((1./d)*11.267327))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*12.231100))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom1))'%((1./d)*11.990099))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*8.302200))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom2))'%((1./d)*8.138614))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*7.857800))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom3))'%((1./d)*7.702970))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*10.261600))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom4))'%((1./d)*10.059406))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*11.655400))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom5))'%((1./d)*11.425743))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*5.029800))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom6))'%((1./d)*4.930693))
cmd.select('temp48', 'all within %s of (jessatom7)'%(d*4.969200))
cmd.select('temp48', 'temp48 and not (all within %s of (jessatom7))'%((1./d)*4.871287))
cmd.select('jessatom8', '(temp1 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*11.493800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*11.267327))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*12.231100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*11.990099))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*8.302200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*8.138614))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.857800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*7.702970))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*10.261600))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*10.059406))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*11.655400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*11.425743))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*5.029800))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*4.930693))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*4.969200))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*4.871287))
cmd.select('temp49', 'all within %s of (jessatom0)'%(d*10.504000))
cmd.select('temp49', 'temp49 and not (all within %s of (jessatom0))'%((1./d)*10.297030))
cmd.select('temp50', 'all within %s of (jessatom1)'%(d*11.130200))
cmd.select('temp50', 'temp50 and not (all within %s of (jessatom1))'%((1./d)*10.910891))
cmd.select('temp51', 'all within %s of (jessatom2)'%(d*7.777000))
cmd.select('temp51', 'temp51 and not (all within %s of (jessatom2))'%((1./d)*7.623762))
cmd.select('temp52', 'all within %s of (jessatom3)'%(d*7.160900))
cmd.select('temp52', 'temp52 and not (all within %s of (jessatom3))'%((1./d)*7.019802))
cmd.select('temp53', 'all within %s of (jessatom4)'%(d*9.483900))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom4))'%((1./d)*9.297030))
cmd.select('temp54', 'all within %s of (jessatom5)'%(d*10.837300))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom5))'%((1./d)*10.623762))
cmd.select('temp55', 'all within %s of (jessatom6)'%(d*5.272200))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom6))'%((1./d)*5.168317))
cmd.select('temp56', 'all within %s of (jessatom7)'%(d*5.110600))
cmd.select('temp56', 'temp56 and not (all within %s of (jessatom7))'%((1./d)*5.009901))
cmd.select('temp57', 'all within %s of (jessatom8)'%(d*1.545300))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom8))'%((1./d)*1.514851))
cmd.select('temp58', 'byres jessatom8')
cmd.select('jessatom9', '(temp8 and temp40 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*10.504000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom9))'%((1./d)*10.297030))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*11.130200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom9))'%((1./d)*10.910891))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*7.777000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom9))'%((1./d)*7.623762))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*7.160900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom9))'%((1./d)*7.019802))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*9.483900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom9))'%((1./d)*9.297030))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*10.837300))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom9))'%((1./d)*10.623762))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*5.272200))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom9))'%((1./d)*5.168317))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*5.110600))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom9))'%((1./d)*5.009901))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*1.545300))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom9))'%((1./d)*1.514851))
cmd.select('Jab_1ei9_3_1_2_22', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9')
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