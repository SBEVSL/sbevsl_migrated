'''
FUNC:Jfa_1cg4_6_3_4_4
PDB:1cg4
EC:6.3.4.4
RESI:asp,his,gln
LOCI:a-13,41,224;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  od1')
cmd.select('temp4', 'name  od2')
cmd.select('temp5', 'name  oe1')
cmd.select('temp6', 'name  oe2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.262500))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*1.237624))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.237624))
cmd.select('temp9', 'name  od2')
cmd.select('temp10', 'name  od1')
cmd.select('temp11', 'name  oe2')
cmd.select('temp12', 'name  oe1')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*1.242300))
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*1.217822))
cmd.select('temp14', 'byres jessatom0')
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*2.161400))
cmd.select('temp15', 'temp15 and not within %s of (jessatom1)'%((1./d)*2.118812))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.242300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*1.217822))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.161400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*2.118812))
cmd.select('temp16', 'resn his')
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*8.716300))
cmd.select('temp17', 'temp17 and not within %s of (jessatom0)'%((1./d)*8.544554))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*7.686100))
cmd.select('temp18', 'temp18 and not within %s of (jessatom1)'%((1./d)*7.534653))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*9.736400))
cmd.select('temp19', 'temp19 and not within %s of (jessatom2)'%((1./d)*9.544554))
cmd.select('jessatom3', '(temp0 and temp16 and temp17 and temp18 and temp19)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.716300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*8.544554))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*7.686100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*7.534653))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*9.736400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*9.544554))
cmd.select('temp20', 'name  nd1')
cmd.select('temp21', 'all within %s of (jessatom0)'%(d*8.383000))
cmd.select('temp21', 'temp21 and not within %s of (jessatom0)'%((1./d)*8.217822))
cmd.select('temp22', 'all within %s of (jessatom1)'%(d*7.403300))
cmd.select('temp22', 'temp22 and not within %s of (jessatom1)'%((1./d)*7.257426))
cmd.select('temp23', 'all within %s of (jessatom2)'%(d*9.494000))
cmd.select('temp23', 'temp23 and not within %s of (jessatom2)'%((1./d)*9.306931))
cmd.select('temp24', 'all within %s of (jessatom3)'%(d*1.383700))
cmd.select('temp24', 'temp24 and not within %s of (jessatom3)'%((1./d)*1.356436))
cmd.select('temp25', 'byres jessatom3')
cmd.select('jessatom4', '(temp20 and temp16 and temp21 and temp22 and temp23 and temp24 and temp25)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*8.383000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*8.217822))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*7.403300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*7.257426))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*9.494000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*9.306931))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.383700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.356436))
cmd.select('temp26', 'name  ne2')
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*8.867800))
cmd.select('temp27', 'temp27 and not within %s of (jessatom0)'%((1./d)*8.693069))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*7.726500))
cmd.select('temp28', 'temp28 and not within %s of (jessatom1)'%((1./d)*7.574257))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*9.867700))
cmd.select('temp29', 'temp29 and not within %s of (jessatom2)'%((1./d)*9.673267))
cmd.select('temp30', 'all within %s of (jessatom3)'%(d*2.201800))
cmd.select('temp30', 'temp30 and not within %s of (jessatom3)'%((1./d)*2.158416))
cmd.select('temp31', 'byres jessatom3')
cmd.select('temp32', 'all within %s of (jessatom4)'%(d*2.161400))
cmd.select('temp32', 'temp32 and not within %s of (jessatom4)'%((1./d)*2.118812))
cmd.select('jessatom5', '(temp26 and temp16 and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*8.867800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*8.693069))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.726500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*7.574257))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.867700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*9.673267))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.201800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.158416))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.161400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.118812))
cmd.select('temp33', 'name  cd ')
cmd.select('temp34', 'resn gln')
cmd.select('temp35', 'resn asn')
cmd.select('temp36', 'all within %s of (jessatom0)'%(d*8.847600))
cmd.select('temp36', 'temp36 and not within %s of (jessatom0)'%((1./d)*8.673267))
cmd.select('temp37', 'all within %s of (jessatom1)'%(d*7.867900))
cmd.select('temp37', 'temp37 and not within %s of (jessatom1)'%((1./d)*7.712871))
cmd.select('temp38', 'all within %s of (jessatom2)'%(d*9.312200))
cmd.select('temp38', 'temp38 and not within %s of (jessatom2)'%((1./d)*9.128713))
cmd.select('temp39', 'all within %s of (jessatom3)'%(d*9.130400))
cmd.select('temp39', 'temp39 and not within %s of (jessatom3)'%((1./d)*8.950495))
cmd.select('temp40', 'all within %s of (jessatom4)'%(d*8.736500))
cmd.select('temp40', 'temp40 and not within %s of (jessatom4)'%((1./d)*8.564356))
cmd.select('temp41', 'all within %s of (jessatom5)'%(d*7.261900))
cmd.select('temp41', 'temp41 and not within %s of (jessatom5)'%((1./d)*7.118812))
cmd.select('jessatom6', '(((temp33 and temp34) or (temp33 and temp35)) and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.847600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*8.673267))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*7.867900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*7.712871))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*9.312200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*9.128713))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*9.130400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*8.950495))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*8.736500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*8.564356))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.261900))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*7.118812))
cmd.select('temp42', 'all within %s of (jessatom0)'%(d*10.019200))
cmd.select('temp42', 'temp42 and not within %s of (jessatom0)'%((1./d)*9.821782))
cmd.select('temp43', 'all within %s of (jessatom1)'%(d*9.019300))
cmd.select('temp43', 'temp43 and not within %s of (jessatom1)'%((1./d)*8.841584))
cmd.select('temp44', 'all within %s of (jessatom2)'%(d*10.524200))
cmd.select('temp44', 'temp44 and not within %s of (jessatom2)'%((1./d)*10.316832))
cmd.select('temp45', 'all within %s of (jessatom3)'%(d*9.564700))
cmd.select('temp45', 'temp45 and not within %s of (jessatom3)'%((1./d)*9.376238))
cmd.select('temp46', 'all within %s of (jessatom4)'%(d*9.160700))
cmd.select('temp46', 'temp46 and not within %s of (jessatom4)'%((1./d)*8.980198))
cmd.select('temp47', 'all within %s of (jessatom5)'%(d*7.544700))
cmd.select('temp47', 'temp47 and not within %s of (jessatom5)'%((1./d)*7.396040))
cmd.select('temp48', 'all within %s of (jessatom6)'%(d*1.242300))
cmd.select('temp48', 'temp48 and not within %s of (jessatom6)'%((1./d)*1.217822))
cmd.select('temp49', 'byres jessatom6')
cmd.select('jessatom7', '(((temp5 and temp34) or (temp5 and temp35)) and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*10.019200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*9.821782))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*9.019300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*8.841584))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*10.524200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*10.316832))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*9.564700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*9.376238))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*9.160700))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*8.980198))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.544700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*7.396040))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.242300))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.217822))
cmd.select('temp50', 'all within %s of (jessatom0)'%(d*8.231500))
cmd.select('temp50', 'temp50 and not within %s of (jessatom0)'%((1./d)*8.069307))
cmd.select('temp51', 'all within %s of (jessatom1)'%(d*7.160900))
cmd.select('temp51', 'temp51 and not within %s of (jessatom1)'%((1./d)*7.019802))
cmd.select('temp52', 'all within %s of (jessatom2)'%(d*8.686000))
cmd.select('temp52', 'temp52 and not within %s of (jessatom2)'%((1./d)*8.514851))
cmd.select('temp53', 'all within %s of (jessatom3)'%(d*8.251700))
cmd.select('temp53', 'temp53 and not within %s of (jessatom3)'%((1./d)*8.089109))
cmd.select('temp54', 'all within %s of (jessatom4)'%(d*8.019400))
cmd.select('temp54', 'temp54 and not within %s of (jessatom4)'%((1./d)*7.861386))
cmd.select('temp55', 'all within %s of (jessatom5)'%(d*6.484200))
cmd.select('temp55', 'temp55 and not within %s of (jessatom5)'%((1./d)*6.356436))
cmd.select('temp56', 'all within %s of (jessatom6)'%(d*1.353400))
cmd.select('temp56', 'temp56 and not within %s of (jessatom6)'%((1./d)*1.326733))
cmd.select('temp57', 'byres jessatom6')
cmd.select('temp58', 'all within %s of (jessatom7)'%(d*2.272500))
cmd.select('temp58', 'temp58 and not within %s of (jessatom7)'%((1./d)*2.227723))
cmd.select('jessatom8', '(((temp26 and temp34) or (temp26 and temp35)) and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*8.231500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*8.069307))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.160900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*7.019802))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*8.686000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*8.514851))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*8.251700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*8.089109))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*8.019400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*7.861386))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*6.484200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*6.356436))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.353400))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*1.326733))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.272500))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.227723))
cmd.select('Jfa_1cg4_6_3_4_4', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
