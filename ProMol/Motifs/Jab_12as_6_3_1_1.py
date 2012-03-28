'''
FUNC:Jab_12as_6_3_1_1
PDB:12as
EC:6.3.1.1
RESI:asp,arg,gln
LOCI:a-46,100,116;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.555400))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.524752))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.555400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.524752))
cmd.select('temp6', 'resn arg')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*11.301900))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*11.079208))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*10.776700))
cmd.select('temp8', 'temp8 and not within %s of (jessatom1)'%((1./d)*10.564356))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*11.301900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*11.079208))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*10.776700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*10.564356))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*10.978700))
cmd.select('temp9', 'temp9 and not within %s of (jessatom0)'%((1./d)*10.762376))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*10.302000))
cmd.select('temp10', 'temp10 and not within %s of (jessatom1)'%((1./d)*10.099010))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.555400))
cmd.select('temp11', 'temp11 and not within %s of (jessatom2)'%((1./d)*1.524752))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.978700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*10.762376))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*10.302000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*10.099010))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.555400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*1.524752))
cmd.select('temp13', 'resn gln')
cmd.select('temp14', 'resn asn')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*13.655200))
cmd.select('temp15', 'temp15 and not within %s of (jessatom0)'%((1./d)*13.386139))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*12.150300))
cmd.select('temp16', 'temp16 and not within %s of (jessatom1)'%((1./d)*11.910891))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*12.705800))
cmd.select('temp17', 'temp17 and not within %s of (jessatom2)'%((1./d)*12.455446))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*11.806900))
cmd.select('temp18', 'temp18 and not within %s of (jessatom3)'%((1./d)*11.574257))
cmd.select('jessatom4', '(((temp0 and temp13) or (temp0 and temp14)) and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*13.655200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*13.386139))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*12.150300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*11.910891))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*12.705800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*12.455446))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*11.806900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*11.574257))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*12.251300))
cmd.select('temp19', 'temp19 and not within %s of (jessatom0)'%((1./d)*12.009901))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*10.726200))
cmd.select('temp20', 'temp20 and not within %s of (jessatom1)'%((1./d)*10.514851))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*12.140200))
cmd.select('temp21', 'temp21 and not within %s of (jessatom2)'%((1./d)*11.900990))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*11.190800))
cmd.select('temp22', 'temp22 and not within %s of (jessatom3)'%((1./d)*10.970297))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp23', 'temp23 and not within %s of (jessatom4)'%((1./d)*1.514851))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(((temp3 and temp13) or (temp3 and temp14)) and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*12.251300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*12.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*10.726200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*10.514851))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*12.140200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*11.900990))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*11.190800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*10.970297))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.514851))
cmd.select('Jab_12as_6_3_1_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
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
