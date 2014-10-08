'''
FUNC:S_1uip_3_5_4_4
PDB:1uip
EC:3.5.4.4
RESI:glu,glu,tyr,asp
LOCI:a-217,238,240,295;
'''
IDSpec[(('glu','CD'),('rtyr','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.30,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','CD'),('rtyr','CZ'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.17,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','CD'),('rtyr','OH'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.74,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE1'),('rtyr','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.44,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE1'),('rtyr','CZ'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.34,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE1'),('rtyr','OH'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.99,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE2'),('rtyr','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.14,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE2'),('rtyr','CZ'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.84,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE2'),('rtyr','OH'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.30,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','CD'),('rglu_i','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.44,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.21,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.82,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu_i','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.09,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.56,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.74,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu_i','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.21,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.16,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.26,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','CD'),('rasp','CG'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.00,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','CD'),('rasp','OD1'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.35,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','CD'),('rasp','OD2'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE1'),('rasp','CG'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.96,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE1'),('rasp','OD1'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.06,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE1'),('rasp','OD2'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.20,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE2'),('rasp','CG'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.79,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE2'),('rasp','OD1'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.42,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE2'),('rasp','OD2'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.85,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('tyr','CE1'),('sglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.30,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.44,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.14,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.17,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.34,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.84,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.74,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.99,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.30,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rglu_i','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.99,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('tyr','CE1'),('rglu_i','OE1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.50,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu_i','OE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.86,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('tyr','CZ'),('rglu_i','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.77,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('tyr','CZ'),('rglu_i','OE1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.26,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('tyr','CZ'),('rglu_i','OE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.60,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('tyr','OH'),('rglu_i','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.88,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('tyr','OH'),('rglu_i','OE1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.20,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('tyr','OH'),('rglu_i','OE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.68,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.20,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.88,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.57,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.04,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.76,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.32,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.94,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.71,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.32,resSelectionSubs('asp','OD2',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.44,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.09,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.21,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.21,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.56,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.16,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.82,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.74,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.26,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('styr','CE1'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.99,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('styr','CZ'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.77,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu_i','CD'),('styr','OH'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.88,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('styr','CE1'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.50,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('styr','CZ'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.26,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('styr','OH'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.20,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('styr','CE1'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.86,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('styr','CZ'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.60,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('styr','OH'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.68,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu_i','CD'),('rasp','CG'))] = cmd.select('glu_i19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.24,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu_i','CD'),('rasp','OD1'))] = cmd.select('glu_i20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.63,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu_i','CD'),('rasp','OD2'))] = cmd.select('glu_i21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.07,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu_i','OE1'),('rasp','CG'))] = cmd.select('glu_i22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.47,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu_i','OE1'),('rasp','OD1'))] = cmd.select('glu_i23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.70,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu_i','OE1'),('rasp','OD2'))] = cmd.select('glu_i24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.37,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu_i','OE2'),('rasp','CG'))] = cmd.select('glu_i25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.29,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu_i','OE2'),('rasp','OD1'))] = cmd.select('glu_i26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.86,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu_i','OE2'),('rasp','OD2'))] = cmd.select('glu_i27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.06,resSelectionSubs('asp','OD2',subs)))
IDSpec['glu_i'] = cmd.select('glu_i',' br. glu_i1&br. glu_i2&br. glu_i3&br. glu_i4&br. glu_i5&br. glu_i6&br. glu_i7&br. glu_i8&br. glu_i9&br. glu_i10&br. glu_i11&br. glu_i12&br. glu_i13&br. glu_i14&br. glu_i15&br. glu_i16&br. glu_i17&br. glu_i18&br. glu_i19&br. glu_i20&br. glu_i21&br. glu_i22&br. glu_i23&br. glu_i24&br. glu_i25&br. glu_i26&br. glu_i27')
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
cmd.delete('glu_i19')
cmd.delete('glu_i20')
cmd.delete('glu_i21')
cmd.delete('glu_i22')
cmd.delete('glu_i23')
cmd.delete('glu_i24')
cmd.delete('glu_i25')
cmd.delete('glu_i26')
cmd.delete('glu_i27')
IDSpec[(('asp','CG'),('sglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.00,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.96,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.79,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.35,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.06,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.42,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.22,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.20,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.85,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.20,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CZ'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.04,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','OH'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.94,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.88,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CZ'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.76,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','OH'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.71,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.57,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CZ'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.32,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','OH'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.32,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu_i','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.24,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu_i','OE1'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.47,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu_i','OE2'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.29,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu_i','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.63,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu_i','OE1'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.70,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu_i','OE2'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.86,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu_i','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.07,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu_i','OE1'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.37,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu_i','OE2'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.06,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec['S_1uip_3_5_4_4'] = cmd.select('S_1uip_3_5_4_4', 'glu|tyr|glu_i|asp')
cmd.delete('glu')
cmd.delete('tyr')
cmd.delete('glu_i')
cmd.delete('asp')
