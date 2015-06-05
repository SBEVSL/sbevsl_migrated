'''
FUNC:N_1nia
PDB:1nia
EC:1.7.2.1
PFAM:PF07732,PF07731,PF00394
RESI:cu,cu
LOCI:a-501,502;
'''
cmd.select('cu1', 'n. CU&r. cu w. %s of n. CU&r. cu'%(d*14.60))
cmd.select('cu',' br. cu1')
cmd.delete('cu1')
cmd.select('cui1', 'n. CU&r. cu w. %s of n. CU&cu'%(d*14.60))
cmd.select('cui',' br. cui1')
cmd.delete('cui1')
cmd.select('N_1nia', 'cu|cui')
cmd.delete('cu')
cmd.delete('cui')
