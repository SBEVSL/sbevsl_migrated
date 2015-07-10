'''
FUNC:M_1itq-H152A-D288A-ZN401A-ZN402A
PDB:1itq
EC:3.4.13.19
PFAM:PF01244
RESI:his,asp,zn,zn
LOCI:a-152,288,401,402;
'''
cmd.select('zn1', 'n. ZN&r. zn w. %s of n. ZN&r. zn'%(d*5.38))
cmd.select('zn2', 'n. ZN&r. zn w. %s of n. CB&r. his'%(d*9.85))
cmd.select('zn3', 'n. ZN&r. zn w. %s of n. CG&r. his'%(d*8.68))
cmd.select('zn4', 'n. ZN&r. zn w. %s of n. ND1&r. his'%(d*9.02))
cmd.select('zn5', 'n. ZN&r. zn w. %s of n. CD2&r. his'%(d*7.35))
cmd.select('zn6', 'n. ZN&r. zn w. %s of n. CE1&r. his'%(d*8.07))
cmd.select('zn7', 'n. ZN&r. zn w. %s of n. NE2&r. his'%(d*6.90))
cmd.select('zn8', 'n. ZN&r. zn w. %s of n. CB&r. asp'%(d*8.19))
cmd.select('zn9', 'n. ZN&r. zn w. %s of n. CG&r. asp'%(d*6.97))
cmd.select('zn10', 'n. ZN&r. zn w. %s of n. OD1&r. asp'%(d*5.94))
cmd.select('zn11', 'n. ZN&r. zn w. %s of n. OD2&r. asp'%(d*7.31))
cmd.select('zn',' br. zn1&br. zn2&br. zn3&br. zn4&br. zn5&br. zn6&br. zn7&br. zn8&br. zn9&br. zn10&br. zn11')
cmd.delete('zn1')
cmd.delete('zn2')
cmd.delete('zn3')
cmd.delete('zn4')
cmd.delete('zn5')
cmd.delete('zn6')
cmd.delete('zn7')
cmd.delete('zn8')
cmd.delete('zn9')
cmd.delete('zn10')
cmd.delete('zn11')
cmd.select('zni1', 'n. ZN&r. zn w. %s of n. ZN&zn'%(d*5.38))
cmd.select('zni2', 'n. ZN&r. zn w. %s of n. CB&r. his'%(d*8.76))
cmd.select('zni3', 'n. ZN&r. zn w. %s of n. CG&r. his'%(d*7.71))
cmd.select('zni4', 'n. ZN&r. zn w. %s of n. ND1&r. his'%(d*8.10))
cmd.select('zni5', 'n. ZN&r. zn w. %s of n. CD2&r. his'%(d*6.51))
cmd.select('zni6', 'n. ZN&r. zn w. %s of n. CE1&r. his'%(d*7.31))
cmd.select('zni7', 'n. ZN&r. zn w. %s of n. NE2&r. his'%(d*6.22))
cmd.select('zni8', 'n. ZN&r. zn w. %s of n. CB&r. asp'%(d*8.03))
cmd.select('zni9', 'n. ZN&r. zn w. %s of n. CG&r. asp'%(d*6.77))
cmd.select('zni10', 'n. ZN&r. zn w. %s of n. OD1&r. asp'%(d*6.51))
cmd.select('zni11', 'n. ZN&r. zn w. %s of n. OD2&r. asp'%(d*6.38))
cmd.select('zni',' br. zni1&br. zni2&br. zni3&br. zni4&br. zni5&br. zni6&br. zni7&br. zni8&br. zni9&br. zni10&br. zni11')
cmd.delete('zni1')
cmd.delete('zni2')
cmd.delete('zni3')
cmd.delete('zni4')
cmd.delete('zni5')
cmd.delete('zni6')
cmd.delete('zni7')
cmd.delete('zni8')
cmd.delete('zni9')
cmd.delete('zni10')
cmd.delete('zni11')
cmd.select('his1', 'n. CB&r. his w. %s of n. ZN&zn'%(d*9.85))
cmd.select('his2', 'n. CG&r. his w. %s of n. ZN&zn'%(d*8.68))
cmd.select('his3', 'n. ND1&r. his w. %s of n. ZN&zn'%(d*9.02))
cmd.select('his4', 'n. CD2&r. his w. %s of n. ZN&zn'%(d*7.35))
cmd.select('his5', 'n. CE1&r. his w. %s of n. ZN&zn'%(d*8.07))
cmd.select('his6', 'n. NE2&r. his w. %s of n. ZN&zn'%(d*6.90))
cmd.select('his7', 'n. CB&r. his w. %s of n. ZN&zni'%(d*8.76))
cmd.select('his8', 'n. CG&r. his w. %s of n. ZN&zni'%(d*7.71))
cmd.select('his9', 'n. ND1&r. his w. %s of n. ZN&zni'%(d*8.10))
cmd.select('his10', 'n. CD2&r. his w. %s of n. ZN&zni'%(d*6.51))
cmd.select('his11', 'n. CE1&r. his w. %s of n. ZN&zni'%(d*7.31))
cmd.select('his12', 'n. NE2&r. his w. %s of n. ZN&zni'%(d*6.22))
cmd.select('his13', 'n. CB&r. his w. %s of n. CB&r. asp'%(d*14.75))
cmd.select('his14', 'n. CB&r. his w. %s of n. CG&r. asp'%(d*13.40))
cmd.select('his15', 'n. CB&r. his w. %s of n. OD1&r. asp'%(d*12.92))
cmd.select('his16', 'n. CB&r. his w. %s of n. OD2&r. asp'%(d*12.94))
cmd.select('his17', 'n. CG&r. his w. %s of n. CB&r. asp'%(d*13.59))
cmd.select('his18', 'n. CG&r. his w. %s of n. CG&r. asp'%(d*12.19))
cmd.select('his19', 'n. CG&r. his w. %s of n. OD1&r. asp'%(d*11.68))
cmd.select('his20', 'n. CG&r. his w. %s of n. OD2&r. asp'%(d*11.73))
cmd.select('his21', 'n. ND1&r. his w. %s of n. CB&r. asp'%(d*13.75))
cmd.select('his22', 'n. ND1&r. his w. %s of n. CG&r. asp'%(d*12.29))
cmd.select('his23', 'n. ND1&r. his w. %s of n. OD1&r. asp'%(d*11.81))
cmd.select('his24', 'n. ND1&r. his w. %s of n. OD2&r. asp'%(d*11.75))
cmd.select('his25', 'n. CD2&r. his w. %s of n. CB&r. asp'%(d*12.35))
cmd.select('his26', 'n. CD2&r. his w. %s of n. CG&r. asp'%(d*10.96))
cmd.select('his27', 'n. CD2&r. his w. %s of n. OD1&r. asp'%(d*10.40))
cmd.select('his28', 'n. CD2&r. his w. %s of n. OD2&r. asp'%(d*10.58))
cmd.select('his29', 'n. CE1&r. his w. %s of n. CB&r. asp'%(d*12.68))
cmd.select('his30', 'n. CE1&r. his w. %s of n. CG&r. asp'%(d*11.19))
cmd.select('his31', 'n. CE1&r. his w. %s of n. OD1&r. asp'%(d*10.69))
cmd.select('his32', 'n. CE1&r. his w. %s of n. OD2&r. asp'%(d*10.67))
cmd.select('his33', 'n. NE2&r. his w. %s of n. CB&r. asp'%(d*11.74))
cmd.select('his34', 'n. NE2&r. his w. %s of n. CG&r. asp'%(d*10.28))
cmd.select('his35', 'n. NE2&r. his w. %s of n. OD1&r. asp'%(d*9.72))
cmd.select('his36', 'n. NE2&r. his w. %s of n. OD2&r. asp'%(d*9.85))
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
cmd.select('asp1', 'n. CB&r. asp w. %s of n. ZN&zn'%(d*8.19))
cmd.select('asp2', 'n. CG&r. asp w. %s of n. ZN&zn'%(d*6.97))
cmd.select('asp3', 'n. OD1&r. asp w. %s of n. ZN&zn'%(d*5.94))
cmd.select('asp4', 'n. OD2&r. asp w. %s of n. ZN&zn'%(d*7.31))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. ZN&zni'%(d*8.03))
cmd.select('asp6', 'n. CG&r. asp w. %s of n. ZN&zni'%(d*6.77))
cmd.select('asp7', 'n. OD1&r. asp w. %s of n. ZN&zni'%(d*6.51))
cmd.select('asp8', 'n. OD2&r. asp w. %s of n. ZN&zni'%(d*6.38))
cmd.select('asp9', 'n. CB&r. asp w. %s of n. CB&his'%(d*14.75))
cmd.select('asp10', 'n. CB&r. asp w. %s of n. CG&his'%(d*13.59))
cmd.select('asp11', 'n. CB&r. asp w. %s of n. ND1&his'%(d*13.75))
cmd.select('asp12', 'n. CB&r. asp w. %s of n. CD2&his'%(d*12.35))
cmd.select('asp13', 'n. CB&r. asp w. %s of n. CE1&his'%(d*12.68))
cmd.select('asp14', 'n. CB&r. asp w. %s of n. NE2&his'%(d*11.74))
cmd.select('asp15', 'n. CG&r. asp w. %s of n. CB&his'%(d*13.40))
cmd.select('asp16', 'n. CG&r. asp w. %s of n. CG&his'%(d*12.19))
cmd.select('asp17', 'n. CG&r. asp w. %s of n. ND1&his'%(d*12.29))
cmd.select('asp18', 'n. CG&r. asp w. %s of n. CD2&his'%(d*10.96))
cmd.select('asp19', 'n. CG&r. asp w. %s of n. CE1&his'%(d*11.19))
cmd.select('asp20', 'n. CG&r. asp w. %s of n. NE2&his'%(d*10.28))
cmd.select('asp21', 'n. OD1&r. asp w. %s of n. CB&his'%(d*12.92))
cmd.select('asp22', 'n. OD1&r. asp w. %s of n. CG&his'%(d*11.68))
cmd.select('asp23', 'n. OD1&r. asp w. %s of n. ND1&his'%(d*11.81))
cmd.select('asp24', 'n. OD1&r. asp w. %s of n. CD2&his'%(d*10.40))
cmd.select('asp25', 'n. OD1&r. asp w. %s of n. CE1&his'%(d*10.69))
cmd.select('asp26', 'n. OD1&r. asp w. %s of n. NE2&his'%(d*9.72))
cmd.select('asp27', 'n. OD2&r. asp w. %s of n. CB&his'%(d*12.94))
cmd.select('asp28', 'n. OD2&r. asp w. %s of n. CG&his'%(d*11.73))
cmd.select('asp29', 'n. OD2&r. asp w. %s of n. ND1&his'%(d*11.75))
cmd.select('asp30', 'n. OD2&r. asp w. %s of n. CD2&his'%(d*10.58))
cmd.select('asp31', 'n. OD2&r. asp w. %s of n. CE1&his'%(d*10.67))
cmd.select('asp32', 'n. OD2&r. asp w. %s of n. NE2&his'%(d*9.85))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32')
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
cmd.delete('asp29')
cmd.delete('asp30')
cmd.delete('asp31')
cmd.delete('asp32')
cmd.select('M_1itq-H152A-D288A-ZN401A-ZN402A', 'zn|zni|his|asp')
cmd.delete('zn')
cmd.delete('zni')
cmd.delete('his')
cmd.delete('asp')
