'''
FUNC:A_2cpu-D197A-E233A-N300A
PDB:2cpu
EC:3.2.1.1
PFAM:PF02806,PF00128
RESI:asp,glu,asn
LOCI:a-197,233,300;
'''
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&r. glu'%(d*7.74))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. CG&r. glu'%(d*8.47))
cmd.select('asp3', 'n. CB&r. asp w. %s of n. CD&r. glu'%(d*7.85))
cmd.select('asp4', 'n. CB&r. asp w. %s of n. OE1&r. glu'%(d*6.90))
cmd.select('asp5', 'n. CB&r. asp w. %s of n. OE2&r. glu'%(d*8.57))
cmd.select('asp6', 'n. CG&r. asp w. %s of n. CB&r. glu'%(d*7.96))
cmd.select('asp7', 'n. CG&r. asp w. %s of n. CG&r. glu'%(d*8.34))
cmd.select('asp8', 'n. CG&r. asp w. %s of n. CD&r. glu'%(d*7.40))
cmd.select('asp9', 'n. CG&r. asp w. %s of n. OE1&r. glu'%(d*6.41))
cmd.select('asp10', 'n. CG&r. asp w. %s of n. OE2&r. glu'%(d*7.91))
cmd.select('asp11', 'n. OD1&r. asp w. %s of n. CB&r. glu'%(d*7.49))
cmd.select('asp12', 'n. OD1&r. asp w. %s of n. CG&r. glu'%(d*7.65))
cmd.select('asp13', 'n. OD1&r. asp w. %s of n. CD&r. glu'%(d*6.61))
cmd.select('asp14', 'n. OD1&r. asp w. %s of n. OE1&r. glu'%(d*5.80))
cmd.select('asp15', 'n. OD1&r. asp w. %s of n. OE2&r. glu'%(d*6.95))
cmd.select('asp16', 'n. OD2&r. asp w. %s of n. CB&r. glu'%(d*8.89))
cmd.select('asp17', 'n. OD2&r. asp w. %s of n. CG&r. glu'%(d*9.20))
cmd.select('asp18', 'n. OD2&r. asp w. %s of n. CD&r. glu'%(d*8.14))
cmd.select('asp19', 'n. OD2&r. asp w. %s of n. OE1&r. glu'%(d*7.07))
cmd.select('asp20', 'n. OD2&r. asp w. %s of n. OE2&r. glu'%(d*8.60))
cmd.select('asp21', 'n. CB&r. asp w. %s of n. CB&r. asn'%(d*11.90))
cmd.select('asp22', 'n. CB&r. asp w. %s of n. CG&r. asn'%(d*12.09))
cmd.select('asp23', 'n. CB&r. asp w. %s of n. OD1&r. asn'%(d*12.99))
cmd.select('asp24', 'n. CB&r. asp w. %s of n. ND2&r. asn'%(d*11.44))
cmd.select('asp25', 'n. CG&r. asp w. %s of n. CB&r. asn'%(d*10.84))
cmd.select('asp26', 'n. CG&r. asp w. %s of n. CG&r. asn'%(d*10.86))
cmd.select('asp27', 'n. CG&r. asp w. %s of n. OD1&r. asn'%(d*11.74))
cmd.select('asp28', 'n. CG&r. asp w. %s of n. ND2&r. asn'%(d*10.14))
cmd.select('asp29', 'n. OD1&r. asp w. %s of n. CB&r. asn'%(d*9.64))
cmd.select('asp30', 'n. OD1&r. asp w. %s of n. CG&r. asn'%(d*9.74))
cmd.select('asp31', 'n. OD1&r. asp w. %s of n. OD1&r. asn'%(d*10.64))
cmd.select('asp32', 'n. OD1&r. asp w. %s of n. ND2&r. asn'%(d*9.07))
cmd.select('asp33', 'n. OD2&r. asp w. %s of n. CB&r. asn'%(d*11.33))
cmd.select('asp34', 'n. OD2&r. asp w. %s of n. CG&r. asn'%(d*11.16))
cmd.select('asp35', 'n. OD2&r. asp w. %s of n. OD1&r. asn'%(d*11.97))
cmd.select('asp36', 'n. OD2&r. asp w. %s of n. ND2&r. asn'%(d*10.33))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36')
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
cmd.delete('asp33')
cmd.delete('asp34')
cmd.delete('asp35')
cmd.delete('asp36')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&asp'%(d*7.74))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. CG&asp'%(d*7.96))
cmd.select('glu3', 'n. CB&r. glu w. %s of n. OD1&asp'%(d*7.49))
cmd.select('glu4', 'n. CB&r. glu w. %s of n. OD2&asp'%(d*8.89))
cmd.select('glu5', 'n. CG&r. glu w. %s of n. CB&asp'%(d*8.47))
cmd.select('glu6', 'n. CG&r. glu w. %s of n. CG&asp'%(d*8.34))
cmd.select('glu7', 'n. CG&r. glu w. %s of n. OD1&asp'%(d*7.65))
cmd.select('glu8', 'n. CG&r. glu w. %s of n. OD2&asp'%(d*9.20))
cmd.select('glu9', 'n. CD&r. glu w. %s of n. CB&asp'%(d*7.85))
cmd.select('glu10', 'n. CD&r. glu w. %s of n. CG&asp'%(d*7.40))
cmd.select('glu11', 'n. CD&r. glu w. %s of n. OD1&asp'%(d*6.61))
cmd.select('glu12', 'n. CD&r. glu w. %s of n. OD2&asp'%(d*8.14))
cmd.select('glu13', 'n. OE1&r. glu w. %s of n. CB&asp'%(d*6.90))
cmd.select('glu14', 'n. OE1&r. glu w. %s of n. CG&asp'%(d*6.41))
cmd.select('glu15', 'n. OE1&r. glu w. %s of n. OD1&asp'%(d*5.80))
cmd.select('glu16', 'n. OE1&r. glu w. %s of n. OD2&asp'%(d*7.07))
cmd.select('glu17', 'n. OE2&r. glu w. %s of n. CB&asp'%(d*8.57))
cmd.select('glu18', 'n. OE2&r. glu w. %s of n. CG&asp'%(d*7.91))
cmd.select('glu19', 'n. OE2&r. glu w. %s of n. OD1&asp'%(d*6.95))
cmd.select('glu20', 'n. OE2&r. glu w. %s of n. OD2&asp'%(d*8.60))
cmd.select('glu21', 'n. CB&r. glu w. %s of n. CB&r. asn'%(d*10.87))
cmd.select('glu22', 'n. CB&r. glu w. %s of n. CG&r. asn'%(d*11.62))
cmd.select('glu23', 'n. CB&r. glu w. %s of n. OD1&r. asn'%(d*12.83))
cmd.select('glu24', 'n. CB&r. glu w. %s of n. ND2&r. asn'%(d*11.07))
cmd.select('glu25', 'n. CG&r. glu w. %s of n. CB&r. asn'%(d*9.70))
cmd.select('glu26', 'n. CG&r. glu w. %s of n. CG&r. asn'%(d*10.46))
cmd.select('glu27', 'n. CG&r. glu w. %s of n. OD1&r. asn'%(d*11.69))
cmd.select('glu28', 'n. CG&r. glu w. %s of n. ND2&r. asn'%(d*9.91))
cmd.select('glu29', 'n. CD&r. glu w. %s of n. CB&r. asn'%(d*8.77))
cmd.select('glu30', 'n. CD&r. glu w. %s of n. CG&r. asn'%(d*9.33))
cmd.select('glu31', 'n. CD&r. glu w. %s of n. OD1&r. asn'%(d*10.55))
cmd.select('glu32', 'n. CD&r. glu w. %s of n. ND2&r. asn'%(d*8.65))
cmd.select('glu33', 'n. OE1&r. glu w. %s of n. CB&r. asn'%(d*9.37))
cmd.select('glu34', 'n. OE1&r. glu w. %s of n. CG&r. asn'%(d*9.74))
cmd.select('glu35', 'n. OE1&r. glu w. %s of n. OD1&r. asn'%(d*10.92))
cmd.select('glu36', 'n. OE1&r. glu w. %s of n. ND2&r. asn'%(d*8.94))
cmd.select('glu37', 'n. OE2&r. glu w. %s of n. CB&r. asn'%(d*7.61))
cmd.select('glu38', 'n. OE2&r. glu w. %s of n. CG&r. asn'%(d*8.19))
cmd.select('glu39', 'n. OE2&r. glu w. %s of n. OD1&r. asn'%(d*9.42))
cmd.select('glu40', 'n. OE2&r. glu w. %s of n. ND2&r. asn'%(d*7.55))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36&br. glu37&br. glu38&br. glu39&br. glu40')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
cmd.delete('glu37')
cmd.delete('glu38')
cmd.delete('glu39')
cmd.delete('glu40')
cmd.select('asn1', 'n. CB&r. asn w. %s of n. CB&asp'%(d*11.90))
cmd.select('asn2', 'n. CB&r. asn w. %s of n. CG&asp'%(d*10.84))
cmd.select('asn3', 'n. CB&r. asn w. %s of n. OD1&asp'%(d*9.64))
cmd.select('asn4', 'n. CB&r. asn w. %s of n. OD2&asp'%(d*11.33))
cmd.select('asn5', 'n. CG&r. asn w. %s of n. CB&asp'%(d*12.09))
cmd.select('asn6', 'n. CG&r. asn w. %s of n. CG&asp'%(d*10.86))
cmd.select('asn7', 'n. CG&r. asn w. %s of n. OD1&asp'%(d*9.74))
cmd.select('asn8', 'n. CG&r. asn w. %s of n. OD2&asp'%(d*11.16))
cmd.select('asn9', 'n. OD1&r. asn w. %s of n. CB&asp'%(d*12.99))
cmd.select('asn10', 'n. OD1&r. asn w. %s of n. CG&asp'%(d*11.74))
cmd.select('asn11', 'n. OD1&r. asn w. %s of n. OD1&asp'%(d*10.64))
cmd.select('asn12', 'n. OD1&r. asn w. %s of n. OD2&asp'%(d*11.97))
cmd.select('asn13', 'n. ND2&r. asn w. %s of n. CB&asp'%(d*11.44))
cmd.select('asn14', 'n. ND2&r. asn w. %s of n. CG&asp'%(d*10.14))
cmd.select('asn15', 'n. ND2&r. asn w. %s of n. OD1&asp'%(d*9.07))
cmd.select('asn16', 'n. ND2&r. asn w. %s of n. OD2&asp'%(d*10.33))
cmd.select('asn17', 'n. CB&r. asn w. %s of n. CB&glu'%(d*10.87))
cmd.select('asn18', 'n. CB&r. asn w. %s of n. CG&glu'%(d*9.70))
cmd.select('asn19', 'n. CB&r. asn w. %s of n. CD&glu'%(d*8.77))
cmd.select('asn20', 'n. CB&r. asn w. %s of n. OE1&glu'%(d*9.37))
cmd.select('asn21', 'n. CB&r. asn w. %s of n. OE2&glu'%(d*7.61))
cmd.select('asn22', 'n. CG&r. asn w. %s of n. CB&glu'%(d*11.62))
cmd.select('asn23', 'n. CG&r. asn w. %s of n. CG&glu'%(d*10.46))
cmd.select('asn24', 'n. CG&r. asn w. %s of n. CD&glu'%(d*9.33))
cmd.select('asn25', 'n. CG&r. asn w. %s of n. OE1&glu'%(d*9.74))
cmd.select('asn26', 'n. CG&r. asn w. %s of n. OE2&glu'%(d*8.19))
cmd.select('asn27', 'n. OD1&r. asn w. %s of n. CB&glu'%(d*12.83))
cmd.select('asn28', 'n. OD1&r. asn w. %s of n. CG&glu'%(d*11.69))
cmd.select('asn29', 'n. OD1&r. asn w. %s of n. CD&glu'%(d*10.55))
cmd.select('asn30', 'n. OD1&r. asn w. %s of n. OE1&glu'%(d*10.92))
cmd.select('asn31', 'n. OD1&r. asn w. %s of n. OE2&glu'%(d*9.42))
cmd.select('asn32', 'n. ND2&r. asn w. %s of n. CB&glu'%(d*11.07))
cmd.select('asn33', 'n. ND2&r. asn w. %s of n. CG&glu'%(d*9.91))
cmd.select('asn34', 'n. ND2&r. asn w. %s of n. CD&glu'%(d*8.65))
cmd.select('asn35', 'n. ND2&r. asn w. %s of n. OE1&glu'%(d*8.94))
cmd.select('asn36', 'n. ND2&r. asn w. %s of n. OE2&glu'%(d*7.55))
cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36')
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
cmd.delete('asn33')
cmd.delete('asn34')
cmd.delete('asn35')
cmd.delete('asn36')
cmd.select('A_2cpu-D197A-E233A-N300A', 'asp|glu|asn')
cmd.delete('asp')
cmd.delete('glu')
cmd.delete('asn')
