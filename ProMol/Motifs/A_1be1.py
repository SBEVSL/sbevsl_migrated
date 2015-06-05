'''
FUNC:A_1be1
PDB:1be1
EC:5.4.99.1
PFAM:PF02310
RESI:asp,his
LOCI:a-14,16;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&r. his'%(d*8.09))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. CG&r. his'%(d*8.59))
cmd.select('asp3', 'n. CB&r. asp w. %s of n. ND1&r. his'%(d*8.04))
cmd.select('asp4', 'n. CB&r. asp w. %s of n. CD2&r. his'%(d*9.95))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. CE1&r. his'%(d*9.17))
cmd.select('asp6', 'n. CB&r. asp w. %s of n. NE2&r. his'%(d*10.24))
cmd.select('asp7', 'n. CG&r. asp w. %s of n. CB&r. his'%(d*9.14))
cmd.select('asp8', 'n. CG&r. asp w. %s of n. CG&r. his'%(d*9.59))
cmd.select('asp9', 'n. CG&r. asp w. %s of n. ND1&r. his'%(d*8.93))
cmd.select('asp10', 'n. CG&r. asp w. %s of n. CD2&r. his'%(d*10.95))
cmd.select('asp11', 'n. CG&r. asp w. %s of n. CE1&r. his'%(d*10.00))
cmd.select('asp12', 'n. CG&r. asp w. %s of n. NE2&r. his'%(d*11.15))
cmd.select('asp13', 'n. OD1&r. asp w. %s of n. CB&r. his'%(d*10.22))
cmd.select('asp14', 'n. OD1&r. asp w. %s of n. CG&r. his'%(d*10.75))
cmd.select('asp15', 'n. OD1&r. asp w. %s of n. ND1&r. his'%(d*10.13))
cmd.select('asp16', 'n. OD1&r. asp w. %s of n. CD2&r. his'%(d*12.12))
cmd.select('asp17', 'n. OD1&r. asp w. %s of n. CE1&r. his'%(d*11.22))
cmd.select('asp18', 'n. OD1&r. asp w. %s of n. NE2&r. his'%(d*12.36))
cmd.select('asp19', 'n. OD2&r. asp w. %s of n. CB&r. his'%(d*9.06))
cmd.select('asp20', 'n. OD2&r. asp w. %s of n. CG&r. his'%(d*9.36))
cmd.select('asp21', 'n. OD2&r. asp w. %s of n. ND1&r. his'%(d*8.60))
cmd.select('asp22', 'n. OD2&r. asp w. %s of n. CD2&r. his'%(d*10.68))
cmd.select('asp23', 'n. OD2&r. asp w. %s of n. CE1&r. his'%(d*9.59))
cmd.select('asp24', 'n. OD2&r. asp w. %s of n. NE2&r. his'%(d*10.78))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24')
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&asp'%(d*8.09))
cmd.select('his2', 'n. CB&r. his w. %s of n. CG&asp'%(d*9.14))
cmd.select('his3', 'n. CB&r. his w. %s of n. OD1&asp'%(d*10.22))
cmd.select('his4', 'n. CB&r. his w. %s of n. OD2&asp'%(d*9.06))
cmd.select('his5', 'n. CG&r. his w. %s of n. CB&asp'%(d*8.59))
cmd.select('his6', 'n. CG&r. his w. %s of n. CG&asp'%(d*9.59))
cmd.select('his7', 'n. CG&r. his w. %s of n. OD1&asp'%(d*10.75))
cmd.select('his8', 'n. CG&r. his w. %s of n. OD2&asp'%(d*9.36))
cmd.select('his9', 'n. ND1&r. his w. %s of n. CB&asp'%(d*8.04))
cmd.select('his10', 'n. ND1&r. his w. %s of n. CG&asp'%(d*8.93))
cmd.select('his11', 'n. ND1&r. his w. %s of n. OD1&asp'%(d*10.13))
cmd.select('his12', 'n. ND1&r. his w. %s of n. OD2&asp'%(d*8.60))
cmd.select('his13', 'n. CD2&r. his w. %s of n. CB&asp'%(d*9.95))
cmd.select('his14', 'n. CD2&r. his w. %s of n. CG&asp'%(d*10.95))
cmd.select('his15', 'n. CD2&r. his w. %s of n. OD1&asp'%(d*12.12))
cmd.select('his16', 'n. CD2&r. his w. %s of n. OD2&asp'%(d*10.68))
cmd.select('his17', 'n. CE1&r. his w. %s of n. CB&asp'%(d*9.17))
cmd.select('his18', 'n. CE1&r. his w. %s of n. CG&asp'%(d*10.00))
cmd.select('his19', 'n. CE1&r. his w. %s of n. OD1&asp'%(d*11.22))
cmd.select('his20', 'n. CE1&r. his w. %s of n. OD2&asp'%(d*9.59))
cmd.select('his21', 'n. NE2&r. his w. %s of n. CB&asp'%(d*10.24))
cmd.select('his22', 'n. NE2&r. his w. %s of n. CG&asp'%(d*11.15))
cmd.select('his23', 'n. NE2&r. his w. %s of n. OD1&asp'%(d*12.36))
cmd.select('his24', 'n. NE2&r. his w. %s of n. OD2&asp'%(d*10.78))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.select('A_1be1', 'asp|his')
cmd.delete('asp')
cmd.delete('his')
