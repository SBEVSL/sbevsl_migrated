'''
FUNC:M_1f48
PDB:1f48
EC:3.6.2.16
PFAM:PF02374,PF01656
RESI:gly,lys,mg
LOCI:a-18,21;a-592;
'''
cmd.select('lys1', 'n. CB&r. lys w. %s of n. O&r. gly'%(d*9.52))
cmd.select('lys2', 'n. CB&r. lys w. %s of n. C&r. gly'%(d*8.94))
cmd.select('lys3', 'n. CB&r. lys w. %s of n. CA&r. gly'%(d*9.33))
cmd.select('lys4', 'n. CB&r. lys w. %s of n. N&r. gly'%(d*8.88))
cmd.select('lys5', 'n. CG&r. lys w. %s of n. O&r. gly'%(d*9.39))
cmd.select('lys6', 'n. CG&r. lys w. %s of n. C&r. gly'%(d*8.68))
cmd.select('lys7', 'n. CG&r. lys w. %s of n. CA&r. gly'%(d*9.17))
cmd.select('lys8', 'n. CG&r. lys w. %s of n. N&r. gly'%(d*8.62))
cmd.select('lys9', 'n. CD&r. lys w. %s of n. O&r. gly'%(d*10.28))
cmd.select('lys10', 'n. CD&r. lys w. %s of n. C&r. gly'%(d*9.40))
cmd.select('lys11', 'n. CD&r. lys w. %s of n. CA&r. gly'%(d*9.66))
cmd.select('lys12', 'n. CD&r. lys w. %s of n. N&r. gly'%(d*8.85))
cmd.select('lys13', 'n. CE&r. lys w. %s of n. O&r. gly'%(d*9.99))
cmd.select('lys14', 'n. CE&r. lys w. %s of n. C&r. gly'%(d*9.02))
cmd.select('lys15', 'n. CE&r. lys w. %s of n. CA&r. gly'%(d*8.99))
cmd.select('lys16', 'n. CE&r. lys w. %s of n. N&r. gly'%(d*8.01))
cmd.select('lys17', 'n. NZ&r. lys w. %s of n. O&r. gly'%(d*8.61))
cmd.select('lys18', 'n. NZ&r. lys w. %s of n. C&r. gly'%(d*7.60))
cmd.select('lys19', 'n. NZ&r. lys w. %s of n. CA&r. gly'%(d*7.53))
cmd.select('lys20', 'n. NZ&r. lys w. %s of n. N&r. gly'%(d*6.56))
cmd.select('lys21', 'n. CB&r. lys w. %s of n. MG&r. mg'%(d*6.81))
cmd.select('lys22', 'n. CG&r. lys w. %s of n. MG&r. mg'%(d*7.80))
cmd.select('lys23', 'n. CD&r. lys w. %s of n. MG&r. mg'%(d*7.91))
cmd.select('lys24', 'n. CE&r. lys w. %s of n. MG&r. mg'%(d*6.84))
cmd.select('lys25', 'n. NZ&r. lys w. %s of n. MG&r. mg'%(d*6.68))
cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25')
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
cmd.select('gly1', 'n. O&r. gly w. %s of n. CB&lys'%(d*9.52))
cmd.select('gly2', 'n. O&r. gly w. %s of n. CG&lys'%(d*9.39))
cmd.select('gly3', 'n. O&r. gly w. %s of n. CD&lys'%(d*10.28))
cmd.select('gly4', 'n. O&r. gly w. %s of n. CE&lys'%(d*9.99))
cmd.select('gly5', 'n. O&r. gly w. %s of n. NZ&lys'%(d*8.61))
cmd.select('gly6', 'n. C&r. gly w. %s of n. CB&lys'%(d*8.94))
cmd.select('gly7', 'n. C&r. gly w. %s of n. CG&lys'%(d*8.68))
cmd.select('gly8', 'n. C&r. gly w. %s of n. CD&lys'%(d*9.40))
cmd.select('gly9', 'n. C&r. gly w. %s of n. CE&lys'%(d*9.02))
cmd.select('gly10', 'n. C&r. gly w. %s of n. NZ&lys'%(d*7.60))
cmd.select('gly11', 'n. CA&r. gly w. %s of n. CB&lys'%(d*9.33))
cmd.select('gly12', 'n. CA&r. gly w. %s of n. CG&lys'%(d*9.17))
cmd.select('gly13', 'n. CA&r. gly w. %s of n. CD&lys'%(d*9.66))
cmd.select('gly14', 'n. CA&r. gly w. %s of n. CE&lys'%(d*8.99))
cmd.select('gly15', 'n. CA&r. gly w. %s of n. NZ&lys'%(d*7.53))
cmd.select('gly16', 'n. N&r. gly w. %s of n. CB&lys'%(d*8.88))
cmd.select('gly17', 'n. N&r. gly w. %s of n. CG&lys'%(d*8.62))
cmd.select('gly18', 'n. N&r. gly w. %s of n. CD&lys'%(d*8.85))
cmd.select('gly19', 'n. N&r. gly w. %s of n. CE&lys'%(d*8.01))
cmd.select('gly20', 'n. N&r. gly w. %s of n. NZ&lys'%(d*6.56))
cmd.select('gly21', 'n. O&r. gly w. %s of n. MG&r. mg'%(d*9.84))
cmd.select('gly22', 'n. C&r. gly w. %s of n. MG&r. mg'%(d*9.25))
cmd.select('gly23', 'n. CA&r. gly w. %s of n. MG&r. mg'%(d*8.71))
cmd.select('gly24', 'n. N&r. gly w. %s of n. MG&r. mg'%(d*8.11))
cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24')
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
cmd.select('mg1', 'n. MG&r. mg w. %s of n. CB&lys'%(d*6.81))
cmd.select('mg2', 'n. MG&r. mg w. %s of n. CG&lys'%(d*7.80))
cmd.select('mg3', 'n. MG&r. mg w. %s of n. CD&lys'%(d*7.91))
cmd.select('mg4', 'n. MG&r. mg w. %s of n. CE&lys'%(d*6.84))
cmd.select('mg5', 'n. MG&r. mg w. %s of n. NZ&lys'%(d*6.68))
cmd.select('mg6', 'n. MG&r. mg w. %s of n. O&gly'%(d*9.84))
cmd.select('mg7', 'n. MG&r. mg w. %s of n. C&gly'%(d*9.25))
cmd.select('mg8', 'n. MG&r. mg w. %s of n. CA&gly'%(d*8.71))
cmd.select('mg9', 'n. MG&r. mg w. %s of n. N&gly'%(d*8.11))
cmd.select('mg',' br. mg1&br. mg2&br. mg3&br. mg4&br. mg5&br. mg6&br. mg7&br. mg8&br. mg9')
cmd.delete('mg1')
cmd.delete('mg2')
cmd.delete('mg3')
cmd.delete('mg4')
cmd.delete('mg5')
cmd.delete('mg6')
cmd.delete('mg7')
cmd.delete('mg8')
cmd.delete('mg9')
cmd.select('M_1f48', 'lys|gly|mg')
cmd.delete('lys')
cmd.delete('gly')
cmd.delete('mg')
