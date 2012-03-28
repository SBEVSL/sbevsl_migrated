'''
FUNC:Jab_1bg4_3_2_1_8
PDB:1bg4
EC:3.2.1.8
RESI:glu,his,glu,asp
LOCI:a-132,210,238,240;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.555400))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.524752))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.555400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.524752))
cmd.select('temp6', 'resn his')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*13.130000))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*12.871287))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*12.473500))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom1))'%((1./d)*12.227723))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*13.130000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*12.871287))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*12.473500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*12.227723))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*12.190700))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom0))'%((1./d)*11.950495))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*11.402900))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom1))'%((1./d)*11.178218))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom2))'%((1./d)*1.514851))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*12.190700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*11.950495))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*11.402900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*11.178218))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.514851))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*12.685600))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom0))'%((1./d)*12.435644))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*12.301800))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom1))'%((1./d)*12.059406))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*6.605400))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom2))'%((1./d)*6.475248))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*6.767000))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom3))'%((1./d)*6.633663))
cmd.select('jessatom4', '(((temp0 and temp1) or (temp0 and temp2)) and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*12.685600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*12.435644))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*12.301800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*12.059406))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*6.605400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*6.475248))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*6.767000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*6.633663))
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*11.413000))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom0))'%((1./d)*11.188119))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*10.928200))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom1))'%((1./d)*10.712871))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*6.342800))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom2))'%((1./d)*6.217822))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*6.161000))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom3))'%((1./d)*6.039604))
cmd.select('temp21', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom4))'%((1./d)*1.514851))
cmd.select('temp22', 'byres jessatom4')
cmd.select('jessatom5', '(((temp3 and temp1) or (temp3 and temp2)) and temp17 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.413000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*11.188119))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*10.928200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*10.712871))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*6.342800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*6.217822))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*6.161000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*6.039604))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.514851))
cmd.select('temp23', 'all within %s of (jessatom0)'%(d*17.351800))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom0))'%((1./d)*17.009901))
cmd.select('temp24', 'all within %s of (jessatom1)'%(d*16.675100))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom1))'%((1./d)*16.346535))
cmd.select('temp25', 'all within %s of (jessatom2)'%(d*5.252000))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom2))'%((1./d)*5.148515))
cmd.select('temp26', 'all within %s of (jessatom3)'%(d*6.100400))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom3))'%((1./d)*5.980198))
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*6.686200))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom4))'%((1./d)*6.554455))
cmd.select('temp28', 'all within %s of (jessatom5)'%(d*7.282100))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom5))'%((1./d)*7.138614))
cmd.select('jessatom6', '(((temp0 and temp2) or (temp0 and temp1)) and temp23 and temp24 and temp25 and temp26 and temp27 and temp28)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*17.351800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*17.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*16.675100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*16.346535))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*5.252000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*5.148515))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*6.100400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*5.980198))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.686200))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*6.554455))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.282100))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*7.138614))
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*17.159900))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom0))'%((1./d)*16.821782))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*16.372100))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom1))'%((1./d)*16.049505))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*5.565100))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom2))'%((1./d)*5.455446))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*6.039800))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom3))'%((1./d)*5.920792))
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*6.736700))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom4))'%((1./d)*6.603960))
cmd.select('temp34', 'all within %s of (jessatom5)'%(d*7.110400))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom5))'%((1./d)*6.970297))
cmd.select('temp35', 'all within %s of (jessatom6)'%(d*1.565500))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom6))'%((1./d)*1.534653))
cmd.select('temp36', 'byres jessatom6')
cmd.select('jessatom7', '(((temp3 and temp2) or (temp3 and temp1)) and temp29 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*17.159900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*16.821782))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*16.372100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*16.049505))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*5.565100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*5.455446))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*6.039800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*5.920792))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*6.736700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*6.603960))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.110400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*6.970297))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.565500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.534653))
cmd.select('Jab_1bg4_3_2_1_8', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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