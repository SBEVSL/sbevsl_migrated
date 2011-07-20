'''
FUNC:Jab_1afr_1_14_19_2
PDB:1afr
EC:1.14.19.2
RESI:trp,his,thr,asp
LOCI:a-62,146,199,228;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn trp')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn trp')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('temp6', 'resn his')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*10.554500))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*10.049500))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*10.554500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*10.049500))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*11.322100))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*10.776700))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.555400))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp2 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*11.322100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*10.776700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp13', 'resn thr')
cmd.select('temp14', 'resn ser')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*18.523400))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*17.523500))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*11.261500))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*9.887900))
cmd.select('jessatom4', '(((temp0 and temp13) or (temp0 and temp14)) and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*18.523400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*17.523500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*11.261500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*9.887900))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*17.624500))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*16.725600))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*10.120200))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*8.675900))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(((temp2 and temp13) or (temp2 and temp14)) and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*17.624500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*16.725600))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*10.120200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*8.675900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('temp25', 'resn asp')
cmd.select('temp26', 'resn glu')
cmd.select('temp27', 'all within %s of (jessatom0)'%(d*10.150500))
cmd.select('temp28', 'all within %s of (jessatom1)'%(d*9.433400))
cmd.select('temp29', 'all within %s of (jessatom2)'%(d*9.231400))
cmd.select('temp30', 'all within %s of (jessatom3)'%(d*8.443600))
cmd.select('temp31', 'all within %s of (jessatom4)'%(d*10.039400))
cmd.select('temp32', 'all within %s of (jessatom5)'%(d*9.251600))
cmd.select('jessatom6', '(((temp0 and temp25) or (temp0 and temp26)) and temp27 and temp28 and temp29 and temp30 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*10.150500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.433400))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*9.231400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*8.443600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*10.039400))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*9.251600))
cmd.select('temp33', 'all within %s of (jessatom0)'%(d*9.362700))
cmd.select('temp34', 'all within %s of (jessatom1)'%(d*8.706200))
cmd.select('temp35', 'all within %s of (jessatom2)'%(d*7.807300))
cmd.select('temp36', 'all within %s of (jessatom3)'%(d*7.090200))
cmd.select('temp37', 'all within %s of (jessatom4)'%(d*10.130300))
cmd.select('temp38', 'all within %s of (jessatom5)'%(d*9.180900))
cmd.select('temp39', 'all within %s of (jessatom6)'%(d*1.555400))
cmd.select('temp40', 'byres jessatom6')
cmd.select('jessatom7', '(((temp2 and temp25) or (temp2 and temp26)) and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*9.362700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.706200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*7.807300))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.090200))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*10.130300))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*9.180900))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.555400))
cmd.select('Jab_1afr_1_14_19_2', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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
cmd.delete('temp40')