'''
FUNC:Jfa_1daa_2_6_1_21
PDB:1daa
EC:2.6.1.21
RESI:lys,glu,leu
LOCI:a-145,177,201;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn lys')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  ce ')
cmd.select('temp3', 'resn lys')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.535200))
cmd.select('temp4', 'temp4 and not within %s of (jessatom0)'%((1./d)*1.504950))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.535200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.504950))
cmd.select('temp6', 'name  nz ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.434100))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*2.386139))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.454400))
cmd.select('temp9', 'temp9 and not within %s of (jessatom1)'%((1./d)*1.425743))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.434100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*2.386139))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.454400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*1.425743))
cmd.select('temp10', 'resn glu')
cmd.select('temp11', 'resn asp')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*10.079800))
cmd.select('temp12', 'temp12 and not within %s of (jessatom0)'%((1./d)*9.881188))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*10.433300))
cmd.select('temp13', 'temp13 and not within %s of (jessatom1)'%((1./d)*10.227723))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*9.312200))
cmd.select('temp14', 'temp14 and not within %s of (jessatom2)'%((1./d)*9.128713))
cmd.select('jessatom3', '(((temp0 and temp10) or (temp0 and temp11)) and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*10.079800))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*9.881188))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*10.433300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*10.227723))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*9.312200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*9.128713))
cmd.select('temp15', 'name  oe1')
cmd.select('temp16', 'name  oe2')
cmd.select('temp17', 'name  od1')
cmd.select('temp18', 'name  od2')
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*9.332400))
cmd.select('temp19', 'temp19 and not within %s of (jessatom0)'%((1./d)*9.148515))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*9.665700))
cmd.select('temp20', 'temp20 and not within %s of (jessatom1)'%((1./d)*9.475248))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*8.564800))
cmd.select('temp21', 'temp21 and not within %s of (jessatom2)'%((1./d)*8.396040))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*1.232200))
cmd.select('temp22', 'temp22 and not within %s of (jessatom3)'%((1./d)*1.207921))
cmd.select('temp23', 'byres jessatom3')
cmd.select('jessatom4', '((((temp15 or temp16) and temp10) or ((temp17 or temp18) and temp11)) and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*9.332400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*9.148515))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.665700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*9.475248))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*8.564800))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*8.396040))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.232200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.207921))
cmd.select('temp24', 'name  oe2')
cmd.select('temp25', 'name  oe1')
cmd.select('temp26', 'name  od2')
cmd.select('temp27', 'name  od1')
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*9.837400))
cmd.select('temp28', 'temp28 and not within %s of (jessatom0)'%((1./d)*9.643564))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*10.302000))
cmd.select('temp29', 'temp29 and not within %s of (jessatom1)'%((1./d)*10.099010))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*9.241500))
cmd.select('temp30', 'temp30 and not within %s of (jessatom2)'%((1./d)*9.059406))
cmd.select('temp22', 'temp22 and not within %s of (jessatom3)'%((1./d)*1.207921))
cmd.select('temp31', 'byres jessatom3')
cmd.select('temp32', 'all within %s of (jessatom4)'%(d*2.121000))
cmd.select('temp32', 'temp32 and not within %s of (jessatom4)'%((1./d)*2.079208))
cmd.select('jessatom5', '((((temp24 or temp25) and temp10) or ((temp26 or temp27) and temp11)) and temp28 and temp29 and temp30 and temp22 and temp31 and temp32)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*9.837400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*9.643564))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*10.302000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*10.099010))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.241500))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*9.059406))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.232200))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*1.207921))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.121000))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*2.079208))
cmd.select('temp33', 'name  cg ')
cmd.select('temp34', 'resn leu')
cmd.select('temp35', 'all within %s of (jessatom0)'%(d*5.019700))
cmd.select('temp35', 'temp35 and not within %s of (jessatom0)'%((1./d)*4.920792))
cmd.select('temp36', 'all within %s of (jessatom1)'%(d*5.898400))
cmd.select('temp36', 'temp36 and not within %s of (jessatom1)'%((1./d)*5.782178))
cmd.select('temp37', 'all within %s of (jessatom2)'%(d*5.474200))
cmd.select('temp37', 'temp37 and not within %s of (jessatom2)'%((1./d)*5.366337))
cmd.select('temp38', 'all within %s of (jessatom3)'%(d*6.201400))
cmd.select('temp38', 'temp38 and not within %s of (jessatom3)'%((1./d)*6.079208))
cmd.select('temp39', 'all within %s of (jessatom4)'%(d*5.312600))
cmd.select('temp39', 'temp39 and not within %s of (jessatom4)'%((1./d)*5.207921))
cmd.select('temp40', 'all within %s of (jessatom5)'%(d*6.100400))
cmd.select('temp40', 'temp40 and not within %s of (jessatom5)'%((1./d)*5.980198))
cmd.select('jessatom6', '(temp33 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*5.019700))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*4.920792))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*5.898400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*5.782178))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*5.474200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*5.366337))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*6.201400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*6.079208))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*5.312600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*5.207921))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*6.100400))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*5.980198))
cmd.select('temp41', 'name  cd1')
cmd.select('temp42', 'name  cd2')
cmd.select('temp43', 'all within %s of (jessatom0)'%(d*4.757100))
cmd.select('temp43', 'temp43 and not within %s of (jessatom0)'%((1./d)*4.663366))
cmd.select('temp44', 'all within %s of (jessatom1)'%(d*5.948900))
cmd.select('temp44', 'temp44 and not within %s of (jessatom1)'%((1./d)*5.831683))
cmd.select('temp45', 'all within %s of (jessatom2)'%(d*5.817600))
cmd.select('temp45', 'temp45 and not within %s of (jessatom2)'%((1./d)*5.702970))
cmd.select('temp46', 'all within %s of (jessatom3)'%(d*7.130600))
cmd.select('temp46', 'temp46 and not within %s of (jessatom3)'%((1./d)*6.990099))
cmd.select('temp47', 'all within %s of (jessatom4)'%(d*6.403400))
cmd.select('temp47', 'temp47 and not within %s of (jessatom4)'%((1./d)*6.277228))
cmd.select('temp48', 'all within %s of (jessatom5)'%(d*6.797300))
cmd.select('temp48', 'temp48 and not within %s of (jessatom5)'%((1./d)*6.663366))
cmd.select('temp49', 'all within %s of (jessatom6)'%(d*1.535200))
cmd.select('temp49', 'temp49 and not within %s of (jessatom6)'%((1./d)*1.504950))
cmd.select('temp50', 'byres jessatom6')
cmd.select('jessatom7', '((temp41 or temp42) and temp34 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*4.757100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*4.663366))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*5.948900))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*5.831683))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*5.817600))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*5.702970))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*7.130600))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*6.990099))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*6.403400))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*6.277228))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*6.797300))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*6.663366))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.535200))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*1.504950))
cmd.select('temp51', 'name  cd2')
cmd.select('temp52', 'name  cd1')
cmd.select('temp53', 'all within %s of (jessatom0)'%(d*3.999600))
cmd.select('temp53', 'temp53 and not within %s of (jessatom0)'%((1./d)*3.920792))
cmd.select('temp54', 'all within %s of (jessatom1)'%(d*4.615700))
cmd.select('temp54', 'temp54 and not within %s of (jessatom1)'%((1./d)*4.524752))
cmd.select('temp55', 'all within %s of (jessatom2)'%(d*4.040000))
cmd.select('temp55', 'temp55 and not within %s of (jessatom2)'%((1./d)*3.960396))
cmd.select('temp56', 'all within %s of (jessatom3)'%(d*6.534700))
cmd.select('temp56', 'temp56 and not within %s of (jessatom3)'%((1./d)*6.405941))
cmd.select('temp57', 'all within %s of (jessatom4)'%(d*5.615600))
cmd.select('temp57', 'temp57 and not within %s of (jessatom4)'%((1./d)*5.504950))
cmd.select('temp58', 'all within %s of (jessatom5)'%(d*6.514500))
cmd.select('temp58', 'temp58 and not within %s of (jessatom5)'%((1./d)*6.386139))
cmd.select('temp59', 'all within %s of (jessatom6)'%(d*1.515000))
cmd.select('temp59', 'temp59 and not within %s of (jessatom6)'%((1./d)*1.485149))
cmd.select('temp60', 'byres jessatom6')
cmd.select('temp61', 'all within %s of (jessatom7)'%(d*2.504800))
cmd.select('temp61', 'temp61 and not within %s of (jessatom7)'%((1./d)*2.455446))
cmd.select('jessatom8', '((temp51 or temp52) and temp34 and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*3.999600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*3.920792))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*4.615700))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*4.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*4.040000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*3.960396))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*6.534700))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*6.405941))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*5.615600))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*5.504950))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*6.514500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*6.386139))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*1.515000))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*1.485149))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.504800))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.455446))
cmd.select('Jfa_1daa_2_6_1_21', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
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
cmd.delete('temp40')
cmd.delete('temp41')
cmd.delete('temp42')
cmd.delete('temp43')
cmd.delete('temp44')
cmd.delete('temp45')
cmd.delete('temp46')
cmd.delete('temp47')
cmd.delete('temp48')
cmd.delete('temp49')
cmd.delete('temp50')
cmd.delete('temp51')
cmd.delete('temp52')
cmd.delete('temp53')
cmd.delete('temp54')
cmd.delete('temp55')
cmd.delete('temp56')
cmd.delete('temp57')
cmd.delete('temp58')
cmd.delete('temp59')
cmd.delete('temp60')
cmd.delete('temp61')
