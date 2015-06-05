'''
FUNC:M_2b3i
PDB:2b3i
EC:1.10.99.1
PFAM:PF00127,PF13473
RESI:his,cu1
LOCI:a-85,110;
'''
cmd.select('his1', 'n. CB&r. his w. %s of n. CU&r. cu1'%(d*5.55))
cmd.select('his2', 'n. CG&r. his w. %s of n. CU&r. cu1'%(d*5.12))
cmd.select('his3', 'n. ND1&r. his w. %s of n. CU&r. cu1'%(d*4.03))
cmd.select('his4', 'n. CD2&r. his w. %s of n. CU&r. cu1'%(d*6.19))
cmd.select('his5', 'n. CE1&r. his w. %s of n. CU&r. cu1'%(d*4.92))
cmd.select('his6', 'n. NE2&r. his w. %s of n. CU&r. cu1'%(d*6.10))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.select('cu11', 'n. CU&r. cu1 w. %s of n. CB&his'%(d*5.55))
cmd.select('cu12', 'n. CU&r. cu1 w. %s of n. CG&his'%(d*5.12))
cmd.select('cu13', 'n. CU&r. cu1 w. %s of n. ND1&his'%(d*4.03))
cmd.select('cu14', 'n. CU&r. cu1 w. %s of n. CD2&his'%(d*6.19))
cmd.select('cu15', 'n. CU&r. cu1 w. %s of n. CE1&his'%(d*4.92))
cmd.select('cu16', 'n. CU&r. cu1 w. %s of n. NE2&his'%(d*6.10))
cmd.select('cu1',' br. cu11&br. cu12&br. cu13&br. cu14&br. cu15&br. cu16')
cmd.delete('cu11')
cmd.delete('cu12')
cmd.delete('cu13')
cmd.delete('cu14')
cmd.delete('cu15')
cmd.delete('cu16')
cmd.select('M_2b3i', 'his|cu1')
cmd.delete('his')
cmd.delete('cu1')
