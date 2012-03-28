'''
FUNC:Jfa_3fit_3_6_1_29
PDB:3fit
EC:3.6.1.29
RESI:gln,his,his
LOCI:a-83,94,96;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn gln')
cmd.select('temp2', 'resn asn')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  oe1')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.242300))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.217822))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.242300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.217822))
cmd.select('temp6', 'name  ne2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.333200))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*1.306931))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.252300))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*2.207921))
cmd.select('jessatom2', '(((temp6 and temp1) or (temp6 and temp2)) and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.333200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*1.306931))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.252300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*2.207921))
cmd.select('temp10', 'name  cg ')
cmd.select('temp11', 'resn his')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*13.433000))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom0))'%((1./d)*13.168317))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*14.665200))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom1))'%((1./d)*14.376238))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*12.685600))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom2))'%((1./d)*12.435644))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*13.433000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*13.168317))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*14.665200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*14.376238))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*12.685600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*12.435644))
cmd.select('temp15', 'name  nd1')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*14.685400))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom0))'%((1./d)*14.396040))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*15.917600))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom1))'%((1./d)*15.603960))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*13.887500))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom2))'%((1./d)*13.613861))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.393800))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom3))'%((1./d)*1.366337))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*14.685400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*14.396040))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*15.917600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*15.603960))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*13.887500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*13.613861))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.393800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.366337))
cmd.select('temp21', 'all within %s of (jessatom0)'%(d*14.836900))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom0))'%((1./d)*14.544554))
cmd.select('temp22', 'all within %s of (jessatom1)'%(d*16.079200))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom1))'%((1./d)*15.762376))
cmd.select('temp23', 'all within %s of (jessatom2)'%(d*14.180400))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom2))'%((1./d)*13.900990))
cmd.select('temp24', 'all within %s of (jessatom3)'%(d*2.222000))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom3))'%((1./d)*2.178218))
cmd.select('temp25', 'byres jessatom3')
cmd.select('temp26', 'all within %s of (jessatom4)'%(d*2.151300))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom4))'%((1./d)*2.108911))
cmd.select('jessatom5', '(temp6 and temp11 and temp21 and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*14.836900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*14.544554))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*16.079200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*15.762376))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*14.180400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*13.900990))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.222000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*2.178218))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.151300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*2.108911))
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*8.201200))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom0))'%((1./d)*8.039604))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*9.403100))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom1))'%((1./d)*9.217822))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*7.544700))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom2))'%((1./d)*7.396040))
cmd.select('temp30', 'all within %s of (jessatom3)'%(d*6.211500))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom3))'%((1./d)*6.089109))
cmd.select('temp31', 'all within %s of (jessatom4)'%(d*7.352800))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom4))'%((1./d)*7.207921))
cmd.select('temp32', 'all within %s of (jessatom5)'%(d*7.100300))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom5))'%((1./d)*6.960396))
cmd.select('jessatom6', '(temp10 and temp11 and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.201200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*8.039604))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.403100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*9.217822))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*7.544700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*7.396040))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*6.211500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*6.089109))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*7.352800))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*7.207921))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.100300))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*6.960396))
cmd.select('temp33', 'all within %s of (jessatom0)'%(d*8.039600))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom0))'%((1./d)*7.881188))
cmd.select('temp34', 'all within %s of (jessatom1)'%(d*9.271800))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom1))'%((1./d)*9.089109))
cmd.select('temp35', 'all within %s of (jessatom2)'%(d*7.302300))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom2))'%((1./d)*7.158416))
cmd.select('temp36', 'all within %s of (jessatom3)'%(d*5.635800))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom3))'%((1./d)*5.524752))
cmd.select('temp37', 'all within %s of (jessatom4)'%(d*6.837700))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom4))'%((1./d)*6.702970))
cmd.select('temp38', 'all within %s of (jessatom5)'%(d*6.918500))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom5))'%((1./d)*6.782178))
cmd.select('temp39', 'all within %s of (jessatom6)'%(d*1.393800))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom6))'%((1./d)*1.366337))
cmd.select('temp40', 'byres jessatom6')
cmd.select('jessatom7', '(temp15 and temp11 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.039600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*7.881188))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*9.271800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*9.089109))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*7.302300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*7.158416))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*5.635800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*5.524752))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*6.837700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*6.702970))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*6.918500))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*6.782178))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.393800))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.366337))
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*6.635700))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom0))'%((1./d)*6.504950))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*7.817400))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom1))'%((1./d)*7.663366))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*5.757000))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom2))'%((1./d)*5.643564))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*7.585100))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom3))'%((1./d)*7.435644))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*8.675900))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom4))'%((1./d)*8.504950))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*8.857700))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom5))'%((1./d)*8.683168))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*2.222000))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom6))'%((1./d)*2.178218))
cmd.select('temp48', 'byres jessatom6')
cmd.select('temp49', 'all within %s of (jessatom7)'%(d*2.161400))
cmd.select('temp49', 'temp49 and not (all within %s of (jessatom7))'%((1./d)*2.118812))
cmd.select('jessatom8', '(temp6 and temp11 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.635700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*6.504950))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.817400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*7.663366))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.757000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*5.643564))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.585100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*7.435644))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*8.675900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*8.504950))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*8.857700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*8.683168))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.222000))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*2.178218))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.161400))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.118812))
cmd.select('Jfa_3fit_3_6_1_29', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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