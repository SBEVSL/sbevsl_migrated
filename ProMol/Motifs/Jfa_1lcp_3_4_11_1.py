'''
FUNC:Jfa_1lcp_3_4_11_1
PDB:1lcp
EC:3.4.11.1
RESI:asp,lys,arg
LOCI:a-255,262,336;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn asp')
cmd.select('temp2', 'resn glu')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  od1')
cmd.select('temp4', 'name  od2')
cmd.select('temp5', 'name  oe1')
cmd.select('temp6', 'name  oe2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*1.272600))
cmd.select('temp7', 'temp7 and not within %s of (jessatom0)'%((1./d)*1.247525))
cmd.select('temp8', 'byres jessatom0')
cmd.select('jessatom1', '((((temp3 or temp4) and temp1) or ((temp5 or temp6) and temp2)) and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.272600))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom1)'%((1./d)*1.247525))
cmd.select('temp9', 'name  od2')
cmd.select('temp10', 'name  od1')
cmd.select('temp11', 'name  oe2')
cmd.select('temp12', 'name  oe1')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*1.262500))
cmd.select('temp13', 'temp13 and not within %s of (jessatom0)'%((1./d)*1.237624))
cmd.select('temp14', 'byres jessatom0')
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*2.222000))
cmd.select('temp15', 'temp15 and not within %s of (jessatom1)'%((1./d)*2.178218))
cmd.select('jessatom2', '((((temp9 or temp10) and temp1) or ((temp11 or temp12) and temp2)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*1.262500))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom2)'%((1./d)*1.237624))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom2)'%((1./d)*2.178218))
cmd.select('temp16', 'name  cd ')
cmd.select('temp17', 'resn lys')
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*4.858100))
cmd.select('temp18', 'temp18 and not within %s of (jessatom0)'%((1./d)*4.762376))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*5.070200))
cmd.select('temp19', 'temp19 and not within %s of (jessatom1)'%((1./d)*4.970297))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*4.878300))
cmd.select('temp20', 'temp20 and not within %s of (jessatom2)'%((1./d)*4.782178))
cmd.select('jessatom3', '(temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.858100))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom3)'%((1./d)*4.762376))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.070200))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom3)'%((1./d)*4.970297))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*4.878300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom3)'%((1./d)*4.782178))
cmd.select('temp21', 'name  ce ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*3.666300))
cmd.select('temp22', 'temp22 and not within %s of (jessatom0)'%((1./d)*3.594059))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*4.080400))
cmd.select('temp23', 'temp23 and not within %s of (jessatom1)'%((1./d)*4.000000))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*3.444100))
cmd.select('temp24', 'temp24 and not within %s of (jessatom2)'%((1./d)*3.376238))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*1.545300))
cmd.select('temp25', 'temp25 and not within %s of (jessatom3)'%((1./d)*1.514851))
cmd.select('temp26', 'byres jessatom3')
cmd.select('jessatom4', '(temp21 and temp17 and temp22 and temp23 and temp24 and temp25 and temp26)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*3.666300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom4)'%((1./d)*3.594059))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*4.080400))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom4)'%((1./d)*4.000000))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*3.444100))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom4)'%((1./d)*3.376238))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.545300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom4)'%((1./d)*1.514851))
cmd.select('temp27', 'name  nz ')
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*4.373300))
cmd.select('temp28', 'temp28 and not within %s of (jessatom0)'%((1./d)*4.287129))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*4.807600))
cmd.select('temp29', 'temp29 and not within %s of (jessatom1)'%((1./d)*4.712871))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*3.757200))
cmd.select('temp30', 'temp30 and not within %s of (jessatom2)'%((1./d)*3.683168))
cmd.select('temp31', 'all within %s of (jessatom3)'%(d*2.535100))
cmd.select('temp31', 'temp31 and not within %s of (jessatom3)'%((1./d)*2.485149))
cmd.select('temp32', 'byres jessatom3')
cmd.select('temp33', 'all within %s of (jessatom4)'%(d*1.504900))
cmd.select('temp33', 'temp33 and not within %s of (jessatom4)'%((1./d)*1.475248))
cmd.select('jessatom5', '(temp27 and temp17 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*4.373300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom5)'%((1./d)*4.287129))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*4.807600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom5)'%((1./d)*4.712871))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*3.757200))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom5)'%((1./d)*3.683168))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.535100))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom5)'%((1./d)*2.485149))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.504900))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom5)'%((1./d)*1.475248))
cmd.select('temp34', 'name  ne ')
cmd.select('temp35', 'resn arg')
cmd.select('temp36', 'all within %s of (jessatom0)'%(d*11.140300))
cmd.select('temp36', 'temp36 and not within %s of (jessatom0)'%((1./d)*10.920792))
cmd.select('temp37', 'all within %s of (jessatom1)'%(d*11.241300))
cmd.select('temp37', 'temp37 and not within %s of (jessatom1)'%((1./d)*11.019802))
cmd.select('temp38', 'all within %s of (jessatom2)'%(d*10.201000))
cmd.select('temp38', 'temp38 and not within %s of (jessatom2)'%((1./d)*10.000000))
cmd.select('temp39', 'all within %s of (jessatom3)'%(d*13.564300))
cmd.select('temp39', 'temp39 and not within %s of (jessatom3)'%((1./d)*13.297030))
cmd.select('temp40', 'all within %s of (jessatom4)'%(d*12.231100))
cmd.select('temp40', 'temp40 and not within %s of (jessatom4)'%((1./d)*11.990099))
cmd.select('temp41', 'all within %s of (jessatom5)'%(d*11.211000))
cmd.select('temp41', 'temp41 and not within %s of (jessatom5)'%((1./d)*10.990099))
cmd.select('jessatom6', '(temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*11.140300))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom6)'%((1./d)*10.920792))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*11.241300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom6)'%((1./d)*11.019802))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*10.201000))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom6)'%((1./d)*10.000000))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*13.564300))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom6)'%((1./d)*13.297030))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*12.231100))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom6)'%((1./d)*11.990099))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*11.211000))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom6)'%((1./d)*10.990099))
cmd.select('temp42', 'name  nh1')
cmd.select('temp43', 'name  nh2')
cmd.select('temp44', 'all within %s of (jessatom0)'%(d*12.948200))
cmd.select('temp44', 'temp44 and not within %s of (jessatom0)'%((1./d)*12.693069))
cmd.select('temp45', 'all within %s of (jessatom1)'%(d*13.059300))
cmd.select('temp45', 'temp45 and not within %s of (jessatom1)'%((1./d)*12.801980))
cmd.select('temp46', 'all within %s of (jessatom2)'%(d*11.948300))
cmd.select('temp46', 'temp46 and not within %s of (jessatom2)'%((1./d)*11.712871))
cmd.select('temp47', 'all within %s of (jessatom3)'%(d*14.786400))
cmd.select('temp47', 'temp47 and not within %s of (jessatom3)'%((1./d)*14.495050))
cmd.select('temp48', 'all within %s of (jessatom4)'%(d*13.554200))
cmd.select('temp48', 'temp48 and not within %s of (jessatom4)'%((1./d)*13.287129))
cmd.select('temp49', 'all within %s of (jessatom5)'%(d*12.372500))
cmd.select('temp49', 'temp49 and not within %s of (jessatom5)'%((1./d)*12.128713))
cmd.select('temp50', 'all within %s of (jessatom6)'%(d*2.343200))
cmd.select('temp50', 'temp50 and not within %s of (jessatom6)'%((1./d)*2.297030))
cmd.select('temp51', 'byres jessatom6')
cmd.select('jessatom7', '((temp42 or temp43) and temp35 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50 and temp51)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*12.948200))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom7)'%((1./d)*12.693069))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*13.059300))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom7)'%((1./d)*12.801980))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*11.948300))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom7)'%((1./d)*11.712871))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*14.786400))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom7)'%((1./d)*14.495050))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*13.554200))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom7)'%((1./d)*13.287129))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*12.372500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom7)'%((1./d)*12.128713))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*2.343200))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom7)'%((1./d)*2.297030))
cmd.select('temp52', 'name  nh2')
cmd.select('temp53', 'name  nh1')
cmd.select('temp54', 'all within %s of (jessatom0)'%(d*11.049400))
cmd.select('temp54', 'temp54 and not within %s of (jessatom0)'%((1./d)*10.831683))
cmd.select('temp55', 'all within %s of (jessatom1)'%(d*11.271600))
cmd.select('temp55', 'temp55 and not within %s of (jessatom1)'%((1./d)*11.049505))
cmd.select('temp56', 'all within %s of (jessatom2)'%(d*9.968700))
cmd.select('temp56', 'temp56 and not within %s of (jessatom2)'%((1./d)*9.772277))
cmd.select('temp57', 'all within %s of (jessatom3)'%(d*12.726000))
cmd.select('temp57', 'temp57 and not within %s of (jessatom3)'%((1./d)*12.475248))
cmd.select('temp58', 'all within %s of (jessatom4)'%(d*11.463500))
cmd.select('temp58', 'temp58 and not within %s of (jessatom4)'%((1./d)*11.237624))
cmd.select('temp59', 'all within %s of (jessatom5)'%(d*10.251500))
cmd.select('temp59', 'temp59 and not within %s of (jessatom5)'%((1./d)*10.049505))
cmd.select('temp60', 'all within %s of (jessatom6)'%(d*2.312900))
cmd.select('temp60', 'temp60 and not within %s of (jessatom6)'%((1./d)*2.267327))
cmd.select('temp61', 'byres jessatom6')
cmd.select('temp62', 'all within %s of (jessatom7)'%(d*2.312900))
cmd.select('temp62', 'temp62 and not within %s of (jessatom7)'%((1./d)*2.267327))
cmd.select('jessatom8', '((temp52 or temp53) and temp35 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61 and temp62)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*11.049400))
cmd.select('jessatom0', 'jessatom0 and not within %s of (jessatom8)'%((1./d)*10.831683))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*11.271600))
cmd.select('jessatom1', 'jessatom1 and not within %s of (jessatom8)'%((1./d)*11.049505))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*9.968700))
cmd.select('jessatom2', 'jessatom2 and not within %s of (jessatom8)'%((1./d)*9.772277))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*12.726000))
cmd.select('jessatom3', 'jessatom3 and not within %s of (jessatom8)'%((1./d)*12.475248))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*11.463500))
cmd.select('jessatom4', 'jessatom4 and not within %s of (jessatom8)'%((1./d)*11.237624))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*10.251500))
cmd.select('jessatom5', 'jessatom5 and not within %s of (jessatom8)'%((1./d)*10.049505))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.312900))
cmd.select('jessatom6', 'jessatom6 and not within %s of (jessatom8)'%((1./d)*2.267327))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*2.312900))
cmd.select('jessatom7', 'jessatom7 and not within %s of (jessatom8)'%((1./d)*2.267327))
cmd.select('Jfa_1lcp_3_4_11_1', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8')
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
cmd.delete('temp62')
