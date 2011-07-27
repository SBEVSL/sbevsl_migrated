'''
FUNC:Jab_4pfk_2_7_1_11
PDB:4pfk
EC:2.7.1.11
RESI:gly,arg,thr,asp,arg
LOCI:a-11,72,125,127,171;
'''
cmd.select('temp0', 'name  n  ')
cmd.select('jessatom0', '(temp0)')
cmd.select('temp1', 'name  ca ')
cmd.select('temp2', 'all within %s of (jessatom0)'%(d*1.494800))
cmd.select('temp3', 'byres jessatom0')
cmd.select('jessatom1', '(temp1 and temp2 and temp3)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.494800))
cmd.select('temp4', 'resn arg')
cmd.select('temp5', 'all within %s of (jessatom0)'%(d*8.393100))
cmd.select('temp6', 'all within %s of (jessatom1)'%(d*9.130400))
cmd.select('jessatom2', '(temp1 and temp4 and temp5 and temp6)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*8.393100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*9.130400))
cmd.select('temp7', 'name  cb ')
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*8.362800))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*8.989000))
cmd.select('temp10', 'all within %s of (jessatom2)'%(d*1.535200))
cmd.select('temp11', 'byres jessatom2')
cmd.select('jessatom3', '(temp7 and temp4 and temp8 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.362800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*8.989000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.535200))
cmd.select('temp12', 'resn thr')
cmd.select('temp13', 'resn ser')
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*6.625600))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*6.655900))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*14.806600))
cmd.select('temp17', 'all within %s of (jessatom3)'%(d*14.847000))
cmd.select('jessatom4', '(((temp1 and temp12) or (temp1 and temp13)) and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*6.625600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.655900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*14.806600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*14.847000))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*6.756900))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*7.009400))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*14.655100))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*14.645000))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.595800))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(((temp7 and temp12) or (temp7 and temp13)) and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*6.756900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.009400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*14.655100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*14.645000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.595800))
cmd.select('temp24', 'resn asp')
cmd.select('temp25', 'resn glu')
cmd.select('temp26', 'all within %s of (jessatom0)'%(d*10.130300))
cmd.select('temp27', 'all within %s of (jessatom1)'%(d*9.968700))
cmd.select('temp28', 'all within %s of (jessatom2)'%(d*17.978000))
cmd.select('temp29', 'all within %s of (jessatom3)'%(d*17.634600))
cmd.select('temp30', 'all within %s of (jessatom4)'%(d*5.383300))
cmd.select('temp31', 'all within %s of (jessatom5)'%(d*4.736900))
cmd.select('jessatom6', '(((temp1 and temp24) or (temp1 and temp25)) and temp26 and temp27 and temp28 and temp29 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*10.130300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.968700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*17.978000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*17.634600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*5.383300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*4.736900))
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*9.352600))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*9.332400))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*16.887200))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*16.493300))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*5.443900))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*4.444000))
cmd.select('temp38', 'all within %s of (jessatom6)'%(d*1.565500))
cmd.select('temp39', 'byres jessatom6')
cmd.select('jessatom7', '(((temp7 and temp24) or (temp7 and temp25)) and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*9.352600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*9.332400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*16.887200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*16.493300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.443900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*4.444000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.565500))
cmd.select('temp40', 'all within %s of (jessatom0)'%(d*12.099800))
cmd.select('temp41', 'all within %s of (jessatom1)'%(d*12.039200))
cmd.select('temp42', 'all within %s of (jessatom2)'%(d*17.483100))
cmd.select('temp43', 'all within %s of (jessatom3)'%(d*16.584200))
cmd.select('temp44', 'all within %s of (jessatom4)'%(d*11.352400))
cmd.select('temp45', 'all within %s of (jessatom5)'%(d*10.302000))
cmd.select('temp46', 'all within %s of (jessatom6)'%(d*7.625500))
cmd.select('temp47', 'all within %s of (jessatom7)'%(d*6.585200))
cmd.select('jessatom8', '(temp1 and temp4 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*12.099800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*12.039200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*17.483100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*16.584200))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*11.352400))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*10.302000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*7.625500))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*6.585200))
cmd.select('temp48', 'all within %s of (jessatom0)'%(d*10.908000))
cmd.select('temp49', 'all within %s of (jessatom1)'%(d*10.948400))
cmd.select('temp50', 'all within %s of (jessatom2)'%(d*15.988300))
cmd.select('temp51', 'all within %s of (jessatom3)'%(d*15.099500))
cmd.select('temp52', 'all within %s of (jessatom4)'%(d*10.796900))
cmd.select('temp53', 'all within %s of (jessatom5)'%(d*9.706100))
cmd.select('temp54', 'all within %s of (jessatom6)'%(d*7.746700))
cmd.select('temp55', 'all within %s of (jessatom7)'%(d*6.514500))
cmd.select('temp56', 'all within %s of (jessatom8)'%(d*1.565500))
cmd.select('temp57', 'byres jessatom8')
cmd.select('jessatom9', '(temp7 and temp4 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*10.908000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*10.948400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*15.988300))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*15.099500))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*10.796900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*9.706100))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*7.746700))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*6.514500))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*1.565500))
cmd.select('Jab_4pfk_2_7_1_11', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9')
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
cmd.delete('temp56')
cmd.delete('temp57')