'''
FUNC:M_1ck7
PDB:1ck7
EC:3.4.24.24
PFAM:PF00040,PF01471,PF00045,PF00413
RESI:ala,zn
LOCI:a-404,990;
'''
cmd.select('ala1', 'n. CB&r. ala w. %s of n. ZN&r. zn'%(d*8.69))
cmd.select('ala',' br. ala1')
cmd.delete('ala1')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&ala'%(d*8.69))
cmd.select('zn',' br. zn1')
cmd.delete('zn1')
cmd.select('M_1ck7', 'ala|zn')
cmd.delete('ala')
cmd.delete('zn')
