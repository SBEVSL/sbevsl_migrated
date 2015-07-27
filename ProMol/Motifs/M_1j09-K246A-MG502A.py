'''
FUNC:M_1j09-K246A-MG502A
PDB:1j09
EC:6.1.1.17
PFAM:PF00749
RESI:lys,mg
LOCI:a-246,502;
'''
cmd.select('lys1', 'n. CB&r. lys w. %s of n. MG&r. mg'%(d*9.50))
cmd.select('lys2', 'n. CG&r. lys w. %s of n. MG&r. mg'%(d*8.65))
cmd.select('lys3', 'n. CD&r. lys w. %s of n. MG&r. mg'%(d*8.48))
cmd.select('lys4', 'n. CE&r. lys w. %s of n. MG&r. mg'%(d*8.03))
cmd.select('lys5', 'n. NZ&r. lys w. %s of n. MG&r. mg'%(d*8.12))
cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5')
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. CB&lys'%(d*9.50))
cmd.select('mg2', 'n. MG&r. mg w. %s of n. CG&lys'%(d*8.65))
cmd.select('mg3', 'n. MG&r. mg w. %s of n. CD&lys'%(d*8.48))
cmd.select('mg4', 'n. MG&r. mg w. %s of n. CE&lys'%(d*8.03))
cmd.select('mg5', 'n. MG&r. mg w. %s of n. NZ&lys'%(d*8.12))
cmd.select('mg',' br. mg1&br. mg2&br. mg3&br. mg4&br. mg5')
cmd.delete('mg1')
cmd.delete('mg2')
cmd.delete('mg3')
cmd.delete('mg4')
cmd.delete('mg5')
cmd.select('M_1j09-K246A-MG502A', 'lys|mg')
cmd.delete('lys')
cmd.delete('mg')
