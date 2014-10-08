'''
FUNC:S_1xdb_1_18_6_1
PDB:1xdb
EC:1.18.6.1
RESI:lys,gly,lys,lys,glu
LOCI:a-10,12,15,41,129;
'''
IDSpec[(('lys','CD'),('rgly','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.79,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CD'),('rgly','N'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.72,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CD'),('rgly','O'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.77,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CE'),('rgly','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.66,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','CE'),('rgly','N'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.50,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','CE'),('rgly','O'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.87,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','NZ'),('rgly','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.16,resSelectionSubs('gly','CA',subs)))
IDSpec[(('lys','NZ'),('rgly','N'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.96,resSelectionSubs('gly','N',subs)))
IDSpec[(('lys','NZ'),('rgly','O'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.60,resSelectionSubs('gly','O',subs)))
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.90,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.37,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.56,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.07,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.43,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.68,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.37,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.52,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.69,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.13,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.63,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.67,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.10,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.14,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.64,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.96,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CD'),('rlys_ii','CD'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.01,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','CD'),('rlys_ii','CE'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.49,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','CD'),('rlys_ii','NZ'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.41,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_ii','CD'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.36,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','CE'),('rlys_ii','CE'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.97,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','CE'),('rlys_ii','NZ'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.88,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','CD'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.93,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','CE'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.55,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','NZ'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.44,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27&br. lys28&br. lys29&br. lys30&br. lys31&br. lys32&br. lys33&br. lys34&br. lys35&br. lys36')
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
cmd.delete('lys28')
cmd.delete('lys29')
cmd.delete('lys30')
cmd.delete('lys31')
cmd.delete('lys32')
cmd.delete('lys33')
cmd.delete('lys34')
cmd.delete('lys35')
cmd.delete('lys36')
IDSpec[(('gly','CA'),('slys','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.79,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','CE'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.66,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','CA'),('slys','NZ'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.16,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.72,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','N'),('slys','CE'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.50,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','N'),('slys','NZ'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.96,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.77,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gly','O'),('slys','CE'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.87,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gly','O'),('slys','NZ'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.60,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gly','CA'),('rlys_i','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.43,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('gly','CA'),('rlys_i','CE'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.52,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('gly','CA'),('rlys_i','NZ'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.49,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('gly','N'),('rlys_i','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.10,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('gly','N'),('rlys_i','CE'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.24,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('gly','N'),('rlys_i','NZ'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.54,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('gly','O'),('rlys_i','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.46,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('gly','O'),('rlys_i','CE'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.82,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('gly','O'),('rlys_i','NZ'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.46,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('gly','CA'),('rglu','CD'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.81,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','CA'),('rglu','OE1'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.86,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','CA'),('rglu','OE2'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.81,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','N'),('rglu','CD'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.81,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','N'),('rglu','OE1'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.01,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','N'),('rglu','OE2'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.74,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','O'),('rglu','CD'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.16,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','O'),('rglu','OE1'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.91,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','O'),('rglu','OE2'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.36,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','CA'),('rlys_ii','CD'))] = cmd.select('gly28', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.11,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('gly','CA'),('rlys_ii','CE'))] = cmd.select('gly29', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+13.69,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('gly','CA'),('rlys_ii','NZ'))] = cmd.select('gly30', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+14.62,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('gly','N'),('rlys_ii','CD'))] = cmd.select('gly31', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.44,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('gly','N'),('rlys_ii','CE'))] = cmd.select('gly32', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+13.19,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('gly','N'),('rlys_ii','NZ'))] = cmd.select('gly33', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.22,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('gly','O'),('rlys_ii','CD'))] = cmd.select('gly34', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.31,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('gly','O'),('rlys_ii','CE'))] = cmd.select('gly35', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.78,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('gly','O'),('rlys_ii','NZ'))] = cmd.select('gly36', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.61,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27&br. gly28&br. gly29&br. gly30&br. gly31&br. gly32&br. gly33&br. gly34&br. gly35&br. gly36')
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
cmd.delete('gly28')
cmd.delete('gly29')
cmd.delete('gly30')
cmd.delete('gly31')
cmd.delete('gly32')
cmd.delete('gly33')
cmd.delete('gly34')
cmd.delete('gly35')
cmd.delete('gly36')
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.90,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.07,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.37,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.37,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.43,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.52,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.56,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.68,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.69,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','CA'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.43,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','N'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.10,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sgly','O'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.46,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','CA'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.52,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','N'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.24,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sgly','O'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.82,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','CA'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.49,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','N'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.54,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sgly','O'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.46,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rglu','CD'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.79,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','CD'),('rglu','OE1'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.85,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','CD'),('rglu','OE2'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.89,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','CE'),('rglu','CD'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.34,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','CE'),('rglu','OE1'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.57,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','CE'),('rglu','OE2'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.21,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','NZ'),('rglu','CD'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.56,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','NZ'),('rglu','OE1'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.94,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','NZ'),('rglu','OE2'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.19,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','CD'))] = cmd.select('lys_i28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.73,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','CE'))] = cmd.select('lys_i29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.71,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','NZ'))] = cmd.select('lys_i30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+19.89,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','CD'))] = cmd.select('lys_i31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.72,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','CE'))] = cmd.select('lys_i32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.63,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','NZ'))] = cmd.select('lys_i33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.82,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','CD'))] = cmd.select('lys_i34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.49,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','CE'))] = cmd.select('lys_i35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.28,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','NZ'))] = cmd.select('lys_i36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.40,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27&br. lys_i28&br. lys_i29&br. lys_i30&br. lys_i31&br. lys_i32&br. lys_i33&br. lys_i34&br. lys_i35&br. lys_i36')
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
cmd.delete('lys_i28')
cmd.delete('lys_i29')
cmd.delete('lys_i30')
cmd.delete('lys_i31')
cmd.delete('lys_i32')
cmd.delete('lys_i33')
cmd.delete('lys_i34')
cmd.delete('lys_i35')
cmd.delete('lys_i36')
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.13,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.67,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.64,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.40,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.20,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.63,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.14,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.96,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.81,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','N'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.81,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','O'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.16,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.86,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','N'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.01,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','O'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.91,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.81,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','N'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.74,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','O'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.36,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.79,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','CE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.34,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','NZ'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.56,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.85,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','CE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.57,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','NZ'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.94,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.89,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','CE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.21,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','NZ'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.19,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('rlys_ii','CD'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.31,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('glu','CD'),('rlys_ii','CE'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.59,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('glu','CD'),('rlys_ii','NZ'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+17.96,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys_ii','CD'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+17.34,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('glu','OE1'),('rlys_ii','CE'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+17.56,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('glu','OE1'),('rlys_ii','NZ'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+18.90,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys_ii','CD'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.21,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('glu','OE2'),('rlys_ii','CE'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.45,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('glu','OE2'),('rlys_ii','NZ'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.80,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
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
IDSpec[(('lys_ii','CD'),('slys','CD'))] = cmd.select('lys_ii1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.01,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','CE'))] = cmd.select('lys_ii2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.36,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','NZ'))] = cmd.select('lys_ii3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CD'))] = cmd.select('lys_ii4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.49,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CE'))] = cmd.select('lys_ii5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.97,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','NZ'))] = cmd.select('lys_ii6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+14.55,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CD'))] = cmd.select('lys_ii7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.41,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CE'))] = cmd.select('lys_ii8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.88,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','NZ'))] = cmd.select('lys_ii9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.44,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sgly','CA'))] = cmd.select('lys_ii10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.11,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sgly','N'))] = cmd.select('lys_ii11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.44,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sgly','O'))] = cmd.select('lys_ii12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.31,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sgly','CA'))] = cmd.select('lys_ii13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.69,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sgly','N'))] = cmd.select('lys_ii14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.19,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sgly','O'))] = cmd.select('lys_ii15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.78,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sgly','CA'))] = cmd.select('lys_ii16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.62,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sgly','N'))] = cmd.select('lys_ii17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.22,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sgly','O'))] = cmd.select('lys_ii18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.61,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CD'))] = cmd.select('lys_ii19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.73,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CE'))] = cmd.select('lys_ii20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.72,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','NZ'))] = cmd.select('lys_ii21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.49,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CD'))] = cmd.select('lys_ii22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.71,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CE'))] = cmd.select('lys_ii23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.63,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','NZ'))] = cmd.select('lys_ii24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.28,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CD'))] = cmd.select('lys_ii25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.89,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CE'))] = cmd.select('lys_ii26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.82,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','NZ'))] = cmd.select('lys_ii27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.40,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sglu','CD'))] = cmd.select('lys_ii28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sglu','OE1'))] = cmd.select('lys_ii29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.34,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sglu','OE2'))] = cmd.select('lys_ii30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.21,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sglu','CD'))] = cmd.select('lys_ii31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.59,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sglu','OE1'))] = cmd.select('lys_ii32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.56,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sglu','OE2'))] = cmd.select('lys_ii33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.45,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sglu','CD'))] = cmd.select('lys_ii34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.96,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sglu','OE1'))] = cmd.select('lys_ii35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.90,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sglu','OE2'))] = cmd.select('lys_ii36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.80,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['lys_ii'] = cmd.select('lys_ii',' br. lys_ii1&br. lys_ii2&br. lys_ii3&br. lys_ii4&br. lys_ii5&br. lys_ii6&br. lys_ii7&br. lys_ii8&br. lys_ii9&br. lys_ii10&br. lys_ii11&br. lys_ii12&br. lys_ii13&br. lys_ii14&br. lys_ii15&br. lys_ii16&br. lys_ii17&br. lys_ii18&br. lys_ii19&br. lys_ii20&br. lys_ii21&br. lys_ii22&br. lys_ii23&br. lys_ii24&br. lys_ii25&br. lys_ii26&br. lys_ii27&br. lys_ii28&br. lys_ii29&br. lys_ii30&br. lys_ii31&br. lys_ii32&br. lys_ii33&br. lys_ii34&br. lys_ii35&br. lys_ii36')
IDSpec['r_lys_ii'] = cmd.count_atoms(resSelectionSubs('lys_ii', subs=subs, selection=True))
cmd.delete('lys_ii1')
cmd.delete('lys_ii2')
cmd.delete('lys_ii3')
cmd.delete('lys_ii4')
cmd.delete('lys_ii5')
cmd.delete('lys_ii6')
cmd.delete('lys_ii7')
cmd.delete('lys_ii8')
cmd.delete('lys_ii9')
cmd.delete('lys_ii10')
cmd.delete('lys_ii11')
cmd.delete('lys_ii12')
cmd.delete('lys_ii13')
cmd.delete('lys_ii14')
cmd.delete('lys_ii15')
cmd.delete('lys_ii16')
cmd.delete('lys_ii17')
cmd.delete('lys_ii18')
cmd.delete('lys_ii19')
cmd.delete('lys_ii20')
cmd.delete('lys_ii21')
cmd.delete('lys_ii22')
cmd.delete('lys_ii23')
cmd.delete('lys_ii24')
cmd.delete('lys_ii25')
cmd.delete('lys_ii26')
cmd.delete('lys_ii27')
cmd.delete('lys_ii28')
cmd.delete('lys_ii29')
cmd.delete('lys_ii30')
cmd.delete('lys_ii31')
cmd.delete('lys_ii32')
cmd.delete('lys_ii33')
cmd.delete('lys_ii34')
cmd.delete('lys_ii35')
cmd.delete('lys_ii36')
IDSpec['S_1xdb_1_18_6_1'] = cmd.select('S_1xdb_1_18_6_1', 'lys|gly|lys_i|glu|lys_ii')
cmd.delete('lys')
cmd.delete('gly')
cmd.delete('lys_i')
cmd.delete('glu')
cmd.delete('lys_ii')
