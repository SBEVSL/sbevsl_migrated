'''
FUNC:N_1nfs
PDB:1nfs
EC:5.3.3.2
PFAM:PF00293
RESI:mn,mg
LOCI:a-201,401;
'''
cmd.select('mn1', 'n. MN&r. mn w. %s of n. MG&r. mg'%(d*11.06))
cmd.select('mn',' br. mn1')
cmd.delete('mn1')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. MN&mn'%(d*11.06))
cmd.select('mg',' br. mg1')
cmd.delete('mg1')
cmd.select('N_1nfs', 'mn|mg')
cmd.delete('mn')
cmd.delete('mg')
