'''
FUNC:S_1br2_3_6_1_32
PDB:1br2
EC:3.6.1.32
RESI:gly,asn,gly,glu
LOCI:a-180,242,468,470;
'''
IDSpec[(('asn','CG'),('rgly','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.48,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asn','CG'),('rgly','N'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.85,resSelectionSubs('gly','N',subs)))
IDSpec[(('asn','CG'),('rgly','O'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.69,resSelectionSubs('gly','O',subs)))
IDSpec[(('asn','ND2'),('rgly','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.13,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asn','ND2'),('rgly','N'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.35,resSelectionSubs('gly','N',subs)))
IDSpec[(('asn','ND2'),('rgly','O'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.29,resSelectionSubs('gly','O',subs)))
IDSpec[(('asn','OD1'),('rgly','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.30,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asn','OD1'),('rgly','N'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.89,resSelectionSubs('gly','N',subs)))
IDSpec[(('asn','OD1'),('rgly','O'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.14,resSelectionSubs('gly','O',subs)))
IDSpec[(('asn','CG'),('rgly_i','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.41,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('asn','CG'),('rgly_i','N'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.11,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('asn','CG'),('rgly_i','O'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.47,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('asn','ND2'),('rgly_i','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.57,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('asn','ND2'),('rgly_i','N'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.22,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('asn','ND2'),('rgly_i','O'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.92,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('asn','OD1'),('rgly_i','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.62,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('asn','OD1'),('rgly_i','N'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.31,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('asn','OD1'),('rgly_i','O'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.70,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('asn','CG'),('rglu','CD'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.86,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','CG'),('rglu','OE1'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.65,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','CG'),('rglu','OE2'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.60,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','ND2'),('rglu','CD'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.77,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','ND2'),('rglu','OE1'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.52,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','ND2'),('rglu','OE2'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.53,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','OD1'),('rglu','CD'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.95,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','OD1'),('rglu','OE1'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.75,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','OD1'),('rglu','OE2'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+13.65,resSelectionSubs('glu','OE2',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
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
IDSpec[(('gly','CA'),('sasn','CG'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.48,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasn','ND2'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.13,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly','CA'),('sasn','OD1'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.30,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly','N'),('sasn','CG'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.85,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sasn','ND2'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.35,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly','N'),('sasn','OD1'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.89,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly','O'),('sasn','CG'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.69,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sasn','ND2'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.29,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly','O'),('sasn','OD1'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.14,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly','CA'),('rgly_i','CA'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.42,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','CA'),('rgly_i','N'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.78,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','CA'),('rgly_i','O'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.91,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','N'),('rgly_i','CA'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.01,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','N'),('rgly_i','N'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.40,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','N'),('rgly_i','O'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.47,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','O'),('rgly_i','CA'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.10,resSelectionSubs('gly_i','CA',subs)))
IDSpec[(('gly','O'),('rgly_i','N'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.49,resSelectionSubs('gly_i','N',subs)))
IDSpec[(('gly','O'),('rgly_i','O'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.97,resSelectionSubs('gly_i','O',subs)))
IDSpec[(('gly','CA'),('rglu','CD'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.76,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','CA'),('rglu','OE1'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.64,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','CA'),('rglu','OE2'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.85,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','N'),('rglu','CD'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.51,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','N'),('rglu','OE1'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','N'),('rglu','OE2'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.62,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly','O'),('rglu','CD'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+14.13,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly','O'),('rglu','OE1'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+13.01,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly','O'),('rglu','OE2'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+15.22,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('gly_i','CA'),('sasn','CG'))] = cmd.select('gly_i1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.41,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasn','ND2'))] = cmd.select('gly_i2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.57,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sasn','OD1'))] = cmd.select('gly_i3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+12.62,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasn','CG'))] = cmd.select('gly_i4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.11,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasn','ND2'))] = cmd.select('gly_i5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.22,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly_i','N'),('sasn','OD1'))] = cmd.select('gly_i6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.31,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasn','CG'))] = cmd.select('gly_i7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.47,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasn','ND2'))] = cmd.select('gly_i8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.92,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly_i','O'),('sasn','OD1'))] = cmd.select('gly_i9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.70,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','CA'))] = cmd.select('gly_i10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.42,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','N'))] = cmd.select('gly_i11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.01,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','CA'),('sgly','O'))] = cmd.select('gly_i12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.10,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','CA'))] = cmd.select('gly_i13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.78,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','N'))] = cmd.select('gly_i14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.40,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','N'),('sgly','O'))] = cmd.select('gly_i15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.49,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','CA'))] = cmd.select('gly_i16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.91,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','N'))] = cmd.select('gly_i17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.47,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('gly_i','O'),('sgly','O'))] = cmd.select('gly_i18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.97,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('gly_i','CA'),('rglu','CD'))] = cmd.select('gly_i19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.42,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly_i','CA'),('rglu','OE1'))] = cmd.select('gly_i20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.77,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly_i','CA'),('rglu','OE2'))] = cmd.select('gly_i21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.29,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly_i','N'),('rglu','CD'))] = cmd.select('gly_i22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.29,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly_i','N'),('rglu','OE1'))] = cmd.select('gly_i23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.56,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly_i','N'),('rglu','OE2'))] = cmd.select('gly_i24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.99,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gly_i','O'),('rglu','CD'))] = cmd.select('gly_i25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.19,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gly_i','O'),('rglu','OE1'))] = cmd.select('gly_i26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.73,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gly_i','O'),('rglu','OE2'))] = cmd.select('gly_i27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.13,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('sasn','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.86,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','ND2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.77,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','OD1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.95,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.65,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','ND2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.52,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','OD1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.75,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.60,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','ND2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.53,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','OD1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.65,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.76,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','N'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.51,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly','O'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.13,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.64,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','N'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.40,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly','O'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.01,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.85,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','N'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.62,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly','O'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.22,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly_i','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.42,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly_i','N'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.29,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('glu','CD'),('sgly_i','O'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.19,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly_i','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.77,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly_i','N'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.56,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgly_i','O'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.73,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly_i','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.29,resSelectionSubs('gly_i','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly_i','N'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.99,resSelectionSubs('gly_i','N',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgly_i','O'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.13,resSelectionSubs('gly_i','O',subs,selection=True)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27')
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
IDSpec['S_1br2_3_6_1_32'] = cmd.select('S_1br2_3_6_1_32', 'asn|gly|gly_i|glu')
cmd.delete('asn')
cmd.delete('gly')
cmd.delete('gly_i')
cmd.delete('glu')