'''
FUNC:N_1ck7_3_4_24_24
PDB:1ck7
EC:3.4.24.24
RESI:ala,zn
LOCI:a-404,990;
'''
cmd.select('ala1', 'n. CB&r. ala w. %s of n. ZN&r. zn'%(d*7.69))
cmd.select('ala2', 'n. O&r. ala w. %s of n. ZN&r. zn'%(d*7.67))
cmd.select('ala3', 'n. C&r. ala w. %s of n. ZN&r. zn'%(d*7.74))
cmd.select('ala4', 'n. CA&r. ala w. %s of n. ZN&r. zn'%(d*6.83))
cmd.select('ala5', 'n. N&r. ala w. %s of n. ZN&r. zn'%(d*7.02))
cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5')
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&ala'%(d*7.69))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. O&ala'%(d*7.67))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. C&ala'%(d*7.74))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. CA&ala'%(d*6.83))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. N&ala'%(d*7.02))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.select('N_1ck7_3_4_24_24', 'ala|zn')
cmd.delete('ala')
cmd.delete('zn')
