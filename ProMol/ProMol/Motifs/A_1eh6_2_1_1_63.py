'''
FUNC:A_1eh6_2_1_1_63
PDB:1eh6
EC:2.1.1.63
RESI:asn,cys,his,glu
LOCI:a-137,145,146,172;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. asn'%(d*6.83))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&r. asn'%(d*6.78))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. OD1&r. asn'%(d*7.89))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. ND2&r. asn'%(d*5.82))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. CB&r. asn'%(d*6.70))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. CG&r. asn'%(d*6.53))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. OD1&r. asn'%(d*7.65))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. ND2&r. asn'%(d*5.45))
cmd.select('cys9', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*7.59))
cmd.select('cys10', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*8.06))
cmd.select('cys11', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*7.59))
cmd.select('cys12', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*9.26))
cmd.select('cys13', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*8.61))
cmd.select('cys14', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*9.55))
cmd.select('cys15', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*7.22))
cmd.select('cys16', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*7.71))
cmd.select('cys17', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*7.13))
cmd.select('cys18', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*9.01))
cmd.select('cys19', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*8.24))
cmd.select('cys20', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*9.29))
cmd.select('cys21', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*15.06))
cmd.select('cys22', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*14.20))
cmd.select('cys23', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*12.94))
cmd.select('cys24', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*12.87))
cmd.select('cys25', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*12.15))
cmd.select('cys26', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*14.99))
cmd.select('cys27', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*14.00))
cmd.select('cys28', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*12.85))
cmd.select('cys29', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*12.99))
cmd.select('cys30', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*11.95))
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
cmd.select('asn1', 'n. CB&r. asn w. %s of n. CB&cys'%(d*6.83))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. SG&cys'%(d*6.70))
cmd.select('asn3', 'n. CG&r. asn w. %s of n. CB&cys'%(d*6.78))
cmd.select('asn4', 'n. CG&r. asn w. %s of n. SG&cys'%(d*6.53))
cmd.select('asn5', 'n. OD1&r. asn w. %s of n. CB&cys'%(d*7.89))
cmd.select('asn6', 'n. OD1&r. asn w. %s of n. SG&cys'%(d*7.65))
cmd.select('asn7', 'n. ND2&r. asn w. %s of n. CB&cys'%(d*5.82))
cmd.select('asn8', 'n. ND2&r. asn w. %s of n. SG&cys'%(d*5.45))
cmd.select('asn9', 'n. CB&r. asn w. %s of n. CB&r. his'%(d*11.89))
cmd.select('asn10', 'n. CB&r. asn w. %s of n. CG&r. his'%(d*12.19))
cmd.select('asn11', 'n. CB&r. asn w. %s of n. ND1&r. his'%(d*11.35))
cmd.select('asn12', 'n. CB&r. asn w. %s of n. CD2&r. his'%(d*13.41))
cmd.select('asn13', 'n. CB&r. asn w. %s of n. CE1&r. his'%(d*12.18))
cmd.select('asn14', 'n. CB&r. asn w. %s of n. NE2&r. his'%(d*13.40))
cmd.select('asn15', 'n. CG&r. asn w. %s of n. CB&r. his'%(d*11.49))
cmd.select('asn16', 'n. CG&r. asn w. %s of n. CG&r. his'%(d*11.57))
cmd.select('asn17', 'n. CG&r. asn w. %s of n. ND1&r. his'%(d*10.59))
cmd.select('asn18', 'n. CG&r. asn w. %s of n. CD2&r. his'%(d*12.73))
cmd.select('asn19', 'n. CG&r. asn w. %s of n. CE1&r. his'%(d*11.28))
cmd.select('asn20', 'n. CG&r. asn w. %s of n. NE2&r. his'%(d*12.55))
cmd.select('asn21', 'n. OD1&r. asn w. %s of n. CB&r. his'%(d*12.44))
cmd.select('asn22', 'n. OD1&r. asn w. %s of n. CG&r. his'%(d*12.40))
cmd.select('asn23', 'n. OD1&r. asn w. %s of n. ND1&r. his'%(d*11.32))
cmd.select('asn24', 'n. OD1&r. asn w. %s of n. CD2&r. his'%(d*13.49))
cmd.select('asn25', 'n. OD1&r. asn w. %s of n. CE1&r. his'%(d*11.90))
cmd.select('asn26', 'n. OD1&r. asn w. %s of n. NE2&r. his'%(d*13.19))
cmd.select('asn27', 'n. ND2&r. asn w. %s of n. CB&r. his'%(d*10.22))
cmd.select('asn28', 'n. ND2&r. asn w. %s of n. CG&r. his'%(d*10.26))
cmd.select('asn29', 'n. ND2&r. asn w. %s of n. ND1&r. his'%(d*9.26))
cmd.select('asn30', 'n. ND2&r. asn w. %s of n. CD2&r. his'%(d*11.40))
cmd.select('asn31', 'n. ND2&r. asn w. %s of n. CE1&r. his'%(d*9.97))
cmd.select('asn32', 'n. ND2&r. asn w. %s of n. NE2&r. his'%(d*11.23))
cmd.select('asn33', 'n. CB&r. asn w. %s of n. CB&r. glu'%(d*19.19))
cmd.select('asn34', 'n. CB&r. asn w. %s of n. CG&r. glu'%(d*18.11))
cmd.select('asn35', 'n. CB&r. asn w. %s of n. CD&r. glu'%(d*16.85))
cmd.select('asn36', 'n. CB&r. asn w. %s of n. OE1&r. glu'%(d*16.92))
cmd.select('asn37', 'n. CB&r. asn w. %s of n. OE2&r. glu'%(d*15.87))
cmd.select('asn38', 'n. CG&r. asn w. %s of n. CB&r. glu'%(d*18.34))
cmd.select('asn39', 'n. CG&r. asn w. %s of n. CG&r. glu'%(d*17.20))
cmd.select('asn40', 'n. CG&r. asn w. %s of n. CD&r. glu'%(d*15.92))
cmd.select('asn41', 'n. CG&r. asn w. %s of n. OE1&r. glu'%(d*16.04))
cmd.select('asn42', 'n. CG&r. asn w. %s of n. OE2&r. glu'%(d*14.90))
cmd.select('asn43', 'n. OD1&r. asn w. %s of n. CB&r. glu'%(d*18.93))
cmd.select('asn44', 'n. OD1&r. asn w. %s of n. CG&r. glu'%(d*17.75))
cmd.select('asn45', 'n. OD1&r. asn w. %s of n. CD&r. glu'%(d*16.47))
cmd.select('asn46', 'n. OD1&r. asn w. %s of n. OE1&r. glu'%(d*16.59))
cmd.select('asn47', 'n. OD1&r. asn w. %s of n. OE2&r. glu'%(d*15.41))
cmd.select('asn48', 'n. ND2&r. asn w. %s of n. CB&r. glu'%(d*17.03))
cmd.select('asn49', 'n. ND2&r. asn w. %s of n. CG&r. glu'%(d*15.89))
cmd.select('asn50', 'n. ND2&r. asn w. %s of n. CD&r. glu'%(d*14.63))
cmd.select('asn50',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36&br. asn37&br. asn38&br. asn39&br. asn40&br. asn41&br. asn42&br. asn43&br. asn44&br. asn45&br. asn46&br. asn47&br. asn48&br. asn49&br. asn50')
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
cmd.delete('asn19')
cmd.delete('asn20')
cmd.delete('asn21')
cmd.delete('asn22')
cmd.delete('asn23')
cmd.delete('asn24')
cmd.delete('asn25')
cmd.delete('asn26')
cmd.delete('asn27')
cmd.delete('asn28')
cmd.delete('asn29')
cmd.delete('asn30')
cmd.delete('asn31')
cmd.delete('asn32')
cmd.delete('asn33')
cmd.delete('asn34')
cmd.delete('asn35')
cmd.delete('asn36')
cmd.delete('asn37')
cmd.delete('asn38')
cmd.delete('asn39')
cmd.delete('asn40')
cmd.delete('asn41')
cmd.delete('asn42')
cmd.delete('asn43')
cmd.delete('asn44')
cmd.delete('asn45')
cmd.delete('asn46')
cmd.delete('asn47')
cmd.delete('asn48')
cmd.delete('asn49')
cmd.select('asn51', 'n. ND2&r. asn w. %s of n. OE1&r. glu'%(d*14.75))
cmd.select('asn52', 'n. ND2&r. asn w. %s of n. OE2&r. glu'%(d*13.60))
cmd.select('asn',' asn50&br. asn51&br. asn52')
cmd.delete('asn50')
cmd.delete('asn51')
cmd.delete('asn52')
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&cys'%(d*7.59))
cmd.select('his2', 'n. CB&r. his w. %s of n. SG&cys'%(d*7.22))
cmd.select('his3', 'n. CG&r. his w. %s of n. CB&cys'%(d*8.06))
cmd.select('his4', 'n. CG&r. his w. %s of n. SG&cys'%(d*7.71))
cmd.select('his5', 'n. ND1&r. his w. %s of n. CB&cys'%(d*7.59))
cmd.select('his6', 'n. ND1&r. his w. %s of n. SG&cys'%(d*7.13))
cmd.select('his7', 'n. CD2&r. his w. %s of n. CB&cys'%(d*9.26))
cmd.select('his8', 'n. CD2&r. his w. %s of n. SG&cys'%(d*9.01))
cmd.select('his9', 'n. CE1&r. his w. %s of n. CB&cys'%(d*8.61))
cmd.select('his10', 'n. CE1&r. his w. %s of n. SG&cys'%(d*8.24))
cmd.select('his11', 'n. NE2&r. his w. %s of n. CB&cys'%(d*9.55))
cmd.select('his12', 'n. NE2&r. his w. %s of n. SG&cys'%(d*9.29))
cmd.select('his13', 'n. CB&r. his w. %s of n. CB&asn'%(d*11.89))
cmd.select('his14', 'n. CB&r. his w. %s of n. CG&asn'%(d*11.49))
cmd.select('his15', 'n. CB&r. his w. %s of n. OD1&asn'%(d*12.44))
cmd.select('his16', 'n. CB&r. his w. %s of n. ND2&asn'%(d*10.22))
cmd.select('his17', 'n. CG&r. his w. %s of n. CB&asn'%(d*12.19))
cmd.select('his18', 'n. CG&r. his w. %s of n. CG&asn'%(d*11.57))
cmd.select('his19', 'n. CG&r. his w. %s of n. OD1&asn'%(d*12.40))
cmd.select('his20', 'n. CG&r. his w. %s of n. ND2&asn'%(d*10.26))
cmd.select('his21', 'n. ND1&r. his w. %s of n. CB&asn'%(d*11.35))
cmd.select('his22', 'n. ND1&r. his w. %s of n. CG&asn'%(d*10.59))
cmd.select('his23', 'n. ND1&r. his w. %s of n. OD1&asn'%(d*11.32))
cmd.select('his24', 'n. ND1&r. his w. %s of n. ND2&asn'%(d*9.26))
cmd.select('his25', 'n. CD2&r. his w. %s of n. CB&asn'%(d*13.41))
cmd.select('his26', 'n. CD2&r. his w. %s of n. CG&asn'%(d*12.73))
cmd.select('his27', 'n. CD2&r. his w. %s of n. OD1&asn'%(d*13.49))
cmd.select('his28', 'n. CD2&r. his w. %s of n. ND2&asn'%(d*11.40))
cmd.select('his29', 'n. CE1&r. his w. %s of n. CB&asn'%(d*12.18))
cmd.select('his30', 'n. CE1&r. his w. %s of n. CG&asn'%(d*11.28))
cmd.select('his31', 'n. CE1&r. his w. %s of n. OD1&asn'%(d*11.90))
cmd.select('his32', 'n. CE1&r. his w. %s of n. ND2&asn'%(d*9.97))
cmd.select('his33', 'n. NE2&r. his w. %s of n. CB&asn'%(d*13.40))
cmd.select('his34', 'n. NE2&r. his w. %s of n. CG&asn'%(d*12.55))
cmd.select('his35', 'n. NE2&r. his w. %s of n. OD1&asn'%(d*13.19))
cmd.select('his36', 'n. NE2&r. his w. %s of n. ND2&asn'%(d*11.23))
cmd.select('his37', 'n. CB&r. his w. %s of n. CB&r. glu'%(d*10.38))
cmd.select('his38', 'n. CB&r. his w. %s of n. CG&r. glu'%(d*9.63))
cmd.select('his39', 'n. CB&r. his w. %s of n. CD&r. glu'%(d*8.76))
cmd.select('his40', 'n. CB&r. his w. %s of n. OE1&r. glu'%(d*8.97))
cmd.select('his41', 'n. CB&r. his w. %s of n. OE2&r. glu'%(d*8.15))
cmd.select('his42', 'n. CG&r. his w. %s of n. CB&r. glu'%(d*9.38))
cmd.select('his43', 'n. CG&r. his w. %s of n. CG&r. glu'%(d*8.48))
cmd.select('his44', 'n. CG&r. his w. %s of n. CD&r. glu'%(d*7.51))
cmd.select('his45', 'n. CG&r. his w. %s of n. OE1&r. glu'%(d*7.79))
cmd.select('his46', 'n. CG&r. his w. %s of n. OE2&r. glu'%(d*6.78))
cmd.select('his47', 'n. ND1&r. his w. %s of n. CB&r. glu'%(d*9.98))
cmd.select('his48', 'n. ND1&r. his w. %s of n. CG&r. glu'%(d*8.90))
cmd.select('his49', 'n. ND1&r. his w. %s of n. CD&r. glu'%(d*7.81))
cmd.select('his50', 'n. ND1&r. his w. %s of n. OE1&r. glu'%(d*8.14))
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
cmd.select('his51', 'n. ND1&r. his w. %s of n. OE2&r. glu'%(d*6.87))
cmd.select('his52', 'n. CD2&r. his w. %s of n. CB&r. glu'%(d*8.03))
cmd.select('his53', 'n. CD2&r. his w. %s of n. CG&r. glu'%(d*7.15))
cmd.select('his54', 'n. CD2&r. his w. %s of n. CD&r. glu'%(d*6.20))
cmd.select('his55', 'n. CD2&r. his w. %s of n. OE1&r. glu'%(d*6.51))
cmd.select('his56', 'n. CD2&r. his w. %s of n. OE2&r. glu'%(d*5.59))
cmd.select('his57', 'n. CE1&r. his w. %s of n. CB&r. glu'%(d*9.13))
cmd.select('his58', 'n. CE1&r. his w. %s of n. CG&r. glu'%(d*7.94))
cmd.select('his59', 'n. CE1&r. his w. %s of n. CD&r. glu'%(d*6.79))
cmd.select('his60', 'n. CE1&r. his w. %s of n. OE1&r. glu'%(d*7.18))
cmd.select('his61', 'n. CE1&r. his w. %s of n. OE2&r. glu'%(d*5.75))
cmd.select('his62', 'n. NE2&r. his w. %s of n. CB&r. glu'%(d*7.84))
cmd.select('his63', 'n. NE2&r. his w. %s of n. CG&r. glu'%(d*6.74))
cmd.select('his64', 'n. NE2&r. his w. %s of n. CD&r. glu'%(d*5.61))
cmd.select('his65', 'n. NE2&r. his w. %s of n. OE1&r. glu'%(d*6.02))
cmd.select('his66', 'n. NE2&r. his w. %s of n. OE2&r. glu'%(d*4.71))
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
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&cys'%(d*15.06))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. SG&cys'%(d*14.99))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&cys'%(d*14.20))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. SG&cys'%(d*14.00))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&cys'%(d*12.94))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. SG&cys'%(d*12.85))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&cys'%(d*12.87))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. SG&cys'%(d*12.99))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&cys'%(d*12.15))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. SG&cys'%(d*11.95))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&asn'%(d*19.19))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. CG&asn'%(d*18.34))
cmd.select('glu13', 'n. CB&r. glu w. %s of n. OD1&asn'%(d*18.93))
cmd.select('glu14', 'n. CB&r. glu w. %s of n. ND2&asn'%(d*17.03))
cmd.select('glu15', 'n. CG&r. glu w. %s of n. CB&asn'%(d*18.11))
cmd.select('glu16', 'n. CG&r. glu w. %s of n. CG&asn'%(d*17.20))
cmd.select('glu17', 'n. CG&r. glu w. %s of n. OD1&asn'%(d*17.75))
cmd.select('glu18', 'n. CG&r. glu w. %s of n. ND2&asn'%(d*15.89))
cmd.select('glu19', 'n. CD&r. glu w. %s of n. CB&asn'%(d*16.85))
cmd.select('glu20', 'n. CD&r. glu w. %s of n. CG&asn'%(d*15.92))
cmd.select('glu21', 'n. CD&r. glu w. %s of n. OD1&asn'%(d*16.47))
cmd.select('glu22', 'n. CD&r. glu w. %s of n. ND2&asn'%(d*14.63))
cmd.select('glu23', 'n. OE1&r. glu w. %s of n. CB&asn'%(d*16.92))
cmd.select('glu24', 'n. OE1&r. glu w. %s of n. CG&asn'%(d*16.04))
cmd.select('glu25', 'n. OE1&r. glu w. %s of n. OD1&asn'%(d*16.59))
cmd.select('glu26', 'n. OE1&r. glu w. %s of n. ND2&asn'%(d*14.75))
cmd.select('glu27', 'n. OE2&r. glu w. %s of n. CB&asn'%(d*15.87))
cmd.select('glu28', 'n. OE2&r. glu w. %s of n. CG&asn'%(d*14.90))
cmd.select('glu29', 'n. OE2&r. glu w. %s of n. OD1&asn'%(d*15.41))
cmd.select('glu30', 'n. OE2&r. glu w. %s of n. ND2&asn'%(d*13.60))
cmd.select('glu31', 'n. CB&r. glu w. %s of n. CB&his'%(d*10.38))
cmd.select('glu32', 'n. CB&r. glu w. %s of n. CG&his'%(d*9.38))
cmd.select('glu33', 'n. CB&r. glu w. %s of n. ND1&his'%(d*9.98))
cmd.select('glu34', 'n. CB&r. glu w. %s of n. CD2&his'%(d*8.03))
cmd.select('glu35', 'n. CB&r. glu w. %s of n. CE1&his'%(d*9.13))
cmd.select('glu36', 'n. CB&r. glu w. %s of n. NE2&his'%(d*7.84))
cmd.select('glu37', 'n. CG&r. glu w. %s of n. CB&his'%(d*9.63))
cmd.select('glu38', 'n. CG&r. glu w. %s of n. CG&his'%(d*8.48))
cmd.select('glu39', 'n. CG&r. glu w. %s of n. ND1&his'%(d*8.90))
cmd.select('glu40', 'n. CG&r. glu w. %s of n. CD2&his'%(d*7.15))
cmd.select('glu41', 'n. CG&r. glu w. %s of n. CE1&his'%(d*7.94))
cmd.select('glu42', 'n. CG&r. glu w. %s of n. NE2&his'%(d*6.74))
cmd.select('glu43', 'n. CD&r. glu w. %s of n. CB&his'%(d*8.76))
cmd.select('glu44', 'n. CD&r. glu w. %s of n. CG&his'%(d*7.51))
cmd.select('glu45', 'n. CD&r. glu w. %s of n. ND1&his'%(d*7.81))
cmd.select('glu46', 'n. CD&r. glu w. %s of n. CD2&his'%(d*6.20))
cmd.select('glu47', 'n. CD&r. glu w. %s of n. CE1&his'%(d*6.79))
cmd.select('glu48', 'n. CD&r. glu w. %s of n. NE2&his'%(d*5.61))
cmd.select('glu49', 'n. OE1&r. glu w. %s of n. CB&his'%(d*8.97))
cmd.select('glu50', 'n. OE1&r. glu w. %s of n. CG&his'%(d*7.79))
cmd.select('glu50',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36&br. glu37&br. glu38&br. glu39&br. glu40&br. glu41&br. glu42&br. glu43&br. glu44&br. glu45&br. glu46&br. glu47&br. glu48&br. glu49&br. glu50')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
cmd.delete('glu37')
cmd.delete('glu38')
cmd.delete('glu39')
cmd.delete('glu40')
cmd.delete('glu41')
cmd.delete('glu42')
cmd.delete('glu43')
cmd.delete('glu44')
cmd.delete('glu45')
cmd.delete('glu46')
cmd.delete('glu47')
cmd.delete('glu48')
cmd.delete('glu49')
cmd.select('glu51', 'n. OE1&r. glu w. %s of n. ND1&his'%(d*8.14))
cmd.select('glu52', 'n. OE1&r. glu w. %s of n. CD2&his'%(d*6.51))
cmd.select('glu53', 'n. OE1&r. glu w. %s of n. CE1&his'%(d*7.18))
cmd.select('glu54', 'n. OE1&r. glu w. %s of n. NE2&his'%(d*6.02))
cmd.select('glu55', 'n. OE2&r. glu w. %s of n. CB&his'%(d*8.15))
cmd.select('glu56', 'n. OE2&r. glu w. %s of n. CG&his'%(d*6.78))
cmd.select('glu57', 'n. OE2&r. glu w. %s of n. ND1&his'%(d*6.87))
cmd.select('glu58', 'n. OE2&r. glu w. %s of n. CD2&his'%(d*5.59))
cmd.select('glu59', 'n. OE2&r. glu w. %s of n. CE1&his'%(d*5.75))
cmd.select('glu60', 'n. OE2&r. glu w. %s of n. NE2&his'%(d*4.71))
cmd.select('glu',' glu50&br. glu51&br. glu52&br. glu53&br. glu54&br. glu55&br. glu56&br. glu57&br. glu58&br. glu59&br. glu60')
cmd.delete('glu50')
cmd.delete('glu51')
cmd.delete('glu52')
cmd.delete('glu53')
cmd.delete('glu54')
cmd.delete('glu55')
cmd.delete('glu56')
cmd.delete('glu57')
cmd.delete('glu58')
cmd.delete('glu59')
cmd.delete('glu60')
cmd.select('A_1eh6_2_1_1_63', 'cys|asn|his|glu')
cmd.delete('cys')
cmd.delete('asn')
cmd.delete('his')
cmd.delete('glu')
