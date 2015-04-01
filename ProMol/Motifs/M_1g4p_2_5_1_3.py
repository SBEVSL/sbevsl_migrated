'''
FUNC:M_1g4p_2_5_1_3
PDB:1g4p
EC:2.5.1.3
RESI:ala,mg
LOCI:a-130,2003;
'''
cmd.select('ala1', 'n. CB&r. ala w. %s of n. MG&r. mg'%(d*8.47))
cmd.select('ala',' br. ala1')
cmd.delete('ala1')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. CB&ala'%(d*8.47))
cmd.select('mg',' br. mg1')
cmd.delete('mg1')
cmd.select('M_1g4p_2_5_1_3', 'ala|mg')
cmd.delete('ala')
cmd.delete('mg')
