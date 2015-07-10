'''
FUNC:M_1rdd-H124A-MG300A
PDB:1rdd
EC:3.1.26.4
PFAM:PF00075
RESI:his,mg
LOCI:a-124,300;
'''
cmd.select('his1', 'n. CB&r. his w. %s of n. MG&r. mg'%(d*12.88))
cmd.select('his2', 'n. CG&r. his w. %s of n. MG&r. mg'%(d*14.06))
cmd.select('his3', 'n. ND1&r. his w. %s of n. MG&r. mg'%(d*15.35))
cmd.select('his4', 'n. CD2&r. his w. %s of n. MG&r. mg'%(d*14.21))
cmd.select('his5', 'n. CE1&r. his w. %s of n. MG&r. mg'%(d*16.16))
cmd.select('his6', 'n. NE2&r. his w. %s of n. MG&r. mg'%(d*15.55))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.select('mg1', 'n. MG&r. mg w. %s of n. CB&his'%(d*12.88))
cmd.select('mg2', 'n. MG&r. mg w. %s of n. CG&his'%(d*14.06))
cmd.select('mg3', 'n. MG&r. mg w. %s of n. ND1&his'%(d*15.35))
cmd.select('mg4', 'n. MG&r. mg w. %s of n. CD2&his'%(d*14.21))
cmd.select('mg5', 'n. MG&r. mg w. %s of n. CE1&his'%(d*16.16))
cmd.select('mg6', 'n. MG&r. mg w. %s of n. NE2&his'%(d*15.55))
cmd.select('mg',' br. mg1&br. mg2&br. mg3&br. mg4&br. mg5&br. mg6')
cmd.delete('mg1')
cmd.delete('mg2')
cmd.delete('mg3')
cmd.delete('mg4')
cmd.delete('mg5')
cmd.delete('mg6')
cmd.select('M_1rdd-H124A-MG300A', 'his|mg')
cmd.delete('his')
cmd.delete('mg')
