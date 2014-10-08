'''
FUNC:S_3bta_3_4_24_69
PDB:3bta
EC:3.4.24.69
RESI:glu,arg,tyr
LOCI:a-261,362,365;
'''
IDSpec[(('arg','CZ'),('rglu','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.35,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','CZ'),('rglu','OE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.36,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','CZ'),('rglu','OE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.51,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NE'),('rglu','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.52,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NE'),('rglu','OE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.56,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NE'),('rglu','OE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.62,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NH1'),('rglu','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.34,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NH1'),('rglu','OE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.31,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NH1'),('rglu','OE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.68,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','CZ'),('rtyr','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.68,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','CZ'),('rtyr','CZ'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.94,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','CZ'),('rtyr','OH'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.69,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NE'),('rtyr','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.90,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NE'),('rtyr','CZ'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.17,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NE'),('rtyr','OH'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.99,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NH1'),('rtyr','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.41,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NH1'),('rtyr','CZ'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.42,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NH1'),('rtyr','OH'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.13,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('glu','CD'),('sarg','CZ'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.35,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.52,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NH1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.34,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','CZ'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.36,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.56,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NH1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.31,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','CZ'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.51,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.62,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NH1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.68,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','CD'),('rtyr','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.03,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','CD'),('rtyr','CZ'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.60,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','CD'),('rtyr','OH'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.40,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE1'),('rtyr','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.07,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE1'),('rtyr','CZ'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.50,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE1'),('rtyr','OH'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.96,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE2'),('rtyr','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.59,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE2'),('rtyr','CZ'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.60,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE2'),('rtyr','OH'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.59,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('sarg','CZ'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.68,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.90,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NH1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.41,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','CZ'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.94,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.17,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NH1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.42,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','CZ'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.69,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.99,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NH1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.13,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.03,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.07,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.59,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.60,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.60,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.40,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.96,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.59,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_3bta_3_4_24_69'] = cmd.select('S_3bta_3_4_24_69', 'arg|glu|tyr')
cmd.delete('arg')
cmd.delete('glu')
cmd.delete('tyr')
