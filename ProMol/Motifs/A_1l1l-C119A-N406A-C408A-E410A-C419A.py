'''
FUNC:A_1l1l-C119A-N406A-C408A-E410A-C419A
PDB:1l1l
EC:1.17.4.2
PFAM:PF02867
RESI:cys,asn,cys,glu,cys
LOCI:a-119,406,408,410,419;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. asn'%(d*5.67))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&r. asn'%(d*6.39))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. OD1&r. asn'%(d*7.48))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. ND2&r. asn'%(d*6.21))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. CB&r. asn'%(d*6.44))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. CG&r. asn'%(d*6.58))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. OD1&r. asn'%(d*7.56))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. ND2&r. asn'%(d*6.04))
cmd.select('cys9', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*5.85))
cmd.select('cys10', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*5.03))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*5.05))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*4.03))
cmd.select('cys13', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*9.17))
cmd.select('cys14', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*9.31))
cmd.select('cys15', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*8.80))
cmd.select('cys16', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*8.95))
cmd.select('cys17', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*11.01))
cmd.select('cys18', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*9.91))
cmd.select('cys19', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*8.86))
cmd.select('cys20', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*8.67))
cmd.select('cys21', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*8.49))
cmd.select('cys22', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*10.17))
cmd.select('cys23', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*8.91))
cmd.select('cys24', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*7.83))
cmd.select('cys25', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*7.91))
cmd.select('cys26', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*7.21))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26')
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
cmd.select('asn1', 'n. CB&r. asn w. %s of n. CB&cys'%(d*5.67))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. SG&cys'%(d*6.44))
cmd.select('asn3', 'n. CG&r. asn w. %s of n. CB&cys'%(d*6.39))
cmd.select('asn4', 'n. CG&r. asn w. %s of n. SG&cys'%(d*6.58))
cmd.select('asn5', 'n. OD1&r. asn w. %s of n. CB&cys'%(d*7.48))
cmd.select('asn6', 'n. OD1&r. asn w. %s of n. SG&cys'%(d*7.56))
cmd.select('asn7', 'n. ND2&r. asn w. %s of n. CB&cys'%(d*6.21))
cmd.select('asn8', 'n. ND2&r. asn w. %s of n. SG&cys'%(d*6.04))
cmd.select('asn9', 'n. CB&r. asn w. %s of n. CB&r. cys'%(d*7.03))
cmd.select('asn10', 'n. CB&r. asn w. %s of n. SG&r. cys'%(d*7.53))
cmd.select('asn11', 'n. CG&r. asn w. %s of n. CB&r. cys'%(d*6.98))
cmd.select('asn12', 'n. CG&r. asn w. %s of n. SG&r. cys'%(d*7.70))
cmd.select('asn13', 'n. OD1&r. asn w. %s of n. CB&r. cys'%(d*7.40))
cmd.select('asn14', 'n. OD1&r. asn w. %s of n. SG&r. cys'%(d*8.42))
cmd.select('asn15', 'n. ND2&r. asn w. %s of n. CB&r. cys'%(d*7.01))
cmd.select('asn16', 'n. ND2&r. asn w. %s of n. SG&r. cys'%(d*7.45))
cmd.select('asn17', 'n. CB&r. asn w. %s of n. CB&r. cys'%(d*7.81))
cmd.select('asn18', 'n. CB&r. asn w. %s of n. SG&r. cys'%(d*8.72))
cmd.select('asn19', 'n. CG&r. asn w. %s of n. CB&r. cys'%(d*6.87))
cmd.select('asn20', 'n. CG&r. asn w. %s of n. SG&r. cys'%(d*8.04))
cmd.select('asn21', 'n. OD1&r. asn w. %s of n. CB&r. cys'%(d*7.34))
cmd.select('asn22', 'n. OD1&r. asn w. %s of n. SG&r. cys'%(d*8.75))
cmd.select('asn23', 'n. ND2&r. asn w. %s of n. CB&r. cys'%(d*5.86))
cmd.select('asn24', 'n. ND2&r. asn w. %s of n. SG&r. cys'%(d*6.93))
cmd.select('asn25', 'n. CB&r. asn w. %s of n. CB&r. glu'%(d*8.99))
cmd.select('asn26', 'n. CB&r. asn w. %s of n. CG&r. glu'%(d*8.36))
cmd.select('asn27', 'n. CB&r. asn w. %s of n. CD&r. glu'%(d*7.62))
cmd.select('asn28', 'n. CB&r. asn w. %s of n. OE1&r. glu'%(d*7.04))
cmd.select('asn29', 'n. CB&r. asn w. %s of n. OE2&r. glu'%(d*7.97))
cmd.select('asn30', 'n. CG&r. asn w. %s of n. CB&r. glu'%(d*7.49))
cmd.select('asn31', 'n. CG&r. asn w. %s of n. CG&r. glu'%(d*6.89))
cmd.select('asn32', 'n. CG&r. asn w. %s of n. CD&r. glu'%(d*6.19))
cmd.select('asn33', 'n. CG&r. asn w. %s of n. OE1&r. glu'%(d*5.60))
cmd.select('asn34', 'n. CG&r. asn w. %s of n. OE2&r. glu'%(d*6.69))
cmd.select('asn35', 'n. OD1&r. asn w. %s of n. CB&r. glu'%(d*6.85))
cmd.select('asn36', 'n. OD1&r. asn w. %s of n. CG&r. glu'%(d*6.43))
cmd.select('asn37', 'n. OD1&r. asn w. %s of n. CD&r. glu'%(d*6.10))
cmd.select('asn38', 'n. OD1&r. asn w. %s of n. OE1&r. glu'%(d*5.60))
cmd.select('asn39', 'n. OD1&r. asn w. %s of n. OE2&r. glu'%(d*6.83))
cmd.select('asn40', 'n. ND2&r. asn w. %s of n. CB&r. glu'%(d*7.17))
cmd.select('asn41', 'n. ND2&r. asn w. %s of n. CG&r. glu'%(d*6.47))
cmd.select('asn42', 'n. ND2&r. asn w. %s of n. CD&r. glu'%(d*5.42))
cmd.select('asn43', 'n. ND2&r. asn w. %s of n. OE1&r. glu'%(d*4.78))
cmd.select('asn44', 'n. ND2&r. asn w. %s of n. OE2&r. glu'%(d*5.75))
cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36&br. asn37&br. asn38&br. asn39&br. asn40&br. asn41&br. asn42&br. asn43&br. asn44')
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
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. CB&cys'%(d*5.85))
cmd.select('cysi2', 'n. CB&r. cys w. %s of n. SG&cys'%(d*5.05))
cmd.select('cysi3', 'n. SG&r. cys w. %s of n. CB&cys'%(d*5.03))
cmd.select('cysi4', 'n. SG&r. cys w. %s of n. SG&cys'%(d*4.03))
cmd.select('cysi5', 'n. CB&r. cys w. %s of n. CB&asn'%(d*7.03))
cmd.select('cysi6', 'n. CB&r. cys w. %s of n. CG&asn'%(d*6.98))
cmd.select('cysi7', 'n. CB&r. cys w. %s of n. OD1&asn'%(d*7.40))
cmd.select('cysi8', 'n. CB&r. cys w. %s of n. ND2&asn'%(d*7.01))
cmd.select('cysi9', 'n. SG&r. cys w. %s of n. CB&asn'%(d*7.53))
cmd.select('cysi10', 'n. SG&r. cys w. %s of n. CG&asn'%(d*7.70))
cmd.select('cysi11', 'n. SG&r. cys w. %s of n. OD1&asn'%(d*8.42))
cmd.select('cysi12', 'n. SG&r. cys w. %s of n. ND2&asn'%(d*7.45))
cmd.select('cysi13', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*10.47))
cmd.select('cysi14', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*11.13))
cmd.select('cysi15', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*10.56))
cmd.select('cysi16', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*10.86))
cmd.select('cysi17', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*9.82))
cmd.select('cysi18', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*8.46))
cmd.select('cysi19', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*8.00))
cmd.select('cysi20', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*8.46))
cmd.select('cysi21', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*7.51))
cmd.select('cysi22', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*10.89))
cmd.select('cysi23', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*9.51))
cmd.select('cysi24', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*8.74))
cmd.select('cysi25', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*9.10))
cmd.select('cysi26', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*8.05))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12&br. cysi13&br. cysi14&br. cysi15&br. cysi16&br. cysi17&br. cysi18&br. cysi19&br. cysi20&br. cysi21&br. cysi22&br. cysi23&br. cysi24&br. cysi25&br. cysi26')
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
cmd.select('cysii1', 'n. CB&r. cys w. %s of n. CB&cys'%(d*9.17))
cmd.select('cysii2', 'n. CB&r. cys w. %s of n. SG&cys'%(d*8.80))
cmd.select('cysii3', 'n. SG&r. cys w. %s of n. CB&cys'%(d*9.31))
cmd.select('cysii4', 'n. SG&r. cys w. %s of n. SG&cys'%(d*8.95))
cmd.select('cysii5', 'n. CB&r. cys w. %s of n. CB&asn'%(d*7.81))
cmd.select('cysii6', 'n. CB&r. cys w. %s of n. CG&asn'%(d*6.87))
cmd.select('cysii7', 'n. CB&r. cys w. %s of n. OD1&asn'%(d*7.34))
cmd.select('cysii8', 'n. CB&r. cys w. %s of n. ND2&asn'%(d*5.86))
cmd.select('cysii9', 'n. SG&r. cys w. %s of n. CB&asn'%(d*8.72))
cmd.select('cysii10', 'n. SG&r. cys w. %s of n. CG&asn'%(d*8.04))
cmd.select('cysii11', 'n. SG&r. cys w. %s of n. OD1&asn'%(d*8.75))
cmd.select('cysii12', 'n. SG&r. cys w. %s of n. ND2&asn'%(d*6.93))
cmd.select('cysii13', 'n. CB&r. cys w. %s of n. CB&cysi'%(d*10.47))
cmd.select('cysii14', 'n. CB&r. cys w. %s of n. SG&cysi'%(d*10.56))
cmd.select('cysii15', 'n. SG&r. cys w. %s of n. CB&cysi'%(d*11.13))
cmd.select('cysii16', 'n. SG&r. cys w. %s of n. SG&cysi'%(d*10.86))
cmd.select('cysii17', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*7.46))
cmd.select('cysii18', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*7.46))
cmd.select('cysii19', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*6.24))
cmd.select('cysii20', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*5.16))
cmd.select('cysii21', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*6.66))
cmd.select('cysii22', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*9.07))
cmd.select('cysii23', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*8.91))
cmd.select('cysii24', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*7.56))
cmd.select('cysii25', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*6.66))
cmd.select('cysii26', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*7.64))
cmd.select('cysii',' br. cysii1&br. cysii2&br. cysii3&br. cysii4&br. cysii5&br. cysii6&br. cysii7&br. cysii8&br. cysii9&br. cysii10&br. cysii11&br. cysii12&br. cysii13&br. cysii14&br. cysii15&br. cysii16&br. cysii17&br. cysii18&br. cysii19&br. cysii20&br. cysii21&br. cysii22&br. cysii23&br. cysii24&br. cysii25&br. cysii26')
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
cmd.delete('cysii23')
cmd.delete('cysii24')
cmd.delete('cysii25')
cmd.delete('cysii26')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&cys'%(d*11.01))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. SG&cys'%(d*10.17))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&cys'%(d*9.91))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. SG&cys'%(d*8.91))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&cys'%(d*8.86))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. SG&cys'%(d*7.83))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&cys'%(d*8.67))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. SG&cys'%(d*7.91))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&cys'%(d*8.49))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. SG&cys'%(d*7.21))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&asn'%(d*8.99))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. CG&asn'%(d*7.49))
cmd.select('glu13', 'n. CB&r. glu w. %s of n. OD1&asn'%(d*6.85))
cmd.select('glu14', 'n. CB&r. glu w. %s of n. ND2&asn'%(d*7.17))
cmd.select('glu15', 'n. CG&r. glu w. %s of n. CB&asn'%(d*8.36))
cmd.select('glu16', 'n. CG&r. glu w. %s of n. CG&asn'%(d*6.89))
cmd.select('glu17', 'n. CG&r. glu w. %s of n. OD1&asn'%(d*6.43))
cmd.select('glu18', 'n. CG&r. glu w. %s of n. ND2&asn'%(d*6.47))
cmd.select('glu19', 'n. CD&r. glu w. %s of n. CB&asn'%(d*7.62))
cmd.select('glu20', 'n. CD&r. glu w. %s of n. CG&asn'%(d*6.19))
cmd.select('glu21', 'n. CD&r. glu w. %s of n. OD1&asn'%(d*6.10))
cmd.select('glu22', 'n. CD&r. glu w. %s of n. ND2&asn'%(d*5.42))
cmd.select('glu23', 'n. OE1&r. glu w. %s of n. CB&asn'%(d*7.04))
cmd.select('glu24', 'n. OE1&r. glu w. %s of n. CG&asn'%(d*5.60))
cmd.select('glu25', 'n. OE1&r. glu w. %s of n. OD1&asn'%(d*5.60))
cmd.select('glu26', 'n. OE1&r. glu w. %s of n. ND2&asn'%(d*4.78))
cmd.select('glu27', 'n. OE2&r. glu w. %s of n. CB&asn'%(d*7.97))
cmd.select('glu28', 'n. OE2&r. glu w. %s of n. CG&asn'%(d*6.69))
cmd.select('glu29', 'n. OE2&r. glu w. %s of n. OD1&asn'%(d*6.83))
cmd.select('glu30', 'n. OE2&r. glu w. %s of n. ND2&asn'%(d*5.75))
cmd.select('glu31', 'n. CB&r. glu w. %s of n. CB&cysi'%(d*9.82))
cmd.select('glu32', 'n. CB&r. glu w. %s of n. SG&cysi'%(d*10.89))
cmd.select('glu33', 'n. CG&r. glu w. %s of n. CB&cysi'%(d*8.46))
cmd.select('glu34', 'n. CG&r. glu w. %s of n. SG&cysi'%(d*9.51))
cmd.select('glu35', 'n. CD&r. glu w. %s of n. CB&cysi'%(d*8.00))
cmd.select('glu36', 'n. CD&r. glu w. %s of n. SG&cysi'%(d*8.74))
cmd.select('glu37', 'n. OE1&r. glu w. %s of n. CB&cysi'%(d*8.46))
cmd.select('glu38', 'n. OE1&r. glu w. %s of n. SG&cysi'%(d*9.10))
cmd.select('glu39', 'n. OE2&r. glu w. %s of n. CB&cysi'%(d*7.51))
cmd.select('glu40', 'n. OE2&r. glu w. %s of n. SG&cysi'%(d*8.05))
cmd.select('glu41', 'n. CB&r. glu w. %s of n. CB&cysii'%(d*7.46))
cmd.select('glu42', 'n. CB&r. glu w. %s of n. SG&cysii'%(d*9.07))
cmd.select('glu43', 'n. CG&r. glu w. %s of n. CB&cysii'%(d*7.46))
cmd.select('glu44', 'n. CG&r. glu w. %s of n. SG&cysii'%(d*8.91))
cmd.select('glu45', 'n. CD&r. glu w. %s of n. CB&cysii'%(d*6.24))
cmd.select('glu46', 'n. CD&r. glu w. %s of n. SG&cysii'%(d*7.56))
cmd.select('glu47', 'n. OE1&r. glu w. %s of n. CB&cysii'%(d*5.16))
cmd.select('glu48', 'n. OE1&r. glu w. %s of n. SG&cysii'%(d*6.66))
cmd.select('glu49', 'n. OE2&r. glu w. %s of n. CB&cysii'%(d*6.66))
cmd.select('glu50', 'n. OE2&r. glu w. %s of n. SG&cysii'%(d*7.64))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36&br. glu37&br. glu38&br. glu39&br. glu40&br. glu41&br. glu42&br. glu43&br. glu44&br. glu45&br. glu46&br. glu47&br. glu48&br. glu49&br. glu50')
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
cmd.delete('glu50')
cmd.select('A_1l1l-C119A-N406A-C408A-E410A-C419A', 'cys|asn|cysi|cysii|glu')
cmd.delete('cys')
cmd.delete('asn')
cmd.delete('cysi')
cmd.delete('cysii')
cmd.delete('glu')
