'''
FUNC:Jab_1hmp_2_4_2_8
PDB:1hmp
EC:2.4.2.8
RESI:glu,asp,asp,lys,arg
LOCI:a-133,134,137,165,169;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.565500))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.534653))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.565500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.534653))
cmd.select('temp6', 'all within %s of (jessatom0)'%(d*3.706700))
cmd.select('temp6', 'temp6 and not within %s of (jessatom0)'%((1./d)*3.633663))
cmd.select('temp7', 'all within %s of (jessatom1)'%(d*4.312700))
cmd.select('temp7', 'temp7 and not within %s of (jessatom1)'%((1./d)*4.227723))
cmd.select('jessatom2', '(((temp0 and temp2) or (temp0 and temp1)) and temp6 and temp7)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*3.706700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*3.633663))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*4.312700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*4.227723))
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*4.706600))
cmd.select('temp8', 'temp8 and not within %s of (jessatom0)'%((1./d)*4.613861))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*5.383300))
cmd.select('temp9', 'temp9 and not within %s of (jessatom1)'%((1./d)*5.277228))
cmd.select('temp10', 'all within %s of (jessatom2)'%(d*1.535200))
cmd.select('temp10', 'temp10 and not within %s of (jessatom2)'%((1./d)*1.504950))
cmd.select('temp11', 'byres jessatom2')
cmd.select('jessatom3', '(((temp3 and temp2) or (temp3 and temp1)) and temp8 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.706600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*4.613861))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.383300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*5.277228))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.535200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*1.504950))
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*10.827200))
cmd.select('temp12', 'temp12 and not within %s of (jessatom0)'%((1./d)*10.613861))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*9.595000))
cmd.select('temp13', 'temp13 and not within %s of (jessatom1)'%((1./d)*9.405941))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*9.958600))
cmd.select('temp14', 'temp14 and not within %s of (jessatom2)'%((1./d)*9.762376))
cmd.select('temp15', 'all within %s of (jessatom3)'%(d*10.554500))
cmd.select('temp15', 'temp15 and not within %s of (jessatom3)'%((1./d)*10.346535))
cmd.select('jessatom4', '(((temp0 and temp2) or (temp0 and temp1)) and temp12 and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*10.827200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*10.613861))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.595000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*9.405941))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*9.958600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*9.762376))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*10.554500))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*10.346535))
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*11.099900))
cmd.select('temp16', 'temp16 and not within %s of (jessatom0)'%((1./d)*10.881188))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*9.908100))
cmd.select('temp17', 'temp17 and not within %s of (jessatom1)'%((1./d)*9.712871))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*10.059600))
cmd.select('temp18', 'temp18 and not within %s of (jessatom2)'%((1./d)*9.861386))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*10.433300))
cmd.select('temp19', 'temp19 and not within %s of (jessatom3)'%((1./d)*10.227723))
cmd.select('temp20', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp20', 'temp20 and not within %s of (jessatom4)'%((1./d)*1.524752))
cmd.select('temp21', 'byres jessatom4')
cmd.select('jessatom5', '(((temp3 and temp2) or (temp3 and temp1)) and temp16 and temp17 and temp18 and temp19 and temp20 and temp21)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.099900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*10.881188))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*9.908100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*9.712871))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*10.059600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*9.861386))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*10.433300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*10.227723))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.524752))
cmd.select('temp22', 'resn lys')
cmd.select('temp23', 'all within %s of (jessatom0)'%(d*12.988600))
cmd.select('temp23', 'temp23 and not within %s of (jessatom0)'%((1./d)*12.732673))
cmd.select('temp24', 'all within %s of (jessatom1)'%(d*12.170500))
cmd.select('temp24', 'temp24 and not within %s of (jessatom1)'%((1./d)*11.930693))
cmd.select('temp25', 'all within %s of (jessatom2)'%(d*11.261500))
cmd.select('temp25', 'temp25 and not within %s of (jessatom2)'%((1./d)*11.039604))
cmd.select('temp26', 'all within %s of (jessatom3)'%(d*12.029100))
cmd.select('temp26', 'temp26 and not within %s of (jessatom3)'%((1./d)*11.792079))
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*5.807500))
cmd.select('temp27', 'temp27 and not within %s of (jessatom4)'%((1./d)*5.693069))
cmd.select('temp28', 'all within %s of (jessatom5)'%(d*6.837700))
cmd.select('temp28', 'temp28 and not within %s of (jessatom5)'%((1./d)*6.702970))
cmd.select('jessatom6', '(temp0 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27 and temp28)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*12.988600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*12.732673))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*12.170500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*11.930693))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*11.261500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*11.039604))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*12.029100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*11.792079))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*5.807500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*5.693069))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*6.837700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*6.702970))
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*13.079500))
cmd.select('temp29', 'temp29 and not within %s of (jessatom0)'%((1./d)*12.821782))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*12.200800))
cmd.select('temp30', 'temp30 and not within %s of (jessatom1)'%((1./d)*11.960396))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*11.312000))
cmd.select('temp31', 'temp31 and not within %s of (jessatom2)'%((1./d)*11.089109))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*11.948300))
cmd.select('temp32', 'temp32 and not within %s of (jessatom3)'%((1./d)*11.712871))
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*4.817700))
cmd.select('temp33', 'temp33 and not within %s of (jessatom4)'%((1./d)*4.722772))
cmd.select('temp34', 'all within %s of (jessatom5)'%(d*5.666100))
cmd.select('temp34', 'temp34 and not within %s of (jessatom5)'%((1./d)*5.554455))
cmd.select('temp35', 'all within %s of (jessatom6)'%(d*1.515000))
cmd.select('temp35', 'temp35 and not within %s of (jessatom6)'%((1./d)*1.485149))
cmd.select('temp36', 'byres jessatom6')
cmd.select('jessatom7', '(temp3 and temp22 and temp29 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*13.079500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*12.821782))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*12.200800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*11.960396))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*11.312000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*11.089109))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*11.948300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*11.712871))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*4.817700))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*4.722772))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*5.666100))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*5.554455))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.515000))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.485149))
cmd.select('temp37', 'resn arg')
cmd.select('temp38', 'all within %s of (jessatom0)'%(d*18.250700))
cmd.select('temp38', 'temp38 and not within %s of (jessatom0)'%((1./d)*17.891089))
cmd.select('temp39', 'all within %s of (jessatom1)'%(d*16.856900))
cmd.select('temp39', 'temp39 and not within %s of (jessatom1)'%((1./d)*16.524752))
cmd.select('temp40', 'all within %s of (jessatom2)'%(d*17.786100))
cmd.select('temp40', 'temp40 and not within %s of (jessatom2)'%((1./d)*17.435644))
cmd.select('temp41', 'all within %s of (jessatom3)'%(d*18.412300))
cmd.select('temp41', 'temp41 and not within %s of (jessatom3)'%((1./d)*18.049505))
cmd.select('temp42', 'all within %s of (jessatom4)'%(d*7.857800))
cmd.select('temp42', 'temp42 and not within %s of (jessatom4)'%((1./d)*7.702970))
cmd.select('temp43', 'all within %s of (jessatom5)'%(d*8.201200))
cmd.select('temp43', 'temp43 and not within %s of (jessatom5)'%((1./d)*8.039604))
cmd.select('temp44', 'all within %s of (jessatom6)'%(d*9.857600))
cmd.select('temp44', 'temp44 and not within %s of (jessatom6)'%((1./d)*9.663366))
cmd.select('temp45', 'all within %s of (jessatom7)'%(d*8.938500))
cmd.select('temp45', 'temp45 and not within %s of (jessatom7)'%((1./d)*8.762376))
cmd.select('jessatom8', '(temp0 and temp37 and temp38 and temp39 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*18.250700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*17.891089))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*16.856900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*16.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*17.786100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*17.435644))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*18.412300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*18.049505))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*7.857800))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*7.702970))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*8.201200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*8.039604))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*9.857600))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*9.663366))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*8.938500))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*8.762376))
cmd.select('temp46', 'all within %s of (jessatom0)'%(d*17.887100))
cmd.select('temp46', 'temp46 and not within %s of (jessatom0)'%((1./d)*17.534653))
cmd.select('temp47', 'all within %s of (jessatom1)'%(d*16.523600))
cmd.select('temp47', 'temp47 and not within %s of (jessatom1)'%((1./d)*16.198020))
cmd.select('temp48', 'all within %s of (jessatom2)'%(d*17.230600))
cmd.select('temp48', 'temp48 and not within %s of (jessatom2)'%((1./d)*16.891089))
cmd.select('temp49', 'all within %s of (jessatom3)'%(d*17.745700))
cmd.select('temp49', 'temp49 and not within %s of (jessatom3)'%((1./d)*17.396040))
cmd.select('temp50', 'all within %s of (jessatom4)'%(d*7.282100))
cmd.select('temp50', 'temp50 and not within %s of (jessatom4)'%((1./d)*7.138614))
cmd.select('temp51', 'all within %s of (jessatom5)'%(d*7.373000))
cmd.select('temp51', 'temp51 and not within %s of (jessatom5)'%((1./d)*7.227723))
cmd.select('temp52', 'all within %s of (jessatom6)'%(d*9.655600))
cmd.select('temp52', 'temp52 and not within %s of (jessatom6)'%((1./d)*9.465347))
cmd.select('temp53', 'all within %s of (jessatom7)'%(d*8.544600))
cmd.select('temp53', 'temp53 and not within %s of (jessatom7)'%((1./d)*8.376238))
cmd.select('temp54', 'all within %s of (jessatom8)'%(d*1.525100))
cmd.select('temp54', 'temp54 and not within %s of (jessatom8)'%((1./d)*1.495050))
cmd.select('temp55', 'byres jessatom8')
cmd.select('jessatom9', '(temp3 and temp37 and temp46 and temp47 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*17.887100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom9)'%((1./d)*17.534653))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*16.523600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom9)'%((1./d)*16.198020))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*17.230600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom9)'%((1./d)*16.891089))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*17.745700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom9)'%((1./d)*17.396040))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*7.282100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom9)'%((1./d)*7.138614))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*7.373000))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom9)'%((1./d)*7.227723))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*9.655600))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom9)'%((1./d)*9.465347))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*8.544600))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom9)'%((1./d)*8.376238))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*1.525100))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom9)'%((1./d)*1.495050))
cmd.select('Jab_1hmp_2_4_2_8', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9')
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
