'''
FUNC:Jab_2npx_1_11_1_1
PDB:2npx
EC:1.11.1.1
RESI:his,ser,arg
LOCI:a-10,41,303;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.504900))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.475248))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.504900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.475248))
cmd.select('temp6', 'name  n  ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*9.140500))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*8.960396))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*8.706200))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom1))'%((1./d)*8.534653))
cmd.select('jessatom2', '(((temp6) or (temp6)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*9.140500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*8.960396))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*8.706200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*8.534653))
cmd.select('temp9', 'name  ca ')
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*10.231300))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom0))'%((1./d)*10.029703))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*9.675800))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom1))'%((1./d)*9.485149))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*1.454400))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom2))'%((1./d)*1.425743))
cmd.select('temp13', 'byres jessatom2')
cmd.select('jessatom3', '(((temp9) or (temp9)) and temp10 and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.231300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*10.029703))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*9.675800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*9.485149))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.454400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.425743))
cmd.select('temp14', 'resn cys')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*10.625200))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom0))'%((1./d)*10.415842))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*9.645500))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom1))'%((1./d)*9.455446))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*4.272300))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom2))'%((1./d)*4.188119))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*3.898600))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom3))'%((1./d)*3.821782))
cmd.select('jessatom4', '(temp0 and temp14 and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*10.625200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*10.415842))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.645500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*9.455446))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.272300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*4.188119))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*3.898600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*3.821782))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*9.756600))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom0))'%((1./d)*9.564356))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*8.696100))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom1))'%((1./d)*8.524752))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*4.928800))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom2))'%((1./d)*4.831683))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*4.938900))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom3))'%((1./d)*4.841584))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom4))'%((1./d)*1.514851))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(temp2 and temp14 and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*9.756600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*9.564356))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*8.696100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*8.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.928800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*4.831683))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*4.938900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*4.841584))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.514851))
cmd.select('temp25', 'resn arg')
cmd.select('temp26', 'all within %s of (jessatom0)'%(d*5.544900))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom0))'%((1./d)*5.435644))
cmd.select('temp27', 'all within %s of (jessatom1)'%(d*5.221700))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom1))'%((1./d)*5.118812))
cmd.select('temp28', 'all within %s of (jessatom2)'%(d*13.675400))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom2))'%((1./d)*13.405941))
cmd.select('temp29', 'all within %s of (jessatom3)'%(d*14.604600))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom3))'%((1./d)*14.316832))
cmd.select('temp30', 'all within %s of (jessatom4)'%(d*13.725900))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom4))'%((1./d)*13.455446))
cmd.select('temp31', 'all within %s of (jessatom5)'%(d*12.463400))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom5))'%((1./d)*12.217822))
cmd.select('jessatom6', '(temp0 and temp25 and temp26 and temp27 and temp28 and temp29 and temp30 and temp31)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*5.544900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*5.435644))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*5.221700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*5.118812))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*13.675400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*13.405941))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*14.604600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*14.316832))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*13.725900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*13.455446))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*12.463400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*12.217822))
cmd.select('temp32', 'all within %s of (jessatom0)'%(d*5.676200))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom0))'%((1./d)*5.564356))
cmd.select('temp33', 'all within %s of (jessatom1)'%(d*5.171200))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom1))'%((1./d)*5.069307))
cmd.select('temp34', 'all within %s of (jessatom2)'%(d*13.099700))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom2))'%((1./d)*12.841584))
cmd.select('temp35', 'all within %s of (jessatom3)'%(d*14.049100))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom3))'%((1./d)*13.772277))
cmd.select('temp36', 'all within %s of (jessatom4)'%(d*12.877500))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom4))'%((1./d)*12.623762))
cmd.select('temp37', 'all within %s of (jessatom5)'%(d*11.534200))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom5))'%((1./d)*11.306931))
cmd.select('temp38', 'all within %s of (jessatom6)'%(d*1.595800))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom6))'%((1./d)*1.564356))
cmd.select('temp39', 'byres jessatom6')
cmd.select('jessatom7', '(temp2 and temp25 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*5.676200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*5.564356))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*5.171200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*5.069307))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*13.099700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*12.841584))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*14.049100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*13.772277))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*12.877500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*12.623762))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*11.534200))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*11.306931))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.595800))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.564356))
cmd.select('Jab_2npx_1_11_1_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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