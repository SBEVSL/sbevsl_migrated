'''
FUNC:M_1qh5-D58A-ZN261A-ZN262A
PDB:1qh5
EC:3.1.2.6
PFAM:PF00753
RESI:asp,zn,zn
LOCI:a-58,261,262;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. ZN&r. zn'%(d*8.67))
cmd.select('asp2', 'n. CG&r. asp w. %s of n. ZN&r. zn'%(d*7.19))
cmd.select('asp3', 'n. OD1&r. asp w. %s of n. ZN&r. zn'%(d*6.53))
cmd.select('asp4', 'n. OD2&r. asp w. %s of n. ZN&r. zn'%(d*6.92))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. ZN&r. zn'%(d*6.58))
cmd.select('asp6', 'n. CG&r. asp w. %s of n. ZN&r. zn'%(d*5.29))
cmd.select('asp7', 'n. OD1&r. asp w. %s of n. ZN&r. zn'%(d*5.55))
cmd.select('asp8', 'n. OD2&r. asp w. %s of n. ZN&r. zn'%(d*4.28))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8')
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&asp'%(d*8.67))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. CG&asp'%(d*7.19))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. OD1&asp'%(d*6.53))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. OD2&asp'%(d*6.92))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. ZN&r. zn'%(d*5.46))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.select('zni1', 'n. ZN&r. zn w. %s of n. CB&asp'%(d*6.58))
cmd.select('zni2', 'n. ZN&r. zn w. %s of n. CG&asp'%(d*5.29))
cmd.select('zni3', 'n. ZN&r. zn w. %s of n. OD1&asp'%(d*5.55))
cmd.select('zni4', 'n. ZN&r. zn w. %s of n. OD2&asp'%(d*4.28))
cmd.select('zni5', 'n. ZN&r. zn w. %s of n. ZN&zn'%(d*5.46))
cmd.select('zni',' br. zni1&br. zni2&br. zni3&br. zni4&br. zni5')
cmd.delete('zni1')
cmd.delete('zni2')
cmd.delete('zni3')
cmd.delete('zni4')
cmd.delete('zni5')
cmd.select('M_1qh5-D58A-ZN261A-ZN262A', 'asp|zn|zni')
cmd.delete('asp')
cmd.delete('zn')
cmd.delete('zni')
