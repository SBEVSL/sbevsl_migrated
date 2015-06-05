'''
FUNC:M_1xa8
PDB:1xa8
EC:4.4.1.22
PFAM:PF04828
RESI:cys,zn
LOCI:a-56,200;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. ZN&r. zn'%(d*23.73))
cmd.select('cys2', 'n. SG&r. cys w. %s of n. ZN&r. zn'%(d*23.79))
cmd.select('cys',' br. cys1&br. cys2')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&cys'%(d*23.73))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. SG&cys'%(d*23.79))
cmd.select('zn',' br. zn1&br. zn2')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.select('M_1xa8', 'cys|zn')
cmd.delete('cys')
cmd.delete('zn')
