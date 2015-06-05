'''
FUNC:N_1hxq
PDB:1hxq
EC:2.7.7.12
PFAM:PF02744,PF01087
RESI:zn,fe
LOCI:a-350,351;
'''
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. FE&r. fe'%(d*31.79))
cmd.select('zn',' br. zn1')
cmd.delete('zn1')
cmd.select('fe1', 'n. FE&r. fe w. %s of n. ZN&zn'%(d*31.79))
cmd.select('fe',' br. fe1')
cmd.delete('fe1')
cmd.select('N_1hxq', 'zn|fe')
cmd.delete('zn')
cmd.delete('fe')
