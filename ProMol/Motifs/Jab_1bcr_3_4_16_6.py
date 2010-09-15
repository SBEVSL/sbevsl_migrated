'''
FUNC:Jab_1bcr_3_4_16_6
PDB:1bcr
EC:3.4.16.6
RESI:gly,ser,tyr,asp,his
LOCI:a-53,146,147;b-338,397;
'''
cmd.select('temp0', 'n. n')
cmd.select('jessatom0', 'temp0')
cmd.select('temp1', 'n. ca')
cmd.select('temp2', 'all w. %s of jessatom0'%(d*1.464500))
cmd.select('temp3', 'br. jessatom0')
cmd.select('jessatom1', 'temp1&temp2&temp3')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.464500))
cmd.select('temp4', 'r. ser')
cmd.select('temp5', 'r. thr')
cmd.select('temp6', 'all w. %s of jessatom0'%(d*6.352900))
cmd.select('temp7', 'all w. %s of jessatom1'%(d*7.474000))
cmd.select('jessatom2', '((temp1&temp4)|(temp1&temp5))&temp6&temp7')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*6.352900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*7.474000))
cmd.select('temp8', 'n. cb')
cmd.select('temp9', 'all w. %s of jessatom0'%(d*5.423700))
cmd.select('temp10', 'all w. %s of jessatom1'%(d*6.453900))
cmd.select('temp11', 'all w. %s of jessatom2'%(d*1.535200))
cmd.select('temp12', 'br. jessatom2')
cmd.select('jessatom3', '((temp8&temp4)|(temp8&temp5))&temp9&temp10&temp11&temp12')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*5.423700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*6.453900))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*1.535200))
cmd.select('temp13', 'n. n')
cmd.select('temp14', 'all w. %s of jessatom0'%(d*4.646000))
cmd.select('temp15', 'all w. %s of jessatom1'%(d*5.757000))
cmd.select('temp16', 'all w. %s of jessatom2'%(d*2.474500))
cmd.select('temp17', 'all w. %s of jessatom3'%(d*2.727000))
cmd.select('jessatom4', 'temp13&temp14&temp15&temp16&temp17')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*4.646000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*5.757000))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*2.474500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*2.727000))
cmd.select('temp18', 'all w. %s of jessatom1'%(d*5.676200))
cmd.select('temp19', 'all w. %s of jessatom2'%(d*3.868300))
cmd.select('temp20', 'all w. %s of jessatom3'%(d*4.191500))
cmd.select('temp21', 'all w. %s of jessatom4'%(d*1.474600))
cmd.select('temp22', 'br. jessatom4')
cmd.select('jessatom5', 'temp1&temp14&temp18&temp19&temp20&temp21&temp22')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*4.646000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*5.676200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*3.868300))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*4.191500))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.474600))
cmd.select('temp23', 'r. asp')
cmd.select('temp24', 'r. glu')
cmd.select('temp25', 'all w. %s of jessatom0'%(d*15.119700))
cmd.select('temp26', 'all w. %s of jessatom1'%(d*15.564100))
cmd.select('temp27', 'all w. %s of jessatom2'%(d*10.877700))
cmd.select('temp28', 'all w. %s of jessatom3'%(d*10.574700))
cmd.select('temp29', 'all w. %s of jessatom4'%(d*12.917900))
cmd.select('temp30', 'all w. %s of jessatom5'%(d*14.271300))
cmd.select('jessatom6', '((temp1&temp23)|(temp1&temp24))&temp25&temp26&temp27&temp28&temp29&temp30')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*15.119700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*15.564100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*10.877700))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*10.574700))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*12.917900))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*14.271300))
cmd.select('temp31', 'all w. %s of jessatom0'%(d*13.988500))
cmd.select('temp32', 'all w. %s of jessatom1'%(d*14.544000))
cmd.select('temp33', 'all w. %s of jessatom2'%(d*9.443500))
cmd.select('temp34', 'all w. %s of jessatom3'%(d*9.241500))
cmd.select('temp35', 'all w. %s of jessatom4'%(d*11.574600))
cmd.select('temp36', 'all w. %s of jessatom5'%(d*12.948200))
cmd.select('temp37', 'all w. %s of jessatom6'%(d*1.565500))
cmd.select('temp38', 'br. jessatom6')
cmd.select('jessatom7', '((temp8&temp23)|(temp8&temp24))&temp31&temp32&temp33&temp34&temp35&temp36&temp37&temp38')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*13.988500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*14.544000))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*9.443500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*9.241500))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*11.574600))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*12.948200))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.565500))
cmd.select('temp39', 'r. his')
cmd.select('temp40', 'all w. %s of jessatom0'%(d*11.877600))
cmd.select('temp41', 'all w. %s of jessatom1'%(d*12.554300))
cmd.select('temp42', 'all w. %s of jessatom2'%(d*8.019400))
cmd.select('temp43', 'all w. %s of jessatom3'%(d*7.494200))
cmd.select('temp44', 'all w. %s of jessatom4'%(d*10.170700))
cmd.select('temp45', 'all w. %s of jessatom5'%(d*11.645300))
cmd.select('temp46', 'all w. %s of jessatom6'%(d*4.928800))
cmd.select('temp47', 'all w. %s of jessatom7'%(d*3.908700))
cmd.select('jessatom8', 'temp1&temp39&temp40&temp41&temp42&temp43&temp44&temp45&temp46&temp47')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*11.877600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*12.554300))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*8.019400))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*7.494200))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*10.170700))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*11.645300))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*4.928800))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*3.908700))
cmd.select('temp48', 'all w. %s of jessatom0'%(d*10.908000))
cmd.select('temp49', 'all w. %s of jessatom1'%(d*11.463500))
cmd.select('temp50', 'all w. %s of jessatom2'%(d*7.625500))
cmd.select('temp51', 'all w. %s of jessatom3'%(d*6.868000))
cmd.select('temp52', 'all w. %s of jessatom4'%(d*9.554600))
cmd.select('temp53', 'all w. %s of jessatom5'%(d*11.009000))
cmd.select('temp54', 'all w. %s of jessatom6'%(d*5.161100))
cmd.select('temp55', 'all w. %s of jessatom7'%(d*4.272300))
cmd.select('temp56', 'all w. %s of jessatom8'%(d*1.515000))
cmd.select('temp57', 'br. jessatom8')
cmd.select('jessatom9', 'temp8&temp39&temp48&temp49&temp50&temp51&temp52&temp53&temp54&temp55&temp56&temp57')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom9'%(d*10.908000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom9'%(d*11.463500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom9'%(d*7.625500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom9'%(d*6.868000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom9'%(d*9.554600))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom9'%(d*11.009000))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom9'%(d*5.161100))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom9'%(d*4.272300))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom9'%(d*1.515000))
cmd.select('Jab_1bcr_3_4_16_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9')
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
