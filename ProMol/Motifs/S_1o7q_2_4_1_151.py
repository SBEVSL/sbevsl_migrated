'''
FUNC:S_1o7q_2_4_1_151
PDB:1o7q
EC:2.4.1.151
RESI:trp,glu,arg
LOCI:a-314,317,365;
'''
IDSpec[(('glu','CD'),('rtrp','CE2'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.78,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','CD'),('rtrp','CZ2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.69,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','CD'),('rtrp','NE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.89,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE1'),('rtrp','CE2'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.70,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE1'),('rtrp','CZ2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.59,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE1'),('rtrp','NE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.78,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE2'),('rtrp','CE2'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.55,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE2'),('rtrp','CZ2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.31,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE2'),('rtrp','NE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.82,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.64,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.75,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.85,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.44,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.62,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.52,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.37,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.42,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.70,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('trp','CE2'),('sglu','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.78,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.70,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.55,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.69,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.59,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.31,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.89,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.78,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.82,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CE2'),('rarg','CZ'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.82,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('trp','CE2'),('rarg','NE'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.15,resSelectionSubs('arg','NE',subs)))
IDSpec[(('trp','CE2'),('rarg','NH1'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.23,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('trp','CZ2'),('rarg','CZ'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+11.34,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('trp','CZ2'),('rarg','NE'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.67,resSelectionSubs('arg','NE',subs)))
IDSpec[(('trp','CZ2'),('rarg','NH1'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.66,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('trp','NE1'),('rarg','CZ'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+13.13,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('trp','NE1'),('rarg','NE'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.45,resSelectionSubs('arg','NE',subs)))
IDSpec[(('trp','NE1'),('rarg','NH1'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+12.55,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.64,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.44,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.37,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.75,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.62,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.42,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.85,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.52,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.70,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('strp','CE2'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.82,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('strp','CZ2'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.34,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('arg','CZ'),('strp','NE1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.13,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('arg','NE'),('strp','CE2'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.15,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('arg','NE'),('strp','CZ2'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.67,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('arg','NE'),('strp','NE1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.45,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('strp','CE2'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.23,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('strp','CZ2'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.66,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('arg','NH1'),('strp','NE1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.55,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18')
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
IDSpec['S_1o7q_2_4_1_151'] = cmd.select('S_1o7q_2_4_1_151', 'glu|trp|arg')
cmd.delete('glu')
cmd.delete('trp')
cmd.delete('arg')
