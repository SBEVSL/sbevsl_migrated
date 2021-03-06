'''
FUNC:A_1afw_2_3_1_16
PDB:1afw
EC:2.3.1.16
RESI:cys,his,cys,gly
LOCI:a-125,375,403,405;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. O&r. gly'%(d*8.72))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. C&r. gly'%(d*8.86))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CA&r. gly'%(d*7.89))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. N&r. gly'%(d*6.65))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. O&r. gly'%(d*7.71))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. C&r. gly'%(d*7.62))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. CA&r. gly'%(d*6.46))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. N&r. gly'%(d*5.46))
cmd.select('cys9', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*8.53))
cmd.select('cys10', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*8.06))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*8.43))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*7.82))
cmd.select('cys13', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*9.54))
cmd.select('cys14', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*8.05))
cmd.select('cys15', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*7.36))
cmd.select('cys16', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*7.33))
cmd.select('cys17', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*6.04))
cmd.select('cys18', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*5.98))
cmd.select('cys19', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*9.80))
cmd.select('cys20', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*8.35))
cmd.select('cys21', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*8.03))
cmd.select('cys22', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*7.32))
cmd.select('cys23', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*6.74))
cmd.select('cys24', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*6.16))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24')
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
cmd.select('gly1', 'n. O&r. gly w. %s of n. CB&cys'%(d*8.72))
cmd.select('gly2', 'n. O&r. gly w. %s of n. SG&cys'%(d*7.71))
cmd.select('gly3', 'n. C&r. gly w. %s of n. CB&cys'%(d*8.86))
cmd.select('gly4', 'n. C&r. gly w. %s of n. SG&cys'%(d*7.62))
cmd.select('gly5', 'n. CA&r. gly w. %s of n. CB&cys'%(d*7.89))
cmd.select('gly6', 'n. CA&r. gly w. %s of n. SG&cys'%(d*6.46))
cmd.select('gly7', 'n. N&r. gly w. %s of n. CB&cys'%(d*6.65))
cmd.select('gly8', 'n. N&r. gly w. %s of n. SG&cys'%(d*5.46))
cmd.select('gly9', 'n. O&r. gly w. %s of n. CB&r. cys'%(d*10.23))
cmd.select('gly10', 'n. O&r. gly w. %s of n. SG&r. cys'%(d*10.70))
cmd.select('gly11', 'n. C&r. gly w. %s of n. CB&r. cys'%(d*9.77))
cmd.select('gly12', 'n. C&r. gly w. %s of n. SG&r. cys'%(d*10.14))
cmd.select('gly13', 'n. CA&r. gly w. %s of n. CB&r. cys'%(d*8.85))
cmd.select('gly14', 'n. CA&r. gly w. %s of n. SG&r. cys'%(d*8.95))
cmd.select('gly15', 'n. N&r. gly w. %s of n. CB&r. cys'%(d*7.88))
cmd.select('gly16', 'n. N&r. gly w. %s of n. SG&r. cys'%(d*8.03))
cmd.select('gly17', 'n. O&r. gly w. %s of n. CB&r. his'%(d*15.45))
cmd.select('gly18', 'n. O&r. gly w. %s of n. CG&r. his'%(d*14.02))
cmd.select('gly19', 'n. O&r. gly w. %s of n. ND1&r. his'%(d*13.72))
cmd.select('gly20', 'n. O&r. gly w. %s of n. CD2&r. his'%(d*12.92))
cmd.select('gly21', 'n. O&r. gly w. %s of n. CE1&r. his'%(d*12.42))
cmd.select('gly22', 'n. O&r. gly w. %s of n. NE2&r. his'%(d*11.85))
cmd.select('gly23', 'n. C&r. gly w. %s of n. CB&r. his'%(d*15.18))
cmd.select('gly24', 'n. C&r. gly w. %s of n. CG&r. his'%(d*13.80))
cmd.select('gly25', 'n. C&r. gly w. %s of n. ND1&r. his'%(d*13.63))
cmd.select('gly26', 'n. C&r. gly w. %s of n. CD2&r. his'%(d*12.62))
cmd.select('gly27', 'n. C&r. gly w. %s of n. CE1&r. his'%(d*12.36))
cmd.select('gly28', 'n. C&r. gly w. %s of n. NE2&r. his'%(d*11.65))
cmd.select('gly29', 'n. CA&r. gly w. %s of n. CB&r. his'%(d*13.81))
cmd.select('gly30', 'n. CA&r. gly w. %s of n. CG&r. his'%(d*12.45))
cmd.select('gly31', 'n. CA&r. gly w. %s of n. ND1&r. his'%(d*12.37))
cmd.select('gly32', 'n. CA&r. gly w. %s of n. CD2&r. his'%(d*11.24))
cmd.select('gly33', 'n. CA&r. gly w. %s of n. CE1&r. his'%(d*11.13))
cmd.select('gly34', 'n. CA&r. gly w. %s of n. NE2&r. his'%(d*10.33))
cmd.select('gly35', 'n. N&r. gly w. %s of n. CB&r. his'%(d*13.02))
cmd.select('gly36', 'n. N&r. gly w. %s of n. CG&r. his'%(d*11.62))
cmd.select('gly37', 'n. N&r. gly w. %s of n. ND1&r. his'%(d*11.40))
cmd.select('gly38', 'n. N&r. gly w. %s of n. CD2&r. his'%(d*10.47))
cmd.select('gly39', 'n. N&r. gly w. %s of n. CE1&r. his'%(d*10.12))
cmd.select('gly40', 'n. N&r. gly w. %s of n. NE2&r. his'%(d*9.45))
cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27&br. gly28&br. gly29&br. gly30&br. gly31&br. gly32&br. gly33&br. gly34&br. gly35&br. gly36&br. gly37&br. gly38&br. gly39&br. gly40')
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
cmd.delete('gly28')
cmd.delete('gly29')
cmd.delete('gly30')
cmd.delete('gly31')
cmd.delete('gly32')
cmd.delete('gly33')
cmd.delete('gly34')
cmd.delete('gly35')
cmd.delete('gly36')
cmd.delete('gly37')
cmd.delete('gly38')
cmd.delete('gly39')
cmd.delete('gly40')
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. CB&cys'%(d*8.53))
cmd.select('cysi2', 'n. CB&r. cys w. %s of n. SG&cys'%(d*8.43))
cmd.select('cysi3', 'n. SG&r. cys w. %s of n. CB&cys'%(d*8.06))
cmd.select('cysi4', 'n. SG&r. cys w. %s of n. SG&cys'%(d*7.82))
cmd.select('cysi5', 'n. CB&r. cys w. %s of n. O&gly'%(d*10.23))
cmd.select('cysi6', 'n. CB&r. cys w. %s of n. C&gly'%(d*9.77))
cmd.select('cysi7', 'n. CB&r. cys w. %s of n. CA&gly'%(d*8.85))
cmd.select('cysi8', 'n. CB&r. cys w. %s of n. N&gly'%(d*7.88))
cmd.select('cysi9', 'n. SG&r. cys w. %s of n. O&gly'%(d*10.70))
cmd.select('cysi10', 'n. SG&r. cys w. %s of n. C&gly'%(d*10.14))
cmd.select('cysi11', 'n. SG&r. cys w. %s of n. CA&gly'%(d*8.95))
cmd.select('cysi12', 'n. SG&r. cys w. %s of n. N&gly'%(d*8.03))
cmd.select('cysi13', 'n. CB&r. cys w. %s of n. CB&r. his'%(d*12.79))
cmd.select('cysi14', 'n. CB&r. cys w. %s of n. CG&r. his'%(d*11.65))
cmd.select('cysi15', 'n. CB&r. cys w. %s of n. ND1&r. his'%(d*11.51))
cmd.select('cysi16', 'n. CB&r. cys w. %s of n. CD2&r. his'%(d*10.76))
cmd.select('cysi17', 'n. CB&r. cys w. %s of n. CE1&r. his'%(d*10.55))
cmd.select('cysi18', 'n. CB&r. cys w. %s of n. NE2&r. his'%(d*10.03))
cmd.select('cysi19', 'n. SG&r. cys w. %s of n. CB&r. his'%(d*11.21))
cmd.select('cysi20', 'n. SG&r. cys w. %s of n. CG&r. his'%(d*10.15))
cmd.select('cysi21', 'n. SG&r. cys w. %s of n. ND1&r. his'%(d*10.19))
cmd.select('cysi22', 'n. SG&r. cys w. %s of n. CD2&r. his'%(d*9.24))
cmd.select('cysi23', 'n. SG&r. cys w. %s of n. CE1&r. his'%(d*9.34))
cmd.select('cysi24', 'n. SG&r. cys w. %s of n. NE2&r. his'%(d*8.69))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12&br. cysi13&br. cysi14&br. cysi15&br. cysi16&br. cysi17&br. cysi18&br. cysi19&br. cysi20&br. cysi21&br. cysi22&br. cysi23&br. cysi24')
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
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&cys'%(d*9.54))
cmd.select('his2', 'n. CB&r. his w. %s of n. SG&cys'%(d*9.80))
cmd.select('his3', 'n. CG&r. his w. %s of n. CB&cys'%(d*8.05))
cmd.select('his4', 'n. CG&r. his w. %s of n. SG&cys'%(d*8.35))
cmd.select('his5', 'n. ND1&r. his w. %s of n. CB&cys'%(d*7.36))
cmd.select('his6', 'n. ND1&r. his w. %s of n. SG&cys'%(d*8.03))
cmd.select('his7', 'n. CD2&r. his w. %s of n. CB&cys'%(d*7.33))
cmd.select('his8', 'n. CD2&r. his w. %s of n. SG&cys'%(d*7.32))
cmd.select('his9', 'n. CE1&r. his w. %s of n. CB&cys'%(d*6.04))
cmd.select('his10', 'n. CE1&r. his w. %s of n. SG&cys'%(d*6.74))
cmd.select('his11', 'n. NE2&r. his w. %s of n. CB&cys'%(d*5.98))
cmd.select('his12', 'n. NE2&r. his w. %s of n. SG&cys'%(d*6.16))
cmd.select('his13', 'n. CB&r. his w. %s of n. O&gly'%(d*15.45))
cmd.select('his14', 'n. CB&r. his w. %s of n. C&gly'%(d*15.18))
cmd.select('his15', 'n. CB&r. his w. %s of n. CA&gly'%(d*13.81))
cmd.select('his16', 'n. CB&r. his w. %s of n. N&gly'%(d*13.02))
cmd.select('his17', 'n. CG&r. his w. %s of n. O&gly'%(d*14.02))
cmd.select('his18', 'n. CG&r. his w. %s of n. C&gly'%(d*13.80))
cmd.select('his19', 'n. CG&r. his w. %s of n. CA&gly'%(d*12.45))
cmd.select('his20', 'n. CG&r. his w. %s of n. N&gly'%(d*11.62))
cmd.select('his21', 'n. ND1&r. his w. %s of n. O&gly'%(d*13.72))
cmd.select('his22', 'n. ND1&r. his w. %s of n. C&gly'%(d*13.63))
cmd.select('his23', 'n. ND1&r. his w. %s of n. CA&gly'%(d*12.37))
cmd.select('his24', 'n. ND1&r. his w. %s of n. N&gly'%(d*11.40))
cmd.select('his25', 'n. CD2&r. his w. %s of n. O&gly'%(d*12.92))
cmd.select('his26', 'n. CD2&r. his w. %s of n. C&gly'%(d*12.62))
cmd.select('his27', 'n. CD2&r. his w. %s of n. CA&gly'%(d*11.24))
cmd.select('his28', 'n. CD2&r. his w. %s of n. N&gly'%(d*10.47))
cmd.select('his29', 'n. CE1&r. his w. %s of n. O&gly'%(d*12.42))
cmd.select('his30', 'n. CE1&r. his w. %s of n. C&gly'%(d*12.36))
cmd.select('his31', 'n. CE1&r. his w. %s of n. CA&gly'%(d*11.13))
cmd.select('his32', 'n. CE1&r. his w. %s of n. N&gly'%(d*10.12))
cmd.select('his33', 'n. NE2&r. his w. %s of n. O&gly'%(d*11.85))
cmd.select('his34', 'n. NE2&r. his w. %s of n. C&gly'%(d*11.65))
cmd.select('his35', 'n. NE2&r. his w. %s of n. CA&gly'%(d*10.33))
cmd.select('his36', 'n. NE2&r. his w. %s of n. N&gly'%(d*9.45))
cmd.select('his37', 'n. CB&r. his w. %s of n. CB&cysi'%(d*12.79))
cmd.select('his38', 'n. CB&r. his w. %s of n. SG&cysi'%(d*11.21))
cmd.select('his39', 'n. CG&r. his w. %s of n. CB&cysi'%(d*11.65))
cmd.select('his40', 'n. CG&r. his w. %s of n. SG&cysi'%(d*10.15))
cmd.select('his41', 'n. ND1&r. his w. %s of n. CB&cysi'%(d*11.51))
cmd.select('his42', 'n. ND1&r. his w. %s of n. SG&cysi'%(d*10.19))
cmd.select('his43', 'n. CD2&r. his w. %s of n. CB&cysi'%(d*10.76))
cmd.select('his44', 'n. CD2&r. his w. %s of n. SG&cysi'%(d*9.24))
cmd.select('his45', 'n. CE1&r. his w. %s of n. CB&cysi'%(d*10.55))
cmd.select('his46', 'n. CE1&r. his w. %s of n. SG&cysi'%(d*9.34))
cmd.select('his47', 'n. NE2&r. his w. %s of n. CB&cysi'%(d*10.03))
cmd.select('his48', 'n. NE2&r. his w. %s of n. SG&cysi'%(d*8.69))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36&br. his37&br. his38&br. his39&br. his40&br. his41&br. his42&br. his43&br. his44&br. his45&br. his46&br. his47&br. his48')
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
cmd.select('A_1afw_2_3_1_16', 'cys|gly|cysi|his')
cmd.delete('cys')
cmd.delete('gly')
cmd.delete('cysi')
cmd.delete('his')
