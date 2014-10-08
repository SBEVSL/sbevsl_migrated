'''
FUNC:S_1glv_6_3_2_3
PDB:1glv
EC:6.3.2.3
RESI:lys,arg,arg
LOCI:a-160,210,225;
'''
IDSpec[(('arg','CZ'),('rlys','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.58,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.11,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','CZ'),('rlys','NZ'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.51,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NE'),('rlys','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.89,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NE'),('rlys','CE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.44,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NE'),('rlys','NZ'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.74,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NH1'),('rlys','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.64,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NH1'),('rlys','CE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+17.16,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NH1'),('rlys','NZ'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.60,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','CZ'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.10,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.76,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NH1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.19,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NE'),('rarg_i','CZ'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.41,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NE'),('rarg_i','NE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+4.71,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NE'),('rarg_i','NH1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.52,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg_i','CZ'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.41,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.99,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NH1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.47,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('lys','CD'),('sarg','CZ'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.58,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.89,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NH1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.64,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','CZ'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.11,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+15.44,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NH1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.16,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','CZ'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+15.51,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.74,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NH1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+16.60,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CD'),('rarg_i','CZ'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.84,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('lys','CD'),('rarg_i','NE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.07,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('lys','CD'),('rarg_i','NH1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+15.04,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('lys','CE'),('rarg_i','CZ'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.49,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('lys','CE'),('rarg_i','NE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.70,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('lys','CE'),('rarg_i','NH1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.77,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('lys','NZ'),('rarg_i','CZ'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.65,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('lys','NZ'),('rarg_i','NE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.81,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('lys','NZ'),('rarg_i','NH1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.85,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.10,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.41,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.41,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.76,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+4.71,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.99,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.19,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.52,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('slys','CD'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.84,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('slys','CE'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.49,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('slys','NZ'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.65,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('slys','CD'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg_i','NE'),('slys','CE'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.70,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('slys','NZ'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.81,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('slys','CD'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.04,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('slys','CE'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.77,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('slys','NZ'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.85,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_1glv_6_3_2_3'] = cmd.select('S_1glv_6_3_2_3', 'arg|lys|arg_i')
cmd.delete('arg')
cmd.delete('lys')
cmd.delete('arg_i')
