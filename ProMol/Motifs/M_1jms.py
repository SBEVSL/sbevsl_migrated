'''
FUNC:M_1jms
PDB:1jms
EC:2.7.7.31
PFAM:PF01909,PF14716,PF10391,PF14792,PF14791
RESI:asp,mg
LOCI:a-434,701;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. MG&r. mg'%(d*5.91))
cmd.select('asp2', 'n. CG&r. asp w. %s of n. MG&r. mg'%(d*5.41))
cmd.select('asp3', 'n. OD1&r. asp w. %s of n. MG&r. mg'%(d*6.46))
cmd.select('asp4', 'n. OD2&r. asp w. %s of n. MG&r. mg'%(d*4.35))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4')
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. CB&asp'%(d*5.91))
cmd.select('mg2', 'n. MG&r. mg w. %s of n. CG&asp'%(d*5.41))
cmd.select('mg3', 'n. MG&r. mg w. %s of n. OD1&asp'%(d*6.46))
cmd.select('mg4', 'n. MG&r. mg w. %s of n. OD2&asp'%(d*4.35))
cmd.select('mg',' br. mg1&br. mg2&br. mg3&br. mg4')
cmd.delete('mg1')
cmd.delete('mg2')
cmd.delete('mg3')
cmd.delete('mg4')
cmd.select('M_1jms', 'asp|mg')
cmd.delete('asp')
cmd.delete('mg')
