'''
FUNC:S_1seu_5_99_1_2
PDB:1seu
EC:5.99.1.2
RESI:arg,arg,his
LOCI:a-488,590,632;
'''
IDSpec[(('his','CE1'),('rarg','CZ'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.48,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','CE1'),('rarg','NE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.86,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','CE1'),('rarg','NH1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.46,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','ND1'),('rarg','CZ'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.20,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','ND1'),('rarg','NE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.77,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','ND1'),('rarg','NH1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.04,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','NE2'),('rarg','CZ'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.29,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('his','NE2'),('rarg','NE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.74,resSelectionSubs('arg','NE',subs)))
IDSpec[(('his','NE2'),('rarg','NH1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.27,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('his','CE1'),('rarg_i','CZ'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.88,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('his','CE1'),('rarg_i','NE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.01,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('his','CE1'),('rarg_i','NH1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.93,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('his','ND1'),('rarg_i','CZ'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.83,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('his','ND1'),('rarg_i','NE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.01,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('his','ND1'),('rarg_i','NH1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.00,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('his','NE2'),('rarg_i','CZ'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.50,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('his','NE2'),('rarg_i','NE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.70,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('his','NE2'),('rarg_i','NH1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.46,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('arg','CZ'),('shis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.48,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.20,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','CZ'),('shis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.29,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.86,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.77,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NE'),('shis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.74,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.46,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.04,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg','NH1'),('shis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.27,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rarg_i','CZ'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.75,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.66,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NH1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.23,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NE'),('rarg_i','CZ'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.35,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NE'),('rarg_i','NE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.01,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NE'),('rarg_i','NH1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.81,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg_i','CZ'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.53,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.39,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NH1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.25,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('arg_i','CZ'),('shis','CE1'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.88,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('shis','ND1'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.83,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('shis','NE2'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.50,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg_i','NE'),('shis','CE1'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.01,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('shis','ND1'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.01,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('shis','NE2'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.70,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('shis','CE1'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.93,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('shis','ND1'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.00,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('shis','NE2'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.75,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.35,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.53,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.66,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.01,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.39,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.23,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.81,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.25,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['arg_i'] = cmd.select('arg_i',' br. arg_i1&br. arg_i2&br. arg_i3&br. arg_i4&br. arg_i5&br. arg_i6&br. arg_i7&br. arg_i8&br. arg_i9&br. arg_i10&br. arg_i11&br. arg_i12&br. arg_i13&br. arg_i14&br. arg_i15&br. arg_i16&br. arg_i17&br. arg_i18')
IDSpec['r_arg_i'] = cmd.count_atoms(resSelectionSubs('arg_i', subs=subs, selection=True))
cmd.delete('arg_i1')
cmd.delete('arg_i2')
cmd.delete('arg_i3')
cmd.delete('arg_i4')
cmd.delete('arg_i5')
cmd.delete('arg_i6')
cmd.delete('arg_i7')
cmd.delete('arg_i8')
cmd.delete('arg_i9')
cmd.delete('arg_i10')
cmd.delete('arg_i11')
cmd.delete('arg_i12')
cmd.delete('arg_i13')
cmd.delete('arg_i14')
cmd.delete('arg_i15')
cmd.delete('arg_i16')
cmd.delete('arg_i17')
cmd.delete('arg_i18')
IDSpec['S_1seu_5_99_1_2'] = cmd.select('S_1seu_5_99_1_2', 'his|arg|arg_i')
cmd.delete('his')
cmd.delete('arg')
cmd.delete('arg_i')
