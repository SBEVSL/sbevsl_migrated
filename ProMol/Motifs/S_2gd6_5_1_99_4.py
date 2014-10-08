'''
FUNC:S_2gd6_5_1_99_4
PDB:2gd6
EC:5.1.99.4
RESI:asp,gly,gly
LOCI:a-156,219,220;
'''
IDSpec[(('gly','CA'),('rgly_i','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.81,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','CA'),('rgly_i','N'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.16,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','CA'),('rgly_i','O'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+4.78,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','N'),('rgly_i','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.44,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','N'),('rgly_i','N'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.71,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','N'),('rgly_i','O'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.25,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','O'),('rgly_i','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.62,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','O'),('rgly_i','N'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.15,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','O'),('rgly_i','O'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.01,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','CA'),('rasp','CG'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+28.82,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','CA'),('rasp','OD1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+29.18,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','CA'),('rasp','OD2'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+28.98,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','N'),('rasp','CG'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+27.51,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','N'),('rasp','OD1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+27.90,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','N'),('rasp','OD2'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+27.66,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly','O'),('rasp','CG'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+31.12,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly','O'),('rasp','OD1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+31.50,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly','O'),('rasp','OD2'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+31.28,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.81,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+4.44,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.62,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.16,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+4.71,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.15,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.78,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+4.25,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.01,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('rasp','CG'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+25.90,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly_i','CA'),('rasp','OD1'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+26.38,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly_i','CA'),('rasp','OD2'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+25.99,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly_i','N'),('rasp','CG'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+25.11,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly_i','N'),('rasp','OD1'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+25.55,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly_i','N'),('rasp','OD2'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+25.27,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('gly_i','O'),('rasp','CG'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+28.01,resSelectionSubs('asp','CG',subs)))
IDSpec[(('gly_i','O'),('rasp','OD1'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+28.47,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('gly_i','O'),('rasp','OD2'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+28.05,resSelectionSubs('asp','OD2',subs)))
IDSpec['gly_i'] = cmd.select('gly_i',' br. gly_i1&br. gly_i2&br. gly_i3&br. gly_i4&br. gly_i5&br. gly_i6&br. gly_i7&br. gly_i8&br. gly_i9&br. gly_i10&br. gly_i11&br. gly_i12&br. gly_i13&br. gly_i14&br. gly_i15&br. gly_i16&br. gly_i17&br. gly_i18')
IDSpec['r_gly_i'] = cmd.count_atoms(resSelectionSubs('gly_i', subs=subs, selection=True))
cmd.delete('gly_i1')
cmd.delete('gly_i2')
cmd.delete('gly_i3')
cmd.delete('gly_i4')
cmd.delete('gly_i5')
cmd.delete('gly_i6')
cmd.delete('gly_i7')
cmd.delete('gly_i8')
cmd.delete('gly_i9')
cmd.delete('gly_i10')
cmd.delete('gly_i11')
cmd.delete('gly_i12')
cmd.delete('gly_i13')
cmd.delete('gly_i14')
cmd.delete('gly_i15')
cmd.delete('gly_i16')
cmd.delete('gly_i17')
cmd.delete('gly_i18')
IDSpec[(('asp','CG'),('sgly','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.82,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','N'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.51,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly','O'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+31.12,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+29.18,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','N'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.90,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly','O'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+31.50,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.98,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','N'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.66,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly','O'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+31.28,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly_i','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+25.90,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly_i','N'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+25.11,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('asp','CG'),('sgly_i','O'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.01,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly_i','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.38,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly_i','N'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+25.55,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('asp','OD1'),('sgly_i','O'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+28.47,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly_i','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+25.99,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly_i','N'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+25.27,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('asp','OD2'),('sgly_i','O'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.05,resSelectionSubs('gly_i','O',subs,selection=True)))
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
IDSpec['S_2gd6_5_1_99_4'] = cmd.select('S_2gd6_5_1_99_4', 'gly|gly_i|asp')
cmd.delete('gly')
cmd.delete('gly_i')
cmd.delete('asp')
