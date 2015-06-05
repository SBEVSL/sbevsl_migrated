'''
FUNC:M_1fua
PDB:1fua
EC:4.1.2.17
PFAM:PF00596
RESI:glu,zn
LOCI:a-73,216;
'''
cmd.select('glu1', 'n. CB&r. glu w. %s of n. ZN&r. zn'%(d*6.84))
cmd.select('glu2', 'n. CG&r. glu w. %s of n. ZN&r. zn'%(d*5.98))
cmd.select('glu3', 'n. CD&r. glu w. %s of n. ZN&r. zn'%(d*4.46))
cmd.select('glu4', 'n. OE1&r. glu w. %s of n. ZN&r. zn'%(d*4.38))
cmd.select('glu5', 'n. OE2&r. glu w. %s of n. ZN&r. zn'%(d*3.89))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&glu'%(d*6.84))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. CG&glu'%(d*5.98))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CD&glu'%(d*4.46))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. OE1&glu'%(d*4.38))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. OE2&glu'%(d*3.89))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.select('M_1fua', 'glu|zn')
cmd.delete('glu')
cmd.delete('zn')
