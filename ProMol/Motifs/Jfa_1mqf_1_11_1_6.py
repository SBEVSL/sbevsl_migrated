'''
FUNC:Jfa_1mqf_1_11_1_6
PDB:1mqf
EC:1.11.1.6
RESI:his,ser,asn
LOCI:a-54,93,127;
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
cmd.select('temp10', 'name  ca ')
cmd.select('temp11', 'resn ser')
cmd.select('temp12', 'resn thr')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*5.656000))
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*5.544554))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*4.908600))
cmd.select('temp14', 'temp14 and not within %s of (jessatom1)'%((1./d)*4.811881))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*7.039700))
cmd.select('temp15', 'temp15 and not within %s of (jessatom2)'%((1./d)*6.900990))
cmd.select('jessatom3', '(((temp10 and temp11) or (temp10 and temp12)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*5.656000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*5.544554))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.908600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*4.811881))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*7.039700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*6.900990))
cmd.select('temp16', 'name  cb ')
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*4.484400))
cmd.select('temp17', 'temp17 and not within %s of (jessatom0)'%((1./d)*4.396040))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*4.009700))
cmd.select('temp18', 'temp18 and not within %s of (jessatom1)'%((1./d)*3.930693))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*6.161000))
cmd.select('temp19', 'temp19 and not within %s of (jessatom2)'%((1./d)*6.039604))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp20', 'temp20 and not within %s of (jessatom3)'%((1./d)*1.524752))
cmd.select('temp21', 'byres jessatom3')
cmd.select('jessatom4', '(((temp16 and temp11) or (temp16 and temp12)) and temp17 and temp18 and temp19 and temp20 and temp21)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.484400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*4.396040))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.009700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*3.930693))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*6.161000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*6.039604))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.555400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.524752))
cmd.select('temp22', 'name  og ')
cmd.select('temp23', 'all within %s of (jessatom0)'%(d*3.535000))
cmd.select('temp23', 'temp23 and not within %s of (jessatom0)'%((1./d)*3.465347))
cmd.select('temp24', 'all within %s of (jessatom1)'%(d*2.848200))
cmd.select('temp24', 'temp24 and not within %s of (jessatom1)'%((1./d)*2.792079))
cmd.select('temp25', 'all within %s of (jessatom2)'%(d*4.989400))
cmd.select('temp25', 'temp25 and not within %s of (jessatom2)'%((1./d)*4.891089))
cmd.select('temp26', 'all within %s of (jessatom3)'%(d*2.464400))
cmd.select('temp26', 'temp26 and not within %s of (jessatom3)'%((1./d)*2.415842))
cmd.select('temp27', 'byres jessatom3')
cmd.select('temp28', 'all within %s of (jessatom4)'%(d*1.434200))
cmd.select('temp28', 'temp28 and not within %s of (jessatom4)'%((1./d)*1.405941))
cmd.select('jessatom5', '(((temp22 and temp11) or (temp22 and temp12)) and temp23 and temp24 and temp25 and temp26 and temp27 and temp28)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*3.535000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*3.465347))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*2.848200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*2.792079))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.989400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*4.891089))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.464400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.415842))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.434200))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.405941))
cmd.select('temp29', 'resn asn')
cmd.select('temp30', 'resn gln')
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*6.676100))
cmd.select('temp31', 'temp31 and not within %s of (jessatom0)'%((1./d)*6.544554))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*5.676200))
cmd.select('temp32', 'temp32 and not within %s of (jessatom1)'%((1./d)*5.564356))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*4.918700))
cmd.select('temp33', 'temp33 and not within %s of (jessatom2)'%((1./d)*4.821782))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*8.857700))
cmd.select('temp34', 'temp34 and not within %s of (jessatom3)'%((1./d)*8.683168))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*8.696100))
cmd.select('temp35', 'temp35 and not within %s of (jessatom4)'%((1./d)*8.524752))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*7.403300))
cmd.select('temp36', 'temp36 and not within %s of (jessatom5)'%((1./d)*7.257426))
cmd.select('jessatom6', '(((temp0 and temp29) or (temp0 and temp30)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*6.676100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*6.544554))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*5.676200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*5.564356))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*4.918700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*4.821782))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*8.857700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*8.683168))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*8.696100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*8.524752))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.403300))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*7.257426))
cmd.select('temp37', 'name  od1')
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*5.544554))
cmd.select('temp38', 'all within %s of (jessatom1)'%(d*4.585400))
cmd.select('temp38', 'temp38 and not within %s of (jessatom1)'%((1./d)*4.495050))
cmd.select('temp39', 'all within %s of (jessatom2)'%(d*4.130900))
cmd.select('temp39', 'temp39 and not within %s of (jessatom2)'%((1./d)*4.049505))
cmd.select('temp40', 'all within %s of (jessatom3)'%(d*7.746700))
cmd.select('temp40', 'temp40 and not within %s of (jessatom3)'%((1./d)*7.594059))
cmd.select('temp41', 'all within %s of (jessatom4)'%(d*7.514400))
cmd.select('temp41', 'temp41 and not within %s of (jessatom4)'%((1./d)*7.366337))
cmd.select('temp42', 'all within %s of (jessatom5)'%(d*6.191300))
cmd.select('temp42', 'temp42 and not within %s of (jessatom5)'%((1./d)*6.069307))
cmd.select('temp43', 'all within %s of (jessatom6)'%(d*1.242300))
cmd.select('temp43', 'temp43 and not within %s of (jessatom6)'%((1./d)*1.217822))
cmd.select('temp44', 'byres jessatom6')
cmd.select('jessatom7', '(((temp37 and temp29) or (temp37 and temp30)) and temp13 and temp38 and temp39 and temp40 and temp41 and temp42 and temp43 and temp44)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*5.656000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*5.544554))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*4.585400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*4.495050))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*4.130900))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*4.049505))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.746700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*7.594059))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*7.514400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*7.366337))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*6.191300))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*6.069307))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.242300))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.217822))
cmd.select('temp45', 'name  nd2')
cmd.select('temp46', 'all within %s of (jessatom0)'%(d*6.847800))
cmd.select('temp46', 'temp46 and not within %s of (jessatom0)'%((1./d)*6.712871))
cmd.select('temp47', 'all within %s of (jessatom1)'%(d*6.049900))
cmd.select('temp47', 'temp47 and not within %s of (jessatom1)'%((1./d)*5.930693))
cmd.select('temp48', 'all within %s of (jessatom2)'%(d*4.827800))
cmd.select('temp48', 'temp48 and not within %s of (jessatom2)'%((1./d)*4.732673))
cmd.select('temp49', 'all within %s of (jessatom3)'%(d*9.706100))
cmd.select('temp49', 'temp49 and not within %s of (jessatom3)'%((1./d)*9.514851))
cmd.select('temp50', 'all within %s of (jessatom4)'%(d*9.443500))
cmd.select('temp50', 'temp50 and not within %s of (jessatom4)'%((1./d)*9.257426))
cmd.select('temp51', 'all within %s of (jessatom5)'%(d*8.150700))
cmd.select('temp51', 'temp51 and not within %s of (jessatom5)'%((1./d)*7.990099))
cmd.select('temp52', 'all within %s of (jessatom6)'%(d*1.343300))
cmd.select('temp52', 'temp52 and not within %s of (jessatom6)'%((1./d)*1.316832))
cmd.select('temp53', 'byres jessatom6')
cmd.select('temp54', 'all within %s of (jessatom7)'%(d*2.262400))
cmd.select('temp54', 'temp54 and not within %s of (jessatom7)'%((1./d)*2.217822))
cmd.select('jessatom8', '(((temp45 and temp29) or (temp45 and temp30)) and temp46 and temp47 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.847800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*6.712871))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*6.049900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*5.930693))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*4.827800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*4.732673))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*9.706100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*9.514851))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*9.443500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*9.257426))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*8.150700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*7.990099))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.343300))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*1.316832))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.262400))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.217822))
cmd.select('Jfa_1mqf_1_11_1_6', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
