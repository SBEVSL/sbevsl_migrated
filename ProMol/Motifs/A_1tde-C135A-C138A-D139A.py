'''
FUNC:A_1tde-C135A-C138A-D139A
PDB:1tde
EC:1.8.1.9
PFAM:PF07992,PF00070,PF13738
RESI:cys,cys,asp
LOCI:a-135,138,139;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. cys'%(d*5.61))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. SG&r. cys'%(d*5.06))
cmd.select('cys3', 'n. SG&r. cys w. %s of n. CB&r. cys'%(d*4.99))
cmd.select('cys4', 'n. SG&r. cys w. %s of n. SG&r. cys'%(d*4.01))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. CB&r. asp'%(d*6.58))
cmd.select('cys6', 'n. CB&r. cys w. %s of n. CG&r. asp'%(d*6.07))
cmd.select('cys7', 'n. CB&r. cys w. %s of n. OD1&r. asp'%(d*5.92))
cmd.select('cys8', 'n. CB&r. cys w. %s of n. OD2&r. asp'%(d*6.36))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. CB&r. asp'%(d*8.21))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. CG&r. asp'%(d*7.62))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. OD1&r. asp'%(d*7.53))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. OD2&r. asp'%(d*7.64))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.select('cysi1', 'n. CB&r. cys w. %s of n. CB&cys'%(d*5.61))
cmd.select('cysi2', 'n. CB&r. cys w. %s of n. SG&cys'%(d*4.99))
cmd.select('cysi3', 'n. SG&r. cys w. %s of n. CB&cys'%(d*5.06))
cmd.select('cysi4', 'n. SG&r. cys w. %s of n. SG&cys'%(d*4.01))
cmd.select('cysi5', 'n. CB&r. cys w. %s of n. CB&r. asp'%(d*8.08))
cmd.select('cysi6', 'n. CB&r. cys w. %s of n. CG&r. asp'%(d*7.67))
cmd.select('cysi7', 'n. CB&r. cys w. %s of n. OD1&r. asp'%(d*8.18))
cmd.select('cysi8', 'n. CB&r. cys w. %s of n. OD2&r. asp'%(d*7.20))
cmd.select('cysi9', 'n. SG&r. cys w. %s of n. CB&r. asp'%(d*8.57))
cmd.select('cysi10', 'n. SG&r. cys w. %s of n. CG&r. asp'%(d*8.27))
cmd.select('cysi11', 'n. SG&r. cys w. %s of n. OD1&r. asp'%(d*8.56))
cmd.select('cysi12', 'n. SG&r. cys w. %s of n. OD2&r. asp'%(d*8.13))
cmd.select('cysi',' br. cysi1&br. cysi2&br. cysi3&br. cysi4&br. cysi5&br. cysi6&br. cysi7&br. cysi8&br. cysi9&br. cysi10&br. cysi11&br. cysi12')
cmd.delete('cysi1')
cmd.delete('cysi2')
cmd.delete('cysi3')
cmd.delete('cysi4')
cmd.delete('cysi5')
cmd.delete('cysi6')
cmd.delete('cysi7')
cmd.delete('cysi8')
cmd.delete('cysi9')
cmd.delete('cysi10')
cmd.delete('cysi11')
cmd.delete('cysi12')
cmd.select('asp1', 'n. CB&r. asp w. %s of n. CB&cys'%(d*6.58))
cmd.select('asp2', 'n. CB&r. asp w. %s of n. SG&cys'%(d*8.21))
cmd.select('asp3', 'n. CG&r. asp w. %s of n. CB&cys'%(d*6.07))
cmd.select('asp4', 'n. CG&r. asp w. %s of n. SG&cys'%(d*7.62))
cmd.select('asp5', 'n. OD1&r. asp w. %s of n. CB&cys'%(d*5.92))
cmd.select('asp6', 'n. OD1&r. asp w. %s of n. SG&cys'%(d*7.53))
cmd.select('asp7', 'n. OD2&r. asp w. %s of n. CB&cys'%(d*6.36))
cmd.select('asp8', 'n. OD2&r. asp w. %s of n. SG&cys'%(d*7.64))
cmd.select('asp9', 'n. CB&r. asp w. %s of n. CB&cysi'%(d*8.08))
cmd.select('asp10', 'n. CB&r. asp w. %s of n. SG&cysi'%(d*8.57))
cmd.select('asp11', 'n. CG&r. asp w. %s of n. CB&cysi'%(d*7.67))
cmd.select('asp12', 'n. CG&r. asp w. %s of n. SG&cysi'%(d*8.27))
cmd.select('asp13', 'n. OD1&r. asp w. %s of n. CB&cysi'%(d*8.18))
cmd.select('asp14', 'n. OD1&r. asp w. %s of n. SG&cysi'%(d*8.56))
cmd.select('asp15', 'n. OD2&r. asp w. %s of n. CB&cysi'%(d*7.20))
cmd.select('asp16', 'n. OD2&r. asp w. %s of n. SG&cysi'%(d*8.13))
cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16')
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
cmd.select('A_1tde-C135A-C138A-D139A', 'cys|cysi|asp')
cmd.delete('cys')
cmd.delete('cysi')
cmd.delete('asp')
