'''
FUNC:R_1g8k_1_20_98_1
PDB:1g8k
EC:1.20.98.1
RESI:4mo,f3s,fes
LOCI:a-5004,5005;b-5006;
'''
cmd.select('4mo1', 'n. MO&r. 4mo w. %s of n. FE1&r. f3s'%(d*15.95))
cmd.select('4mo2', 'n. MO&r. 4mo w. %s of n. FE3&r. f3s'%(d*17.01))
cmd.select('4mo3', 'n. MO&r. 4mo w. %s of n. FE4&r. f3s'%(d*14.34))
cmd.select('4mo4', 'n. MO&r. 4mo w. %s of n. S1&r. f3s'%(d*18.01))
cmd.select('4mo5', 'n. MO&r. 4mo w. %s of n. S2&r. f3s'%(d*14.40))
cmd.select('4mo6', 'n. MO&r. 4mo w. %s of n. S3&r. f3s'%(d*15.40))
cmd.select('4mo7', 'n. MO&r. 4mo w. %s of n. S4&r. f3s'%(d*16.02))
cmd.select('4mo8', 'n. MO&r. 4mo w. %s of n. FE1&r. fes'%(d*28.99))
cmd.select('4mo9', 'n. MO&r. 4mo w. %s of n. FE2&r. fes'%(d*27.17))
cmd.select('4mo10', 'n. MO&r. 4mo w. %s of n. S1&r. fes'%(d*26.89))
cmd.select('4mo11', 'n. MO&r. 4mo w. %s of n. S2&r. fes'%(d*29.40))
cmd.select('4mo',' br. 4mo1&br. 4mo2&br. 4mo3&br. 4mo4&br. 4mo5&br. 4mo6&br. 4mo7&br. 4mo8&br. 4mo9&br. 4mo10&br. 4mo11')
cmd.delete('4mo1')
cmd.delete('4mo2')
cmd.delete('4mo3')
cmd.delete('4mo4')
cmd.delete('4mo5')
cmd.delete('4mo6')
cmd.delete('4mo7')
cmd.delete('4mo8')
cmd.delete('4mo9')
cmd.delete('4mo10')
cmd.delete('4mo11')
cmd.select('f3s1', 'n. FE1&r. f3s w. %s of n. MO&4mo'%(d*15.95))
cmd.select('f3s2', 'n. FE3&r. f3s w. %s of n. MO&4mo'%(d*17.01))
cmd.select('f3s3', 'n. FE4&r. f3s w. %s of n. MO&4mo'%(d*14.34))
cmd.select('f3s4', 'n. S1&r. f3s w. %s of n. MO&4mo'%(d*18.01))
cmd.select('f3s5', 'n. S2&r. f3s w. %s of n. MO&4mo'%(d*14.40))
cmd.select('f3s6', 'n. S3&r. f3s w. %s of n. MO&4mo'%(d*15.40))
cmd.select('f3s7', 'n. S4&r. f3s w. %s of n. MO&4mo'%(d*16.02))
cmd.select('f3s8', 'n. FE1&r. f3s w. %s of n. FE1&r. fes'%(d*18.59))
cmd.select('f3s9', 'n. FE1&r. f3s w. %s of n. FE2&r. fes'%(d*16.29))
cmd.select('f3s10', 'n. FE1&r. f3s w. %s of n. S1&r. fes'%(d*17.00))
cmd.select('f3s11', 'n. FE1&r. f3s w. %s of n. S2&r. fes'%(d*18.19))
cmd.select('f3s12', 'n. FE3&r. f3s w. %s of n. FE1&r. fes'%(d*17.45))
cmd.select('f3s13', 'n. FE3&r. f3s w. %s of n. FE2&r. fes'%(d*14.95))
cmd.select('f3s14', 'n. FE3&r. f3s w. %s of n. S1&r. fes'%(d*15.83))
cmd.select('f3s15', 'n. FE3&r. f3s w. %s of n. S2&r. fes'%(d*16.88))
cmd.select('f3s16', 'n. FE4&r. f3s w. %s of n. FE1&r. fes'%(d*18.75))
cmd.select('f3s17', 'n. FE4&r. f3s w. %s of n. FE2&r. fes'%(d*16.43))
cmd.select('f3s18', 'n. FE4&r. f3s w. %s of n. S1&r. fes'%(d*16.94))
cmd.select('f3s19', 'n. FE4&r. f3s w. %s of n. S2&r. fes'%(d*18.50))
cmd.select('f3s20', 'n. S1&r. f3s w. %s of n. FE1&r. fes'%(d*16.68))
cmd.select('f3s21', 'n. S1&r. f3s w. %s of n. FE2&r. fes'%(d*14.30))
cmd.select('f3s22', 'n. S1&r. f3s w. %s of n. S1&r. fes'%(d*15.22))
cmd.select('f3s23', 'n. S1&r. f3s w. %s of n. S2&r. fes'%(d*16.12))
cmd.select('f3s24', 'n. S2&r. f3s w. %s of n. FE1&r. fes'%(d*18.54))
cmd.select('f3s25', 'n. S2&r. f3s w. %s of n. FE2&r. fes'%(d*16.40))
cmd.select('f3s26', 'n. S2&r. f3s w. %s of n. S1&r. fes'%(d*16.78))
cmd.select('f3s27', 'n. S2&r. f3s w. %s of n. S2&r. fes'%(d*18.43))
cmd.select('f3s28', 'n. S3&r. f3s w. %s of n. FE1&r. fes'%(d*19.68))
cmd.select('f3s29', 'n. S3&r. f3s w. %s of n. FE2&r. fes'%(d*17.23))
cmd.select('f3s30', 'n. S3&r. f3s w. %s of n. S1&r. fes'%(d*18.03))
cmd.select('f3s31', 'n. S3&r. f3s w. %s of n. S2&r. fes'%(d*19.17))
cmd.select('f3s32', 'n. S4&r. f3s w. %s of n. FE1&r. fes'%(d*16.90))
cmd.select('f3s33', 'n. S4&r. f3s w. %s of n. FE2&r. fes'%(d*14.49))
cmd.select('f3s34', 'n. S4&r. f3s w. %s of n. S1&r. fes'%(d*15.07))
cmd.select('f3s35', 'n. S4&r. f3s w. %s of n. S2&r. fes'%(d*16.58))
cmd.select('f3s',' br. f3s1&br. f3s2&br. f3s3&br. f3s4&br. f3s5&br. f3s6&br. f3s7&br. f3s8&br. f3s9&br. f3s10&br. f3s11&br. f3s12&br. f3s13&br. f3s14&br. f3s15&br. f3s16&br. f3s17&br. f3s18&br. f3s19&br. f3s20&br. f3s21&br. f3s22&br. f3s23&br. f3s24&br. f3s25&br. f3s26&br. f3s27&br. f3s28&br. f3s29&br. f3s30&br. f3s31&br. f3s32&br. f3s33&br. f3s34&br. f3s35')
cmd.delete('f3s1')
cmd.delete('f3s2')
cmd.delete('f3s3')
cmd.delete('f3s4')
cmd.delete('f3s5')
cmd.delete('f3s6')
cmd.delete('f3s7')
cmd.delete('f3s8')
cmd.delete('f3s9')
cmd.delete('f3s10')
cmd.delete('f3s11')
cmd.delete('f3s12')
cmd.delete('f3s13')
cmd.delete('f3s14')
cmd.delete('f3s15')
cmd.delete('f3s16')
cmd.delete('f3s17')
cmd.delete('f3s18')
cmd.delete('f3s19')
cmd.delete('f3s20')
cmd.delete('f3s21')
cmd.delete('f3s22')
cmd.delete('f3s23')
cmd.delete('f3s24')
cmd.delete('f3s25')
cmd.delete('f3s26')
cmd.delete('f3s27')
cmd.delete('f3s28')
cmd.delete('f3s29')
cmd.delete('f3s30')
cmd.delete('f3s31')
cmd.delete('f3s32')
cmd.delete('f3s33')
cmd.delete('f3s34')
cmd.delete('f3s35')
cmd.select('fes1', 'n. FE1&r. fes w. %s of n. MO&4mo'%(d*28.99))
cmd.select('fes2', 'n. FE2&r. fes w. %s of n. MO&4mo'%(d*27.17))
cmd.select('fes3', 'n. S1&r. fes w. %s of n. MO&4mo'%(d*26.89))
cmd.select('fes4', 'n. S2&r. fes w. %s of n. MO&4mo'%(d*29.40))
cmd.select('fes5', 'n. FE1&r. fes w. %s of n. FE1&f3s'%(d*18.59))
cmd.select('fes6', 'n. FE1&r. fes w. %s of n. FE3&f3s'%(d*17.45))
cmd.select('fes7', 'n. FE1&r. fes w. %s of n. FE4&f3s'%(d*18.75))
cmd.select('fes8', 'n. FE1&r. fes w. %s of n. S1&f3s'%(d*16.68))
cmd.select('fes9', 'n. FE1&r. fes w. %s of n. S2&f3s'%(d*18.54))
cmd.select('fes10', 'n. FE1&r. fes w. %s of n. S3&f3s'%(d*19.68))
cmd.select('fes11', 'n. FE1&r. fes w. %s of n. S4&f3s'%(d*16.90))
cmd.select('fes12', 'n. FE2&r. fes w. %s of n. FE1&f3s'%(d*16.29))
cmd.select('fes13', 'n. FE2&r. fes w. %s of n. FE3&f3s'%(d*14.95))
cmd.select('fes14', 'n. FE2&r. fes w. %s of n. FE4&f3s'%(d*16.43))
cmd.select('fes15', 'n. FE2&r. fes w. %s of n. S1&f3s'%(d*14.30))
cmd.select('fes16', 'n. FE2&r. fes w. %s of n. S2&f3s'%(d*16.40))
cmd.select('fes17', 'n. FE2&r. fes w. %s of n. S3&f3s'%(d*17.23))
cmd.select('fes18', 'n. FE2&r. fes w. %s of n. S4&f3s'%(d*14.49))
cmd.select('fes19', 'n. S1&r. fes w. %s of n. FE1&f3s'%(d*17.00))
cmd.select('fes20', 'n. S1&r. fes w. %s of n. FE3&f3s'%(d*15.83))
cmd.select('fes21', 'n. S1&r. fes w. %s of n. FE4&f3s'%(d*16.94))
cmd.select('fes22', 'n. S1&r. fes w. %s of n. S1&f3s'%(d*15.22))
cmd.select('fes23', 'n. S1&r. fes w. %s of n. S2&f3s'%(d*16.78))
cmd.select('fes24', 'n. S1&r. fes w. %s of n. S3&f3s'%(d*18.03))
cmd.select('fes25', 'n. S1&r. fes w. %s of n. S4&f3s'%(d*15.07))
cmd.select('fes26', 'n. S2&r. fes w. %s of n. FE1&f3s'%(d*18.19))
cmd.select('fes27', 'n. S2&r. fes w. %s of n. FE3&f3s'%(d*16.88))
cmd.select('fes28', 'n. S2&r. fes w. %s of n. FE4&f3s'%(d*18.50))
cmd.select('fes29', 'n. S2&r. fes w. %s of n. S1&f3s'%(d*16.12))
cmd.select('fes30', 'n. S2&r. fes w. %s of n. S2&f3s'%(d*18.43))
cmd.select('fes31', 'n. S2&r. fes w. %s of n. S3&f3s'%(d*19.17))
cmd.select('fes32', 'n. S2&r. fes w. %s of n. S4&f3s'%(d*16.58))
cmd.select('fes',' br. fes1&br. fes2&br. fes3&br. fes4&br. fes5&br. fes6&br. fes7&br. fes8&br. fes9&br. fes10&br. fes11&br. fes12&br. fes13&br. fes14&br. fes15&br. fes16&br. fes17&br. fes18&br. fes19&br. fes20&br. fes21&br. fes22&br. fes23&br. fes24&br. fes25&br. fes26&br. fes27&br. fes28&br. fes29&br. fes30&br. fes31&br. fes32')
cmd.delete('fes1')
cmd.delete('fes2')
cmd.delete('fes3')
cmd.delete('fes4')
cmd.delete('fes5')
cmd.delete('fes6')
cmd.delete('fes7')
cmd.delete('fes8')
cmd.delete('fes9')
cmd.delete('fes10')
cmd.delete('fes11')
cmd.delete('fes12')
cmd.delete('fes13')
cmd.delete('fes14')
cmd.delete('fes15')
cmd.delete('fes16')
cmd.delete('fes17')
cmd.delete('fes18')
cmd.delete('fes19')
cmd.delete('fes20')
cmd.delete('fes21')
cmd.delete('fes22')
cmd.delete('fes23')
cmd.delete('fes24')
cmd.delete('fes25')
cmd.delete('fes26')
cmd.delete('fes27')
cmd.delete('fes28')
cmd.delete('fes29')
cmd.delete('fes30')
cmd.delete('fes31')
cmd.delete('fes32')
cmd.select('R_1g8k_1_20_98_1', '4mo|f3s|fes')
cmd.delete('4mo')
cmd.delete('f3s')
cmd.delete('fes')
