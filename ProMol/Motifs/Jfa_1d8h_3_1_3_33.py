'''
FUNC:Jfa_1d8h_3_1_3_33
PDB:1d8h
EC:3.1.3.33
RESI:arg,glu,lys,arg
LOCI:a-393,433,456,458;
'''
cmd.select('temp0', 'name  ne ')
cmd.select('temp1', 'resn arg')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nh1')
cmd.select('temp3', 'name  nh2')
cmd.select('temp4', 'resn arg')
cmd.select('temp5', 'all within %s of (jessatom0)'%(d*2.323000))
cmd.select('temp5', 'temp5 and not within %s of (jessatom0)'%((1./d)*2.277228))
cmd.select('temp6', 'byres jessatom0')
cmd.select('jessatom1', '((temp2 or temp3) and temp4 and temp5 and temp6)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*2.323000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*2.277228))
cmd.select('temp7', 'name  nh2')
cmd.select('temp8', 'name  nh1')
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*2.353300))
cmd.select('temp9', 'temp9 and not within %s of (jessatom0)'%((1./d)*2.306931))
cmd.select('temp10', 'byres jessatom0')
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*2.363400))
cmd.select('temp11', 'temp11 and not within %s of (jessatom1)'%((1./d)*2.316832))
cmd.select('jessatom2', '((temp7 or temp8) and temp4 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.353300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*2.306931))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.363400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*2.316832))
cmd.select('temp12', 'name  cd ')
cmd.select('temp13', 'resn glu')
cmd.select('temp14', 'resn asp')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*6.918500))
cmd.select('temp15', 'temp15 and not within %s of (jessatom0)'%((1./d)*6.782178))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*6.231700))
cmd.select('temp16', 'temp16 and not within %s of (jessatom1)'%((1./d)*6.108911))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*5.161100))
cmd.select('temp17', 'temp17 and not within %s of (jessatom2)'%((1./d)*5.059406))
cmd.select('jessatom3', '(((temp12 and temp13) or (temp12 and temp14)) and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*6.918500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*6.782178))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.231700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*6.108911))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*5.161100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*5.059406))
cmd.select('temp18', 'name  oe1')
cmd.select('temp19', 'name  oe2')
cmd.select('temp20', 'name  od1')
cmd.select('temp21', 'name  od2')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*6.322600))
cmd.select('temp22', 'temp22 and not within %s of (jessatom0)'%((1./d)*6.198020))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*5.292400))
cmd.select('temp23', 'temp23 and not within %s of (jessatom1)'%((1./d)*5.188119))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*4.454100))
cmd.select('temp24', 'temp24 and not within %s of (jessatom2)'%((1./d)*4.366337))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*1.282700))
cmd.select('temp25', 'temp25 and not within %s of (jessatom3)'%((1./d)*1.257426))
cmd.select('temp26', 'byres jessatom3')
cmd.select('jessatom4', '((((temp18 or temp19) and temp13) or ((temp20 or temp21) and temp14)) and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*6.322600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*6.198020))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*5.292400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*5.188119))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.454100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*4.366337))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.282700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.257426))
cmd.select('temp27', 'name  oe2')
cmd.select('temp28', 'name  oe1')
cmd.select('temp29', 'name  od2')
cmd.select('temp30', 'name  od1')
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*7.847700))
cmd.select('temp31', 'temp31 and not within %s of (jessatom0)'%((1./d)*7.693069))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*7.292200))
cmd.select('temp32', 'temp32 and not within %s of (jessatom1)'%((1./d)*7.148515))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*5.959000))
cmd.select('temp33', 'temp33 and not within %s of (jessatom2)'%((1./d)*5.841584))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*1.252400))
cmd.select('temp34', 'temp34 and not within %s of (jessatom3)'%((1./d)*1.227723))
cmd.select('temp35', 'byres jessatom3')
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*2.272500))
cmd.select('temp36', 'temp36 and not within %s of (jessatom4)'%((1./d)*2.227723))
cmd.select('jessatom5', '((((temp27 or temp28) and temp13) or ((temp29 or temp30) and temp14)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.847700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*7.693069))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.292200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*7.148515))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*5.959000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*5.841584))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.252400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*1.227723))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.272500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.227723))
cmd.select('temp37', 'resn lys')
cmd.select('temp38', 'all within %s of (jessatom0)'%(d*6.706400))
cmd.select('temp38', 'temp38 and not within %s of (jessatom0)'%((1./d)*6.574257))
cmd.select('temp39', 'all within %s of (jessatom1)'%(d*5.878200))
cmd.select('temp39', 'temp39 and not within %s of (jessatom1)'%((1./d)*5.762376))
cmd.select('temp40', 'all within %s of (jessatom2)'%(d*6.898300))
cmd.select('temp40', 'temp40 and not within %s of (jessatom2)'%((1./d)*6.762376))
cmd.select('temp41', 'all within %s of (jessatom3)'%(d*11.271600))
cmd.select('temp41', 'temp41 and not within %s of (jessatom3)'%((1./d)*11.049505))
cmd.select('temp42', 'all within %s of (jessatom4)'%(d*10.140400))
cmd.select('temp42', 'temp42 and not within %s of (jessatom4)'%((1./d)*9.940594))
cmd.select('temp43', 'all within %s of (jessatom5)'%(d*12.089700))
cmd.select('temp43', 'temp43 and not within %s of (jessatom5)'%((1./d)*11.851485))
cmd.select('jessatom6', '(temp12 and temp37 and temp38 and temp39 and temp40 and temp41 and temp42 and temp43)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*6.706400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*6.574257))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*5.878200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*5.762376))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*6.898300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*6.762376))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*11.271600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*11.049505))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*10.140400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*9.940594))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*12.089700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*11.851485))
cmd.select('temp44', 'name  ce ')
cmd.select('temp45', 'all within %s of (jessatom0)'%(d*6.575100))
cmd.select('temp45', 'temp45 and not within %s of (jessatom0)'%((1./d)*6.445545))
cmd.select('temp46', 'all within %s of (jessatom1)'%(d*5.272200))
cmd.select('temp46', 'temp46 and not within %s of (jessatom1)'%((1./d)*5.168317))
cmd.select('temp47', 'all within %s of (jessatom2)'%(d*6.393300))
cmd.select('temp47', 'temp47 and not within %s of (jessatom2)'%((1./d)*6.267327))
cmd.select('temp48', 'all within %s of (jessatom3)'%(d*10.291900))
cmd.select('temp48', 'temp48 and not within %s of (jessatom3)'%((1./d)*10.089109))
cmd.select('temp49', 'all within %s of (jessatom4)'%(d*9.100100))
cmd.select('temp49', 'temp49 and not within %s of (jessatom4)'%((1./d)*8.920792))
cmd.select('temp50', 'all within %s of (jessatom5)'%(d*11.099900))
cmd.select('temp50', 'temp50 and not within %s of (jessatom5)'%((1./d)*10.881188))
cmd.select('temp51', 'all within %s of (jessatom6)'%(d*1.525100))
cmd.select('temp51', 'temp51 and not within %s of (jessatom6)'%((1./d)*1.495050))
cmd.select('temp52', 'byres jessatom6')
cmd.select('jessatom7', '(temp44 and temp37 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50 and temp51 and temp52)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*6.575100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*6.445545))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*5.272200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*5.168317))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*6.393300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*6.267327))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*10.291900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*10.089109))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*9.100100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*8.920792))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*11.099900))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*10.881188))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.525100))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.495050))
cmd.select('temp53', 'name  nz ')
cmd.select('temp54', 'all within %s of (jessatom0)'%(d*6.938700))
cmd.select('temp54', 'temp54 and not within %s of (jessatom0)'%((1./d)*6.801980))
cmd.select('temp55', 'all within %s of (jessatom1)'%(d*5.686300))
cmd.select('temp55', 'temp55 and not within %s of (jessatom1)'%((1./d)*5.574257))
cmd.select('temp56', 'all within %s of (jessatom2)'%(d*6.292300))
cmd.select('temp56', 'temp56 and not within %s of (jessatom2)'%((1./d)*6.168317))
cmd.select('temp57', 'all within %s of (jessatom3)'%(d*9.958600))
cmd.select('temp57', 'temp57 and not within %s of (jessatom3)'%((1./d)*9.762376))
cmd.select('temp58', 'all within %s of (jessatom4)'%(d*8.776900))
cmd.select('temp58', 'temp58 and not within %s of (jessatom4)'%((1./d)*8.603960))
cmd.select('temp59', 'all within %s of (jessatom5)'%(d*10.635300))
cmd.select('temp59', 'temp59 and not within %s of (jessatom5)'%((1./d)*10.425743))
cmd.select('temp60', 'all within %s of (jessatom6)'%(d*2.444200))
cmd.select('temp60', 'temp60 and not within %s of (jessatom6)'%((1./d)*2.396040))
cmd.select('temp61', 'byres jessatom6')
cmd.select('temp62', 'all within %s of (jessatom7)'%(d*1.515000))
cmd.select('temp62', 'temp62 and not within %s of (jessatom7)'%((1./d)*1.485149))
cmd.select('jessatom8', '(temp53 and temp37 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61 and temp62)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.938700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*6.801980))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*5.686300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*5.574257))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*6.292300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*6.168317))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*9.958600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*9.762376))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*8.776900))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*8.603960))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*10.635300))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*10.425743))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.444200))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*2.396040))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.515000))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*1.485149))
cmd.select('temp63', 'all within %s of (jessatom0)'%(d*10.150500))
cmd.select('temp63', 'temp63 and not within %s of (jessatom0)'%((1./d)*9.950495))
cmd.select('temp64', 'all within %s of (jessatom1)'%(d*8.494100))
cmd.select('temp64', 'temp64 and not within %s of (jessatom1)'%((1./d)*8.326733))
cmd.select('temp65', 'all within %s of (jessatom2)'%(d*8.908200))
cmd.select('temp65', 'temp65 and not within %s of (jessatom2)'%((1./d)*8.732673))
cmd.select('temp66', 'all within %s of (jessatom3)'%(d*11.009000))
cmd.select('temp66', 'temp66 and not within %s of (jessatom3)'%((1./d)*10.792079))
cmd.select('temp67', 'all within %s of (jessatom4)'%(d*9.807100))
cmd.select('temp67', 'temp67 and not within %s of (jessatom4)'%((1./d)*9.613861))
cmd.select('temp68', 'all within %s of (jessatom5)'%(d*11.463500))
cmd.select('temp68', 'temp68 and not within %s of (jessatom5)'%((1./d)*11.237624))
cmd.select('temp69', 'all within %s of (jessatom6)'%(d*5.938800))
cmd.select('temp69', 'temp69 and not within %s of (jessatom6)'%((1./d)*5.821782))
cmd.select('temp70', 'all within %s of (jessatom7)'%(d*4.848000))
cmd.select('temp70', 'temp70 and not within %s of (jessatom7)'%((1./d)*4.752475))
cmd.select('temp71', 'all within %s of (jessatom8)'%(d*3.817800))
cmd.select('temp71', 'temp71 and not within %s of (jessatom8)'%((1./d)*3.742574))
cmd.select('jessatom9', '(temp0 and temp4 and temp63 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69 and temp70 and temp71)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*10.150500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom9)'%((1./d)*9.950495))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*8.494100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom9)'%((1./d)*8.326733))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*8.908200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom9)'%((1./d)*8.732673))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*11.009000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom9)'%((1./d)*10.792079))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*9.807100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom9)'%((1./d)*9.613861))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*11.463500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom9)'%((1./d)*11.237624))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*5.938800))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom9)'%((1./d)*5.821782))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*4.848000))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom9)'%((1./d)*4.752475))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*3.817800))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom9)'%((1./d)*3.742574))
cmd.select('temp72', 'all within %s of (jessatom0)'%(d*8.504200))
cmd.select('temp72', 'temp72 and not within %s of (jessatom0)'%((1./d)*8.336634))
cmd.select('temp73', 'all within %s of (jessatom1)'%(d*6.857900))
cmd.select('temp73', 'temp73 and not within %s of (jessatom1)'%((1./d)*6.722772))
cmd.select('temp74', 'all within %s of (jessatom2)'%(d*6.969000))
cmd.select('temp74', 'temp74 and not within %s of (jessatom2)'%((1./d)*6.831683))
cmd.select('temp75', 'all within %s of (jessatom3)'%(d*8.817300))
cmd.select('temp75', 'temp75 and not within %s of (jessatom3)'%((1./d)*8.643564))
cmd.select('temp76', 'all within %s of (jessatom4)'%(d*7.645700))
cmd.select('temp76', 'temp76 and not within %s of (jessatom4)'%((1./d)*7.495050))
cmd.select('temp77', 'all within %s of (jessatom5)'%(d*9.261700))
cmd.select('temp77', 'temp77 and not within %s of (jessatom5)'%((1./d)*9.079208))
cmd.select('temp78', 'all within %s of (jessatom6)'%(d*5.847900))
cmd.select('temp78', 'temp78 and not within %s of (jessatom6)'%((1./d)*5.732673))
cmd.select('temp79', 'all within %s of (jessatom7)'%(d*4.595500))
cmd.select('temp79', 'temp79 and not within %s of (jessatom7)'%((1./d)*4.504950))
cmd.select('temp80', 'all within %s of (jessatom8)'%(d*3.434000))
cmd.select('temp80', 'temp80 and not within %s of (jessatom8)'%((1./d)*3.366337))
cmd.select('temp81', 'all within %s of (jessatom9)'%(d*2.232100))
cmd.select('temp81', 'temp81 and not within %s of (jessatom9)'%((1./d)*2.188119))
cmd.select('temp82', 'byres jessatom9')
cmd.select('jessatom10', '((temp2 or temp3) and temp4 and temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80 and temp81 and temp82)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*8.504200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom10)'%((1./d)*8.336634))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*6.857900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom10)'%((1./d)*6.722772))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*6.969000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom10)'%((1./d)*6.831683))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*8.817300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom10)'%((1./d)*8.643564))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*7.645700))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom10)'%((1./d)*7.495050))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*9.261700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom10)'%((1./d)*9.079208))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*5.847900))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom10)'%((1./d)*5.732673))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*4.595500))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom10)'%((1./d)*4.504950))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*3.434000))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom10)'%((1./d)*3.366337))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*2.232100))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom10)'%((1./d)*2.188119))
cmd.select('temp83', 'all within %s of (jessatom0)'%(d*8.251700))
cmd.select('temp83', 'temp83 and not within %s of (jessatom0)'%((1./d)*8.089109))
cmd.select('temp84', 'all within %s of (jessatom1)'%(d*6.393300))
cmd.select('temp84', 'temp84 and not within %s of (jessatom1)'%((1./d)*6.267327))
cmd.select('temp85', 'all within %s of (jessatom2)'%(d*7.251800))
cmd.select('temp85', 'temp85 and not within %s of (jessatom2)'%((1./d)*7.108911))
cmd.select('temp86', 'all within %s of (jessatom3)'%(d*9.635400))
cmd.select('temp86', 'temp86 and not within %s of (jessatom3)'%((1./d)*9.445545))
cmd.select('temp87', 'all within %s of (jessatom4)'%(d*8.372900))
cmd.select('temp87', 'temp87 and not within %s of (jessatom4)'%((1./d)*8.207921))
cmd.select('temp88', 'all within %s of (jessatom5)'%(d*10.312100))
cmd.select('temp88', 'temp88 and not within %s of (jessatom5)'%((1./d)*10.108911))
cmd.select('temp89', 'all within %s of (jessatom6)'%(d*4.595500))
cmd.select('temp89', 'temp89 and not within %s of (jessatom6)'%((1./d)*4.504950))
cmd.select('temp90', 'all within %s of (jessatom7)'%(d*3.171400))
cmd.select('temp90', 'temp90 and not within %s of (jessatom7)'%((1./d)*3.108911))
cmd.select('temp91', 'all within %s of (jessatom8)'%(d*2.676500))
cmd.select('temp91', 'temp91 and not within %s of (jessatom8)'%((1./d)*2.623762))
cmd.select('temp92', 'all within %s of (jessatom9)'%(d*2.444200))
cmd.select('temp92', 'temp92 and not within %s of (jessatom9)'%((1./d)*2.396040))
cmd.select('temp93', 'byres jessatom9')
cmd.select('temp94', 'all within %s of (jessatom10)'%(d*2.272500))
cmd.select('temp94', 'temp94 and not within %s of (jessatom10)'%((1./d)*2.227723))
cmd.select('jessatom11', '((temp7 or temp8) and temp4 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp90 and temp91 and temp92 and temp93 and temp94)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*8.251700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom11)'%((1./d)*8.089109))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*6.393300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom11)'%((1./d)*6.267327))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*7.251800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom11)'%((1./d)*7.108911))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*9.635400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom11)'%((1./d)*9.445545))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*8.372900))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom11)'%((1./d)*8.207921))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*10.312100))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom11)'%((1./d)*10.108911))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*4.595500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom11)'%((1./d)*4.504950))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*3.171400))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom11)'%((1./d)*3.108911))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*2.676500))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom11)'%((1./d)*2.623762))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.444200))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom11)'%((1./d)*2.396040))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.272500))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom11)'%((1./d)*2.227723))
cmd.select('Jfa_1d8h_3_1_3_33', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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
cmd.delete('temp93')
cmd.delete('temp94')
