'''
FUNC:Jfa_5mdh_1_1_1_37
PDB:5mdh
EC:1.1.1.37
RESI:asp,asn
LOCI:a-158,185;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  od1')
cmd.select('temp4', 'name  od2')
cmd.select('temp5', 'name  oe1')
cmd.select('temp6', 'name  oe2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.272600))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*1.247525))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.272600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.247525))
cmd.select('temp9', 'name  od2')
cmd.select('temp10', 'name  od1')
cmd.select('temp11', 'name  oe2')
cmd.select('temp12', 'name  oe1')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*1.262500))
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*1.237624))
cmd.select('temp14', 'byres jessatom0')
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*2.222000))
cmd.select('temp15', 'temp15 and not within %s of (jessatom1)'%((1./d)*2.178218))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*1.237624))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*2.178218))
cmd.select('temp16', 'name  ne ')
cmd.select('temp17', 'resn arg')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*6.251900))
cmd.select('temp18', 'temp18 and not within %s of (jessatom0)'%((1./d)*6.128713))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*5.363100))
cmd.select('temp19', 'temp19 and not within %s of (jessatom1)'%((1./d)*5.257426))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*7.352800))
cmd.select('temp20', 'temp20 and not within %s of (jessatom2)'%((1./d)*7.207921))
cmd.select('jessatom3', '(temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*6.251900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*6.128713))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.363100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*5.257426))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*7.352800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*7.207921))
cmd.select('temp21', 'name  nh1')
cmd.select('temp22', 'name  nh2')
cmd.select('temp23', 'all within %s of (jessatom0)'%(d*4.959100))
cmd.select('temp23', 'temp23 and not within %s of (jessatom0)'%((1./d)*4.861386))
cmd.select('temp24', 'all within %s of (jessatom1)'%(d*3.817800))
cmd.select('temp24', 'temp24 and not within %s of (jessatom1)'%((1./d)*3.742574))
cmd.select('temp25', 'all within %s of (jessatom2)'%(d*5.878200))
cmd.select('temp25', 'temp25 and not within %s of (jessatom2)'%((1./d)*5.762376))
cmd.select('temp26', 'all within %s of (jessatom3)'%(d*2.363400))
cmd.select('temp26', 'temp26 and not within %s of (jessatom3)'%((1./d)*2.316832))
cmd.select('temp27', 'byres jessatom3')
cmd.select('jessatom4', '((temp21 or temp22) and temp17 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.959100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*4.861386))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*3.817800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*3.742574))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*5.878200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*5.762376))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*2.363400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*2.316832))
cmd.select('temp28', 'name  nh2')
cmd.select('temp29', 'name  nh1')
cmd.select('temp30', 'all within %s of (jessatom0)'%(d*7.201300))
cmd.select('temp30', 'temp30 and not within %s of (jessatom0)'%((1./d)*7.059406))
cmd.select('temp31', 'all within %s of (jessatom1)'%(d*6.130700))
cmd.select('temp31', 'temp31 and not within %s of (jessatom1)'%((1./d)*6.009901))
cmd.select('temp32', 'all within %s of (jessatom2)'%(d*8.100200))
cmd.select('temp32', 'temp32 and not within %s of (jessatom2)'%((1./d)*7.940594))
cmd.select('temp33', 'all within %s of (jessatom3)'%(d*2.302800))
cmd.select('temp33', 'temp33 and not within %s of (jessatom3)'%((1./d)*2.257426))
cmd.select('temp34', 'byres jessatom3')
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*2.353300))
cmd.select('temp35', 'temp35 and not within %s of (jessatom4)'%((1./d)*2.306931))
cmd.select('jessatom5', '((temp28 or temp29) and temp17 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.201300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*7.059406))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*6.130700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*6.009901))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*8.100200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*7.940594))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.302800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.257426))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.353300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.306931))
cmd.select('temp36', 'resn his')
cmd.select('temp37', 'all within %s of (jessatom0)'%(d*4.676300))
cmd.select('temp37', 'temp37 and not within %s of (jessatom0)'%((1./d)*4.584158))
cmd.select('temp38', 'all within %s of (jessatom1)'%(d*4.666200))
cmd.select('temp38', 'temp38 and not within %s of (jessatom1)'%((1./d)*4.574257))
cmd.select('temp39', 'all within %s of (jessatom2)'%(d*3.817800))
cmd.select('temp39', 'temp39 and not within %s of (jessatom2)'%((1./d)*3.742574))
cmd.select('temp40', 'all within %s of (jessatom3)'%(d*9.009200))
cmd.select('temp40', 'temp40 and not within %s of (jessatom3)'%((1./d)*8.831683))
cmd.select('temp41', 'all within %s of (jessatom4)'%(d*6.908400))
cmd.select('temp41', 'temp41 and not within %s of (jessatom4)'%((1./d)*6.772277))
cmd.select('temp42', 'all within %s of (jessatom5)'%(d*8.746600))
cmd.select('temp42', 'temp42 and not within %s of (jessatom5)'%((1./d)*8.574257))
cmd.select('jessatom6', '(temp0 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41 and temp42)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*4.676300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*4.584158))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*4.666200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*4.574257))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*3.817800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*3.742574))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*9.009200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*8.831683))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.908400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*6.772277))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.746600))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*8.574257))
cmd.select('temp43', 'name  nd1')
cmd.select('temp44', 'all within %s of (jessatom0)'%(d*3.312800))
cmd.select('temp44', 'temp44 and not within %s of (jessatom0)'%((1./d)*3.247525))
cmd.select('temp45', 'all within %s of (jessatom1)'%(d*3.272400))
cmd.select('temp45', 'temp45 and not within %s of (jessatom1)'%((1./d)*3.207921))
cmd.select('temp46', 'all within %s of (jessatom2)'%(d*2.595700))
cmd.select('temp46', 'temp46 and not within %s of (jessatom2)'%((1./d)*2.544554))
cmd.select('temp47', 'all within %s of (jessatom3)'%(d*7.817400))
cmd.select('temp47', 'temp47 and not within %s of (jessatom3)'%((1./d)*7.663366))
cmd.select('temp48', 'all within %s of (jessatom4)'%(d*5.807500))
cmd.select('temp48', 'temp48 and not within %s of (jessatom4)'%((1./d)*5.693069))
cmd.select('temp49', 'all within %s of (jessatom5)'%(d*7.797200))
cmd.select('temp49', 'temp49 and not within %s of (jessatom5)'%((1./d)*7.643564))
cmd.select('temp50', 'all within %s of (jessatom6)'%(d*1.403900))
cmd.select('temp50', 'temp50 and not within %s of (jessatom6)'%((1./d)*1.376238))
cmd.select('temp51', 'byres jessatom6')
cmd.select('jessatom7', '(temp43 and temp36 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50 and temp51)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*3.312800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*3.247525))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*3.272400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*3.207921))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*2.595700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*2.544554))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.817400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*7.663366))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.807500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*5.693069))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.797200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*7.643564))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.403900))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.376238))
cmd.select('temp52', 'name  ne2')
cmd.select('temp53', 'all within %s of (jessatom0)'%(d*4.837900))
cmd.select('temp53', 'temp53 and not within %s of (jessatom0)'%((1./d)*4.742574))
cmd.select('temp54', 'all within %s of (jessatom1)'%(d*4.353100))
cmd.select('temp54', 'temp54 and not within %s of (jessatom1)'%((1./d)*4.267327))
cmd.select('temp55', 'all within %s of (jessatom2)'%(d*4.484400))
cmd.select('temp55', 'temp55 and not within %s of (jessatom2)'%((1./d)*4.396040))
cmd.select('temp56', 'all within %s of (jessatom3)'%(d*7.494200))
cmd.select('temp56', 'temp56 and not within %s of (jessatom3)'%((1./d)*7.346535))
cmd.select('temp57', 'all within %s of (jessatom4)'%(d*5.332800))
cmd.select('temp57', 'temp57 and not within %s of (jessatom4)'%((1./d)*5.227723))
cmd.select('temp58', 'all within %s of (jessatom5)'%(d*6.857900))
cmd.select('temp58', 'temp58 and not within %s of (jessatom5)'%((1./d)*6.722772))
cmd.select('temp59', 'all within %s of (jessatom6)'%(d*2.171500))
cmd.select('temp59', 'temp59 and not within %s of (jessatom6)'%((1./d)*2.128713))
cmd.select('temp60', 'byres jessatom6')
cmd.select('temp61', 'all within %s of (jessatom7)'%(d*2.141200))
cmd.select('temp61', 'temp61 and not within %s of (jessatom7)'%((1./d)*2.099010))
cmd.select('jessatom8', '(temp52 and temp36 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*4.837900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*4.742574))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*4.353100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*4.267327))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*4.484400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*4.396040))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.494200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*7.346535))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*5.332800))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*5.227723))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*6.857900))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*6.722772))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.171500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*2.128713))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.141200))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.099010))
cmd.select('Jfa_5mdh_1_1_1_37', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
cmd.delete('temp61')
