'''
FUNC:M_1kws-E281A-MN500A
PDB:1kws
EC:2.4.1.135
PFAM:PF03360
RESI:glu,mn
LOCI:a-281,500;
'''
cmd.select('glu1', 'n. CB&r. glu w. %s of n. MN&r. mn'%(d*15.24))
cmd.select('glu2', 'n. CG&r. glu w. %s of n. MN&r. mn'%(d*13.74))
cmd.select('glu3', 'n. CD&r. glu w. %s of n. MN&r. mn'%(d*12.93))
cmd.select('glu4', 'n. OE1&r. glu w. %s of n. MN&r. mn'%(d*13.63))
cmd.select('glu5', 'n. OE2&r. glu w. %s of n. MN&r. mn'%(d*11.70))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.select('mn1', 'n. MN&r. mn w. %s of n. CB&glu'%(d*15.24))
cmd.select('mn2', 'n. MN&r. mn w. %s of n. CG&glu'%(d*13.74))
cmd.select('mn3', 'n. MN&r. mn w. %s of n. CD&glu'%(d*12.93))
cmd.select('mn4', 'n. MN&r. mn w. %s of n. OE1&glu'%(d*13.63))
cmd.select('mn5', 'n. MN&r. mn w. %s of n. OE2&glu'%(d*11.70))
cmd.select('mn',' br. mn1&br. mn2&br. mn3&br. mn4&br. mn5')
cmd.delete('mn1')
cmd.delete('mn2')
cmd.delete('mn3')
cmd.delete('mn4')
cmd.delete('mn5')
cmd.select('M_1kws-E281A-MN500A', 'glu|mn')
cmd.delete('glu')
cmd.delete('mn')
