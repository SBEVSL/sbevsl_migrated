'''
FUNC:S_3boo_3_4_24_69
PDB:3boo
EC:3.4.24.69
RESI:glu,arg,tyr
LOCI:a-262,363,366;
'''
IDSpec[(('glu','CD'),('rtyr','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.23,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','CD'),('rtyr','CZ'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.77,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','CD'),('rtyr','OH'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.33,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE1'),('rtyr','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.71,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE1'),('rtyr','CZ'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.67,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE1'),('rtyr','OH'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.50,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE2'),('rtyr','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.07,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE2'),('rtyr','CZ'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.55,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE2'),('rtyr','OH'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.75,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.05,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.08,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.03,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.17,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.16,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.31,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.76,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.87,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.66,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('tyr','CE1'),('sglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.23,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.71,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.77,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.67,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.55,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.75,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rarg','CZ'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CE1'),('rarg','NE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.24,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CE1'),('rarg','NH1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.10,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CZ'),('rarg','CZ'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.50,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CZ'),('rarg','NE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.47,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CZ'),('rarg','NH1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.14,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','OH'),('rarg','CZ'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.25,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','OH'),('rarg','NE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.37,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','OH'),('rarg','NH1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.76,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.05,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.17,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.76,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.08,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.16,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.87,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.03,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.31,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.66,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.26,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CZ'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.50,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','OH'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.25,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.24,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CZ'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.47,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','OH'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.37,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.10,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CZ'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.14,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','OH'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.76,resSelectionSubs('tyr','OH',subs,selection=True)))
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
IDSpec['S_3boo_3_4_24_69'] = cmd.select('S_3boo_3_4_24_69', 'glu|tyr|arg')
cmd.delete('glu')
cmd.delete('tyr')
cmd.delete('arg')
