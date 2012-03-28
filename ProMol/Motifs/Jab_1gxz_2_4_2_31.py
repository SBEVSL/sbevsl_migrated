'''
FUNC:Jab_1gxz_2_4_2_31
PDB:1gxz
EC:2.4.2.31
RESI:ser,glu,arg,glu
LOCI:a-147,159,184,189;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn ser')
cmd.select('temp2', 'resn thr')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.514851))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.514851))
cmd.select('temp6', 'resn glu')
cmd.select('temp7', 'resn asp')
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*13.109800))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom0))'%((1./d)*12.851485))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*11.948300))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*11.712871))
cmd.select('jessatom2', '(((temp0 and temp6) or (temp0 and temp7)) and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*13.109800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*12.851485))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*11.948300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*11.712871))
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*12.554300))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom0))'%((1./d)*12.306931))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*11.342300))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom1))'%((1./d)*11.118812))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom2))'%((1./d)*1.514851))
cmd.select('temp13', 'byres jessatom2')
cmd.select('jessatom3', '(((temp3 and temp6) or (temp3 and temp7)) and temp10 and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*12.554300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*12.306931))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*11.342300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*11.118812))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.514851))
cmd.select('temp14', 'resn arg')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*12.382600))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom0))'%((1./d)*12.138614))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*11.241300))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom1))'%((1./d)*11.019802))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*12.604800))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom2))'%((1./d)*12.356436))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*11.099900))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom3))'%((1./d)*10.881188))
cmd.select('jessatom4', '(temp0 and temp14 and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*12.382600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*12.138614))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*11.241300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*11.019802))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*12.604800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*12.356436))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*11.099900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*10.881188))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*11.554400))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom0))'%((1./d)*11.326733))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*10.332300))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom1))'%((1./d)*10.128713))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*11.099900))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom2))'%((1./d)*10.881188))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*9.605100))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom3))'%((1./d)*9.415842))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom4))'%((1./d)*1.514851))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(temp3 and temp14 and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*11.554400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*11.326733))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*10.332300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*10.128713))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*11.099900))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*10.881188))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*9.605100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*9.415842))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.514851))
cmd.select('temp25', 'all within %s of (jessatom0)'%(d*6.605400))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom0))'%((1./d)*6.475248))
cmd.select('temp26', 'all within %s of (jessatom1)'%(d*6.524600))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom1))'%((1./d)*6.396040))
cmd.select('temp27', 'all within %s of (jessatom2)'%(d*13.857200))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom2))'%((1./d)*13.584158))
cmd.select('temp28', 'all within %s of (jessatom3)'%(d*12.746200))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom3))'%((1./d)*12.495050))
cmd.select('temp29', 'all within %s of (jessatom4)'%(d*8.605200))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom4))'%((1./d)*8.435644))
cmd.select('temp30', 'all within %s of (jessatom5)'%(d*8.352700))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom5))'%((1./d)*8.188119))
cmd.select('jessatom6', '(((temp0 and temp6) or (temp0 and temp7)) and temp25 and temp26 and temp27 and temp28 and temp29 and temp30)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*6.605400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*6.475248))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*6.524600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*6.396040))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*13.857200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*13.584158))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*12.746200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*12.495050))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*8.605200))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*8.435644))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*8.352700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*8.188119))
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*5.989300))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom0))'%((1./d)*5.871287))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*5.656000))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom1))'%((1./d)*5.544554))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*13.412800))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom2))'%((1./d)*13.148515))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*12.281600))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom3))'%((1./d)*12.039604))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*7.817400))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom4))'%((1./d)*7.663366))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*7.504300))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom5))'%((1./d)*7.356436))
cmd.select('temp37', 'all within %s of (jessatom6)'%(d*1.545300))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom6))'%((1./d)*1.514851))
cmd.select('temp38', 'byres jessatom6')
cmd.select('jessatom7', '(((temp3 and temp6) or (temp3 and temp7)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*5.989300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*5.871287))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*5.656000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*5.544554))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*13.412800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*13.148515))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*12.281600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*12.039604))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*7.817400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*7.663366))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*7.504300))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*7.356436))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.545300))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.514851))
cmd.select('Jab_1gxz_2_4_2_31', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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