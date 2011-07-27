'''
FUNC:Jfa_1brl_1_14_14_3
PDB:1brl
EC:1.14.14.3
RESI:his,his,phe
LOCI:a-4,45,261;
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
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.191700))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.191700))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.191700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.191700))
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*6.039800))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*5.999400))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*6.908400))
cmd.select('jessatom3', '(temp0 and temp3 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*6.039800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.999400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*6.908400))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*6.878100))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*7.059900))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*7.857800))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*1.414000))
cmd.select('temp17', 'byres jessatom3')
cmd.select('jessatom4', '(temp2 and temp3 and temp13 and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*6.878100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*7.059900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*7.857800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.414000))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*7.080100))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*8.403200))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*2.222000))
cmd.select('temp21', 'byres jessatom3')
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*2.201800))
cmd.select('jessatom5', '(temp6 and temp3 and temp18 and temp14 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.080100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.059900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*8.403200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.222000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.201800))
cmd.select('temp23', 'name  ce1')
cmd.select('temp24', 'name  ce2')
cmd.select('temp25', 'resn phe')
cmd.select('temp26', 'all within %s of (jessatom0)'%(d*14.180400))
cmd.select('temp27', 'all within %s of (jessatom1)'%(d*12.958300))
cmd.select('temp28', 'all within %s of (jessatom2)'%(d*12.746200))
cmd.select('temp29', 'all within %s of (jessatom3)'%(d*15.008600))
cmd.select('temp30', 'all within %s of (jessatom4)'%(d*16.331700))
cmd.select('temp31', 'all within %s of (jessatom5)'%(d*16.351900))
cmd.select('jessatom6', '((temp23 or temp24) and temp25 and temp26 and temp27 and temp28 and temp29 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*14.180400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*12.958300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*12.746200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*15.008600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*16.331700))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*16.351900))
cmd.select('temp32', 'name  ce2')
cmd.select('temp33', 'name  ce1')
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*16.149900))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*14.937900))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*14.655100))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*17.372000))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*18.705200))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*18.715300))
cmd.select('temp40', 'all within %s of (jessatom6)'%(d*2.454300))
cmd.select('temp41', 'byres jessatom6')
cmd.select('jessatom7', '((temp32 or temp33) and temp25 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*16.149900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*14.937900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*14.655100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*17.372000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*18.705200))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*18.715300))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*2.454300))
cmd.select('temp42', 'name  cz ')
cmd.select('temp43', 'all within %s of (jessatom0)'%(d*14.958100))
cmd.select('temp44', 'all within %s of (jessatom1)'%(d*13.705700))
cmd.select('temp45', 'all within %s of (jessatom2)'%(d*13.534000))
cmd.select('temp46', 'all within %s of (jessatom3)'%(d*16.099400))
cmd.select('temp47', 'all within %s of (jessatom4)'%(d*17.442700))
cmd.select('temp48', 'all within %s of (jessatom5)'%(d*17.382100))
cmd.select('temp49', 'all within %s of (jessatom6)'%(d*1.414000))
cmd.select('temp50', 'byres jessatom6')
cmd.select('temp51', 'all within %s of (jessatom7)'%(d*1.414000))
cmd.select('jessatom8', '(temp42 and temp25 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50 and temp51)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*14.958100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*13.705700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*13.534000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*16.099400))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*17.442700))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*17.382100))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.414000))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.414000))
cmd.select('Jfa_1brl_1_14_14_3', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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