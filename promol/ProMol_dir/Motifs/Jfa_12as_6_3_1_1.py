'''
FUNC:Jfa_12as_6_3_1_1
PDB:12as
EC:6.3.1.1
RESI:asp,arg,gln
'''
cmd.select('temp0', 'n. cg')
cmd.select('temp1', 'r. asp')
cmd.select('temp2', 'r. glu')
cmd.select('jessatom0', '((temp0&temp1)|(temp0&temp2))')
cmd.select('temp3', 'n. od1')
cmd.select('temp4', 'n. od2')
cmd.select('temp5', 'n. oe1')
cmd.select('temp6', 'n. oe2')
cmd.select('temp7', 'all w. %s of jessatom0'%(d*1.262500))
cmd.select('temp8', 'br. jessatom0')
cmd.select('jessatom1', '(((temp3|temp4)&temp1)|((temp5|temp6)&temp2))&temp7&temp8')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.262500))
cmd.select('temp9', 'n. od2')
cmd.select('temp10', 'n. od1')
cmd.select('temp11', 'n. oe2')
cmd.select('temp12', 'n. oe1')
cmd.select('temp13', 'br. jessatom0')
cmd.select('temp14', 'all w. %s of jessatom1'%(d*2.211900))
cmd.select('jessatom2', '(((temp9|temp10)&temp1)|((temp11|temp12)&temp2))&temp7&temp13&temp14')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*1.262500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*2.211900))
cmd.select('temp15', 'n. ne')
cmd.select('temp16', 'r. arg')
cmd.select('temp17', 'all w. %s of jessatom0'%(d*7.423500))
cmd.select('temp18', 'all w. %s of jessatom1'%(d*7.958800))
cmd.select('temp19', 'all w. %s of jessatom2'%(d*6.666000))
cmd.select('jessatom3', 'temp15&temp16&temp17&temp18&temp19')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*7.423500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*7.958800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*6.666000))
cmd.select('temp20', 'n. nh1')
cmd.select('temp21', 'n. nh2')
cmd.select('temp22', 'all w. %s of jessatom0'%(d*6.433700))
cmd.select('temp23', 'all w. %s of jessatom1'%(d*6.746800))
cmd.select('temp24', 'all w. %s of jessatom2'%(d*5.605500))
cmd.select('temp25', 'all w. %s of jessatom3'%(d*2.272500))
cmd.select('temp26', 'br. jessatom3')
cmd.select('jessatom4', '(temp20|temp21)&temp16&temp22&temp23&temp24&temp25&temp26')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*6.433700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*6.746800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*5.605500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*2.272500))
cmd.select('temp27', 'n. nh2')
cmd.select('temp28', 'n. nh1')
cmd.select('temp29', 'all w. %s of jessatom0'%(d*5.827700))
cmd.select('temp30', 'all w. %s of jessatom1'%(d*6.544800))
cmd.select('temp31', 'all w. %s of jessatom2'%(d*4.858100))
cmd.select('temp32', 'all w. %s of jessatom3'%(d*2.323000))
cmd.select('temp33', 'br. jessatom3')
cmd.select('temp34', 'all w. %s of jessatom4'%(d*2.272500))
cmd.select('jessatom5', '(temp27|temp28)&temp16&temp29&temp30&temp31&temp32&temp33&temp34')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*5.827700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*6.544800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*4.858100))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*2.323000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*2.272500))
cmd.select('temp35', 'n. cd')
cmd.select('temp36', 'r. gln')
cmd.select('temp37', 'r. asn')
cmd.select('temp38', 'all w. %s of jessatom0'%(d*8.423400))
cmd.select('temp39', 'all w. %s of jessatom1'%(d*9.382900))
cmd.select('temp40', 'all w. %s of jessatom2'%(d*7.211400))
cmd.select('temp41', 'all w. %s of jessatom3'%(d*6.524600))
cmd.select('temp42', 'all w. %s of jessatom4'%(d*6.464000))
cmd.select('temp43', 'all w. %s of jessatom5'%(d*4.797500))
cmd.select('jessatom6', '((temp35&temp36)|(temp35&temp37))&temp38&temp39&temp40&temp41&temp42&temp43')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*8.423400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*9.382900))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*7.211400))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*6.524600))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*6.464000))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*4.797500))
cmd.select('temp44', 'all w. %s of jessatom0'%(d*7.766900))
cmd.select('temp45', 'all w. %s of jessatom1'%(d*8.665800))
cmd.select('temp46', 'all w. %s of jessatom2'%(d*6.554900))
cmd.select('temp47', 'all w. %s of jessatom3'%(d*5.363100))
cmd.select('temp48', 'all w. %s of jessatom4'%(d*5.231800))
cmd.select('temp49', 'all w. %s of jessatom5'%(d*3.636000))
cmd.select('temp50', 'all w. %s of jessatom6'%(d*1.242300))
cmd.select('temp51', 'br. jessatom6')
cmd.select('jessatom7', '((temp5&temp36)|(temp5&temp37))&temp44&temp45&temp46&temp47&temp48&temp49&temp50&temp51')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*7.766900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*8.665800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*6.554900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*5.363100))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*5.231800))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*3.636000))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.242300))
cmd.select('temp52', 'n. ne2')
cmd.select('temp53', 'all w. %s of jessatom0'%(d*8.029500))
cmd.select('temp54', 'all w. %s of jessatom1'%(d*9.039500))
cmd.select('temp55', 'all w. %s of jessatom2'%(d*6.857900))
cmd.select('temp56', 'all w. %s of jessatom3'%(d*7.383100))
cmd.select('temp57', 'all w. %s of jessatom4'%(d*7.171000))
cmd.select('temp58', 'all w. %s of jessatom5'%(d*5.403500))
cmd.select('temp59', 'all w. %s of jessatom6'%(d*1.343300))
cmd.select('temp60', 'br. jessatom6')
cmd.select('temp61', 'all w. %s of jessatom7'%(d*2.262400))
cmd.select('jessatom8', '((temp52&temp36)|(temp52&temp37))&temp53&temp54&temp55&temp56&temp57&temp58&temp59&temp60&temp61')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*8.029500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*9.039500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*6.857900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*7.383100))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*7.171000))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*5.403500))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*1.343300))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*2.262400))
cmd.select('Jfa_12as_6_3_1_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
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
