'''
FUNC:Jab_1h17_2_3_1_54
PDB:1h17
EC:2.3.1.54
RESI:trp,cys,cys,gly
LOCI:a-333,418,419,734;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn trp')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn trp')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.514851))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.514851))
cmd.select('temp6', 'resn cys')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*5.140900))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*5.039604))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*3.878400))
cmd.select('temp8', 'temp8 and not within %s of (jessatom1)'%((1./d)*3.801980))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*5.140900))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*5.039604))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*3.878400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*3.801980))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*6.130700))
cmd.select('temp9', 'temp9 and not within %s of (jessatom0)'%((1./d)*6.009901))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*4.686400))
cmd.select('temp10', 'temp10 and not within %s of (jessatom1)'%((1./d)*4.594059))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp11', 'temp11 and not within %s of (jessatom2)'%((1./d)*1.514851))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp2 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*6.130700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*6.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.686400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*4.594059))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*1.514851))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*7.272000))
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*7.128713))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*6.383200))
cmd.select('temp14', 'temp14 and not within %s of (jessatom1)'%((1./d)*6.257426))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*3.848100))
cmd.select('temp15', 'temp15 and not within %s of (jessatom2)'%((1./d)*3.772277))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*4.191500))
cmd.select('temp16', 'temp16 and not within %s of (jessatom3)'%((1./d)*4.108911))
cmd.select('jessatom4', '(temp0 and temp6 and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*7.272000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*7.128713))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.383200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*6.257426))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.848100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*3.772277))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*4.191500))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*4.108911))
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*7.979000))
cmd.select('temp17', 'temp17 and not within %s of (jessatom0)'%((1./d)*7.821782))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*7.029600))
cmd.select('temp18', 'temp18 and not within %s of (jessatom1)'%((1./d)*6.891089))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*4.797500))
cmd.select('temp19', 'temp19 and not within %s of (jessatom2)'%((1./d)*4.702970))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*4.726800))
cmd.select('temp20', 'temp20 and not within %s of (jessatom3)'%((1./d)*4.633663))
cmd.select('temp21', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp21', 'temp21 and not within %s of (jessatom4)'%((1./d)*1.514851))
cmd.select('temp22', 'byres jessatom4')
cmd.select('jessatom5', '(temp2 and temp6 and temp17 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*7.979000))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*7.821782))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*7.029600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*6.891089))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.797500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*4.702970))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*4.726800))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*4.633663))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.514851))
cmd.select('temp23', 'resn gly')
cmd.select('temp24', 'all within %s of (jessatom0)'%(d*9.261700))
cmd.select('temp24', 'temp24 and not within %s of (jessatom0)'%((1./d)*9.079208))
cmd.select('temp25', 'all within %s of (jessatom1)'%(d*8.776900))
cmd.select('temp25', 'temp25 and not within %s of (jessatom1)'%((1./d)*8.603960))
cmd.select('temp26', 'all within %s of (jessatom2)'%(d*7.847700))
cmd.select('temp26', 'temp26 and not within %s of (jessatom2)'%((1./d)*7.693069))
cmd.select('temp27', 'all within %s of (jessatom3)'%(d*8.019400))
cmd.select('temp27', 'temp27 and not within %s of (jessatom3)'%((1./d)*7.861386))
cmd.select('temp28', 'all within %s of (jessatom4)'%(d*4.575300))
cmd.select('temp28', 'temp28 and not within %s of (jessatom4)'%((1./d)*4.485149))
cmd.select('temp29', 'all within %s of (jessatom5)'%(d*3.646100))
cmd.select('temp29', 'temp29 and not within %s of (jessatom5)'%((1./d)*3.574257))
cmd.select('jessatom6', '(temp0 and temp23 and temp24 and temp25 and temp26 and temp27 and temp28 and temp29)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*9.261700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*9.079208))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*8.776900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*8.603960))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*7.847700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*7.693069))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*8.019400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*7.861386))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*4.575300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*4.485149))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*3.646100))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*3.574257))
cmd.select('temp30', 'name  c  ')
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*7.888100))
cmd.select('temp31', 'temp31 and not within %s of (jessatom0)'%((1./d)*7.732673))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*7.554800))
cmd.select('temp32', 'temp32 and not within %s of (jessatom1)'%((1./d)*7.405941))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*7.090200))
cmd.select('temp33', 'temp33 and not within %s of (jessatom2)'%((1./d)*6.950495))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*7.484100))
cmd.select('temp34', 'temp34 and not within %s of (jessatom3)'%((1./d)*7.336634))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*4.252100))
cmd.select('temp35', 'temp35 and not within %s of (jessatom4)'%((1./d)*4.168317))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*3.696600))
cmd.select('temp36', 'temp36 and not within %s of (jessatom5)'%((1./d)*3.623762))
cmd.select('temp37', 'all within %s of (jessatom6)'%(d*1.535200))
cmd.select('temp37', 'temp37 and not within %s of (jessatom6)'%((1./d)*1.504950))
cmd.select('temp38', 'byres jessatom6')
cmd.select('jessatom7', '(temp30 and temp23 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*7.888100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*7.732673))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*7.554800))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*7.405941))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*7.090200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*6.950495))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.484100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*7.336634))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*4.252100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*4.168317))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*3.696600))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*3.623762))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.535200))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.504950))
cmd.select('Jab_1h17_2_3_1_54', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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
