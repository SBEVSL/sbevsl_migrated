'''
FUNC:M_1gp5_1_14_11_19
PDB:1gp5
EC:1.14.11.19
RESI:lys,fe
LOCI:a-213,390;
'''
cmd.select('lys1', 'n. CB&r. lys w. %s of n. FE&r. fe'%(d*11.05))
cmd.select('lys2', 'n. CG&r. lys w. %s of n. FE&r. fe'%(d*11.10))
cmd.select('lys3', 'n. CD&r. lys w. %s of n. FE&r. fe'%(d*10.03))
cmd.select('lys4', 'n. CE&r. lys w. %s of n. FE&r. fe'%(d*10.47))
cmd.select('lys5', 'n. NZ&r. lys w. %s of n. FE&r. fe'%(d*9.68))
cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5')
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.select('fe1', 'n. FE&r. fe w. %s of n. CB&lys'%(d*11.05))
cmd.select('fe2', 'n. FE&r. fe w. %s of n. CG&lys'%(d*11.10))
cmd.select('fe3', 'n. FE&r. fe w. %s of n. CD&lys'%(d*10.03))
cmd.select('fe4', 'n. FE&r. fe w. %s of n. CE&lys'%(d*10.47))
cmd.select('fe5', 'n. FE&r. fe w. %s of n. NZ&lys'%(d*9.68))
cmd.select('fe',' br. fe1&br. fe2&br. fe3&br. fe4&br. fe5')
cmd.delete('fe1')
cmd.delete('fe2')
cmd.delete('fe3')
cmd.delete('fe4')
cmd.delete('fe5')
cmd.select('M_1gp5_1_14_11_19', 'lys|fe')
cmd.delete('lys')
cmd.delete('fe')
