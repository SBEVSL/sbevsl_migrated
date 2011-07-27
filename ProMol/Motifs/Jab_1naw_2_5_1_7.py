'''
FUNC:Jab_1naw_2_5_1_7
PDB:1naw
EC:2.5.1.7
RESI:asn,cys,asp,arg
LOCI:a-23,115,305,397;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn asn')
cmd.select('temp2', 'resn gln')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.535200))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.535200))
cmd.select('temp6', 'resn cys')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*27.835600))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*27.290200))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*27.835600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*27.290200))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*28.805200))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*28.239600))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.555400))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*28.805200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*28.239600))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp13', 'resn asp')
cmd.select('temp14', 'resn glu')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*12.200800))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*10.776700))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*27.956800))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*28.461800))
cmd.select('jessatom4', '(((temp0 and temp13) or (temp0 and temp14)) and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*12.200800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*10.776700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*27.956800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*28.461800))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*10.675700))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*9.261700))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*27.926500))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*28.502200))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(((temp3 and temp13) or (temp3 and temp14)) and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*10.675700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*9.261700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*27.926500))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*28.502200))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('temp25', 'resn arg')
cmd.select('temp26', 'all within %s of (jessatom0)'%(d*11.887700))
cmd.select('temp27', 'all within %s of (jessatom1)'%(d*11.998800))
cmd.select('temp28', 'all within %s of (jessatom2)'%(d*27.068000))
cmd.select('temp29', 'all within %s of (jessatom3)'%(d*27.532600))
cmd.select('temp30', 'all within %s of (jessatom4)'%(d*14.786400))
cmd.select('temp31', 'all within %s of (jessatom5)'%(d*13.948100))
cmd.select('jessatom6', '(temp0 and temp25 and temp26 and temp27 and temp28 and temp29 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*11.887700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*11.998800))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*27.068000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*27.532600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*14.786400))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*13.948100))
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*12.099800))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*12.130100))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*25.573200))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*26.017600))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*14.695500))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*13.907700))
cmd.select('temp38', 'all within %s of (jessatom6)'%(d*1.545300))
cmd.select('temp39', 'byres jessatom6')
cmd.select('jessatom7', '(temp3 and temp25 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*12.099800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*12.130100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*25.573200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*26.017600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*14.695500))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*13.907700))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.545300))
cmd.select('Jab_1naw_2_5_1_7', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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