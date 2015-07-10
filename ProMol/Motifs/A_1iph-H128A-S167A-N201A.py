'''
FUNC:A_1iph-H128A-S167A-N201A
PDB:1iph
EC:1.11.1.6
PFAM:PF00199,PF06628
RESI:his,ser,asn
LOCI:a-128,167,201;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. his'%(d*6.06))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. his'%(d*6.28))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. ND1&r. his'%(d*5.75))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. CD2&r. his'%(d*7.61))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. CE1&r. his'%(d*6.89))
cmd.select('ser6', 'n. CB&r. ser w. %s of n. NE2&r. his'%(d*7.85))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CB&r. his'%(d*5.88))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CG&r. his'%(d*5.64))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. ND1&r. his'%(d*4.84))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. CD2&r. his'%(d*6.83))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. CE1&r. his'%(d*5.80))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. NE2&r. his'%(d*6.85))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. CB&r. asn'%(d*10.90))
cmd.select('ser14', 'n. CB&r. ser w. %s of n. CG&r. asn'%(d*10.59))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. OD1&r. asn'%(d*9.63))
cmd.select('ser16', 'n. CB&r. ser w. %s of n. ND2&r. asn'%(d*11.77))
cmd.select('ser17', 'n. OG&r. ser w. %s of n. CB&r. asn'%(d*9.59))
cmd.select('ser18', 'n. OG&r. ser w. %s of n. CG&r. asn'%(d*9.27))
cmd.select('ser19', 'n. OG&r. ser w. %s of n. OD1&r. asn'%(d*8.30))
cmd.select('ser20', 'n. OG&r. ser w. %s of n. ND2&r. asn'%(d*10.47))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&ser'%(d*6.06))
cmd.select('his2', 'n. CB&r. his w. %s of n. OG&ser'%(d*5.88))
cmd.select('his3', 'n. CG&r. his w. %s of n. CB&ser'%(d*6.28))
cmd.select('his4', 'n. CG&r. his w. %s of n. OG&ser'%(d*5.64))
cmd.select('his5', 'n. ND1&r. his w. %s of n. CB&ser'%(d*5.75))
cmd.select('his6', 'n. ND1&r. his w. %s of n. OG&ser'%(d*4.84))
cmd.select('his7', 'n. CD2&r. his w. %s of n. CB&ser'%(d*7.61))
cmd.select('his8', 'n. CD2&r. his w. %s of n. OG&ser'%(d*6.83))
cmd.select('his9', 'n. CE1&r. his w. %s of n. CB&ser'%(d*6.89))
cmd.select('his10', 'n. CE1&r. his w. %s of n. OG&ser'%(d*5.80))
cmd.select('his11', 'n. NE2&r. his w. %s of n. CB&ser'%(d*7.85))
cmd.select('his12', 'n. NE2&r. his w. %s of n. OG&ser'%(d*6.85))
cmd.select('his13', 'n. CB&r. his w. %s of n. CB&r. asn'%(d*11.29))
cmd.select('his14', 'n. CB&r. his w. %s of n. CG&r. asn'%(d*10.35))
cmd.select('his15', 'n. CB&r. his w. %s of n. OD1&r. asn'%(d*9.16))
cmd.select('his16', 'n. CB&r. his w. %s of n. ND2&r. asn'%(d*11.26))
cmd.select('his17', 'n. CG&r. his w. %s of n. CB&r. asn'%(d*9.84))
cmd.select('his18', 'n. CG&r. his w. %s of n. CG&r. asn'%(d*8.85))
cmd.select('his19', 'n. CG&r. his w. %s of n. OD1&r. asn'%(d*7.66))
cmd.select('his20', 'n. CG&r. his w. %s of n. ND2&r. asn'%(d*9.74))
cmd.select('his21', 'n. ND1&r. his w. %s of n. CB&r. asn'%(d*8.76))
cmd.select('his22', 'n. ND1&r. his w. %s of n. CG&r. asn'%(d*7.92))
cmd.select('his23', 'n. ND1&r. his w. %s of n. OD1&r. asn'%(d*6.78))
cmd.select('his24', 'n. ND1&r. his w. %s of n. ND2&r. asn'%(d*8.90))
cmd.select('his25', 'n. CD2&r. his w. %s of n. CB&r. asn'%(d*9.58))
cmd.select('his26', 'n. CD2&r. his w. %s of n. CG&r. asn'%(d*8.40))
cmd.select('his27', 'n. CD2&r. his w. %s of n. OD1&r. asn'%(d*7.20))
cmd.select('his28', 'n. CD2&r. his w. %s of n. ND2&r. asn'%(d*9.12))
cmd.select('his29', 'n. CE1&r. his w. %s of n. CB&r. asn'%(d*7.72))
cmd.select('his30', 'n. CE1&r. his w. %s of n. CG&r. asn'%(d*6.74))
cmd.select('his31', 'n. CE1&r. his w. %s of n. OD1&r. asn'%(d*5.57))
cmd.select('his32', 'n. CE1&r. his w. %s of n. ND2&r. asn'%(d*7.65))
cmd.select('his33', 'n. NE2&r. his w. %s of n. CB&r. asn'%(d*8.30))
cmd.select('his34', 'n. NE2&r. his w. %s of n. CG&r. asn'%(d*7.09))
cmd.select('his35', 'n. NE2&r. his w. %s of n. OD1&r. asn'%(d*5.92))
cmd.select('his36', 'n. NE2&r. his w. %s of n. ND2&r. asn'%(d*7.81))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36')
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
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
cmd.select('asn1', 'n. CB&r. asn w. %s of n. CB&ser'%(d*10.90))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. OG&ser'%(d*9.59))
cmd.select('asn3', 'n. CG&r. asn w. %s of n. CB&ser'%(d*10.59))
cmd.select('asn4', 'n. CG&r. asn w. %s of n. OG&ser'%(d*9.27))
cmd.select('asn5', 'n. OD1&r. asn w. %s of n. CB&ser'%(d*9.63))
cmd.select('asn6', 'n. OD1&r. asn w. %s of n. OG&ser'%(d*8.30))
cmd.select('asn7', 'n. ND2&r. asn w. %s of n. CB&ser'%(d*11.77))
cmd.select('asn8', 'n. ND2&r. asn w. %s of n. OG&ser'%(d*10.47))
cmd.select('asn9', 'n. CB&r. asn w. %s of n. CB&his'%(d*11.29))
cmd.select('asn10', 'n. CB&r. asn w. %s of n. CG&his'%(d*9.84))
cmd.select('asn11', 'n. CB&r. asn w. %s of n. ND1&his'%(d*8.76))
cmd.select('asn12', 'n. CB&r. asn w. %s of n. CD2&his'%(d*9.58))
cmd.select('asn13', 'n. CB&r. asn w. %s of n. CE1&his'%(d*7.72))
cmd.select('asn14', 'n. CB&r. asn w. %s of n. NE2&his'%(d*8.30))
cmd.select('asn15', 'n. CG&r. asn w. %s of n. CB&his'%(d*10.35))
cmd.select('asn16', 'n. CG&r. asn w. %s of n. CG&his'%(d*8.85))
cmd.select('asn17', 'n. CG&r. asn w. %s of n. ND1&his'%(d*7.92))
cmd.select('asn18', 'n. CG&r. asn w. %s of n. CD2&his'%(d*8.40))
cmd.select('asn19', 'n. CG&r. asn w. %s of n. CE1&his'%(d*6.74))
cmd.select('asn20', 'n. CG&r. asn w. %s of n. NE2&his'%(d*7.09))
cmd.select('asn21', 'n. OD1&r. asn w. %s of n. CB&his'%(d*9.16))
cmd.select('asn22', 'n. OD1&r. asn w. %s of n. CG&his'%(d*7.66))
cmd.select('asn23', 'n. OD1&r. asn w. %s of n. ND1&his'%(d*6.78))
cmd.select('asn24', 'n. OD1&r. asn w. %s of n. CD2&his'%(d*7.20))
cmd.select('asn25', 'n. OD1&r. asn w. %s of n. CE1&his'%(d*5.57))
cmd.select('asn26', 'n. OD1&r. asn w. %s of n. NE2&his'%(d*5.92))
cmd.select('asn27', 'n. ND2&r. asn w. %s of n. CB&his'%(d*11.26))
cmd.select('asn28', 'n. ND2&r. asn w. %s of n. CG&his'%(d*9.74))
cmd.select('asn29', 'n. ND2&r. asn w. %s of n. ND1&his'%(d*8.90))
cmd.select('asn30', 'n. ND2&r. asn w. %s of n. CD2&his'%(d*9.12))
cmd.select('asn31', 'n. ND2&r. asn w. %s of n. CE1&his'%(d*7.65))
cmd.select('asn32', 'n. ND2&r. asn w. %s of n. NE2&his'%(d*7.81))
cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32')
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
cmd.delete('asn19')
cmd.delete('asn20')
cmd.delete('asn21')
cmd.delete('asn22')
cmd.delete('asn23')
cmd.delete('asn24')
cmd.delete('asn25')
cmd.delete('asn26')
cmd.delete('asn27')
cmd.delete('asn28')
cmd.delete('asn29')
cmd.delete('asn30')
cmd.delete('asn31')
cmd.delete('asn32')
cmd.select('A_1iph-H128A-S167A-N201A', 'ser|his|asn')
cmd.delete('ser')
cmd.delete('his')
cmd.delete('asn')
