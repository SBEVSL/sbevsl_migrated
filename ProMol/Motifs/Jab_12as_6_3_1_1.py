'''
FUNC:Jab_12as_6_3_1_1
PDB:12as
EC:6.3.1.1
RESI:asp,arg,gln
LOCI:a-46,100,116;
'''
cmd.select('temp0', 'n. ca')
cmd.select('temp1', 'r. asp')
cmd.select('temp2', 'r. glu')
cmd.select('jessatom0', '((temp0&temp1)|(temp0&temp2))')
cmd.select('temp3', 'n. cb')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.555400))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', '((temp3&temp1)|(temp3&temp2))&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.555400))
cmd.select('temp6', 'r. arg')
cmd.select('temp7', 'all w. %s of jessatom0'%(d*11.301900))
cmd.select('temp8', 'all w. %s of jessatom1'%(d*10.776700))
cmd.select('jessatom2', 'temp0&temp6&temp7&temp8')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*11.301900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*10.776700))
cmd.select('temp9', 'all w. %s of jessatom0'%(d*10.978700))
cmd.select('temp10', 'all w. %s of jessatom1'%(d*10.302000))
cmd.select('temp11', 'all w. %s of jessatom2'%(d*1.555400))
cmd.select('temp12', 'br. jessatom2')
cmd.select('jessatom3', 'temp3&temp6&temp9&temp10&temp11&temp12')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*10.978700))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*10.302000))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*1.555400))
cmd.select('temp13', 'r. gln')
cmd.select('temp14', 'r. asn')
cmd.select('temp15', 'all w. %s of jessatom0'%(d*13.655200))
cmd.select('temp16', 'all w. %s of jessatom1'%(d*12.150300))
cmd.select('temp17', 'all w. %s of jessatom2'%(d*12.705800))
cmd.select('temp18', 'all w. %s of jessatom3'%(d*11.806900))
cmd.select('jessatom4', '((temp0&temp13)|(temp0&temp14))&temp15&temp16&temp17&temp18')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*13.655200))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*12.150300))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*12.705800))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*11.806900))
cmd.select('temp19', 'all w. %s of jessatom0'%(d*12.251300))
cmd.select('temp20', 'all w. %s of jessatom1'%(d*10.726200))
cmd.select('temp21', 'all w. %s of jessatom2'%(d*12.140200))
cmd.select('temp22', 'all w. %s of jessatom3'%(d*11.190800))
cmd.select('temp23', 'all w. %s of jessatom4'%(d*1.545300))
cmd.select('temp24', 'br. jessatom4')
cmd.select('jessatom5', '((temp3&temp13)|(temp3&temp14))&temp19&temp20&temp21&temp22&temp23&temp24')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*12.251300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*10.726200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*12.140200))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*11.190800))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.545300))
cmd.select('Jab_12as_6_3_1_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('temp0')
cmd.delete('temp1')
cmd.delete('temp2')
cmd.delete('temp3')
cmd.delete('temp4')
cmd.delete('temp5')
cmd.delete('temp6')
cmd.delete('temp7')
cmd.delete('temp8')
cmd.delete('temp9')
cmd.delete('temp10')
cmd.delete('temp11')
cmd.delete('temp12')
cmd.delete('temp13')
cmd.delete('temp14')
cmd.delete('temp15')
cmd.delete('temp16')
cmd.delete('temp17')
cmd.delete('temp18')
cmd.delete('temp19')
cmd.delete('temp20')
cmd.delete('temp21')
cmd.delete('temp22')
cmd.delete('temp23')
cmd.delete('temp24')
