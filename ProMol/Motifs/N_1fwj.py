'''
FUNC:N_1fwj
PDB:1fwj
EC:3.5.1.5
PFAM:PF00699,PF13594,PF00547,PF00449,PF01979
RESI:ni,ni
LOCI:c-574,575;
'''
cmd.select('ni1', 'n. NI&r. ni w. %s of n. NI&r. ni'%(d*5.59))
cmd.select('ni',' br. ni1')
cmd.delete('ni1')
cmd.select('nii1', 'n. NI&r. ni w. %s of n. NI&ni'%(d*5.59))
cmd.select('nii',' br. nii1')
cmd.delete('nii1')
cmd.select('N_1fwj', 'ni|nii')
cmd.delete('ni')
cmd.delete('nii')
