'''
FUNC:A_1d5r-D92A-C124A-R130A
PDB:1d5r
EC:3.1.3.67
PFAM:PF00782,PF10409,PF00102
RESI:asp,cys,arg
LOCI:a-92,124,130;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. arg'%(d*5.86))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&r. arg'%(d*6.67))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CD&r. arg'%(d*6.43))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. NE&r. arg'%(d*5.81))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. CZ&r. arg'%(d*6.18))
cmd.select('cys6', 'n. CB&r. cys w. %s of n. NH1&r. arg'%(d*6.99))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. NH2&r. arg'%(d*6.30))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. CB&r. arg'%(d*6.02))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. CG&r. arg'%(d*6.96))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. CD&r. arg'%(d*7.18))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. NE&r. arg'%(d*6.53))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. CZ&r. arg'%(d*7.18))
cmd.select('cys13', 'n. SG&r. cys w. %s of n. NH1&r. arg'%(d*8.23))
cmd.select('cys14', 'n. SG&r. cys w. %s of n. NH2&r. arg'%(d*7.16))
cmd.select('cys15', 'n. CB&r. cys w. %s of n. CB&r. asp'%(d*10.11))
cmd.select('cys16', 'n. CB&r. cys w. %s of n. CG&r. asp'%(d*9.89))
cmd.select('cys17', 'n. CB&r. cys w. %s of n. OD1&r. asp'%(d*10.65))
cmd.select('cys18', 'n. CB&r. cys w. %s of n. OD2&r. asp'%(d*9.20))
cmd.select('cys19', 'n. SG&r. cys w. %s of n. CB&r. asp'%(d*10.63))
cmd.select('cys20', 'n. SG&r. cys w. %s of n. CG&r. asp'%(d*10.15))
cmd.select('cys21', 'n. SG&r. cys w. %s of n. OD1&r. asp'%(d*10.88))
cmd.select('cys22', 'n. SG&r. cys w. %s of n. OD2&r. asp'%(d*9.25))
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
cmd.select('arg1', 'n. CB&r. arg w. %s of n. CB&cys'%(d*5.86))
cmd.select('arg2', 'n. CB&r. arg w. %s of n. SG&cys'%(d*6.02))
cmd.select('arg3', 'n. CG&r. arg w. %s of n. CB&cys'%(d*6.67))
cmd.select('arg4', 'n. CG&r. arg w. %s of n. SG&cys'%(d*6.96))
cmd.select('arg5', 'n. CD&r. arg w. %s of n. CB&cys'%(d*6.43))
cmd.select('arg6', 'n. CD&r. arg w. %s of n. SG&cys'%(d*7.18))
cmd.select('arg7', 'n. NE&r. arg w. %s of n. CB&cys'%(d*5.81))
cmd.select('arg8', 'n. NE&r. arg w. %s of n. SG&cys'%(d*6.53))
cmd.select('arg9', 'n. CZ&r. arg w. %s of n. CB&cys'%(d*6.18))
cmd.select('arg10', 'n. CZ&r. arg w. %s of n. SG&cys'%(d*7.18))
cmd.select('arg11', 'n. NH1&r. arg w. %s of n. CB&cys'%(d*6.99))
cmd.select('arg12', 'n. NH1&r. arg w. %s of n. SG&cys'%(d*8.23))
cmd.select('arg13', 'n. NH2&r. arg w. %s of n. CB&cys'%(d*6.30))
cmd.select('arg14', 'n. NH2&r. arg w. %s of n. SG&cys'%(d*7.16))
cmd.select('arg15', 'n. CB&r. arg w. %s of n. CB&r. asp'%(d*9.66))
cmd.select('arg16', 'n. CB&r. arg w. %s of n. CG&r. asp'%(d*9.75))
cmd.select('arg17', 'n. CB&r. arg w. %s of n. OD1&r. asp'%(d*10.87))
cmd.select('arg18', 'n. CB&r. arg w. %s of n. OD2&r. asp'%(d*8.90))
cmd.select('arg19', 'n. CG&r. arg w. %s of n. CB&r. asp'%(d*8.37))
cmd.select('arg20', 'n. CG&r. arg w. %s of n. CG&r. asp'%(d*8.61))
cmd.select('arg21', 'n. CG&r. arg w. %s of n. OD1&r. asp'%(d*9.79))
cmd.select('arg22', 'n. CG&r. arg w. %s of n. OD2&r. asp'%(d*7.83))
cmd.select('arg23', 'n. CD&r. arg w. %s of n. CB&r. asp'%(d*7.36))
cmd.select('arg24', 'n. CD&r. arg w. %s of n. CG&r. asp'%(d*7.78))
cmd.select('arg25', 'n. CD&r. arg w. %s of n. OD1&r. asp'%(d*8.93))
cmd.select('arg26', 'n. CD&r. arg w. %s of n. OD2&r. asp'%(d*7.23))
cmd.select('arg27', 'n. NE&r. arg w. %s of n. CB&r. asp'%(d*6.69))
cmd.select('arg28', 'n. NE&r. arg w. %s of n. CG&r. asp'%(d*6.85))
cmd.select('arg29', 'n. NE&r. arg w. %s of n. OD1&r. asp'%(d*7.90))
cmd.select('arg30', 'n. NE&r. arg w. %s of n. OD2&r. asp'%(d*6.28))
cmd.select('arg31', 'n. CZ&r. arg w. %s of n. CB&r. asp'%(d*6.18))
cmd.select('arg32', 'n. CZ&r. arg w. %s of n. CG&r. asp'%(d*6.45))
cmd.select('arg33', 'n. CZ&r. arg w. %s of n. OD1&r. asp'%(d*7.36))
cmd.select('arg34', 'n. CZ&r. arg w. %s of n. OD2&r. asp'%(d*6.19))
cmd.select('arg35', 'n. NH1&r. arg w. %s of n. CB&r. asp'%(d*6.32))
cmd.select('arg36', 'n. NH1&r. arg w. %s of n. CG&r. asp'%(d*6.98))
cmd.select('arg37', 'n. NH1&r. arg w. %s of n. OD1&r. asp'%(d*7.87))
cmd.select('arg38', 'n. NH1&r. arg w. %s of n. OD2&r. asp'%(d*6.99))
cmd.select('arg39', 'n. NH2&r. arg w. %s of n. CB&r. asp'%(d*6.10))
cmd.select('arg40', 'n. NH2&r. arg w. %s of n. CG&r. asp'%(d*6.02))
cmd.select('arg41', 'n. NH2&r. arg w. %s of n. OD1&r. asp'%(d*6.71))
cmd.select('arg42', 'n. NH2&r. arg w. %s of n. OD2&r. asp'%(d*5.82))
cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27&br. arg28&br. arg29&br. arg30&br. arg31&br. arg32&br. arg33&br. arg34&br. arg35&br. arg36&br. arg37&br. arg38&br. arg39&br. arg40&br. arg41&br. arg42')
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
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&cys'%(d*10.11))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. SG&cys'%(d*10.63))
cmd.select('asp3', 'n. CG&r. asp w. %s of n. CB&cys'%(d*9.89))
cmd.select('asp4', 'n. CG&r. asp w. %s of n. SG&cys'%(d*10.15))
cmd.select('asp5', 'n. OD1&r. asp w. %s of n. CB&cys'%(d*10.65))
cmd.select('asp6', 'n. OD1&r. asp w. %s of n. SG&cys'%(d*10.88))
cmd.select('asp7', 'n. OD2&r. asp w. %s of n. CB&cys'%(d*9.20))
cmd.select('asp8', 'n. OD2&r. asp w. %s of n. SG&cys'%(d*9.25))
cmd.select('asp9', 'n. CB&r. asp w. %s of n. CB&arg'%(d*9.66))
cmd.select('asp10', 'n. CB&r. asp w. %s of n. CG&arg'%(d*8.37))
cmd.select('asp11', 'n. CB&r. asp w. %s of n. CD&arg'%(d*7.36))
cmd.select('asp12', 'n. CB&r. asp w. %s of n. NE&arg'%(d*6.69))
cmd.select('asp13', 'n. CB&r. asp w. %s of n. CZ&arg'%(d*6.18))
cmd.select('asp14', 'n. CB&r. asp w. %s of n. NH1&arg'%(d*6.32))
cmd.select('asp15', 'n. CB&r. asp w. %s of n. NH2&arg'%(d*6.10))
cmd.select('asp16', 'n. CG&r. asp w. %s of n. CB&arg'%(d*9.75))
cmd.select('asp17', 'n. CG&r. asp w. %s of n. CG&arg'%(d*8.61))
cmd.select('asp18', 'n. CG&r. asp w. %s of n. CD&arg'%(d*7.78))
cmd.select('asp19', 'n. CG&r. asp w. %s of n. NE&arg'%(d*6.85))
cmd.select('asp20', 'n. CG&r. asp w. %s of n. CZ&arg'%(d*6.45))
cmd.select('asp21', 'n. CG&r. asp w. %s of n. NH1&arg'%(d*6.98))
cmd.select('asp22', 'n. CG&r. asp w. %s of n. NH2&arg'%(d*6.02))
cmd.select('asp23', 'n. OD1&r. asp w. %s of n. CB&arg'%(d*10.87))
cmd.select('asp24', 'n. OD1&r. asp w. %s of n. CG&arg'%(d*9.79))
cmd.select('asp25', 'n. OD1&r. asp w. %s of n. CD&arg'%(d*8.93))
cmd.select('asp26', 'n. OD1&r. asp w. %s of n. NE&arg'%(d*7.90))
cmd.select('asp27', 'n. OD1&r. asp w. %s of n. CZ&arg'%(d*7.36))
cmd.select('asp28', 'n. OD1&r. asp w. %s of n. NH1&arg'%(d*7.87))
cmd.select('asp29', 'n. OD1&r. asp w. %s of n. NH2&arg'%(d*6.71))
cmd.select('asp30', 'n. OD2&r. asp w. %s of n. CB&arg'%(d*8.90))
cmd.select('asp31', 'n. OD2&r. asp w. %s of n. CG&arg'%(d*7.83))
cmd.select('asp32', 'n. OD2&r. asp w. %s of n. CD&arg'%(d*7.23))
cmd.select('asp33', 'n. OD2&r. asp w. %s of n. NE&arg'%(d*6.28))
cmd.select('asp34', 'n. OD2&r. asp w. %s of n. CZ&arg'%(d*6.19))
cmd.select('asp35', 'n. OD2&r. asp w. %s of n. NH1&arg'%(d*6.99))
cmd.select('asp36', 'n. OD2&r. asp w. %s of n. NH2&arg'%(d*5.82))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36')
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
cmd.select('A_1d5r-D92A-C124A-R130A', 'cys|arg|asp')
cmd.delete('cys')
cmd.delete('arg')
cmd.delete('asp')