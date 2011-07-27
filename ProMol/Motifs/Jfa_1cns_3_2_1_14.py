'''
FUNC:Jfa_1cns_3_2_1_14
PDB:1cns
EC:3.2.1.14
RESI:glu,glu,ser
LOCI:a-67,89,120;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  oe1')
cmd.select('temp4', 'name  oe2')
cmd.select('temp5', 'name  od1')
cmd.select('temp6', 'name  od2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.262500))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.262500))
cmd.select('temp9', 'name  oe2')
cmd.select('temp10', 'name  oe1')
cmd.select('temp11', 'name  od2')
cmd.select('temp12', 'name  od1')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*1.242300))
cmd.select('temp14', 'byres jessatom0')
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*2.181600))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.242300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.181600))
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*10.372700))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*9.160700))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*11.261500))
cmd.select('jessatom3', '(((temp0 and temp1) or (temp0 and temp2)) and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.372700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*9.160700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*11.261500))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*9.938400))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*8.756700))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*10.817100))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*1.252400))
cmd.select('temp23', 'byres jessatom3')
cmd.select('jessatom4', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*9.938400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*8.756700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*10.817100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.252400))
cmd.select('temp24', 'all within %s of (jessatom0)'%(d*10.867600))
cmd.select('temp25', 'all within %s of (jessatom1)'%(d*9.625300))
cmd.select('temp26', 'all within %s of (jessatom2)'%(d*11.665500))
cmd.select('temp27', 'byres jessatom3')
cmd.select('temp28', 'all within %s of (jessatom4)'%(d*2.191700))
cmd.select('jessatom5', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp24 and temp25 and temp26 and temp22 and temp27 and temp28)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*10.867600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*9.625300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*11.665500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.252400))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.191700))
cmd.select('temp29', 'name  ca ')
cmd.select('temp30', 'resn ser')
cmd.select('temp31', 'resn thr')
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*10.231300))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*9.514200))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*10.857500))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*7.484100))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*6.241800))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*8.150700))
cmd.select('jessatom6', '(((temp29 and temp30) or (temp29 and temp31)) and temp32 and temp33 and temp34 and temp35 and temp36 and temp37)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*10.231300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.514200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*10.857500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*7.484100))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.241800))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.150700))
cmd.select('temp38', 'name  cb ')
cmd.select('temp39', 'all within %s of (jessatom0)'%(d*9.473800))
cmd.select('temp40', 'all within %s of (jessatom1)'%(d*8.655700))
cmd.select('temp41', 'all within %s of (jessatom2)'%(d*10.049500))
cmd.select('temp42', 'all within %s of (jessatom3)'%(d*6.625600))
cmd.select('temp43', 'all within %s of (jessatom4)'%(d*5.413600))
cmd.select('temp44', 'all within %s of (jessatom5)'%(d*7.150800))
cmd.select('temp45', 'all within %s of (jessatom6)'%(d*1.535200))
cmd.select('temp46', 'byres jessatom6')
cmd.select('jessatom7', '(((temp38 and temp30) or (temp38 and temp31)) and temp39 and temp40 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*9.473800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.655700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*10.049500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.625600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.413600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.150800))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.535200))
cmd.select('temp47', 'name  og ')
cmd.select('temp48', 'all within %s of (jessatom0)'%(d*9.241500))
cmd.select('temp49', 'all within %s of (jessatom1)'%(d*8.312300))
cmd.select('temp50', 'all within %s of (jessatom2)'%(d*9.938400))
cmd.select('temp51', 'all within %s of (jessatom3)'%(d*5.231800))
cmd.select('temp52', 'all within %s of (jessatom4)'%(d*3.999600))
cmd.select('temp53', 'all within %s of (jessatom5)'%(d*5.827700))
cmd.select('temp54', 'all within %s of (jessatom6)'%(d*2.434100))
cmd.select('temp55', 'byres jessatom6')
cmd.select('temp56', 'all within %s of (jessatom7)'%(d*1.424100))
cmd.select('jessatom8', '(((temp47 and temp30) or (temp47 and temp31)) and temp48 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*9.241500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*8.312300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*9.938400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*5.231800))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*3.999600))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*5.827700))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.434100))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.424100))
cmd.select('Jfa_1cns_3_2_1_14', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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