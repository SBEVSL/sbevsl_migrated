'''
FUNC:M_1dqs-H275A-ZN402A
PDB:1dqs
EC:4.6.1.3
PFAM:PF13685,PF00465,PF01761
RESI:his,zn
LOCI:a-275,402;
'''
cmd.select('his1', 'n. CB&r. his w. %s of n. ZN&r. zn'%(d*10.16))
cmd.select('his2', 'n. CG&r. his w. %s of n. ZN&r. zn'%(d*8.87))
cmd.select('his3', 'n. ND1&r. his w. %s of n. ZN&r. zn'%(d*8.55))
cmd.select('his4', 'n. CD2&r. his w. %s of n. ZN&r. zn'%(d*8.03))
cmd.select('his5', 'n. CE1&r. his w. %s of n. ZN&r. zn'%(d*7.56))
cmd.select('his6', 'n. NE2&r. his w. %s of n. ZN&r. zn'%(d*7.13))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&his'%(d*10.16))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. CG&his'%(d*8.87))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. ND1&his'%(d*8.55))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. CD2&his'%(d*8.03))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. CE1&his'%(d*7.56))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. NE2&his'%(d*7.13))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.delete('zn6')
cmd.select('M_1dqs-H275A-ZN402A', 'his|zn')
cmd.delete('his')
cmd.delete('zn')
