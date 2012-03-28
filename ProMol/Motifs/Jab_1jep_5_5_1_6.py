'''
FUNC:Jab_1jep_5_5_1_6
PDB:1jep
EC:5.5.1.6
RESI:thr,tyr,asn,thr
LOCI:a-48,106,113,190;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn thr')
cmd.select('temp2', 'resn ser')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.555400))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.524752))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.555400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.524752))
cmd.select('temp6', 'resn tyr')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*9.574800))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*9.386139))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*8.332500))
cmd.select('temp8', 'temp8 and not within %s of (jessatom1)'%((1./d)*8.168317))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*9.574800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*9.386139))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*8.332500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*8.168317))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*8.928400))
cmd.select('temp9', 'temp9 and not within %s of (jessatom0)'%((1./d)*8.752475))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*7.625500))
cmd.select('temp10', 'temp10 and not within %s of (jessatom1)'%((1./d)*7.475248))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp11', 'temp11 and not within %s of (jessatom2)'%((1./d)*1.514851))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*8.928400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*8.752475))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*7.625500))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*7.475248))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*1.514851))
cmd.select('temp13', 'resn asn')
cmd.select('temp14', 'resn gln')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*15.998400))
cmd.select('temp15', 'temp15 and not within %s of (jessatom0)'%((1./d)*15.683168))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*14.917700))
cmd.select('temp16', 'temp16 and not within %s of (jessatom1)'%((1./d)*14.623762))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*11.867500))
cmd.select('temp17', 'temp17 and not within %s of (jessatom2)'%((1./d)*11.633663))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*12.736100))
cmd.select('temp18', 'temp18 and not within %s of (jessatom3)'%((1./d)*12.485149))
cmd.select('jessatom4', '(((temp0 and temp13) or (temp0 and temp14)) and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*15.998400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*15.683168))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*14.917700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*14.623762))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*11.867500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*11.633663))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*12.736100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*12.485149))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*14.655100))
cmd.select('temp19', 'temp19 and not within %s of (jessatom0)'%((1./d)*14.366337))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*13.594600))
cmd.select('temp20', 'temp20 and not within %s of (jessatom1)'%((1./d)*13.326733))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*11.271600))
cmd.select('temp21', 'temp21 and not within %s of (jessatom2)'%((1./d)*11.049505))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*12.049300))
cmd.select('temp22', 'temp22 and not within %s of (jessatom3)'%((1./d)*11.811881))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp23', 'temp23 and not within %s of (jessatom4)'%((1./d)*1.514851))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(((temp3 and temp13) or (temp3 and temp14)) and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*14.655100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*14.366337))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*13.594600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*13.326733))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*11.271600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*11.049505))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*12.049300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*11.811881))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.514851))
cmd.select('temp25', 'all within %s of (jessatom0)'%(d*14.968200))
cmd.select('temp25', 'temp25 and not within %s of (jessatom0)'%((1./d)*14.673267))
cmd.select('temp26', 'all within %s of (jessatom1)'%(d*14.049100))
cmd.select('temp26', 'temp26 and not within %s of (jessatom1)'%((1./d)*13.772277))
cmd.select('temp27', 'all within %s of (jessatom2)'%(d*14.443000))
cmd.select('temp27', 'temp27 and not within %s of (jessatom2)'%((1./d)*14.158416))
cmd.select('temp28', 'all within %s of (jessatom3)'%(d*14.735900))
cmd.select('temp28', 'temp28 and not within %s of (jessatom3)'%((1./d)*14.445545))
cmd.select('temp29', 'all within %s of (jessatom4)'%(d*6.383200))
cmd.select('temp29', 'temp29 and not within %s of (jessatom4)'%((1./d)*6.257426))
cmd.select('temp30', 'all within %s of (jessatom5)'%(d*5.373200))
cmd.select('temp30', 'temp30 and not within %s of (jessatom5)'%((1./d)*5.267327))
cmd.select('jessatom6', '(((temp0 and temp1) or (temp0 and temp2)) and temp25 and temp26 and temp27 and temp28 and temp29 and temp30)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*14.968200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*14.673267))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*14.049100))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*13.772277))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*14.443000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*14.158416))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*14.735900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*14.445545))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.383200))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*6.257426))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*5.373200))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*5.267327))
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*14.372300))
cmd.select('temp31', 'temp31 and not within %s of (jessatom0)'%((1./d)*14.089109))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*13.362300))
cmd.select('temp32', 'temp32 and not within %s of (jessatom1)'%((1./d)*13.099010))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*13.069400))
cmd.select('temp33', 'temp33 and not within %s of (jessatom2)'%((1./d)*12.811881))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*13.422900))
cmd.select('temp34', 'temp34 and not within %s of (jessatom3)'%((1./d)*13.158416))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*5.090400))
cmd.select('temp35', 'temp35 and not within %s of (jessatom4)'%((1./d)*4.990099))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*4.009700))
cmd.select('temp36', 'temp36 and not within %s of (jessatom5)'%((1./d)*3.930693))
cmd.select('temp37', 'all within %s of (jessatom6)'%(d*1.565500))
cmd.select('temp37', 'temp37 and not within %s of (jessatom6)'%((1./d)*1.534653))
cmd.select('temp38', 'byres jessatom6')
cmd.select('jessatom7', '(((temp3 and temp1) or (temp3 and temp2)) and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*14.372300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*14.089109))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*13.362300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*13.099010))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*13.069400))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*12.811881))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*13.422900))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*13.158416))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*5.090400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*4.990099))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*4.009700))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*3.930693))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.565500))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.534653))
cmd.select('Jab_1jep_5_5_1_6', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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
