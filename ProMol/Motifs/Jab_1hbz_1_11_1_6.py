'''
FUNC:Jab_1hbz_1_11_1_6
PDB:1hbz
EC:1.11.1.6
RESI:his,ser,asn
LOCI:a-61,99,133;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.555400))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.555400))
cmd.select('temp6', 'resn ser')
cmd.select('temp7', 'resn thr')
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*5.686300))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*5.454000))
cmd.select('jessatom2', '(((temp0 and temp6) or (temp0 and temp7)) and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*5.686300))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*5.454000))
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*4.413700))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*4.029900))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp13', 'byres jessatom2')
cmd.select('jessatom3', '(((temp2 and temp6) or (temp2 and temp7)) and temp10 and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.413700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.029900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp14', 'resn asn')
cmd.select('temp15', 'resn gln')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*10.716100))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*9.615200))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*9.079900))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*9.110200))
cmd.select('jessatom4', '(((temp0 and temp14) or (temp0 and temp15)) and temp16 and temp17 and temp18 and temp19)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*10.716100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.615200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*9.079900))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*9.110200))
cmd.select('temp20', 'all within %s of (jessatom0)'%(d*10.524200))
cmd.select('temp21', 'all within %s of (jessatom1)'%(d*9.524300))
cmd.select('temp22', 'all within %s of (jessatom2)'%(d*9.534400))
cmd.select('temp23', 'all within %s of (jessatom3)'%(d*9.483900))
cmd.select('temp24', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp25', 'byres jessatom4')
cmd.select('jessatom5', '(((temp2 and temp14) or (temp2 and temp15)) and temp20 and temp21 and temp22 and temp23 and temp24 and temp25)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*10.524200))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*9.524300))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.534400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*9.483900))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('Jab_1hbz_1_11_1_6', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
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