'''
FUNC:S_1za1_2_1_3_2
PDB:1za1
EC:2.1.3.2
RESI:arg,thr,arg,his
LOCI:a-54,55,105,134;
'''
IDSpec[(('arg','CZ'),('rhis','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','CZ'),('rhis','ND1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.88,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','CZ'),('rhis','NE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.79,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NE'),('rhis','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.42,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NE'),('rhis','ND1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.64,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NE'),('rhis','NE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.62,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','NH1'),('rhis','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.82,resSelectionSubs('his','CE1',subs)))
IDSpec[(('arg','NH1'),('rhis','ND1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.96,resSelectionSubs('his','ND1',subs)))
IDSpec[(('arg','NH1'),('rhis','NE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.83,resSelectionSubs('his','NE2',subs)))
IDSpec[(('arg','CZ'),('rarg_i','CZ'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.62,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.40,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NH1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.57,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NE'),('rarg_i','CZ'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.86,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NE'),('rarg_i','NE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.66,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NE'),('rarg_i','NH1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.64,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg_i','CZ'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.52,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.35,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NH1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.53,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','CZ'),('rthr','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.46,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','CZ'),('rthr','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.92,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','CZ'),('rthr','OG1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.16,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NE'),('rthr','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.89,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NE'),('rthr','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.54,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NE'),('rthr','OG1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.85,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NH1'),('rthr','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.13,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NH1'),('rthr','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.34,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NH1'),('rthr','OG1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.46,resSelectionSubs('thr','OG1',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27')
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
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
IDSpec[(('his','CE1'),('sarg','CZ'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.70,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.42,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','CE1'),('sarg','NH1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.82,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','CZ'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.88,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.64,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','ND1'),('sarg','NH1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.96,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','CZ'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.79,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.62,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('his','NE2'),('sarg','NH1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.83,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('his','CE1'),('rarg_i','CZ'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.09,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('his','CE1'),('rarg_i','NE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.05,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('his','CE1'),('rarg_i','NH1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.83,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('his','ND1'),('rarg_i','CZ'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.74,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('his','ND1'),('rarg_i','NE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.63,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('his','ND1'),('rarg_i','NH1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.58,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('his','NE2'),('rarg_i','CZ'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.63,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('his','NE2'),('rarg_i','NE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.78,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('his','NE2'),('rarg_i','NH1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.51,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('his','CE1'),('rthr','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.24,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his','CE1'),('rthr','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.00,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his','CE1'),('rthr','OG1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.37,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('his','ND1'),('rthr','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.52,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his','ND1'),('rthr','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.25,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his','ND1'),('rthr','OG1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.67,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('his','NE2'),('rthr','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.26,resSelectionSubs('thr','CA',subs)))
IDSpec[(('his','NE2'),('rthr','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.00,resSelectionSubs('thr','CB',subs)))
IDSpec[(('his','NE2'),('rthr','OG1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.06,resSelectionSubs('thr','OG1',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27')
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
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.62,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.86,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.52,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.40,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.66,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.35,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.57,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.64,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.53,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('shis','CE1'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.09,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('shis','ND1'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.74,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('shis','NE2'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.63,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg_i','NE'),('shis','CE1'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.05,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('shis','ND1'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.63,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('shis','NE2'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.78,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('shis','CE1'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.83,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('shis','ND1'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.58,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('shis','NE2'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.51,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('rthr','CA'))] = cmd.select('arg_i19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.16,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg_i','CZ'),('rthr','CB'))] = cmd.select('arg_i20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.70,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg_i','CZ'),('rthr','OG1'))] = cmd.select('arg_i21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.42,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg_i','NE'),('rthr','CA'))] = cmd.select('arg_i22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.57,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg_i','NE'),('rthr','CB'))] = cmd.select('arg_i23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.18,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg_i','NE'),('rthr','OG1'))] = cmd.select('arg_i24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.23,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg_i','NH1'),('rthr','CA'))] = cmd.select('arg_i25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.44,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg_i','NH1'),('rthr','CB'))] = cmd.select('arg_i26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.90,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg_i','NH1'),('rthr','OG1'))] = cmd.select('arg_i27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.57,resSelectionSubs('thr','OG1',subs)))
IDSpec['arg_i'] = cmd.select('arg_i',' br. arg_i1&br. arg_i2&br. arg_i3&br. arg_i4&br. arg_i5&br. arg_i6&br. arg_i7&br. arg_i8&br. arg_i9&br. arg_i10&br. arg_i11&br. arg_i12&br. arg_i13&br. arg_i14&br. arg_i15&br. arg_i16&br. arg_i17&br. arg_i18&br. arg_i19&br. arg_i20&br. arg_i21&br. arg_i22&br. arg_i23&br. arg_i24&br. arg_i25&br. arg_i26&br. arg_i27')
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
cmd.delete('arg_i19')
cmd.delete('arg_i20')
cmd.delete('arg_i21')
cmd.delete('arg_i22')
cmd.delete('arg_i23')
cmd.delete('arg_i24')
cmd.delete('arg_i25')
cmd.delete('arg_i26')
cmd.delete('arg_i27')
IDSpec[(('thr','CA'),('sarg','CZ'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.46,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.89,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NH1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.13,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','CZ'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.92,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.54,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NH1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.34,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','CZ'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.16,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.85,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NH1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.46,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis','CE1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.24,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis','ND1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.52,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('thr','CA'),('shis','NE2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.26,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('thr','CB'),('shis','CE1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.00,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('thr','CB'),('shis','ND1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.25,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('thr','CB'),('shis','NE2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.00,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis','CE1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.37,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis','ND1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.67,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('thr','OG1'),('shis','NE2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.06,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg_i','CZ'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.16,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg_i','NE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.57,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg_i','NH1'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.44,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg_i','CZ'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.70,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg_i','NE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.18,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg_i','NH1'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.90,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg_i','CZ'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.42,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg_i','NE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.23,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg_i','NH1'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.57,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27')
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
cmd.delete('thr19')
cmd.delete('thr20')
cmd.delete('thr21')
cmd.delete('thr22')
cmd.delete('thr23')
cmd.delete('thr24')
cmd.delete('thr25')
cmd.delete('thr26')
cmd.delete('thr27')
IDSpec['S_1za1_2_1_3_2'] = cmd.select('S_1za1_2_1_3_2', 'arg|his|arg_i|thr')
cmd.delete('arg')
cmd.delete('his')
cmd.delete('arg_i')
cmd.delete('thr')
