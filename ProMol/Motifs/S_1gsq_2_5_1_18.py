'''
FUNC:S_1gsq_2_5_1_18
PDB:1gsq
EC:2.5.1.18
RESI:tyr,arg,lys
LOCI:a-7,13,103;
'''
IDSpec[(('tyr','CE1'),('rlys','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.46,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CE1'),('rlys','CE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.63,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CE1'),('rlys','NZ'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+18.77,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CZ'),('rlys','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.85,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CZ'),('rlys','CE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.03,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CZ'),('rlys','NZ'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.24,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','OH'),('rlys','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.51,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','OH'),('rlys','CE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.72,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','OH'),('rlys','NZ'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+16.97,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CE1'),('rarg','CZ'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CE1'),('rarg','NE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.43,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CE1'),('rarg','NH1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.17,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CZ'),('rarg','CZ'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.15,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CZ'),('rarg','NE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.01,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CZ'),('rarg','NH1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.58,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','OH'),('rarg','CZ'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.06,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','OH'),('rarg','NE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.96,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','OH'),('rarg','NH1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.60,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('lys','CD'),('styr','CE1'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+19.46,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','CZ'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.85,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','OH'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.51,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CE1'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.63,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CZ'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.03,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','OH'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.72,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CE1'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.77,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CZ'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.24,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','OH'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.97,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CD'),('rarg','CZ'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.83,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CD'),('rarg','NE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.76,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CD'),('rarg','NH1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.30,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','CE'),('rarg','CZ'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.58,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CE'),('rarg','NE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.62,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CE'),('rarg','NH1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.88,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','NZ'),('rarg','CZ'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.62,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','NZ'),('rarg','NE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.63,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','NZ'),('rarg','NH1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.94,resSelectionSubs('arg','NH1',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
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
IDSpec[(('arg','CZ'),('styr','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.67,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CZ'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.15,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','OH'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.06,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.43,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CZ'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.01,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','OH'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.96,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.17,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CZ'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.58,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','OH'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.60,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.58,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.76,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.62,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.63,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.30,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.88,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.94,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_1gsq_2_5_1_18'] = cmd.select('S_1gsq_2_5_1_18', 'tyr|lys|arg')
cmd.delete('tyr')
cmd.delete('lys')
cmd.delete('arg')
