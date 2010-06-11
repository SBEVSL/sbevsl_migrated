'''
FUNC:P_1kdn_2_7_4_6
PDB:1kdn
EC:2.7.4.6
RESI:lys,asn
'''
cmd.select('lys1', 'n. CB&r. lys w. %s of n. CB&r. asn'%(d*9.41))
cmd.select('lys2', 'n. CB&r. lys w. %s of n. CG&r. asn'%(d*8.85))
cmd.select('lys3', 'n. CB&r. lys w. %s of n. OD1&r. asn'%(d*7.70))
cmd.select('lys4', 'n. CB&r. lys w. %s of n. ND2&r. asn'%(d*9.87))
cmd.select('lys5', 'n. CG&r. lys w. %s of n. CB&r. asn'%(d*9.01))
cmd.select('lys6', 'n. CG&r. lys w. %s of n. CG&r. asn'%(d*8.21))
cmd.select('lys7', 'n. CG&r. lys w. %s of n. OD1&r. asn'%(d*7.05))
cmd.select('lys8', 'n. CG&r. lys w. %s of n. ND2&r. asn'%(d*9.05))
cmd.select('lys9', 'n. CD&r. lys w. %s of n. CB&r. asn'%(d*7.73))
cmd.select('lys10', 'n. CD&r. lys w. %s of n. CG&r. asn'%(d*6.81))
cmd.select('lys11', 'n. CD&r. lys w. %s of n. OD1&r. asn'%(d*5.61))
cmd.select('lys12', 'n. CD&r. lys w. %s of n. ND2&r. asn'%(d*7.63))
cmd.select('lys13', 'n. CE&r. lys w. %s of n. CB&r. asn'%(d*7.62))
cmd.select('lys14', 'n. CE&r. lys w. %s of n. CG&r. asn'%(d*6.44))
cmd.select('lys15', 'n. CE&r. lys w. %s of n. OD1&r. asn'%(d*5.36))
cmd.select('lys16', 'n. CE&r. lys w. %s of n. ND2&r. asn'%(d*6.95))
cmd.select('lys17', 'n. NZ&r. lys w. %s of n. CB&r. asn'%(d*7.01))
cmd.select('lys18', 'n. NZ&r. lys w. %s of n. CG&r. asn'%(d*5.64))
cmd.select('lys19', 'n. NZ&r. lys w. %s of n. OD1&r. asn'%(d*4.65))
cmd.select('lys20', 'n. NZ&r. lys w. %s of n. ND2&r. asn'%(d*5.94))
cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20')
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
cmd.select('asn1', 'n. CB&r. asn w. %s of n. CB&lys'%(d*9.41))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. CG&lys'%(d*9.01))
cmd.select('asn3', 'n. CB&r. asn w. %s of n. CD&lys'%(d*7.73))
cmd.select('asn4', 'n. CB&r. asn w. %s of n. CE&lys'%(d*7.62))
cmd.select('asn5', 'n. CB&r. asn w. %s of n. NZ&lys'%(d*7.01))
cmd.select('asn6', 'n. CG&r. asn w. %s of n. CB&lys'%(d*8.85))
cmd.select('asn7', 'n. CG&r. asn w. %s of n. CG&lys'%(d*8.21))
cmd.select('asn8', 'n. CG&r. asn w. %s of n. CD&lys'%(d*6.81))
cmd.select('asn9', 'n. CG&r. asn w. %s of n. CE&lys'%(d*6.44))
cmd.select('asn10', 'n. CG&r. asn w. %s of n. NZ&lys'%(d*5.64))
cmd.select('asn11', 'n. OD1&r. asn w. %s of n. CB&lys'%(d*7.70))
cmd.select('asn12', 'n. OD1&r. asn w. %s of n. CG&lys'%(d*7.05))
cmd.select('asn13', 'n. OD1&r. asn w. %s of n. CD&lys'%(d*5.61))
cmd.select('asn14', 'n. OD1&r. asn w. %s of n. CE&lys'%(d*5.36))
cmd.select('asn15', 'n. OD1&r. asn w. %s of n. NZ&lys'%(d*4.65))
cmd.select('asn16', 'n. ND2&r. asn w. %s of n. CB&lys'%(d*9.87))
cmd.select('asn17', 'n. ND2&r. asn w. %s of n. CG&lys'%(d*9.05))
cmd.select('asn18', 'n. ND2&r. asn w. %s of n. CD&lys'%(d*7.63))
cmd.select('asn19', 'n. ND2&r. asn w. %s of n. CE&lys'%(d*6.95))
cmd.select('asn20', 'n. ND2&r. asn w. %s of n. NZ&lys'%(d*5.94))
cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20')
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
cmd.select('P_1kdn_2_7_4_6', 'lys|asn')
cmd.delete('lys')
cmd.delete('asn')
