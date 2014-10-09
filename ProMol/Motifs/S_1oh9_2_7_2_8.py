'''
FUNC:S_1oh9_2_7_2_8
PDB:1oh9
EC:2.7.2.8
RESI:lys,gly,gly,lys
LOCI:a-8,11,45,217;
'''
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.72,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.63,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.99,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.38,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.36,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.70,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.73,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.82,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.98,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.21,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.91,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.31,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.68,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.32,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.71,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.57,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.31,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.88,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.14,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.82,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.45,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.16,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.59,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.12,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.21,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.43,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.95,resSelectionSubs('lys','NZ',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
IDSpec[(('gly','CA'),('slys','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.72,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CE'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.38,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','NZ'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.73,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.63,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CE'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.36,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','N'),('slys','NZ'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.82,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.99,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CE'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.70,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','O'),('slys','NZ'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.98,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','CA'),('rgly','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.08,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','CA'),('rgly','N'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.69,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','CA'),('rgly','O'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.41,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','N'),('rgly','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.44,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','N'),('rgly','N'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.84,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','N'),('rgly','O'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.65,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','O'),('rgly','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.23,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','O'),('rgly','N'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.20,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','O'),('rgly','O'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.25,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','CA'),('rlys','CD'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.04,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','CA'),('rlys','CE'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.62,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','CA'),('rlys','NZ'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.66,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','N'),('rlys','CD'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.61,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','N'),('rlys','CE'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.24,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','N'),('rlys','NZ'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.17,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','O'),('rlys','CD'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.92,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','O'),('rlys','CE'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.45,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','O'),('rlys','NZ'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.63,resSelectionSubs('lys','NZ',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27')
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
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
IDSpec[(('gly_i','CA'),('slys','CD'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.21,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','CE'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.68,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','NZ'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','CD'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.91,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','CE'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.32,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','NZ'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.31,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','CD'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.31,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','CE'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.71,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','NZ'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.88,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.08,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.44,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.23,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.69,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.84,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.20,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.41,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.65,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.25,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('rlys','CD'))] = cmd.select('gly_i19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.51,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly_i','CA'),('rlys','CE'))] = cmd.select('gly_i20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.19,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly_i','CA'),('rlys','NZ'))] = cmd.select('gly_i21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.52,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly_i','N'),('rlys','CD'))] = cmd.select('gly_i22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.05,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly_i','N'),('rlys','CE'))] = cmd.select('gly_i23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.77,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly_i','N'),('rlys','NZ'))] = cmd.select('gly_i24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly_i','O'),('rlys','CD'))] = cmd.select('gly_i25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.73,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly_i','O'),('rlys','CE'))] = cmd.select('gly_i26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.42,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly_i','O'),('rlys','NZ'))] = cmd.select('gly_i27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.59,resSelectionSubs('lys','NZ',subs)))
IDSpec['gly_i'] = cmd.select('gly_i',' br. gly_i1&br. gly_i2&br. gly_i3&br. gly_i4&br. gly_i5&br. gly_i6&br. gly_i7&br. gly_i8&br. gly_i9&br. gly_i10&br. gly_i11&br. gly_i12&br. gly_i13&br. gly_i14&br. gly_i15&br. gly_i16&br. gly_i17&br. gly_i18&br. gly_i19&br. gly_i20&br. gly_i21&br. gly_i22&br. gly_i23&br. gly_i24&br. gly_i25&br. gly_i26&br. gly_i27')
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
cmd.delete('gly_i19')
cmd.delete('gly_i20')
cmd.delete('gly_i21')
cmd.delete('gly_i22')
cmd.delete('gly_i23')
cmd.delete('gly_i24')
cmd.delete('gly_i25')
cmd.delete('gly_i26')
cmd.delete('gly_i27')
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.14,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.16,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.21,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.82,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.59,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.43,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.45,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.12,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.95,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','CA'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.04,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','N'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.61,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','O'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.92,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','CA'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.62,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','N'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.24,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','O'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.45,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','CA'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.66,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','N'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.17,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','O'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.63,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly_i','CA'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.51,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly_i','N'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.05,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly_i','O'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.73,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly_i','CA'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.19,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly_i','N'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.77,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly_i','O'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.42,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly_i','CA'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.52,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly_i','N'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.87,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly_i','O'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.59,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27')
IDSpec['r_lys_i'] = cmd.count_atoms(resSelectionSubs('lys_i', subs=subs, selection=True))
cmd.delete('lys_i1')
cmd.delete('lys_i2')
cmd.delete('lys_i3')
cmd.delete('lys_i4')
cmd.delete('lys_i5')
cmd.delete('lys_i6')
cmd.delete('lys_i7')
cmd.delete('lys_i8')
cmd.delete('lys_i9')
cmd.delete('lys_i10')
cmd.delete('lys_i11')
cmd.delete('lys_i12')
cmd.delete('lys_i13')
cmd.delete('lys_i14')
cmd.delete('lys_i15')
cmd.delete('lys_i16')
cmd.delete('lys_i17')
cmd.delete('lys_i18')
cmd.delete('lys_i19')
cmd.delete('lys_i20')
cmd.delete('lys_i21')
cmd.delete('lys_i22')
cmd.delete('lys_i23')
cmd.delete('lys_i24')
cmd.delete('lys_i25')
cmd.delete('lys_i26')
cmd.delete('lys_i27')
IDSpec['S_1oh9_2_7_2_8'] = cmd.select('S_1oh9_2_7_2_8', 'lys|gly|gly_i|lys_i')
cmd.delete('lys')
cmd.delete('gly')
cmd.delete('gly_i')
cmd.delete('lys_i')
