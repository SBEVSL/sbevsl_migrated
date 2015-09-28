'''
FUNC:R_1nfs_5_3_3_2
PDB:1nfs
EC:5.3.3.2
RESI:mn,mg
LOCI:a-201,401;
'''
cmd.select('mn1', 'n. MN&r. mn w. %s of n. MG&r. mg'%(d*11.06))
cmd.select('mn',' br. mn1')
cmd.delete('mn1')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. MN&mn'%(d*11.06))
cmd.select('mg',' br. mg1')
cmd.delete('mg1')
cmd.select('R_1nfs_5_3_3_2', 'mn|mg')
cmd.delete('mn')
cmd.delete('mg')
