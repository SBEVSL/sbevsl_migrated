'''
FUNC:Jfa_1pjb_1_4_1_1
PDB:1pjb
EC:1.4.1.1
RESI:lys,his,glu,asp
LOCI:a-74,95,117,269;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn lys')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  ce ')
cmd.select('temp3', 'resn lys')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.525100))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.525100))
cmd.select('temp6', 'name  nz ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.535100))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.535200))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.535100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.535200))
cmd.select('temp10', 'name  cg ')
cmd.select('temp11', 'resn his')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*8.009300))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*6.948800))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*6.090300))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.009300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.948800))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*6.090300))
cmd.select('temp15', 'name  nd1')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*6.807400))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*5.847900))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*4.898500))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.393800))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*6.807400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*5.847900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.898500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.393800))
cmd.select('temp21', 'name  ne2')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*8.029500))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*6.908400))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*5.696400))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.222000))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*2.161400))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*8.029500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*6.908400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*5.696400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.222000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.161400))
cmd.select('temp28', 'resn glu')
cmd.select('temp29', 'resn asp')
cmd.select('temp30', 'all within %s of (jessatom0)'%(d*9.564700))
cmd.select('temp31', 'all within %s of (jessatom1)'%(d*9.100100))
cmd.select('temp32', 'all within %s of (jessatom2)'%(d*8.039600))
cmd.select('temp33', 'all within %s of (jessatom3)'%(d*4.474300))
cmd.select('temp34', 'all within %s of (jessatom4)'%(d*4.221800))
cmd.select('temp35', 'all within %s of (jessatom5)'%(d*4.837900))
cmd.select('jessatom6', '(((temp0 and temp28) or (temp0 and temp29)) and temp30 and temp31 and temp32 and temp33 and temp34 and temp35)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*9.564700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.100100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*8.039600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*4.474300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.221800))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*4.837900))
cmd.select('temp36', 'name  oe1')
cmd.select('temp37', 'name  oe2')
cmd.select('temp38', 'name  od1')
cmd.select('temp39', 'name  od2')
cmd.select('temp40', 'all within %s of (jessatom0)'%(d*8.797100))
cmd.select('temp41', 'all within %s of (jessatom1)'%(d*8.494100))
cmd.select('temp42', 'all within %s of (jessatom2)'%(d*7.453800))
cmd.select('temp43', 'all within %s of (jessatom3)'%(d*4.969200))
cmd.select('temp44', 'all within %s of (jessatom4)'%(d*4.363200))
cmd.select('temp45', 'all within %s of (jessatom5)'%(d*5.201500))
cmd.select('temp46', 'all within %s of (jessatom6)'%(d*1.252400))
cmd.select('temp47', 'byres jessatom6')
cmd.select('jessatom7', '((((temp36 or temp37) and temp28) or ((temp38 or temp39) and temp29)) and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.797100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.494100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*7.453800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*4.969200))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*4.363200))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*5.201500))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.252400))
cmd.select('temp48', 'name  oe2')
cmd.select('temp49', 'name  oe1')
cmd.select('temp50', 'name  od2')
cmd.select('temp51', 'name  od1')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*9.837400))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*9.322300))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*8.403200))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*4.181400))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*4.201600))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*5.100500))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*1.282700))
cmd.select('temp59', 'byres jessatom6')
cmd.select('temp60', 'all within %s of (jessatom7)'%(d*2.222000))
cmd.select('jessatom8', '((((temp48 or temp49) and temp28) or ((temp50 or temp51) and temp29)) and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*9.837400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*9.322300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*8.403200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*4.181400))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*4.201600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*5.100500))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.282700))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.222000))
cmd.select('temp61', 'all within %s of (jessatom0)'%(d*11.190800))
cmd.select('temp62', 'all within %s of (jessatom1)'%(d*9.716200))
cmd.select('temp63', 'all within %s of (jessatom2)'%(d*9.019300))
cmd.select('temp64', 'all within %s of (jessatom3)'%(d*8.251700))
cmd.select('temp65', 'all within %s of (jessatom4)'%(d*8.534500))
cmd.select('temp66', 'all within %s of (jessatom5)'%(d*7.100300))
cmd.select('temp67', 'all within %s of (jessatom6)'%(d*11.918000))
cmd.select('temp68', 'all within %s of (jessatom7)'%(d*12.281600))
cmd.select('temp69', 'all within %s of (jessatom8)'%(d*12.069500))
cmd.select('jessatom9', '(((temp10 and temp29) or (temp10 and temp28)) and temp61 and temp62 and temp63 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*11.190800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*9.716200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*9.019300))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*8.251700))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*8.534500))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*7.100300))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*11.918000))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*12.281600))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*12.069500))
cmd.select('temp70', 'all within %s of (jessatom0)'%(d*12.049300))
cmd.select('temp71', 'all within %s of (jessatom1)'%(d*10.605000))
cmd.select('temp72', 'all within %s of (jessatom2)'%(d*9.786900))
cmd.select('temp73', 'all within %s of (jessatom3)'%(d*8.978900))
cmd.select('temp74', 'all within %s of (jessatom4)'%(d*9.251600))
cmd.select('temp75', 'all within %s of (jessatom5)'%(d*7.615400))
cmd.select('temp76', 'all within %s of (jessatom6)'%(d*12.352300))
cmd.select('temp77', 'all within %s of (jessatom7)'%(d*12.736100))
cmd.select('temp78', 'all within %s of (jessatom8)'%(d*12.584600))
cmd.select('temp79', 'all within %s of (jessatom9)'%(d*1.272600))
cmd.select('temp80', 'byres jessatom9')
cmd.select('jessatom10', '((((temp38 or temp39) and temp29) or ((temp36 or temp37) and temp28)) and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*12.049300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*10.605000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*9.786900))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*8.978900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*9.251600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*7.615400))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*12.352300))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*12.736100))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*12.584600))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.272600))
cmd.select('temp81', 'all within %s of (jessatom0)'%(d*10.069700))
cmd.select('temp82', 'all within %s of (jessatom1)'%(d*8.595100))
cmd.select('temp83', 'all within %s of (jessatom2)'%(d*7.837600))
cmd.select('temp84', 'all within %s of (jessatom3)'%(d*7.080100))
cmd.select('temp85', 'all within %s of (jessatom4)'%(d*7.302300))
cmd.select('temp86', 'all within %s of (jessatom5)'%(d*5.928700))
cmd.select('temp87', 'all within %s of (jessatom6)'%(d*10.766600))
cmd.select('temp88', 'all within %s of (jessatom7)'%(d*11.089800))
cmd.select('temp89', 'all within %s of (jessatom8)'%(d*10.918100))
cmd.select('temp90', 'all within %s of (jessatom9)'%(d*1.262500))
cmd.select('temp91', 'byres jessatom9')
cmd.select('temp92', 'all within %s of (jessatom10)'%(d*2.232100))
cmd.select('jessatom11', '((((temp50 or temp51) and temp29) or ((temp48 or temp49) and temp28)) and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp90 and temp91 and temp92)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*10.069700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*8.595100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*7.837600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*7.080100))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*7.302300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*5.928700))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*10.766600))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*11.089800))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*10.918100))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*1.262500))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.232100))
cmd.select('Jfa_1pjb_1_4_1_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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