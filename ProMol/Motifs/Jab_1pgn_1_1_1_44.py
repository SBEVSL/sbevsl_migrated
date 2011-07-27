'''
FUNC:Jab_1pgn_1_1_1_44
PDB:1pgn
EC:1.1.1.44
RESI:gly,lys,asn,glu
LOCI:a-130,183,187,190;
'''
cmd.select('temp0', 'name  n  ')
cmd.select('jessatom0', '(temp0)')
cmd.select('temp1', 'name  ca ')
cmd.select('temp2', 'all within %s of (jessatom0)'%(d*1.464500))
cmd.select('temp3', 'byres jessatom0')
cmd.select('jessatom1', '(temp1 and temp2 and temp3)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.464500))
cmd.select('temp4', 'resn lys')
cmd.select('temp5', 'all within %s of (jessatom0)'%(d*12.180600))
cmd.select('temp6', 'all within %s of (jessatom1)'%(d*13.231000))
cmd.select('jessatom2', '(temp1 and temp4 and temp5 and temp6)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*12.180600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*13.231000))
cmd.select('temp7', 'name  cb ')
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*11.766500))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*12.746200))
cmd.select('temp10', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp11', 'byres jessatom2')
cmd.select('jessatom3', '(temp7 and temp4 and temp8 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*11.766500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*12.746200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp12', 'resn asn')
cmd.select('temp13', 'resn gln')
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*11.534200))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*12.281600))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*6.575100))
cmd.select('temp17', 'all within %s of (jessatom3)'%(d*7.433600))
cmd.select('jessatom4', '(((temp1 and temp12) or (temp1 and temp13)) and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*11.534200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*12.281600))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*6.575100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*7.433600))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*11.392800))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*12.019000))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*6.433700))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*7.039700))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.525100))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(((temp7 and temp12) or (temp7 and temp13)) and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.392800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*12.019000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*6.433700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*7.039700))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.525100))
cmd.select('temp24', 'resn glu')
cmd.select('temp25', 'resn asp')
cmd.select('temp26', 'all within %s of (jessatom0)'%(d*12.513900))
cmd.select('temp27', 'all within %s of (jessatom1)'%(d*13.210800))
cmd.select('temp28', 'all within %s of (jessatom2)'%(d*10.584800))
cmd.select('temp29', 'all within %s of (jessatom3)'%(d*11.615000))
cmd.select('temp30', 'all within %s of (jessatom4)'%(d*4.686400))
cmd.select('temp31', 'all within %s of (jessatom5)'%(d*5.928700))
cmd.select('jessatom6', '(((temp1 and temp24) or (temp1 and temp25)) and temp26 and temp27 and temp28 and temp29 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*12.513900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*13.210800))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*10.584800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*11.615000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.686400))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*5.928700))
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*11.160500))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*11.837200))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*9.716200))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*10.605000))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*3.807700))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*4.918700))
cmd.select('temp38', 'all within %s of (jessatom6)'%(d*1.515000))
cmd.select('temp39', 'byres jessatom6')
cmd.select('jessatom7', '(((temp7 and temp24) or (temp7 and temp25)) and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*11.160500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*11.837200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*9.716200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*10.605000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*3.807700))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*4.918700))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.515000))
cmd.select('Jab_1pgn_1_1_1_44', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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
cmd.delete('temp38')
cmd.delete('temp39')