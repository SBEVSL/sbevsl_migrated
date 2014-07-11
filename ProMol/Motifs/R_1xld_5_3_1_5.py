'''
FUNC:R_1xld_5_3_1_5
PDB:1xld
EC:5.3.1.5
RESI:mn,mn
LOCI:a-398,399;
'''
cmd.select('mn1', 'n. MN&r. mn w. %s of n. MN&r. mn'%(d*6.68))
cmd.select('mn',' br. mn1')
cmd.delete('mn1')
cmd.select('mni1', 'n. MN&r. mn w. %s of n. MN&mn'%(d*6.68))
cmd.select('mni',' br. mni1')
cmd.delete('mni1')
cmd.select('R_1xld_5_3_1_5', 'mn|mni')
cmd.delete('mn')
cmd.delete('mni')
