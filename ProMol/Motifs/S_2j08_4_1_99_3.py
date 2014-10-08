'''
FUNC:S_2j08_4_1_99_3
PDB:2j08
EC:4.1.99.3
RESI:trp,trp,trp
LOCI:a-275,328,351;
'''
IDSpec[(('trp','CE2'),('rtrp_i','CE2'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.03,resSelectionSubs('trp_i','CE2',subs)))
IDSpec[(('trp','CE2'),('rtrp_i','CZ2'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.05,resSelectionSubs('trp_i','CZ2',subs)))
IDSpec[(('trp','CE2'),('rtrp_i','NE1'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.63,resSelectionSubs('trp_i','NE1',subs)))
IDSpec[(('trp','CZ2'),('rtrp_i','CE2'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.17,resSelectionSubs('trp_i','CE2',subs)))
IDSpec[(('trp','CZ2'),('rtrp_i','CZ2'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.19,resSelectionSubs('trp_i','CZ2',subs)))
IDSpec[(('trp','CZ2'),('rtrp_i','NE1'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.63,resSelectionSubs('trp_i','NE1',subs)))
IDSpec[(('trp','NE1'),('rtrp_i','CE2'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.70,resSelectionSubs('trp_i','CE2',subs)))
IDSpec[(('trp','NE1'),('rtrp_i','CZ2'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.77,resSelectionSubs('trp_i','CZ2',subs)))
IDSpec[(('trp','NE1'),('rtrp_i','NE1'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.29,resSelectionSubs('trp_i','NE1',subs)))
IDSpec[(('trp','CE2'),('rtrp_ii','CE2'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.51,resSelectionSubs('trp_ii','CE2',subs)))
IDSpec[(('trp','CE2'),('rtrp_ii','CZ2'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+12.26,resSelectionSubs('trp_ii','CZ2',subs)))
IDSpec[(('trp','CE2'),('rtrp_ii','NE1'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.88,resSelectionSubs('trp_ii','NE1',subs)))
IDSpec[(('trp','CZ2'),('rtrp_ii','CE2'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.29,resSelectionSubs('trp_ii','CE2',subs)))
IDSpec[(('trp','CZ2'),('rtrp_ii','CZ2'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.14,resSelectionSubs('trp_ii','CZ2',subs)))
IDSpec[(('trp','CZ2'),('rtrp_ii','NE1'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.50,resSelectionSubs('trp_ii','NE1',subs)))
IDSpec[(('trp','NE1'),('rtrp_ii','CE2'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+12.05,resSelectionSubs('trp_ii','CE2',subs)))
IDSpec[(('trp','NE1'),('rtrp_ii','CZ2'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+12.67,resSelectionSubs('trp_ii','CZ2',subs)))
IDSpec[(('trp','NE1'),('rtrp_ii','NE1'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+12.57,resSelectionSubs('trp_ii','NE1',subs)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9&br. trp10&br. trp11&br. trp12&br. trp13&br. trp14&br. trp15&br. trp16&br. trp17&br. trp18')
IDSpec['r_trp'] = cmd.count_atoms(resSelectionSubs('trp', subs=subs, selection=True))
cmd.delete('trp1')
cmd.delete('trp2')
cmd.delete('trp3')
cmd.delete('trp4')
cmd.delete('trp5')
cmd.delete('trp6')
cmd.delete('trp7')
cmd.delete('trp8')
cmd.delete('trp9')
cmd.delete('trp10')
cmd.delete('trp11')
cmd.delete('trp12')
cmd.delete('trp13')
cmd.delete('trp14')
cmd.delete('trp15')
cmd.delete('trp16')
cmd.delete('trp17')
cmd.delete('trp18')
IDSpec[(('trp_i','CE2'),('strp','CE2'))] = cmd.select('trp_i1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.03,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('trp_i','CE2'),('strp','CZ2'))] = cmd.select('trp_i2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.17,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('trp_i','CE2'),('strp','NE1'))] = cmd.select('trp_i3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+6.70,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('trp_i','CZ2'),('strp','CE2'))] = cmd.select('trp_i4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.05,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('trp_i','CZ2'),('strp','CZ2'))] = cmd.select('trp_i5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.19,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('trp_i','CZ2'),('strp','NE1'))] = cmd.select('trp_i6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.77,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('trp_i','NE1'),('strp','CE2'))] = cmd.select('trp_i7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.63,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('trp_i','NE1'),('strp','CZ2'))] = cmd.select('trp_i8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.63,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('trp_i','NE1'),('strp','NE1'))] = cmd.select('trp_i9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+6.29,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('trp_i','CE2'),('rtrp_ii','CE2'))] = cmd.select('trp_i10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.96,resSelectionSubs('trp_ii','CE2',subs)))
IDSpec[(('trp_i','CE2'),('rtrp_ii','CZ2'))] = cmd.select('trp_i11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+14.14,resSelectionSubs('trp_ii','CZ2',subs)))
IDSpec[(('trp_i','CE2'),('rtrp_ii','NE1'))] = cmd.select('trp_i12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+14.91,resSelectionSubs('trp_ii','NE1',subs)))
IDSpec[(('trp_i','CZ2'),('rtrp_ii','CE2'))] = cmd.select('trp_i13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.78,resSelectionSubs('trp_ii','CE2',subs)))
IDSpec[(('trp_i','CZ2'),('rtrp_ii','CZ2'))] = cmd.select('trp_i14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.04,resSelectionSubs('trp_ii','CZ2',subs)))
IDSpec[(('trp_i','CZ2'),('rtrp_ii','NE1'))] = cmd.select('trp_i15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.71,resSelectionSubs('trp_ii','NE1',subs)))
IDSpec[(('trp_i','NE1'),('rtrp_ii','CE2'))] = cmd.select('trp_i16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.47,resSelectionSubs('trp_ii','CE2',subs)))
IDSpec[(('trp_i','NE1'),('rtrp_ii','CZ2'))] = cmd.select('trp_i17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.70,resSelectionSubs('trp_ii','CZ2',subs)))
IDSpec[(('trp_i','NE1'),('rtrp_ii','NE1'))] = cmd.select('trp_i18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+15.34,resSelectionSubs('trp_ii','NE1',subs)))
IDSpec['trp_i'] = cmd.select('trp_i',' br. trp_i1&br. trp_i2&br. trp_i3&br. trp_i4&br. trp_i5&br. trp_i6&br. trp_i7&br. trp_i8&br. trp_i9&br. trp_i10&br. trp_i11&br. trp_i12&br. trp_i13&br. trp_i14&br. trp_i15&br. trp_i16&br. trp_i17&br. trp_i18')
IDSpec['r_trp_i'] = cmd.count_atoms(resSelectionSubs('trp_i', subs=subs, selection=True))
cmd.delete('trp_i1')
cmd.delete('trp_i2')
cmd.delete('trp_i3')
cmd.delete('trp_i4')
cmd.delete('trp_i5')
cmd.delete('trp_i6')
cmd.delete('trp_i7')
cmd.delete('trp_i8')
cmd.delete('trp_i9')
cmd.delete('trp_i10')
cmd.delete('trp_i11')
cmd.delete('trp_i12')
cmd.delete('trp_i13')
cmd.delete('trp_i14')
cmd.delete('trp_i15')
cmd.delete('trp_i16')
cmd.delete('trp_i17')
cmd.delete('trp_i18')
IDSpec[(('trp_ii','CE2'),('strp','CE2'))] = cmd.select('trp_ii1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.51,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('trp_ii','CE2'),('strp','CZ2'))] = cmd.select('trp_ii2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+12.29,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('trp_ii','CE2'),('strp','NE1'))] = cmd.select('trp_ii3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+12.05,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('trp_ii','CZ2'),('strp','CE2'))] = cmd.select('trp_ii4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.26,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('trp_ii','CZ2'),('strp','CZ2'))] = cmd.select('trp_ii5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.14,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('trp_ii','CZ2'),('strp','NE1'))] = cmd.select('trp_ii6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.67,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('trp_ii','NE1'),('strp','CE2'))] = cmd.select('trp_ii7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.88,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('trp_ii','NE1'),('strp','CZ2'))] = cmd.select('trp_ii8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+12.50,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('trp_ii','NE1'),('strp','NE1'))] = cmd.select('trp_ii9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+12.57,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('trp_ii','CE2'),('strp_i','CE2'))] = cmd.select('trp_ii10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.96,resSelectionSubs('trp_i','CE2',subs,selection=True)))
IDSpec[(('trp_ii','CE2'),('strp_i','CZ2'))] = cmd.select('trp_ii11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.78,resSelectionSubs('trp_i','CZ2',subs,selection=True)))
IDSpec[(('trp_ii','CE2'),('strp_i','NE1'))] = cmd.select('trp_ii12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+14.47,resSelectionSubs('trp_i','NE1',subs,selection=True)))
IDSpec[(('trp_ii','CZ2'),('strp_i','CE2'))] = cmd.select('trp_ii13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.14,resSelectionSubs('trp_i','CE2',subs,selection=True)))
IDSpec[(('trp_ii','CZ2'),('strp_i','CZ2'))] = cmd.select('trp_ii14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.04,resSelectionSubs('trp_i','CZ2',subs,selection=True)))
IDSpec[(('trp_ii','CZ2'),('strp_i','NE1'))] = cmd.select('trp_ii15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.70,resSelectionSubs('trp_i','NE1',subs,selection=True)))
IDSpec[(('trp_ii','NE1'),('strp_i','CE2'))] = cmd.select('trp_ii16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.91,resSelectionSubs('trp_i','CE2',subs,selection=True)))
IDSpec[(('trp_ii','NE1'),('strp_i','CZ2'))] = cmd.select('trp_ii17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.71,resSelectionSubs('trp_i','CZ2',subs,selection=True)))
IDSpec[(('trp_ii','NE1'),('strp_i','NE1'))] = cmd.select('trp_ii18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+15.34,resSelectionSubs('trp_i','NE1',subs,selection=True)))
IDSpec['trp_ii'] = cmd.select('trp_ii',' br. trp_ii1&br. trp_ii2&br. trp_ii3&br. trp_ii4&br. trp_ii5&br. trp_ii6&br. trp_ii7&br. trp_ii8&br. trp_ii9&br. trp_ii10&br. trp_ii11&br. trp_ii12&br. trp_ii13&br. trp_ii14&br. trp_ii15&br. trp_ii16&br. trp_ii17&br. trp_ii18')
IDSpec['r_trp_ii'] = cmd.count_atoms(resSelectionSubs('trp_ii', subs=subs, selection=True))
cmd.delete('trp_ii1')
cmd.delete('trp_ii2')
cmd.delete('trp_ii3')
cmd.delete('trp_ii4')
cmd.delete('trp_ii5')
cmd.delete('trp_ii6')
cmd.delete('trp_ii7')
cmd.delete('trp_ii8')
cmd.delete('trp_ii9')
cmd.delete('trp_ii10')
cmd.delete('trp_ii11')
cmd.delete('trp_ii12')
cmd.delete('trp_ii13')
cmd.delete('trp_ii14')
cmd.delete('trp_ii15')
cmd.delete('trp_ii16')
cmd.delete('trp_ii17')
cmd.delete('trp_ii18')
IDSpec['S_2j08_4_1_99_3'] = cmd.select('S_2j08_4_1_99_3', 'trp|trp_i|trp_ii')
cmd.delete('trp')
cmd.delete('trp_i')
cmd.delete('trp_ii')
