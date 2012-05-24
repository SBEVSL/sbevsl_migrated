'''
FUNC:Jab_1edd_3_8_1_5
PDB:1edd
EC:3.8.1.5
RESI:asp,asp,his
LOCI:a-124,260,289;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.565500))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.565500))
cmd.select('temp6', 'all within %s of (jessatom0)'%(d*11.392800))
cmd.select('temp7', 'all within %s of (jessatom1)'%(d*11.009000))
cmd.select('jessatom2', '(((temp0 and temp1) or (temp0 and temp2)) and temp6 and temp7)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*11.392800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*11.009000))
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*10.009100))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*9.716200))
cmd.select('temp10', 'all within %s of (jessatom2)'%(d*1.575600))
cmd.select('temp11', 'byres jessatom2')
cmd.select('jessatom3', '(((temp3 and temp1) or (temp3 and temp2)) and temp8 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.009100))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*9.716200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.575600))
cmd.select('temp12', 'resn his')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*8.221400))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*7.463900))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*4.787400))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*3.939000))
cmd.select('jessatom4', '(temp0 and temp12 and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*8.221400))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*7.463900))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.787400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*3.939000))
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*7.847700))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*6.938700))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*5.161100))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*4.474300))
cmd.select('temp21', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp22', 'byres jessatom4')
cmd.select('jessatom5', '(temp3 and temp12 and temp17 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.847700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*6.938700))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*5.161100))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*4.474300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('Jab_1edd_3_8_1_5', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
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