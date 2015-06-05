'''
FUNC:M_1ctt
PDB:1ctt
EC:3.5.4.5
PFAM:PF00383,PF08211
RESI:glu,cys,zn
LOCI:a-104,132,296;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. glu'%(d*6.21))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&r. glu'%(d*6.12))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CD&r. glu'%(d*5.83))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. OE1&r. glu'%(d*6.83))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. OE2&r. glu'%(d*5.44))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. CB&r. glu'%(d*5.91))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. CG&r. glu'%(d*6.09))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. CD&r. glu'%(d*5.51))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. OE1&r. glu'%(d*6.02))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. OE2&r. glu'%(d*5.47))
cmd.select('cys11', 'n. CB&r. cys w. %s of n. ZN&r. zn'%(d*5.17))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. ZN&r. zn'%(d*4.11))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&cys'%(d*6.21))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. SG&cys'%(d*5.91))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&cys'%(d*6.12))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. SG&cys'%(d*6.09))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&cys'%(d*5.83))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. SG&cys'%(d*5.51))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&cys'%(d*6.83))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. SG&cys'%(d*6.02))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&cys'%(d*5.44))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. SG&cys'%(d*5.47))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. ZN&r. zn'%(d*7.40))
cmd.select('glu12', 'n. CG&r. glu w. %s of n. ZN&r. zn'%(d*7.09))
cmd.select('glu13', 'n. CD&r. glu w. %s of n. ZN&r. zn'%(d*5.93))
cmd.select('glu14', 'n. OE1&r. glu w. %s of n. ZN&r. zn'%(d*6.17))
cmd.select('glu15', 'n. OE2&r. glu w. %s of n. ZN&r. zn'%(d*5.49))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&cys'%(d*5.17))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. SG&cys'%(d*4.11))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CB&glu'%(d*7.40))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. CG&glu'%(d*7.09))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. CD&glu'%(d*5.93))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. OE1&glu'%(d*6.17))
cmd.select('zn7', 'n. ZN&r. zn w. %s of n. OE2&glu'%(d*5.49))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6&br. zn7')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.delete('zn6')
cmd.delete('zn7')
cmd.select('M_1ctt', 'cys|glu|zn')
cmd.delete('cys')
cmd.delete('glu')
cmd.delete('zn')
