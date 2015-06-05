'''
FUNC:M_1qlh
PDB:1qlh
EC:1.1.1.1
PFAM:PF00107,PF08240
RESI:ser,his,zn,zn
LOCI:a-48,51,375,376;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. his'%(d*7.28))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. his'%(d*7.28))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. ND1&r. his'%(d*6.59))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. CD2&r. his'%(d*8.30))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. CE1&r. his'%(d*7.35))
cmd.select('ser6', 'n. CB&r. ser w. %s of n. NE2&r. his'%(d*8.32))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CB&r. his'%(d*7.80))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CG&r. his'%(d*7.50))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. ND1&r. his'%(d*6.51))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. CD2&r. his'%(d*8.44))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. CE1&r. his'%(d*7.03))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. NE2&r. his'%(d*8.17))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. ZN&r. zn'%(d*6.04))
cmd.select('ser14', 'n. OG&r. ser w. %s of n. ZN&r. zn'%(d*5.85))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. ZN&r. zn'%(d*22.50))
cmd.select('ser16', 'n. OG&r. ser w. %s of n. ZN&r. zn'%(d*22.21))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16')
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
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&ser'%(d*7.28))
cmd.select('his2', 'n. CB&r. his w. %s of n. OG&ser'%(d*7.80))
cmd.select('his3', 'n. CG&r. his w. %s of n. CB&ser'%(d*7.28))
cmd.select('his4', 'n. CG&r. his w. %s of n. OG&ser'%(d*7.50))
cmd.select('his5', 'n. ND1&r. his w. %s of n. CB&ser'%(d*6.59))
cmd.select('his6', 'n. ND1&r. his w. %s of n. OG&ser'%(d*6.51))
cmd.select('his7', 'n. CD2&r. his w. %s of n. CB&ser'%(d*8.30))
cmd.select('his8', 'n. CD2&r. his w. %s of n. OG&ser'%(d*8.44))
cmd.select('his9', 'n. CE1&r. his w. %s of n. CB&ser'%(d*7.35))
cmd.select('his10', 'n. CE1&r. his w. %s of n. OG&ser'%(d*7.03))
cmd.select('his11', 'n. NE2&r. his w. %s of n. CB&ser'%(d*8.32))
cmd.select('his12', 'n. NE2&r. his w. %s of n. OG&ser'%(d*8.17))
cmd.select('his13', 'n. CB&r. his w. %s of n. ZN&r. zn'%(d*11.25))
cmd.select('his14', 'n. CG&r. his w. %s of n. ZN&r. zn'%(d*11.02))
cmd.select('his15', 'n. ND1&r. his w. %s of n. ZN&r. zn'%(d*10.15))
cmd.select('his16', 'n. CD2&r. his w. %s of n. ZN&r. zn'%(d*11.81))
cmd.select('his17', 'n. CE1&r. his w. %s of n. ZN&r. zn'%(d*10.49))
cmd.select('his18', 'n. NE2&r. his w. %s of n. ZN&r. zn'%(d*11.49))
cmd.select('his19', 'n. CB&r. his w. %s of n. ZN&r. zn'%(d*25.96))
cmd.select('his20', 'n. CG&r. his w. %s of n. ZN&r. zn'%(d*26.38))
cmd.select('his21', 'n. ND1&r. his w. %s of n. ZN&r. zn'%(d*25.54))
cmd.select('his22', 'n. CD2&r. his w. %s of n. ZN&r. zn'%(d*27.63))
cmd.select('his23', 'n. CE1&r. his w. %s of n. ZN&r. zn'%(d*26.30))
cmd.select('his24', 'n. NE2&r. his w. %s of n. ZN&r. zn'%(d*27.56))
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
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. CB&ser'%(d*6.04))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. OG&ser'%(d*5.85))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CB&his'%(d*11.25))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. CG&his'%(d*11.02))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. ND1&his'%(d*10.15))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. CD2&his'%(d*11.81))
cmd.select('zn7', 'n. ZN&r. zn w. %s of n. CE1&his'%(d*10.49))
cmd.select('zn8', 'n. ZN&r. zn w. %s of n. NE2&his'%(d*11.49))
cmd.select('zn9', 'n. ZN&r. zn w. %s of n. ZN&r. zn'%(d*21.35))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6&br. zn7&br. zn8&br. zn9')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.delete('zn6')
cmd.delete('zn7')
cmd.delete('zn8')
cmd.delete('zn9')
cmd.select('zni1', 'n. ZN&r. zn w. %s of n. CB&ser'%(d*22.50))
cmd.select('zni2', 'n. ZN&r. zn w. %s of n. OG&ser'%(d*22.21))
cmd.select('zni3', 'n. ZN&r. zn w. %s of n. CB&his'%(d*25.96))
cmd.select('zni4', 'n. ZN&r. zn w. %s of n. CG&his'%(d*26.38))
cmd.select('zni5', 'n. ZN&r. zn w. %s of n. ND1&his'%(d*25.54))
cmd.select('zni6', 'n. ZN&r. zn w. %s of n. CD2&his'%(d*27.63))
cmd.select('zni7', 'n. ZN&r. zn w. %s of n. CE1&his'%(d*26.30))
cmd.select('zni8', 'n. ZN&r. zn w. %s of n. NE2&his'%(d*27.56))
cmd.select('zni9', 'n. ZN&r. zn w. %s of n. ZN&zn'%(d*21.35))
cmd.select('zni',' br. zni1&br. zni2&br. zni3&br. zni4&br. zni5&br. zni6&br. zni7&br. zni8&br. zni9')
cmd.delete('zni1')
cmd.delete('zni2')
cmd.delete('zni3')
cmd.delete('zni4')
cmd.delete('zni5')
cmd.delete('zni6')
cmd.delete('zni7')
cmd.delete('zni8')
cmd.delete('zni9')
cmd.select('M_1qlh', 'ser|his|zn|zni')
cmd.delete('ser')
cmd.delete('his')
cmd.delete('zn')
cmd.delete('zni')
