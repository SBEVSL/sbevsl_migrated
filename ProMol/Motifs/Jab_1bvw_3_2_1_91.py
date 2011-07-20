'''
FUNC:Jab_1bvw_3_2_1_91
PDB:1bvw
EC:3.2.1.91
RESI:tyr,arg,asp,asp
LOCI:a-174,179,180,226;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn tyr')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn tyr')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('temp6', 'resn arg')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*8.484000))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*8.847600))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*8.484000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*8.847600))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*7.362900))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*7.665900))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.555400))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp2 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*7.362900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*7.665900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp13', 'resn asp')
cmd.select('temp14', 'resn glu')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*9.968700))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*9.827300))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*3.817800))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*4.464200))
cmd.select('jessatom4', '(((temp0 and temp13) or (temp0 and temp14)) and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*9.968700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.827300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.817800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*4.464200))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*9.908100))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*9.584900))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*4.413700))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*4.605600))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(((temp2 and temp13) or (temp2 and temp14)) and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*9.908100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*9.584900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.413700))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*4.605600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('temp25', 'all within %s of (jessatom0)'%(d*9.039500))
cmd.select('temp26', 'all within %s of (jessatom1)'%(d*8.635500))
cmd.select('temp27', 'all within %s of (jessatom2)'%(d*8.100200))
cmd.select('temp28', 'all within %s of (jessatom3)'%(d*8.271900))
cmd.select('temp29', 'all within %s of (jessatom4)'%(d*5.898400))
cmd.select('temp30', 'all within %s of (jessatom5)'%(d*6.393300))
cmd.select('jessatom6', '(((temp0 and temp13) or (temp0 and temp14)) and temp25 and temp26 and temp27 and temp28 and temp29 and temp30)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*9.039500))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*8.635500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*8.100200))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*8.271900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*5.898400))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*6.393300))
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*8.948600))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*8.383000))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*7.635600))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*7.676000))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*5.100500))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*5.272200))
cmd.select('temp37', 'all within %s of (jessatom6)'%(d*1.545300))
cmd.select('temp38', 'byres jessatom6')
cmd.select('jessatom7', '(((temp2 and temp13) or (temp2 and temp14)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.948600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*8.383000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*7.635600))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.676000))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.100500))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*5.272200))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.545300))
cmd.select('Jab_1bvw_3_2_1_91', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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