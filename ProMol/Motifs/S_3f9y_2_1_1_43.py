'''
FUNC:S_3f9y_2_1_1_43
PDB:3f9y
EC:2.1.1.43
RESI:tyr,tyr
LOCI:a-245,336;
'''
IDSpec[(('tyr','CE1'),('rtyr_i','CE1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.63,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','CZ'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.94,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','OH'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.97,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','CE1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.33,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','CZ'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.49,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','OH'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.57,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','CE1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.08,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','CZ'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.99,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','OH'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.01,resSelectionSubs('tyr_i','OH',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9')
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
IDSpec[(('tyr_i','CE1'),('styr','CE1'))] = cmd.select('tyr_i1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.63,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','CZ'))] = cmd.select('tyr_i2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.33,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','OH'))] = cmd.select('tyr_i3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.08,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','CE1'))] = cmd.select('tyr_i4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.94,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','CZ'))] = cmd.select('tyr_i5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.49,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','OH'))] = cmd.select('tyr_i6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.99,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','CE1'))] = cmd.select('tyr_i7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.97,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','CZ'))] = cmd.select('tyr_i8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.57,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','OH'))] = cmd.select('tyr_i9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.01,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['tyr_i'] = cmd.select('tyr_i',' br. tyr_i1&br. tyr_i2&br. tyr_i3&br. tyr_i4&br. tyr_i5&br. tyr_i6&br. tyr_i7&br. tyr_i8&br. tyr_i9')
IDSpec['r_tyr_i'] = cmd.count_atoms(resSelectionSubs('tyr_i', subs=subs, selection=True))
cmd.delete('tyr_i1')
cmd.delete('tyr_i2')
cmd.delete('tyr_i3')
cmd.delete('tyr_i4')
cmd.delete('tyr_i5')
cmd.delete('tyr_i6')
cmd.delete('tyr_i7')
cmd.delete('tyr_i8')
cmd.delete('tyr_i9')
IDSpec['S_3f9y_2_1_1_43'] = cmd.select('S_3f9y_2_1_1_43', 'tyr|tyr_i')
cmd.delete('tyr')
cmd.delete('tyr_i')
