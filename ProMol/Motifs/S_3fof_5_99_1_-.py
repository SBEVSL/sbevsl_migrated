'''
FUNC:S_3fof_5_99_1_-
PDB:3fof
EC:5.99.1.-
RESI:arg,his,tyr
LOCI:a-28,74,118;
'''
IDSpec[(('tyr','CE1'),('rarg','CZ'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+39.64,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CE1'),('rarg','NE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+40.37,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CE1'),('rarg','NH1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+38.91,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CZ'),('rarg','CZ'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+39.12,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CZ'),('rarg','NE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+39.83,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CZ'),('rarg','NH1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+38.43,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','OH'),('rarg','CZ'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+40.02,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','OH'),('rarg','NE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+40.72,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','OH'),('rarg','NH1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+39.36,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CE1'),('rhis','CE1'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+26.43,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CE1'),('rhis','ND1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+26.62,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CE1'),('rhis','NE2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+25.38,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','CZ'),('rhis','CE1'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+25.93,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','CZ'),('rhis','ND1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+26.17,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','CZ'),('rhis','NE2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+24.85,resSelectionSubs('his','NE2',subs)))
IDSpec[(('tyr','OH'),('rhis','CE1'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+26.85,resSelectionSubs('his','CE1',subs)))
IDSpec[(('tyr','OH'),('rhis','ND1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+27.11,resSelectionSubs('his','ND1',subs)))
IDSpec[(('tyr','OH'),('rhis','NE2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+25.73,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('arg','CZ'),('styr','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+39.64,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CZ'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+39.12,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','OH'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+40.02,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+40.37,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CZ'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+39.83,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','OH'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+40.72,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+38.91,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CZ'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+38.43,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','OH'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+39.36,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','CZ'),('rhis','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.35,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','CZ'),('rhis','ND1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.46,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','CZ'),('rhis','NE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.44,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NE'),('rhis','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.21,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NE'),('rhis','ND1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.41,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NE'),('rhis','NE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.27,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NH1'),('rhis','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.69,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NH1'),('rhis','ND1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.76,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NH1'),('rhis','NE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.83,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('styr','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+26.43,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','CZ'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+25.93,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('styr','OH'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+26.85,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+26.62,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','CZ'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+26.17,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('styr','OH'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+27.11,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.38,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','CZ'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+24.85,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('styr','OH'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+25.73,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','CZ'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.35,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.21,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NH1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+14.69,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','CZ'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.46,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+16.41,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NH1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+14.76,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','CZ'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.44,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+17.27,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NH1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.83,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
IDSpec['S_3fof_5_99_1_-'] = cmd.select('S_3fof_5_99_1_-', 'tyr|arg|his')
cmd.delete('tyr')
cmd.delete('arg')
cmd.delete('his')
