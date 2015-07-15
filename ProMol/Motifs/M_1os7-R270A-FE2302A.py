'''
FUNC:M_1os7-R270A-FE2302A
PDB:1os7
EC:1.14.11.17
PFAM:PF02668
RESI:arg,fe2
LOCI:a-270;a-302;
'''
cmd.select('arg1', 'n. CB&r. arg w. %s of n. FE&r. fe2'%(d*9.53))
cmd.select('arg2', 'n. CG&r. arg w. %s of n. FE&r. fe2'%(d*8.85))
cmd.select('arg3', 'n. CD&r. arg w. %s of n. FE&r. fe2'%(d*7.48))
cmd.select('arg4', 'n. NE&r. arg w. %s of n. FE&r. fe2'%(d*7.52))
cmd.select('arg5', 'n. CZ&r. arg w. %s of n. FE&r. fe2'%(d*6.87))
cmd.select('arg6', 'n. NH1&r. arg w. %s of n. FE&r. fe2'%(d*5.93))
cmd.select('arg7', 'n. NH2&r. arg w. %s of n. FE&r. fe2'%(d*7.53))
cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7')
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.select('fe21', 'n. FE&r. fe2 w. %s of n. CB&arg'%(d*9.53))
cmd.select('fe22', 'n. FE&r. fe2 w. %s of n. CG&arg'%(d*8.85))
cmd.select('fe23', 'n. FE&r. fe2 w. %s of n. CD&arg'%(d*7.48))
cmd.select('fe24', 'n. FE&r. fe2 w. %s of n. NE&arg'%(d*7.52))
cmd.select('fe25', 'n. FE&r. fe2 w. %s of n. CZ&arg'%(d*6.87))
cmd.select('fe26', 'n. FE&r. fe2 w. %s of n. NH1&arg'%(d*5.93))
cmd.select('fe27', 'n. FE&r. fe2 w. %s of n. NH2&arg'%(d*7.53))
cmd.select('fe2',' br. fe21&br. fe22&br. fe23&br. fe24&br. fe25&br. fe26&br. fe27')
cmd.delete('fe21')
cmd.delete('fe22')
cmd.delete('fe23')
cmd.delete('fe24')
cmd.delete('fe25')
cmd.delete('fe26')
cmd.delete('fe27')
cmd.select('M_1os7-R270A-FE2302A', 'arg|fe2')
cmd.delete('arg')
cmd.delete('fe2')