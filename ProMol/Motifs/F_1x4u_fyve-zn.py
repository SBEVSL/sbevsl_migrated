'''
FUNC:F_1x4u_fyve-zn
PDB:1x4u
EC:fyve-zn
RESI:cys,cys,cys,cys,zn
LOCI:a-17,20,41,44,201;
'''
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.33))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.34))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.51))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.33))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.25))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.34))
cmd.select('zn7', 'n. ZN&r. zn w. %s of n. CB&r. cys'%(d*5.51))
cmd.select('zn8', 'n. ZN&r. zn w. %s of n. SG&r. cys'%(d*4.36))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6&br. zn7&br. zn8')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.delete('zn6')
cmd.delete('zn7')
cmd.delete('zn8')
cmd.select('cys1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.33))
cmd.select('cys2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.34))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*7.15))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*5.98))
cmd.select('cys5', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*6.91))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.92))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*7.77))
cmd.select('cys8', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*7.35))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*6.10))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.82))
cmd.select('cys11', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*6.24))
cmd.select('cys12', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*6.55))
cmd.select('cys13', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*6.23))
cmd.select('cys14', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.97))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14')
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
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.51))
cmd.select('cysi2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.33))
cmd.select('cysi3', 'n. CB&r. cys w. %s of n. CB&cys'%(d*7.15))
cmd.select('cysi4', 'n. CB&r. cys w. %s of n. SG&cys'%(d*6.91))
cmd.select('cysi5', 'n. SG&r. cys w. %s of n. CB&cys'%(d*5.98))
cmd.select('cysi6', 'n. SG&r. cys w. %s of n. SG&cys'%(d*5.92))
cmd.select('cysi7', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*8.07))
cmd.select('cysi8', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*6.37))
cmd.select('cysi9', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*7.39))
cmd.select('cysi10', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*6.00))
cmd.select('cysi11', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*8.24))
cmd.select('cysi12', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*7.12))
cmd.select('cysi13', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*6.47))
cmd.select('cysi14', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.55))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12&br. cysi13&br. cysi14')
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
cmd.select('cysii1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.25))
cmd.select('cysii2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.34))
cmd.select('cysii3', 'n. CB&r. cys w. %s of n. CB&cys'%(d*7.77))
cmd.select('cysii4', 'n. CB&r. cys w. %s of n. SG&cys'%(d*6.10))
cmd.select('cysii5', 'n. SG&r. cys w. %s of n. CB&cys'%(d*7.35))
cmd.select('cysii6', 'n. SG&r. cys w. %s of n. SG&cys'%(d*5.82))
cmd.select('cysii7', 'n. CB&r. cys w. %s of n. CB&cysi'%(d*8.07))
cmd.select('cysii8', 'n. CB&r. cys w. %s of n. SG&cysi'%(d*7.39))
cmd.select('cysii9', 'n. SG&r. cys w. %s of n. CB&cysi'%(d*6.37))
cmd.select('cysii10', 'n. SG&r. cys w. %s of n. SG&cysi'%(d*6.00))
cmd.select('cysii11', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*7.08))
cmd.select('cysii12', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*5.77))
cmd.select('cysii13', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*7.19))
cmd.select('cysii14', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*5.61))
cmd.select('cysii',' br. cysii1&br. cysii2&br. cysii3&br. cysii4&br. cysii5&br. cysii6&br. cysii7&br. cysii8&br. cysii9&br. cysii10&br. cysii11&br. cysii12&br. cysii13&br. cysii14')
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
cmd.select('cysiii1', 'n. CB&r. cys w. %s of n. ZN&zn'%(d*5.51))
cmd.select('cysiii2', 'n. SG&r. cys w. %s of n. ZN&zn'%(d*4.36))
cmd.select('cysiii3', 'n. CB&r. cys w. %s of n. CB&cys'%(d*6.24))
cmd.select('cysiii4', 'n. CB&r. cys w. %s of n. SG&cys'%(d*6.23))
cmd.select('cysiii5', 'n. SG&r. cys w. %s of n. CB&cys'%(d*6.55))
cmd.select('cysiii6', 'n. SG&r. cys w. %s of n. SG&cys'%(d*5.97))
cmd.select('cysiii7', 'n. CB&r. cys w. %s of n. CB&cysi'%(d*8.24))
cmd.select('cysiii8', 'n. CB&r. cys w. %s of n. SG&cysi'%(d*6.47))
cmd.select('cysiii9', 'n. SG&r. cys w. %s of n. CB&cysi'%(d*7.12))
cmd.select('cysiii10', 'n. SG&r. cys w. %s of n. SG&cysi'%(d*5.55))
cmd.select('cysiii11', 'n. CB&r. cys w. %s of n. CB&cysii'%(d*7.08))
cmd.select('cysiii12', 'n. CB&r. cys w. %s of n. SG&cysii'%(d*7.19))
cmd.select('cysiii13', 'n. SG&r. cys w. %s of n. CB&cysii'%(d*5.77))
cmd.select('cysiii14', 'n. SG&r. cys w. %s of n. SG&cysii'%(d*5.61))
cmd.select('cysiii',' br. cysiii1&br. cysiii2&br. cysiii3&br. cysiii4&br. cysiii5&br. cysiii6&br. cysiii7&br. cysiii8&br. cysiii9&br. cysiii10&br. cysiii11&br. cysiii12&br. cysiii13&br. cysiii14')
cmd.delete('cysiii1')
cmd.delete('cysiii2')
cmd.delete('cysiii3')
cmd.delete('cysiii4')
cmd.delete('cysiii5')
cmd.delete('cysiii6')
cmd.delete('cysiii7')
cmd.delete('cysiii8')
cmd.delete('cysiii9')
cmd.delete('cysiii10')
cmd.delete('cysiii11')
cmd.delete('cysiii12')
cmd.delete('cysiii13')
cmd.delete('cysiii14')
cmd.select('F_1x4u_fyve-zn', 'zn|cys|cysi|cysii|cysiii')
cmd.delete('zn')
cmd.delete('cys')
cmd.delete('cysi')
cmd.delete('cysii')
cmd.delete('cysiii')
