'''
FUNC:A_1b65-Y146A-N218A-S250A-S288A-G289A
PDB:1b65
EC:3.4.11.19
PFAM:PF03576
RESI:tyr,asn,ser,ser,gly
LOCI:a-146,218,250,288,289;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. O&r. gly'%(d*5.40))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. C&r. gly'%(d*6.09))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CA&r. gly'%(d*6.10))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. N&r. gly'%(d*5.55))
cmd.select('ser5', 'n. OG&r. ser w. %s of n. O&r. gly'%(d*5.72))
cmd.select('ser6', 'n. OG&r. ser w. %s of n. C&r. gly'%(d*6.03))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CA&r. gly'%(d*5.51))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. N&r. gly'%(d*4.78))
cmd.select('ser9', 'n. CB&r. ser w. %s of n. CB&r. ser'%(d*7.24))
cmd.select('ser10', 'n. CB&r. ser w. %s of n. OG&r. ser'%(d*6.58))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. CB&r. ser'%(d*6.93))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. OG&r. ser'%(d*6.66))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. CB&r. asn'%(d*6.65))
cmd.select('ser14', 'n. CB&r. ser w. %s of n. CG&r. asn'%(d*7.06))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. OD1&r. asn'%(d*8.28))
cmd.select('ser16', 'n. CB&r. ser w. %s of n. ND2&r. asn'%(d*6.36))
cmd.select('ser17', 'n. OG&r. ser w. %s of n. CB&r. asn'%(d*7.71))
cmd.select('ser18', 'n. OG&r. ser w. %s of n. CG&r. asn'%(d*7.81))
cmd.select('ser19', 'n. OG&r. ser w. %s of n. OD1&r. asn'%(d*8.98))
cmd.select('ser20', 'n. OG&r. ser w. %s of n. ND2&r. asn'%(d*6.86))
cmd.select('ser21', 'n. CB&r. ser w. %s of n. CB&r. tyr'%(d*7.82))
cmd.select('ser22', 'n. CB&r. ser w. %s of n. CG&r. tyr'%(d*9.21))
cmd.select('ser23', 'n. CB&r. ser w. %s of n. CD1&r. tyr'%(d*10.25))
cmd.select('ser24', 'n. CB&r. ser w. %s of n. CD2&r. tyr'%(d*9.60))
cmd.select('ser25', 'n. CB&r. ser w. %s of n. CE1&r. tyr'%(d*11.53))
cmd.select('ser26', 'n. CB&r. ser w. %s of n. CE2&r. tyr'%(d*10.95))
cmd.select('ser27', 'n. CB&r. ser w. %s of n. CZ&r. tyr'%(d*11.80))
cmd.select('ser28', 'n. CB&r. ser w. %s of n. OH&r. tyr'%(d*13.13))
cmd.select('ser29', 'n. CB&r. ser w. %s of n. O&r. tyr'%(d*8.42))
cmd.select('ser30', 'n. CB&r. ser w. %s of n. C&r. tyr'%(d*8.69))
cmd.select('ser31', 'n. CB&r. ser w. %s of n. CA&r. tyr'%(d*7.92))
cmd.select('ser32', 'n. CB&r. ser w. %s of n. N&r. tyr'%(d*6.71))
cmd.select('ser33', 'n. OG&r. ser w. %s of n. CB&r. tyr'%(d*7.35))
cmd.select('ser34', 'n. OG&r. ser w. %s of n. CG&r. tyr'%(d*8.64))
cmd.select('ser35', 'n. OG&r. ser w. %s of n. CD1&r. tyr'%(d*9.61))
cmd.select('ser36', 'n. OG&r. ser w. %s of n. CD2&r. tyr'%(d*9.05))
cmd.select('ser37', 'n. OG&r. ser w. %s of n. CE1&r. tyr'%(d*10.84))
cmd.select('ser38', 'n. OG&r. ser w. %s of n. CE2&r. tyr'%(d*10.34))
cmd.select('ser39', 'n. OG&r. ser w. %s of n. CZ&r. tyr'%(d*11.13))
cmd.select('ser40', 'n. OG&r. ser w. %s of n. OH&r. tyr'%(d*12.42))
cmd.select('ser41', 'n. OG&r. ser w. %s of n. O&r. tyr'%(d*8.49))
cmd.select('ser42', 'n. OG&r. ser w. %s of n. C&r. tyr'%(d*8.73))
cmd.select('ser43', 'n. OG&r. ser w. %s of n. CA&r. tyr'%(d*7.80))
cmd.select('ser44', 'n. OG&r. ser w. %s of n. N&r. tyr'%(d*6.79))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27&br. ser28&br. ser29&br. ser30&br. ser31&br. ser32&br. ser33&br. ser34&br. ser35&br. ser36&br. ser37&br. ser38&br. ser39&br. ser40&br. ser41&br. ser42&br. ser43&br. ser44')
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
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
cmd.delete('ser28')
cmd.delete('ser29')
cmd.delete('ser30')
cmd.delete('ser31')
cmd.delete('ser32')
cmd.delete('ser33')
cmd.delete('ser34')
cmd.delete('ser35')
cmd.delete('ser36')
cmd.delete('ser37')
cmd.delete('ser38')
cmd.delete('ser39')
cmd.delete('ser40')
cmd.delete('ser41')
cmd.delete('ser42')
cmd.delete('ser43')
cmd.delete('ser44')
cmd.select('gly1', 'n. O&r. gly w. %s of n. CB&ser'%(d*5.40))
cmd.select('gly2', 'n. O&r. gly w. %s of n. OG&ser'%(d*5.72))
cmd.select('gly3', 'n. C&r. gly w. %s of n. CB&ser'%(d*6.09))
cmd.select('gly4', 'n. C&r. gly w. %s of n. OG&ser'%(d*6.03))
cmd.select('gly5', 'n. CA&r. gly w. %s of n. CB&ser'%(d*6.10))
cmd.select('gly6', 'n. CA&r. gly w. %s of n. OG&ser'%(d*5.51))
cmd.select('gly7', 'n. N&r. gly w. %s of n. CB&ser'%(d*5.55))
cmd.select('gly8', 'n. N&r. gly w. %s of n. OG&ser'%(d*4.78))
cmd.select('gly9', 'n. O&r. gly w. %s of n. CB&r. ser'%(d*7.39))
cmd.select('gly10', 'n. O&r. gly w. %s of n. OG&r. ser'%(d*6.84))
cmd.select('gly11', 'n. C&r. gly w. %s of n. CB&r. ser'%(d*6.95))
cmd.select('gly12', 'n. C&r. gly w. %s of n. OG&r. ser'%(d*6.70))
cmd.select('gly13', 'n. CA&r. gly w. %s of n. CB&r. ser'%(d*6.79))
cmd.select('gly14', 'n. CA&r. gly w. %s of n. OG&r. ser'%(d*6.91))
cmd.select('gly15', 'n. N&r. gly w. %s of n. CB&r. ser'%(d*5.55))
cmd.select('gly16', 'n. N&r. gly w. %s of n. OG&r. ser'%(d*5.78))
cmd.select('gly17', 'n. O&r. gly w. %s of n. CB&r. asn'%(d*9.47))
cmd.select('gly18', 'n. O&r. gly w. %s of n. CG&r. asn'%(d*10.23))
cmd.select('gly19', 'n. O&r. gly w. %s of n. OD1&r. asn'%(d*11.45))
cmd.select('gly20', 'n. O&r. gly w. %s of n. ND2&r. asn'%(d*9.71))
cmd.select('gly21', 'n. C&r. gly w. %s of n. CB&r. asn'%(d*10.41))
cmd.select('gly22', 'n. C&r. gly w. %s of n. CG&r. asn'%(d*11.06))
cmd.select('gly23', 'n. C&r. gly w. %s of n. OD1&r. asn'%(d*12.28))
cmd.select('gly24', 'n. C&r. gly w. %s of n. ND2&r. asn'%(d*10.45))
cmd.select('gly25', 'n. CA&r. gly w. %s of n. CB&r. asn'%(d*10.70))
cmd.select('gly26', 'n. CA&r. gly w. %s of n. CG&r. asn'%(d*11.11))
cmd.select('gly27', 'n. CA&r. gly w. %s of n. OD1&r. asn'%(d*12.31))
cmd.select('gly28', 'n. CA&r. gly w. %s of n. ND2&r. asn'%(d*10.30))
cmd.select('gly29', 'n. N&r. gly w. %s of n. CB&r. asn'%(d*9.99))
cmd.select('gly30', 'n. N&r. gly w. %s of n. CG&r. asn'%(d*10.29))
cmd.select('gly31', 'n. N&r. gly w. %s of n. OD1&r. asn'%(d*11.44))
cmd.select('gly32', 'n. N&r. gly w. %s of n. ND2&r. asn'%(d*9.45))
cmd.select('gly33', 'n. O&r. gly w. %s of n. CB&r. tyr'%(d*10.73))
cmd.select('gly34', 'n. O&r. gly w. %s of n. CG&r. tyr'%(d*12.13))
cmd.select('gly35', 'n. O&r. gly w. %s of n. CD1&r. tyr'%(d*12.96))
cmd.select('gly36', 'n. O&r. gly w. %s of n. CD2&r. tyr'%(d*12.69))
cmd.select('gly37', 'n. O&r. gly w. %s of n. CE1&r. tyr'%(d*14.27))
cmd.select('gly38', 'n. O&r. gly w. %s of n. CE2&r. tyr'%(d*14.00))
cmd.select('gly39', 'n. O&r. gly w. %s of n. CZ&r. tyr'%(d*14.71))
cmd.select('gly40', 'n. O&r. gly w. %s of n. OH&r. tyr'%(d*16.03))
cmd.select('gly41', 'n. O&r. gly w. %s of n. O&r. tyr'%(d*11.72))
cmd.select('gly42', 'n. O&r. gly w. %s of n. C&r. tyr'%(d*11.84))
cmd.select('gly43', 'n. O&r. gly w. %s of n. CA&r. tyr'%(d*10.85))
cmd.select('gly44', 'n. O&r. gly w. %s of n. N&r. tyr'%(d*9.56))
cmd.select('gly45', 'n. C&r. gly w. %s of n. CB&r. tyr'%(d*11.17))
cmd.select('gly46', 'n. C&r. gly w. %s of n. CG&r. tyr'%(d*12.49))
cmd.select('gly47', 'n. C&r. gly w. %s of n. CD1&r. tyr'%(d*13.29))
cmd.select('gly48', 'n. C&r. gly w. %s of n. CD2&r. tyr'%(d*13.02))
cmd.select('gly49', 'n. C&r. gly w. %s of n. CE1&r. tyr'%(d*14.54))
cmd.select('gly50', 'n. C&r. gly w. %s of n. CE2&r. tyr'%(d*14.28))
cmd.select('gly50',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27&br. gly28&br. gly29&br. gly30&br. gly31&br. gly32&br. gly33&br. gly34&br. gly35&br. gly36&br. gly37&br. gly38&br. gly39&br. gly40&br. gly41&br. gly42&br. gly43&br. gly44&br. gly45&br. gly46&br. gly47&br. gly48&br. gly49&br. gly50')
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
cmd.delete('gly41')
cmd.delete('gly42')
cmd.delete('gly43')
cmd.delete('gly44')
cmd.delete('gly45')
cmd.delete('gly46')
cmd.delete('gly47')
cmd.delete('gly48')
cmd.delete('gly49')
cmd.select('gly51', 'n. C&r. gly w. %s of n. CZ&r. tyr'%(d*14.96))
cmd.select('gly52', 'n. C&r. gly w. %s of n. OH&r. tyr'%(d*16.24))
cmd.select('gly53', 'n. C&r. gly w. %s of n. O&r. tyr'%(d*12.38))
cmd.select('gly54', 'n. C&r. gly w. %s of n. C&r. tyr'%(d*12.51))
cmd.select('gly55', 'n. C&r. gly w. %s of n. CA&r. tyr'%(d*11.47))
cmd.select('gly56', 'n. C&r. gly w. %s of n. N&r. tyr'%(d*10.27))
cmd.select('gly57', 'n. CA&r. gly w. %s of n. CB&r. tyr'%(d*10.41))
cmd.select('gly58', 'n. CA&r. gly w. %s of n. CG&r. tyr'%(d*11.62))
cmd.select('gly59', 'n. CA&r. gly w. %s of n. CD1&r. tyr'%(d*12.35))
cmd.select('gly60', 'n. CA&r. gly w. %s of n. CD2&r. tyr'%(d*12.16))
cmd.select('gly61', 'n. CA&r. gly w. %s of n. CE1&r. tyr'%(d*13.54))
cmd.select('gly62', 'n. CA&r. gly w. %s of n. CE2&r. tyr'%(d*13.35))
cmd.select('gly63', 'n. CA&r. gly w. %s of n. CZ&r. tyr'%(d*13.97))
cmd.select('gly64', 'n. CA&r. gly w. %s of n. OH&r. tyr'%(d*15.20))
cmd.select('gly65', 'n. CA&r. gly w. %s of n. O&r. tyr'%(d*11.95))
cmd.select('gly66', 'n. CA&r. gly w. %s of n. C&r. tyr'%(d*12.05))
cmd.select('gly67', 'n. CA&r. gly w. %s of n. CA&r. tyr'%(d*10.93))
cmd.select('gly68', 'n. CA&r. gly w. %s of n. N&r. tyr'%(d*9.88))
cmd.select('gly69', 'n. N&r. gly w. %s of n. CB&r. tyr'%(d*9.83))
cmd.select('gly70', 'n. N&r. gly w. %s of n. CG&r. tyr'%(d*10.98))
cmd.select('gly71', 'n. N&r. gly w. %s of n. CD1&r. tyr'%(d*11.83))
cmd.select('gly72', 'n. N&r. gly w. %s of n. CD2&r. tyr'%(d*11.33))
cmd.select('gly73', 'n. N&r. gly w. %s of n. CE1&r. tyr'%(d*12.96))
cmd.select('gly74', 'n. N&r. gly w. %s of n. CE2&r. tyr'%(d*12.50))
cmd.select('gly75', 'n. N&r. gly w. %s of n. CZ&r. tyr'%(d*13.24))
cmd.select('gly76', 'n. N&r. gly w. %s of n. OH&r. tyr'%(d*14.44))
cmd.select('gly77', 'n. N&r. gly w. %s of n. O&r. tyr'%(d*11.20))
cmd.select('gly78', 'n. N&r. gly w. %s of n. C&r. tyr'%(d*11.46))
cmd.select('gly79', 'n. N&r. gly w. %s of n. CA&r. tyr'%(d*10.46))
cmd.select('gly80', 'n. N&r. gly w. %s of n. N&r. tyr'%(d*9.51))
cmd.select('gly',' gly50&br. gly51&br. gly52&br. gly53&br. gly54&br. gly55&br. gly56&br. gly57&br. gly58&br. gly59&br. gly60&br. gly61&br. gly62&br. gly63&br. gly64&br. gly65&br. gly66&br. gly67&br. gly68&br. gly69&br. gly70&br. gly71&br. gly72&br. gly73&br. gly74&br. gly75&br. gly76&br. gly77&br. gly78&br. gly79&br. gly80')
cmd.delete('gly50')
cmd.delete('gly51')
cmd.delete('gly52')
cmd.delete('gly53')
cmd.delete('gly54')
cmd.delete('gly55')
cmd.delete('gly56')
cmd.delete('gly57')
cmd.delete('gly58')
cmd.delete('gly59')
cmd.delete('gly60')
cmd.delete('gly61')
cmd.delete('gly62')
cmd.delete('gly63')
cmd.delete('gly64')
cmd.delete('gly65')
cmd.delete('gly66')
cmd.delete('gly67')
cmd.delete('gly68')
cmd.delete('gly69')
cmd.delete('gly70')
cmd.delete('gly71')
cmd.delete('gly72')
cmd.delete('gly73')
cmd.delete('gly74')
cmd.delete('gly75')
cmd.delete('gly76')
cmd.delete('gly77')
cmd.delete('gly78')
cmd.delete('gly79')
cmd.delete('gly80')
cmd.select('seri1', 'n. CB&r. ser w. %s of n. CB&ser'%(d*7.24))
cmd.select('seri2', 'n. CB&r. ser w. %s of n. OG&ser'%(d*6.93))
cmd.select('seri3', 'n. OG&r. ser w. %s of n. CB&ser'%(d*6.58))
cmd.select('seri4', 'n. OG&r. ser w. %s of n. OG&ser'%(d*6.66))
cmd.select('seri5', 'n. CB&r. ser w. %s of n. O&gly'%(d*7.39))
cmd.select('seri6', 'n. CB&r. ser w. %s of n. C&gly'%(d*6.95))
cmd.select('seri7', 'n. CB&r. ser w. %s of n. CA&gly'%(d*6.79))
cmd.select('seri8', 'n. CB&r. ser w. %s of n. N&gly'%(d*5.55))
cmd.select('seri9', 'n. OG&r. ser w. %s of n. O&gly'%(d*6.84))
cmd.select('seri10', 'n. OG&r. ser w. %s of n. C&gly'%(d*6.70))
cmd.select('seri11', 'n. OG&r. ser w. %s of n. CA&gly'%(d*6.91))
cmd.select('seri12', 'n. OG&r. ser w. %s of n. N&gly'%(d*5.78))
cmd.select('seri13', 'n. CB&r. ser w. %s of n. CB&r. asn'%(d*10.18))
cmd.select('seri14', 'n. CB&r. ser w. %s of n. CG&r. asn'%(d*10.50))
cmd.select('seri15', 'n. CB&r. ser w. %s of n. OD1&r. asn'%(d*11.44))
cmd.select('seri16', 'n. CB&r. ser w. %s of n. ND2&r. asn'%(d*9.96))
cmd.select('seri17', 'n. OG&r. ser w. %s of n. CB&r. asn'%(d*9.14))
cmd.select('seri18', 'n. OG&r. ser w. %s of n. CG&r. asn'%(d*9.64))
cmd.select('seri19', 'n. OG&r. ser w. %s of n. OD1&r. asn'%(d*10.60))
cmd.select('seri20', 'n. OG&r. ser w. %s of n. ND2&r. asn'%(d*9.28))
cmd.select('seri21', 'n. CB&r. ser w. %s of n. CB&r. tyr'%(d*11.54))
cmd.select('seri22', 'n. CB&r. ser w. %s of n. CG&r. tyr'%(d*12.50))
cmd.select('seri23', 'n. CB&r. ser w. %s of n. CD1&r. tyr'%(d*13.59))
cmd.select('seri24', 'n. CB&r. ser w. %s of n. CD2&r. tyr'%(d*12.39))
cmd.select('seri25', 'n. CB&r. ser w. %s of n. CE1&r. tyr'%(d*14.55))
cmd.select('seri26', 'n. CB&r. ser w. %s of n. CE2&r. tyr'%(d*13.43))
cmd.select('seri27', 'n. CB&r. ser w. %s of n. CZ&r. tyr'%(d*14.45))
cmd.select('seri28', 'n. CB&r. ser w. %s of n. OH&r. tyr'%(d*15.52))
cmd.select('seri29', 'n. CB&r. ser w. %s of n. O&r. tyr'%(d*12.15))
cmd.select('seri30', 'n. CB&r. ser w. %s of n. C&r. tyr'%(d*12.80))
cmd.select('seri31', 'n. CB&r. ser w. %s of n. CA&r. tyr'%(d*12.23))
cmd.select('seri32', 'n. CB&r. ser w. %s of n. N&r. tyr'%(d*11.40))
cmd.select('seri33', 'n. OG&r. ser w. %s of n. CB&r. tyr'%(d*11.39))
cmd.select('seri34', 'n. OG&r. ser w. %s of n. CG&r. tyr'%(d*12.46))
cmd.select('seri35', 'n. OG&r. ser w. %s of n. CD1&r. tyr'%(d*13.61))
cmd.select('seri36', 'n. OG&r. ser w. %s of n. CD2&r. tyr'%(d*12.38))
cmd.select('seri37', 'n. OG&r. ser w. %s of n. CE1&r. tyr'%(d*14.66))
cmd.select('seri38', 'n. OG&r. ser w. %s of n. CE2&r. tyr'%(d*13.51))
cmd.select('seri39', 'n. OG&r. ser w. %s of n. CZ&r. tyr'%(d*14.57))
cmd.select('seri40', 'n. OG&r. ser w. %s of n. OH&r. tyr'%(d*15.71))
cmd.select('seri41', 'n. OG&r. ser w. %s of n. O&r. tyr'%(d*11.71))
cmd.select('seri42', 'n. OG&r. ser w. %s of n. C&r. tyr'%(d*12.37))
cmd.select('seri43', 'n. OG&r. ser w. %s of n. CA&r. tyr'%(d*11.88))
cmd.select('seri44', 'n. OG&r. ser w. %s of n. N&r. tyr'%(d*10.93))
cmd.select('seri',' br. seri1&br. seri2&br. seri3&br. seri4&br. seri5&br. seri6&br. seri7&br. seri8&br. seri9&br. seri10&br. seri11&br. seri12&br. seri13&br. seri14&br. seri15&br. seri16&br. seri17&br. seri18&br. seri19&br. seri20&br. seri21&br. seri22&br. seri23&br. seri24&br. seri25&br. seri26&br. seri27&br. seri28&br. seri29&br. seri30&br. seri31&br. seri32&br. seri33&br. seri34&br. seri35&br. seri36&br. seri37&br. seri38&br. seri39&br. seri40&br. seri41&br. seri42&br. seri43&br. seri44')
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
cmd.delete('seri25')
cmd.delete('seri26')
cmd.delete('seri27')
cmd.delete('seri28')
cmd.delete('seri29')
cmd.delete('seri30')
cmd.delete('seri31')
cmd.delete('seri32')
cmd.delete('seri33')
cmd.delete('seri34')
cmd.delete('seri35')
cmd.delete('seri36')
cmd.delete('seri37')
cmd.delete('seri38')
cmd.delete('seri39')
cmd.delete('seri40')
cmd.delete('seri41')
cmd.delete('seri42')
cmd.delete('seri43')
cmd.delete('seri44')
cmd.select('asn1', 'n. CB&r. asn w. %s of n. CB&ser'%(d*6.65))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. OG&ser'%(d*7.71))
cmd.select('asn3', 'n. CG&r. asn w. %s of n. CB&ser'%(d*7.06))
cmd.select('asn4', 'n. CG&r. asn w. %s of n. OG&ser'%(d*7.81))
cmd.select('asn5', 'n. OD1&r. asn w. %s of n. CB&ser'%(d*8.28))
cmd.select('asn6', 'n. OD1&r. asn w. %s of n. OG&ser'%(d*8.98))
cmd.select('asn7', 'n. ND2&r. asn w. %s of n. CB&ser'%(d*6.36))
cmd.select('asn8', 'n. ND2&r. asn w. %s of n. OG&ser'%(d*6.86))
cmd.select('asn9', 'n. CB&r. asn w. %s of n. O&gly'%(d*9.47))
cmd.select('asn10', 'n. CB&r. asn w. %s of n. C&gly'%(d*10.41))
cmd.select('asn11', 'n. CB&r. asn w. %s of n. CA&gly'%(d*10.70))
cmd.select('asn12', 'n. CB&r. asn w. %s of n. N&gly'%(d*9.99))
cmd.select('asn13', 'n. CG&r. asn w. %s of n. O&gly'%(d*10.23))
cmd.select('asn14', 'n. CG&r. asn w. %s of n. C&gly'%(d*11.06))
cmd.select('asn15', 'n. CG&r. asn w. %s of n. CA&gly'%(d*11.11))
cmd.select('asn16', 'n. CG&r. asn w. %s of n. N&gly'%(d*10.29))
cmd.select('asn17', 'n. OD1&r. asn w. %s of n. O&gly'%(d*11.45))
cmd.select('asn18', 'n. OD1&r. asn w. %s of n. C&gly'%(d*12.28))
cmd.select('asn19', 'n. OD1&r. asn w. %s of n. CA&gly'%(d*12.31))
cmd.select('asn20', 'n. OD1&r. asn w. %s of n. N&gly'%(d*11.44))
cmd.select('asn21', 'n. ND2&r. asn w. %s of n. O&gly'%(d*9.71))
cmd.select('asn22', 'n. ND2&r. asn w. %s of n. C&gly'%(d*10.45))
cmd.select('asn23', 'n. ND2&r. asn w. %s of n. CA&gly'%(d*10.30))
cmd.select('asn24', 'n. ND2&r. asn w. %s of n. N&gly'%(d*9.45))
cmd.select('asn25', 'n. CB&r. asn w. %s of n. CB&seri'%(d*10.18))
cmd.select('asn26', 'n. CB&r. asn w. %s of n. OG&seri'%(d*9.14))
cmd.select('asn27', 'n. CG&r. asn w. %s of n. CB&seri'%(d*10.50))
cmd.select('asn28', 'n. CG&r. asn w. %s of n. OG&seri'%(d*9.64))
cmd.select('asn29', 'n. OD1&r. asn w. %s of n. CB&seri'%(d*11.44))
cmd.select('asn30', 'n. OD1&r. asn w. %s of n. OG&seri'%(d*10.60))
cmd.select('asn31', 'n. ND2&r. asn w. %s of n. CB&seri'%(d*9.96))
cmd.select('asn32', 'n. ND2&r. asn w. %s of n. OG&seri'%(d*9.28))
cmd.select('asn33', 'n. CB&r. asn w. %s of n. CB&r. tyr'%(d*8.57))
cmd.select('asn34', 'n. CB&r. asn w. %s of n. CG&r. tyr'%(d*9.70))
cmd.select('asn35', 'n. CB&r. asn w. %s of n. CD1&r. tyr'%(d*10.93))
cmd.select('asn36', 'n. CB&r. asn w. %s of n. CD2&r. tyr'%(d*9.68))
cmd.select('asn37', 'n. CB&r. asn w. %s of n. CE1&r. tyr'%(d*12.03))
cmd.select('asn38', 'n. CB&r. asn w. %s of n. CE2&r. tyr'%(d*10.91))
cmd.select('asn39', 'n. CB&r. asn w. %s of n. CZ&r. tyr'%(d*11.98))
cmd.select('asn40', 'n. CB&r. asn w. %s of n. OH&r. tyr'%(d*13.21))
cmd.select('asn41', 'n. CB&r. asn w. %s of n. O&r. tyr'%(d*6.97))
cmd.select('asn42', 'n. CB&r. asn w. %s of n. C&r. tyr'%(d*7.63))
cmd.select('asn43', 'n. CB&r. asn w. %s of n. CA&r. tyr'%(d*7.96))
cmd.select('asn44', 'n. CB&r. asn w. %s of n. N&r. tyr'%(d*7.07))
cmd.select('asn45', 'n. CG&r. asn w. %s of n. CB&r. tyr'%(d*7.57))
cmd.select('asn46', 'n. CG&r. asn w. %s of n. CG&r. tyr'%(d*8.52))
cmd.select('asn47', 'n. CG&r. asn w. %s of n. CD1&r. tyr'%(d*9.78))
cmd.select('asn48', 'n. CG&r. asn w. %s of n. CD2&r. tyr'%(d*8.35))
cmd.select('asn49', 'n. CG&r. asn w. %s of n. CE1&r. tyr'%(d*10.79))
cmd.select('asn50', 'n. CG&r. asn w. %s of n. CE2&r. tyr'%(d*9.52))
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
cmd.select('asn51', 'n. CG&r. asn w. %s of n. CZ&r. tyr'%(d*10.63))
cmd.select('asn52', 'n. CG&r. asn w. %s of n. OH&r. tyr'%(d*11.82))
cmd.select('asn53', 'n. CG&r. asn w. %s of n. O&r. tyr'%(d*5.63))
cmd.select('asn54', 'n. CG&r. asn w. %s of n. C&r. tyr'%(d*6.47))
cmd.select('asn55', 'n. CG&r. asn w. %s of n. CA&r. tyr'%(d*7.03))
cmd.select('asn56', 'n. CG&r. asn w. %s of n. N&r. tyr'%(d*6.46))
cmd.select('asn57', 'n. OD1&r. asn w. %s of n. CB&r. tyr'%(d*8.12))
cmd.select('asn58', 'n. OD1&r. asn w. %s of n. CG&r. tyr'%(d*8.86))
cmd.select('asn59', 'n. OD1&r. asn w. %s of n. CD1&r. tyr'%(d*10.10))
cmd.select('asn60', 'n. OD1&r. asn w. %s of n. CD2&r. tyr'%(d*8.52))
cmd.select('asn61', 'n. OD1&r. asn w. %s of n. CE1&r. tyr'%(d*10.96))
cmd.select('asn62', 'n. OD1&r. asn w. %s of n. CE2&r. tyr'%(d*9.54))
cmd.select('asn63', 'n. OD1&r. asn w. %s of n. CZ&r. tyr'%(d*10.68))
cmd.select('asn64', 'n. OD1&r. asn w. %s of n. OH&r. tyr'%(d*11.77))
cmd.select('asn65', 'n. OD1&r. asn w. %s of n. O&r. tyr'%(d*5.72))
cmd.select('asn66', 'n. OD1&r. asn w. %s of n. C&r. tyr'%(d*6.65))
cmd.select('asn67', 'n. OD1&r. asn w. %s of n. CA&r. tyr'%(d*7.53))
cmd.select('asn68', 'n. OD1&r. asn w. %s of n. N&r. tyr'%(d*7.22))
cmd.select('asn69', 'n. ND2&r. asn w. %s of n. CB&r. tyr'%(d*6.33))
cmd.select('asn70', 'n. ND2&r. asn w. %s of n. CG&r. tyr'%(d*7.34))
cmd.select('asn71', 'n. ND2&r. asn w. %s of n. CD1&r. tyr'%(d*8.62))
cmd.select('asn72', 'n. ND2&r. asn w. %s of n. CD2&r. tyr'%(d*7.23))
cmd.select('asn73', 'n. ND2&r. asn w. %s of n. CE1&r. tyr'%(d*9.67))
cmd.select('asn74', 'n. ND2&r. asn w. %s of n. CE2&r. tyr'%(d*8.48))
cmd.select('asn75', 'n. ND2&r. asn w. %s of n. CZ&r. tyr'%(d*9.57))
cmd.select('asn76', 'n. ND2&r. asn w. %s of n. OH&r. tyr'%(d*10.80))
cmd.select('asn77', 'n. ND2&r. asn w. %s of n. O&r. tyr'%(d*4.85))
cmd.select('asn78', 'n. ND2&r. asn w. %s of n. C&r. tyr'%(d*5.67))
cmd.select('asn79', 'n. ND2&r. asn w. %s of n. CA&r. tyr'%(d*6.00))
cmd.select('asn80', 'n. ND2&r. asn w. %s of n. N&r. tyr'%(d*5.47))
cmd.select('asn',' asn50&br. asn51&br. asn52&br. asn53&br. asn54&br. asn55&br. asn56&br. asn57&br. asn58&br. asn59&br. asn60&br. asn61&br. asn62&br. asn63&br. asn64&br. asn65&br. asn66&br. asn67&br. asn68&br. asn69&br. asn70&br. asn71&br. asn72&br. asn73&br. asn74&br. asn75&br. asn76&br. asn77&br. asn78&br. asn79&br. asn80')
cmd.delete('asn50')
cmd.delete('asn51')
cmd.delete('asn52')
cmd.delete('asn53')
cmd.delete('asn54')
cmd.delete('asn55')
cmd.delete('asn56')
cmd.delete('asn57')
cmd.delete('asn58')
cmd.delete('asn59')
cmd.delete('asn60')
cmd.delete('asn61')
cmd.delete('asn62')
cmd.delete('asn63')
cmd.delete('asn64')
cmd.delete('asn65')
cmd.delete('asn66')
cmd.delete('asn67')
cmd.delete('asn68')
cmd.delete('asn69')
cmd.delete('asn70')
cmd.delete('asn71')
cmd.delete('asn72')
cmd.delete('asn73')
cmd.delete('asn74')
cmd.delete('asn75')
cmd.delete('asn76')
cmd.delete('asn77')
cmd.delete('asn78')
cmd.delete('asn79')
cmd.delete('asn80')
cmd.select('tyr1', 'n. CB&r. tyr w. %s of n. CB&ser'%(d*7.82))
cmd.select('tyr2', 'n. CB&r. tyr w. %s of n. OG&ser'%(d*7.35))
cmd.select('tyr3', 'n. CG&r. tyr w. %s of n. CB&ser'%(d*9.21))
cmd.select('tyr4', 'n. CG&r. tyr w. %s of n. OG&ser'%(d*8.64))
cmd.select('tyr5', 'n. CD1&r. tyr w. %s of n. CB&ser'%(d*10.25))
cmd.select('tyr6', 'n. CD1&r. tyr w. %s of n. OG&ser'%(d*9.61))
cmd.select('tyr7', 'n. CD2&r. tyr w. %s of n. CB&ser'%(d*9.60))
cmd.select('tyr8', 'n. CD2&r. tyr w. %s of n. OG&ser'%(d*9.05))
cmd.select('tyr9', 'n. CE1&r. tyr w. %s of n. CB&ser'%(d*11.53))
cmd.select('tyr10', 'n. CE1&r. tyr w. %s of n. OG&ser'%(d*10.84))
cmd.select('tyr11', 'n. CE2&r. tyr w. %s of n. CB&ser'%(d*10.95))
cmd.select('tyr12', 'n. CE2&r. tyr w. %s of n. OG&ser'%(d*10.34))
cmd.select('tyr13', 'n. CZ&r. tyr w. %s of n. CB&ser'%(d*11.80))
cmd.select('tyr14', 'n. CZ&r. tyr w. %s of n. OG&ser'%(d*11.13))
cmd.select('tyr15', 'n. OH&r. tyr w. %s of n. CB&ser'%(d*13.13))
cmd.select('tyr16', 'n. OH&r. tyr w. %s of n. OG&ser'%(d*12.42))
cmd.select('tyr17', 'n. O&r. tyr w. %s of n. CB&ser'%(d*8.42))
cmd.select('tyr18', 'n. O&r. tyr w. %s of n. OG&ser'%(d*8.49))
cmd.select('tyr19', 'n. C&r. tyr w. %s of n. CB&ser'%(d*8.69))
cmd.select('tyr20', 'n. C&r. tyr w. %s of n. OG&ser'%(d*8.73))
cmd.select('tyr21', 'n. CA&r. tyr w. %s of n. CB&ser'%(d*7.92))
cmd.select('tyr22', 'n. CA&r. tyr w. %s of n. OG&ser'%(d*7.80))
cmd.select('tyr23', 'n. N&r. tyr w. %s of n. CB&ser'%(d*6.71))
cmd.select('tyr24', 'n. N&r. tyr w. %s of n. OG&ser'%(d*6.79))
cmd.select('tyr25', 'n. CB&r. tyr w. %s of n. O&gly'%(d*10.73))
cmd.select('tyr26', 'n. CB&r. tyr w. %s of n. C&gly'%(d*11.17))
cmd.select('tyr27', 'n. CB&r. tyr w. %s of n. CA&gly'%(d*10.41))
cmd.select('tyr28', 'n. CB&r. tyr w. %s of n. N&gly'%(d*9.83))
cmd.select('tyr29', 'n. CG&r. tyr w. %s of n. O&gly'%(d*12.13))
cmd.select('tyr30', 'n. CG&r. tyr w. %s of n. C&gly'%(d*12.49))
cmd.select('tyr31', 'n. CG&r. tyr w. %s of n. CA&gly'%(d*11.62))
cmd.select('tyr32', 'n. CG&r. tyr w. %s of n. N&gly'%(d*10.98))
cmd.select('tyr33', 'n. CD1&r. tyr w. %s of n. O&gly'%(d*12.96))
cmd.select('tyr34', 'n. CD1&r. tyr w. %s of n. C&gly'%(d*13.29))
cmd.select('tyr35', 'n. CD1&r. tyr w. %s of n. CA&gly'%(d*12.35))
cmd.select('tyr36', 'n. CD1&r. tyr w. %s of n. N&gly'%(d*11.83))
cmd.select('tyr37', 'n. CD2&r. tyr w. %s of n. O&gly'%(d*12.69))
cmd.select('tyr38', 'n. CD2&r. tyr w. %s of n. C&gly'%(d*13.02))
cmd.select('tyr39', 'n. CD2&r. tyr w. %s of n. CA&gly'%(d*12.16))
cmd.select('tyr40', 'n. CD2&r. tyr w. %s of n. N&gly'%(d*11.33))
cmd.select('tyr41', 'n. CE1&r. tyr w. %s of n. O&gly'%(d*14.27))
cmd.select('tyr42', 'n. CE1&r. tyr w. %s of n. C&gly'%(d*14.54))
cmd.select('tyr43', 'n. CE1&r. tyr w. %s of n. CA&gly'%(d*13.54))
cmd.select('tyr44', 'n. CE1&r. tyr w. %s of n. N&gly'%(d*12.96))
cmd.select('tyr45', 'n. CE2&r. tyr w. %s of n. O&gly'%(d*14.00))
cmd.select('tyr46', 'n. CE2&r. tyr w. %s of n. C&gly'%(d*14.28))
cmd.select('tyr47', 'n. CE2&r. tyr w. %s of n. CA&gly'%(d*13.35))
cmd.select('tyr48', 'n. CE2&r. tyr w. %s of n. N&gly'%(d*12.50))
cmd.select('tyr49', 'n. CZ&r. tyr w. %s of n. O&gly'%(d*14.71))
cmd.select('tyr50', 'n. CZ&r. tyr w. %s of n. C&gly'%(d*14.96))
cmd.select('tyr50',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27&br. tyr28&br. tyr29&br. tyr30&br. tyr31&br. tyr32&br. tyr33&br. tyr34&br. tyr35&br. tyr36&br. tyr37&br. tyr38&br. tyr39&br. tyr40&br. tyr41&br. tyr42&br. tyr43&br. tyr44&br. tyr45&br. tyr46&br. tyr47&br. tyr48&br. tyr49&br. tyr50')
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
cmd.delete('tyr28')
cmd.delete('tyr29')
cmd.delete('tyr30')
cmd.delete('tyr31')
cmd.delete('tyr32')
cmd.delete('tyr33')
cmd.delete('tyr34')
cmd.delete('tyr35')
cmd.delete('tyr36')
cmd.delete('tyr37')
cmd.delete('tyr38')
cmd.delete('tyr39')
cmd.delete('tyr40')
cmd.delete('tyr41')
cmd.delete('tyr42')
cmd.delete('tyr43')
cmd.delete('tyr44')
cmd.delete('tyr45')
cmd.delete('tyr46')
cmd.delete('tyr47')
cmd.delete('tyr48')
cmd.delete('tyr49')
cmd.select('tyr51', 'n. CZ&r. tyr w. %s of n. CA&gly'%(d*13.97))
cmd.select('tyr52', 'n. CZ&r. tyr w. %s of n. N&gly'%(d*13.24))
cmd.select('tyr53', 'n. OH&r. tyr w. %s of n. O&gly'%(d*16.03))
cmd.select('tyr54', 'n. OH&r. tyr w. %s of n. C&gly'%(d*16.24))
cmd.select('tyr55', 'n. OH&r. tyr w. %s of n. CA&gly'%(d*15.20))
cmd.select('tyr56', 'n. OH&r. tyr w. %s of n. N&gly'%(d*14.44))
cmd.select('tyr57', 'n. O&r. tyr w. %s of n. O&gly'%(d*11.72))
cmd.select('tyr58', 'n. O&r. tyr w. %s of n. C&gly'%(d*12.38))
cmd.select('tyr59', 'n. O&r. tyr w. %s of n. CA&gly'%(d*11.95))
cmd.select('tyr60', 'n. O&r. tyr w. %s of n. N&gly'%(d*11.20))
cmd.select('tyr61', 'n. C&r. tyr w. %s of n. O&gly'%(d*11.84))
cmd.select('tyr62', 'n. C&r. tyr w. %s of n. C&gly'%(d*12.51))
cmd.select('tyr63', 'n. C&r. tyr w. %s of n. CA&gly'%(d*12.05))
cmd.select('tyr64', 'n. C&r. tyr w. %s of n. N&gly'%(d*11.46))
cmd.select('tyr65', 'n. CA&r. tyr w. %s of n. O&gly'%(d*10.85))
cmd.select('tyr66', 'n. CA&r. tyr w. %s of n. C&gly'%(d*11.47))
cmd.select('tyr67', 'n. CA&r. tyr w. %s of n. CA&gly'%(d*10.93))
cmd.select('tyr68', 'n. CA&r. tyr w. %s of n. N&gly'%(d*10.46))
cmd.select('tyr69', 'n. N&r. tyr w. %s of n. O&gly'%(d*9.56))
cmd.select('tyr70', 'n. N&r. tyr w. %s of n. C&gly'%(d*10.27))
cmd.select('tyr71', 'n. N&r. tyr w. %s of n. CA&gly'%(d*9.88))
cmd.select('tyr72', 'n. N&r. tyr w. %s of n. N&gly'%(d*9.51))
cmd.select('tyr73', 'n. CB&r. tyr w. %s of n. CB&seri'%(d*11.54))
cmd.select('tyr74', 'n. CB&r. tyr w. %s of n. OG&seri'%(d*11.39))
cmd.select('tyr75', 'n. CG&r. tyr w. %s of n. CB&seri'%(d*12.50))
cmd.select('tyr76', 'n. CG&r. tyr w. %s of n. OG&seri'%(d*12.46))
cmd.select('tyr77', 'n. CD1&r. tyr w. %s of n. CB&seri'%(d*13.59))
cmd.select('tyr78', 'n. CD1&r. tyr w. %s of n. OG&seri'%(d*13.61))
cmd.select('tyr79', 'n. CD2&r. tyr w. %s of n. CB&seri'%(d*12.39))
cmd.select('tyr80', 'n. CD2&r. tyr w. %s of n. OG&seri'%(d*12.38))
cmd.select('tyr81', 'n. CE1&r. tyr w. %s of n. CB&seri'%(d*14.55))
cmd.select('tyr82', 'n. CE1&r. tyr w. %s of n. OG&seri'%(d*14.66))
cmd.select('tyr83', 'n. CE2&r. tyr w. %s of n. CB&seri'%(d*13.43))
cmd.select('tyr84', 'n. CE2&r. tyr w. %s of n. OG&seri'%(d*13.51))
cmd.select('tyr85', 'n. CZ&r. tyr w. %s of n. CB&seri'%(d*14.45))
cmd.select('tyr86', 'n. CZ&r. tyr w. %s of n. OG&seri'%(d*14.57))
cmd.select('tyr87', 'n. OH&r. tyr w. %s of n. CB&seri'%(d*15.52))
cmd.select('tyr88', 'n. OH&r. tyr w. %s of n. OG&seri'%(d*15.71))
cmd.select('tyr89', 'n. O&r. tyr w. %s of n. CB&seri'%(d*12.15))
cmd.select('tyr90', 'n. O&r. tyr w. %s of n. OG&seri'%(d*11.71))
cmd.select('tyr91', 'n. C&r. tyr w. %s of n. CB&seri'%(d*12.80))
cmd.select('tyr92', 'n. C&r. tyr w. %s of n. OG&seri'%(d*12.37))
cmd.select('tyr93', 'n. CA&r. tyr w. %s of n. CB&seri'%(d*12.23))
cmd.select('tyr94', 'n. CA&r. tyr w. %s of n. OG&seri'%(d*11.88))
cmd.select('tyr95', 'n. N&r. tyr w. %s of n. CB&seri'%(d*11.40))
cmd.select('tyr96', 'n. N&r. tyr w. %s of n. OG&seri'%(d*10.93))
cmd.select('tyr97', 'n. CB&r. tyr w. %s of n. CB&asn'%(d*8.57))
cmd.select('tyr98', 'n. CB&r. tyr w. %s of n. CG&asn'%(d*7.57))
cmd.select('tyr99', 'n. CB&r. tyr w. %s of n. OD1&asn'%(d*8.12))
cmd.select('tyr100', 'n. CB&r. tyr w. %s of n. ND2&asn'%(d*6.33))
cmd.select('tyr100',' br. tyr51&br. tyr52&br. tyr53&br. tyr54&br. tyr55&br. tyr56&br. tyr57&br. tyr58&br. tyr59&br. tyr60&br. tyr61&br. tyr62&br. tyr63&br. tyr64&br. tyr65&br. tyr66&br. tyr67&br. tyr68&br. tyr69&br. tyr70&br. tyr71&br. tyr72&br. tyr73&br. tyr74&br. tyr75&br. tyr76&br. tyr77&br. tyr78&br. tyr79&br. tyr80&br. tyr81&br. tyr82&br. tyr83&br. tyr84&br. tyr85&br. tyr86&br. tyr87&br. tyr88&br. tyr89&br. tyr90&br. tyr91&br. tyr92&br. tyr93&br. tyr94&br. tyr95&br. tyr96&br. tyr97&br. tyr98&br. tyr99&br. tyr100')
cmd.delete('tyr51')
cmd.delete('tyr52')
cmd.delete('tyr53')
cmd.delete('tyr54')
cmd.delete('tyr55')
cmd.delete('tyr56')
cmd.delete('tyr57')
cmd.delete('tyr58')
cmd.delete('tyr59')
cmd.delete('tyr60')
cmd.delete('tyr61')
cmd.delete('tyr62')
cmd.delete('tyr63')
cmd.delete('tyr64')
cmd.delete('tyr65')
cmd.delete('tyr66')
cmd.delete('tyr67')
cmd.delete('tyr68')
cmd.delete('tyr69')
cmd.delete('tyr70')
cmd.delete('tyr71')
cmd.delete('tyr72')
cmd.delete('tyr73')
cmd.delete('tyr74')
cmd.delete('tyr75')
cmd.delete('tyr76')
cmd.delete('tyr77')
cmd.delete('tyr78')
cmd.delete('tyr79')
cmd.delete('tyr80')
cmd.delete('tyr81')
cmd.delete('tyr82')
cmd.delete('tyr83')
cmd.delete('tyr84')
cmd.delete('tyr85')
cmd.delete('tyr86')
cmd.delete('tyr87')
cmd.delete('tyr88')
cmd.delete('tyr89')
cmd.delete('tyr90')
cmd.delete('tyr91')
cmd.delete('tyr92')
cmd.delete('tyr93')
cmd.delete('tyr94')
cmd.delete('tyr95')
cmd.delete('tyr96')
cmd.delete('tyr97')
cmd.delete('tyr98')
cmd.delete('tyr99')
cmd.select('tyr101', 'n. CG&r. tyr w. %s of n. CB&asn'%(d*9.70))
cmd.select('tyr102', 'n. CG&r. tyr w. %s of n. CG&asn'%(d*8.52))
cmd.select('tyr103', 'n. CG&r. tyr w. %s of n. OD1&asn'%(d*8.86))
cmd.select('tyr104', 'n. CG&r. tyr w. %s of n. ND2&asn'%(d*7.34))
cmd.select('tyr105', 'n. CD1&r. tyr w. %s of n. CB&asn'%(d*10.93))
cmd.select('tyr106', 'n. CD1&r. tyr w. %s of n. CG&asn'%(d*9.78))
cmd.select('tyr107', 'n. CD1&r. tyr w. %s of n. OD1&asn'%(d*10.10))
cmd.select('tyr108', 'n. CD1&r. tyr w. %s of n. ND2&asn'%(d*8.62))
cmd.select('tyr109', 'n. CD2&r. tyr w. %s of n. CB&asn'%(d*9.68))
cmd.select('tyr110', 'n. CD2&r. tyr w. %s of n. CG&asn'%(d*8.35))
cmd.select('tyr111', 'n. CD2&r. tyr w. %s of n. OD1&asn'%(d*8.52))
cmd.select('tyr112', 'n. CD2&r. tyr w. %s of n. ND2&asn'%(d*7.23))
cmd.select('tyr113', 'n. CE1&r. tyr w. %s of n. CB&asn'%(d*12.03))
cmd.select('tyr114', 'n. CE1&r. tyr w. %s of n. CG&asn'%(d*10.79))
cmd.select('tyr115', 'n. CE1&r. tyr w. %s of n. OD1&asn'%(d*10.96))
cmd.select('tyr116', 'n. CE1&r. tyr w. %s of n. ND2&asn'%(d*9.67))
cmd.select('tyr117', 'n. CE2&r. tyr w. %s of n. CB&asn'%(d*10.91))
cmd.select('tyr118', 'n. CE2&r. tyr w. %s of n. CG&asn'%(d*9.52))
cmd.select('tyr119', 'n. CE2&r. tyr w. %s of n. OD1&asn'%(d*9.54))
cmd.select('tyr120', 'n. CE2&r. tyr w. %s of n. ND2&asn'%(d*8.48))
cmd.select('tyr121', 'n. CZ&r. tyr w. %s of n. CB&asn'%(d*11.98))
cmd.select('tyr122', 'n. CZ&r. tyr w. %s of n. CG&asn'%(d*10.63))
cmd.select('tyr123', 'n. CZ&r. tyr w. %s of n. OD1&asn'%(d*10.68))
cmd.select('tyr124', 'n. CZ&r. tyr w. %s of n. ND2&asn'%(d*9.57))
cmd.select('tyr125', 'n. OH&r. tyr w. %s of n. CB&asn'%(d*13.21))
cmd.select('tyr126', 'n. OH&r. tyr w. %s of n. CG&asn'%(d*11.82))
cmd.select('tyr127', 'n. OH&r. tyr w. %s of n. OD1&asn'%(d*11.77))
cmd.select('tyr128', 'n. OH&r. tyr w. %s of n. ND2&asn'%(d*10.80))
cmd.select('tyr129', 'n. O&r. tyr w. %s of n. CB&asn'%(d*6.97))
cmd.select('tyr130', 'n. O&r. tyr w. %s of n. CG&asn'%(d*5.63))
cmd.select('tyr131', 'n. O&r. tyr w. %s of n. OD1&asn'%(d*5.72))
cmd.select('tyr132', 'n. O&r. tyr w. %s of n. ND2&asn'%(d*4.85))
cmd.select('tyr133', 'n. C&r. tyr w. %s of n. CB&asn'%(d*7.63))
cmd.select('tyr134', 'n. C&r. tyr w. %s of n. CG&asn'%(d*6.47))
cmd.select('tyr135', 'n. C&r. tyr w. %s of n. OD1&asn'%(d*6.65))
cmd.select('tyr136', 'n. C&r. tyr w. %s of n. ND2&asn'%(d*5.67))
cmd.select('tyr137', 'n. CA&r. tyr w. %s of n. CB&asn'%(d*7.96))
cmd.select('tyr138', 'n. CA&r. tyr w. %s of n. CG&asn'%(d*7.03))
cmd.select('tyr139', 'n. CA&r. tyr w. %s of n. OD1&asn'%(d*7.53))
cmd.select('tyr140', 'n. CA&r. tyr w. %s of n. ND2&asn'%(d*6.00))
cmd.select('tyr141', 'n. N&r. tyr w. %s of n. CB&asn'%(d*7.07))
cmd.select('tyr142', 'n. N&r. tyr w. %s of n. CG&asn'%(d*6.46))
cmd.select('tyr143', 'n. N&r. tyr w. %s of n. OD1&asn'%(d*7.22))
cmd.select('tyr144', 'n. N&r. tyr w. %s of n. ND2&asn'%(d*5.47))
cmd.select('tyr',' tyr50&tyr100&br. tyr101&br. tyr102&br. tyr103&br. tyr104&br. tyr105&br. tyr106&br. tyr107&br. tyr108&br. tyr109&br. tyr110&br. tyr111&br. tyr112&br. tyr113&br. tyr114&br. tyr115&br. tyr116&br. tyr117&br. tyr118&br. tyr119&br. tyr120&br. tyr121&br. tyr122&br. tyr123&br. tyr124&br. tyr125&br. tyr126&br. tyr127&br. tyr128&br. tyr129&br. tyr130&br. tyr131&br. tyr132&br. tyr133&br. tyr134&br. tyr135&br. tyr136&br. tyr137&br. tyr138&br. tyr139&br. tyr140&br. tyr141&br. tyr142&br. tyr143&br. tyr144')
cmd.delete('tyr50')
cmd.delete('tyr100')
cmd.delete('tyr101')
cmd.delete('tyr102')
cmd.delete('tyr103')
cmd.delete('tyr104')
cmd.delete('tyr105')
cmd.delete('tyr106')
cmd.delete('tyr107')
cmd.delete('tyr108')
cmd.delete('tyr109')
cmd.delete('tyr110')
cmd.delete('tyr111')
cmd.delete('tyr112')
cmd.delete('tyr113')
cmd.delete('tyr114')
cmd.delete('tyr115')
cmd.delete('tyr116')
cmd.delete('tyr117')
cmd.delete('tyr118')
cmd.delete('tyr119')
cmd.delete('tyr120')
cmd.delete('tyr121')
cmd.delete('tyr122')
cmd.delete('tyr123')
cmd.delete('tyr124')
cmd.delete('tyr125')
cmd.delete('tyr126')
cmd.delete('tyr127')
cmd.delete('tyr128')
cmd.delete('tyr129')
cmd.delete('tyr130')
cmd.delete('tyr131')
cmd.delete('tyr132')
cmd.delete('tyr133')
cmd.delete('tyr134')
cmd.delete('tyr135')
cmd.delete('tyr136')
cmd.delete('tyr137')
cmd.delete('tyr138')
cmd.delete('tyr139')
cmd.delete('tyr140')
cmd.delete('tyr141')
cmd.delete('tyr142')
cmd.delete('tyr143')
cmd.delete('tyr144')
cmd.select('A_1b65-Y146A-N218A-S250A-S288A-G289A', 'ser|gly|seri|asn|tyr')
cmd.delete('ser')
cmd.delete('gly')
cmd.delete('seri')
cmd.delete('asn')
cmd.delete('tyr')
