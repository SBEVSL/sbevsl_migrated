'''
FUNC:Jfa_1kf5_3_1_27_5
PDB:1kf5
EC:3.1.27.5
RESI:his,lys,his,phe
LOCI:a-12,41,119,120;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nd1')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.383700))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.383700))
cmd.select('temp6', 'name  ne2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.242200))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.201800))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.242200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.201800))
cmd.select('temp10', 'name  cd ')
cmd.select('temp11', 'resn lys')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*8.251700))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*7.373000))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*6.999300))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.251700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*7.373000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*6.999300))
cmd.select('temp15', 'name  ce ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*7.605300))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*6.726600))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*6.049900))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*7.605300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.726600))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*6.049900))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp21', 'name  nz ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*6.110500))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*5.272200))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*4.585400))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.525000))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*1.494800))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*6.110500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*5.272200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.585400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.525000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.494800))
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*8.453700))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*8.574900))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*6.827600))
cmd.select('temp31', 'all within %s of (jessatom3)'%(d*11.473600))
cmd.select('temp32', 'all within %s of (jessatom4)'%(d*9.988900))
cmd.select('temp33', 'all within %s of (jessatom5)'%(d*9.160700))
cmd.select('jessatom6', '(temp0 and temp3 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.453700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*8.574900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*6.827600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*11.473600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*9.988900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*9.160700))
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*8.383000))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*8.342600))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*6.524600))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*10.413100))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*8.908200))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*8.201200))
cmd.select('temp40', 'all within %s of (jessatom6)'%(d*1.353400))
cmd.select('temp41', 'byres jessatom6')
cmd.select('jessatom7', '(temp2 and temp3 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.383000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.342600))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*6.524600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*10.413100))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*8.908200))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*8.201200))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.353400))
cmd.select('temp42', 'all within %s of (jessatom0)'%(d*9.433400))
cmd.select('temp43', 'all within %s of (jessatom1)'%(d*9.261700))
cmd.select('temp44', 'all within %s of (jessatom2)'%(d*7.787100))
cmd.select('temp45', 'all within %s of (jessatom3)'%(d*11.716000))
cmd.select('temp46', 'all within %s of (jessatom4)'%(d*10.180800))
cmd.select('temp47', 'all within %s of (jessatom5)'%(d*9.524300))
cmd.select('temp48', 'all within %s of (jessatom6)'%(d*2.211900))
cmd.select('temp49', 'byres jessatom6')
cmd.select('temp50', 'all within %s of (jessatom7)'%(d*2.151300))
cmd.select('jessatom8', '(temp6 and temp3 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*9.433400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*9.261700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*7.787100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*11.716000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*10.180800))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*9.524300))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.211900))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.151300))
cmd.select('temp51', 'name  n  ')
cmd.select('temp52', 'all within %s of (jessatom0)'%(d*5.413600))
cmd.select('temp53', 'all within %s of (jessatom1)'%(d*5.615600))
cmd.select('temp54', 'all within %s of (jessatom2)'%(d*4.282400))
cmd.select('temp55', 'all within %s of (jessatom3)'%(d*10.332300))
cmd.select('temp56', 'all within %s of (jessatom4)'%(d*9.019300))
cmd.select('temp57', 'all within %s of (jessatom5)'%(d*7.827500))
cmd.select('temp58', 'all within %s of (jessatom6)'%(d*3.353200))
cmd.select('temp59', 'all within %s of (jessatom7)'%(d*3.757200))
cmd.select('temp60', 'all within %s of (jessatom8)'%(d*4.383400))
cmd.select('jessatom9', '(temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*5.413600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*5.615600))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*4.282400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*10.332300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*9.019300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*7.827500))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*3.353200))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*3.757200))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*4.383400))
cmd.select('temp61', 'name  ca ')
cmd.select('temp62', 'all within %s of (jessatom0)'%(d*5.373200))
cmd.select('temp63', 'all within %s of (jessatom1)'%(d*5.373200))
cmd.select('temp64', 'all within %s of (jessatom3)'%(d*10.574700))
cmd.select('temp65', 'all within %s of (jessatom4)'%(d*9.281900))
cmd.select('temp66', 'all within %s of (jessatom5)'%(d*8.080000))
cmd.select('temp67', 'all within %s of (jessatom6)'%(d*4.363200))
cmd.select('temp68', 'all within %s of (jessatom7)'%(d*4.706600))
cmd.select('temp69', 'all within %s of (jessatom8)'%(d*4.767200))
cmd.select('temp70', 'all within %s of (jessatom9)'%(d*1.494800))
cmd.select('temp71', 'byres jessatom9')
cmd.select('jessatom10', '(temp61 and temp62 and temp63 and temp24 and temp64 and temp65 and temp66 and temp67 and temp68 and temp69 and temp70 and temp71)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*5.373200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*5.373200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*4.585400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*10.574700))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*9.281900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*8.080000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*4.363200))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*4.706600))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*4.767200))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.494800))
cmd.select('temp72', 'name  c  ')
cmd.select('temp73', 'all within %s of (jessatom0)'%(d*6.565000))
cmd.select('temp74', 'all within %s of (jessatom1)'%(d*6.312500))
cmd.select('temp75', 'all within %s of (jessatom2)'%(d*5.524700))
cmd.select('temp76', 'all within %s of (jessatom3)'%(d*10.675700))
cmd.select('temp77', 'all within %s of (jessatom4)'%(d*9.312200))
cmd.select('temp78', 'all within %s of (jessatom5)'%(d*8.271900))
cmd.select('temp79', 'all within %s of (jessatom6)'%(d*4.120800))
cmd.select('temp80', 'all within %s of (jessatom7)'%(d*4.282400))
cmd.select('temp81', 'all within %s of (jessatom8)'%(d*3.797600))
cmd.select('temp82', 'all within %s of (jessatom9)'%(d*2.444200))
cmd.select('temp83', 'byres jessatom9')
cmd.select('temp84', 'all within %s of (jessatom10)'%(d*1.535200))
cmd.select('jessatom11', '(temp72 and temp73 and temp74 and temp75 and temp76 and temp77 and temp78 and temp79 and temp80 and temp81 and temp82 and temp83 and temp84)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*6.565000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*6.312500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*5.524700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*10.675700))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*9.312200))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*8.271900))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*4.120800))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*4.282400))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*3.797600))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*2.444200))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*1.535200))
cmd.select('Jfa_1kf5_3_1_27_5', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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