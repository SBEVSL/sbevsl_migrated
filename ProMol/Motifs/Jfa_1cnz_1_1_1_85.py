'''
FUNC:Jfa_1cnz_1_1_1_85
PDB:1cnz
EC:1.1.1.85
RESI:lys,asp,tyr
LOCI:a-195,227;b-145;
'''
cmd.select('temp0', 'name  ce1')
cmd.select('temp1', 'resn tyr')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cz ')
cmd.select('temp3', 'resn tyr')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.393800))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.393800))
cmd.select('temp6', 'name  oh ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.413900))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.393800))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.413900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.393800))
cmd.select('temp10', 'name  cd ')
cmd.select('temp11', 'resn lys')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*6.009500))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*5.171200))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*4.393500))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*6.009500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.171200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.393500))
cmd.select('temp15', 'name  ce ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*4.878300))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*4.262200))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*3.444100))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*4.878300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.262200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.444100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp21', 'name  nz ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*5.464100))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*4.959100))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*3.878400))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.535100))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*1.504900))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*5.464100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*4.959100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*3.878400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.535100))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.504900))
cmd.select('temp28', 'name  cg ')
cmd.select('temp29', 'resn asp')
cmd.select('temp30', 'resn glu')
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*8.302200))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*7.585100))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*6.231700))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*4.868200))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*4.736900))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*3.514800))
cmd.select('jessatom6', '(((temp28 and temp29) or (temp28 and temp30)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.302200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*7.585100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*6.231700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*4.868200))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.736900))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*3.514800))
cmd.select('temp37', 'name  od1')
cmd.select('temp38', 'name  od2')
cmd.select('temp39', 'name  oe1')
cmd.select('temp40', 'name  oe2')
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*8.645600))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*7.908300))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*6.615500))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*4.353100))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*4.494500))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*3.444100))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*1.242300))
cmd.select('temp48', 'byres jessatom6')
cmd.select('jessatom7', '((((temp37 or temp38) and temp29) or ((temp39 or temp40) and temp30)) and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.645600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*7.908300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*6.615500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*4.353100))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*4.494500))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*3.444100))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.242300))
cmd.select('temp49', 'name  od2')
cmd.select('temp50', 'name  od1')
cmd.select('temp51', 'name  oe2')
cmd.select('temp52', 'name  oe1')
cmd.select('temp53', 'all within %s of (jessatom0)'%(d*7.817400))
cmd.select('temp54', 'all within %s of (jessatom1)'%(d*7.272000))
cmd.select('temp55', 'all within %s of (jessatom2)'%(d*5.938800))
cmd.select('temp56', 'all within %s of (jessatom3)'%(d*5.181300))
cmd.select('temp57', 'all within %s of (jessatom4)'%(d*4.676300))
cmd.select('temp58', 'all within %s of (jessatom5)'%(d*3.252200))
cmd.select('temp59', 'all within %s of (jessatom6)'%(d*1.222100))
cmd.select('temp60', 'byres jessatom6')
cmd.select('temp61', 'all within %s of (jessatom7)'%(d*2.151300))
cmd.select('jessatom8', '((((temp49 or temp50) and temp29) or ((temp51 or temp52) and temp30)) and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*7.817400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*7.272000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.938800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*5.181300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*4.676300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*3.252200))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.222100))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.151300))
cmd.select('Jfa_1cnz_1_1_1_85', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
cmd.delete('temp59')
cmd.delete('temp60')
cmd.delete('temp61')