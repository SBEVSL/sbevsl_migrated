'''
FUNC:M_1goj
PDB:1goj
EC:3.6.4.4
PFAM:PF00225
RESI:gly,mg
LOCI:a-238,401;
'''
cmd.select('gly1', 'n. O&r. gly w. %s of n. MG&r. mg'%(d*12.22))
cmd.select('gly2', 'n. C&r. gly w. %s of n. MG&r. mg'%(d*11.43))
cmd.select('gly3', 'n. CA&r. gly w. %s of n. MG&r. mg'%(d*9.98))
cmd.select('gly4', 'n. N&r. gly w. %s of n. MG&r. mg'%(d*9.48))
cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4')
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. O&gly'%(d*12.22))
cmd.select('mg2', 'n. MG&r. mg w. %s of n. C&gly'%(d*11.43))
cmd.select('mg3', 'n. MG&r. mg w. %s of n. CA&gly'%(d*9.98))
cmd.select('mg4', 'n. MG&r. mg w. %s of n. N&gly'%(d*9.48))
cmd.select('mg',' br. mg1&br. mg2&br. mg3&br. mg4')
cmd.delete('mg1')
cmd.delete('mg2')
cmd.delete('mg3')
cmd.delete('mg4')
cmd.select('M_1goj', 'gly|mg')
cmd.delete('gly')
cmd.delete('mg')
