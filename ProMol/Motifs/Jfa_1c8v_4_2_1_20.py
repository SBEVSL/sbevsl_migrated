'''
FUNC:Jfa_1c8v_4_2_1_20
PDB:1c8v
EC:4.2.1.20
RESI:his,lys,lys,asp
LOCI:b-86,87,167,305;
'''
cmd.select('temp0', 'name  cg ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  nd1')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.393800))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.366337))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.393800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.366337))
cmd.select('temp6', 'name  ne2')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.222000))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*2.178218))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*2.161400))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*2.118812))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.222000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*2.178218))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*2.161400))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*2.118812))
cmd.select('temp10', 'name  cd ')
cmd.select('temp11', 'resn lys')
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*6.241800))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom0))'%((1./d)*6.118812))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*5.666100))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom1))'%((1./d)*5.554455))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*5.373200))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom2))'%((1./d)*5.267327))
cmd.select('jessatom3', '(temp10 and temp11 and temp12 and temp13 and temp14)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*6.241800))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*6.118812))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*5.666100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*5.554455))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*5.373200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*5.267327))
cmd.select('temp15', 'name  ce ')
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*6.878100))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom0))'%((1./d)*6.742574))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*6.140800))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom1))'%((1./d)*6.019802))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*5.585300))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom2))'%((1./d)*5.475248))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*1.555400))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom3))'%((1./d)*1.524752))
cmd.select('temp20', 'byres jessatom3')
cmd.select('jessatom4', '(temp15 and temp11 and temp16 and temp17 and temp18 and temp19 and temp20)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*6.878100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*6.742574))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*6.140800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*6.019802))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*5.585300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*5.475248))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.555400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.524752))
cmd.select('temp21', 'name  nz ')
cmd.select('temp22', 'all within %s of (jessatom0)'%(d*6.292300))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom0))'%((1./d)*6.168317))
cmd.select('temp23', 'all within %s of (jessatom1)'%(d*5.433800))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom1))'%((1./d)*5.326733))
cmd.select('temp24', 'all within %s of (jessatom2)'%(d*4.757100))
cmd.select('temp24', 'temp24 and not (all within %s of (jessatom2))'%((1./d)*4.663366))
cmd.select('temp25', 'all within %s of (jessatom3)'%(d*2.615900))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom3))'%((1./d)*2.564356))
cmd.select('temp26', 'byres jessatom3')
cmd.select('temp27', 'all within %s of (jessatom4)'%(d*1.474600))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom4))'%((1./d)*1.445545))
cmd.select('jessatom5', '(temp21 and temp11 and temp22 and temp23 and temp24 and temp25 and temp26 and temp27)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*6.292300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*6.168317))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*5.433800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*5.326733))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*4.757100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*4.663366))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*2.615900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*2.564356))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.474600))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.445545))
cmd.select('temp28', 'all within %s of (jessatom0)'%(d*23.048200))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom0))'%((1./d)*22.594059))
cmd.select('temp29', 'all within %s of (jessatom1)'%(d*22.270500))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom1))'%((1./d)*21.831683))
cmd.select('temp30', 'all within %s of (jessatom2)'%(d*20.927200))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom2))'%((1./d)*20.514851))
cmd.select('temp31', 'all within %s of (jessatom3)'%(d*19.159700))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom3))'%((1./d)*18.782178))
cmd.select('temp32', 'all within %s of (jessatom4)'%(d*17.685100))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom4))'%((1./d)*17.336634))
cmd.select('temp33', 'all within %s of (jessatom5)'%(d*17.432600))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom5))'%((1./d)*17.089109))
cmd.select('jessatom6', '(temp10 and temp11 and temp28 and temp29 and temp30 and temp31 and temp32 and temp33)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*23.048200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*22.594059))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*22.270500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*21.831683))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*20.927200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*20.514851))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*19.159700))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*18.782178))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*17.685100))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*17.336634))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*17.432600))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*17.089109))
cmd.select('temp34', 'all within %s of (jessatom0)'%(d*24.007700))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom0))'%((1./d)*23.534653))
cmd.select('temp35', 'all within %s of (jessatom1)'%(d*23.189600))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom1))'%((1./d)*22.732673))
cmd.select('temp36', 'all within %s of (jessatom2)'%(d*21.927100))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom2))'%((1./d)*21.495050))
cmd.select('temp37', 'all within %s of (jessatom3)'%(d*19.886900))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom3))'%((1./d)*19.495050))
cmd.select('temp38', 'all within %s of (jessatom4)'%(d*18.422400))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom4))'%((1./d)*18.059406))
cmd.select('temp39', 'all within %s of (jessatom5)'%(d*18.230500))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom5))'%((1./d)*17.871287))
cmd.select('temp40', 'all within %s of (jessatom6)'%(d*1.545300))
cmd.select('temp40', 'temp40 and not (all within %s of (jessatom6))'%((1./d)*1.514851))
cmd.select('temp41', 'byres jessatom6')
cmd.select('jessatom7', '(temp15 and temp11 and temp34 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40 and temp41)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*24.007700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*23.534653))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*23.189600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*22.732673))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*21.927100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*21.495050))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*19.886900))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*19.495050))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*18.422400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*18.059406))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*18.230500))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*17.871287))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.545300))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.514851))
cmd.select('temp42', 'all within %s of (jessatom0)'%(d*25.179300))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom0))'%((1./d)*24.683168))
cmd.select('temp43', 'all within %s of (jessatom1)'%(d*24.391500))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom1))'%((1./d)*23.910891))
cmd.select('temp44', 'all within %s of (jessatom2)'%(d*23.088600))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom2))'%((1./d)*22.633663))
cmd.select('temp45', 'all within %s of (jessatom3)'%(d*20.927200))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom3))'%((1./d)*20.514851))
cmd.select('temp46', 'all within %s of (jessatom4)'%(d*19.493000))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom4))'%((1./d)*19.108911))
cmd.select('temp47', 'all within %s of (jessatom5)'%(d*19.381900))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom5))'%((1./d)*19.000000))
cmd.select('temp48', 'all within %s of (jessatom6)'%(d*2.585600))
cmd.select('temp48', 'temp48 and not (all within %s of (jessatom6))'%((1./d)*2.534653))
cmd.select('temp49', 'byres jessatom6')
cmd.select('temp50', 'all within %s of (jessatom7)'%(d*1.504900))
cmd.select('temp50', 'temp50 and not (all within %s of (jessatom7))'%((1./d)*1.475248))
cmd.select('jessatom8', '(temp21 and temp11 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48 and temp49 and temp50)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*25.179300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*24.683168))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*24.391500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*23.910891))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*23.088600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*22.633663))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*20.927200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*20.514851))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*19.493000))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*19.108911))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*19.381900))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*19.000000))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.585600))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*2.534653))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.504900))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*1.475248))
cmd.select('temp51', 'resn asp')
cmd.select('temp52', 'resn glu')
cmd.select('temp53', 'all within %s of (jessatom0)'%(d*16.493300))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom0))'%((1./d)*16.168317))
cmd.select('temp54', 'all within %s of (jessatom1)'%(d*15.311600))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom1))'%((1./d)*15.009901))
cmd.select('temp55', 'all within %s of (jessatom2)'%(d*14.847000))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom2))'%((1./d)*14.554455))
cmd.select('temp56', 'all within %s of (jessatom3)'%(d*13.513800))
cmd.select('temp56', 'temp56 and not (all within %s of (jessatom3))'%((1./d)*13.247525))
cmd.select('temp57', 'all within %s of (jessatom4)'%(d*12.069500))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom4))'%((1./d)*11.831683))
cmd.select('temp58', 'all within %s of (jessatom5)'%(d*11.382700))
cmd.select('temp58', 'temp58 and not (all within %s of (jessatom5))'%((1./d)*11.158416))
cmd.select('temp59', 'all within %s of (jessatom6)'%(d*10.897900))
cmd.select('temp59', 'temp59 and not (all within %s of (jessatom6))'%((1./d)*10.683168))
cmd.select('temp60', 'all within %s of (jessatom7)'%(d*11.200900))
cmd.select('temp60', 'temp60 and not (all within %s of (jessatom7))'%((1./d)*10.980198))
cmd.select('temp61', 'all within %s of (jessatom8)'%(d*12.655300))
cmd.select('temp61', 'temp61 and not (all within %s of (jessatom8))'%((1./d)*12.405941))
cmd.select('jessatom9', '(((temp0 and temp51) or (temp0 and temp52)) and temp53 and temp54 and temp55 and temp56 and temp57 and temp58 and temp59 and temp60 and temp61)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*16.493300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom9))'%((1./d)*16.168317))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*15.311600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom9))'%((1./d)*15.009901))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*14.847000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom9))'%((1./d)*14.554455))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*13.513800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom9))'%((1./d)*13.247525))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*12.069500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom9))'%((1./d)*11.831683))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*11.382700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom9))'%((1./d)*11.158416))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*10.897900))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom9))'%((1./d)*10.683168))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*11.200900))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom9))'%((1./d)*10.980198))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*12.655300))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom9))'%((1./d)*12.405941))
cmd.select('temp62', 'name  od1')
cmd.select('temp63', 'name  od2')
cmd.select('temp64', 'name  oe1')
cmd.select('temp65', 'name  oe2')
cmd.select('temp66', 'all within %s of (jessatom0)'%(d*17.341700))
cmd.select('temp66', 'temp66 and not (all within %s of (jessatom0))'%((1./d)*17.000000))
cmd.select('temp67', 'all within %s of (jessatom1)'%(d*16.129700))
cmd.select('temp67', 'temp67 and not (all within %s of (jessatom1))'%((1./d)*15.811881))
cmd.select('temp68', 'all within %s of (jessatom2)'%(d*15.756000))
cmd.select('temp68', 'temp68 and not (all within %s of (jessatom2))'%((1./d)*15.445545))
cmd.select('temp69', 'all within %s of (jessatom3)'%(d*14.109700))
cmd.select('temp69', 'temp69 and not (all within %s of (jessatom3))'%((1./d)*13.831683))
cmd.select('temp70', 'all within %s of (jessatom4)'%(d*12.695700))
cmd.select('temp70', 'temp70 and not (all within %s of (jessatom4))'%((1./d)*12.445545))
cmd.select('temp71', 'all within %s of (jessatom5)'%(d*12.120000))
cmd.select('temp71', 'temp71 and not (all within %s of (jessatom5))'%((1./d)*11.881188))
cmd.select('temp72', 'all within %s of (jessatom6)'%(d*11.059500))
cmd.select('temp72', 'temp72 and not (all within %s of (jessatom6))'%((1./d)*10.841584))
cmd.select('temp73', 'all within %s of (jessatom7)'%(d*11.190800))
cmd.select('temp73', 'temp73 and not (all within %s of (jessatom7))'%((1./d)*10.970297))
cmd.select('temp74', 'all within %s of (jessatom8)'%(d*12.604800))
cmd.select('temp74', 'temp74 and not (all within %s of (jessatom8))'%((1./d)*12.356436))
cmd.select('temp75', 'all within %s of (jessatom9)'%(d*1.272600))
cmd.select('temp75', 'temp75 and not (all within %s of (jessatom9))'%((1./d)*1.247525))
cmd.select('temp76', 'byres jessatom9')
cmd.select('jessatom10', '((((temp62 or temp63) and temp51) or ((temp64 or temp65) and temp52)) and temp66 and temp67 and temp68 and temp69 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*17.341700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom10))'%((1./d)*17.000000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*16.129700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom10))'%((1./d)*15.811881))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*15.756000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom10))'%((1./d)*15.445545))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*14.109700))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom10))'%((1./d)*13.831683))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*12.695700))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom10))'%((1./d)*12.445545))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*12.120000))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom10))'%((1./d)*11.881188))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*11.059500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom10))'%((1./d)*10.841584))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*11.190800))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom10))'%((1./d)*10.970297))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*12.604800))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom10))'%((1./d)*12.356436))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.272600))
cmd.select('jessatom9', 'jessatom9 and not (all within %s of (jessatom10))'%((1./d)*1.247525))
cmd.select('temp77', 'name  od2')
cmd.select('temp78', 'name  od1')
cmd.select('temp79', 'name  oe2')
cmd.select('temp80', 'name  oe1')
cmd.select('temp81', 'all within %s of (jessatom0)'%(d*16.402400))
cmd.select('temp81', 'temp81 and not (all within %s of (jessatom0))'%((1./d)*16.079208))
cmd.select('temp82', 'all within %s of (jessatom1)'%(d*15.200500))
cmd.select('temp82', 'temp82 and not (all within %s of (jessatom1))'%((1./d)*14.900990))
cmd.select('temp83', 'all within %s of (jessatom2)'%(d*14.776300))
cmd.select('temp83', 'temp83 and not (all within %s of (jessatom2))'%((1./d)*14.485149))
cmd.select('temp84', 'all within %s of (jessatom3)'%(d*13.877400))
cmd.select('temp84', 'temp84 and not (all within %s of (jessatom3))'%((1./d)*13.603960))
cmd.select('temp85', 'all within %s of (jessatom4)'%(d*12.453300))
cmd.select('temp85', 'temp85 and not (all within %s of (jessatom4))'%((1./d)*12.207921))
cmd.select('temp86', 'all within %s of (jessatom5)'%(d*11.635200))
cmd.select('temp86', 'temp86 and not (all within %s of (jessatom5))'%((1./d)*11.405941))
cmd.select('temp87', 'all within %s of (jessatom6)'%(d*11.544300))
cmd.select('temp87', 'temp87 and not (all within %s of (jessatom6))'%((1./d)*11.316832))
cmd.select('temp88', 'all within %s of (jessatom7)'%(d*11.928100))
cmd.select('temp88', 'temp88 and not (all within %s of (jessatom7))'%((1./d)*11.693069))
cmd.select('temp89', 'all within %s of (jessatom8)'%(d*13.402700))
cmd.select('temp89', 'temp89 and not (all within %s of (jessatom8))'%((1./d)*13.138614))
cmd.select('temp75', 'temp75 and not (all within %s of (jessatom9))'%((1./d)*1.247525))
cmd.select('temp90', 'byres jessatom9')
cmd.select('temp91', 'all within %s of (jessatom10)'%(d*2.211900))
cmd.select('temp91', 'temp91 and not (all within %s of (jessatom10))'%((1./d)*2.168317))
cmd.select('jessatom11', '((((temp77 or temp78) and temp51) or ((temp79 or temp80) and temp52)) and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89 and temp75 and temp90 and temp91)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*16.402400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom11))'%((1./d)*16.079208))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*15.200500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom11))'%((1./d)*14.900990))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*14.776300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom11))'%((1./d)*14.485149))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*13.877400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom11))'%((1./d)*13.603960))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*12.453300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom11))'%((1./d)*12.207921))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*11.635200))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom11))'%((1./d)*11.405941))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*11.544300))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom11))'%((1./d)*11.316832))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*11.928100))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom11))'%((1./d)*11.693069))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*13.402700))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom11))'%((1./d)*13.138614))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*1.272600))
cmd.select('jessatom9', 'jessatom9 and not (all within %s of (jessatom11))'%((1./d)*1.247525))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.211900))
cmd.select('jessatom10', 'jessatom10 and not (all within %s of (jessatom11))'%((1./d)*2.168317))
cmd.select('Jfa_1c8v_4_2_1_20', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
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
cmd.delete('temp63')
cmd.delete('temp64')
cmd.delete('temp65')
cmd.delete('temp66')
cmd.delete('temp67')
cmd.delete('temp68')
cmd.delete('temp69')
cmd.delete('temp70')
cmd.delete('temp71')
cmd.delete('temp72')
cmd.delete('temp73')
cmd.delete('temp74')
cmd.delete('temp75')
cmd.delete('temp76')
cmd.delete('temp77')
cmd.delete('temp78')
cmd.delete('temp79')
cmd.delete('temp80')
cmd.delete('temp81')
cmd.delete('temp82')
cmd.delete('temp83')
cmd.delete('temp84')
cmd.delete('temp85')
cmd.delete('temp86')
cmd.delete('temp87')
cmd.delete('temp88')
cmd.delete('temp89')
cmd.delete('temp90')
cmd.delete('temp91')