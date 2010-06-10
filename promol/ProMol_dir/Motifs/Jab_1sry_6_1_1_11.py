'''
FUNC:Jab_1sry_6_1_1_11
PDB:1sry
EC:6.1.1.11
RESI:arg,glu,ser,asp,arg
'''
cmd.select('temp0', 'n. ca')
cmd.select('temp1', 'r. arg')
cmd.select('jessatom0', 'temp0&temp1')
cmd.select('temp2', 'n. cb')
cmd.select('temp3', 'r. arg')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.545300))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', 'temp2&temp3&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.545300))
cmd.select('temp6', 'r. glu')
cmd.select('temp7', 'r. asp')
cmd.select('temp8', 'all w. %s of jessatom0'%(d*5.454000))
cmd.select('temp9', 'all w. %s of jessatom1'%(d*5.161100))
cmd.select('jessatom2', '((temp0&temp6)|(temp0&temp7))&temp8&temp9')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*5.454000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*5.161100))
cmd.select('temp10', 'all w. %s of jessatom0'%(d*5.888300))
cmd.select('temp11', 'all w. %s of jessatom1'%(d*5.585300))
cmd.select('temp12', 'all w. %s of jessatom2'%(d*1.545300))
cmd.select('temp13', 'br. jessatom2')
cmd.select('jessatom3', '((temp2&temp6)|(temp2&temp7))&temp10&temp11&temp12&temp13')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*5.888300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*5.585300))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*1.545300))
cmd.select('temp14', 'r. ser')
cmd.select('temp15', 'r. thr')
cmd.select('temp16', 'all w. %s of jessatom0'%(d*12.695700))
cmd.select('temp17', 'all w. %s of jessatom1'%(d*12.120000))
cmd.select('temp18', 'all w. %s of jessatom2'%(d*7.322500))
cmd.select('temp19', 'all w. %s of jessatom3'%(d*7.059900))
cmd.select('jessatom4', '((temp0&temp14)|(temp0&temp15))&temp16&temp17&temp18&temp19')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*12.695700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*12.120000))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*7.322500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*7.059900))
cmd.select('temp20', 'all w. %s of jessatom0'%(d*13.867300))
cmd.select('temp21', 'all w. %s of jessatom1'%(d*13.352200))
cmd.select('temp22', 'all w. %s of jessatom2'%(d*8.433500))
cmd.select('temp23', 'all w. %s of jessatom3'%(d*8.322400))
cmd.select('temp24', 'all w. %s of jessatom4'%(d*1.555400))
cmd.select('temp25', 'br. jessatom4')
cmd.select('jessatom5', '((temp2&temp14)|(temp2&temp15))&temp20&temp21&temp22&temp23&temp24&temp25')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*13.867300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*13.352200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*8.433500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*8.322400))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.555400))
cmd.select('temp26', 'all w. %s of jessatom0'%(d*18.806200))
cmd.select('temp27', 'all w. %s of jessatom1'%(d*17.836600))
cmd.select('temp28', 'all w. %s of jessatom2'%(d*15.129800))
cmd.select('temp29', 'all w. %s of jessatom3'%(d*14.049100))
cmd.select('temp30', 'all w. %s of jessatom4'%(d*10.958500))
cmd.select('temp31', 'all w. %s of jessatom5'%(d*11.776600))
cmd.select('jessatom6', '((temp0&temp7)|(temp0&temp6))&temp26&temp27&temp28&temp29&temp30&temp31')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*18.806200))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*17.836600))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*15.129800))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*14.049100))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*10.958500))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*11.776600))
cmd.select('temp32', 'all w. %s of jessatom0'%(d*20.058600))
cmd.select('temp33', 'all w. %s of jessatom1'%(d*19.109200))
cmd.select('temp34', 'all w. %s of jessatom2'%(d*16.513500))
cmd.select('temp35', 'all w. %s of jessatom3'%(d*15.372200))
cmd.select('temp36', 'all w. %s of jessatom4'%(d*12.402800))
cmd.select('temp37', 'all w. %s of jessatom5'%(d*13.200700))
cmd.select('temp38', 'all w. %s of jessatom6'%(d*1.555400))
cmd.select('temp39', 'br. jessatom6')
cmd.select('jessatom7', '((temp2&temp7)|(temp2&temp6))&temp32&temp33&temp34&temp35&temp36&temp37&temp38&temp39')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*20.058600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*19.109200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*16.513500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*15.372200))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*12.402800))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*13.200700))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.555400))
cmd.select('temp40', 'all w. %s of jessatom0'%(d*9.079900))
cmd.select('temp41', 'all w. %s of jessatom1'%(d*8.090100))
cmd.select('temp42', 'all w. %s of jessatom2'%(d*7.847700))
cmd.select('temp43', 'all w. %s of jessatom3'%(d*6.736700))
cmd.select('temp44', 'all w. %s of jessatom4'%(d*10.150500))
cmd.select('temp45', 'all w. %s of jessatom5'%(d*11.705900))
cmd.select('temp46', 'all w. %s of jessatom6'%(d*10.564600))
cmd.select('temp47', 'all w. %s of jessatom7'%(d*11.615000))
cmd.select('jessatom8', 'temp0&temp3&temp40&temp41&temp42&temp43&temp44&temp45&temp46&temp47')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*9.079900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*8.090100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*7.847700))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*6.736700))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*10.150500))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*11.705900))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*10.564600))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*11.615000))
cmd.select('temp48', 'all w. %s of jessatom0'%(d*9.413200))
cmd.select('temp49', 'all w. %s of jessatom1'%(d*8.393100))
cmd.select('temp50', 'all w. %s of jessatom2'%(d*7.261900))
cmd.select('temp51', 'all w. %s of jessatom3'%(d*6.171100))
cmd.select('temp52', 'all w. %s of jessatom4'%(d*8.706200))
cmd.select('temp53', 'all w. %s of jessatom5'%(d*10.251500))
cmd.select('temp54', 'all w. %s of jessatom6'%(d*9.645500))
cmd.select('temp55', 'all w. %s of jessatom7'%(d*10.817100))
cmd.select('temp56', 'all w. %s of jessatom8'%(d*1.555400))
cmd.select('temp57', 'br. jessatom8')
cmd.select('jessatom9', 'temp2&temp3&temp48&temp49&temp50&temp51&temp52&temp53&temp54&temp55&temp56&temp57')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom9'%(d*9.413200))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom9'%(d*8.393100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom9'%(d*7.261900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom9'%(d*6.171100))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom9'%(d*8.706200))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom9'%(d*10.251500))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom9'%(d*9.645500))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom9'%(d*10.817100))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom9'%(d*1.555400))
cmd.select('Jab_1sry_6_1_1_11', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9')
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
