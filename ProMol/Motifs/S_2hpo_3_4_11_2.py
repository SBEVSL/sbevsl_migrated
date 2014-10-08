'''
FUNC:S_2hpo_3_4_11_2
PDB:2hpo
EC:3.4.11.2
RESI:glu,glu,tyr
LOCI:a-264,298,381;
'''
IDSpec[(('glu','CD'),('rglu_i','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.45,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.21,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.13,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu_i','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.53,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.34,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.10,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu_i','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.46,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.23,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.02,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','CD'),('rtyr','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.20,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','CD'),('rtyr','CZ'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.16,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','CD'),('rtyr','OH'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.14,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE1'),('rtyr','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.69,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE1'),('rtyr','CZ'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.57,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE1'),('rtyr','OH'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.50,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE2'),('rtyr','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.73,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE2'),('rtyr','CZ'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.83,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE2'),('rtyr','OH'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.85,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.45,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.53,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.46,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.21,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.34,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.23,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.13,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.10,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.02,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('rtyr','CE1'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.63,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu_i','CD'),('rtyr','CZ'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.24,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu_i','CD'),('rtyr','OH'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.57,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu_i','OE1'),('rtyr','CE1'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.32,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu_i','OE1'),('rtyr','CZ'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.97,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu_i','OE1'),('rtyr','OH'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.20,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu_i','OE2'),('rtyr','CE1'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.90,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu_i','OE2'),('rtyr','CZ'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.50,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu_i','OE2'),('rtyr','OH'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.91,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('sglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.20,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.69,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.73,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.16,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.57,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.83,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.14,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.85,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu_i','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.63,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu_i','OE1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.32,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu_i','OE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.90,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu_i','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.24,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu_i','OE1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.97,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu_i','OE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.50,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu_i','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.57,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu_i','OE1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.20,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu_i','OE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.91,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18')
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
IDSpec['S_2hpo_3_4_11_2'] = cmd.select('S_2hpo_3_4_11_2', 'glu|glu_i|tyr')
cmd.delete('glu')
cmd.delete('glu_i')
cmd.delete('tyr')
