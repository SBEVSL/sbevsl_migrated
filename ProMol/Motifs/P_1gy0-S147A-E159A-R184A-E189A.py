'''
FUNC:P_1gy0-S147A-E159A-R184A-E189A
PDB:1gy0
EC:2.4.2.31
PFAM:PF01129
RESI:ser,glu,arg,glu
LOCI:a-147,159,184,189;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*13.58))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*14.64))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*15.34))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*14.74))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*16.59))
cmd.select('ser6', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*12.74))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*13.88))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*14.54))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*13.92))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*15.77))
cmd.select('ser11', 'n. CB&r. ser w. %s of n. CB&r. arg'%(d*12.64))
cmd.select('ser12', 'n. CB&r. ser w. %s of n. CG&r. arg'%(d*13.18))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. CD&r. arg'%(d*13.09))
cmd.select('ser14', 'n. CB&r. ser w. %s of n. NE&r. arg'%(d*14.03))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. CZ&r. arg'%(d*14.36))
cmd.select('ser16', 'n. CB&r. ser w. %s of n. NH1&r. arg'%(d*13.84))
cmd.select('ser17', 'n. CB&r. ser w. %s of n. NH2&r. arg'%(d*15.35))
cmd.select('ser18', 'n. OG&r. ser w. %s of n. CB&r. arg'%(d*12.75))
cmd.select('ser19', 'n. OG&r. ser w. %s of n. CG&r. arg'%(d*13.14))
cmd.select('ser20', 'n. OG&r. ser w. %s of n. CD&r. arg'%(d*12.87))
cmd.select('ser21', 'n. OG&r. ser w. %s of n. NE&r. arg'%(d*13.70))
cmd.select('ser22', 'n. OG&r. ser w. %s of n. CZ&r. arg'%(d*13.89))
cmd.select('ser23', 'n. OG&r. ser w. %s of n. NH1&r. arg'%(d*13.31))
cmd.select('ser24', 'n. OG&r. ser w. %s of n. NH2&r. arg'%(d*14.81))
cmd.select('ser25', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*7.40))
cmd.select('ser26', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*5.92))
cmd.select('ser27', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*5.66))
cmd.select('ser28', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*6.27))
cmd.select('ser29', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*5.43))
cmd.select('ser30', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*8.46))
cmd.select('ser31', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*7.05))
cmd.select('ser32', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*6.64))
cmd.select('ser33', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*6.96))
cmd.select('ser34', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*6.51))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27&br. ser28&br. ser29&br. ser30&br. ser31&br. ser32&br. ser33&br. ser34')
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
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*13.58))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*12.74))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*14.64))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*13.88))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*15.34))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*14.54))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*14.74))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*13.92))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*16.59))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*15.77))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&r. arg'%(d*11.24))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. CG&r. arg'%(d*11.03))
cmd.select('glu13', 'n. CB&r. glu w. %s of n. CD&r. arg'%(d*9.60))
cmd.select('glu14', 'n. CB&r. glu w. %s of n. NE&r. arg'%(d*9.73))
cmd.select('glu15', 'n. CB&r. glu w. %s of n. CZ&r. arg'%(d*8.85))
cmd.select('glu16', 'n. CB&r. glu w. %s of n. NH1&r. arg'%(d*7.54))
cmd.select('glu17', 'n. CB&r. glu w. %s of n. NH2&r. arg'%(d*9.46))
cmd.select('glu18', 'n. CG&r. glu w. %s of n. CB&r. arg'%(d*10.89))
cmd.select('glu19', 'n. CG&r. glu w. %s of n. CG&r. arg'%(d*10.61))
cmd.select('glu20', 'n. CG&r. glu w. %s of n. CD&r. arg'%(d*9.16))
cmd.select('glu21', 'n. CG&r. glu w. %s of n. NE&r. arg'%(d*9.20))
cmd.select('glu22', 'n. CG&r. glu w. %s of n. CZ&r. arg'%(d*8.27))
cmd.select('glu23', 'n. CG&r. glu w. %s of n. NH1&r. arg'%(d*6.99))
cmd.select('glu24', 'n. CG&r. glu w. %s of n. NH2&r. arg'%(d*8.83))
cmd.select('glu25', 'n. CD&r. glu w. %s of n. CB&r. arg'%(d*11.02))
cmd.select('glu26', 'n. CD&r. glu w. %s of n. CG&r. arg'%(d*10.50))
cmd.select('glu27', 'n. CD&r. glu w. %s of n. CD&r. arg'%(d*9.00))
cmd.select('glu28', 'n. CD&r. glu w. %s of n. NE&r. arg'%(d*8.73))
cmd.select('glu29', 'n. CD&r. glu w. %s of n. CZ&r. arg'%(d*7.63))
cmd.select('glu30', 'n. CD&r. glu w. %s of n. NH1&r. arg'%(d*6.46))
cmd.select('glu31', 'n. CD&r. glu w. %s of n. NH2&r. arg'%(d*7.91))
cmd.select('glu32', 'n. OE1&r. glu w. %s of n. CB&r. arg'%(d*10.41))
cmd.select('glu33', 'n. OE1&r. glu w. %s of n. CG&r. arg'%(d*9.76))
cmd.select('glu34', 'n. OE1&r. glu w. %s of n. CD&r. arg'%(d*8.25))
cmd.select('glu35', 'n. OE1&r. glu w. %s of n. NE&r. arg'%(d*7.87))
cmd.select('glu36', 'n. OE1&r. glu w. %s of n. CZ&r. arg'%(d*6.70))
cmd.select('glu37', 'n. OE1&r. glu w. %s of n. NH1&r. arg'%(d*5.58))
cmd.select('glu38', 'n. OE1&r. glu w. %s of n. NH2&r. arg'%(d*6.94))
cmd.select('glu39', 'n. OE2&r. glu w. %s of n. CB&r. arg'%(d*11.94))
cmd.select('glu40', 'n. OE2&r. glu w. %s of n. CG&r. arg'%(d*11.36))
cmd.select('glu41', 'n. OE2&r. glu w. %s of n. CD&r. arg'%(d*9.88))
cmd.select('glu42', 'n. OE2&r. glu w. %s of n. NE&r. arg'%(d*9.49))
cmd.select('glu43', 'n. OE2&r. glu w. %s of n. CZ&r. arg'%(d*8.32))
cmd.select('glu44', 'n. OE2&r. glu w. %s of n. NH1&r. arg'%(d*7.29))
cmd.select('glu45', 'n. OE2&r. glu w. %s of n. NH2&r. arg'%(d*8.42))
cmd.select('glu46', 'n. CB&r. glu w. %s of n. CB&r. glu'%(d*14.14))
cmd.select('glu47', 'n. CB&r. glu w. %s of n. CG&r. glu'%(d*14.03))
cmd.select('glu48', 'n. CB&r. glu w. %s of n. CD&r. glu'%(d*13.75))
cmd.select('glu49', 'n. CB&r. glu w. %s of n. OE1&r. glu'%(d*12.81))
cmd.select('glu50', 'n. CB&r. glu w. %s of n. OE2&r. glu'%(d*14.60))
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
cmd.select('glu51', 'n. CG&r. glu w. %s of n. CB&r. glu'%(d*14.67))
cmd.select('glu52', 'n. CG&r. glu w. %s of n. CG&r. glu'%(d*14.72))
cmd.select('glu53', 'n. CG&r. glu w. %s of n. CD&r. glu'%(d*14.43))
cmd.select('glu54', 'n. CG&r. glu w. %s of n. OE1&r. glu'%(d*13.41))
cmd.select('glu55', 'n. CG&r. glu w. %s of n. OE2&r. glu'%(d*15.33))
cmd.select('glu56', 'n. CD&r. glu w. %s of n. CB&r. glu'%(d*15.51))
cmd.select('glu57', 'n. CD&r. glu w. %s of n. CG&r. glu'%(d*15.53))
cmd.select('glu58', 'n. CD&r. glu w. %s of n. CD&r. glu'%(d*15.08))
cmd.select('glu59', 'n. CD&r. glu w. %s of n. OE1&r. glu'%(d*14.01))
cmd.select('glu60', 'n. CD&r. glu w. %s of n. OE2&r. glu'%(d*15.92))
cmd.select('glu61', 'n. OE1&r. glu w. %s of n. CB&r. glu'%(d*15.07))
cmd.select('glu62', 'n. OE1&r. glu w. %s of n. CG&r. glu'%(d*15.02))
cmd.select('glu63', 'n. OE1&r. glu w. %s of n. CD&r. glu'%(d*14.45))
cmd.select('glu64', 'n. OE1&r. glu w. %s of n. OE1&r. glu'%(d*13.36))
cmd.select('glu65', 'n. OE1&r. glu w. %s of n. OE2&r. glu'%(d*15.22))
cmd.select('glu66', 'n. OE2&r. glu w. %s of n. CB&r. glu'%(d*16.71))
cmd.select('glu67', 'n. OE2&r. glu w. %s of n. CG&r. glu'%(d*16.76))
cmd.select('glu68', 'n. OE2&r. glu w. %s of n. CD&r. glu'%(d*16.32))
cmd.select('glu69', 'n. OE2&r. glu w. %s of n. OE1&r. glu'%(d*15.24))
cmd.select('glu70', 'n. OE2&r. glu w. %s of n. OE2&r. glu'%(d*17.16))
cmd.select('glu',' glu50&br. glu51&br. glu52&br. glu53&br. glu54&br. glu55&br. glu56&br. glu57&br. glu58&br. glu59&br. glu60&br. glu61&br. glu62&br. glu63&br. glu64&br. glu65&br. glu66&br. glu67&br. glu68&br. glu69&br. glu70')
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
cmd.delete('glu61')
cmd.delete('glu62')
cmd.delete('glu63')
cmd.delete('glu64')
cmd.delete('glu65')
cmd.delete('glu66')
cmd.delete('glu67')
cmd.delete('glu68')
cmd.delete('glu69')
cmd.delete('glu70')
cmd.select('arg1', 'n. CB&r. arg w. %s of n. CB&ser'%(d*12.64))
cmd.select('arg2', 'n. CB&r. arg w. %s of n. OG&ser'%(d*12.75))
cmd.select('arg3', 'n. CG&r. arg w. %s of n. CB&ser'%(d*13.18))
cmd.select('arg4', 'n. CG&r. arg w. %s of n. OG&ser'%(d*13.14))
cmd.select('arg5', 'n. CD&r. arg w. %s of n. CB&ser'%(d*13.09))
cmd.select('arg6', 'n. CD&r. arg w. %s of n. OG&ser'%(d*12.87))
cmd.select('arg7', 'n. NE&r. arg w. %s of n. CB&ser'%(d*14.03))
cmd.select('arg8', 'n. NE&r. arg w. %s of n. OG&ser'%(d*13.70))
cmd.select('arg9', 'n. CZ&r. arg w. %s of n. CB&ser'%(d*14.36))
cmd.select('arg10', 'n. CZ&r. arg w. %s of n. OG&ser'%(d*13.89))
cmd.select('arg11', 'n. NH1&r. arg w. %s of n. CB&ser'%(d*13.84))
cmd.select('arg12', 'n. NH1&r. arg w. %s of n. OG&ser'%(d*13.31))
cmd.select('arg13', 'n. NH2&r. arg w. %s of n. CB&ser'%(d*15.35))
cmd.select('arg14', 'n. NH2&r. arg w. %s of n. OG&ser'%(d*14.81))
cmd.select('arg15', 'n. CB&r. arg w. %s of n. CB&glu'%(d*11.24))
cmd.select('arg16', 'n. CB&r. arg w. %s of n. CG&glu'%(d*10.89))
cmd.select('arg17', 'n. CB&r. arg w. %s of n. CD&glu'%(d*11.02))
cmd.select('arg18', 'n. CB&r. arg w. %s of n. OE1&glu'%(d*10.41))
cmd.select('arg19', 'n. CB&r. arg w. %s of n. OE2&glu'%(d*11.94))
cmd.select('arg20', 'n. CG&r. arg w. %s of n. CB&glu'%(d*11.03))
cmd.select('arg21', 'n. CG&r. arg w. %s of n. CG&glu'%(d*10.61))
cmd.select('arg22', 'n. CG&r. arg w. %s of n. CD&glu'%(d*10.50))
cmd.select('arg23', 'n. CG&r. arg w. %s of n. OE1&glu'%(d*9.76))
cmd.select('arg24', 'n. CG&r. arg w. %s of n. OE2&glu'%(d*11.36))
cmd.select('arg25', 'n. CD&r. arg w. %s of n. CB&glu'%(d*9.60))
cmd.select('arg26', 'n. CD&r. arg w. %s of n. CG&glu'%(d*9.16))
cmd.select('arg27', 'n. CD&r. arg w. %s of n. CD&glu'%(d*9.00))
cmd.select('arg28', 'n. CD&r. arg w. %s of n. OE1&glu'%(d*8.25))
cmd.select('arg29', 'n. CD&r. arg w. %s of n. OE2&glu'%(d*9.88))
cmd.select('arg30', 'n. NE&r. arg w. %s of n. CB&glu'%(d*9.73))
cmd.select('arg31', 'n. NE&r. arg w. %s of n. CG&glu'%(d*9.20))
cmd.select('arg32', 'n. NE&r. arg w. %s of n. CD&glu'%(d*8.73))
cmd.select('arg33', 'n. NE&r. arg w. %s of n. OE1&glu'%(d*7.87))
cmd.select('arg34', 'n. NE&r. arg w. %s of n. OE2&glu'%(d*9.49))
cmd.select('arg35', 'n. CZ&r. arg w. %s of n. CB&glu'%(d*8.85))
cmd.select('arg36', 'n. CZ&r. arg w. %s of n. CG&glu'%(d*8.27))
cmd.select('arg37', 'n. CZ&r. arg w. %s of n. CD&glu'%(d*7.63))
cmd.select('arg38', 'n. CZ&r. arg w. %s of n. OE1&glu'%(d*6.70))
cmd.select('arg39', 'n. CZ&r. arg w. %s of n. OE2&glu'%(d*8.32))
cmd.select('arg40', 'n. NH1&r. arg w. %s of n. CB&glu'%(d*7.54))
cmd.select('arg41', 'n. NH1&r. arg w. %s of n. CG&glu'%(d*6.99))
cmd.select('arg42', 'n. NH1&r. arg w. %s of n. CD&glu'%(d*6.46))
cmd.select('arg43', 'n. NH1&r. arg w. %s of n. OE1&glu'%(d*5.58))
cmd.select('arg44', 'n. NH1&r. arg w. %s of n. OE2&glu'%(d*7.29))
cmd.select('arg45', 'n. NH2&r. arg w. %s of n. CB&glu'%(d*9.46))
cmd.select('arg46', 'n. NH2&r. arg w. %s of n. CG&glu'%(d*8.83))
cmd.select('arg47', 'n. NH2&r. arg w. %s of n. CD&glu'%(d*7.91))
cmd.select('arg48', 'n. NH2&r. arg w. %s of n. OE1&glu'%(d*6.94))
cmd.select('arg49', 'n. NH2&r. arg w. %s of n. OE2&glu'%(d*8.42))
cmd.select('arg50', 'n. CB&r. arg w. %s of n. CB&r. glu'%(d*10.00))
cmd.select('arg50',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27&br. arg28&br. arg29&br. arg30&br. arg31&br. arg32&br. arg33&br. arg34&br. arg35&br. arg36&br. arg37&br. arg38&br. arg39&br. arg40&br. arg41&br. arg42&br. arg43&br. arg44&br. arg45&br. arg46&br. arg47&br. arg48&br. arg49&br. arg50')
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
cmd.delete('arg28')
cmd.delete('arg29')
cmd.delete('arg30')
cmd.delete('arg31')
cmd.delete('arg32')
cmd.delete('arg33')
cmd.delete('arg34')
cmd.delete('arg35')
cmd.delete('arg36')
cmd.delete('arg37')
cmd.delete('arg38')
cmd.delete('arg39')
cmd.delete('arg40')
cmd.delete('arg41')
cmd.delete('arg42')
cmd.delete('arg43')
cmd.delete('arg44')
cmd.delete('arg45')
cmd.delete('arg46')
cmd.delete('arg47')
cmd.delete('arg48')
cmd.delete('arg49')
cmd.select('arg51', 'n. CB&r. arg w. %s of n. CG&r. glu'%(d*10.64))
cmd.select('arg52', 'n. CB&r. arg w. %s of n. CD&r. glu'%(d*10.00))
cmd.select('arg53', 'n. CB&r. arg w. %s of n. OE1&r. glu'%(d*8.81))
cmd.select('arg54', 'n. CB&r. arg w. %s of n. OE2&r. glu'%(d*10.85))
cmd.select('arg55', 'n. CG&r. arg w. %s of n. CB&r. glu'%(d*11.14))
cmd.select('arg56', 'n. CG&r. arg w. %s of n. CG&r. glu'%(d*11.60))
cmd.select('arg57', 'n. CG&r. arg w. %s of n. CD&r. glu'%(d*10.80))
cmd.select('arg58', 'n. CG&r. arg w. %s of n. OE1&r. glu'%(d*9.57))
cmd.select('arg59', 'n. CG&r. arg w. %s of n. OE2&r. glu'%(d*11.53))
cmd.select('arg60', 'n. CD&r. arg w. %s of n. CB&r. glu'%(d*11.54))
cmd.select('arg61', 'n. CD&r. arg w. %s of n. CG&r. glu'%(d*11.89))
cmd.select('arg62', 'n. CD&r. arg w. %s of n. CD&r. glu'%(d*11.12))
cmd.select('arg63', 'n. CD&r. arg w. %s of n. OE1&r. glu'%(d*9.86))
cmd.select('arg64', 'n. CD&r. arg w. %s of n. OE2&r. glu'%(d*11.89))
cmd.select('arg65', 'n. NE&r. arg w. %s of n. CB&r. glu'%(d*12.87))
cmd.select('arg66', 'n. NE&r. arg w. %s of n. CG&r. glu'%(d*13.13))
cmd.select('arg67', 'n. NE&r. arg w. %s of n. CD&r. glu'%(d*12.26))
cmd.select('arg68', 'n. NE&r. arg w. %s of n. OE1&r. glu'%(d*11.01))
cmd.select('arg69', 'n. NE&r. arg w. %s of n. OE2&r. glu'%(d*12.95))
cmd.select('arg70', 'n. CZ&r. arg w. %s of n. CB&r. glu'%(d*13.62))
cmd.select('arg71', 'n. CZ&r. arg w. %s of n. CG&r. glu'%(d*13.78))
cmd.select('arg72', 'n. CZ&r. arg w. %s of n. CD&r. glu'%(d*12.94))
cmd.select('arg73', 'n. CZ&r. arg w. %s of n. OE1&r. glu'%(d*11.69))
cmd.select('arg74', 'n. CZ&r. arg w. %s of n. OE2&r. glu'%(d*13.62))
cmd.select('arg75', 'n. NH1&r. arg w. %s of n. CB&r. glu'%(d*13.26))
cmd.select('arg76', 'n. NH1&r. arg w. %s of n. CG&r. glu'%(d*13.39))
cmd.select('arg77', 'n. NH1&r. arg w. %s of n. CD&r. glu'%(d*12.65))
cmd.select('arg78', 'n. NH1&r. arg w. %s of n. OE1&r. glu'%(d*11.43))
cmd.select('arg79', 'n. NH1&r. arg w. %s of n. OE2&r. glu'%(d*13.41))
cmd.select('arg80', 'n. NH2&r. arg w. %s of n. CB&r. glu'%(d*14.84))
cmd.select('arg81', 'n. NH2&r. arg w. %s of n. CG&r. glu'%(d*14.96))
cmd.select('arg82', 'n. NH2&r. arg w. %s of n. CD&r. glu'%(d*14.04))
cmd.select('arg83', 'n. NH2&r. arg w. %s of n. OE1&r. glu'%(d*12.80))
cmd.select('arg84', 'n. NH2&r. arg w. %s of n. OE2&r. glu'%(d*14.66))
cmd.select('arg',' arg50&br. arg51&br. arg52&br. arg53&br. arg54&br. arg55&br. arg56&br. arg57&br. arg58&br. arg59&br. arg60&br. arg61&br. arg62&br. arg63&br. arg64&br. arg65&br. arg66&br. arg67&br. arg68&br. arg69&br. arg70&br. arg71&br. arg72&br. arg73&br. arg74&br. arg75&br. arg76&br. arg77&br. arg78&br. arg79&br. arg80&br. arg81&br. arg82&br. arg83&br. arg84')
cmd.delete('arg50')
cmd.delete('arg51')
cmd.delete('arg52')
cmd.delete('arg53')
cmd.delete('arg54')
cmd.delete('arg55')
cmd.delete('arg56')
cmd.delete('arg57')
cmd.delete('arg58')
cmd.delete('arg59')
cmd.delete('arg60')
cmd.delete('arg61')
cmd.delete('arg62')
cmd.delete('arg63')
cmd.delete('arg64')
cmd.delete('arg65')
cmd.delete('arg66')
cmd.delete('arg67')
cmd.delete('arg68')
cmd.delete('arg69')
cmd.delete('arg70')
cmd.delete('arg71')
cmd.delete('arg72')
cmd.delete('arg73')
cmd.delete('arg74')
cmd.delete('arg75')
cmd.delete('arg76')
cmd.delete('arg77')
cmd.delete('arg78')
cmd.delete('arg79')
cmd.delete('arg80')
cmd.delete('arg81')
cmd.delete('arg82')
cmd.delete('arg83')
cmd.delete('arg84')
cmd.select('glui1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*7.40))
cmd.select('glui2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*8.46))
cmd.select('glui3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*5.92))
cmd.select('glui4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*7.05))
cmd.select('glui5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*5.66))
cmd.select('glui6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*6.64))
cmd.select('glui7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*6.27))
cmd.select('glui8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*6.96))
cmd.select('glui9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*5.43))
cmd.select('glui10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*6.51))
cmd.select('glui11', 'n. CB&r. glu w. %s of n. CB&glu'%(d*14.14))
cmd.select('glui12', 'n. CB&r. glu w. %s of n. CG&glu'%(d*14.67))
cmd.select('glui13', 'n. CB&r. glu w. %s of n. CD&glu'%(d*15.51))
cmd.select('glui14', 'n. CB&r. glu w. %s of n. OE1&glu'%(d*15.07))
cmd.select('glui15', 'n. CB&r. glu w. %s of n. OE2&glu'%(d*16.71))
cmd.select('glui16', 'n. CG&r. glu w. %s of n. CB&glu'%(d*14.03))
cmd.select('glui17', 'n. CG&r. glu w. %s of n. CG&glu'%(d*14.72))
cmd.select('glui18', 'n. CG&r. glu w. %s of n. CD&glu'%(d*15.53))
cmd.select('glui19', 'n. CG&r. glu w. %s of n. OE1&glu'%(d*15.02))
cmd.select('glui20', 'n. CG&r. glu w. %s of n. OE2&glu'%(d*16.76))
cmd.select('glui21', 'n. CD&r. glu w. %s of n. CB&glu'%(d*13.75))
cmd.select('glui22', 'n. CD&r. glu w. %s of n. CG&glu'%(d*14.43))
cmd.select('glui23', 'n. CD&r. glu w. %s of n. CD&glu'%(d*15.08))
cmd.select('glui24', 'n. CD&r. glu w. %s of n. OE1&glu'%(d*14.45))
cmd.select('glui25', 'n. CD&r. glu w. %s of n. OE2&glu'%(d*16.32))
cmd.select('glui26', 'n. OE1&r. glu w. %s of n. CB&glu'%(d*12.81))
cmd.select('glui27', 'n. OE1&r. glu w. %s of n. CG&glu'%(d*13.41))
cmd.select('glui28', 'n. OE1&r. glu w. %s of n. CD&glu'%(d*14.01))
cmd.select('glui29', 'n. OE1&r. glu w. %s of n. OE1&glu'%(d*13.36))
cmd.select('glui30', 'n. OE1&r. glu w. %s of n. OE2&glu'%(d*15.24))
cmd.select('glui31', 'n. OE2&r. glu w. %s of n. CB&glu'%(d*14.60))
cmd.select('glui32', 'n. OE2&r. glu w. %s of n. CG&glu'%(d*15.33))
cmd.select('glui33', 'n. OE2&r. glu w. %s of n. CD&glu'%(d*15.92))
cmd.select('glui34', 'n. OE2&r. glu w. %s of n. OE1&glu'%(d*15.22))
cmd.select('glui35', 'n. OE2&r. glu w. %s of n. OE2&glu'%(d*17.16))
cmd.select('glui36', 'n. CB&r. glu w. %s of n. CB&arg'%(d*10.00))
cmd.select('glui37', 'n. CB&r. glu w. %s of n. CG&arg'%(d*11.14))
cmd.select('glui38', 'n. CB&r. glu w. %s of n. CD&arg'%(d*11.54))
cmd.select('glui39', 'n. CB&r. glu w. %s of n. NE&arg'%(d*12.87))
cmd.select('glui40', 'n. CB&r. glu w. %s of n. CZ&arg'%(d*13.62))
cmd.select('glui41', 'n. CB&r. glu w. %s of n. NH1&arg'%(d*13.26))
cmd.select('glui42', 'n. CB&r. glu w. %s of n. NH2&arg'%(d*14.84))
cmd.select('glui43', 'n. CG&r. glu w. %s of n. CB&arg'%(d*10.64))
cmd.select('glui44', 'n. CG&r. glu w. %s of n. CG&arg'%(d*11.60))
cmd.select('glui45', 'n. CG&r. glu w. %s of n. CD&arg'%(d*11.89))
cmd.select('glui46', 'n. CG&r. glu w. %s of n. NE&arg'%(d*13.13))
cmd.select('glui47', 'n. CG&r. glu w. %s of n. CZ&arg'%(d*13.78))
cmd.select('glui48', 'n. CG&r. glu w. %s of n. NH1&arg'%(d*13.39))
cmd.select('glui49', 'n. CG&r. glu w. %s of n. NH2&arg'%(d*14.96))
cmd.select('glui50', 'n. CD&r. glu w. %s of n. CB&arg'%(d*10.00))
cmd.select('glui50',' br. glui1&br. glui2&br. glui3&br. glui4&br. glui5&br. glui6&br. glui7&br. glui8&br. glui9&br. glui10&br. glui11&br. glui12&br. glui13&br. glui14&br. glui15&br. glui16&br. glui17&br. glui18&br. glui19&br. glui20&br. glui21&br. glui22&br. glui23&br. glui24&br. glui25&br. glui26&br. glui27&br. glui28&br. glui29&br. glui30&br. glui31&br. glui32&br. glui33&br. glui34&br. glui35&br. glui36&br. glui37&br. glui38&br. glui39&br. glui40&br. glui41&br. glui42&br. glui43&br. glui44&br. glui45&br. glui46&br. glui47&br. glui48&br. glui49&br. glui50')
cmd.delete('glui1')
cmd.delete('glui2')
cmd.delete('glui3')
cmd.delete('glui4')
cmd.delete('glui5')
cmd.delete('glui6')
cmd.delete('glui7')
cmd.delete('glui8')
cmd.delete('glui9')
cmd.delete('glui10')
cmd.delete('glui11')
cmd.delete('glui12')
cmd.delete('glui13')
cmd.delete('glui14')
cmd.delete('glui15')
cmd.delete('glui16')
cmd.delete('glui17')
cmd.delete('glui18')
cmd.delete('glui19')
cmd.delete('glui20')
cmd.delete('glui21')
cmd.delete('glui22')
cmd.delete('glui23')
cmd.delete('glui24')
cmd.delete('glui25')
cmd.delete('glui26')
cmd.delete('glui27')
cmd.delete('glui28')
cmd.delete('glui29')
cmd.delete('glui30')
cmd.delete('glui31')
cmd.delete('glui32')
cmd.delete('glui33')
cmd.delete('glui34')
cmd.delete('glui35')
cmd.delete('glui36')
cmd.delete('glui37')
cmd.delete('glui38')
cmd.delete('glui39')
cmd.delete('glui40')
cmd.delete('glui41')
cmd.delete('glui42')
cmd.delete('glui43')
cmd.delete('glui44')
cmd.delete('glui45')
cmd.delete('glui46')
cmd.delete('glui47')
cmd.delete('glui48')
cmd.delete('glui49')
cmd.select('glui51', 'n. CD&r. glu w. %s of n. CG&arg'%(d*10.80))
cmd.select('glui52', 'n. CD&r. glu w. %s of n. CD&arg'%(d*11.12))
cmd.select('glui53', 'n. CD&r. glu w. %s of n. NE&arg'%(d*12.26))
cmd.select('glui54', 'n. CD&r. glu w. %s of n. CZ&arg'%(d*12.94))
cmd.select('glui55', 'n. CD&r. glu w. %s of n. NH1&arg'%(d*12.65))
cmd.select('glui56', 'n. CD&r. glu w. %s of n. NH2&arg'%(d*14.04))
cmd.select('glui57', 'n. OE1&r. glu w. %s of n. CB&arg'%(d*8.81))
cmd.select('glui58', 'n. OE1&r. glu w. %s of n. CG&arg'%(d*9.57))
cmd.select('glui59', 'n. OE1&r. glu w. %s of n. CD&arg'%(d*9.86))
cmd.select('glui60', 'n. OE1&r. glu w. %s of n. NE&arg'%(d*11.01))
cmd.select('glui61', 'n. OE1&r. glu w. %s of n. CZ&arg'%(d*11.69))
cmd.select('glui62', 'n. OE1&r. glu w. %s of n. NH1&arg'%(d*11.43))
cmd.select('glui63', 'n. OE1&r. glu w. %s of n. NH2&arg'%(d*12.80))
cmd.select('glui64', 'n. OE2&r. glu w. %s of n. CB&arg'%(d*10.85))
cmd.select('glui65', 'n. OE2&r. glu w. %s of n. CG&arg'%(d*11.53))
cmd.select('glui66', 'n. OE2&r. glu w. %s of n. CD&arg'%(d*11.89))
cmd.select('glui67', 'n. OE2&r. glu w. %s of n. NE&arg'%(d*12.95))
cmd.select('glui68', 'n. OE2&r. glu w. %s of n. CZ&arg'%(d*13.62))
cmd.select('glui69', 'n. OE2&r. glu w. %s of n. NH1&arg'%(d*13.41))
cmd.select('glui70', 'n. OE2&r. glu w. %s of n. NH2&arg'%(d*14.66))
cmd.select('glui',' glui50&br. glui51&br. glui52&br. glui53&br. glui54&br. glui55&br. glui56&br. glui57&br. glui58&br. glui59&br. glui60&br. glui61&br. glui62&br. glui63&br. glui64&br. glui65&br. glui66&br. glui67&br. glui68&br. glui69&br. glui70')
cmd.delete('glui50')
cmd.delete('glui51')
cmd.delete('glui52')
cmd.delete('glui53')
cmd.delete('glui54')
cmd.delete('glui55')
cmd.delete('glui56')
cmd.delete('glui57')
cmd.delete('glui58')
cmd.delete('glui59')
cmd.delete('glui60')
cmd.delete('glui61')
cmd.delete('glui62')
cmd.delete('glui63')
cmd.delete('glui64')
cmd.delete('glui65')
cmd.delete('glui66')
cmd.delete('glui67')
cmd.delete('glui68')
cmd.delete('glui69')
cmd.delete('glui70')
cmd.select('P_1gy0-S147A-E159A-R184A-E189A', 'ser|glu|arg|glui')
cmd.delete('ser')
cmd.delete('glu')
cmd.delete('arg')
cmd.delete('glui')
