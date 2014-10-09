'''
FUNC:S_1qcx_4_2_2_10
PDB:1qcx
EC:4.2.2.10
RESI:asp,arg,arg
LOCI:a-154,176,236;
'''
IDSpec[(('arg','CZ'),('rarg','CZ'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.30,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg','NE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.92,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','CZ'),('rarg','NH1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.18,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NE'),('rarg','CZ'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.29,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NE'),('rarg','NE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.80,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NE'),('rarg','NH1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.27,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg','CZ'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.06,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg','NE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.73,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NH1'),('rarg','NH1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.00,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.87,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.16,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.78,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.57,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.80,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.57,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.90,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.47,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.30,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.29,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.06,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.92,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.80,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.73,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.18,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.27,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.00,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('rasp','CG'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.19,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg_i','CZ'),('rasp','OD1'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.77,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg_i','CZ'),('rasp','OD2'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.79,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg_i','NE'),('rasp','CG'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.70,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg_i','NE'),('rasp','OD1'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+4.99,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg_i','NE'),('rasp','OD2'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg_i','NH1'),('rasp','CG'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg_i','NH1'),('rasp','OD1'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.01,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg_i','NH1'),('rasp','OD2'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.10,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.87,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.57,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.57,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.16,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.80,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.90,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.78,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.60,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg_i','CZ'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.19,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg_i','NE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.70,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg_i','NH1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.50,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg_i','CZ'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.77,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg_i','NE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.99,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg_i','NH1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.01,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg_i','CZ'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.79,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg_i','NE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.60,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg_i','NH1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.10,resSelectionSubs('arg_i','NH1',subs,selection=True)))
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
IDSpec['S_1qcx_4_2_2_10'] = cmd.select('S_1qcx_4_2_2_10', 'arg|arg_i|asp')
cmd.delete('arg')
cmd.delete('arg_i')
cmd.delete('asp')
