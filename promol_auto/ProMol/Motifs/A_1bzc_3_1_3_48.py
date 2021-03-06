'''
FUNC:A_1bzc_3_1_3_48
PDB:1bzc
EC:3.1.3.48
RESI:asp,cys,arg,ser
LOCI:a-181,215,221,222;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. arg'%(d*5.85))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&r. arg'%(d*6.66))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CD&r. arg'%(d*6.31))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. NE&r. arg'%(d*5.60))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. CZ&r. arg'%(d*5.92))
cmd.select('cys6', 'n. CB&r. cys w. %s of n. NH1&r. arg'%(d*6.78))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. NH2&r. arg'%(d*6.03))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. CB&r. arg'%(d*5.98))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. CG&r. arg'%(d*6.96))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. CD&r. arg'%(d*7.08))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. NE&r. arg'%(d*6.32))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. CZ&r. arg'%(d*6.91))
cmd.select('cys13', 'n. SG&r. cys w. %s of n. NH1&r. arg'%(d*8.01))
cmd.select('cys14', 'n. SG&r. cys w. %s of n. NH2&r. arg'%(d*6.83))
cmd.select('cys15', 'n. CB&r. cys w. %s of n. CB&r. ser'%(d*6.87))
cmd.select('cys16', 'n. CB&r. cys w. %s of n. OG&r. ser'%(d*5.89))
cmd.select('cys17', 'n. SG&r. cys w. %s of n. CB&r. ser'%(d*5.70))
cmd.select('cys18', 'n. SG&r. cys w. %s of n. OG&r. ser'%(d*5.02))
cmd.select('cys19', 'n. CB&r. cys w. %s of n. CB&r. asp'%(d*9.13))
cmd.select('cys20', 'n. CB&r. cys w. %s of n. CG&r. asp'%(d*10.47))
cmd.select('cys21', 'n. CB&r. cys w. %s of n. OD1&r. asp'%(d*11.05))
cmd.select('cys22', 'n. CB&r. cys w. %s of n. OD2&r. asp'%(d*11.08))
cmd.select('cys23', 'n. SG&r. cys w. %s of n. CB&r. asp'%(d*9.66))
cmd.select('cys24', 'n. SG&r. cys w. %s of n. CG&r. asp'%(d*11.07))
cmd.select('cys25', 'n. SG&r. cys w. %s of n. OD1&r. asp'%(d*11.83))
cmd.select('cys26', 'n. SG&r. cys w. %s of n. OD2&r. asp'%(d*11.55))
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
cmd.select('arg1', 'n. CB&r. arg w. %s of n. CB&cys'%(d*5.85))
cmd.select('arg2', 'n. CB&r. arg w. %s of n. SG&cys'%(d*5.98))
cmd.select('arg3', 'n. CG&r. arg w. %s of n. CB&cys'%(d*6.66))
cmd.select('arg4', 'n. CG&r. arg w. %s of n. SG&cys'%(d*6.96))
cmd.select('arg5', 'n. CD&r. arg w. %s of n. CB&cys'%(d*6.31))
cmd.select('arg6', 'n. CD&r. arg w. %s of n. SG&cys'%(d*7.08))
cmd.select('arg7', 'n. NE&r. arg w. %s of n. CB&cys'%(d*5.60))
cmd.select('arg8', 'n. NE&r. arg w. %s of n. SG&cys'%(d*6.32))
cmd.select('arg9', 'n. CZ&r. arg w. %s of n. CB&cys'%(d*5.92))
cmd.select('arg10', 'n. CZ&r. arg w. %s of n. SG&cys'%(d*6.91))
cmd.select('arg11', 'n. NH1&r. arg w. %s of n. CB&cys'%(d*6.78))
cmd.select('arg12', 'n. NH1&r. arg w. %s of n. SG&cys'%(d*8.01))
cmd.select('arg13', 'n. NH2&r. arg w. %s of n. CB&cys'%(d*6.03))
cmd.select('arg14', 'n. NH2&r. arg w. %s of n. SG&cys'%(d*6.83))
cmd.select('arg15', 'n. CB&r. arg w. %s of n. CB&r. ser'%(d*7.42))
cmd.select('arg16', 'n. CB&r. arg w. %s of n. OG&r. ser'%(d*7.33))
cmd.select('arg17', 'n. CG&r. arg w. %s of n. CB&r. ser'%(d*8.86))
cmd.select('arg18', 'n. CG&r. arg w. %s of n. OG&r. ser'%(d*8.75))
cmd.select('arg19', 'n. CD&r. arg w. %s of n. CB&r. ser'%(d*9.55))
cmd.select('arg20', 'n. CD&r. arg w. %s of n. OG&r. ser'%(d*9.17))
cmd.select('arg21', 'n. NE&r. arg w. %s of n. CB&r. ser'%(d*9.35))
cmd.select('arg22', 'n. NE&r. arg w. %s of n. OG&r. ser'%(d*8.86))
cmd.select('arg23', 'n. CZ&r. arg w. %s of n. CB&r. ser'%(d*10.24))
cmd.select('arg24', 'n. CZ&r. arg w. %s of n. OG&r. ser'%(d*9.58))
cmd.select('arg25', 'n. NH1&r. arg w. %s of n. CB&r. ser'%(d*11.21))
cmd.select('arg26', 'n. NH1&r. arg w. %s of n. OG&r. ser'%(d*10.49))
cmd.select('arg27', 'n. NH2&r. arg w. %s of n. CB&r. ser'%(d*10.41))
cmd.select('arg28', 'n. NH2&r. arg w. %s of n. OG&r. ser'%(d*9.70))
cmd.select('arg29', 'n. CB&r. arg w. %s of n. CB&r. asp'%(d*9.13))
cmd.select('arg30', 'n. CB&r. arg w. %s of n. CG&r. asp'%(d*10.59))
cmd.select('arg31', 'n. CB&r. arg w. %s of n. OD1&r. asp'%(d*11.02))
cmd.select('arg32', 'n. CB&r. arg w. %s of n. OD2&r. asp'%(d*11.45))
cmd.select('arg33', 'n. CG&r. arg w. %s of n. CB&r. asp'%(d*8.09))
cmd.select('arg34', 'n. CG&r. arg w. %s of n. CG&r. asp'%(d*9.50))
cmd.select('arg35', 'n. CG&r. arg w. %s of n. OD1&r. asp'%(d*9.85))
cmd.select('arg36', 'n. CG&r. arg w. %s of n. OD2&r. asp'%(d*10.44))
cmd.select('arg37', 'n. CD&r. arg w. %s of n. CB&r. asp'%(d*7.16))
cmd.select('arg38', 'n. CD&r. arg w. %s of n. CG&r. asp'%(d*8.50))
cmd.select('arg39', 'n. CD&r. arg w. %s of n. OD1&r. asp'%(d*8.75))
cmd.select('arg40', 'n. CD&r. arg w. %s of n. OD2&r. asp'%(d*9.51))
cmd.select('arg41', 'n. NE&r. arg w. %s of n. CB&r. asp'%(d*6.28))
cmd.select('arg42', 'n. NE&r. arg w. %s of n. CG&r. asp'%(d*7.70))
cmd.select('arg43', 'n. NE&r. arg w. %s of n. OD1&r. asp'%(d*8.16))
cmd.select('arg44', 'n. NE&r. arg w. %s of n. OD2&r. asp'%(d*8.58))
cmd.select('arg45', 'n. CZ&r. arg w. %s of n. CB&r. asp'%(d*5.56))
cmd.select('arg46', 'n. CZ&r. arg w. %s of n. CG&r. asp'%(d*6.85))
cmd.select('arg47', 'n. CZ&r. arg w. %s of n. OD1&r. asp'%(d*7.26))
cmd.select('arg48', 'n. CZ&r. arg w. %s of n. OD2&r. asp'%(d*7.73))
cmd.select('arg49', 'n. NH1&r. arg w. %s of n. CB&r. asp'%(d*5.76))
cmd.select('arg50', 'n. NH1&r. arg w. %s of n. CG&r. asp'%(d*6.78))
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
cmd.select('arg51', 'n. NH1&r. arg w. %s of n. OD1&r. asp'%(d*6.88))
cmd.select('arg52', 'n. NH1&r. arg w. %s of n. OD2&r. asp'%(d*7.81))
cmd.select('arg53', 'n. NH2&r. arg w. %s of n. CB&r. asp'%(d*5.21))
cmd.select('arg54', 'n. NH2&r. arg w. %s of n. CG&r. asp'%(d*6.45))
cmd.select('arg55', 'n. NH2&r. arg w. %s of n. OD1&r. asp'%(d*7.10))
cmd.select('arg56', 'n. NH2&r. arg w. %s of n. OD2&r. asp'%(d*7.10))
cmd.select('arg',' arg50&br. arg51&br. arg52&br. arg53&br. arg54&br. arg55&br. arg56')
cmd.delete('arg50')
cmd.delete('arg51')
cmd.delete('arg52')
cmd.delete('arg53')
cmd.delete('arg54')
cmd.delete('arg55')
cmd.delete('arg56')
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&cys'%(d*6.87))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. SG&cys'%(d*5.70))
cmd.select('ser3', 'n. OG&r. ser w. %s of n. CB&cys'%(d*5.89))
cmd.select('ser4', 'n. OG&r. ser w. %s of n. SG&cys'%(d*5.02))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. CB&arg'%(d*7.42))
cmd.select('ser6', 'n. CB&r. ser w. %s of n. CG&arg'%(d*8.86))
cmd.select('ser7', 'n. CB&r. ser w. %s of n. CD&arg'%(d*9.55))
cmd.select('ser8', 'n. CB&r. ser w. %s of n. NE&arg'%(d*9.35))
cmd.select('ser9', 'n. CB&r. ser w. %s of n. CZ&arg'%(d*10.24))
cmd.select('ser10', 'n. CB&r. ser w. %s of n. NH1&arg'%(d*11.21))
cmd.select('ser11', 'n. CB&r. ser w. %s of n. NH2&arg'%(d*10.41))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. CB&arg'%(d*7.33))
cmd.select('ser13', 'n. OG&r. ser w. %s of n. CG&arg'%(d*8.75))
cmd.select('ser14', 'n. OG&r. ser w. %s of n. CD&arg'%(d*9.17))
cmd.select('ser15', 'n. OG&r. ser w. %s of n. NE&arg'%(d*8.86))
cmd.select('ser16', 'n. OG&r. ser w. %s of n. CZ&arg'%(d*9.58))
cmd.select('ser17', 'n. OG&r. ser w. %s of n. NH1&arg'%(d*10.49))
cmd.select('ser18', 'n. OG&r. ser w. %s of n. NH2&arg'%(d*9.70))
cmd.select('ser19', 'n. CB&r. ser w. %s of n. CB&r. asp'%(d*13.09))
cmd.select('ser20', 'n. CB&r. ser w. %s of n. CG&r. asp'%(d*14.57))
cmd.select('ser21', 'n. CB&r. ser w. %s of n. OD1&r. asp'%(d*15.29))
cmd.select('ser22', 'n. CB&r. ser w. %s of n. OD2&r. asp'%(d*15.09))
cmd.select('ser23', 'n. OG&r. ser w. %s of n. CB&r. asp'%(d*12.59))
cmd.select('ser24', 'n. OG&r. ser w. %s of n. CG&r. asp'%(d*14.02))
cmd.select('ser25', 'n. OG&r. ser w. %s of n. OD1&r. asp'%(d*14.71))
cmd.select('ser26', 'n. OG&r. ser w. %s of n. OD2&r. asp'%(d*14.55))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26')
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
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&cys'%(d*9.13))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. SG&cys'%(d*9.66))
cmd.select('asp3', 'n. CG&r. asp w. %s of n. CB&cys'%(d*10.47))
cmd.select('asp4', 'n. CG&r. asp w. %s of n. SG&cys'%(d*11.07))
cmd.select('asp5', 'n. OD1&r. asp w. %s of n. CB&cys'%(d*11.05))
cmd.select('asp6', 'n. OD1&r. asp w. %s of n. SG&cys'%(d*11.83))
cmd.select('asp7', 'n. OD2&r. asp w. %s of n. CB&cys'%(d*11.08))
cmd.select('asp8', 'n. OD2&r. asp w. %s of n. SG&cys'%(d*11.55))
cmd.select('asp9', 'n. CB&r. asp w. %s of n. CB&arg'%(d*9.13))
cmd.select('asp10', 'n. CB&r. asp w. %s of n. CG&arg'%(d*8.09))
cmd.select('asp11', 'n. CB&r. asp w. %s of n. CD&arg'%(d*7.16))
cmd.select('asp12', 'n. CB&r. asp w. %s of n. NE&arg'%(d*6.28))
cmd.select('asp13', 'n. CB&r. asp w. %s of n. CZ&arg'%(d*5.56))
cmd.select('asp14', 'n. CB&r. asp w. %s of n. NH1&arg'%(d*5.76))
cmd.select('asp15', 'n. CB&r. asp w. %s of n. NH2&arg'%(d*5.21))
cmd.select('asp16', 'n. CG&r. asp w. %s of n. CB&arg'%(d*10.59))
cmd.select('asp17', 'n. CG&r. asp w. %s of n. CG&arg'%(d*9.50))
cmd.select('asp18', 'n. CG&r. asp w. %s of n. CD&arg'%(d*8.50))
cmd.select('asp19', 'n. CG&r. asp w. %s of n. NE&arg'%(d*7.70))
cmd.select('asp20', 'n. CG&r. asp w. %s of n. CZ&arg'%(d*6.85))
cmd.select('asp21', 'n. CG&r. asp w. %s of n. NH1&arg'%(d*6.78))
cmd.select('asp22', 'n. CG&r. asp w. %s of n. NH2&arg'%(d*6.45))
cmd.select('asp23', 'n. OD1&r. asp w. %s of n. CB&arg'%(d*11.02))
cmd.select('asp24', 'n. OD1&r. asp w. %s of n. CG&arg'%(d*9.85))
cmd.select('asp25', 'n. OD1&r. asp w. %s of n. CD&arg'%(d*8.75))
cmd.select('asp26', 'n. OD1&r. asp w. %s of n. NE&arg'%(d*8.16))
cmd.select('asp27', 'n. OD1&r. asp w. %s of n. CZ&arg'%(d*7.26))
cmd.select('asp28', 'n. OD1&r. asp w. %s of n. NH1&arg'%(d*6.88))
cmd.select('asp29', 'n. OD1&r. asp w. %s of n. NH2&arg'%(d*7.10))
cmd.select('asp30', 'n. OD2&r. asp w. %s of n. CB&arg'%(d*11.45))
cmd.select('asp31', 'n. OD2&r. asp w. %s of n. CG&arg'%(d*10.44))
cmd.select('asp32', 'n. OD2&r. asp w. %s of n. CD&arg'%(d*9.51))
cmd.select('asp33', 'n. OD2&r. asp w. %s of n. NE&arg'%(d*8.58))
cmd.select('asp34', 'n. OD2&r. asp w. %s of n. CZ&arg'%(d*7.73))
cmd.select('asp35', 'n. OD2&r. asp w. %s of n. NH1&arg'%(d*7.81))
cmd.select('asp36', 'n. OD2&r. asp w. %s of n. NH2&arg'%(d*7.10))
cmd.select('asp37', 'n. CB&r. asp w. %s of n. CB&ser'%(d*13.09))
cmd.select('asp38', 'n. CB&r. asp w. %s of n. OG&ser'%(d*12.59))
cmd.select('asp39', 'n. CG&r. asp w. %s of n. CB&ser'%(d*14.57))
cmd.select('asp40', 'n. CG&r. asp w. %s of n. OG&ser'%(d*14.02))
cmd.select('asp41', 'n. OD1&r. asp w. %s of n. CB&ser'%(d*15.29))
cmd.select('asp42', 'n. OD1&r. asp w. %s of n. OG&ser'%(d*14.71))
cmd.select('asp43', 'n. OD2&r. asp w. %s of n. CB&ser'%(d*15.09))
cmd.select('asp44', 'n. OD2&r. asp w. %s of n. OG&ser'%(d*14.55))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36&br. asp37&br. asp38&br. asp39&br. asp40&br. asp41&br. asp42&br. asp43&br. asp44')
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
cmd.delete('asp28')
cmd.delete('asp29')
cmd.delete('asp30')
cmd.delete('asp31')
cmd.delete('asp32')
cmd.delete('asp33')
cmd.delete('asp34')
cmd.delete('asp35')
cmd.delete('asp36')
cmd.delete('asp37')
cmd.delete('asp38')
cmd.delete('asp39')
cmd.delete('asp40')
cmd.delete('asp41')
cmd.delete('asp42')
cmd.delete('asp43')
cmd.delete('asp44')
cmd.select('A_1bzc_3_1_3_48', 'cys|arg|ser|asp')
cmd.delete('cys')
cmd.delete('arg')
cmd.delete('ser')
cmd.delete('asp')
