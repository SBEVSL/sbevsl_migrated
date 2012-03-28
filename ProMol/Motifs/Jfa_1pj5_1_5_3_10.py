'''
FUNC:Jfa_1pj5_1_5_3_10
PDB:1pj5
EC:1.5.3.10
RESI:his,tyr,asp
LOCI:a-225,259,552;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nd1')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.393800))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.366337))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.393800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.366337))
cmd.select('temp6', 'name  ne2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.222000))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*2.178218))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.171500))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*2.128713))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*2.178218))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.171500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*2.128713))
cmd.select('temp10', 'name  ce1')
cmd.select('temp11', 'resn tyr')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*7.070000))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom0))'%((1./d)*6.930693))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*6.696300))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom1))'%((1./d)*6.564356))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*4.878300))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom2))'%((1./d)*4.782178))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*7.070000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*6.930693))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.696300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*6.564356))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.878300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*4.782178))
cmd.select('temp15', 'name  cz ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*5.777200))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom0))'%((1./d)*5.663366))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*5.454000))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom1))'%((1./d)*5.346535))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*3.565300))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom2))'%((1./d)*3.495050))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.434200))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom3))'%((1./d)*1.405941))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*5.777200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*5.663366))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*5.454000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*5.346535))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.565300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*3.495050))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.434200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.405941))
cmd.select('temp21', 'name  oh ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*4.938900))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom0))'%((1./d)*4.841584))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*4.908600))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom1))'%((1./d)*4.811881))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*2.817900))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom2))'%((1./d)*2.762376))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.444200))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom3))'%((1./d)*2.396040))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*1.383700))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom4))'%((1./d)*1.356436))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*4.938900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*4.841584))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*4.908600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*4.811881))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*2.817900))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*2.762376))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.444200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*2.396040))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.383700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.356436))
cmd.select('temp28', 'resn asp')
cmd.select('temp29', 'resn glu')
cmd.select('temp30', 'all within %s of (jessatom0)'%(d*39.430400))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom0))'%((1./d)*38.653465))
cmd.select('temp31', 'all within %s of (jessatom1)'%(d*39.844500))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom1))'%((1./d)*39.059406))
cmd.select('temp32', 'all within %s of (jessatom2)'%(d*39.390000))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom2))'%((1./d)*38.613861))
cmd.select('temp33', 'all within %s of (jessatom3)'%(d*40.602000))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom3))'%((1./d)*39.801980))
cmd.select('temp34', 'all within %s of (jessatom4)'%(d*39.753600))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom4))'%((1./d)*38.970297))
cmd.select('temp35', 'all within %s of (jessatom5)'%(d*39.773800))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom5))'%((1./d)*38.990099))
cmd.select('jessatom6', '(((temp0 and temp28) or (temp0 and temp29)) and temp30 and temp31 and temp32 and temp33 and temp34 and temp35)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*39.430400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*38.653465))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*39.844500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*39.059406))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*39.390000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*38.613861))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*40.602000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*39.801980))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*39.753600))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*38.970297))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*39.773800))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*38.990099))
cmd.select('temp36', 'name  od1')
cmd.select('temp37', 'name  od2')
cmd.select('temp38', 'name  oe1')
cmd.select('temp39', 'name  oe2')
cmd.select('temp40', 'all within %s of (jessatom0)'%(d*38.268900))
cmd.select('temp40', 'temp40 and not (all within %s of (jessatom0))'%((1./d)*37.514851))
cmd.select('temp41', 'all within %s of (jessatom1)'%(d*38.672900))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom1))'%((1./d)*37.910891))
cmd.select('temp42', 'all within %s of (jessatom2)'%(d*38.248700))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom2))'%((1./d)*37.495050))
cmd.select('temp43', 'all within %s of (jessatom3)'%(d*39.541500))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom3))'%((1./d)*38.762376))
cmd.select('temp44', 'all within %s of (jessatom4)'%(d*38.672900))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom4))'%((1./d)*37.910891))
cmd.select('temp45', 'all within %s of (jessatom5)'%(d*38.672900))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom5))'%((1./d)*37.910891))
cmd.select('temp46', 'all within %s of (jessatom6)'%(d*1.272600))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom6))'%((1./d)*1.247525))
cmd.select('temp47', 'byres jessatom6')
cmd.select('jessatom7', '((((temp36 or temp37) and temp28) or ((temp38 or temp39) and temp29)) and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*38.268900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*37.514851))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*38.672900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*37.910891))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*38.248700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*37.495050))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*39.541500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*38.762376))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*38.672900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*37.910891))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*38.672900))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*37.910891))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.272600))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.247525))
cmd.select('temp48', 'name  od2')
cmd.select('temp49', 'name  od1')
cmd.select('temp50', 'name  oe2')
cmd.select('temp51', 'name  oe1')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*40.016200))
cmd.select('temp52', 'temp52 and not (all within %s of (jessatom0))'%((1./d)*39.227723))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*40.379800))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom1))'%((1./d)*39.584158))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*39.945500))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom2))'%((1./d)*39.158416))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*41.096900))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom3))'%((1./d)*40.287129))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*40.268700))
cmd.select('temp56', 'temp56 and not (all within %s of (jessatom4))'%((1./d)*39.475248))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*40.319200))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom5))'%((1./d)*39.524752))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*1.282700))
cmd.select('temp58', 'temp58 and not (all within %s of (jessatom6))'%((1./d)*1.257426))
cmd.select('temp59', 'byres jessatom6')
cmd.select('temp60', 'all within %s of (jessatom7)'%(d*2.201800))
cmd.select('temp60', 'temp60 and not (all within %s of (jessatom7))'%((1./d)*2.158416))
cmd.select('jessatom8', '((((temp48 or temp49) and temp28) or ((temp50 or temp51) and temp29)) and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*40.016200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*39.227723))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*40.379800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*39.584158))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*39.945500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*39.158416))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*41.096900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*40.287129))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*40.268700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*39.475248))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*40.319200))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*39.524752))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.282700))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*1.257426))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.201800))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.158416))
cmd.select('Jfa_1pj5_1_5_3_10', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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