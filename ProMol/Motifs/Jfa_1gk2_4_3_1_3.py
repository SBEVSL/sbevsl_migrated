'''
FUNC:Jfa_1gk2_4_3_1_3
PDB:1gk2
EC:4.3.1.3
RESI:ala,ser,gly,tyr,glu
'''
cmd.select('temp0', 'n. ca')
cmd.select('temp1', 'r. ala')
cmd.select('jessatom0', 'temp0&temp1')
cmd.select('temp2', 'n. c')
cmd.select('temp3', 'r. ala')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.545300))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', 'temp2&temp3&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.545300))
cmd.select('temp6', 'n. cb')
cmd.select('temp7', 'all w. %s of jessatom0'%(d*1.525100))
cmd.select('temp8', 'br. jessatom0')
cmd.select('temp9', 'all w. %s of jessatom1'%(d*2.535100))
cmd.select('jessatom2', 'temp6&temp3&temp7&temp8&temp9')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*1.525100))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*2.535100))
cmd.select('temp10', 'r. ser')
cmd.select('temp11', 'r. thr')
cmd.select('temp12', 'all w. %s of jessatom0'%(d*3.848100))
cmd.select('temp13', 'all w. %s of jessatom1'%(d*2.514900))
cmd.select('temp14', 'all w. %s of jessatom2'%(d*4.848000))
cmd.select('jessatom3', '((temp0&temp10)|(temp0&temp11))&temp12&temp13&temp14')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*3.848100))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*2.514900))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*4.848000))
cmd.select('temp15', 'all w. %s of jessatom0'%(d*4.534900))
cmd.select('temp16', 'all w. %s of jessatom1'%(d*3.009800))
cmd.select('temp17', 'all w. %s of jessatom2'%(d*5.312600))
cmd.select('temp18', 'all w. %s of jessatom3'%(d*1.535200))
cmd.select('temp19', 'br. jessatom3')
cmd.select('jessatom4', '((temp6&temp10)|(temp6&temp11))&temp15&temp16&temp17&temp18&temp19')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*4.534900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*3.009800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*5.312600))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*1.535200))
cmd.select('temp20', 'n. og')
cmd.select('temp21', 'all w. %s of jessatom0'%(d*5.928700))
cmd.select('temp22', 'all w. %s of jessatom1'%(d*4.413700))
cmd.select('temp23', 'all w. %s of jessatom2'%(d*6.726600))
cmd.select('temp24', 'all w. %s of jessatom3'%(d*2.444200))
cmd.select('temp25', 'br. jessatom3')
cmd.select('temp26', 'all w. %s of jessatom4'%(d*1.434200))
cmd.select('jessatom5', '((temp20&temp10)|(temp20&temp11))&temp21&temp22&temp23&temp24&temp25&temp26')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*5.928700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*4.413700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*6.726600))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*2.444200))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.434200))
cmd.select('temp27', 'n. n')
cmd.select('temp28', 'r. gly')
cmd.select('temp29', 'all w. %s of jessatom0'%(d*3.918800))
cmd.select('temp30', 'all w. %s of jessatom2'%(d*5.342900))
cmd.select('temp31', 'all w. %s of jessatom3'%(d*2.413900))
cmd.select('temp32', 'all w. %s of jessatom4'%(d*3.191600))
cmd.select('temp33', 'all w. %s of jessatom5'%(d*3.939000))
cmd.select('jessatom6', 'temp27&temp28&temp29&temp16&temp30&temp31&temp32&temp33')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*3.918800))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*3.009800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*5.342900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*2.413900))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*3.191600))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*3.939000))
cmd.select('temp34', 'all w. %s of jessatom0'%(d*4.716700))
cmd.select('temp35', 'all w. %s of jessatom1'%(d*4.151100))
cmd.select('temp36', 'all w. %s of jessatom2'%(d*6.211500))
cmd.select('temp37', 'all w. %s of jessatom3'%(d*3.817800))
cmd.select('temp38', 'all w. %s of jessatom4'%(d*4.595500))
cmd.select('temp39', 'all w. %s of jessatom5'%(d*5.191400))
cmd.select('temp40', 'all w. %s of jessatom6'%(d*1.444300))
cmd.select('temp41', 'br. jessatom6')
cmd.select('jessatom7', 'temp0&temp28&temp34&temp35&temp36&temp37&temp38&temp39&temp40&temp41')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*4.716700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*4.151100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*6.211500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*3.817800))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*4.595500))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*5.191400))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.444300))
cmd.select('temp42', 'all w. %s of jessatom0'%(d*4.989400))
cmd.select('temp43', 'all w. %s of jessatom1'%(d*4.565200))
cmd.select('temp44', 'all w. %s of jessatom2'%(d*6.403400))
cmd.select('temp45', 'all w. %s of jessatom3'%(d*4.827800))
cmd.select('temp46', 'all w. %s of jessatom4'%(d*5.282300))
cmd.select('temp47', 'all w. %s of jessatom5'%(d*5.969100))
cmd.select('temp48', 'all w. %s of jessatom6'%(d*2.474500))
cmd.select('temp49', 'br. jessatom6')
cmd.select('temp50', 'all w. %s of jessatom7'%(d*1.535200))
cmd.select('jessatom8', 'temp2&temp28&temp42&temp43&temp44&temp45&temp46&temp47&temp48&temp49&temp50')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*4.989400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*4.565200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*6.403400))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*4.827800))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*5.282300))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*5.969100))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*2.474500))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*1.535200))
cmd.select('temp51', 'n. ce1')
cmd.select('temp52', 'r. tyr')
cmd.select('temp53', 'all w. %s of jessatom0'%(d*44.581400))
cmd.select('temp54', 'all w. %s of jessatom1'%(d*46.106500))
cmd.select('temp55', 'all w. %s of jessatom2'%(d*44.248100))
cmd.select('temp56', 'all w. %s of jessatom3'%(d*48.126500))
cmd.select('temp57', 'all w. %s of jessatom4'%(d*49.075900))
cmd.select('temp58', 'all w. %s of jessatom5'%(d*50.419200))
cmd.select('temp59', 'all w. %s of jessatom6'%(d*47.086200))
cmd.select('temp60', 'all w. %s of jessatom7'%(d*46.540800))
cmd.select('temp61', 'all w. %s of jessatom8'%(d*46.076200))
cmd.select('jessatom9', 'temp51&temp52&temp53&temp54&temp55&temp56&temp57&temp58&temp59&temp60&temp61')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom9'%(d*44.581400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom9'%(d*46.106500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom9'%(d*44.248100))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom9'%(d*48.126500))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom9'%(d*49.075900))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom9'%(d*50.419200))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom9'%(d*47.086200))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom9'%(d*46.540800))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom9'%(d*46.076200))
cmd.select('temp62', 'n. cz')
cmd.select('temp63', 'all w. %s of jessatom0'%(d*44.096600))
cmd.select('temp64', 'all w. %s of jessatom1'%(d*45.621700))
cmd.select('temp65', 'all w. %s of jessatom2'%(d*43.712800))
cmd.select('temp66', 'all w. %s of jessatom3'%(d*47.672000))
cmd.select('temp67', 'all w. %s of jessatom4'%(d*48.611300))
cmd.select('temp68', 'all w. %s of jessatom5'%(d*49.954600))
cmd.select('temp69', 'all w. %s of jessatom6'%(d*46.692300))
cmd.select('temp70', 'all w. %s of jessatom7'%(d*46.187300))
cmd.select('temp71', 'all w. %s of jessatom8'%(d*45.722700))
cmd.select('temp72', 'all w. %s of jessatom9'%(d*1.393800))
cmd.select('temp73', 'br. jessatom9')
cmd.select('jessatom10', 'temp62&temp52&temp63&temp64&temp65&temp66&temp67&temp68&temp69&temp70&temp71&temp72&temp73')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom10'%(d*44.096600))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom10'%(d*45.621700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom10'%(d*43.712800))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom10'%(d*47.672000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom10'%(d*48.611300))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom10'%(d*49.954600))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom10'%(d*46.692300))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom10'%(d*46.187300))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom10'%(d*45.722700))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom10'%(d*1.393800))
cmd.select('temp74', 'n. oh')
cmd.select('temp75', 'all w. %s of jessatom0'%(d*44.884400))
cmd.select('temp76', 'all w. %s of jessatom1'%(d*46.409500))
cmd.select('temp77', 'all w. %s of jessatom2'%(d*44.470300))
cmd.select('temp78', 'all w. %s of jessatom3'%(d*48.459800))
cmd.select('temp79', 'all w. %s of jessatom4'%(d*49.399100))
cmd.select('temp80', 'all w. %s of jessatom5'%(d*50.752500))
cmd.select('temp81', 'all w. %s of jessatom6'%(d*47.530600))
cmd.select('temp82', 'all w. %s of jessatom7'%(d*47.045800))
cmd.select('temp83', 'all w. %s of jessatom8'%(d*46.621600))
cmd.select('temp84', 'all w. %s of jessatom9'%(d*2.393700))
cmd.select('temp85', 'br. jessatom9')
cmd.select('temp86', 'all w. %s of jessatom10'%(d*1.393800))
cmd.select('jessatom11', 'temp74&temp52&temp75&temp76&temp77&temp78&temp79&temp80&temp81&temp82&temp83&temp84&temp85&temp86')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom11'%(d*44.884400))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom11'%(d*46.409500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom11'%(d*44.470300))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom11'%(d*48.459800))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom11'%(d*49.399100))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom11'%(d*50.752500))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom11'%(d*47.530600))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom11'%(d*47.045800))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom11'%(d*46.621600))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom11'%(d*2.393700))
cmd.select('jessatom10', 'jessatom10 w. %s of jessatom11'%(d*1.393800))
cmd.select('temp87', 'n. cd')
cmd.select('temp88', 'r. glu')
cmd.select('temp89', 'r. asp')
cmd.select('temp90', 'all w. %s of jessatom0'%(d*5.837800))
cmd.select('temp91', 'all w. %s of jessatom1'%(d*4.696500))
cmd.select('temp92', 'all w. %s of jessatom2'%(d*5.656000))
cmd.select('temp93', 'all w. %s of jessatom3'%(d*4.979300))
cmd.select('temp94', 'all w. %s of jessatom4'%(d*3.767300))
cmd.select('temp95', 'all w. %s of jessatom5'%(d*4.383400))
cmd.select('temp96', 'all w. %s of jessatom6'%(d*6.464000))
cmd.select('temp97', 'all w. %s of jessatom7'%(d*7.777000))
cmd.select('temp98', 'all w. %s of jessatom8'%(d*7.938600))
cmd.select('temp99', 'all w. %s of jessatom9'%(d*49.540500))
cmd.select('temp100', 'all w. %s of jessatom10'%(d*48.995100))
cmd.select('temp101', 'all w. %s of jessatom11'%(d*49.752600))
cmd.select('jessatom12', '((temp87&temp88)|(temp87&temp89))&temp90&temp91&temp92&temp93&temp94&temp95&temp96&temp97&temp98&temp99&temp100&temp101')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom12'%(d*5.837800))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom12'%(d*4.696500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom12'%(d*5.656000))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom12'%(d*4.979300))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom12'%(d*3.767300))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom12'%(d*4.383400))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom12'%(d*6.464000))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom12'%(d*7.777000))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom12'%(d*7.938600))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom12'%(d*49.540500))
cmd.select('jessatom10', 'jessatom10 w. %s of jessatom12'%(d*48.995100))
cmd.select('jessatom11', 'jessatom11 w. %s of jessatom12'%(d*49.752600))
cmd.select('temp102', 'n. oe1')
cmd.select('temp103', 'n. oe2')
cmd.select('temp104', 'n. od1')
cmd.select('temp105', 'n. od2')
cmd.select('temp106', 'all w. %s of jessatom0'%(d*5.070200))
cmd.select('temp107', 'all w. %s of jessatom1'%(d*4.120800))
cmd.select('temp108', 'all w. %s of jessatom2'%(d*4.807600))
cmd.select('temp109', 'all w. %s of jessatom3'%(d*5.029800))
cmd.select('temp110', 'all w. %s of jessatom4'%(d*3.999600))
cmd.select('temp111', 'all w. %s of jessatom5'%(d*4.928800))
cmd.select('temp112', 'all w. %s of jessatom6'%(d*6.181200))
cmd.select('temp113', 'all w. %s of jessatom7'%(d*7.403300))
cmd.select('temp114', 'all w. %s of jessatom8'%(d*7.413400))
cmd.select('temp115', 'all w. %s of jessatom9'%(d*48.399200))
cmd.select('temp116', 'all w. %s of jessatom10'%(d*47.853800))
cmd.select('temp117', 'all w. %s of jessatom11'%(d*48.611300))
cmd.select('temp118', 'all w. %s of jessatom12'%(d*1.262500))
cmd.select('temp119', 'br. jessatom12')
cmd.select('jessatom13', '(((temp102|temp103)&temp88)|((temp104|temp105)&temp89))&temp106&temp107&temp108&temp109&temp110&temp111&temp112&temp113&temp114&temp115&temp116&temp117&temp118&temp119')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom13'%(d*5.070200))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom13'%(d*4.120800))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom13'%(d*4.807600))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom13'%(d*5.029800))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom13'%(d*3.999600))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom13'%(d*4.928800))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom13'%(d*6.181200))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom13'%(d*7.403300))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom13'%(d*7.413400))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom13'%(d*48.399200))
cmd.select('jessatom10', 'jessatom10 w. %s of jessatom13'%(d*47.853800))
cmd.select('jessatom11', 'jessatom11 w. %s of jessatom13'%(d*48.611300))
cmd.select('jessatom12', 'jessatom12 w. %s of jessatom13'%(d*1.262500))
cmd.select('temp120', 'n. oe2')
cmd.select('temp121', 'n. oe1')
cmd.select('temp122', 'n. od2')
cmd.select('temp123', 'n. od1')
cmd.select('temp124', 'all w. %s of jessatom0'%(d*6.171100))
cmd.select('temp125', 'all w. %s of jessatom1'%(d*4.817700))
cmd.select('temp126', 'all w. %s of jessatom2'%(d*6.282200))
cmd.select('temp127', 'all w. %s of jessatom3'%(d*4.524800))
cmd.select('temp128', 'all w. %s of jessatom4'%(d*3.100700))
cmd.select('temp129', 'all w. %s of jessatom5'%(d*3.403700))
cmd.select('temp130', 'all w. %s of jessatom6'%(d*5.989300))
cmd.select('temp131', 'all w. %s of jessatom7'%(d*7.292200))
cmd.select('temp132', 'all w. %s of jessatom8'%(d*7.534600))
cmd.select('temp133', 'all w. %s of jessatom9'%(d*50.298000))
cmd.select('temp134', 'all w. %s of jessatom10'%(d*49.772800))
cmd.select('temp135', 'all w. %s of jessatom11'%(d*50.550500))
cmd.select('temp136', 'br. jessatom12')
cmd.select('temp137', 'all w. %s of jessatom13'%(d*2.232100))
cmd.select('jessatom14', '(((temp120|temp121)&temp88)|((temp122|temp123)&temp89))&temp124&temp125&temp126&temp127&temp128&temp129&temp130&temp131&temp132&temp133&temp134&temp135&temp118&temp136&temp137')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom14'%(d*6.171100))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom14'%(d*4.817700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom14'%(d*6.282200))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom14'%(d*4.524800))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom14'%(d*3.100700))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom14'%(d*3.403700))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom14'%(d*5.989300))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom14'%(d*7.292200))
cmd.select('jessatom8', 'jessatom8 w. %s of jessatom14'%(d*7.534600))
cmd.select('jessatom9', 'jessatom9 w. %s of jessatom14'%(d*50.298000))
cmd.select('jessatom10', 'jessatom10 w. %s of jessatom14'%(d*49.772800))
cmd.select('jessatom11', 'jessatom11 w. %s of jessatom14'%(d*50.550500))
cmd.select('jessatom12', 'jessatom12 w. %s of jessatom14'%(d*1.262500))
cmd.select('jessatom13', 'jessatom13 w. %s of jessatom14'%(d*2.232100))
cmd.select('Jfa_1gk2_4_3_1_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11|br. jessatom12|br. jessatom13|br. jessatom14')
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
cmd.delete('jessatom12')
cmd.delete('jessatom13')
cmd.delete('jessatom14')
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
cmd.delete('temp93')
cmd.delete('temp94')
cmd.delete('temp95')
cmd.delete('temp96')
cmd.delete('temp97')
cmd.delete('temp98')
cmd.delete('temp99')
cmd.delete('temp100')
cmd.delete('temp101')
cmd.delete('temp102')
cmd.delete('temp103')
cmd.delete('temp104')
cmd.delete('temp105')
cmd.delete('temp106')
cmd.delete('temp107')
cmd.delete('temp108')
cmd.delete('temp109')
cmd.delete('temp110')
cmd.delete('temp111')
cmd.delete('temp112')
cmd.delete('temp113')
cmd.delete('temp114')
cmd.delete('temp115')
cmd.delete('temp116')
cmd.delete('temp117')
cmd.delete('temp118')
cmd.delete('temp119')
cmd.delete('temp120')
cmd.delete('temp121')
cmd.delete('temp122')
cmd.delete('temp123')
cmd.delete('temp124')
cmd.delete('temp125')
cmd.delete('temp126')
cmd.delete('temp127')
cmd.delete('temp128')
cmd.delete('temp129')
cmd.delete('temp130')
cmd.delete('temp131')
cmd.delete('temp132')
cmd.delete('temp133')
cmd.delete('temp134')
cmd.delete('temp135')
cmd.delete('temp136')
cmd.delete('temp137')