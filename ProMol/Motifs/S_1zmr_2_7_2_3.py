'''
FUNC:S_1zmr_2_7_2_3
PDB:1zmr
EC:2.7.2.3
RESI:arg,lys,gly,gly
LOCI:a-36,193,341,364;
'''
IDSpec[(('gly','CA'),('rlys','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+17.43,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','CA'),('rlys','CE'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.39,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','CA'),('rlys','NZ'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.45,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','N'),('rlys','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+17.94,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','N'),('rlys','CE'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+18.84,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','N'),('rlys','NZ'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+18.94,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','O'),('rlys','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+18.11,resSelectionSubs('lys','CD',subs)))
IDSpec[(('gly','O'),('rlys','CE'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.22,resSelectionSubs('lys','CE',subs)))
IDSpec[(('gly','O'),('rlys','NZ'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.30,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('gly','CA'),('rgly','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.02,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','CA'),('rgly','N'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.98,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','CA'),('rgly','O'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.38,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','N'),('rgly','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','N'),('rgly','N'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.85,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','N'),('rgly','O'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.20,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','O'),('rgly','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.89,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gly','O'),('rgly','N'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.69,resSelectionSubs('gly','N',subs)))
IDSpec[(('gly','O'),('rgly','O'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.18,resSelectionSubs('gly','O',subs)))
IDSpec[(('gly','CA'),('rarg','CZ'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.88,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','CA'),('rarg','NE'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.76,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','CA'),('rarg','NH1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.43,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','N'),('rarg','CZ'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.65,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','N'),('rarg','NE'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.48,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','N'),('rarg','NH1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.28,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly','O'),('rarg','CZ'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.76,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly','O'),('rarg','NE'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.55,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly','O'),('rarg','NH1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.23,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('lys','CD'),('sgly','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.43,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','N'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.94,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','CD'),('sgly','O'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.11,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.39,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','N'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.84,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','CE'),('sgly','O'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.22,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.45,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','N'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.94,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys','NZ'),('sgly','O'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.30,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.83,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.43,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.75,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.38,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.10,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.20,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.89,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.63,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.82,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CD'),('rarg','CZ'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.65,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CD'),('rarg','NE'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+26.67,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CD'),('rarg','NH1'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.67,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','CE'),('rarg','CZ'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.04,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CE'),('rarg','NE'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+27.08,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CE'),('rarg','NH1'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.08,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','NZ'),('rarg','CZ'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+26.01,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','NZ'),('rarg','NE'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','NZ'),('rarg','NH1'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+25.99,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.02,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.84,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.89,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.98,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.85,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.69,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.38,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.20,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.18,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','CD'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+17.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','CE'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.38,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','CA'),('slys','NZ'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.89,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','CD'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+17.43,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','CE'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+18.10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','N'),('slys','NZ'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+18.63,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','CD'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+18.75,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','CE'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.20,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly_i','O'),('slys','NZ'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+19.82,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly_i','CA'),('rarg','CZ'))] = cmd.select('gly_i19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.43,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly_i','CA'),('rarg','NE'))] = cmd.select('gly_i20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.90,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly_i','CA'),('rarg','NH1'))] = cmd.select('gly_i21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.03,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly_i','N'),('rarg','CZ'))] = cmd.select('gly_i22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.92,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly_i','N'),('rarg','NE'))] = cmd.select('gly_i23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.40,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly_i','N'),('rarg','NH1'))] = cmd.select('gly_i24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.39,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('gly_i','O'),('rarg','CZ'))] = cmd.select('gly_i25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.54,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('gly_i','O'),('rarg','NE'))] = cmd.select('gly_i26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.82,resSelectionSubs('arg','NE',subs)))
IDSpec[(('gly_i','O'),('rarg','NH1'))] = cmd.select('gly_i27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.34,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sgly','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.88,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','N'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.65,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly','O'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.76,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.76,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','N'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.48,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly','O'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.55,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.43,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','N'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.28,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly','O'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.23,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+25.65,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+26.04,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+26.01,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+26.67,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+27.08,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+27.10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+25.67,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.08,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+25.99,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly_i','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.43,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly_i','N'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.92,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('arg','CZ'),('sgly_i','O'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.54,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly_i','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.90,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly_i','N'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.40,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('arg','NE'),('sgly_i','O'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.82,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly_i','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.03,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly_i','N'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.39,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('arg','NH1'),('sgly_i','O'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.34,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
IDSpec['S_1zmr_2_7_2_3'] = cmd.select('S_1zmr_2_7_2_3', 'gly|lys|gly_i|arg')
cmd.delete('gly')
cmd.delete('lys')
cmd.delete('gly_i')
cmd.delete('arg')
