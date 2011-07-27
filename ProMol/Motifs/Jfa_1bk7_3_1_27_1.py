'''
FUNC:Jfa_1bk7_3_1_27_1
PDB:1bk7
EC:3.1.27.1
RESI:his,glu,his
LOCI:a-34,84,88;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nd1')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.393800))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.393800))
cmd.select('temp6', 'name  ne2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.222000))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.161400))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.161400))
cmd.select('temp10', 'name  cd ')
cmd.select('temp11', 'resn glu')
cmd.select('temp12', 'resn asp')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*5.595400))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*6.464000))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*4.777300))
cmd.select('jessatom3', '(((temp10 and temp11) or (temp10 and temp12)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*5.595400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.464000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.777300))
cmd.select('temp16', 'name  oe1')
cmd.select('temp17', 'name  oe2')
cmd.select('temp18', 'name  od1')
cmd.select('temp19', 'name  od2')
cmd.select('temp20', 'all within %s of (jessatom0)'%(d*5.585300))
cmd.select('temp21', 'all within %s of (jessatom1)'%(d*6.433700))
cmd.select('temp22', 'all within %s of (jessatom2)'%(d*4.969200))
cmd.select('temp23', 'all within %s of (jessatom3)'%(d*1.262500))
cmd.select('temp24', 'byres jessatom3')
cmd.select('jessatom4', '((((temp16 or temp17) and temp11) or ((temp18 or temp19) and temp12)) and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*5.585300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.433700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.969200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.262500))
cmd.select('temp25', 'name  oe2')
cmd.select('temp26', 'name  oe1')
cmd.select('temp27', 'name  od2')
cmd.select('temp28', 'name  od1')
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*5.413600))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*6.090300))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*4.151100))
cmd.select('temp32', 'byres jessatom3')
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*2.211900))
cmd.select('jessatom5', '((((temp25 or temp26) and temp11) or ((temp27 or temp28) and temp12)) and temp29 and temp30 and temp31 and temp23 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*5.413600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*6.090300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.151100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.262500))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.211900))
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*8.706200))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*9.160700))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*7.888100))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*5.140900))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*4.171300))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*5.605500))
cmd.select('jessatom6', '(temp0 and temp3 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.706200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.160700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*7.888100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*5.140900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.171300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*5.605500))
cmd.select('temp40', 'all within %s of (jessatom0)'%(d*8.989000))
cmd.select('temp41', 'all within %s of (jessatom1)'%(d*9.271800))
cmd.select('temp42', 'all within %s of (jessatom2)'%(d*8.150700))
cmd.select('temp43', 'all within %s of (jessatom3)'%(d*6.150900))
cmd.select('temp44', 'all within %s of (jessatom4)'%(d*5.151000))
cmd.select('temp45', 'all within %s of (jessatom5)'%(d*6.464000))
cmd.select('temp46', 'all within %s of (jessatom6)'%(d*1.393800))
cmd.select('temp47', 'byres jessatom6')
cmd.select('jessatom7', '(temp2 and temp3 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.989000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*9.271800))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*8.150700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.150900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.151000))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*6.464000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.393800))
cmd.select('temp48', 'all within %s of (jessatom0)'%(d*7.564900))
cmd.select('temp49', 'all within %s of (jessatom1)'%(d*7.766900))
cmd.select('temp50', 'all within %s of (jessatom2)'%(d*6.363000))
cmd.select('temp51', 'all within %s of (jessatom3)'%(d*4.747000))
cmd.select('temp52', 'all within %s of (jessatom4)'%(d*4.009700))
cmd.select('temp53', 'all within %s of (jessatom5)'%(d*4.726800))
cmd.select('temp54', 'all within %s of (jessatom6)'%(d*2.222000))
cmd.select('temp55', 'byres jessatom6')
cmd.select('temp56', 'all within %s of (jessatom7)'%(d*2.161400))
cmd.select('jessatom8', '(temp6 and temp3 and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*7.564900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.766900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*6.363000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*4.747000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*4.009700))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*4.726800))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.222000))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.161400))
cmd.select('Jfa_1bk7_3_1_27_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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