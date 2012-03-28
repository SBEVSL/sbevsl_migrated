'''
FUNC:Jfa_1pzp_3_5_2_6
PDB:1pzp
EC:3.5.2.6
RESI:ser,lys,ser,glu
LOCI:a-70,73,130,166;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn ser')
cmd.select('temp2', 'resn thr')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.514851))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.514851))
cmd.select('temp6', 'name  og ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.413900))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*2.366337))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.434200))
cmd.select('temp9', 'temp9 and not within %s of (jessatom1)'%((1./d)*1.405941))
cmd.select('jessatom2', '(((temp6 and temp1) or (temp6 and temp2)) and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.413900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*2.366337))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.434200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*1.405941))
cmd.select('temp10', 'name  cd ')
cmd.select('temp11', 'resn lys')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*4.242000))
cmd.select('temp12', 'temp12 and not within %s of (jessatom0)'%((1./d)*4.158416))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*3.989500))
cmd.select('temp13', 'temp13 and not within %s of (jessatom1)'%((1./d)*3.910891))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*3.969300))
cmd.select('temp14', 'temp14 and not within %s of (jessatom2)'%((1./d)*3.891089))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.242000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*4.158416))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*3.989500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*3.910891))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*3.969300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*3.891089))
cmd.select('temp15', 'name  ce ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*4.221800))
cmd.select('temp16', 'temp16 and not within %s of (jessatom0)'%((1./d)*4.138614))
cmd.select('temp13', 'temp13 and not within %s of (jessatom1)'%((1./d)*3.910891))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*3.444100))
cmd.select('temp17', 'temp17 and not within %s of (jessatom2)'%((1./d)*3.376238))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*1.575600))
cmd.select('temp18', 'temp18 and not within %s of (jessatom3)'%((1./d)*1.544554))
cmd.select('temp19', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp13 and temp17 and temp18 and temp19)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.221800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*4.138614))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*3.989500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*3.910891))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.444100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*3.376238))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.575600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.544554))
cmd.select('temp20', 'name  nz ')
cmd.select('temp21', 'all within %s of (jessatom0)'%(d*4.292500))
cmd.select('temp21', 'temp21 and not within %s of (jessatom0)'%((1./d)*4.207921))
cmd.select('temp22', 'all within %s of (jessatom1)'%(d*3.615800))
cmd.select('temp22', 'temp22 and not within %s of (jessatom1)'%((1./d)*3.544554))
cmd.select('temp23', 'all within %s of (jessatom2)'%(d*2.686600))
cmd.select('temp23', 'temp23 and not within %s of (jessatom2)'%((1./d)*2.633663))
cmd.select('temp24', 'all within %s of (jessatom3)'%(d*2.565400))
cmd.select('temp24', 'temp24 and not within %s of (jessatom3)'%((1./d)*2.514851))
cmd.select('temp25', 'byres jessatom3')
cmd.select('temp26', 'all within %s of (jessatom4)'%(d*1.484700))
cmd.select('temp26', 'temp26 and not within %s of (jessatom4)'%((1./d)*1.455446))
cmd.select('jessatom5', '(temp20 and temp11 and temp21 and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*4.292500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*4.207921))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*3.615800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*3.544554))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*2.686600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*2.633663))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.565400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.514851))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.484700))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.455446))
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*6.625600))
cmd.select('temp27', 'temp27 and not within %s of (jessatom0)'%((1./d)*6.495050))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*5.322700))
cmd.select('temp28', 'temp28 and not within %s of (jessatom1)'%((1./d)*5.217822))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*5.050000))
cmd.select('temp29', 'temp29 and not within %s of (jessatom2)'%((1./d)*4.950495))
cmd.select('temp30', 'all within %s of (jessatom3)'%(d*4.474300))
cmd.select('temp30', 'temp30 and not within %s of (jessatom3)'%((1./d)*4.386139))
cmd.select('temp31', 'all within %s of (jessatom4)'%(d*4.807600))
cmd.select('temp31', 'temp31 and not within %s of (jessatom4)'%((1./d)*4.712871))
cmd.select('temp32', 'all within %s of (jessatom5)'%(d*4.019800))
cmd.select('temp32', 'temp32 and not within %s of (jessatom5)'%((1./d)*3.940594))
cmd.select('jessatom6', '(((temp0 and temp1) or (temp0 and temp2)) and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*6.625600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*6.495050))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*5.322700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*5.217822))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*5.050000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*4.950495))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*4.474300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*4.386139))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.807600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*4.712871))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*4.019800))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*3.940594))
cmd.select('temp33', 'all within %s of (jessatom0)'%(d*6.100400))
cmd.select('temp33', 'temp33 and not within %s of (jessatom0)'%((1./d)*5.980198))
cmd.select('temp34', 'all within %s of (jessatom1)'%(d*4.625800))
cmd.select('temp34', 'temp34 and not within %s of (jessatom1)'%((1./d)*4.534653))
cmd.select('temp35', 'all within %s of (jessatom2)'%(d*4.393500))
cmd.select('temp35', 'temp35 and not within %s of (jessatom2)'%((1./d)*4.306931))
cmd.select('temp36', 'all within %s of (jessatom3)'%(d*5.050000))
cmd.select('temp36', 'temp36 and not within %s of (jessatom3)'%((1./d)*4.950495))
cmd.select('temp37', 'all within %s of (jessatom4)'%(d*5.252000))
cmd.select('temp37', 'temp37 and not within %s of (jessatom4)'%((1./d)*5.148515))
cmd.select('temp38', 'all within %s of (jessatom5)'%(d*4.211700))
cmd.select('temp38', 'temp38 and not within %s of (jessatom5)'%((1./d)*4.128713))
cmd.select('temp39', 'all within %s of (jessatom6)'%(d*1.555400))
cmd.select('temp39', 'temp39 and not within %s of (jessatom6)'%((1./d)*1.524752))
cmd.select('temp40', 'byres jessatom6')
cmd.select('jessatom7', '(((temp3 and temp1) or (temp3 and temp2)) and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*6.100400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*5.980198))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*4.625800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*4.534653))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*4.393500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*4.306931))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*5.050000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*4.950495))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.252000))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*5.148515))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*4.211700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*4.128713))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.555400))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.524752))
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*4.676300))
cmd.select('temp41', 'temp41 and not within %s of (jessatom0)'%((1./d)*4.584158))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*3.201700))
cmd.select('temp42', 'temp42 and not within %s of (jessatom1)'%((1./d)*3.138614))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*3.060300))
cmd.select('temp43', 'temp43 and not within %s of (jessatom2)'%((1./d)*3.000000))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*4.231900))
cmd.select('temp44', 'temp44 and not within %s of (jessatom3)'%((1./d)*4.148515))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*4.393500))
cmd.select('temp45', 'temp45 and not within %s of (jessatom4)'%((1./d)*4.306931))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*3.413800))
cmd.select('temp46', 'temp46 and not within %s of (jessatom5)'%((1./d)*3.346535))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*2.424000))
cmd.select('temp47', 'temp47 and not within %s of (jessatom6)'%((1./d)*2.376238))
cmd.select('temp48', 'byres jessatom6')
cmd.select('temp49', 'all within %s of (jessatom7)'%(d*1.434200))
cmd.select('temp49', 'temp49 and not within %s of (jessatom7)'%((1./d)*1.405941))
cmd.select('jessatom8', '(((temp6 and temp1) or (temp6 and temp2)) and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*4.676300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*4.584158))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*3.201700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*3.138614))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*3.060300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*3.000000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*4.231900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*4.148515))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*4.393500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*4.306931))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*3.413800))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*3.346535))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.424000))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*2.376238))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.434200))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*1.405941))
cmd.select('temp50', 'resn glu')
cmd.select('temp51', 'resn asp')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*5.948900))
cmd.select('temp52', 'temp52 and not within %s of (jessatom0)'%((1./d)*5.831683))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*6.120600))
cmd.select('temp53', 'temp53 and not within %s of (jessatom1)'%((1./d)*6.000000))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*4.989400))
cmd.select('temp54', 'temp54 and not within %s of (jessatom2)'%((1./d)*4.891089))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*5.716600))
cmd.select('temp55', 'temp55 and not within %s of (jessatom3)'%((1./d)*5.603960))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*4.191500))
cmd.select('temp56', 'temp56 and not within %s of (jessatom4)'%((1./d)*4.108911))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*4.151100))
cmd.select('temp57', 'temp57 and not within %s of (jessatom5)'%((1./d)*4.069307))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*8.049700))
cmd.select('temp58', 'temp58 and not within %s of (jessatom6)'%((1./d)*7.891089))
cmd.select('temp59', 'all within %s of (jessatom7)'%(d*8.090100))
cmd.select('temp59', 'temp59 and not within %s of (jessatom7)'%((1./d)*7.930693))
cmd.select('temp60', 'all within %s of (jessatom8)'%(d*7.221500))
cmd.select('temp60', 'temp60 and not within %s of (jessatom8)'%((1./d)*7.079208))
cmd.select('jessatom9', '(((temp10 and temp50) or (temp10 and temp51)) and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*5.948900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom9)'%((1./d)*5.831683))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*6.120600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom9)'%((1./d)*6.000000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*4.989400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom9)'%((1./d)*4.891089))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*5.716600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom9)'%((1./d)*5.603960))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*4.191500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom9)'%((1./d)*4.108911))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*4.151100))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom9)'%((1./d)*4.069307))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*8.049700))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom9)'%((1./d)*7.891089))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*8.090100))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom9)'%((1./d)*7.930693))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*7.221500))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom9)'%((1./d)*7.079208))
cmd.select('temp61', 'name  oe1')
cmd.select('temp62', 'name  oe2')
cmd.select('temp63', 'name  od1')
cmd.select('temp64', 'name  od2')
cmd.select('temp65', 'all within %s of (jessatom0)'%(d*6.383200))
cmd.select('temp65', 'temp65 and not within %s of (jessatom0)'%((1./d)*6.257426))
cmd.select('temp66', 'all within %s of (jessatom1)'%(d*6.494300))
cmd.select('temp66', 'temp66 and not within %s of (jessatom1)'%((1./d)*6.366337))
cmd.select('temp67', 'all within %s of (jessatom2)'%(d*5.272200))
cmd.select('temp67', 'temp67 and not within %s of (jessatom2)'%((1./d)*5.168317))
cmd.select('temp68', 'all within %s of (jessatom3)'%(d*6.696300))
cmd.select('temp68', 'temp68 and not within %s of (jessatom3)'%((1./d)*6.564356))
cmd.select('temp69', 'all within %s of (jessatom4)'%(d*5.171200))
cmd.select('temp69', 'temp69 and not within %s of (jessatom4)'%((1./d)*5.069307))
cmd.select('temp70', 'all within %s of (jessatom5)'%(d*4.848000))
cmd.select('temp70', 'temp70 and not within %s of (jessatom5)'%((1./d)*4.752475))
cmd.select('temp71', 'all within %s of (jessatom6)'%(d*8.595100))
cmd.select('temp71', 'temp71 and not within %s of (jessatom6)'%((1./d)*8.425743))
cmd.select('temp72', 'all within %s of (jessatom7)'%(d*8.453700))
cmd.select('temp72', 'temp72 and not within %s of (jessatom7)'%((1./d)*8.287129))
cmd.select('temp73', 'all within %s of (jessatom8)'%(d*7.595200))
cmd.select('temp73', 'temp73 and not within %s of (jessatom8)'%((1./d)*7.445545))
cmd.select('temp74', 'all within %s of (jessatom9)'%(d*1.252400))
cmd.select('temp74', 'temp74 and not within %s of (jessatom9)'%((1./d)*1.227723))
cmd.select('temp75', 'byres jessatom9')
cmd.select('jessatom10', '((((temp61 or temp62) and temp50) or ((temp63 or temp64) and temp51)) and temp65 and temp66 and temp67 and temp68 and temp69 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*6.383200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom10)'%((1./d)*6.257426))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*6.494300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom10)'%((1./d)*6.366337))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*5.272200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom10)'%((1./d)*5.168317))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*6.696300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom10)'%((1./d)*6.564356))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*5.171200))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom10)'%((1./d)*5.069307))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*4.848000))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom10)'%((1./d)*4.752475))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*8.595100))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom10)'%((1./d)*8.425743))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*8.453700))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom10)'%((1./d)*8.287129))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*7.595200))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom10)'%((1./d)*7.445545))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.252400))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom10)'%((1./d)*1.227723))
cmd.select('temp76', 'name  oe2')
cmd.select('temp77', 'name  oe1')
cmd.select('temp78', 'name  od2')
cmd.select('temp79', 'name  od1')
cmd.select('temp80', 'all within %s of (jessatom0)'%(d*4.757100))
cmd.select('temp80', 'temp80 and not within %s of (jessatom0)'%((1./d)*4.663366))
cmd.select('temp81', 'all within %s of (jessatom1)'%(d*5.019700))
cmd.select('temp81', 'temp81 and not within %s of (jessatom1)'%((1./d)*4.920792))
cmd.select('temp82', 'all within %s of (jessatom2)'%(d*4.019800))
cmd.select('temp82', 'temp82 and not within %s of (jessatom2)'%((1./d)*3.940594))
cmd.select('temp83', 'all within %s of (jessatom3)'%(d*4.706600))
cmd.select('temp83', 'temp83 and not within %s of (jessatom3)'%((1./d)*4.613861))
cmd.select('temp84', 'all within %s of (jessatom4)'%(d*3.262300))
cmd.select('temp84', 'temp84 and not within %s of (jessatom4)'%((1./d)*3.198020))
cmd.select('temp85', 'all within %s of (jessatom5)'%(d*3.383500))
cmd.select('temp85', 'temp85 and not within %s of (jessatom5)'%((1./d)*3.316832))
cmd.select('temp86', 'all within %s of (jessatom6)'%(d*7.383100))
cmd.select('temp86', 'temp86 and not within %s of (jessatom6)'%((1./d)*7.237624))
cmd.select('temp87', 'all within %s of (jessatom7)'%(d*7.393200))
cmd.select('temp87', 'temp87 and not within %s of (jessatom7)'%((1./d)*7.247525))
cmd.select('temp88', 'all within %s of (jessatom8)'%(d*6.393300))
cmd.select('temp88', 'temp88 and not within %s of (jessatom8)'%((1./d)*6.267327))
cmd.select('temp74', 'temp74 and not within %s of (jessatom9)'%((1./d)*1.227723))
cmd.select('temp89', 'byres jessatom9')
cmd.select('temp90', 'all within %s of (jessatom10)'%(d*2.181600))
cmd.select('temp90', 'temp90 and not within %s of (jessatom10)'%((1./d)*2.138614))
cmd.select('jessatom11', '((((temp76 or temp77) and temp50) or ((temp78 or temp79) and temp51)) and temp80 and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp74 and temp89 and temp90)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*4.757100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom11)'%((1./d)*4.663366))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*5.019700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom11)'%((1./d)*4.920792))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*4.019800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom11)'%((1./d)*3.940594))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*4.706600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom11)'%((1./d)*4.613861))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*3.262300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom11)'%((1./d)*3.198020))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*3.383500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom11)'%((1./d)*3.316832))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*7.383100))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom11)'%((1./d)*7.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*7.393200))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom11)'%((1./d)*7.247525))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*6.393300))
cmd.select('jessatom8', 'jessatom8 and not within %s of (jessatom11)'%((1./d)*6.267327))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*1.252400))
cmd.select('jessatom9', 'jessatom9 and not within %s of (jessatom11)'%((1./d)*1.227723))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.181600))
cmd.select('jessatom10', 'jessatom10 and not within %s of (jessatom11)'%((1./d)*2.138614))
cmd.select('Jfa_1pzp_3_5_2_6', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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
