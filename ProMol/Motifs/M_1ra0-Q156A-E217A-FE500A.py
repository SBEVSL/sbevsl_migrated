'''
FUNC:M_1ra0-Q156A-E217A-FE500A
PDB:1ra0
EC:3.5.4.1
PFAM:PF13594,PF07969,PF13147
RESI:gln,glu,fe
LOCI:a-156,217,500;
'''
cmd.select('gln1', 'n. CB&r. gln w. %s of n. CB&r. glu'%(d*13.59))
cmd.select('gln2', 'n. CB&r. gln w. %s of n. CG&r. glu'%(d*13.91))
cmd.select('gln3', 'n. CB&r. gln w. %s of n. CD&r. glu'%(d*12.83))
cmd.select('gln4', 'n. CB&r. gln w. %s of n. OE1&r. glu'%(d*13.26))
cmd.select('gln5', 'n. CB&r. gln w. %s of n. OE2&r. glu'%(d*11.65))
cmd.select('gln6', 'n. CG&r. gln w. %s of n. CB&r. glu'%(d*13.05))
cmd.select('gln7', 'n. CG&r. gln w. %s of n. CG&r. glu'%(d*13.25))
cmd.select('gln8', 'n. CG&r. gln w. %s of n. CD&r. glu'%(d*12.13))
cmd.select('gln9', 'n. CG&r. gln w. %s of n. OE1&r. glu'%(d*12.49))
cmd.select('gln10', 'n. CG&r. gln w. %s of n. OE2&r. glu'%(d*11.02))
cmd.select('gln11', 'n. CD&r. gln w. %s of n. CB&r. glu'%(d*11.70))
cmd.select('gln12', 'n. CD&r. gln w. %s of n. CG&r. glu'%(d*11.81))
cmd.select('gln13', 'n. CD&r. gln w. %s of n. CD&r. glu'%(d*10.65))
cmd.select('gln14', 'n. CD&r. gln w. %s of n. OE1&r. glu'%(d*10.98))
cmd.select('gln15', 'n. CD&r. gln w. %s of n. OE2&r. glu'%(d*9.56))
cmd.select('gln16', 'n. OE1&r. gln w. %s of n. CB&r. glu'%(d*11.73))
cmd.select('gln17', 'n. OE1&r. gln w. %s of n. CG&r. glu'%(d*11.68))
cmd.select('gln18', 'n. OE1&r. gln w. %s of n. CD&r. glu'%(d*10.40))
cmd.select('gln19', 'n. OE1&r. gln w. %s of n. OE1&r. glu'%(d*10.58))
cmd.select('gln20', 'n. OE1&r. gln w. %s of n. OE2&r. glu'%(d*9.36))
cmd.select('gln21', 'n. NE2&r. gln w. %s of n. CB&r. glu'%(d*10.64))
cmd.select('gln22', 'n. NE2&r. gln w. %s of n. CG&r. glu'%(d*10.88))
cmd.select('gln23', 'n. NE2&r. gln w. %s of n. CD&r. glu'%(d*9.83))
cmd.select('gln24', 'n. NE2&r. gln w. %s of n. OE1&r. glu'%(d*10.30))
cmd.select('gln25', 'n. NE2&r. gln w. %s of n. OE2&r. glu'%(d*8.71))
cmd.select('gln26', 'n. CB&r. gln w. %s of n. FE&r. fe'%(d*10.96))
cmd.select('gln27', 'n. CG&r. gln w. %s of n. FE&r. fe'%(d*10.79))
cmd.select('gln28', 'n. CD&r. gln w. %s of n. FE&r. fe'%(d*9.47))
cmd.select('gln29', 'n. OE1&r. gln w. %s of n. FE&r. fe'%(d*8.66))
cmd.select('gln30', 'n. NE2&r. gln w. %s of n. FE&r. fe'%(d*9.45))
cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27&br. gln28&br. gln29&br. gln30')
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
cmd.delete('gln19')
cmd.delete('gln20')
cmd.delete('gln21')
cmd.delete('gln22')
cmd.delete('gln23')
cmd.delete('gln24')
cmd.delete('gln25')
cmd.delete('gln26')
cmd.delete('gln27')
cmd.delete('gln28')
cmd.delete('gln29')
cmd.delete('gln30')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&gln'%(d*13.59))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. CG&gln'%(d*13.05))
cmd.select('glu3', 'n. CB&r. glu w. %s of n. CD&gln'%(d*11.70))
cmd.select('glu4', 'n. CB&r. glu w. %s of n. OE1&gln'%(d*11.73))
cmd.select('glu5', 'n. CB&r. glu w. %s of n. NE2&gln'%(d*10.64))
cmd.select('glu6', 'n. CG&r. glu w. %s of n. CB&gln'%(d*13.91))
cmd.select('glu7', 'n. CG&r. glu w. %s of n. CG&gln'%(d*13.25))
cmd.select('glu8', 'n. CG&r. glu w. %s of n. CD&gln'%(d*11.81))
cmd.select('glu9', 'n. CG&r. glu w. %s of n. OE1&gln'%(d*11.68))
cmd.select('glu10', 'n. CG&r. glu w. %s of n. NE2&gln'%(d*10.88))
cmd.select('glu11', 'n. CD&r. glu w. %s of n. CB&gln'%(d*12.83))
cmd.select('glu12', 'n. CD&r. glu w. %s of n. CG&gln'%(d*12.13))
cmd.select('glu13', 'n. CD&r. glu w. %s of n. CD&gln'%(d*10.65))
cmd.select('glu14', 'n. CD&r. glu w. %s of n. OE1&gln'%(d*10.40))
cmd.select('glu15', 'n. CD&r. glu w. %s of n. NE2&gln'%(d*9.83))
cmd.select('glu16', 'n. OE1&r. glu w. %s of n. CB&gln'%(d*13.26))
cmd.select('glu17', 'n. OE1&r. glu w. %s of n. CG&gln'%(d*12.49))
cmd.select('glu18', 'n. OE1&r. glu w. %s of n. CD&gln'%(d*10.98))
cmd.select('glu19', 'n. OE1&r. glu w. %s of n. OE1&gln'%(d*10.58))
cmd.select('glu20', 'n. OE1&r. glu w. %s of n. NE2&gln'%(d*10.30))
cmd.select('glu21', 'n. OE2&r. glu w. %s of n. CB&gln'%(d*11.65))
cmd.select('glu22', 'n. OE2&r. glu w. %s of n. CG&gln'%(d*11.02))
cmd.select('glu23', 'n. OE2&r. glu w. %s of n. CD&gln'%(d*9.56))
cmd.select('glu24', 'n. OE2&r. glu w. %s of n. OE1&gln'%(d*9.36))
cmd.select('glu25', 'n. OE2&r. glu w. %s of n. NE2&gln'%(d*8.71))
cmd.select('glu26', 'n. CB&r. glu w. %s of n. FE&r. fe'%(d*9.65))
cmd.select('glu27', 'n. CG&r. glu w. %s of n. FE&r. fe'%(d*9.23))
cmd.select('glu28', 'n. CD&r. glu w. %s of n. FE&r. fe'%(d*7.96))
cmd.select('glu29', 'n. OE1&r. glu w. %s of n. FE&r. fe'%(d*7.84))
cmd.select('glu30', 'n. OE2&r. glu w. %s of n. FE&r. fe'%(d*7.36))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30')
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
cmd.select('fe1', 'n. FE&r. fe w. %s of n. CB&gln'%(d*10.96))
cmd.select('fe2', 'n. FE&r. fe w. %s of n. CG&gln'%(d*10.79))
cmd.select('fe3', 'n. FE&r. fe w. %s of n. CD&gln'%(d*9.47))
cmd.select('fe4', 'n. FE&r. fe w. %s of n. OE1&gln'%(d*8.66))
cmd.select('fe5', 'n. FE&r. fe w. %s of n. NE2&gln'%(d*9.45))
cmd.select('fe6', 'n. FE&r. fe w. %s of n. CB&glu'%(d*9.65))
cmd.select('fe7', 'n. FE&r. fe w. %s of n. CG&glu'%(d*9.23))
cmd.select('fe8', 'n. FE&r. fe w. %s of n. CD&glu'%(d*7.96))
cmd.select('fe9', 'n. FE&r. fe w. %s of n. OE1&glu'%(d*7.84))
cmd.select('fe10', 'n. FE&r. fe w. %s of n. OE2&glu'%(d*7.36))
cmd.select('fe',' br. fe1&br. fe2&br. fe3&br. fe4&br. fe5&br. fe6&br. fe7&br. fe8&br. fe9&br. fe10')
cmd.delete('fe1')
cmd.delete('fe2')
cmd.delete('fe3')
cmd.delete('fe4')
cmd.delete('fe5')
cmd.delete('fe6')
cmd.delete('fe7')
cmd.delete('fe8')
cmd.delete('fe9')
cmd.delete('fe10')
cmd.select('M_1ra0-Q156A-E217A-FE500A', 'gln|glu|fe')
cmd.delete('gln')
cmd.delete('glu')
cmd.delete('fe')
