'''
FUNC:M_1w2n
PDB:1w2n
EC:1.14.20.1
PFAM:PF03171,PF14226
RESI:arg,fe
LOCI:a-74,312;
'''
cmd.select('arg1', 'n. CB&r. arg w. %s of n. FE&r. fe'%(d*16.32))
cmd.select('arg2', 'n. CG&r. arg w. %s of n. FE&r. fe'%(d*16.21))
cmd.select('arg3', 'n. CD&r. arg w. %s of n. FE&r. fe'%(d*17.06))
cmd.select('arg4', 'n. NE&r. arg w. %s of n. FE&r. fe'%(d*16.55))
cmd.select('arg5', 'n. CZ&r. arg w. %s of n. FE&r. fe'%(d*17.33))
cmd.select('arg6', 'n. NH1&r. arg w. %s of n. FE&r. fe'%(d*18.61))
cmd.select('arg7', 'n. NH2&r. arg w. %s of n. FE&r. fe'%(d*16.91))
cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7')
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.select('fe1', 'n. FE&r. fe w. %s of n. CB&arg'%(d*16.32))
cmd.select('fe2', 'n. FE&r. fe w. %s of n. CG&arg'%(d*16.21))
cmd.select('fe3', 'n. FE&r. fe w. %s of n. CD&arg'%(d*17.06))
cmd.select('fe4', 'n. FE&r. fe w. %s of n. NE&arg'%(d*16.55))
cmd.select('fe5', 'n. FE&r. fe w. %s of n. CZ&arg'%(d*17.33))
cmd.select('fe6', 'n. FE&r. fe w. %s of n. NH1&arg'%(d*18.61))
cmd.select('fe7', 'n. FE&r. fe w. %s of n. NH2&arg'%(d*16.91))
cmd.select('fe',' br. fe1&br. fe2&br. fe3&br. fe4&br. fe5&br. fe6&br. fe7')
cmd.delete('fe1')
cmd.delete('fe2')
cmd.delete('fe3')
cmd.delete('fe4')
cmd.delete('fe5')
cmd.delete('fe6')
cmd.delete('fe7')
cmd.select('M_1w2n', 'arg|fe')
cmd.delete('arg')
cmd.delete('fe')
