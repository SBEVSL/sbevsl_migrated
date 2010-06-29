'''
FUNC:Jfa_5csm_5_4_99_5
PDB:5csm
EC:5.4.99.5
RESI:arg,arg,lys,glu
'''
cmd.select('temp0', 'n. ne')
cmd.select('temp1', 'r. arg')
cmd.select('jessatom0', 'temp0&temp1')
cmd.select('temp2', 'n. nh1')
cmd.select('temp3', 'n. nh2')
cmd.select('temp4', 'r. arg')
cmd.select('temp5', 'all w. %s of jessatom0'%(d*2.333100))
cmd.select('temp6', 'br. jessatom0')
cmd.select('jessatom1', '(temp2|temp3)&temp4&temp5&temp6')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*2.333100))
cmd.select('temp7', 'n. nh2')
cmd.select('temp8', 'n. nh1')
cmd.select('temp9', 'all w. %s of jessatom0'%(d*2.312900))
cmd.select('temp10', 'br. jessatom0')
cmd.select('temp11', 'all w. %s of jessatom1'%(d*2.312900))
cmd.select('jessatom2', '(temp7|temp8)&temp4&temp9&temp10&temp11')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*2.312900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*2.312900))
cmd.select('temp12', 'all w. %s of jessatom0'%(d*12.816900))
cmd.select('temp13', 'all w. %s of jessatom1'%(d*14.665200))
cmd.select('temp14', 'all w. %s of jessatom2'%(d*14.725800))
cmd.select('jessatom3', 'temp0&temp4&temp12&temp13&temp14')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*12.816900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*14.665200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*14.725800))
cmd.select('temp15', 'all w. %s of jessatom0'%(d*13.200700))
cmd.select('temp16', 'all w. %s of jessatom1'%(d*15.109600))
cmd.select('temp17', 'all w. %s of jessatom2'%(d*14.867200))
cmd.select('temp18', 'all w. %s of jessatom3'%(d*2.353300))
cmd.select('temp19', 'br. jessatom3')
cmd.select('jessatom4', '(temp2|temp3)&temp4&temp15&temp16&temp17&temp18&temp19')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*13.200700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*15.109600))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*14.867200))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*2.353300))
cmd.select('temp20', 'all w. %s of jessatom0'%(d*12.332100))
cmd.select('temp21', 'all w. %s of jessatom1'%(d*14.382400))
cmd.select('temp22', 'all w. %s of jessatom2'%(d*14.119800))
cmd.select('temp23', 'all w. %s of jessatom3'%(d*2.333100))
cmd.select('temp24', 'br. jessatom3')
cmd.select('temp25', 'all w. %s of jessatom4'%(d*2.323000))
cmd.select('jessatom5', '(temp7|temp8)&temp4&temp20&temp21&temp22&temp23&temp24&temp25')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*12.332100))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*14.382400))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*14.119800))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*2.333100))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*2.323000))
cmd.select('temp26', 'n. cd')
cmd.select('temp27', 'r. lys')
cmd.select('temp28', 'all w. %s of jessatom0'%(d*11.069600))
cmd.select('temp29', 'all w. %s of jessatom1'%(d*12.392700))
cmd.select('temp30', 'all w. %s of jessatom2'%(d*10.625200))
cmd.select('temp31', 'all w. %s of jessatom3'%(d*13.806700))
cmd.select('temp32', 'all w. %s of jessatom4'%(d*12.261400))
cmd.select('temp33', 'all w. %s of jessatom5'%(d*12.534100))
cmd.select('jessatom6', 'temp26&temp27&temp28&temp29&temp30&temp31&temp32&temp33')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*11.069600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*12.392700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*10.625200))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*13.806700))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*12.261400))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*12.534100))
cmd.select('temp34', 'n. ce')
cmd.select('temp35', 'all w. %s of jessatom0'%(d*9.877800))
cmd.select('temp36', 'all w. %s of jessatom1'%(d*11.362500))
cmd.select('temp37', 'all w. %s of jessatom2'%(d*9.595000))
cmd.select('temp38', 'all w. %s of jessatom3'%(d*12.816900))
cmd.select('temp39', 'all w. %s of jessatom4'%(d*11.413000))
cmd.select('temp40', 'all w. %s of jessatom5'%(d*11.463500))
cmd.select('temp41', 'all w. %s of jessatom6'%(d*1.535200))
cmd.select('temp42', 'br. jessatom6')
cmd.select('jessatom7', 'temp34&temp27&temp35&temp36&temp37&temp38&temp39&temp40&temp41&temp42')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*9.877800))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*11.362500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*9.595000))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*12.816900))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*11.413000))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*11.463500))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.535200))
cmd.select('temp43', 'n. nz')
cmd.select('temp44', 'all w. %s of jessatom0'%(d*9.231400))
cmd.select('temp45', 'all w. %s of jessatom1'%(d*10.685800))
cmd.select('temp46', 'all w. %s of jessatom2'%(d*8.736500))
cmd.select('temp47', 'all w. %s of jessatom3'%(d*13.584500))
cmd.select('temp48', 'all w. %s of jessatom4'%(d*12.352300))
cmd.select('temp49', 'all w. %s of jessatom5'%(d*12.170500))
cmd.select('temp50', 'all w. %s of jessatom6'%(d*2.545200))
cmd.select('temp51', 'br. jessatom6')
cmd.select('temp52', 'all w. %s of jessatom7'%(d*1.504900))
cmd.select('jessatom8', 'temp43&temp27&temp44&temp45&temp46&temp47&temp48&temp49&temp50&temp51&temp52')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*9.231400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*10.685800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*8.736500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*13.584500))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*12.352300))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*12.170500))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*2.545200))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*1.504900))
cmd.select('temp53', 'r. glu')
cmd.select('temp54', 'r. asp')
cmd.select('temp55', 'all w. %s of jessatom0'%(d*13.261300))
cmd.select('temp56', 'all w. %s of jessatom1'%(d*15.049000))
cmd.select('temp57', 'all w. %s of jessatom2'%(d*13.826900))
cmd.select('temp58', 'all w. %s of jessatom3'%(d*9.746500))
cmd.select('temp59', 'all w. %s of jessatom4'%(d*7.655800))
cmd.select('temp60', 'all w. %s of jessatom5'%(d*8.484000))
cmd.select('temp61', 'all w. %s of jessatom6'%(d*5.938800))
cmd.select('temp62', 'all w. %s of jessatom7'%(d*5.787300))
cmd.select('temp63', 'all w. %s of jessatom8'%(d*7.160900))
cmd.select('jessatom9', '((temp26&temp53)|(temp26&temp54))&temp55&temp56&temp57&temp58&temp59&temp60&temp61&temp62&temp63')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom9'%(d*13.261300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom9'%(d*15.049000))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom9'%(d*13.826900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom9'%(d*9.746500))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom9'%(d*7.655800))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom9'%(d*8.484000))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom9'%(d*5.938800))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom9'%(d*5.787300))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom9'%(d*7.160900))
cmd.select('temp64', 'n. oe1')
cmd.select('temp65', 'n. oe2')
cmd.select('temp66', 'n. od1')
cmd.select('temp67', 'n. od2')
cmd.select('temp68', 'all w. %s of jessatom0'%(d*12.988600))
cmd.select('temp69', 'all w. %s of jessatom1'%(d*14.735900))
cmd.select('temp70', 'all w. %s of jessatom2'%(d*13.362300))
cmd.select('temp71', 'all w. %s of jessatom3'%(d*10.706000))
cmd.select('temp72', 'all w. %s of jessatom4'%(d*8.706200))
cmd.select('temp73', 'all w. %s of jessatom5'%(d*9.362700))
cmd.select('temp74', 'all w. %s of jessatom6'%(d*4.827800))
cmd.select('temp75', 'all w. %s of jessatom7'%(d*4.767200))
cmd.select('temp76', 'all w. %s of jessatom8'%(d*6.150900))
cmd.select('temp77', 'all w. %s of jessatom9'%(d*1.242300))
cmd.select('temp78', 'br. jessatom9')
cmd.select('jessatom10', '(((temp64|temp65)&temp53)|((temp66|temp67)&temp54))&temp68&temp69&temp70&temp71&temp72&temp73&temp74&temp75&temp76&temp77&temp78')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom10'%(d*12.988600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom10'%(d*14.735900))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom10'%(d*13.362300))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom10'%(d*10.706000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom10'%(d*8.706200))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom10'%(d*9.362700))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom10'%(d*4.827800))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom10'%(d*4.767200))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom10'%(d*6.150900))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom10'%(d*1.242300))
cmd.select('temp79', 'n. oe2')
cmd.select('temp80', 'n. oe1')
cmd.select('temp81', 'n. od2')
cmd.select('temp82', 'n. od1')
cmd.select('temp83', 'all w. %s of jessatom0'%(d*12.625000))
cmd.select('temp84', 'all w. %s of jessatom1'%(d*14.493500))
cmd.select('temp85', 'all w. %s of jessatom3'%(d*8.605200))
cmd.select('temp86', 'all w. %s of jessatom4'%(d*6.554900))
cmd.select('temp87', 'all w. %s of jessatom5'%(d*7.272000))
cmd.select('temp88', 'all w. %s of jessatom6'%(d*6.474100))
cmd.select('temp89', 'all w. %s of jessatom7'%(d*6.029700))
cmd.select('temp90', 'all w. %s of jessatom8'%(d*7.292200))
cmd.select('temp91', 'br. jessatom9')
cmd.select('temp92', 'all w. %s of jessatom10'%(d*2.161400))
cmd.select('jessatom11', '(((temp79|temp80)&temp53)|((temp81|temp82)&temp54))&temp83&temp84&temp70&temp85&temp86&temp87&temp88&temp89&temp90&temp77&temp91&temp92')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom11'%(d*12.625000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom11'%(d*14.493500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom11'%(d*13.362300))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom11'%(d*8.605200))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom11'%(d*6.554900))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom11'%(d*7.272000))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom11'%(d*6.474100))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom11'%(d*6.029700))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom11'%(d*7.292200))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom11'%(d*1.242300))
cmd.select('jessatom10', 'jessatom10 w. %s of jessatom11'%(d*2.161400))
cmd.select('Jfa_5csm_5_4_99_5', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
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
cmd.delete('temp92')