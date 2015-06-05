'''
FUNC:M_1ksj
PDB:1ksj
EC:3.1.4.17
PFAM:PF05351,PF01926,PF09439,PF00025,PF00071
RESI:gln,mg
LOCI:a-70,205;
'''
cmd.select('gln1', 'n. CB&r. gln w. %s of n. MG&r. mg'%(d*11.26))
cmd.select('gln2', 'n. CG&r. gln w. %s of n. MG&r. mg'%(d*10.04))
cmd.select('gln3', 'n. CD&r. gln w. %s of n. MG&r. mg'%(d*10.56))
cmd.select('gln4', 'n. OE1&r. gln w. %s of n. MG&r. mg'%(d*11.79))
cmd.select('gln5', 'n. NE2&r. gln w. %s of n. MG&r. mg'%(d*9.80))
cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5')
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. CB&gln'%(d*11.26))
cmd.select('mg2', 'n. MG&r. mg w. %s of n. CG&gln'%(d*10.04))
cmd.select('mg3', 'n. MG&r. mg w. %s of n. CD&gln'%(d*10.56))
cmd.select('mg4', 'n. MG&r. mg w. %s of n. OE1&gln'%(d*11.79))
cmd.select('mg5', 'n. MG&r. mg w. %s of n. NE2&gln'%(d*9.80))
cmd.select('mg',' br. mg1&br. mg2&br. mg3&br. mg4&br. mg5')
cmd.delete('mg1')
cmd.delete('mg2')
cmd.delete('mg3')
cmd.delete('mg4')
cmd.delete('mg5')
cmd.select('M_1ksj', 'gln|mg')
cmd.delete('gln')
cmd.delete('mg')
