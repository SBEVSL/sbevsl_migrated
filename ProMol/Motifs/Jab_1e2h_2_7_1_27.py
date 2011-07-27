'''
FUNC:Jab_1e2h_2_7_1_27
PDB:1e2h
EC:2.7.1.27
RESI:gly,glu,arg,arg
LOCI:a-59,83,163,222;
'''
cmd.select('temp0', 'name  n  ')
cmd.select('jessatom0', '(temp0)')
cmd.select('temp1', 'name  ca ')
cmd.select('temp2', 'all within %s of (jessatom0)'%(d*1.454400))
cmd.select('temp3', 'byres jessatom0')
cmd.select('jessatom1', '(temp1 and temp2 and temp3)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.454400))
cmd.select('temp4', 'resn glu')
cmd.select('temp5', 'resn asp')
cmd.select('temp6', 'all within %s of (jessatom0)'%(d*12.079600))
cmd.select('temp7', 'all within %s of (jessatom1)'%(d*13.180500))
cmd.select('jessatom2', '(((temp1 and temp4) or (temp1 and temp5)) and temp6 and temp7)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*12.079600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*13.180500))
cmd.select('temp8', 'name  cb ')
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*10.776700))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*11.827100))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(((temp8 and temp4) or (temp8 and temp5)) and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.776700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*11.827100))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp13', 'resn arg')
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*11.786700))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*13.109800))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*7.615400))
cmd.select('temp17', 'all within %s of (jessatom3)'%(d*8.029500))
cmd.select('jessatom4', '(temp1 and temp13 and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*11.786700))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*13.109800))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*7.615400))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*8.029500))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*11.170600))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*12.544200))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*7.070000))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*7.383100))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(temp8 and temp13 and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.170600))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*12.544200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*7.070000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*7.383100))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('temp24', 'all within %s of (jessatom0)'%(d*9.271800))
cmd.select('temp25', 'all within %s of (jessatom1)'%(d*9.514200))
cmd.select('temp26', 'all within %s of (jessatom2)'%(d*11.443300))
cmd.select('temp27', 'all within %s of (jessatom3)'%(d*10.059600))
cmd.select('temp28', 'all within %s of (jessatom4)'%(d*15.877200))
cmd.select('temp29', 'all within %s of (jessatom5)'%(d*14.776300))
cmd.select('jessatom6', '(temp1 and temp13 and temp24 and temp25 and temp26 and temp27 and temp28 and temp29)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*9.271800))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*9.514200))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*11.443300))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*10.059600))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*15.877200))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*14.776300))
cmd.select('temp30', 'all within %s of (jessatom0)'%(d*8.675900))
cmd.select('temp31', 'all within %s of (jessatom1)'%(d*9.140500))
cmd.select('temp32', 'all within %s of (jessatom2)'%(d*10.180800))
cmd.select('temp33', 'all within %s of (jessatom3)'%(d*8.817300))
cmd.select('temp34', 'all within %s of (jessatom4)'%(d*14.453100))
cmd.select('temp35', 'all within %s of (jessatom5)'%(d*13.301700))
cmd.select('temp36', 'all within %s of (jessatom6)'%(d*1.555400))
cmd.select('temp37', 'byres jessatom6')
cmd.select('jessatom7', '(temp8 and temp13 and temp30 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*8.675900))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*9.140500))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*10.180800))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*8.817300))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*14.453100))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*13.301700))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.555400))
cmd.select('Jab_1e2h_2_7_1_27', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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