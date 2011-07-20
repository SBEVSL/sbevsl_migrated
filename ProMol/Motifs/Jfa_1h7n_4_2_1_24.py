'''
FUNC:Jfa_1h7n_4_2_1_24
PDB:1h7n
EC:4.2.1.24
RESI:asp,ser,lys,lys
LOCI:a-131,179,210,263;
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
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.262500))
cmd.select('temp9', 'name  od2')
cmd.select('temp10', 'name  od1')
cmd.select('temp11', 'name  oe2')
cmd.select('temp12', 'name  oe1')
cmd.select('temp13', 'byres jessatom0')
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*2.222000))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp7 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.262500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.222000))
cmd.select('temp15', 'name  ca ')
cmd.select('temp16', 'resn ser')
cmd.select('temp17', 'resn thr')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*5.231800))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*4.383400))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*5.363100))
cmd.select('jessatom3', '(((temp15 and temp16) or (temp15 and temp17)) and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*5.231800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.383400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*5.363100))
cmd.select('temp21', 'name  cb ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*4.100600))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*3.151200))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*4.292500))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp26', 'byres jessatom3')
cmd.select('jessatom4', '(((temp21 and temp16) or (temp21 and temp17)) and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.100600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*3.151200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.292500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp27', 'name  og ')
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*3.403700))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*2.858300))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*3.221900))
cmd.select('temp31', 'all within %s of (jessatom3)'%(d*2.424000))
cmd.select('temp32', 'byres jessatom3')
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*1.434200))
cmd.select('jessatom5', '(((temp27 and temp16) or (temp27 and temp17)) and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*3.403700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*2.858300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*3.221900))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.424000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.434200))
cmd.select('temp34', 'name  cd ')
cmd.select('temp35', 'resn lys')
cmd.select('temp36', 'all within %s of (jessatom0)'%(d*8.504200))
cmd.select('temp37', 'all within %s of (jessatom1)'%(d*7.484100))
cmd.select('temp38', 'all within %s of (jessatom2)'%(d*8.605200))
cmd.select('temp39', 'all within %s of (jessatom3)'%(d*4.797500))
cmd.select('temp40', 'all within %s of (jessatom4)'%(d*4.747000))
cmd.select('temp41', 'all within %s of (jessatom5)'%(d*5.666100))
cmd.select('jessatom6', '(temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.504200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*7.484100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*8.605200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*4.797500))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.747000))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*5.666100))
cmd.select('temp42', 'name  ce ')
cmd.select('temp43', 'all within %s of (jessatom0)'%(d*8.160800))
cmd.select('temp44', 'all within %s of (jessatom1)'%(d*7.272000))
cmd.select('temp45', 'all within %s of (jessatom2)'%(d*8.130500))
cmd.select('temp46', 'all within %s of (jessatom3)'%(d*5.231800))
cmd.select('temp47', 'all within %s of (jessatom4)'%(d*4.827800))
cmd.select('temp48', 'all within %s of (jessatom5)'%(d*5.423700))
cmd.select('temp49', 'all within %s of (jessatom6)'%(d*1.545300))
cmd.select('temp50', 'byres jessatom6')
cmd.select('jessatom7', '(temp42 and temp35 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.160800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*7.272000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*8.130500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*5.231800))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*4.827800))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*5.423700))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.545300))
cmd.select('temp51', 'name  nz ')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*6.696300))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*5.868100))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*6.625600))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*4.322800))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*3.625900))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*4.040000))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*2.484600))
cmd.select('temp59', 'byres jessatom6')
cmd.select('temp60', 'all within %s of (jessatom7)'%(d*1.515000))
cmd.select('jessatom8', '(temp51 and temp35 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.696300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*5.868100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*6.625600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*4.322800))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*3.625900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*4.040000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.484600))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.515000))
cmd.select('temp61', 'all within %s of (jessatom1)'%(d*7.403300))
cmd.select('temp62', 'all within %s of (jessatom2)'%(d*9.009200))
cmd.select('temp63', 'all within %s of (jessatom3)'%(d*6.918500))
cmd.select('temp64', 'all within %s of (jessatom4)'%(d*6.110500))
cmd.select('temp65', 'all within %s of (jessatom5)'%(d*7.080100))
cmd.select('temp66', 'all within %s of (jessatom6)'%(d*4.100600))
cmd.select('temp67', 'all within %s of (jessatom7)'%(d*4.120800))
cmd.select('temp68', 'all within %s of (jessatom8)'%(d*4.363200))
cmd.select('jessatom9', '(temp34 and temp35 and temp36 and temp61 and temp62 and temp63 and temp64 and temp65 and temp66 and temp67 and temp68)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*8.504200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*7.403300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*9.009200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*6.918500))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*6.110500))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*7.080100))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*4.100600))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*4.120800))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*4.363200))
cmd.select('temp69', 'all within %s of (jessatom0)'%(d*8.231500))
cmd.select('temp70', 'all within %s of (jessatom2)'%(d*8.585000))
cmd.select('temp71', 'all within %s of (jessatom3)'%(d*7.241700))
cmd.select('temp72', 'all within %s of (jessatom4)'%(d*6.221600))
cmd.select('temp73', 'all within %s of (jessatom5)'%(d*6.928600))
cmd.select('temp74', 'all within %s of (jessatom6)'%(d*4.474300))
cmd.select('temp75', 'all within %s of (jessatom7)'%(d*3.928900))
cmd.select('temp76', 'all within %s of (jessatom8)'%(d*3.989500))
cmd.select('temp77', 'all within %s of (jessatom9)'%(d*1.545300))
cmd.select('temp78', 'byres jessatom9')
cmd.select('jessatom10', '(temp42 and temp35 and temp69 and temp44 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*8.231500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*7.272000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*8.585000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*7.241700))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*6.221600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*6.928600))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*4.474300))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*3.928900))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*3.989500))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.545300))
cmd.select('temp79', 'all within %s of (jessatom0)'%(d*6.797300))
cmd.select('temp80', 'all within %s of (jessatom1)'%(d*5.898400))
cmd.select('temp81', 'all within %s of (jessatom2)'%(d*7.100300))
cmd.select('temp82', 'all within %s of (jessatom3)'%(d*6.191300))
cmd.select('temp83', 'all within %s of (jessatom4)'%(d*5.009600))
cmd.select('temp84', 'all within %s of (jessatom5)'%(d*5.555000))
cmd.select('temp85', 'all within %s of (jessatom6)'%(d*4.322800))
cmd.select('temp86', 'all within %s of (jessatom7)'%(d*3.595600))
cmd.select('temp87', 'all within %s of (jessatom8)'%(d*3.090600))
cmd.select('temp88', 'all within %s of (jessatom9)'%(d*2.474500))
cmd.select('temp89', 'byres jessatom9')
cmd.select('temp90', 'all within %s of (jessatom10)'%(d*1.515000))
cmd.select('jessatom11', '(temp51 and temp35 and temp79 and temp80 and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp90)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*6.797300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*5.898400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*7.100300))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*6.191300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*5.009600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*5.555000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*4.322800))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*3.595600))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*3.090600))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.474500))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*1.515000))
cmd.select('Jfa_1h7n_4_2_1_24', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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