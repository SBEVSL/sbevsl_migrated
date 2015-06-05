'''
FUNC:A_1d1q
PDB:1d1q
EC:3.1.3.2
PFAM:PF01451
RESI:ala,arg,ser,asp
LOCI:a-13,19,20,132;
'''
cmd.select('ala1', 'n. CB&r. ala w. %s of n. CB&r. ser'%(d*5.80))
cmd.select('ala2', 'n. CB&r. ala w. %s of n. OG&r. ser'%(d*5.75))
cmd.select('ala3', 'n. CB&r. ala w. %s of n. CB&r. arg'%(d*6.36))
cmd.select('ala4', 'n. CB&r. ala w. %s of n. CG&r. arg'%(d*7.35))
cmd.select('ala5', 'n. CB&r. ala w. %s of n. CD&r. arg'%(d*7.10))
cmd.select('ala6', 'n. CB&r. ala w. %s of n. NE&r. arg'%(d*6.18))
cmd.select('ala7', 'n. CB&r. ala w. %s of n. CZ&r. arg'%(d*6.21))
cmd.select('ala8', 'n. CB&r. ala w. %s of n. NH1&r. arg'%(d*7.06))
cmd.select('ala9', 'n. CB&r. ala w. %s of n. NH2&r. arg'%(d*5.95))
cmd.select('ala10', 'n. CB&r. ala w. %s of n. CB&r. asp'%(d*9.72))
cmd.select('ala11', 'n. CB&r. ala w. %s of n. CG&r. asp'%(d*9.62))
cmd.select('ala12', 'n. CB&r. ala w. %s of n. OD1&r. asp'%(d*9.68))
cmd.select('ala13', 'n. CB&r. ala w. %s of n. OD2&r. asp'%(d*9.79))
cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13')
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&ala'%(d*5.80))
cmd.select('ser2', 'n. OG&r. ser w. %s of n. CB&ala'%(d*5.75))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CB&r. arg'%(d*7.24))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. CG&r. arg'%(d*8.75))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. CD&r. arg'%(d*9.25))
cmd.select('ser6', 'n. CB&r. ser w. %s of n. NE&r. arg'%(d*8.93))
cmd.select('ser7', 'n. CB&r. ser w. %s of n. CZ&r. arg'%(d*9.47))
cmd.select('ser8', 'n. CB&r. ser w. %s of n. NH1&r. arg'%(d*10.25))
cmd.select('ser9', 'n. CB&r. ser w. %s of n. NH2&r. arg'%(d*9.53))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. CB&r. arg'%(d*7.75))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. CG&r. arg'%(d*9.18))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. CD&r. arg'%(d*9.66))
cmd.select('ser13', 'n. OG&r. ser w. %s of n. NE&r. arg'%(d*9.11))
cmd.select('ser14', 'n. OG&r. ser w. %s of n. CZ&r. arg'%(d*9.61))
cmd.select('ser15', 'n. OG&r. ser w. %s of n. NH1&r. arg'%(d*10.54))
cmd.select('ser16', 'n. OG&r. ser w. %s of n. NH2&r. arg'%(d*9.45))
cmd.select('ser17', 'n. CB&r. ser w. %s of n. CB&r. asp'%(d*12.98))
cmd.select('ser18', 'n. CB&r. ser w. %s of n. CG&r. asp'%(d*12.82))
cmd.select('ser19', 'n. CB&r. ser w. %s of n. OD1&r. asp'%(d*12.59))
cmd.select('ser20', 'n. CB&r. ser w. %s of n. OD2&r. asp'%(d*13.15))
cmd.select('ser21', 'n. OG&r. ser w. %s of n. CB&r. asp'%(d*12.94))
cmd.select('ser22', 'n. OG&r. ser w. %s of n. CG&r. asp'%(d*12.59))
cmd.select('ser23', 'n. OG&r. ser w. %s of n. OD1&r. asp'%(d*12.34))
cmd.select('ser24', 'n. OG&r. ser w. %s of n. OD2&r. asp'%(d*12.80))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24')
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
cmd.select('arg1', 'n. CB&r. arg w. %s of n. CB&ala'%(d*6.36))
cmd.select('arg2', 'n. CG&r. arg w. %s of n. CB&ala'%(d*7.35))
cmd.select('arg3', 'n. CD&r. arg w. %s of n. CB&ala'%(d*7.10))
cmd.select('arg4', 'n. NE&r. arg w. %s of n. CB&ala'%(d*6.18))
cmd.select('arg5', 'n. CZ&r. arg w. %s of n. CB&ala'%(d*6.21))
cmd.select('arg6', 'n. NH1&r. arg w. %s of n. CB&ala'%(d*7.06))
cmd.select('arg7', 'n. NH2&r. arg w. %s of n. CB&ala'%(d*5.95))
cmd.select('arg8', 'n. CB&r. arg w. %s of n. CB&ser'%(d*7.24))
cmd.select('arg9', 'n. CB&r. arg w. %s of n. OG&ser'%(d*7.75))
cmd.select('arg10', 'n. CG&r. arg w. %s of n. CB&ser'%(d*8.75))
cmd.select('arg11', 'n. CG&r. arg w. %s of n. OG&ser'%(d*9.18))
cmd.select('arg12', 'n. CD&r. arg w. %s of n. CB&ser'%(d*9.25))
cmd.select('arg13', 'n. CD&r. arg w. %s of n. OG&ser'%(d*9.66))
cmd.select('arg14', 'n. NE&r. arg w. %s of n. CB&ser'%(d*8.93))
cmd.select('arg15', 'n. NE&r. arg w. %s of n. OG&ser'%(d*9.11))
cmd.select('arg16', 'n. CZ&r. arg w. %s of n. CB&ser'%(d*9.47))
cmd.select('arg17', 'n. CZ&r. arg w. %s of n. OG&ser'%(d*9.61))
cmd.select('arg18', 'n. NH1&r. arg w. %s of n. CB&ser'%(d*10.25))
cmd.select('arg19', 'n. NH1&r. arg w. %s of n. OG&ser'%(d*10.54))
cmd.select('arg20', 'n. NH2&r. arg w. %s of n. CB&ser'%(d*9.53))
cmd.select('arg21', 'n. NH2&r. arg w. %s of n. OG&ser'%(d*9.45))
cmd.select('arg22', 'n. CB&r. arg w. %s of n. CB&r. asp'%(d*9.00))
cmd.select('arg23', 'n. CB&r. arg w. %s of n. CG&r. asp'%(d*9.13))
cmd.select('arg24', 'n. CB&r. arg w. %s of n. OD1&r. asp'%(d*8.72))
cmd.select('arg25', 'n. CB&r. arg w. %s of n. OD2&r. asp'%(d*9.93))
cmd.select('arg26', 'n. CG&r. arg w. %s of n. CB&r. asp'%(d*7.92))
cmd.select('arg27', 'n. CG&r. arg w. %s of n. CG&r. asp'%(d*8.16))
cmd.select('arg28', 'n. CG&r. arg w. %s of n. OD1&r. asp'%(d*7.71))
cmd.select('arg29', 'n. CG&r. arg w. %s of n. OD2&r. asp'%(d*9.12))
cmd.select('arg30', 'n. CD&r. arg w. %s of n. CB&r. asp'%(d*6.80))
cmd.select('arg31', 'n. CD&r. arg w. %s of n. CG&r. asp'%(d*7.30))
cmd.select('arg32', 'n. CD&r. arg w. %s of n. OD1&r. asp'%(d*7.13))
cmd.select('arg33', 'n. CD&r. arg w. %s of n. OD2&r. asp'%(d*8.22))
cmd.select('arg34', 'n. NE&r. arg w. %s of n. CB&r. asp'%(d*6.23))
cmd.select('arg35', 'n. NE&r. arg w. %s of n. CG&r. asp'%(d*6.48))
cmd.select('arg36', 'n. NE&r. arg w. %s of n. OD1&r. asp'%(d*6.43))
cmd.select('arg37', 'n. NE&r. arg w. %s of n. OD2&r. asp'%(d*7.21))
cmd.select('arg38', 'n. CZ&r. arg w. %s of n. CB&r. asp'%(d*5.76))
cmd.select('arg39', 'n. CZ&r. arg w. %s of n. CG&r. asp'%(d*6.18))
cmd.select('arg40', 'n. CZ&r. arg w. %s of n. OD1&r. asp'%(d*6.50))
cmd.select('arg41', 'n. CZ&r. arg w. %s of n. OD2&r. asp'%(d*6.72))
cmd.select('arg42', 'n. NH1&r. arg w. %s of n. CB&r. asp'%(d*5.82))
cmd.select('arg43', 'n. NH1&r. arg w. %s of n. CG&r. asp'%(d*6.68))
cmd.select('arg44', 'n. NH1&r. arg w. %s of n. OD1&r. asp'%(d*7.18))
cmd.select('arg45', 'n. NH1&r. arg w. %s of n. OD2&r. asp'%(d*7.25))
cmd.select('arg46', 'n. NH2&r. arg w. %s of n. CB&r. asp'%(d*5.89))
cmd.select('arg47', 'n. NH2&r. arg w. %s of n. CG&r. asp'%(d*5.97))
cmd.select('arg48', 'n. NH2&r. arg w. %s of n. OD1&r. asp'%(d*6.42))
cmd.select('arg49', 'n. NH2&r. arg w. %s of n. OD2&r. asp'%(d*6.17))
cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27&br. arg28&br. arg29&br. arg30&br. arg31&br. arg32&br. arg33&br. arg34&br. arg35&br. arg36&br. arg37&br. arg38&br. arg39&br. arg40&br. arg41&br. arg42&br. arg43&br. arg44&br. arg45&br. arg46&br. arg47&br. arg48&br. arg49')
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
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&ala'%(d*9.72))
cmd.select('asp2', 'n. CG&r. asp w. %s of n. CB&ala'%(d*9.62))
cmd.select('asp3', 'n. OD1&r. asp w. %s of n. CB&ala'%(d*9.68))
cmd.select('asp4', 'n. OD2&r. asp w. %s of n. CB&ala'%(d*9.79))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. CB&ser'%(d*12.98))
cmd.select('asp6', 'n. CB&r. asp w. %s of n. OG&ser'%(d*12.94))
cmd.select('asp7', 'n. CG&r. asp w. %s of n. CB&ser'%(d*12.82))
cmd.select('asp8', 'n. CG&r. asp w. %s of n. OG&ser'%(d*12.59))
cmd.select('asp9', 'n. OD1&r. asp w. %s of n. CB&ser'%(d*12.59))
cmd.select('asp10', 'n. OD1&r. asp w. %s of n. OG&ser'%(d*12.34))
cmd.select('asp11', 'n. OD2&r. asp w. %s of n. CB&ser'%(d*13.15))
cmd.select('asp12', 'n. OD2&r. asp w. %s of n. OG&ser'%(d*12.80))
cmd.select('asp13', 'n. CB&r. asp w. %s of n. CB&arg'%(d*9.00))
cmd.select('asp14', 'n. CB&r. asp w. %s of n. CG&arg'%(d*7.92))
cmd.select('asp15', 'n. CB&r. asp w. %s of n. CD&arg'%(d*6.80))
cmd.select('asp16', 'n. CB&r. asp w. %s of n. NE&arg'%(d*6.23))
cmd.select('asp17', 'n. CB&r. asp w. %s of n. CZ&arg'%(d*5.76))
cmd.select('asp18', 'n. CB&r. asp w. %s of n. NH1&arg'%(d*5.82))
cmd.select('asp19', 'n. CB&r. asp w. %s of n. NH2&arg'%(d*5.89))
cmd.select('asp20', 'n. CG&r. asp w. %s of n. CB&arg'%(d*9.13))
cmd.select('asp21', 'n. CG&r. asp w. %s of n. CG&arg'%(d*8.16))
cmd.select('asp22', 'n. CG&r. asp w. %s of n. CD&arg'%(d*7.30))
cmd.select('asp23', 'n. CG&r. asp w. %s of n. NE&arg'%(d*6.48))
cmd.select('asp24', 'n. CG&r. asp w. %s of n. CZ&arg'%(d*6.18))
cmd.select('asp25', 'n. CG&r. asp w. %s of n. NH1&arg'%(d*6.68))
cmd.select('asp26', 'n. CG&r. asp w. %s of n. NH2&arg'%(d*5.97))
cmd.select('asp27', 'n. OD1&r. asp w. %s of n. CB&arg'%(d*8.72))
cmd.select('asp28', 'n. OD1&r. asp w. %s of n. CG&arg'%(d*7.71))
cmd.select('asp29', 'n. OD1&r. asp w. %s of n. CD&arg'%(d*7.13))
cmd.select('asp30', 'n. OD1&r. asp w. %s of n. NE&arg'%(d*6.43))
cmd.select('asp31', 'n. OD1&r. asp w. %s of n. CZ&arg'%(d*6.50))
cmd.select('asp32', 'n. OD1&r. asp w. %s of n. NH1&arg'%(d*7.18))
cmd.select('asp33', 'n. OD1&r. asp w. %s of n. NH2&arg'%(d*6.42))
cmd.select('asp34', 'n. OD2&r. asp w. %s of n. CB&arg'%(d*9.93))
cmd.select('asp35', 'n. OD2&r. asp w. %s of n. CG&arg'%(d*9.12))
cmd.select('asp36', 'n. OD2&r. asp w. %s of n. CD&arg'%(d*8.22))
cmd.select('asp37', 'n. OD2&r. asp w. %s of n. NE&arg'%(d*7.21))
cmd.select('asp38', 'n. OD2&r. asp w. %s of n. CZ&arg'%(d*6.72))
cmd.select('asp39', 'n. OD2&r. asp w. %s of n. NH1&arg'%(d*7.25))
cmd.select('asp40', 'n. OD2&r. asp w. %s of n. NH2&arg'%(d*6.17))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36&br. asp37&br. asp38&br. asp39&br. asp40')
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
cmd.select('A_1d1q', 'ala|ser|arg|asp')
cmd.delete('ala')
cmd.delete('ser')
cmd.delete('arg')
cmd.delete('asp')
