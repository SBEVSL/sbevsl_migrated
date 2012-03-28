'''
FUNC:Jab_1gal_1_1_3_4
PDB:1gal
EC:1.1.3.4
RESI:glu,his,his
LOCI:a-412,516,559;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn glu')
cmd.select('temp2', 'resn asp')
cmd.select('jessatom0', '(((temp0 and temp1) or (temp0 and temp2)))')
cmd.select('temp3', 'name  cb ')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.535200))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.504950))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(((temp3 and temp1) or (temp3 and temp2)) and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.535200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.504950))
cmd.select('temp6', 'resn his')
cmd.select('temp7', 'all within %s of (jessatom0)'%(d*13.190600))
cmd.select('temp7', 'temp7 and not (all within %s of (jessatom0))'%((1./d)*12.930693))
cmd.select('temp8', 'all within %s of (jessatom1)'%(d*11.938200))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom1))'%((1./d)*11.702970))
cmd.select('jessatom2', '(temp0 and temp6 and temp7 and temp8)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*13.190600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*12.930693))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*11.938200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*11.702970))
cmd.select('temp9', 'all within %s of (jessatom0)'%(d*11.675600))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom0))'%((1./d)*11.445545))
cmd.select('temp10', 'all within %s of (jessatom1)'%(d*10.423200))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom1))'%((1./d)*10.217822))
cmd.select('temp11', 'all within %s of (jessatom2)'%(d*1.565500))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom2))'%((1./d)*1.534653))
cmd.select('temp12', 'byres jessatom2')
cmd.select('jessatom3', '(temp3 and temp6 and temp9 and temp10 and temp11 and temp12)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*11.675600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*11.445545))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*10.423200))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*10.217822))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.565500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.534653))
cmd.select('temp13', 'all within %s of (jessatom0)'%(d*9.988900))
cmd.select('temp13', 'temp13 and not (all within %s of (jessatom0))'%((1./d)*9.792079))
cmd.select('temp14', 'all within %s of (jessatom1)'%(d*8.494100))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom1))'%((1./d)*8.326733))
cmd.select('temp15', 'all within %s of (jessatom2)'%(d*8.564800))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom2))'%((1./d)*8.396040))
cmd.select('temp16', 'all within %s of (jessatom3)'%(d*7.524500))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom3))'%((1./d)*7.376238))
cmd.select('jessatom4', '(temp0 and temp6 and temp13 and temp14 and temp15 and temp16)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*9.988900))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*9.792079))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*8.494100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*8.326733))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*8.564800))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*8.396040))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*7.524500))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*7.376238))
cmd.select('temp17', 'all within %s of (jessatom0)'%(d*10.241400))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom0))'%((1./d)*10.039604))
cmd.select('temp18', 'all within %s of (jessatom1)'%(d*8.736500))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom1))'%((1./d)*8.564356))
cmd.select('temp19', 'all within %s of (jessatom2)'%(d*9.433400))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom2))'%((1./d)*9.247525))
cmd.select('temp20', 'all within %s of (jessatom3)'%(d*8.463800))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom3))'%((1./d)*8.297030))
cmd.select('temp21', 'all within %s of (jessatom4)'%(d*1.515000))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom4))'%((1./d)*1.485149))
cmd.select('temp22', 'byres jessatom4')
cmd.select('jessatom5', '(temp3 and temp6 and temp17 and temp18 and temp19 and temp20 and temp21 and temp22)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*10.241400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*10.039604))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*8.736500))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*8.564356))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*9.433400))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*9.247525))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*8.463800))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*8.297030))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.515000))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.485149))
cmd.select('Jab_1gal_1_1_3_4', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5')
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