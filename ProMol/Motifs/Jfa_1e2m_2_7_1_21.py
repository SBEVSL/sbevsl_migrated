'''
FUNC:Jfa_1e2m_2_7_1_21
PDB:1e2m
EC:2.7.1.21
RESI:gly,glu,arg,arg
LOCI:a-59,83,163,222;
'''
cmd.select('temp0', 'name  n  ')
cmd.select('jessatom0', '(temp0)')
cmd.select('temp1', 'name  ca ')
cmd.select('temp2', 'all within %s of (jessatom0)'%(d*1.454400))
cmd.select('temp2', 'temp2 and not (all within %s of (jessatom0))'%((1./d)*1.425743))
cmd.select('temp3', 'byres jessatom0')
cmd.select('jessatom1', '(temp1 and temp2 and temp3)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.454400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.425743))
cmd.select('temp4', 'name  c  ')
cmd.select('temp5', 'all within %s of (jessatom0)'%(d*2.545200))
cmd.select('temp5', 'temp5 and not (all within %s of (jessatom0))'%((1./d)*2.495050))
cmd.select('temp6', 'byres jessatom0')
cmd.select('temp7', 'all within %s of (jessatom1)'%(d*1.525100))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom1))'%((1./d)*1.495050))
cmd.select('jessatom2', '(temp4 and temp5 and temp6 and temp7)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.545200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*2.495050))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.525100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*1.495050))
cmd.select('temp8', 'name  cd ')
cmd.select('temp9', 'resn glu')
cmd.select('temp10', 'resn asp')
cmd.select('temp11', 'all within %s of (jessatom0)'%(d*8.857700))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom0))'%((1./d)*8.683168))
cmd.select('temp12', 'all within %s of (jessatom1)'%(d*9.857600))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom1))'%((1./d)*9.663366))
cmd.select('temp13', 'all within %s of (jessatom2)'%(d*10.928200))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom2))'%((1./d)*10.712871))
cmd.select('jessatom3', '(((temp8 and temp9) or (temp8 and temp10)) and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.857700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*8.683168))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*9.857600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*9.663366))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*10.928200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*10.712871))
cmd.select('temp14', 'name  oe1')
cmd.select('temp15', 'name  oe2')
cmd.select('temp16', 'name  od1')
cmd.select('temp17', 'name  od2')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*9.019300))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom0))'%((1./d)*8.841584))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*9.877800))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom1))'%((1./d)*9.683168))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*10.968600))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom2))'%((1./d)*10.752475))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*1.262500))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom3))'%((1./d)*1.237624))
cmd.select('temp22', 'byres jessatom3')
cmd.select('jessatom4', '((((temp14 or temp15) and temp9) or ((temp16 or temp17) and temp10)) and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*9.019300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*8.841584))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.877800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*9.683168))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*10.968600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*10.752475))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.262500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.237624))
cmd.select('temp23', 'name  oe2')
cmd.select('temp24', 'name  oe1')
cmd.select('temp25', 'name  od2')
cmd.select('temp26', 'name  od1')
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*7.817400))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom0))'%((1./d)*7.663366))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*8.898100))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom1))'%((1./d)*8.722772))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*9.999000))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom2))'%((1./d)*9.801980))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom3))'%((1./d)*1.237624))
cmd.select('temp30', 'byres jessatom3')
cmd.select('temp31', 'all within %s of (jessatom4)'%(d*2.211900))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom4))'%((1./d)*2.168317))
cmd.select('jessatom5', '((((temp23 or temp24) and temp9) or ((temp25 or temp26) and temp10)) and temp27 and temp28 and temp29 and temp21 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.817400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*7.663366))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*8.898100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*8.722772))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.999000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*9.801980))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.262500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*1.237624))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.211900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*2.168317))
cmd.select('temp32', 'name  ne ')
cmd.select('temp33', 'resn arg')
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*7.726500))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom0))'%((1./d)*7.574257))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*9.180900))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom1))'%((1./d)*9.000000))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*10.019200))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom2))'%((1./d)*9.821782))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*6.019600))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom3))'%((1./d)*5.900990))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*7.160900))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom4))'%((1./d)*7.019802))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*4.959100))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom5))'%((1./d)*4.861386))
cmd.select('jessatom6', '(temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*7.726500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*7.574257))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.180900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*9.000000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*10.019200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*9.821782))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*6.019600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*5.900990))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*7.160900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*7.019802))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*4.959100))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*4.861386))
cmd.select('temp40', 'name  nh1')
cmd.select('temp41', 'name  nh2')
cmd.select('temp42', 'all within %s of (jessatom0)'%(d*7.554800))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom0))'%((1./d)*7.405941))
cmd.select('temp43', 'all within %s of (jessatom1)'%(d*8.989000))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom1))'%((1./d)*8.811881))
cmd.select('temp44', 'all within %s of (jessatom2)'%(d*9.635400))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom2))'%((1./d)*9.445545))
cmd.select('temp45', 'all within %s of (jessatom3)'%(d*8.201200))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom3))'%((1./d)*8.039604))
cmd.select('temp46', 'all within %s of (jessatom4)'%(d*9.261700))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom4))'%((1./d)*9.079208))
cmd.select('temp47', 'all within %s of (jessatom5)'%(d*7.059900))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom5))'%((1./d)*6.920792))
cmd.select('temp48', 'all within %s of (jessatom6)'%(d*2.333100))
cmd.select('temp48', 'temp48 and not (all within %s of (jessatom6))'%((1./d)*2.287129))
cmd.select('temp49', 'byres jessatom6')
cmd.select('jessatom7', '((temp40 or temp41) and temp33 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*7.554800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*7.405941))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.989000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*8.811881))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*9.635400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*9.445545))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*8.201200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*8.039604))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*9.261700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*9.079208))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.059900))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*6.920792))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*2.333100))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*2.287129))
cmd.select('temp50', 'name  nh2')
cmd.select('temp51', 'name  nh1')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*5.645900))
cmd.select('temp52', 'temp52 and not (all within %s of (jessatom0))'%((1./d)*5.534653))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*7.100300))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom1))'%((1./d)*6.960396))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*7.968900))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom2))'%((1./d)*7.811881))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*6.726600))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom3))'%((1./d)*6.594059))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*7.635600))
cmd.select('temp56', 'temp56 and not (all within %s of (jessatom4))'%((1./d)*7.485149))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*5.494400))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom5))'%((1./d)*5.386139))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*2.312900))
cmd.select('temp58', 'temp58 and not (all within %s of (jessatom6))'%((1./d)*2.267327))
cmd.select('temp59', 'byres jessatom6')
cmd.select('temp60', 'all within %s of (jessatom7)'%(d*2.323000))
cmd.select('temp60', 'temp60 and not (all within %s of (jessatom7))'%((1./d)*2.277228))
cmd.select('jessatom8', '((temp50 or temp51) and temp33 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*5.645900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*5.534653))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.100300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*6.960396))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*7.968900))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*7.811881))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*6.726600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*6.594059))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*7.635600))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*7.485149))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*5.494400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*5.386139))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.312900))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*2.267327))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.323000))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*2.277228))
cmd.select('temp61', 'all within %s of (jessatom0)'%(d*6.817500))
cmd.select('temp61', 'temp61 and not (all within %s of (jessatom0))'%((1./d)*6.683168))
cmd.select('temp62', 'all within %s of (jessatom1)'%(d*7.534600))
cmd.select('temp62', 'temp62 and not (all within %s of (jessatom1))'%((1./d)*7.386139))
cmd.select('temp63', 'all within %s of (jessatom2)'%(d*8.766800))
cmd.select('temp63', 'temp63 and not (all within %s of (jessatom2))'%((1./d)*8.594059))
cmd.select('temp64', 'all within %s of (jessatom3)'%(d*3.262300))
cmd.select('temp64', 'temp64 and not (all within %s of (jessatom3))'%((1./d)*3.198020))
cmd.select('temp65', 'all within %s of (jessatom4)'%(d*2.777500))
cmd.select('temp65', 'temp65 and not (all within %s of (jessatom4))'%((1./d)*2.722772))
cmd.select('temp66', 'all within %s of (jessatom5)'%(d*2.989600))
cmd.select('temp66', 'temp66 and not (all within %s of (jessatom5))'%((1./d)*2.930693))
cmd.select('temp67', 'all within %s of (jessatom6)'%(d*7.140700))
cmd.select('temp67', 'temp67 and not (all within %s of (jessatom6))'%((1./d)*7.000000))
cmd.select('temp68', 'all within %s of (jessatom7)'%(d*8.837500))
cmd.select('temp68', 'temp68 and not (all within %s of (jessatom7))'%((1./d)*8.663366))
cmd.select('temp69', 'all within %s of (jessatom8)'%(d*6.756900))
cmd.select('temp69', 'temp69 and not (all within %s of (jessatom8))'%((1./d)*6.623762))
cmd.select('jessatom9', '(temp32 and temp33 and temp61 and temp62 and temp63 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*6.817500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom9))'%((1./d)*6.683168))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*7.534600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom9))'%((1./d)*7.386139))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*8.766800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom9))'%((1./d)*8.594059))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*3.262300))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom9))'%((1./d)*3.198020))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*2.777500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom9))'%((1./d)*2.722772))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*2.989600))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom9))'%((1./d)*2.930693))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*7.140700))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom9))'%((1./d)*7.000000))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*8.837500))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom9))'%((1./d)*8.663366))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*6.756900))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom9))'%((1./d)*6.623762))
cmd.select('temp70', 'all within %s of (jessatom0)'%(d*4.666200))
cmd.select('temp70', 'temp70 and not (all within %s of (jessatom0))'%((1./d)*4.574257))
cmd.select('temp71', 'all within %s of (jessatom1)'%(d*5.241900))
cmd.select('temp71', 'temp71 and not (all within %s of (jessatom1))'%((1./d)*5.138614))
cmd.select('temp72', 'all within %s of (jessatom2)'%(d*6.494300))
cmd.select('temp72', 'temp72 and not (all within %s of (jessatom2))'%((1./d)*6.366337))
cmd.select('temp73', 'all within %s of (jessatom3)'%(d*5.161100))
cmd.select('temp73', 'temp73 and not (all within %s of (jessatom3))'%((1./d)*5.059406))
cmd.select('temp74', 'all within %s of (jessatom4)'%(d*4.888400))
cmd.select('temp74', 'temp74 and not (all within %s of (jessatom4))'%((1./d)*4.792079))
cmd.select('temp75', 'all within %s of (jessatom5)'%(d*4.504600))
cmd.select('temp75', 'temp75 and not (all within %s of (jessatom5))'%((1./d)*4.415842))
cmd.select('temp76', 'all within %s of (jessatom6)'%(d*7.332600))
cmd.select('temp76', 'temp76 and not (all within %s of (jessatom6))'%((1./d)*7.188119))
cmd.select('temp77', 'all within %s of (jessatom7)'%(d*8.504200))
cmd.select('temp77', 'temp77 and not (all within %s of (jessatom7))'%((1./d)*8.336634))
cmd.select('temp78', 'all within %s of (jessatom8)'%(d*6.241800))
cmd.select('temp78', 'temp78 and not (all within %s of (jessatom8))'%((1./d)*6.118812))
cmd.select('temp79', 'all within %s of (jessatom9)'%(d*2.333100))
cmd.select('temp79', 'temp79 and not (all within %s of (jessatom9))'%((1./d)*2.287129))
cmd.select('temp80', 'byres jessatom9')
cmd.select('jessatom10', '((temp40 or temp41) and temp33 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*4.666200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom10))'%((1./d)*4.574257))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*5.241900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom10))'%((1./d)*5.138614))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*6.494300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom10))'%((1./d)*6.366337))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*5.161100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom10))'%((1./d)*5.059406))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*4.888400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom10))'%((1./d)*4.792079))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*4.504600))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom10))'%((1./d)*4.415842))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*7.332600))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom10))'%((1./d)*7.188119))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*8.504200))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom10))'%((1./d)*8.336634))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*6.241800))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom10))'%((1./d)*6.118812))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*2.333100))
cmd.select('jessatom9', 'jessatom9 and not (all within %s of (jessatom10))'%((1./d)*2.287129))
cmd.select('temp81', 'all within %s of (jessatom0)'%(d*5.827700))
cmd.select('temp81', 'temp81 and not (all within %s of (jessatom0))'%((1./d)*5.712871))
cmd.select('temp82', 'all within %s of (jessatom1)'%(d*6.575100))
cmd.select('temp82', 'temp82 and not (all within %s of (jessatom1))'%((1./d)*6.445545))
cmd.select('temp83', 'all within %s of (jessatom2)'%(d*7.544700))
cmd.select('temp83', 'temp83 and not (all within %s of (jessatom2))'%((1./d)*7.396040))
cmd.select('temp84', 'all within %s of (jessatom3)'%(d*3.676400))
cmd.select('temp84', 'temp84 and not (all within %s of (jessatom3))'%((1./d)*3.603960))
cmd.select('temp85', 'all within %s of (jessatom4)'%(d*3.494600))
cmd.select('temp85', 'temp85 and not (all within %s of (jessatom4))'%((1./d)*3.425743))
cmd.select('temp86', 'all within %s of (jessatom5)'%(d*3.201700))
cmd.select('temp86', 'temp86 and not (all within %s of (jessatom5))'%((1./d)*3.138614))
cmd.select('temp87', 'all within %s of (jessatom6)'%(d*6.645800))
cmd.select('temp87', 'temp87 and not (all within %s of (jessatom6))'%((1./d)*6.514851))
cmd.select('temp88', 'all within %s of (jessatom7)'%(d*8.130500))
cmd.select('temp88', 'temp88 and not (all within %s of (jessatom7))'%((1./d)*7.970297))
cmd.select('temp89', 'all within %s of (jessatom8)'%(d*6.140800))
cmd.select('temp89', 'temp89 and not (all within %s of (jessatom8))'%((1./d)*6.019802))
cmd.select('temp90', 'all within %s of (jessatom9)'%(d*2.302800))
cmd.select('temp90', 'temp90 and not (all within %s of (jessatom9))'%((1./d)*2.257426))
cmd.select('temp91', 'byres jessatom9')
cmd.select('temp92', 'all within %s of (jessatom10)'%(d*2.312900))
cmd.select('temp92', 'temp92 and not (all within %s of (jessatom10))'%((1./d)*2.267327))
cmd.select('jessatom11', '((temp50 or temp51) and temp33 and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp90 and temp91 and temp92)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*5.827700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom11))'%((1./d)*5.712871))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*6.575100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom11))'%((1./d)*6.445545))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*7.544700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom11))'%((1./d)*7.396040))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*3.676400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom11))'%((1./d)*3.603960))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*3.494600))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom11))'%((1./d)*3.425743))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*3.201700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom11))'%((1./d)*3.138614))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*6.645800))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom11))'%((1./d)*6.514851))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*8.130500))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom11))'%((1./d)*7.970297))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*6.140800))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom11))'%((1./d)*6.019802))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.302800))
cmd.select('jessatom9', 'jessatom9 and not (all within %s of (jessatom11))'%((1./d)*2.257426))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.312900))
cmd.select('jessatom10', 'jessatom10 and not (all within %s of (jessatom11))'%((1./d)*2.267327))
cmd.select('Jfa_1e2m_2_7_1_21', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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
cmd.delete('temp84')
cmd.delete('temp85')
cmd.delete('temp86')
cmd.delete('temp87')
cmd.delete('temp88')
cmd.delete('temp89')
cmd.delete('temp90')
cmd.delete('temp91')
cmd.delete('temp92')