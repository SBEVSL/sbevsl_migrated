'''
FUNC:Jfa_2dnj_3_1_21_1
PDB:2dnj
EC:3.1.21.1
RESI:glu,his,asp,his
LOCI:a-78,134,212,252;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  oe1')
cmd.select('temp4', 'name  oe2')
cmd.select('temp5', 'name  od1')
cmd.select('temp6', 'name  od2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.222100))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.222100))
cmd.select('temp9', 'name  oe2')
cmd.select('temp10', 'name  oe1')
cmd.select('temp11', 'name  od2')
cmd.select('temp12', 'name  od1')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*1.272600))
cmd.select('temp14', 'byres jessatom0')
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*2.191700))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.272600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.191700))
cmd.select('temp16', 'name  cg ')
cmd.select('temp17', 'resn his')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*4.484400))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*3.575400))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*4.595500))
cmd.select('jessatom3', '(temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.484400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*3.575400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.595500))
cmd.select('temp21', 'name  nd1')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*3.221900))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*2.504800))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*3.201700))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*1.393800))
cmd.select('temp26', 'byres jessatom3')
cmd.select('jessatom4', '(temp21 and temp17 and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*3.221900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*2.504800))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.201700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.393800))
cmd.select('temp27', 'name  ne2')
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*4.979300))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*4.545000))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*4.494500))
cmd.select('temp31', 'all within %s of (jessatom3)'%(d*2.211900))
cmd.select('temp32', 'byres jessatom3')
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*2.141200))
cmd.select('jessatom5', '(temp27 and temp17 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*4.979300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*4.545000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.494500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.211900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.141200))
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*12.362400))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*11.564500))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*12.231100))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*8.655700))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*9.574800))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*8.463800))
cmd.select('jessatom6', '(((temp16 and temp2) or (temp16 and temp1)) and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*12.362400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*11.564500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*12.231100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*8.655700))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*9.574800))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.463800))
cmd.select('temp40', 'all within %s of (jessatom0)'%(d*12.756300))
cmd.select('temp41', 'all within %s of (jessatom1)'%(d*12.049300))
cmd.select('temp42', 'all within %s of (jessatom2)'%(d*12.503800))
cmd.select('temp43', 'all within %s of (jessatom3)'%(d*9.180900))
cmd.select('temp44', 'all within %s of (jessatom4)'%(d*9.988900))
cmd.select('temp45', 'all within %s of (jessatom5)'%(d*8.675900))
cmd.select('temp46', 'all within %s of (jessatom6)'%(d*1.282700))
cmd.select('temp47', 'byres jessatom6')
cmd.select('jessatom7', '((((temp5 or temp6) and temp2) or ((temp3 or temp4) and temp1)) and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*12.756300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*12.049300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*12.503800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*9.180900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*9.988900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*8.675900))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.282700))
cmd.select('temp48', 'all within %s of (jessatom0)'%(d*11.241300))
cmd.select('temp49', 'all within %s of (jessatom1)'%(d*10.423200))
cmd.select('temp50', 'all within %s of (jessatom2)'%(d*11.160500))
cmd.select('temp51', 'all within %s of (jessatom3)'%(d*7.625500))
cmd.select('temp52', 'all within %s of (jessatom4)'%(d*8.514300))
cmd.select('temp53', 'all within %s of (jessatom5)'%(d*7.575000))
cmd.select('temp54', 'all within %s of (jessatom6)'%(d*1.252400))
cmd.select('temp55', 'byres jessatom6')
cmd.select('temp56', 'all within %s of (jessatom7)'%(d*2.211900))
cmd.select('jessatom8', '((((temp11 or temp12) and temp2) or ((temp9 or temp10) and temp1)) and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*11.241300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*10.423200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*11.160500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*7.625500))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*8.514300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*7.575000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.252400))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.211900))
cmd.select('temp57', 'all within %s of (jessatom0)'%(d*11.029200))
cmd.select('temp58', 'all within %s of (jessatom1)'%(d*10.615100))
cmd.select('temp59', 'all within %s of (jessatom2)'%(d*10.564600))
cmd.select('temp60', 'all within %s of (jessatom3)'%(d*8.514300))
cmd.select('temp61', 'all within %s of (jessatom4)'%(d*8.817300))
cmd.select('temp62', 'all within %s of (jessatom5)'%(d*7.494200))
cmd.select('temp63', 'all within %s of (jessatom6)'%(d*4.383400))
cmd.select('temp64', 'all within %s of (jessatom7)'%(d*3.706700))
cmd.select('temp65', 'all within %s of (jessatom8)'%(d*4.161200))
cmd.select('jessatom9', '(temp16 and temp17 and temp57 and temp58 and temp59 and temp60 and temp61 and temp62 and temp63 and temp64 and temp65)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*11.029200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*10.615100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*10.564600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*8.514300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*8.817300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*7.494200))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*4.383400))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*3.706700))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*4.161200))
cmd.select('temp66', 'all within %s of (jessatom0)'%(d*11.160500))
cmd.select('temp67', 'all within %s of (jessatom1)'%(d*10.655500))
cmd.select('temp68', 'all within %s of (jessatom2)'%(d*10.706000))
cmd.select('temp69', 'all within %s of (jessatom3)'%(d*8.160800))
cmd.select('temp70', 'all within %s of (jessatom4)'%(d*8.645600))
cmd.select('temp71', 'all within %s of (jessatom5)'%(d*7.160900))
cmd.select('temp72', 'all within %s of (jessatom6)'%(d*3.494600))
cmd.select('temp73', 'all within %s of (jessatom7)'%(d*2.727000))
cmd.select('temp74', 'all within %s of (jessatom8)'%(d*3.444100))
cmd.select('temp75', 'all within %s of (jessatom9)'%(d*1.403900))
cmd.select('temp76', 'byres jessatom9')
cmd.select('jessatom10', '(temp21 and temp17 and temp66 and temp67 and temp68 and temp69 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*11.160500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*10.655500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*10.706000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*8.160800))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*8.645600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*7.160900))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*3.494600))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*2.727000))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*3.444100))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.403900))
cmd.select('temp77', 'all within %s of (jessatom0)'%(d*9.938400))
cmd.select('temp78', 'all within %s of (jessatom1)'%(d*9.635400))
cmd.select('temp79', 'all within %s of (jessatom2)'%(d*9.302100))
cmd.select('temp80', 'all within %s of (jessatom3)'%(d*7.463900))
cmd.select('temp81', 'all within %s of (jessatom4)'%(d*7.655800))
cmd.select('temp82', 'all within %s of (jessatom5)'%(d*6.019600))
cmd.select('temp83', 'all within %s of (jessatom6)'%(d*5.443900))
cmd.select('temp84', 'all within %s of (jessatom7)'%(d*4.797500))
cmd.select('temp85', 'all within %s of (jessatom8)'%(d*5.130800))
cmd.select('temp86', 'all within %s of (jessatom9)'%(d*2.191700))
cmd.select('temp87', 'byres jessatom9')
cmd.select('temp88', 'all within %s of (jessatom10)'%(d*2.141200))
cmd.select('jessatom11', '(temp27 and temp17 and temp77 and temp78 and temp79 and temp80 and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*9.938400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*9.635400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*9.302100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*7.463900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*7.655800))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*6.019600))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*5.443900))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*4.797500))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*5.130800))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.191700))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.141200))
cmd.select('Jfa_2dnj_3_1_21_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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