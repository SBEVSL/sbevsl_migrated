'''
FUNC:S_3ha1_5_1_1_1
PDB:3ha1
EC:5.1.1.1
RESI:arg,tyr,thr
LOCI:a-138,270,316;
'''
IDSpec[(('arg','CZ'),('rthr','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+34.42,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','CZ'),('rthr','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+35.89,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','CZ'),('rthr','OG1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+36.19,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NE'),('rthr','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+34.98,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NE'),('rthr','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+36.45,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NE'),('rthr','OG1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+36.79,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NH1'),('rthr','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+33.11,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NH1'),('rthr','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+34.58,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NH1'),('rthr','OG1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+34.87,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','CZ'),('rtyr','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+39.96,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','CZ'),('rtyr','CZ'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+38.95,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','CZ'),('rtyr','OH'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+39.13,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NE'),('rtyr','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+40.34,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NE'),('rtyr','CZ'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+39.36,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NE'),('rtyr','OH'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+39.53,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NH1'),('rtyr','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+38.67,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NH1'),('rtyr','CZ'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+37.67,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NH1'),('rtyr','OH'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+37.85,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('thr','CA'),('sarg','CZ'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+34.42,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+34.98,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NH1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+33.11,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','CZ'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+35.89,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+36.45,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NH1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+34.58,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','CZ'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+36.19,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+36.79,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NH1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+34.87,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CA'),('rtyr','CE1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.31,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('thr','CA'),('rtyr','CZ'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.22,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('thr','CA'),('rtyr','OH'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.63,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('thr','CB'),('rtyr','CE1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.41,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('thr','CB'),('rtyr','CZ'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.31,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('thr','CB'),('rtyr','OH'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.64,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('thr','OG1'),('rtyr','CE1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.41,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('thr','OG1'),('rtyr','CZ'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.31,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('thr','OG1'),('rtyr','OH'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.46,resSelectionSubs('tyr','OH',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
IDSpec[(('tyr','CE1'),('sarg','CZ'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+39.96,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+40.34,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NH1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+38.67,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','CZ'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+38.95,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+39.36,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NH1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+37.67,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','CZ'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+39.13,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+39.53,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NH1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+37.85,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sthr','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.31,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sthr','CB'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.41,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sthr','OG1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.41,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sthr','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.22,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sthr','CB'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.31,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sthr','OG1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.31,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sthr','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.63,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sthr','CB'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.64,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('tyr','OH'),('sthr','OG1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.46,resSelectionSubs('thr','OG1',subs,selection=True)))
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
IDSpec['S_3ha1_5_1_1_1'] = cmd.select('S_3ha1_5_1_1_1', 'arg|thr|tyr')
cmd.delete('arg')
cmd.delete('thr')
cmd.delete('tyr')