'''
FUNC:S_2cet_3_2_1_21
PDB:2cet
EC:3.2.1.21
RESI:glu,asn,glu
LOCI:a-166,293,351;
'''
IDSpec[(('glu','CD'),('rasn','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.42,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','CD'),('rasn','ND2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.41,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','CD'),('rasn','OD1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.55,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE1'),('rasn','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.50,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE1'),('rasn','ND2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.42,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE1'),('rasn','OD1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.63,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE2'),('rasn','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.52,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE2'),('rasn','ND2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.74,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE2'),('rasn','OD1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.74,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','CD'),('rglu','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.29,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','CD'),('rglu','OE1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.96,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','CD'),('rglu','OE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.16,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.73,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE1'),('rglu','OE1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.24,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu','OE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.55,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.75,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE2'),('rglu','OE1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.34,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu','OE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.89,resSelectionSubs('glu','OE2',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18')
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
IDSpec[(('asn','CG'),('sglu','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.42,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.52,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.41,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.42,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.74,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.55,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.63,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.74,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','CG'),('rglu','CD'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.64,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','CG'),('rglu','OE1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.96,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','CG'),('rglu','OE2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.04,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','ND2'),('rglu','CD'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.10,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','ND2'),('rglu','OE1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','ND2'),('rglu','OE2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.20,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','OD1'),('rglu','CD'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.95,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','OD1'),('rglu','OE1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.56,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','OD1'),('rglu','OE2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.29,resSelectionSubs('glu','OE2',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
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
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.29,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.73,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.75,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.96,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.24,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.34,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.16,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.55,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.89,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sasn','CG'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.64,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sasn','ND2'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.10,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sasn','OD1'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.95,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sasn','CG'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.96,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sasn','ND2'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.40,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sasn','OD1'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.56,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sasn','CG'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.04,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sasn','ND2'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.20,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sasn','OD1'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.29,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec['glu_i'] = cmd.select('glu_i',' br. glu_i1&br. glu_i2&br. glu_i3&br. glu_i4&br. glu_i5&br. glu_i6&br. glu_i7&br. glu_i8&br. glu_i9&br. glu_i10&br. glu_i11&br. glu_i12&br. glu_i13&br. glu_i14&br. glu_i15&br. glu_i16&br. glu_i17&br. glu_i18')
IDSpec['r_glu_i'] = cmd.count_atoms(resSelectionSubs('glu_i', subs=subs, selection=True))
cmd.delete('glu_i1')
cmd.delete('glu_i2')
cmd.delete('glu_i3')
cmd.delete('glu_i4')
cmd.delete('glu_i5')
cmd.delete('glu_i6')
cmd.delete('glu_i7')
cmd.delete('glu_i8')
cmd.delete('glu_i9')
cmd.delete('glu_i10')
cmd.delete('glu_i11')
cmd.delete('glu_i12')
cmd.delete('glu_i13')
cmd.delete('glu_i14')
cmd.delete('glu_i15')
cmd.delete('glu_i16')
cmd.delete('glu_i17')
cmd.delete('glu_i18')
IDSpec['S_2cet_3_2_1_21'] = cmd.select('S_2cet_3_2_1_21', 'glu|asn|glu_i')
cmd.delete('glu')
cmd.delete('asn')
cmd.delete('glu_i')
