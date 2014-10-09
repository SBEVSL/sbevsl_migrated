'''
FUNC:S_2ewn_6_3_4_15
PDB:2ewn
EC:6.3.4.15
RESI:arg,lys,arg
LOCI:a-118,183,317;
'''
IDSpec[(('arg','CZ'),('rarg','CZ'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.52,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg','NE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.71,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','CZ'),('rarg','NH1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.13,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NE'),('rarg','CZ'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.92,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NE'),('rarg','NE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.11,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NE'),('rarg','NH1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.56,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg','CZ'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+23.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg','NE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+22.90,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NH1'),('rarg','NH1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+23.24,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','CZ'),('rlys','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.79,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.02,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','CZ'),('rlys','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.63,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NE'),('rlys','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.45,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NE'),('rlys','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.49,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NE'),('rlys','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.08,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NH1'),('rlys','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.56,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NH1'),('rlys','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.95,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NH1'),('rlys','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.64,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.52,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.92,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+23.67,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.71,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.11,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+22.90,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+22.13,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.56,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+23.24,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('rlys','CD'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.97,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg_i','CZ'),('rlys','CE'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+20.98,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg_i','CZ'),('rlys','NZ'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+19.89,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg_i','NE'),('rlys','CD'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+20.95,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg_i','NE'),('rlys','CE'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+19.94,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg_i','NE'),('rlys','NZ'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.90,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg_i','NH1'),('rlys','CD'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.84,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg_i','NH1'),('rlys','CE'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+20.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg_i','NH1'),('rlys','NZ'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.71,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sarg','CZ'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.79,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.45,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NH1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.56,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','CZ'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.02,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.49,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NH1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.95,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','CZ'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.63,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.08,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NH1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.64,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg_i','CZ'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.97,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg_i','NE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+20.95,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg_i','NH1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.84,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg_i','CZ'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+20.98,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg_i','NE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.94,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg_i','NH1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+20.87,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg_i','CZ'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.89,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg_i','NE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.90,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg_i','NH1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.71,resSelectionSubs('arg_i','NH1',subs,selection=True)))
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
IDSpec['S_2ewn_6_3_4_15'] = cmd.select('S_2ewn_6_3_4_15', 'arg|arg_i|lys')
cmd.delete('arg')
cmd.delete('arg_i')
cmd.delete('lys')