'''
FUNC:A_1arz
PDB:1arz
EC:1.3.1.26
PFAM:PF05173,PF01113
RESI:his,lys
LOCI:a-159,163;
'''
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&r. lys'%(d*6.17))
cmd.select('his2', 'n. CB&r. his w. %s of n. CG&r. lys'%(d*6.62))
cmd.select('his3', 'n. CB&r. his w. %s of n. CD&r. lys'%(d*5.79))
cmd.select('his4', 'n. CB&r. his w. %s of n. CE&r. lys'%(d*6.95))
cmd.select('his5', 'n. CB&r. his w. %s of n. NZ&r. lys'%(d*8.07))
cmd.select('his6', 'n. CG&r. his w. %s of n. CB&r. lys'%(d*6.86))
cmd.select('his7', 'n. CG&r. his w. %s of n. CG&r. lys'%(d*6.86))
cmd.select('his8', 'n. CG&r. his w. %s of n. CD&r. lys'%(d*5.63))
cmd.select('his9', 'n. CG&r. his w. %s of n. CE&r. lys'%(d*6.41))
cmd.select('his10', 'n. CG&r. his w. %s of n. NZ&r. lys'%(d*7.49))
cmd.select('his11', 'n. ND1&r. his w. %s of n. CB&r. lys'%(d*7.41))
cmd.select('his12', 'n. ND1&r. his w. %s of n. CG&r. lys'%(d*7.11))
cmd.select('his13', 'n. ND1&r. his w. %s of n. CD&r. lys'%(d*5.75))
cmd.select('his14', 'n. ND1&r. his w. %s of n. CE&r. lys'%(d*6.14))
cmd.select('his15', 'n. ND1&r. his w. %s of n. NZ&r. lys'%(d*7.38))
cmd.select('his16', 'n. CD2&r. his w. %s of n. CB&r. lys'%(d*7.55))
cmd.select('his17', 'n. CD2&r. his w. %s of n. CG&r. lys'%(d*7.41))
cmd.select('his18', 'n. CD2&r. his w. %s of n. CD&r. lys'%(d*6.10))
cmd.select('his19', 'n. CD2&r. his w. %s of n. CE&r. lys'%(d*6.67))
cmd.select('his20', 'n. CD2&r. his w. %s of n. NZ&r. lys'%(d*7.45))
cmd.select('his21', 'n. CE1&r. his w. %s of n. CB&r. lys'%(d*8.28))
cmd.select('his22', 'n. CE1&r. his w. %s of n. CG&r. lys'%(d*7.76))
cmd.select('his23', 'n. CE1&r. his w. %s of n. CD&r. lys'%(d*6.26))
cmd.select('his24', 'n. CE1&r. his w. %s of n. CE&r. lys'%(d*6.27))
cmd.select('his25', 'n. CE1&r. his w. %s of n. NZ&r. lys'%(d*7.29))
cmd.select('his26', 'n. NE2&r. his w. %s of n. CB&r. lys'%(d*8.37))
cmd.select('his27', 'n. NE2&r. his w. %s of n. CG&r. lys'%(d*7.93))
cmd.select('his28', 'n. NE2&r. his w. %s of n. CD&r. lys'%(d*6.45))
cmd.select('his29', 'n. NE2&r. his w. %s of n. CE&r. lys'%(d*6.58))
cmd.select('his30', 'n. NE2&r. his w. %s of n. NZ&r. lys'%(d*7.32))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30')
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
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.select('lys1', 'n. CB&r. lys w. %s of n. CB&his'%(d*6.17))
cmd.select('lys2', 'n. CB&r. lys w. %s of n. CG&his'%(d*6.86))
cmd.select('lys3', 'n. CB&r. lys w. %s of n. ND1&his'%(d*7.41))
cmd.select('lys4', 'n. CB&r. lys w. %s of n. CD2&his'%(d*7.55))
cmd.select('lys5', 'n. CB&r. lys w. %s of n. CE1&his'%(d*8.28))
cmd.select('lys6', 'n. CB&r. lys w. %s of n. NE2&his'%(d*8.37))
cmd.select('lys7', 'n. CG&r. lys w. %s of n. CB&his'%(d*6.62))
cmd.select('lys8', 'n. CG&r. lys w. %s of n. CG&his'%(d*6.86))
cmd.select('lys9', 'n. CG&r. lys w. %s of n. ND1&his'%(d*7.11))
cmd.select('lys10', 'n. CG&r. lys w. %s of n. CD2&his'%(d*7.41))
cmd.select('lys11', 'n. CG&r. lys w. %s of n. CE1&his'%(d*7.76))
cmd.select('lys12', 'n. CG&r. lys w. %s of n. NE2&his'%(d*7.93))
cmd.select('lys13', 'n. CD&r. lys w. %s of n. CB&his'%(d*5.79))
cmd.select('lys14', 'n. CD&r. lys w. %s of n. CG&his'%(d*5.63))
cmd.select('lys15', 'n. CD&r. lys w. %s of n. ND1&his'%(d*5.75))
cmd.select('lys16', 'n. CD&r. lys w. %s of n. CD2&his'%(d*6.10))
cmd.select('lys17', 'n. CD&r. lys w. %s of n. CE1&his'%(d*6.26))
cmd.select('lys18', 'n. CD&r. lys w. %s of n. NE2&his'%(d*6.45))
cmd.select('lys19', 'n. CE&r. lys w. %s of n. CB&his'%(d*6.95))
cmd.select('lys20', 'n. CE&r. lys w. %s of n. CG&his'%(d*6.41))
cmd.select('lys21', 'n. CE&r. lys w. %s of n. ND1&his'%(d*6.14))
cmd.select('lys22', 'n. CE&r. lys w. %s of n. CD2&his'%(d*6.67))
cmd.select('lys23', 'n. CE&r. lys w. %s of n. CE1&his'%(d*6.27))
cmd.select('lys24', 'n. CE&r. lys w. %s of n. NE2&his'%(d*6.58))
cmd.select('lys25', 'n. NZ&r. lys w. %s of n. CB&his'%(d*8.07))
cmd.select('lys26', 'n. NZ&r. lys w. %s of n. CG&his'%(d*7.49))
cmd.select('lys27', 'n. NZ&r. lys w. %s of n. ND1&his'%(d*7.38))
cmd.select('lys28', 'n. NZ&r. lys w. %s of n. CD2&his'%(d*7.45))
cmd.select('lys29', 'n. NZ&r. lys w. %s of n. CE1&his'%(d*7.29))
cmd.select('lys30', 'n. NZ&r. lys w. %s of n. NE2&his'%(d*7.32))
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
cmd.select('A_1arz', 'his|lys')
cmd.delete('his')
cmd.delete('lys')
