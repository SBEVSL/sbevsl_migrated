'''
FUNC:S_1pn0_1_14_13_7
PDB:1pn0
EC:1.14.13.7
RESI:asp,arg,tyr
LOCI:a-54,281,289;
'''
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.44,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.44,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.75,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.59,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.95,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.84,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.92,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.97,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','CG'),('rtyr','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.99,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','CG'),('rtyr','CZ'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.82,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr','OH'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.80,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD1'),('rtyr','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.50,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD1'),('rtyr','CZ'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.30,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD1'),('rtyr','OH'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.18,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD2'),('rtyr','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.50,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD2'),('rtyr','CZ'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.52,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD2'),('rtyr','OH'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.73,resSelectionSubs('tyr','OH',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
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
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.67,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.84,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.59,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.92,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.75,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.95,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+4.97,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rtyr','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.82,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','CZ'),('rtyr','CZ'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.89,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','CZ'),('rtyr','OH'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.26,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NE'),('rtyr','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.03,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NE'),('rtyr','CZ'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.23,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NE'),('rtyr','OH'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.58,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NH1'),('rtyr','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.64,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NH1'),('rtyr','CZ'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.65,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NH1'),('rtyr','OH'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.06,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('sasp','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.99,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.50,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.50,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.30,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.80,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.18,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','CZ'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.82,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.03,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NH1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.64,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','CZ'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.89,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.23,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NH1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.65,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','CZ'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.26,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.58,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NH1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.06,resSelectionSubs('arg','NH1',subs,selection=True)))
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
IDSpec['S_1pn0_1_14_13_7'] = cmd.select('S_1pn0_1_14_13_7', 'asp|arg|tyr')
cmd.delete('asp')
cmd.delete('arg')
cmd.delete('tyr')
