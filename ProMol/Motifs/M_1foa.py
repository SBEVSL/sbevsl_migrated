'''
FUNC:M_1foa
PDB:1foa
EC:2.4.1.101
PFAM:PF03071
RESI:asp,mn
LOCI:a-291;a-448;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. MN&r. mn'%(d*13.00))
cmd.select('asp2', 'n. CG&r. asp w. %s of n. MN&r. mn'%(d*12.21))
cmd.select('asp3', 'n. OD1&r. asp w. %s of n. MN&r. mn'%(d*11.35))
cmd.select('asp4', 'n. OD2&r. asp w. %s of n. MN&r. mn'%(d*12.60))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4')
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.select('mn1', 'n. MN&r. mn w. %s of n. CB&asp'%(d*13.00))
cmd.select('mn2', 'n. MN&r. mn w. %s of n. CG&asp'%(d*12.21))
cmd.select('mn3', 'n. MN&r. mn w. %s of n. OD1&asp'%(d*11.35))
cmd.select('mn4', 'n. MN&r. mn w. %s of n. OD2&asp'%(d*12.60))
cmd.select('mn',' br. mn1&br. mn2&br. mn3&br. mn4')
cmd.delete('mn1')
cmd.delete('mn2')
cmd.delete('mn3')
cmd.delete('mn4')
cmd.select('M_1foa', 'asp|mn')
cmd.delete('asp')
cmd.delete('mn')
