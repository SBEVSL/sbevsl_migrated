'''
FUNC:Jab_2tps_2_5_1_3
PDB:2tps
EC:2.5.1.3
RESI:arg,ser,lys
LOCI:a-59,130,159;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn arg')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn arg')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.555400))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.524752))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.555400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.524752))
cmd.select('temp6', 'resn ser')
cmd.select('temp7', 'resn thr')
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*13.786500))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom0))'%((1./d)*13.514851))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*12.685600))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*12.435644))
cmd.select('jessatom2', '(((temp0 and temp6) or (temp0 and temp7)) and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*13.786500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*13.514851))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*12.685600))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*12.435644))
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*12.887600))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom0))'%((1./d)*12.633663))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*11.766500))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom1))'%((1./d)*11.534653))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*1.545300))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom2))'%((1./d)*1.514851))
cmd.select('temp13', 'byres jessatom2')
cmd.select('jessatom3', '(((temp2 and temp6) or (temp2 and temp7)) and temp10 and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*12.887600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*12.633663))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*11.766500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*11.534653))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.545300))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.514851))
cmd.select('temp14', 'resn lys')
cmd.select('temp15', 'all within %s of (jessatom0)'%(d*10.897900))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom0))'%((1./d)*10.683168))
cmd.select('temp16', 'all within %s of (jessatom1)'%(d*9.726300))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom1))'%((1./d)*9.534653))
cmd.select('temp17', 'all within %s of (jessatom2)'%(d*13.018900))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom2))'%((1./d)*12.762376))
cmd.select('temp18', 'all within %s of (jessatom3)'%(d*11.625100))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom3))'%((1./d)*11.396040))
cmd.select('jessatom4', '(temp0 and temp14 and temp15 and temp16 and temp17 and temp18)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*10.897900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*10.683168))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*9.726300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*9.534653))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*13.018900))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*12.762376))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*11.625100))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*11.396040))
cmd.select('temp19', 'all within %s of (jessatom0)'%(d*10.473700))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom0))'%((1./d)*10.267327))
cmd.select('temp20', 'all within %s of (jessatom1)'%(d*9.211200))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom1))'%((1./d)*9.029703))
cmd.select('temp21', 'all within %s of (jessatom2)'%(d*11.483700))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom2))'%((1./d)*11.257426))
cmd.select('temp22', 'all within %s of (jessatom3)'%(d*10.100000))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom3))'%((1./d)*9.900990))
cmd.select('temp23', 'all within %s of (jessatom4)'%(d*1.535200))
cmd.select('temp23', 'temp23 and not (all within %s of (jessatom4))'%((1./d)*1.504950))
cmd.select('temp24', 'byres jessatom4')
cmd.select('jessatom5', '(temp2 and temp14 and temp19 and temp20 and temp21 and temp22 and temp23 and temp24)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*10.473700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*10.267327))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*9.211200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*9.029703))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*11.483700))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*11.257426))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*10.100000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*9.900990))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.535200))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.504950))
cmd.select('Jab_2tps_2_5_1_3', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
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