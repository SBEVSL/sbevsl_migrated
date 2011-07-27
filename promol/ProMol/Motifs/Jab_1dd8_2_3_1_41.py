'''
FUNC:Jab_1dd8_2_3_1_41
PDB:1dd8
EC:2.3.1.41
RESI:cys,his,lys,his,phe,phe
LOCI:a-163,298,328,333,390,392;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn cys')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn cys')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('temp6', 'resn his')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*9.049600))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*7.979000))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*9.049600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*7.979000))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*8.443600))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*7.302300))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.535200))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp2 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.443600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*7.302300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.535200))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*8.514300))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*8.009300))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*9.382900))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*9.958600))
cmd.select('jessatom4', '(temp0 and temp6 and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*8.514300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*8.009300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*9.382900))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*9.958600))
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*8.019400))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*7.322500))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*9.049600))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*9.443500))
cmd.select('temp21', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp22', 'byres jessatom4')
cmd.select('jessatom5', '(temp2 and temp6 and temp17 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*8.019400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.322500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.049600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*9.443500))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('temp23', 'name  n  ')
cmd.select('temp24', 'all within %s of (jessatom0)'%(d*5.443900))
cmd.select('temp25', 'all within %s of (jessatom1)'%(d*4.959100))
cmd.select('temp26', 'all within %s of (jessatom2)'%(d*11.140300))
cmd.select('temp27', 'all within %s of (jessatom3)'%(d*9.958600))
cmd.select('temp28', 'all within %s of (jessatom4)'%(d*12.130100))
cmd.select('temp29', 'all within %s of (jessatom5)'%(d*11.059500))
cmd.select('jessatom6', '(temp23 and temp24 and temp25 and temp26 and temp27 and temp28 and temp29)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*5.443900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*4.959100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*11.140300))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*9.958600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*12.130100))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*11.059500))
cmd.select('temp30', 'all within %s of (jessatom0)'%(d*6.807400))
cmd.select('temp31', 'all within %s of (jessatom1)'%(d*6.352900))
cmd.select('temp32', 'all within %s of (jessatom2)'%(d*12.392700))
cmd.select('temp33', 'all within %s of (jessatom3)'%(d*11.170600))
cmd.select('temp34', 'all within %s of (jessatom4)'%(d*13.180500))
cmd.select('temp35', 'all within %s of (jessatom5)'%(d*12.029100))
cmd.select('temp36', 'all within %s of (jessatom6)'%(d*1.474600))
cmd.select('temp37', 'byres jessatom6')
cmd.select('jessatom7', '(temp0 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*6.807400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*6.352900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*12.392700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*11.170600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*13.180500))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*12.029100))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.474600))
cmd.select('Jab_1dd8_2_3_1_41', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
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