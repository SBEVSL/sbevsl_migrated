'''
FUNC:M_2phk_2_7_11_19
PDB:2phk
EC:2.7.11.19
RESI:asp,lys,mn,mn
LOCI:a-149,151,382,383;
'''
cmd.select('lys1', 'n. CB&r. lys w. %s of n. CB&r. asp'%(d*8.50))
cmd.select('lys2', 'n. CB&r. lys w. %s of n. CG&r. asp'%(d*7.92))
cmd.select('lys3', 'n. CB&r. lys w. %s of n. OD1&r. asp'%(d*7.18))
cmd.select('lys4', 'n. CB&r. lys w. %s of n. OD2&r. asp'%(d*8.48))
cmd.select('lys5', 'n. CG&r. lys w. %s of n. CB&r. asp'%(d*7.79))
cmd.select('lys6', 'n. CG&r. lys w. %s of n. CG&r. asp'%(d*7.02))
cmd.select('lys7', 'n. CG&r. lys w. %s of n. OD1&r. asp'%(d*6.45))
cmd.select('lys8', 'n. CG&r. lys w. %s of n. OD2&r. asp'%(d*7.35))
cmd.select('lys9', 'n. CD&r. lys w. %s of n. CB&r. asp'%(d*8.02))
cmd.select('lys10', 'n. CD&r. lys w. %s of n. CG&r. asp'%(d*6.93))
cmd.select('lys11', 'n. CD&r. lys w. %s of n. OD1&r. asp'%(d*6.19))
cmd.select('lys12', 'n. CD&r. lys w. %s of n. OD2&r. asp'%(d*7.11))
cmd.select('lys13', 'n. CE&r. lys w. %s of n. CB&r. asp'%(d*7.88))
cmd.select('lys14', 'n. CE&r. lys w. %s of n. CG&r. asp'%(d*6.62))
cmd.select('lys15', 'n. CE&r. lys w. %s of n. OD1&r. asp'%(d*6.17))
cmd.select('lys16', 'n. CE&r. lys w. %s of n. OD2&r. asp'%(d*6.43))
cmd.select('lys17', 'n. NZ&r. lys w. %s of n. CB&r. asp'%(d*8.05))
cmd.select('lys18', 'n. NZ&r. lys w. %s of n. CG&r. asp'%(d*6.61))
cmd.select('lys19', 'n. NZ&r. lys w. %s of n. OD1&r. asp'%(d*6.09))
cmd.select('lys20', 'n. NZ&r. lys w. %s of n. OD2&r. asp'%(d*6.28))
cmd.select('lys21', 'n. CB&r. lys w. %s of n. MN&r. mn'%(d*11.63))
cmd.select('lys22', 'n. CG&r. lys w. %s of n. MN&r. mn'%(d*10.24))
cmd.select('lys23', 'n. CD&r. lys w. %s of n. MN&r. mn'%(d*9.91))
cmd.select('lys24', 'n. CE&r. lys w. %s of n. MN&r. mn'%(d*8.66))
cmd.select('lys25', 'n. NZ&r. lys w. %s of n. MN&r. mn'%(d*8.36))
cmd.select('lys26', 'n. CB&r. lys w. %s of n. MN&r. mn'%(d*9.46))
cmd.select('lys27', 'n. CG&r. lys w. %s of n. MN&r. mn'%(d*7.96))
cmd.select('lys28', 'n. CD&r. lys w. %s of n. MN&r. mn'%(d*7.71))
cmd.select('lys29', 'n. CE&r. lys w. %s of n. MN&r. mn'%(d*6.31))
cmd.select('lys30', 'n. NZ&r. lys w. %s of n. MN&r. mn'%(d*6.58))
cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27&br. lys28&br. lys29&br. lys30')
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
cmd.delete('lys28')
cmd.delete('lys29')
cmd.delete('lys30')
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&lys'%(d*8.50))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. CG&lys'%(d*7.79))
cmd.select('asp3', 'n. CB&r. asp w. %s of n. CD&lys'%(d*8.02))
cmd.select('asp4', 'n. CB&r. asp w. %s of n. CE&lys'%(d*7.88))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. NZ&lys'%(d*8.05))
cmd.select('asp6', 'n. CG&r. asp w. %s of n. CB&lys'%(d*7.92))
cmd.select('asp7', 'n. CG&r. asp w. %s of n. CG&lys'%(d*7.02))
cmd.select('asp8', 'n. CG&r. asp w. %s of n. CD&lys'%(d*6.93))
cmd.select('asp9', 'n. CG&r. asp w. %s of n. CE&lys'%(d*6.62))
cmd.select('asp10', 'n. CG&r. asp w. %s of n. NZ&lys'%(d*6.61))
cmd.select('asp11', 'n. OD1&r. asp w. %s of n. CB&lys'%(d*7.18))
cmd.select('asp12', 'n. OD1&r. asp w. %s of n. CG&lys'%(d*6.45))
cmd.select('asp13', 'n. OD1&r. asp w. %s of n. CD&lys'%(d*6.19))
cmd.select('asp14', 'n. OD1&r. asp w. %s of n. CE&lys'%(d*6.17))
cmd.select('asp15', 'n. OD1&r. asp w. %s of n. NZ&lys'%(d*6.09))
cmd.select('asp16', 'n. OD2&r. asp w. %s of n. CB&lys'%(d*8.48))
cmd.select('asp17', 'n. OD2&r. asp w. %s of n. CG&lys'%(d*7.35))
cmd.select('asp18', 'n. OD2&r. asp w. %s of n. CD&lys'%(d*7.11))
cmd.select('asp19', 'n. OD2&r. asp w. %s of n. CE&lys'%(d*6.43))
cmd.select('asp20', 'n. OD2&r. asp w. %s of n. NZ&lys'%(d*6.28))
cmd.select('asp21', 'n. CB&r. asp w. %s of n. MN&r. mn'%(d*7.69))
cmd.select('asp22', 'n. CG&r. asp w. %s of n. MN&r. mn'%(d*7.10))
cmd.select('asp23', 'n. OD1&r. asp w. %s of n. MN&r. mn'%(d*8.07))
cmd.select('asp24', 'n. OD2&r. asp w. %s of n. MN&r. mn'%(d*5.91))
cmd.select('asp25', 'n. CB&r. asp w. %s of n. MN&r. mn'%(d*8.64))
cmd.select('asp26', 'n. CG&r. asp w. %s of n. MN&r. mn'%(d*7.71))
cmd.select('asp27', 'n. OD1&r. asp w. %s of n. MN&r. mn'%(d*8.22))
cmd.select('asp28', 'n. OD2&r. asp w. %s of n. MN&r. mn'%(d*6.73))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28')
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
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
cmd.delete('asp28')
cmd.select('mn1', 'n. MN&r. mn w. %s of n. CB&lys'%(d*11.63))
cmd.select('mn2', 'n. MN&r. mn w. %s of n. CG&lys'%(d*10.24))
cmd.select('mn3', 'n. MN&r. mn w. %s of n. CD&lys'%(d*9.91))
cmd.select('mn4', 'n. MN&r. mn w. %s of n. CE&lys'%(d*8.66))
cmd.select('mn5', 'n. MN&r. mn w. %s of n. NZ&lys'%(d*8.36))
cmd.select('mn6', 'n. MN&r. mn w. %s of n. CB&asp'%(d*7.69))
cmd.select('mn7', 'n. MN&r. mn w. %s of n. CG&asp'%(d*7.10))
cmd.select('mn8', 'n. MN&r. mn w. %s of n. OD1&asp'%(d*8.07))
cmd.select('mn9', 'n. MN&r. mn w. %s of n. OD2&asp'%(d*5.91))
cmd.select('mn10', 'n. MN&r. mn w. %s of n. MN&r. mn'%(d*5.91))
cmd.select('mn',' br. mn1&br. mn2&br. mn3&br. mn4&br. mn5&br. mn6&br. mn7&br. mn8&br. mn9&br. mn10')
cmd.delete('mn1')
cmd.delete('mn2')
cmd.delete('mn3')
cmd.delete('mn4')
cmd.delete('mn5')
cmd.delete('mn6')
cmd.delete('mn7')
cmd.delete('mn8')
cmd.delete('mn9')
cmd.delete('mn10')
cmd.select('mni1', 'n. MN&r. mn w. %s of n. CB&lys'%(d*9.46))
cmd.select('mni2', 'n. MN&r. mn w. %s of n. CG&lys'%(d*7.96))
cmd.select('mni3', 'n. MN&r. mn w. %s of n. CD&lys'%(d*7.71))
cmd.select('mni4', 'n. MN&r. mn w. %s of n. CE&lys'%(d*6.31))
cmd.select('mni5', 'n. MN&r. mn w. %s of n. NZ&lys'%(d*6.58))
cmd.select('mni6', 'n. MN&r. mn w. %s of n. CB&asp'%(d*8.64))
cmd.select('mni7', 'n. MN&r. mn w. %s of n. CG&asp'%(d*7.71))
cmd.select('mni8', 'n. MN&r. mn w. %s of n. OD1&asp'%(d*8.22))
cmd.select('mni9', 'n. MN&r. mn w. %s of n. OD2&asp'%(d*6.73))
cmd.select('mni10', 'n. MN&r. mn w. %s of n. MN&mn'%(d*5.91))
cmd.select('mni',' br. mni1&br. mni2&br. mni3&br. mni4&br. mni5&br. mni6&br. mni7&br. mni8&br. mni9&br. mni10')
cmd.delete('mni1')
cmd.delete('mni2')
cmd.delete('mni3')
cmd.delete('mni4')
cmd.delete('mni5')
cmd.delete('mni6')
cmd.delete('mni7')
cmd.delete('mni8')
cmd.delete('mni9')
cmd.delete('mni10')
cmd.select('M_2phk_2_7_11_19', 'lys|asp|mn|mni')
cmd.delete('lys')
cmd.delete('asp')
cmd.delete('mn')
cmd.delete('mni')
