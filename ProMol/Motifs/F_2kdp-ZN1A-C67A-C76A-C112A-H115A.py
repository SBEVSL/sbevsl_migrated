'''
FUNC:F_2kdp-ZN1A-C67A-C76A-C112A-H115A
PDB:2kdp
EC:N/A
PFAM:PF13866
RESI:zn,cys,cys,cys,his
LOCI:a-1,67,76,112,115;
'''
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.30))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.29))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.84))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.30))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.22))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.30))
cmd.select('zn7', 'n. ZN&r. zn w. %s of n. CB&r. his'%(d*5.73))
cmd.select('zn8', 'n. ZN&r. zn w. %s of n. CG&r. his'%(d*5.02))
cmd.select('zn9', 'n. ZN&r. zn w. %s of n. ND1&r. his'%(d*3.98))
cmd.select('zn10', 'n. ZN&r. zn w. %s of n. CD2&r. his'%(d*5.84))
cmd.select('zn11', 'n. ZN&r. zn w. %s of n. CE1&r. his'%(d*4.51))
cmd.select('zn12', 'n. ZN&r. zn w. %s of n. NE2&r. his'%(d*5.60))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6&br. zn7&br. zn8&br. zn9&br. zn10&br. zn11&br. zn12')
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
cmd.select('cys1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.30))
cmd.select('cys2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.29))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*7.73))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*6.77))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*6.61))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.38))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*5.44))
cmd.select('cys8', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*5.68))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*5.78))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.75))
cmd.select('cys11', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*8.90))
cmd.select('cys12', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*7.85))
cmd.select('cys13', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*6.67))
cmd.select('cys14', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*8.14))
cmd.select('cys15', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*6.22))
cmd.select('cys16', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*7.22))
cmd.select('cys17', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*7.62))
cmd.select('cys18', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*6.64))
cmd.select('cys19', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*5.72))
cmd.select('cys20', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*6.92))
cmd.select('cys21', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*5.43))
cmd.select('cys22', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*6.23))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22')
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
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.84))
cmd.select('cysi2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.30))
cmd.select('cysi3', 'n. CB&r. cys w. %s of n. CB&cys'%(d*7.73))
cmd.select('cysi4', 'n. CB&r. cys w. %s of n. SG&cys'%(d*6.61))
cmd.select('cysi5', 'n. SG&r. cys w. %s of n. CB&cys'%(d*6.77))
cmd.select('cysi6', 'n. SG&r. cys w. %s of n. SG&cys'%(d*5.38))
cmd.select('cysi7', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*6.10))
cmd.select('cysi8', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*6.49))
cmd.select('cysi9', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*5.92))
cmd.select('cysi10', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.72))
cmd.select('cysi11', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*7.37))
cmd.select('cysi12', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*7.64))
cmd.select('cysi13', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*7.31))
cmd.select('cysi14', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*8.63))
cmd.select('cysi15', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*8.15))
cmd.select('cysi16', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*8.90))
cmd.select('cysi17', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*5.93))
cmd.select('cysi18', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*5.94))
cmd.select('cysi19', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*5.61))
cmd.select('cysi20', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*6.85))
cmd.select('cysi21', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*6.41))
cmd.select('cysi22', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*7.10))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12&br. cysi13&br. cysi14&br. cysi15&br. cysi16&br. cysi17&br. cysi18&br. cysi19&br. cysi20&br. cysi21&br. cysi22')
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
cmd.select('cysii1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.22))
cmd.select('cysii2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.30))
cmd.select('cysii3', 'n. CB&r. cys w. %s of n. CB&cys'%(d*5.44))
cmd.select('cysii4', 'n. CB&r. cys w. %s of n. SG&cys'%(d*5.78))
cmd.select('cysii5', 'n. SG&r. cys w. %s of n. CB&cys'%(d*5.68))
cmd.select('cysii6', 'n. SG&r. cys w. %s of n. SG&cys'%(d*5.75))
cmd.select('cysii7', 'n. CB&r. cys w. %s of n. CB&cysi'%(d*6.10))
cmd.select('cysii8', 'n. CB&r. cys w. %s of n. SG&cysi'%(d*5.92))
cmd.select('cysii9', 'n. SG&r. cys w. %s of n. CB&cysi'%(d*6.49))
cmd.select('cysii10', 'n. SG&r. cys w. %s of n. SG&cysi'%(d*5.72))
cmd.select('cysii11', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*8.46))
cmd.select('cysii12', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*8.07))
cmd.select('cysii13', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*6.92))
cmd.select('cysii14', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*9.01))
cmd.select('cysii15', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*7.37))
cmd.select('cysii16', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*8.63))
cmd.select('cysii17', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*7.10))
cmd.select('cysii18', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*6.67))
cmd.select('cysii19', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*5.46))
cmd.select('cysii20', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*7.67))
cmd.select('cysii21', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*6.04))
cmd.select('cysii22', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*7.35))
cmd.select('cysii',' br. cysii1&br. cysii2&br. cysii3&br. cysii4&br. cysii5&br. cysii6&br. cysii7&br. cysii8&br. cysii9&br. cysii10&br. cysii11&br. cysii12&br. cysii13&br. cysii14&br. cysii15&br. cysii16&br. cysii17&br. cysii18&br. cysii19&br. cysii20&br. cysii21&br. cysii22')
cmd.delete('cysii1')
cmd.delete('cysii2')
cmd.delete('cysii3')
cmd.delete('cysii4')
cmd.delete('cysii5')
cmd.delete('cysii6')
cmd.delete('cysii7')
cmd.delete('cysii8')
cmd.delete('cysii9')
cmd.delete('cysii10')
cmd.delete('cysii11')
cmd.delete('cysii12')
cmd.delete('cysii13')
cmd.delete('cysii14')
cmd.delete('cysii15')
cmd.delete('cysii16')
cmd.delete('cysii17')
cmd.delete('cysii18')
cmd.delete('cysii19')
cmd.delete('cysii20')
cmd.delete('cysii21')
cmd.delete('cysii22')
cmd.select('his1', 'n. CB&r. his w. %s of n. ZN&zn'%(d*5.73))
cmd.select('his2', 'n. CG&r. his w. %s of n. ZN&zn'%(d*5.02))
cmd.select('his3', 'n. ND1&r. his w. %s of n. ZN&zn'%(d*3.98))
cmd.select('his4', 'n. CD2&r. his w. %s of n. ZN&zn'%(d*5.84))
cmd.select('his5', 'n. CE1&r. his w. %s of n. ZN&zn'%(d*4.51))
cmd.select('his6', 'n. NE2&r. his w. %s of n. ZN&zn'%(d*5.60))
cmd.select('his7', 'n. CB&r. his w. %s of n. CB&cys'%(d*8.90))
cmd.select('his8', 'n. CB&r. his w. %s of n. SG&cys'%(d*7.62))
cmd.select('his9', 'n. CG&r. his w. %s of n. CB&cys'%(d*7.85))
cmd.select('his10', 'n. CG&r. his w. %s of n. SG&cys'%(d*6.64))
cmd.select('his11', 'n. ND1&r. his w. %s of n. CB&cys'%(d*6.67))
cmd.select('his12', 'n. ND1&r. his w. %s of n. SG&cys'%(d*5.72))
cmd.select('his13', 'n. CD2&r. his w. %s of n. CB&cys'%(d*8.14))
cmd.select('his14', 'n. CD2&r. his w. %s of n. SG&cys'%(d*6.92))
cmd.select('his15', 'n. CE1&r. his w. %s of n. CB&cys'%(d*6.22))
cmd.select('his16', 'n. CE1&r. his w. %s of n. SG&cys'%(d*5.43))
cmd.select('his17', 'n. NE2&r. his w. %s of n. CB&cys'%(d*7.22))
cmd.select('his18', 'n. NE2&r. his w. %s of n. SG&cys'%(d*6.23))
cmd.select('his19', 'n. CB&r. his w. %s of n. CB&cysi'%(d*7.37))
cmd.select('his20', 'n. CB&r. his w. %s of n. SG&cysi'%(d*5.93))
cmd.select('his21', 'n. CG&r. his w. %s of n. CB&cysi'%(d*7.64))
cmd.select('his22', 'n. CG&r. his w. %s of n. SG&cysi'%(d*5.94))
cmd.select('his23', 'n. ND1&r. his w. %s of n. CB&cysi'%(d*7.31))
cmd.select('his24', 'n. ND1&r. his w. %s of n. SG&cysi'%(d*5.61))
cmd.select('his25', 'n. CD2&r. his w. %s of n. CB&cysi'%(d*8.63))
cmd.select('his26', 'n. CD2&r. his w. %s of n. SG&cysi'%(d*6.85))
cmd.select('his27', 'n. CE1&r. his w. %s of n. CB&cysi'%(d*8.15))
cmd.select('his28', 'n. CE1&r. his w. %s of n. SG&cysi'%(d*6.41))
cmd.select('his29', 'n. NE2&r. his w. %s of n. CB&cysi'%(d*8.90))
cmd.select('his30', 'n. NE2&r. his w. %s of n. SG&cysi'%(d*7.10))
cmd.select('his31', 'n. CB&r. his w. %s of n. CB&cysii'%(d*8.46))
cmd.select('his32', 'n. CB&r. his w. %s of n. SG&cysii'%(d*7.10))
cmd.select('his33', 'n. CG&r. his w. %s of n. CB&cysii'%(d*8.07))
cmd.select('his34', 'n. CG&r. his w. %s of n. SG&cysii'%(d*6.67))
cmd.select('his35', 'n. ND1&r. his w. %s of n. CB&cysii'%(d*6.92))
cmd.select('his36', 'n. ND1&r. his w. %s of n. SG&cysii'%(d*5.46))
cmd.select('his37', 'n. CD2&r. his w. %s of n. CB&cysii'%(d*9.01))
cmd.select('his38', 'n. CD2&r. his w. %s of n. SG&cysii'%(d*7.67))
cmd.select('his39', 'n. CE1&r. his w. %s of n. CB&cysii'%(d*7.37))
cmd.select('his40', 'n. CE1&r. his w. %s of n. SG&cysii'%(d*6.04))
cmd.select('his41', 'n. NE2&r. his w. %s of n. CB&cysii'%(d*8.63))
cmd.select('his42', 'n. NE2&r. his w. %s of n. SG&cysii'%(d*7.35))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36&br. his37&br. his38&br. his39&br. his40&br. his41&br. his42')
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
cmd.select('F_2kdp-ZN1A-C67A-C76A-C112A-H115A', 'zn|cys|cysi|cysii|his')
cmd.delete('zn')
cmd.delete('cys')
cmd.delete('cysi')
cmd.delete('cysii')
cmd.delete('his')
