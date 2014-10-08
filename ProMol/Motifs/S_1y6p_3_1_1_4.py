'''
FUNC:S_1y6p_3_1_1_4
PDB:1y6p
EC:3.1.1.4
RESI:gly,his,asp
LOCI:a-30,48,99;
'''
IDSpec[(('his','CE1'),('rgly','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.45,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','CE1'),('rgly','N'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.02,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','CE1'),('rgly','O'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.05,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','ND1'),('rgly','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.00,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','ND1'),('rgly','N'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.39,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','ND1'),('rgly','O'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.51,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','NE2'),('rgly','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.67,resSelectionSubs('gly','CA',subs)))
IDSpec[(('his','NE2'),('rgly','N'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.18,resSelectionSubs('gly','N',subs)))
IDSpec[(('his','NE2'),('rgly','O'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.34,resSelectionSubs('gly','O',subs)))
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.85,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.80,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.02,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.97,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.85,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.98,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.90,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.92,resSelectionSubs('asp','OD2',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
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
IDSpec[(('gly','CA'),('shis','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.45,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis','ND1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.00,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','CA'),('shis','NE2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.67,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','N'),('shis','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.02,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','N'),('shis','ND1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.39,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','N'),('shis','NE2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.18,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','O'),('shis','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.05,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gly','O'),('shis','ND1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.51,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gly','O'),('shis','NE2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.34,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gly','CA'),('rasp','CG'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.33,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','CA'),('rasp','OD1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.68,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','CA'),('rasp','OD2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','N'),('rasp','CG'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','N'),('rasp','OD1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.41,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','N'),('rasp','OD2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.50,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','O'),('rasp','CG'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.36,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','O'),('rasp','OD1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.53,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','O'),('rasp','OD2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.70,resSelectionSubs('asp','OD2',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.85,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.02,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.98,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.80,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.97,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.90,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.60,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.85,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.92,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.33,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','N'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.10,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','O'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.36,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.68,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','N'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.41,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','O'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.53,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.60,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','N'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.50,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','O'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.70,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
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
IDSpec['S_1y6p_3_1_1_4'] = cmd.select('S_1y6p_3_1_1_4', 'his|gly|asp')
cmd.delete('his')
cmd.delete('gly')
cmd.delete('asp')
