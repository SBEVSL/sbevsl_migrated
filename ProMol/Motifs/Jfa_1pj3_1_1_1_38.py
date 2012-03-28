'''
FUNC:Jfa_1pj3_1_1_1_38
PDB:1pj3
EC:1.1.1.38
RESI:tyr,lys,asp
LOCI:a-112,183,278;
'''
cmd.select('temp0', 'name  ce1')
cmd.select('temp1', 'resn tyr')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cz ')
cmd.select('temp3', 'resn tyr')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.403900))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.376238))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.403900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.376238))
cmd.select('temp6', 'name  oh ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.424000))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*2.376238))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.393800))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*1.366337))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.424000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*2.376238))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.393800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*1.366337))
cmd.select('temp10', 'name  cd ')
cmd.select('temp11', 'resn lys')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*4.161200))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom0))'%((1./d)*4.079208))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*4.696500))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom1))'%((1./d)*4.603960))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*4.373300))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom2))'%((1./d)*4.287129))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.161200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*4.079208))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.696500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*4.603960))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.373300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*4.287129))
cmd.select('temp15', 'name  ce ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*4.009700))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom0))'%((1./d)*3.930693))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*4.433900))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom1))'%((1./d)*4.346535))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*3.868300))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom2))'%((1./d)*3.792079))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom3))'%((1./d)*1.514851))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.009700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*3.930693))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.433900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*4.346535))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.868300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*3.792079))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.545300))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.514851))
cmd.select('temp21', 'name  nz ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*3.939000))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom0))'%((1./d)*3.861386))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*3.858200))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom1))'%((1./d)*3.782178))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*2.898700))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom2))'%((1./d)*2.841584))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.545200))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom3))'%((1./d)*2.495050))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*1.515000))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom4))'%((1./d)*1.485149))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*3.939000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*3.861386))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*3.858200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*3.782178))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*2.898700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*2.841584))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.545200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*2.495050))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.515000))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.485149))
cmd.select('temp28', 'name  cg ')
cmd.select('temp29', 'resn asp')
cmd.select('temp30', 'resn glu')
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*8.170900))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom0))'%((1./d)*8.009901))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*7.817400))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom1))'%((1./d)*7.663366))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*6.625600))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom2))'%((1./d)*6.495050))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*5.312600))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom3))'%((1./d)*5.207921))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*5.039900))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom4))'%((1./d)*4.940594))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*4.433900))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom5))'%((1./d)*4.346535))
cmd.select('jessatom6', '(((temp28 and temp29) or (temp28 and temp30)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.170900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*8.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*7.817400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*7.663366))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*6.625600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*6.495050))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*5.312600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*5.207921))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*5.039900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*4.940594))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*4.433900))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*4.346535))
cmd.select('temp37', 'name  od1')
cmd.select('temp38', 'name  od2')
cmd.select('temp39', 'name  oe1')
cmd.select('temp40', 'name  oe2')
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*8.726400))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom0))'%((1./d)*8.554455))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*8.221400))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom1))'%((1./d)*8.059406))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*6.989200))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom2))'%((1./d)*6.851485))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*6.171100))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom3))'%((1./d)*6.049505))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*5.999400))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom4))'%((1./d)*5.881188))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*5.201500))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom5))'%((1./d)*5.099010))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*1.262500))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom6))'%((1./d)*1.237624))
cmd.select('temp48', 'byres jessatom6')
cmd.select('jessatom7', '((((temp37 or temp38) and temp29) or ((temp39 or temp40) and temp30)) and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.726400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*8.554455))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.221400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*8.059406))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*6.989200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*6.851485))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.171100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*6.049505))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.999400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*5.881188))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*5.201500))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*5.099010))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.237624))
cmd.select('temp49', 'name  od2')
cmd.select('temp50', 'name  od1')
cmd.select('temp51', 'name  oe2')
cmd.select('temp52', 'name  oe1')
cmd.select('temp53', 'all within %s of (jessatom0)'%(d*6.928600))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom0))'%((1./d)*6.792079))
cmd.select('temp54', 'all within %s of (jessatom1)'%(d*6.655900))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom1))'%((1./d)*6.524752))
cmd.select('temp55', 'all within %s of (jessatom2)'%(d*5.504500))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom2))'%((1./d)*5.396040))
cmd.select('temp56', 'all within %s of (jessatom3)'%(d*4.130900))
cmd.select('temp56', 'temp56 and not (all within %s of (jessatom3))'%((1./d)*4.049505))
cmd.select('temp57', 'all within %s of (jessatom4)'%(d*3.817800))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom4))'%((1./d)*3.742574))
cmd.select('temp58', 'all within %s of (jessatom5)'%(d*3.201700))
cmd.select('temp58', 'temp58 and not (all within %s of (jessatom5))'%((1./d)*3.138614))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom6))'%((1./d)*1.237624))
cmd.select('temp59', 'byres jessatom6')
cmd.select('temp60', 'all within %s of (jessatom7)'%(d*2.211900))
cmd.select('temp60', 'temp60 and not (all within %s of (jessatom7))'%((1./d)*2.168317))
cmd.select('jessatom8', '((((temp49 or temp50) and temp29) or ((temp51 or temp52) and temp30)) and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp47 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.928600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*6.792079))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*6.655900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*6.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.504500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*5.396040))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*4.130900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*4.049505))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*3.817800))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*3.742574))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*3.201700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*3.138614))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.262500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*1.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.211900))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.168317))
cmd.select('Jfa_1pj3_1_1_1_38', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
cmd.delete('temp58')
cmd.delete('temp59')
cmd.delete('temp60')