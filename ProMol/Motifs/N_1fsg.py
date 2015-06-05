'''
FUNC:N_1fsg
PDB:1fsg
EC:2.4.2.8
PFAM:PF00156
RESI:mg,mg
LOCI:a-301,302;
'''
cmd.select('mg1', 'n. MG&r. mg w. %s of n. MG&r. mg'%(d*7.20))
cmd.select('mg',' br. mg1')
cmd.delete('mg1')
cmd.select('mgi1', 'n. MG&r. mg w. %s of n. MG&mg'%(d*7.20))
cmd.select('mgi',' br. mgi1')
cmd.delete('mgi1')
cmd.select('N_1fsg', 'mg|mgi')
cmd.delete('mg')
cmd.delete('mgi')
