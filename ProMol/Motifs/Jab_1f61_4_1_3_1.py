'''
FUNC:Jab_1f61_4_1_3_1
PDB:1f61
EC:4.1.3.1
RESI:his,cys,arg
LOCI:a-180,191,228;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.565500))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.534653))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.565500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.534653))
cmd.select('temp6', 'resn cys')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*25.149000))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*24.653465))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*24.623800))
cmd.select('temp8', 'temp8 and not within %s of (jessatom1)'%((1./d)*24.138614))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*25.149000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*24.653465))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*24.623800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*24.138614))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*25.755000))
cmd.select('temp9', 'temp9 and not within %s of (jessatom0)'%((1./d)*25.247525))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*25.239900))
cmd.select('temp10', 'temp10 and not within %s of (jessatom1)'%((1./d)*24.742574))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.555400))
cmd.select('temp11', 'temp11 and not within %s of (jessatom2)'%((1./d)*1.524752))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp2 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*25.755000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*25.247525))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*25.239900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*24.742574))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.555400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*1.524752))
cmd.select('temp13', 'resn arg')
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*6.696300))
cmd.select('temp14', 'temp14 and not within %s of (jessatom0)'%((1./d)*6.564356))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*6.060000))
cmd.select('temp15', 'temp15 and not within %s of (jessatom1)'%((1./d)*5.940594))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*22.119000))
cmd.select('temp16', 'temp16 and not within %s of (jessatom2)'%((1./d)*21.683168))
cmd.select('temp17', 'all within %s of (jessatom3)'%(d*23.048200))
cmd.select('temp17', 'temp17 and not within %s of (jessatom3)'%((1./d)*22.594059))
cmd.select('jessatom4', '(temp0 and temp13 and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*6.696300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*6.564356))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.060000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*5.940594))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*22.119000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*21.683168))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*23.048200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*22.594059))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*6.100400))
cmd.select('temp18', 'temp18 and not within %s of (jessatom0)'%((1./d)*5.980198))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*5.292400))
cmd.select('temp19', 'temp19 and not within %s of (jessatom1)'%((1./d)*5.188119))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*21.321100))
cmd.select('temp20', 'temp20 and not within %s of (jessatom2)'%((1./d)*20.900990))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*22.179600))
cmd.select('temp21', 'temp21 and not within %s of (jessatom3)'%((1./d)*21.742574))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp22', 'temp22 and not within %s of (jessatom4)'%((1./d)*1.524752))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(temp2 and temp13 and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*6.100400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*5.980198))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*5.292400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*5.188119))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*21.321100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*20.900990))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*22.179600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*21.742574))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.524752))
cmd.select('Jab_1f61_4_1_3_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
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
