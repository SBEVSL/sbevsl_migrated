'''
FUNC:Jab_1xid_5_3_1_5
PDB:1xid
EC:5.3.1.5
RESI:his,asp,glu,lys
LOCI:a-54,57,181,183;
'''
cmd.select('temp0', 'name  ca ')
cmd.select('temp1', 'resn his')
cmd.select('jessatom0', '(temp0 and temp1)')
cmd.select('temp2', 'name  cb ')
cmd.select('temp3', 'resn his')
cmd.select('temp4', 'all within %s of (jessatom0)'%(d*1.535200))
cmd.select('temp4', 'temp4 and not (all within %s of (jessatom0))'%((1./d)*1.504950))
cmd.select('temp5', 'byres jessatom0')
cmd.select('jessatom1', '(temp2 and temp3 and temp4 and temp5)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom1)'%(d*1.535200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom1))'%((1./d)*1.504950))
cmd.select('temp6', 'resn asp')
cmd.select('temp7', 'resn glu')
cmd.select('temp8', 'all within %s of (jessatom0)'%(d*5.211600))
cmd.select('temp8', 'temp8 and not (all within %s of (jessatom0))'%((1./d)*5.108911))
cmd.select('temp9', 'all within %s of (jessatom1)'%(d*5.019700))
cmd.select('temp9', 'temp9 and not (all within %s of (jessatom1))'%((1./d)*4.920792))
cmd.select('jessatom2', '(((temp0 and temp6) or (temp0 and temp7)) and temp8 and temp9)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom2)'%(d*5.211600))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom2))'%((1./d)*5.108911))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom2)'%(d*5.019700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom2))'%((1./d)*4.920792))
cmd.select('temp10', 'all within %s of (jessatom0)'%(d*4.565200))
cmd.select('temp10', 'temp10 and not (all within %s of (jessatom0))'%((1./d)*4.475248))
cmd.select('temp11', 'all within %s of (jessatom1)'%(d*4.555100))
cmd.select('temp11', 'temp11 and not (all within %s of (jessatom1))'%((1./d)*4.465347))
cmd.select('temp12', 'all within %s of (jessatom2)'%(d*1.535200))
cmd.select('temp12', 'temp12 and not (all within %s of (jessatom2))'%((1./d)*1.504950))
cmd.select('temp13', 'byres jessatom2')
cmd.select('jessatom3', '(((temp2 and temp6) or (temp2 and temp7)) and temp10 and temp11 and temp12 and temp13)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom3)'%(d*4.565200))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom3))'%((1./d)*4.475248))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom3)'%(d*4.555100))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom3))'%((1./d)*4.465347))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom3)'%(d*1.535200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom3))'%((1./d)*1.504950))
cmd.select('temp14', 'all within %s of (jessatom0)'%(d*13.978400))
cmd.select('temp14', 'temp14 and not (all within %s of (jessatom0))'%((1./d)*13.702970))
cmd.select('temp15', 'all within %s of (jessatom1)'%(d*13.806700))
cmd.select('temp15', 'temp15 and not (all within %s of (jessatom1))'%((1./d)*13.534653))
cmd.select('temp16', 'all within %s of (jessatom2)'%(d*18.493100))
cmd.select('temp16', 'temp16 and not (all within %s of (jessatom2))'%((1./d)*18.128713))
cmd.select('temp17', 'all within %s of (jessatom3)'%(d*17.513400))
cmd.select('temp17', 'temp17 and not (all within %s of (jessatom3))'%((1./d)*17.168317))
cmd.select('jessatom4', '(((temp0 and temp7) or (temp0 and temp6)) and temp14 and temp15 and temp16 and temp17)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom4)'%(d*13.978400))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom4))'%((1./d)*13.702970))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom4)'%(d*13.806700))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom4))'%((1./d)*13.534653))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom4)'%(d*18.493100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom4))'%((1./d)*18.128713))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom4)'%(d*17.513400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom4))'%((1./d)*17.168317))
cmd.select('temp18', 'all within %s of (jessatom0)'%(d*12.594700))
cmd.select('temp18', 'temp18 and not (all within %s of (jessatom0))'%((1./d)*12.346535))
cmd.select('temp19', 'all within %s of (jessatom1)'%(d*12.412900))
cmd.select('temp19', 'temp19 and not (all within %s of (jessatom1))'%((1./d)*12.168317))
cmd.select('temp20', 'all within %s of (jessatom2)'%(d*17.018500))
cmd.select('temp20', 'temp20 and not (all within %s of (jessatom2))'%((1./d)*16.683168))
cmd.select('temp21', 'all within %s of (jessatom3)'%(d*16.018600))
cmd.select('temp21', 'temp21 and not (all within %s of (jessatom3))'%((1./d)*15.702970))
cmd.select('temp22', 'all within %s of (jessatom4)'%(d*1.555400))
cmd.select('temp22', 'temp22 and not (all within %s of (jessatom4))'%((1./d)*1.524752))
cmd.select('temp23', 'byres jessatom4')
cmd.select('jessatom5', '(((temp2 and temp7) or (temp2 and temp6)) and temp18 and temp19 and temp20 and temp21 and temp22 and temp23)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom5)'%(d*12.594700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom5))'%((1./d)*12.346535))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom5)'%(d*12.412900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom5))'%((1./d)*12.168317))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom5)'%(d*17.018500))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom5))'%((1./d)*16.683168))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom5)'%(d*16.018600))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom5))'%((1./d)*15.702970))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom5)'%(d*1.555400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom5))'%((1./d)*1.524752))
cmd.select('temp24', 'resn lys')
cmd.select('temp25', 'all within %s of (jessatom0)'%(d*17.574000))
cmd.select('temp25', 'temp25 and not (all within %s of (jessatom0))'%((1./d)*17.227723))
cmd.select('temp26', 'all within %s of (jessatom1)'%(d*16.856900))
cmd.select('temp26', 'temp26 and not (all within %s of (jessatom1))'%((1./d)*16.524752))
cmd.select('temp27', 'all within %s of (jessatom2)'%(d*21.018100))
cmd.select('temp27', 'temp27 and not (all within %s of (jessatom2))'%((1./d)*20.603960))
cmd.select('temp28', 'all within %s of (jessatom3)'%(d*20.200000))
cmd.select('temp28', 'temp28 and not (all within %s of (jessatom3))'%((1./d)*19.801980))
cmd.select('temp29', 'all within %s of (jessatom4)'%(d*6.807400))
cmd.select('temp29', 'temp29 and not (all within %s of (jessatom4))'%((1./d)*6.673267))
cmd.select('temp30', 'all within %s of (jessatom5)'%(d*7.120500))
cmd.select('temp30', 'temp30 and not (all within %s of (jessatom5))'%((1./d)*6.980198))
cmd.select('jessatom6', '(temp0 and temp24 and temp25 and temp26 and temp27 and temp28 and temp29 and temp30)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom6)'%(d*17.574000))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom6))'%((1./d)*17.227723))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom6)'%(d*16.856900))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom6))'%((1./d)*16.524752))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom6)'%(d*21.018100))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom6))'%((1./d)*20.603960))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom6)'%(d*20.200000))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom6))'%((1./d)*19.801980))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom6)'%(d*6.807400))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom6))'%((1./d)*6.673267))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom6)'%(d*7.120500))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom6))'%((1./d)*6.980198))
cmd.select('temp31', 'all within %s of (jessatom0)'%(d*16.331700))
cmd.select('temp31', 'temp31 and not (all within %s of (jessatom0))'%((1./d)*16.009901))
cmd.select('temp32', 'all within %s of (jessatom1)'%(d*15.554000))
cmd.select('temp32', 'temp32 and not (all within %s of (jessatom1))'%((1./d)*15.247525))
cmd.select('temp33', 'all within %s of (jessatom2)'%(d*19.614200))
cmd.select('temp33', 'temp33 and not (all within %s of (jessatom2))'%((1./d)*19.227723))
cmd.select('temp34', 'all within %s of (jessatom3)'%(d*18.826400))
cmd.select('temp34', 'temp34 and not (all within %s of (jessatom3))'%((1./d)*18.455446))
cmd.select('temp35', 'all within %s of (jessatom4)'%(d*6.827600))
cmd.select('temp35', 'temp35 and not (all within %s of (jessatom4))'%((1./d)*6.693069))
cmd.select('temp36', 'all within %s of (jessatom5)'%(d*6.807400))
cmd.select('temp36', 'temp36 and not (all within %s of (jessatom5))'%((1./d)*6.673267))
cmd.select('temp37', 'all within %s of (jessatom6)'%(d*1.565500))
cmd.select('temp37', 'temp37 and not (all within %s of (jessatom6))'%((1./d)*1.534653))
cmd.select('temp38', 'byres jessatom6')
cmd.select('jessatom7', '(temp2 and temp24 and temp31 and temp32 and temp33 and temp34 and temp35 and temp36 and temp37 and temp38)')
cmd.select('jessatom0', 'jessatom0 within %s of (jessatom7)'%(d*16.331700))
cmd.select('jessatom0', 'jessatom0 and not (all within %s of (jessatom7))'%((1./d)*16.009901))
cmd.select('jessatom1', 'jessatom1 within %s of (jessatom7)'%(d*15.554000))
cmd.select('jessatom1', 'jessatom1 and not (all within %s of (jessatom7))'%((1./d)*15.247525))
cmd.select('jessatom2', 'jessatom2 within %s of (jessatom7)'%(d*19.614200))
cmd.select('jessatom2', 'jessatom2 and not (all within %s of (jessatom7))'%((1./d)*19.227723))
cmd.select('jessatom3', 'jessatom3 within %s of (jessatom7)'%(d*18.826400))
cmd.select('jessatom3', 'jessatom3 and not (all within %s of (jessatom7))'%((1./d)*18.455446))
cmd.select('jessatom4', 'jessatom4 within %s of (jessatom7)'%(d*6.827600))
cmd.select('jessatom4', 'jessatom4 and not (all within %s of (jessatom7))'%((1./d)*6.693069))
cmd.select('jessatom5', 'jessatom5 within %s of (jessatom7)'%(d*6.807400))
cmd.select('jessatom5', 'jessatom5 and not (all within %s of (jessatom7))'%((1./d)*6.673267))
cmd.select('jessatom6', 'jessatom6 within %s of (jessatom7)'%(d*1.565500))
cmd.select('jessatom6', 'jessatom6 and not (all within %s of (jessatom7))'%((1./d)*1.534653))
cmd.select('Jab_1xid_5_3_1_5', 'byres jessatom0|byres jessatom1|byres jessatom2|byres jessatom3|byres jessatom4|byres jessatom5|byres jessatom6|byres jessatom7')
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