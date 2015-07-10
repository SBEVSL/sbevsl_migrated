'''
FUNC:Pfa_1pzp-S70A-K73A-S130A-E166A
PDB:1pzp
EC:3.5.2.6
PFAM:PF00768,PF00144,PF13354
RESI:ser,lys,ser,glu
LOCI:a-70,73,130,166;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. lys'%(d*7.30))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. lys'%(d*6.71))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CD&r. lys'%(d*5.95))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. CE&r. lys'%(d*5.95))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. NZ&r. lys'%(d*5.58))
cmd.select('ser6', 'n. OG&r. ser w. %s of n. CB&r. lys'%(d*7.82))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CG&r. lys'%(d*6.89))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CD&r. lys'%(d*5.93))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. CE&r. lys'%(d*5.41))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. NZ&r. lys'%(d*4.66))
cmd.select('ser11', 'n. CB&r. ser w. %s of n. CB&r. ser'%(d*6.58))
cmd.select('ser12', 'n. CB&r. ser w. %s of n. OG&r. ser'%(d*5.17))
cmd.select('ser13', 'n. OG&r. ser w. %s of n. CB&r. ser'%(d*6.35))
cmd.select('ser14', 'n. OG&r. ser w. %s of n. OG&r. ser'%(d*5.03))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*10.46))
cmd.select('ser16', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*9.23))
cmd.select('ser17', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*8.06))
cmd.select('ser18', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*8.43))
cmd.select('ser19', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*6.97))
cmd.select('ser20', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*9.28))
cmd.select('ser21', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*8.16))
cmd.select('ser22', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*6.94))
cmd.select('ser23', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*7.22))
cmd.select('ser24', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*5.98))
cmd.select('ser', 'br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.select('lys1', 'n. CB&r. lys w. %s of n. CB&ser'%(d*7.30))
cmd.select('lys2', 'n. CB&r. lys w. %s of n. OG&ser'%(d*7.82))
cmd.select('lys3', 'n. CG&r. lys w. %s of n. CB&ser'%(d*6.71))
cmd.select('lys4', 'n. CG&r. lys w. %s of n. OG&ser'%(d*6.89))
cmd.select('lys5', 'n. CD&r. lys w. %s of n. CB&ser'%(d*5.95))
cmd.select('lys6', 'n. CD&r. lys w. %s of n. OG&ser'%(d*5.93))
cmd.select('lys7', 'n. CE&r. lys w. %s of n. CB&ser'%(d*5.95))
cmd.select('lys8', 'n. CE&r. lys w. %s of n. OG&ser'%(d*5.41))
cmd.select('lys9', 'n. NZ&r. lys w. %s of n. CB&ser'%(d*5.58))
cmd.select('lys10', 'n. NZ&r. lys w. %s of n. OG&ser'%(d*4.66))
cmd.select('lys11', 'n. CB&r. lys w. %s of n. CB&r. ser'%(d*8.94))
cmd.select('lys12', 'n. CB&r. lys w. %s of n. OG&r. ser'%(d*8.12))
cmd.select('lys13', 'n. CG&r. lys w. %s of n. CB&r. ser'%(d*8.47))
cmd.select('lys14', 'n. CG&r. lys w. %s of n. OG&r. ser'%(d*7.59))
cmd.select('lys15', 'n. CD&r. lys w. %s of n. CB&r. ser'%(d*7.00))
cmd.select('lys16', 'n. CD&r. lys w. %s of n. OG&r. ser'%(d*6.19))
cmd.select('lys17', 'n. CE&r. lys w. %s of n. CB&r. ser'%(d*7.20))
cmd.select('lys18', 'n. CE&r. lys w. %s of n. OG&r. ser'%(d*6.35))
cmd.select('lys19', 'n. NZ&r. lys w. %s of n. CB&r. ser'%(d*6.17))
cmd.select('lys20', 'n. NZ&r. lys w. %s of n. OG&r. ser'%(d*5.38))
cmd.select('lys21', 'n. CB&r. lys w. %s of n. CB&r. glu'%(d*11.25))
cmd.select('lys22', 'n. CB&r. lys w. %s of n. CG&r. glu'%(d*9.76))
cmd.select('lys23', 'n. CB&r. lys w. %s of n. CD&r. glu'%(d*9.50))
cmd.select('lys24', 'n. CB&r. lys w. %s of n. OE1&r. glu'%(d*10.56))
cmd.select('lys25', 'n. CB&r. lys w. %s of n. OE2&r. glu'%(d*8.42))
cmd.select('lys26', 'n. CG&r. lys w. %s of n. CB&r. glu'%(d*9.71))
cmd.select('lys27', 'n. CG&r. lys w. %s of n. CG&r. glu'%(d*8.24))
cmd.select('lys28', 'n. CG&r. lys w. %s of n. CD&r. glu'%(d*7.99))
cmd.select('lys29', 'n. CG&r. lys w. %s of n. OE1&r. glu'%(d*9.07))
cmd.select('lys30', 'n. CG&r. lys w. %s of n. OE2&r. glu'%(d*6.95))
cmd.select('lys31', 'n. CD&r. lys w. %s of n. CB&r. glu'%(d*9.43))
cmd.select('lys32', 'n. CD&r. lys w. %s of n. CG&r. glu'%(d*8.04))
cmd.select('lys33', 'n. CD&r. lys w. %s of n. CD&r. glu'%(d*7.66))
cmd.select('lys34', 'n. CD&r. lys w. %s of n. OE1&r. glu'%(d*8.63))
cmd.select('lys35', 'n. CD&r. lys w. %s of n. OE2&r. glu'%(d*6.66))
cmd.select('lys36', 'n. CE&r. lys w. %s of n. CB&r. glu'%(d*7.94))
cmd.select('lys37', 'n. CE&r. lys w. %s of n. CG&r. glu'%(d*6.57))
cmd.select('lys38', 'n. CE&r. lys w. %s of n. CD&r. glu'%(d*6.15))
cmd.select('lys39', 'n. CE&r. lys w. %s of n. OE1&r. glu'%(d*7.12))
cmd.select('lys40', 'n. CE&r. lys w. %s of n. OE2&r. glu'%(d*5.23))
cmd.select('lys41', 'n. NZ&r. lys w. %s of n. CB&r. glu'%(d*7.92))
cmd.select('lys42', 'n. NZ&r. lys w. %s of n. CG&r. glu'%(d*6.76))
cmd.select('lys43', 'n. NZ&r. lys w. %s of n. CD&r. glu'%(d*6.11))
cmd.select('lys44', 'n. NZ&r. lys w. %s of n. OE1&r. glu'%(d*6.80))
cmd.select('lys45', 'n. NZ&r. lys w. %s of n. OE2&r. glu'%(d*5.35))
cmd.select('lys', 'br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27&br. lys28&br. lys29&br. lys30&br. lys31&br. lys32&br. lys33&br. lys34&br. lys35&br. lys36&br. lys37&br. lys38&br. lys39&br. lys40&br. lys41&br. lys42&br. lys43&br. lys44&br. lys45')
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
cmd.delete('lys28')
cmd.delete('lys29')
cmd.delete('lys30')
cmd.delete('lys31')
cmd.delete('lys32')
cmd.delete('lys33')
cmd.delete('lys34')
cmd.delete('lys35')
cmd.delete('lys36')
cmd.delete('lys37')
cmd.delete('lys38')
cmd.delete('lys39')
cmd.delete('lys40')
cmd.delete('lys41')
cmd.delete('lys42')
cmd.delete('lys43')
cmd.delete('lys44')
cmd.delete('lys45')
cmd.select('seri1', 'n. CB&r. ser w. %s of n. CB&ser'%(d*6.58))
cmd.select('seri2', 'n. CB&r. ser w. %s of n. OG&ser'%(d*6.35))
cmd.select('seri3', 'n. OG&r. ser w. %s of n. CB&ser'%(d*5.17))
cmd.select('seri4', 'n. OG&r. ser w. %s of n. OG&ser'%(d*5.03))
cmd.select('seri5', 'n. CB&r. ser w. %s of n. CB&lys'%(d*8.94))
cmd.select('seri6', 'n. CB&r. ser w. %s of n. CG&lys'%(d*8.47))
cmd.select('seri7', 'n. CB&r. ser w. %s of n. CD&lys'%(d*7.00))
cmd.select('seri8', 'n. CB&r. ser w. %s of n. CE&lys'%(d*7.20))
cmd.select('seri9', 'n. CB&r. ser w. %s of n. NZ&lys'%(d*6.17))
cmd.select('seri10', 'n. OG&r. ser w. %s of n. CB&lys'%(d*8.12))
cmd.select('seri11', 'n. OG&r. ser w. %s of n. CG&lys'%(d*7.59))
cmd.select('seri12', 'n. OG&r. ser w. %s of n. CD&lys'%(d*6.19))
cmd.select('seri13', 'n. OG&r. ser w. %s of n. CE&lys'%(d*6.35))
cmd.select('seri14', 'n. OG&r. ser w. %s of n. NZ&lys'%(d*5.38))
cmd.select('seri15', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*11.68))
cmd.select('seri16', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*10.76))
cmd.select('seri17', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*10.01))
cmd.select('seri18', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*10.37))
cmd.select('seri19', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*9.32))
cmd.select('seri20', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*11.07))
cmd.select('seri21', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*10.04))
cmd.select('seri22', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*9.15))
cmd.select('seri23', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*9.52))
cmd.select('seri24', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*8.33))
cmd.select('seri', 'br. seri1&br. seri2&br. seri3&br. seri4&br. seri5&br. seri6&br. seri7&br. seri8&br. seri9&br. seri10&br. seri11&br. seri12&br. seri13&br. seri14&br. seri15&br. seri16&br. seri17&br. seri18&br. seri19&br. seri20&br. seri21&br. seri22&br. seri23&br. seri24')
cmd.delete('seri1')
cmd.delete('seri2')
cmd.delete('seri3')
cmd.delete('seri4')
cmd.delete('seri5')
cmd.delete('seri6')
cmd.delete('seri7')
cmd.delete('seri8')
cmd.delete('seri9')
cmd.delete('seri10')
cmd.delete('seri11')
cmd.delete('seri12')
cmd.delete('seri13')
cmd.delete('seri14')
cmd.delete('seri15')
cmd.delete('seri16')
cmd.delete('seri17')
cmd.delete('seri18')
cmd.delete('seri19')
cmd.delete('seri20')
cmd.delete('seri21')
cmd.delete('seri22')
cmd.delete('seri23')
cmd.delete('seri24')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*10.46))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*9.28))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*9.23))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*8.16))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*8.06))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*6.94))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*8.43))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*7.22))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*6.97))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*5.98))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&lys'%(d*11.25))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. CG&lys'%(d*9.71))
cmd.select('glu13', 'n. CB&r. glu w. %s of n. CD&lys'%(d*9.43))
cmd.select('glu14', 'n. CB&r. glu w. %s of n. CE&lys'%(d*7.94))
cmd.select('glu15', 'n. CB&r. glu w. %s of n. NZ&lys'%(d*7.92))
cmd.select('glu16', 'n. CG&r. glu w. %s of n. CB&lys'%(d*9.76))
cmd.select('glu17', 'n. CG&r. glu w. %s of n. CG&lys'%(d*8.24))
cmd.select('glu18', 'n. CG&r. glu w. %s of n. CD&lys'%(d*8.04))
cmd.select('glu19', 'n. CG&r. glu w. %s of n. CE&lys'%(d*6.57))
cmd.select('glu20', 'n. CG&r. glu w. %s of n. NZ&lys'%(d*6.76))
cmd.select('glu21', 'n. CD&r. glu w. %s of n. CB&lys'%(d*9.50))
cmd.select('glu22', 'n. CD&r. glu w. %s of n. CG&lys'%(d*7.99))
cmd.select('glu23', 'n. CD&r. glu w. %s of n. CD&lys'%(d*7.66))
cmd.select('glu24', 'n. CD&r. glu w. %s of n. CE&lys'%(d*6.15))
cmd.select('glu25', 'n. CD&r. glu w. %s of n. NZ&lys'%(d*6.11))
cmd.select('glu26', 'n. OE1&r. glu w. %s of n. CB&lys'%(d*10.56))
cmd.select('glu27', 'n. OE1&r. glu w. %s of n. CG&lys'%(d*9.07))
cmd.select('glu28', 'n. OE1&r. glu w. %s of n. CD&lys'%(d*8.63))
cmd.select('glu29', 'n. OE1&r. glu w. %s of n. CE&lys'%(d*7.12))
cmd.select('glu30', 'n. OE1&r. glu w. %s of n. NZ&lys'%(d*6.80))
cmd.select('glu31', 'n. OE2&r. glu w. %s of n. CB&lys'%(d*8.42))
cmd.select('glu32', 'n. OE2&r. glu w. %s of n. CG&lys'%(d*6.95))
cmd.select('glu33', 'n. OE2&r. glu w. %s of n. CD&lys'%(d*6.66))
cmd.select('glu34', 'n. OE2&r. glu w. %s of n. CE&lys'%(d*5.23))
cmd.select('glu35', 'n. OE2&r. glu w. %s of n. NZ&lys'%(d*5.35))
cmd.select('glu36', 'n. CB&r. glu w. %s of n. CB&seri'%(d*11.68))
cmd.select('glu37', 'n. CB&r. glu w. %s of n. OG&seri'%(d*11.07))
cmd.select('glu38', 'n. CG&r. glu w. %s of n. CB&seri'%(d*10.76))
cmd.select('glu39', 'n. CG&r. glu w. %s of n. OG&seri'%(d*10.04))
cmd.select('glu40', 'n. CD&r. glu w. %s of n. CB&seri'%(d*10.01))
cmd.select('glu41', 'n. CD&r. glu w. %s of n. OG&seri'%(d*9.15))
cmd.select('glu42', 'n. OE1&r. glu w. %s of n. CB&seri'%(d*10.37))
cmd.select('glu43', 'n. OE1&r. glu w. %s of n. OG&seri'%(d*9.52))
cmd.select('glu44', 'n. OE2&r. glu w. %s of n. CB&seri'%(d*9.32))
cmd.select('glu45', 'n. OE2&r. glu w. %s of n. OG&seri'%(d*8.33))
cmd.select('glu', 'br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36&br. glu37&br. glu38&br. glu39&br. glu40&br. glu41&br. glu42&br. glu43&br. glu44&br. glu45')
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
cmd.select('Pfa_1pzp-S70A-K73A-S130A-E166A', 'ser|lys|seri|glu')
cmd.delete('ser')
cmd.delete('lys')
cmd.delete('seri')
cmd.delete('glu')
