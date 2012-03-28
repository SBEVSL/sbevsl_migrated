'''
FUNC:Jfa_1dvj_4_1_1_23
PDB:1dvj
EC:4.1.1.23
RESI:lys,asp,lys,asp
LOCI:a-42,70,72,75;
'''
cmd.select('temp0', 'name  cd ')
cmd.select('temp1', 'resn lys')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  ce ')
cmd.select('temp3', 'resn lys')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.525100))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.495050))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.525100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.495050))
cmd.select('temp6', 'name  nz ')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*2.555300))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*2.504950))
cmd.select('temp8', 'byres jessatom0')
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*1.515000))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*1.485149))
cmd.select('jessatom2', '(temp6 and temp3 and temp7 and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*2.555300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*2.504950))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*1.515000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*1.485149))
cmd.select('temp10', 'name  cg ')
cmd.select('temp11', 'resn asp')
cmd.select('temp12', 'resn glu')
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*4.050100))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom0))'%((1./d)*3.970297))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*4.221800))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom1))'%((1./d)*4.138614))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*3.494600))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom2))'%((1./d)*3.425743))
cmd.select('jessatom3', '(((temp10 and temp11) or (temp10 and temp12)) and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.050100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*3.970297))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.221800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*4.138614))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*3.494600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*3.425743))
cmd.select('temp16', 'name  od1')
cmd.select('temp17', 'name  od2')
cmd.select('temp18', 'name  oe1')
cmd.select('temp19', 'name  oe2')
cmd.select('temp20', 'all within %s of (jessatom0)'%(d*5.100500))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom0))'%((1./d)*5.000000))
cmd.select('temp21', 'all within %s of (jessatom1)'%(d*5.363100))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom1))'%((1./d)*5.257426))
cmd.select('temp22', 'all within %s of (jessatom2)'%(d*4.706600))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom2))'%((1./d)*4.613861))
cmd.select('temp23', 'all within %s of (jessatom3)'%(d*1.262500))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom3))'%((1./d)*1.237624))
cmd.select('temp24', 'byres jessatom3')
cmd.select('jessatom4', '((((temp16 or temp17) and temp11) or ((temp18 or temp19) and temp12)) and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*5.100500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*5.000000))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*5.363100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*5.257426))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*4.706600))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*4.613861))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*1.262500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*1.237624))
cmd.select('temp25', 'name  od2')
cmd.select('temp26', 'name  od1')
cmd.select('temp27', 'name  oe2')
cmd.select('temp28', 'name  oe1')
cmd.select('temp29', 'all within %s of (jessatom0)'%(d*3.646100))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom0))'%((1./d)*3.574257))
cmd.select('temp30', 'all within %s of (jessatom1)'%(d*3.423900))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom1))'%((1./d)*3.356436))
cmd.select('temp31', 'all within %s of (jessatom2)'%(d*2.646200))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom2))'%((1./d)*2.594059))
cmd.select('temp32', 'all within %s of (jessatom3)'%(d*1.252400))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom3))'%((1./d)*1.227723))
cmd.select('temp33', 'byres jessatom3')
cmd.select('temp34', 'all within %s of (jessatom4)'%(d*2.211900))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom4))'%((1./d)*2.168317))
cmd.select('jessatom5', '((((temp25 or temp26) and temp11) or ((temp27 or temp28) and temp12)) and temp29 and temp30 and temp31 and temp32 and temp33 and temp34)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*3.646100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*3.574257))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*3.423900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*3.356436))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*2.646200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*2.594059))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*1.252400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*1.227723))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*2.211900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*2.168317))
cmd.select('temp35', 'all within %s of (jessatom0)'%(d*8.302200))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom0))'%((1./d)*8.138614))
cmd.select('temp36', 'all within %s of (jessatom1)'%(d*8.211300))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom1))'%((1./d)*8.049505))
cmd.select('temp37', 'all within %s of (jessatom2)'%(d*7.484100))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom2))'%((1./d)*7.336634))
cmd.select('temp38', 'all within %s of (jessatom3)'%(d*4.676300))
cmd.select('temp38', 'temp38 and not (all within %s of (jessatom3))'%((1./d)*4.584158))
cmd.select('temp39', 'all within %s of (jessatom4)'%(d*3.676400))
cmd.select('temp39', 'temp39 and not (all within %s of (jessatom4))'%((1./d)*3.603960))
cmd.select('temp40', 'all within %s of (jessatom5)'%(d*4.918700))
cmd.select('temp40', 'temp40 and not (all within %s of (jessatom5))'%((1./d)*4.821782))
cmd.select('jessatom6', '(temp0 and temp3 and temp35 and temp36 and temp37 and temp38 and temp39 and temp40)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*8.302200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*8.138614))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*8.211300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*8.049505))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*7.484100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*7.336634))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*4.676300))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*4.584158))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*3.676400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*3.603960))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*4.918700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*4.821782))
cmd.select('temp41', 'all within %s of (jessatom0)'%(d*7.676000))
cmd.select('temp41', 'temp41 and not (all within %s of (jessatom0))'%((1./d)*7.524752))
cmd.select('temp42', 'all within %s of (jessatom1)'%(d*7.352800))
cmd.select('temp42', 'temp42 and not (all within %s of (jessatom1))'%((1./d)*7.207921))
cmd.select('temp43', 'all within %s of (jessatom2)'%(d*6.635700))
cmd.select('temp43', 'temp43 and not (all within %s of (jessatom2))'%((1./d)*6.504950))
cmd.select('temp44', 'all within %s of (jessatom3)'%(d*4.454100))
cmd.select('temp44', 'temp44 and not (all within %s of (jessatom3))'%((1./d)*4.366337))
cmd.select('temp45', 'all within %s of (jessatom4)'%(d*3.787500))
cmd.select('temp45', 'temp45 and not (all within %s of (jessatom4))'%((1./d)*3.712871))
cmd.select('temp46', 'all within %s of (jessatom5)'%(d*4.282400))
cmd.select('temp46', 'temp46 and not (all within %s of (jessatom5))'%((1./d)*4.198020))
cmd.select('temp47', 'all within %s of (jessatom6)'%(d*1.565500))
cmd.select('temp47', 'temp47 and not (all within %s of (jessatom6))'%((1./d)*1.534653))
cmd.select('temp48', 'byres jessatom6')
cmd.select('jessatom7', '(temp2 and temp3 and temp41 and temp42 and temp43 and temp44 and temp45 and temp46 and temp47 and temp48)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*7.676000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*7.524752))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*7.352800))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*7.207921))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*6.635700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*6.504950))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*4.454100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*4.366337))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*3.787500))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*3.712871))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*4.282400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*4.198020))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.565500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.534653))
cmd.select('temp49', 'all within %s of (jessatom0)'%(d*6.322600))
cmd.select('temp49', 'temp49 and not (all within %s of (jessatom0))'%((1./d)*6.198020))
cmd.select('temp50', 'all within %s of (jessatom1)'%(d*5.928700))
cmd.select('temp50', 'temp50 and not (all within %s of (jessatom1))'%((1./d)*5.811881))
cmd.select('temp51', 'all within %s of (jessatom2)'%(d*5.130800))
cmd.select('temp51', 'temp51 and not (all within %s of (jessatom2))'%((1./d)*5.029703))
cmd.select('temp52', 'all within %s of (jessatom3)'%(d*3.181500))
cmd.select('temp52', 'temp52 and not (all within %s of (jessatom3))'%((1./d)*3.118812))
cmd.select('temp53', 'all within %s of (jessatom4)'%(d*2.858300))
cmd.select('temp53', 'temp53 and not (all within %s of (jessatom4))'%((1./d)*2.801980))
cmd.select('temp54', 'all within %s of (jessatom5)'%(d*2.838100))
cmd.select('temp54', 'temp54 and not (all within %s of (jessatom5))'%((1./d)*2.782178))
cmd.select('temp55', 'all within %s of (jessatom6)'%(d*2.585600))
cmd.select('temp55', 'temp55 and not (all within %s of (jessatom6))'%((1./d)*2.534653))
cmd.select('temp56', 'byres jessatom6')
cmd.select('temp57', 'all within %s of (jessatom7)'%(d*1.525100))
cmd.select('temp57', 'temp57 and not (all within %s of (jessatom7))'%((1./d)*1.495050))
cmd.select('jessatom8', '(temp6 and temp3 and temp49 and temp50 and temp51 and temp52 and temp53 and temp54 and temp55 and temp56 and temp57)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom8)'%(d*6.322600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom8))'%((1./d)*6.198020))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom8)'%(d*5.928700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom8))'%((1./d)*5.811881))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom8)'%(d*5.130800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom8))'%((1./d)*5.029703))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom8)'%(d*3.181500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom8))'%((1./d)*3.118812))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom8)'%(d*2.858300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom8))'%((1./d)*2.801980))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom8)'%(d*2.838100))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom8))'%((1./d)*2.782178))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom8)'%(d*2.585600))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom8))'%((1./d)*2.534653))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom8)'%(d*1.525100))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom8))'%((1./d)*1.495050))
cmd.select('temp58', 'all within %s of (jessatom0)'%(d*20.088900))
cmd.select('temp58', 'temp58 and not (all within %s of (jessatom0))'%((1./d)*19.693069))
cmd.select('temp59', 'all within %s of (jessatom1)'%(d*20.452500))
cmd.select('temp59', 'temp59 and not (all within %s of (jessatom1))'%((1./d)*20.049505))
cmd.select('temp60', 'all within %s of (jessatom2)'%(d*19.493000))
cmd.select('temp60', 'temp60 and not (all within %s of (jessatom2))'%((1./d)*19.108911))
cmd.select('temp61', 'all within %s of (jessatom3)'%(d*16.240800))
cmd.select('temp61', 'temp61 and not (all within %s of (jessatom3))'%((1./d)*15.920792))
cmd.select('temp62', 'all within %s of (jessatom4)'%(d*15.180300))
cmd.select('temp62', 'temp62 and not (all within %s of (jessatom4))'%((1./d)*14.881188))
cmd.select('temp63', 'all within %s of (jessatom5)'%(d*17.170000))
cmd.select('temp63', 'temp63 and not (all within %s of (jessatom5))'%((1./d)*16.831683))
cmd.select('temp64', 'all within %s of (jessatom6)'%(d*13.503700))
cmd.select('temp64', 'temp64 and not (all within %s of (jessatom6))'%((1./d)*13.237624))
cmd.select('temp65', 'all within %s of (jessatom7)'%(d*14.948000))
cmd.select('temp65', 'temp65 and not (all within %s of (jessatom7))'%((1./d)*14.653465))
cmd.select('temp66', 'all within %s of (jessatom8)'%(d*15.725700))
cmd.select('temp66', 'temp66 and not (all within %s of (jessatom8))'%((1./d)*15.415842))
cmd.select('jessatom9', '(((temp10 and temp11) or (temp10 and temp12)) and temp58 and temp59 and temp60 and temp61 and temp62 and temp63 and temp64 and temp65 and temp66)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom9)'%(d*20.088900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom9))'%((1./d)*19.693069))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom9)'%(d*20.452500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom9))'%((1./d)*20.049505))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom9)'%(d*19.493000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom9))'%((1./d)*19.108911))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom9)'%(d*16.240800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom9))'%((1./d)*15.920792))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom9)'%(d*15.180300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom9))'%((1./d)*14.881188))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom9)'%(d*17.170000))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom9))'%((1./d)*16.831683))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom9)'%(d*13.503700))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom9))'%((1./d)*13.237624))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom9)'%(d*14.948000))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom9))'%((1./d)*14.653465))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom9)'%(d*15.725700))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom9))'%((1./d)*15.415842))
cmd.select('temp67', 'all within %s of (jessatom0)'%(d*21.280700))
cmd.select('temp67', 'temp67 and not (all within %s of (jessatom0))'%((1./d)*20.861386))
cmd.select('temp68', 'all within %s of (jessatom1)'%(d*21.644300))
cmd.select('temp68', 'temp68 and not (all within %s of (jessatom1))'%((1./d)*21.217822))
cmd.select('temp69', 'all within %s of (jessatom2)'%(d*20.705000))
cmd.select('temp69', 'temp69 and not (all within %s of (jessatom2))'%((1./d)*20.297030))
cmd.select('temp70', 'all within %s of (jessatom3)'%(d*17.422500))
cmd.select('temp70', 'temp70 and not (all within %s of (jessatom3))'%((1./d)*17.079208))
cmd.select('temp71', 'all within %s of (jessatom4)'%(d*16.351900))
cmd.select('temp71', 'temp71 and not (all within %s of (jessatom4))'%((1./d)*16.029703))
cmd.select('temp72', 'all within %s of (jessatom5)'%(d*18.351700))
cmd.select('temp72', 'temp72 and not (all within %s of (jessatom5))'%((1./d)*17.990099))
cmd.select('temp73', 'all within %s of (jessatom6)'%(d*14.574300))
cmd.select('temp73', 'temp73 and not (all within %s of (jessatom6))'%((1./d)*14.287129))
cmd.select('temp74', 'all within %s of (jessatom7)'%(d*16.018600))
cmd.select('temp74', 'temp74 and not (all within %s of (jessatom7))'%((1./d)*15.702970))
cmd.select('temp75', 'all within %s of (jessatom8)'%(d*16.846800))
cmd.select('temp75', 'temp75 and not (all within %s of (jessatom8))'%((1./d)*16.514851))
cmd.select('temp76', 'all within %s of (jessatom9)'%(d*1.272600))
cmd.select('temp76', 'temp76 and not (all within %s of (jessatom9))'%((1./d)*1.247525))
cmd.select('temp77', 'byres jessatom9')
cmd.select('jessatom10', '((((temp16 or temp17) and temp11) or ((temp18 or temp19) and temp12)) and temp67 and temp68 and temp69 and temp70 and temp71 and temp72 and temp73 and temp74 and temp75 and temp76 and temp77)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom10)'%(d*21.280700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom10))'%((1./d)*20.861386))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom10)'%(d*21.644300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom10))'%((1./d)*21.217822))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom10)'%(d*20.705000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom10))'%((1./d)*20.297030))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom10)'%(d*17.422500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom10))'%((1./d)*17.079208))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom10)'%(d*16.351900))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom10))'%((1./d)*16.029703))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom10)'%(d*18.351700))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom10))'%((1./d)*17.990099))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom10)'%(d*14.574300))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom10))'%((1./d)*14.287129))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom10)'%(d*16.018600))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom10))'%((1./d)*15.702970))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom10)'%(d*16.846800))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom10))'%((1./d)*16.514851))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom10)'%(d*1.272600))
cmd.select('jessatom9', 'jessatom9 and not (all within %s of (jessatom10))'%((1./d)*1.247525))
cmd.select('temp78', 'all within %s of (jessatom0)'%(d*19.836400))
cmd.select('temp78', 'temp78 and not (all within %s of (jessatom0))'%((1./d)*19.445545))
cmd.select('temp79', 'all within %s of (jessatom1)'%(d*20.149500))
cmd.select('temp79', 'temp79 and not (all within %s of (jessatom1))'%((1./d)*19.752475))
cmd.select('temp80', 'all within %s of (jessatom2)'%(d*19.119300))
cmd.select('temp80', 'temp80 and not (all within %s of (jessatom2))'%((1./d)*18.742574))
cmd.select('temp81', 'all within %s of (jessatom3)'%(d*15.958000))
cmd.select('temp81', 'temp81 and not (all within %s of (jessatom3))'%((1./d)*15.643564))
cmd.select('temp82', 'all within %s of (jessatom4)'%(d*14.948000))
cmd.select('temp82', 'temp82 and not (all within %s of (jessatom4))'%((1./d)*14.653465))
cmd.select('temp83', 'all within %s of (jessatom5)'%(d*16.877100))
cmd.select('temp83', 'temp83 and not (all within %s of (jessatom5))'%((1./d)*16.544554))
cmd.select('temp84', 'all within %s of (jessatom6)'%(d*13.342100))
cmd.select('temp84', 'temp84 and not (all within %s of (jessatom6))'%((1./d)*13.079208))
cmd.select('temp85', 'all within %s of (jessatom7)'%(d*14.746000))
cmd.select('temp85', 'temp85 and not (all within %s of (jessatom7))'%((1./d)*14.455446))
cmd.select('temp86', 'all within %s of (jessatom8)'%(d*15.463100))
cmd.select('temp86', 'temp86 and not (all within %s of (jessatom8))'%((1./d)*15.158416))
cmd.select('temp87', 'all within %s of (jessatom9)'%(d*1.262500))
cmd.select('temp87', 'temp87 and not (all within %s of (jessatom9))'%((1./d)*1.237624))
cmd.select('temp88', 'byres jessatom9')
cmd.select('temp89', 'all within %s of (jessatom10)'%(d*2.222000))
cmd.select('temp89', 'temp89 and not (all within %s of (jessatom10))'%((1./d)*2.178218))
cmd.select('jessatom11', '((((temp25 or temp26) and temp11) or ((temp27 or temp28) and temp12)) and temp78 and temp79 and temp80 and temp81 and temp82 and temp83 and temp84 and temp85 and temp86 and temp87 and temp88 and temp89)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom11)'%(d*19.836400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom11))'%((1./d)*19.445545))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom11)'%(d*20.149500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom11))'%((1./d)*19.752475))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom11)'%(d*19.119300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom11))'%((1./d)*18.742574))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom11)'%(d*15.958000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom11))'%((1./d)*15.643564))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom11)'%(d*14.948000))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom11))'%((1./d)*14.653465))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom11)'%(d*16.877100))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom11))'%((1./d)*16.544554))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom11)'%(d*13.342100))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom11))'%((1./d)*13.079208))
cmd.select('jessatom7', 'jessatom7 within %s of (jessatom11)'%(d*14.746000))
cmd.select('jessatom7', 'jessatom7 and not (all within %s of (jessatom11))'%((1./d)*14.455446))
cmd.select('jessatom8', 'jessatom8 within %s of (jessatom11)'%(d*15.463100))
cmd.select('jessatom8', 'jessatom8 and not (all within %s of (jessatom11))'%((1./d)*15.158416))
cmd.select('jessatom9', 'jessatom9 within %s of (jessatom11)'%(d*1.262500))
cmd.select('jessatom9', 'jessatom9 and not (all within %s of (jessatom11))'%((1./d)*1.237624))
cmd.select('jessatom10', 'jessatom10 within %s of (jessatom11)'%(d*2.222000))
cmd.select('jessatom10', 'jessatom10 and not (all within %s of (jessatom11))'%((1./d)*2.178218))
cmd.select('Jfa_1dvj_4_1_1_23', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7|byres jessatom8|byres jessatom9|byres jessatom10|byres jessatom11')
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