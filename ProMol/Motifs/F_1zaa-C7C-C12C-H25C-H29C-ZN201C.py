'''
FUNC:F_1zaa-C7C-C12C-H25C-H29C-ZN201C
PDB:1zaa
EC:N/A
PFAM:PF13465,PF00096
RESI:cys,cys,his,his,zn
LOCI:c-7,12,25,29,201;
'''
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*4.87))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.44))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.11))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.23))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. CB&r. his'%(d*7.63))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. CG&r. his'%(d*6.24))
cmd.select('zn7', 'n. ZN&r. zn w. %s of n. ND1&r. his'%(d*6.30))
cmd.select('zn8', 'n. ZN&r. zn w. %s of n. CD2&r. his'%(d*5.05))
cmd.select('zn9', 'n. ZN&r. zn w. %s of n. CE1&r. his'%(d*5.20))
cmd.select('zn10', 'n. ZN&r. zn w. %s of n. NE2&r. his'%(d*4.14))
cmd.select('zn11', 'n. ZN&r. zn w. %s of n. CB&r. his'%(d*7.18))
cmd.select('zn12', 'n. ZN&r. zn w. %s of n. CG&r. his'%(d*5.83))
cmd.select('zn13', 'n. ZN&r. zn w. %s of n. ND1&r. his'%(d*6.04))
cmd.select('zn14', 'n. ZN&r. zn w. %s of n. CD2&r. his'%(d*4.59))
cmd.select('zn15', 'n. ZN&r. zn w. %s of n. CE1&r. his'%(d*5.07))
cmd.select('zn16', 'n. ZN&r. zn w. %s of n. NE2&r. his'%(d*3.88))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6&br. zn7&br. zn8&br. zn9&br. zn10&br. zn11&br. zn12&br. zn13&br. zn14&br. zn15&br. zn16')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.delete('zn6')
cmd.delete('zn7')
cmd.delete('zn8')
cmd.delete('zn9')
cmd.delete('zn10')
cmd.delete('zn11')
cmd.delete('zn12')
cmd.delete('zn13')
cmd.delete('zn14')
cmd.delete('zn15')
cmd.delete('zn16')
cmd.select('cys1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*4.87))
cmd.select('cys2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.44))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*6.29))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*5.83))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*5.81))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.85))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*10.33))
cmd.select('cys8', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*8.88))
cmd.select('cys9', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*8.63))
cmd.select('cys10', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*7.82))
cmd.select('cys11', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*7.35))
cmd.select('cys12', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*6.71))
cmd.select('cys13', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*9.08))
cmd.select('cys14', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*7.63))
cmd.select('cys15', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*7.21))
cmd.select('cys16', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*6.78))
cmd.select('cys17', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*5.95))
cmd.select('cys18', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*5.57))
cmd.select('cys19', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*8.78))
cmd.select('cys20', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*7.38))
cmd.select('cys21', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*6.99))
cmd.select('cys22', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*6.60))
cmd.select('cys23', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*5.83))
cmd.select('cys24', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*5.49))
cmd.select('cys25', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*9.28))
cmd.select('cys26', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*7.83))
cmd.select('cys27', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*7.56))
cmd.select('cys28', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*6.81))
cmd.select('cys29', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*6.29))
cmd.select('cys30', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*5.67))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27&br. cys28&br. cys29&br. cys30')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
cmd.delete('cys28')
cmd.delete('cys29')
cmd.delete('cys30')
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.11))
cmd.select('cysi2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.23))
cmd.select('cysi3', 'n. CB&r. cys w. %s of n. CB&cys'%(d*6.29))
cmd.select('cysi4', 'n. CB&r. cys w. %s of n. SG&cys'%(d*5.81))
cmd.select('cysi5', 'n. SG&r. cys w. %s of n. CB&cys'%(d*5.83))
cmd.select('cysi6', 'n. SG&r. cys w. %s of n. SG&cys'%(d*5.85))
cmd.select('cysi7', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*8.15))
cmd.select('cysi8', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*7.14))
cmd.select('cysi9', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*7.63))
cmd.select('cysi10', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*6.03))
cmd.select('cysi11', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*6.96))
cmd.select('cysi12', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*5.90))
cmd.select('cysi13', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*8.19))
cmd.select('cysi14', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*7.10))
cmd.select('cysi15', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*7.65))
cmd.select('cysi16', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*5.76))
cmd.select('cysi17', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*6.86))
cmd.select('cysi18', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*5.59))
cmd.select('cysi19', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*9.31))
cmd.select('cysi20', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*8.27))
cmd.select('cysi21', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*8.82))
cmd.select('cysi22', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*6.98))
cmd.select('cysi23', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*8.02))
cmd.select('cysi24', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*6.80))
cmd.select('cysi25', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*7.59))
cmd.select('cysi26', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*6.61))
cmd.select('cysi27', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*7.25))
cmd.select('cysi28', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*5.39))
cmd.select('cysi29', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*6.64))
cmd.select('cysi30', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*5.44))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12&br. cysi13&br. cysi14&br. cysi15&br. cysi16&br. cysi17&br. cysi18&br. cysi19&br. cysi20&br. cysi21&br. cysi22&br. cysi23&br. cysi24&br. cysi25&br. cysi26&br. cysi27&br. cysi28&br. cysi29&br. cysi30')
cmd.delete('cysi1')
cmd.delete('cysi2')
cmd.delete('cysi3')
cmd.delete('cysi4')
cmd.delete('cysi5')
cmd.delete('cysi6')
cmd.delete('cysi7')
cmd.delete('cysi8')
cmd.delete('cysi9')
cmd.delete('cysi10')
cmd.delete('cysi11')
cmd.delete('cysi12')
cmd.delete('cysi13')
cmd.delete('cysi14')
cmd.delete('cysi15')
cmd.delete('cysi16')
cmd.delete('cysi17')
cmd.delete('cysi18')
cmd.delete('cysi19')
cmd.delete('cysi20')
cmd.delete('cysi21')
cmd.delete('cysi22')
cmd.delete('cysi23')
cmd.delete('cysi24')
cmd.delete('cysi25')
cmd.delete('cysi26')
cmd.delete('cysi27')
cmd.delete('cysi28')
cmd.delete('cysi29')
cmd.delete('cysi30')
cmd.select('his1', 'n. CB&r. his w. %s of n. ZN&zn'%(d*7.63))
cmd.select('his2', 'n. CG&r. his w. %s of n. ZN&zn'%(d*6.24))
cmd.select('his3', 'n. ND1&r. his w. %s of n. ZN&zn'%(d*6.30))
cmd.select('his4', 'n. CD2&r. his w. %s of n. ZN&zn'%(d*5.05))
cmd.select('his5', 'n. CE1&r. his w. %s of n. ZN&zn'%(d*5.20))
cmd.select('his6', 'n. NE2&r. his w. %s of n. ZN&zn'%(d*4.14))
cmd.select('his7', 'n. CB&r. his w. %s of n. CB&cys'%(d*10.33))
cmd.select('his8', 'n. CB&r. his w. %s of n. SG&cys'%(d*9.08))
cmd.select('his9', 'n. CG&r. his w. %s of n. CB&cys'%(d*8.88))
cmd.select('his10', 'n. CG&r. his w. %s of n. SG&cys'%(d*7.63))
cmd.select('his11', 'n. ND1&r. his w. %s of n. CB&cys'%(d*8.63))
cmd.select('his12', 'n. ND1&r. his w. %s of n. SG&cys'%(d*7.21))
cmd.select('his13', 'n. CD2&r. his w. %s of n. CB&cys'%(d*7.82))
cmd.select('his14', 'n. CD2&r. his w. %s of n. SG&cys'%(d*6.78))
cmd.select('his15', 'n. CE1&r. his w. %s of n. CB&cys'%(d*7.35))
cmd.select('his16', 'n. CE1&r. his w. %s of n. SG&cys'%(d*5.95))
cmd.select('his17', 'n. NE2&r. his w. %s of n. CB&cys'%(d*6.71))
cmd.select('his18', 'n. NE2&r. his w. %s of n. SG&cys'%(d*5.57))
cmd.select('his19', 'n. CB&r. his w. %s of n. CB&cysi'%(d*8.15))
cmd.select('his20', 'n. CB&r. his w. %s of n. SG&cysi'%(d*8.19))
cmd.select('his21', 'n. CG&r. his w. %s of n. CB&cysi'%(d*7.14))
cmd.select('his22', 'n. CG&r. his w. %s of n. SG&cysi'%(d*7.10))
cmd.select('his23', 'n. ND1&r. his w. %s of n. CB&cysi'%(d*7.63))
cmd.select('his24', 'n. ND1&r. his w. %s of n. SG&cysi'%(d*7.65))
cmd.select('his25', 'n. CD2&r. his w. %s of n. CB&cysi'%(d*6.03))
cmd.select('his26', 'n. CD2&r. his w. %s of n. SG&cysi'%(d*5.76))
cmd.select('his27', 'n. CE1&r. his w. %s of n. CB&cysi'%(d*6.96))
cmd.select('his28', 'n. CE1&r. his w. %s of n. SG&cysi'%(d*6.86))
cmd.select('his29', 'n. NE2&r. his w. %s of n. CB&cysi'%(d*5.90))
cmd.select('his30', 'n. NE2&r. his w. %s of n. SG&cysi'%(d*5.59))
cmd.select('his31', 'n. CB&r. his w. %s of n. CB&r. his'%(d*9.72))
cmd.select('his32', 'n. CB&r. his w. %s of n. CG&r. his'%(d*9.10))
cmd.select('his33', 'n. CB&r. his w. %s of n. ND1&r. his'%(d*9.83))
cmd.select('his34', 'n. CB&r. his w. %s of n. CD2&r. his'%(d*8.11))
cmd.select('his35', 'n. CB&r. his w. %s of n. CE1&r. his'%(d*9.40))
cmd.select('his36', 'n. CB&r. his w. %s of n. NE2&r. his'%(d*8.36))
cmd.select('his37', 'n. CG&r. his w. %s of n. CB&r. his'%(d*8.90))
cmd.select('his38', 'n. CG&r. his w. %s of n. CG&r. his'%(d*8.05))
cmd.select('his39', 'n. CG&r. his w. %s of n. ND1&r. his'%(d*8.65))
cmd.select('his40', 'n. CG&r. his w. %s of n. CD2&r. his'%(d*6.98))
cmd.select('his41', 'n. CG&r. his w. %s of n. CE1&r. his'%(d*8.09))
cmd.select('his42', 'n. CG&r. his w. %s of n. NE2&r. his'%(d*7.03))
cmd.select('his43', 'n. ND1&r. his w. %s of n. CB&r. his'%(d*9.35))
cmd.select('his44', 'n. ND1&r. his w. %s of n. CG&r. his'%(d*8.34))
cmd.select('his45', 'n. ND1&r. his w. %s of n. ND1&r. his'%(d*8.66))
cmd.select('his46', 'n. ND1&r. his w. %s of n. CD2&r. his'%(d*7.33))
cmd.select('his47', 'n. ND1&r. his w. %s of n. CE1&r. his'%(d*7.93))
cmd.select('his48', 'n. ND1&r. his w. %s of n. NE2&r. his'%(d*7.05))
cmd.select('his49', 'n. CD2&r. his w. %s of n. CB&r. his'%(d*7.97))
cmd.select('his50', 'n. CD2&r. his w. %s of n. CG&r. his'%(d*7.05))
cmd.select('his50',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36&br. his37&br. his38&br. his39&br. his40&br. his41&br. his42&br. his43&br. his44&br. his45&br. his46&br. his47&br. his48&br. his49&br. his50')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
cmd.delete('his37')
cmd.delete('his38')
cmd.delete('his39')
cmd.delete('his40')
cmd.delete('his41')
cmd.delete('his42')
cmd.delete('his43')
cmd.delete('his44')
cmd.delete('his45')
cmd.delete('his46')
cmd.delete('his47')
cmd.delete('his48')
cmd.delete('his49')
cmd.select('his51', 'n. CD2&r. his w. %s of n. ND1&r. his'%(d*7.72))
cmd.select('his52', 'n. CD2&r. his w. %s of n. CD2&r. his'%(d*5.86))
cmd.select('his53', 'n. CD2&r. his w. %s of n. CE1&r. his'%(d*7.14))
cmd.select('his54', 'n. CD2&r. his w. %s of n. NE2&r. his'%(d*5.96))
cmd.select('his55', 'n. CE1&r. his w. %s of n. CB&r. his'%(d*8.77))
cmd.select('his56', 'n. CE1&r. his w. %s of n. CG&r. his'%(d*7.59))
cmd.select('his57', 'n. CE1&r. his w. %s of n. ND1&r. his'%(d*7.75))
cmd.select('his58', 'n. CE1&r. his w. %s of n. CD2&r. his'%(d*6.54))
cmd.select('his59', 'n. CE1&r. his w. %s of n. CE1&r. his'%(d*6.86))
cmd.select('his60', 'n. CE1&r. his w. %s of n. NE2&r. his'%(d*6.00))
cmd.select('his61', 'n. NE2&r. his w. %s of n. CB&r. his'%(d*7.90))
cmd.select('his62', 'n. NE2&r. his w. %s of n. CG&r. his'%(d*6.72))
cmd.select('his63', 'n. NE2&r. his w. %s of n. ND1&r. his'%(d*7.08))
cmd.select('his64', 'n. NE2&r. his w. %s of n. CD2&r. his'%(d*5.52))
cmd.select('his65', 'n. NE2&r. his w. %s of n. CE1&r. his'%(d*6.26))
cmd.select('his66', 'n. NE2&r. his w. %s of n. NE2&r. his'%(d*5.15))
cmd.select('his',' his50&br. his51&br. his52&br. his53&br. his54&br. his55&br. his56&br. his57&br. his58&br. his59&br. his60&br. his61&br. his62&br. his63&br. his64&br. his65&br. his66')
cmd.delete('his50')
cmd.delete('his51')
cmd.delete('his52')
cmd.delete('his53')
cmd.delete('his54')
cmd.delete('his55')
cmd.delete('his56')
cmd.delete('his57')
cmd.delete('his58')
cmd.delete('his59')
cmd.delete('his60')
cmd.delete('his61')
cmd.delete('his62')
cmd.delete('his63')
cmd.delete('his64')
cmd.delete('his65')
cmd.delete('his66')
cmd.select('hisi1', 'n. CB&r. his w. %s of n. ZN&zn'%(d*7.18))
cmd.select('hisi2', 'n. CG&r. his w. %s of n. ZN&zn'%(d*5.83))
cmd.select('hisi3', 'n. ND1&r. his w. %s of n. ZN&zn'%(d*6.04))
cmd.select('hisi4', 'n. CD2&r. his w. %s of n. ZN&zn'%(d*4.59))
cmd.select('hisi5', 'n. CE1&r. his w. %s of n. ZN&zn'%(d*5.07))
cmd.select('hisi6', 'n. NE2&r. his w. %s of n. ZN&zn'%(d*3.88))
cmd.select('hisi7', 'n. CB&r. his w. %s of n. CB&cys'%(d*8.78))
cmd.select('hisi8', 'n. CB&r. his w. %s of n. SG&cys'%(d*9.28))
cmd.select('hisi9', 'n. CG&r. his w. %s of n. CB&cys'%(d*7.38))
cmd.select('hisi10', 'n. CG&r. his w. %s of n. SG&cys'%(d*7.83))
cmd.select('hisi11', 'n. ND1&r. his w. %s of n. CB&cys'%(d*6.99))
cmd.select('hisi12', 'n. ND1&r. his w. %s of n. SG&cys'%(d*7.56))
cmd.select('hisi13', 'n. CD2&r. his w. %s of n. CB&cys'%(d*6.60))
cmd.select('hisi14', 'n. CD2&r. his w. %s of n. SG&cys'%(d*6.81))
cmd.select('hisi15', 'n. CE1&r. his w. %s of n. CB&cys'%(d*5.83))
cmd.select('hisi16', 'n. CE1&r. his w. %s of n. SG&cys'%(d*6.29))
cmd.select('hisi17', 'n. NE2&r. his w. %s of n. CB&cys'%(d*5.49))
cmd.select('hisi18', 'n. NE2&r. his w. %s of n. SG&cys'%(d*5.67))
cmd.select('hisi19', 'n. CB&r. his w. %s of n. CB&cysi'%(d*9.31))
cmd.select('hisi20', 'n. CB&r. his w. %s of n. SG&cysi'%(d*7.59))
cmd.select('hisi21', 'n. CG&r. his w. %s of n. CB&cysi'%(d*8.27))
cmd.select('hisi22', 'n. CG&r. his w. %s of n. SG&cysi'%(d*6.61))
cmd.select('hisi23', 'n. ND1&r. his w. %s of n. CB&cysi'%(d*8.82))
cmd.select('hisi24', 'n. ND1&r. his w. %s of n. SG&cysi'%(d*7.25))
cmd.select('hisi25', 'n. CD2&r. his w. %s of n. CB&cysi'%(d*6.98))
cmd.select('hisi26', 'n. CD2&r. his w. %s of n. SG&cysi'%(d*5.39))
cmd.select('hisi27', 'n. CE1&r. his w. %s of n. CB&cysi'%(d*8.02))
cmd.select('hisi28', 'n. CE1&r. his w. %s of n. SG&cysi'%(d*6.64))
cmd.select('hisi29', 'n. NE2&r. his w. %s of n. CB&cysi'%(d*6.80))
cmd.select('hisi30', 'n. NE2&r. his w. %s of n. SG&cysi'%(d*5.44))
cmd.select('hisi31', 'n. CB&r. his w. %s of n. CB&his'%(d*9.72))
cmd.select('hisi32', 'n. CB&r. his w. %s of n. CG&his'%(d*8.90))
cmd.select('hisi33', 'n. CB&r. his w. %s of n. ND1&his'%(d*9.35))
cmd.select('hisi34', 'n. CB&r. his w. %s of n. CD2&his'%(d*7.97))
cmd.select('hisi35', 'n. CB&r. his w. %s of n. CE1&his'%(d*8.77))
cmd.select('hisi36', 'n. CB&r. his w. %s of n. NE2&his'%(d*7.90))
cmd.select('hisi37', 'n. CG&r. his w. %s of n. CB&his'%(d*9.10))
cmd.select('hisi38', 'n. CG&r. his w. %s of n. CG&his'%(d*8.05))
cmd.select('hisi39', 'n. CG&r. his w. %s of n. ND1&his'%(d*8.34))
cmd.select('hisi40', 'n. CG&r. his w. %s of n. CD2&his'%(d*7.05))
cmd.select('hisi41', 'n. CG&r. his w. %s of n. CE1&his'%(d*7.59))
cmd.select('hisi42', 'n. CG&r. his w. %s of n. NE2&his'%(d*6.72))
cmd.select('hisi43', 'n. ND1&r. his w. %s of n. CB&his'%(d*9.83))
cmd.select('hisi44', 'n. ND1&r. his w. %s of n. CG&his'%(d*8.65))
cmd.select('hisi45', 'n. ND1&r. his w. %s of n. ND1&his'%(d*8.66))
cmd.select('hisi46', 'n. ND1&r. his w. %s of n. CD2&his'%(d*7.72))
cmd.select('hisi47', 'n. ND1&r. his w. %s of n. CE1&his'%(d*7.75))
cmd.select('hisi48', 'n. ND1&r. his w. %s of n. NE2&his'%(d*7.08))
cmd.select('hisi49', 'n. CD2&r. his w. %s of n. CB&his'%(d*8.11))
cmd.select('hisi50', 'n. CD2&r. his w. %s of n. CG&his'%(d*6.98))
cmd.select('hisi50',' br. hisi1&br. hisi2&br. hisi3&br. hisi4&br. hisi5&br. hisi6&br. hisi7&br. hisi8&br. hisi9&br. hisi10&br. hisi11&br. hisi12&br. hisi13&br. hisi14&br. hisi15&br. hisi16&br. hisi17&br. hisi18&br. hisi19&br. hisi20&br. hisi21&br. hisi22&br. hisi23&br. hisi24&br. hisi25&br. hisi26&br. hisi27&br. hisi28&br. hisi29&br. hisi30&br. hisi31&br. hisi32&br. hisi33&br. hisi34&br. hisi35&br. hisi36&br. hisi37&br. hisi38&br. hisi39&br. hisi40&br. hisi41&br. hisi42&br. hisi43&br. hisi44&br. hisi45&br. hisi46&br. hisi47&br. hisi48&br. hisi49&br. hisi50')
cmd.delete('hisi1')
cmd.delete('hisi2')
cmd.delete('hisi3')
cmd.delete('hisi4')
cmd.delete('hisi5')
cmd.delete('hisi6')
cmd.delete('hisi7')
cmd.delete('hisi8')
cmd.delete('hisi9')
cmd.delete('hisi10')
cmd.delete('hisi11')
cmd.delete('hisi12')
cmd.delete('hisi13')
cmd.delete('hisi14')
cmd.delete('hisi15')
cmd.delete('hisi16')
cmd.delete('hisi17')
cmd.delete('hisi18')
cmd.delete('hisi19')
cmd.delete('hisi20')
cmd.delete('hisi21')
cmd.delete('hisi22')
cmd.delete('hisi23')
cmd.delete('hisi24')
cmd.delete('hisi25')
cmd.delete('hisi26')
cmd.delete('hisi27')
cmd.delete('hisi28')
cmd.delete('hisi29')
cmd.delete('hisi30')
cmd.delete('hisi31')
cmd.delete('hisi32')
cmd.delete('hisi33')
cmd.delete('hisi34')
cmd.delete('hisi35')
cmd.delete('hisi36')
cmd.delete('hisi37')
cmd.delete('hisi38')
cmd.delete('hisi39')
cmd.delete('hisi40')
cmd.delete('hisi41')
cmd.delete('hisi42')
cmd.delete('hisi43')
cmd.delete('hisi44')
cmd.delete('hisi45')
cmd.delete('hisi46')
cmd.delete('hisi47')
cmd.delete('hisi48')
cmd.delete('hisi49')
cmd.select('hisi51', 'n. CD2&r. his w. %s of n. ND1&his'%(d*7.33))
cmd.select('hisi52', 'n. CD2&r. his w. %s of n. CD2&his'%(d*5.86))
cmd.select('hisi53', 'n. CD2&r. his w. %s of n. CE1&his'%(d*6.54))
cmd.select('hisi54', 'n. CD2&r. his w. %s of n. NE2&his'%(d*5.52))
cmd.select('hisi55', 'n. CE1&r. his w. %s of n. CB&his'%(d*9.40))
cmd.select('hisi56', 'n. CE1&r. his w. %s of n. CG&his'%(d*8.09))
cmd.select('hisi57', 'n. CE1&r. his w. %s of n. ND1&his'%(d*7.93))
cmd.select('hisi58', 'n. CE1&r. his w. %s of n. CD2&his'%(d*7.14))
cmd.select('hisi59', 'n. CE1&r. his w. %s of n. CE1&his'%(d*6.86))
cmd.select('hisi60', 'n. CE1&r. his w. %s of n. NE2&his'%(d*6.26))
cmd.select('hisi61', 'n. NE2&r. his w. %s of n. CB&his'%(d*8.36))
cmd.select('hisi62', 'n. NE2&r. his w. %s of n. CG&his'%(d*7.03))
cmd.select('hisi63', 'n. NE2&r. his w. %s of n. ND1&his'%(d*7.05))
cmd.select('hisi64', 'n. NE2&r. his w. %s of n. CD2&his'%(d*5.96))
cmd.select('hisi65', 'n. NE2&r. his w. %s of n. CE1&his'%(d*6.00))
cmd.select('hisi66', 'n. NE2&r. his w. %s of n. NE2&his'%(d*5.15))
cmd.select('hisi',' hisi50&br. hisi51&br. hisi52&br. hisi53&br. hisi54&br. hisi55&br. hisi56&br. hisi57&br. hisi58&br. hisi59&br. hisi60&br. hisi61&br. hisi62&br. hisi63&br. hisi64&br. hisi65&br. hisi66')
cmd.delete('hisi50')
cmd.delete('hisi51')
cmd.delete('hisi52')
cmd.delete('hisi53')
cmd.delete('hisi54')
cmd.delete('hisi55')
cmd.delete('hisi56')
cmd.delete('hisi57')
cmd.delete('hisi58')
cmd.delete('hisi59')
cmd.delete('hisi60')
cmd.delete('hisi61')
cmd.delete('hisi62')
cmd.delete('hisi63')
cmd.delete('hisi64')
cmd.delete('hisi65')
cmd.delete('hisi66')
cmd.select('F_1zaa-C7C-C12C-H25C-H29C-ZN201C', 'zn|cys|cysi|his|hisi')
cmd.delete('zn')
cmd.delete('cys')
cmd.delete('cysi')
cmd.delete('his')
cmd.delete('hisi')
