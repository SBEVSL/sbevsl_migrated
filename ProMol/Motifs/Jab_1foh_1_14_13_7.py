'''
FUNC:Jab_1foh_1_14_13_7
PDB:1foh
EC:1.14.13.7
RESI:asp,arg,tyr
LOCI:a-54,281,289;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.535200))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.504950))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.535200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.504950))
cmd.select('temp6', 'resn arg')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*8.635500))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*8.465347))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*7.474000))
cmd.select('temp8', 'temp8 and not within %s of (jessatom1)'%((1./d)*7.326733))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*8.635500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*8.465347))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*7.474000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*7.326733))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*7.928500))
cmd.select('temp9', 'temp9 and not within %s of (jessatom0)'%((1./d)*7.772277))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*6.625600))
cmd.select('temp10', 'temp10 and not within %s of (jessatom1)'%((1./d)*6.495050))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.555400))
cmd.select('temp11', 'temp11 and not within %s of (jessatom2)'%((1./d)*1.524752))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*7.928500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*7.772277))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*6.625600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*6.495050))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.555400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*1.524752))
cmd.select('temp13', 'resn tyr')
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*12.352300))
cmd.select('temp14', 'temp14 and not within %s of (jessatom0)'%((1./d)*12.108911))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*11.332200))
cmd.select('temp15', 'temp15 and not within %s of (jessatom1)'%((1./d)*11.108911))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*12.827000))
cmd.select('temp16', 'temp16 and not within %s of (jessatom2)'%((1./d)*12.574257))
cmd.select('temp17', 'all within %s of (jessatom3)'%(d*12.039200))
cmd.select('temp17', 'temp17 and not within %s of (jessatom3)'%((1./d)*11.801980))
cmd.select('jessatom4', '(temp0 and temp13 and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*12.352300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*12.108911))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*11.332200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*11.108911))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*12.827000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*12.574257))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*12.039200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*11.801980))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*11.857400))
cmd.select('temp18', 'temp18 and not within %s of (jessatom0)'%((1./d)*11.623762))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*10.978700))
cmd.select('temp19', 'temp19 and not within %s of (jessatom1)'%((1./d)*10.762376))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*12.988600))
cmd.select('temp20', 'temp20 and not within %s of (jessatom2)'%((1./d)*12.732673))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*12.281600))
cmd.select('temp21', 'temp21 and not within %s of (jessatom3)'%((1./d)*12.039604))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.525100))
cmd.select('temp22', 'temp22 and not within %s of (jessatom4)'%((1./d)*1.495050))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(temp3 and temp13 and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.857400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*11.623762))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*10.978700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*10.762376))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*12.988600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*12.732673))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*12.281600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*12.039604))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.525100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.495050))
cmd.select('Jab_1foh_1_14_13_7', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
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
