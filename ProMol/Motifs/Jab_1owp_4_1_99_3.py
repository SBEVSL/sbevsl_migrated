'''
FUNC:Jab_1owp_4_1_99_3
PDB:1owp
EC:4.1.99.3
RESI:trp,trp,trp
LOCI:a-314,367,390;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn trp')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn trp')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.545300))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.514851))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.545300))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.514851))
cmd.select('temp6', 'all within %s of (jessatom0)'%(d*9.039500))
cmd.select('temp6', 'temp6 and not (all within %s of (jessatom0))'%((1./d)*8.861386))
cmd.select('temp7', 'all within %s of (jessatom1)'%(d*7.827500))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom1))'%((1./d)*7.673267))
cmd.select('jessatom2', '(temp0 and temp3 and temp6 and temp7)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*9.039500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*8.861386))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*7.827500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*7.673267))
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*9.706100))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom0))'%((1./d)*9.514851))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*8.605200))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*8.435644))
cmd.select('temp10', 'all within %s of (jessatom2)'%(d*1.565500))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom2))'%((1./d)*1.534653))
cmd.select('temp11', 'byres jessatom2')
cmd.select('jessatom3', '(temp2 and temp3 and temp8 and temp9 and temp10 and temp11)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*9.706100))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*9.514851))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*8.605200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*8.435644))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.565500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.534653))
cmd.select('temp12', 'all within %s of (jessatom0)'%(d*14.786400))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom0))'%((1./d)*14.495050))
cmd.select('temp13', 'all within %s of (jessatom1)'%(d*13.766300))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom1))'%((1./d)*13.495050))
cmd.select('temp14', 'all within %s of (jessatom2)'%(d*6.565000))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom2))'%((1./d)*6.435644))
cmd.select('temp15', 'all within %s of (jessatom3)'%(d*5.312600))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom3))'%((1./d)*5.207921))
cmd.select('jessatom4', '(temp0 and temp3 and temp12 and temp13 and temp14 and temp15)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*14.786400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*14.495050))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*13.766300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*13.495050))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*6.565000))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*6.435644))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*5.312600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*5.207921))
cmd.select('temp16', 'all within %s of (jessatom0)'%(d*14.291500))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom0))'%((1./d)*14.009901))
cmd.select('temp17', 'all within %s of (jessatom1)'%(d*13.160300))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom1))'%((1./d)*12.900990))
cmd.select('temp18', 'all within %s of (jessatom2)'%(d*5.676200))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom2))'%((1./d)*5.564356))
cmd.select('temp19', 'all within %s of (jessatom3)'%(d*4.666200))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom3))'%((1./d)*4.574257))
cmd.select('temp20', 'all within %s of (jessatom4)'%(d*1.545300))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom4))'%((1./d)*1.514851))
cmd.select('temp21', 'byres jessatom4')
cmd.select('jessatom5', '(temp2 and temp3 and temp16 and temp17 and temp18 and temp19 and temp20 and temp21)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*14.291500))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*14.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*13.160300))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*12.900990))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*5.676200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*5.564356))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*4.666200))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*4.574257))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.545300))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.514851))
cmd.select('Jab_1owp_4_1_99_3', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
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