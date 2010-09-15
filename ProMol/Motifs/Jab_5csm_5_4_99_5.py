'''
FUNC:Jab_5csm_5_4_99_5
PDB:5csm
EC:5.4.99.5
RESI:arg,arg,lys,glu
LOCI:a-16,157,168,246;
'''
cmd.select('temp0', 'n. ca')
cmd.select('temp1', 'r. arg')
cmd.select('jessatom0', 'temp0&temp1')
cmd.select('temp2', 'n. cb')
cmd.select('temp3', 'r. arg')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.535200))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', 'temp2&temp3&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.535200))
cmd.select('temp6', 'all w. %s of jessatom0'%(d*11.463500))
cmd.select('temp7', 'all w. %s of jessatom1'%(d*12.887600))
cmd.select('jessatom2', 'temp0&temp3&temp6&temp7')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*11.463500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*12.887600))
cmd.select('temp8', 'all w. %s of jessatom0'%(d*11.493800))
cmd.select('temp9', 'all w. %s of jessatom1'%(d*12.847200))
cmd.select('temp10', 'all w. %s of jessatom2'%(d*1.555400))
cmd.select('temp11', 'br. jessatom2')
cmd.select('jessatom3', 'temp2&temp3&temp8&temp9&temp10&temp11')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*11.493800))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*12.847200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*1.555400))
cmd.select('temp12', 'r. lys')
cmd.select('temp13', 'all w. %s of jessatom0'%(d*13.534000))
cmd.select('temp14', 'all w. %s of jessatom1'%(d*13.766300))
cmd.select('temp15', 'all w. %s of jessatom2'%(d*17.473000))
cmd.select('temp16', 'all w. %s of jessatom3'%(d*18.371900))
cmd.select('jessatom4', 'temp0&temp12&temp13&temp14&temp15&temp16')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*13.534000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*13.766300))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*17.473000))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*18.371900))
cmd.select('temp17', 'all w. %s of jessatom0'%(d*13.392600))
cmd.select('temp18', 'all w. %s of jessatom1'%(d*13.645100))
cmd.select('temp19', 'all w. %s of jessatom2'%(d*16.856900))
cmd.select('temp20', 'all w. %s of jessatom3'%(d*17.695200))
cmd.select('temp21', 'all w. %s of jessatom4'%(d*1.535200))
cmd.select('temp22', 'br. jessatom4')
cmd.select('jessatom5', 'temp2&temp12&temp17&temp18&temp19&temp20&temp21&temp22')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*13.392600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*13.645100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*16.856900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*17.695200))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.535200))
cmd.select('temp23', 'r. glu')
cmd.select('temp24', 'r. asp')
cmd.select('temp25', 'all w. %s of jessatom0'%(d*15.796400))
cmd.select('temp26', 'all w. %s of jessatom1'%(d*16.705400))
cmd.select('temp27', 'all w. %s of jessatom2'%(d*12.311900))
cmd.select('temp28', 'all w. %s of jessatom3'%(d*13.241100))
cmd.select('temp29', 'all w. %s of jessatom4'%(d*10.190900))
cmd.select('temp30', 'all w. %s of jessatom5'%(d*9.110200))
cmd.select('jessatom6', '((temp0&temp23)|(temp0&temp24))&temp25&temp26&temp27&temp28&temp29&temp30')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*15.796400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*16.705400))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*12.311900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*13.241100))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*10.190900))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*9.110200))
cmd.select('temp31', 'all w. %s of jessatom0'%(d*14.735900))
cmd.select('temp32', 'all w. %s of jessatom1'%(d*15.554000))
cmd.select('temp33', 'all w. %s of jessatom2'%(d*12.130100))
cmd.select('temp34', 'all w. %s of jessatom3'%(d*12.958300))
cmd.select('temp35', 'all w. %s of jessatom4'%(d*9.443500))
cmd.select('temp36', 'all w. %s of jessatom5'%(d*8.241600))
cmd.select('temp37', 'all w. %s of jessatom6'%(d*1.545300))
cmd.select('temp38', 'br. jessatom6')
cmd.select('jessatom7', '((temp2&temp23)|(temp2&temp24))&temp31&temp32&temp33&temp34&temp35&temp36&temp37&temp38')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*14.735900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*15.554000))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*12.130100))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*12.958300))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*9.443500))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*8.241600))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.545300))
cmd.select('Jab_5csm_5_4_99_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7')
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
