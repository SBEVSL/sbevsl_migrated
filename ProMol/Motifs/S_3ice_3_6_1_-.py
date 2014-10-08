'''
FUNC:S_3ice_3_6_1_-
PDB:3ice
EC:3.6.1.-
RESI:lys,glu,arg,arg
LOCI:a-184,211,212,366;
'''
IDSpec[(('arg','CZ'),('rarg_i','CZ'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+31.01,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+31.98,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NH1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+29.89,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NE'),('rarg_i','CZ'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+31.53,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NE'),('rarg_i','NE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+32.46,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NE'),('rarg_i','NH1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+30.42,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg_i','CZ'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+29.77,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+30.74,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NH1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+28.64,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','CZ'),('rglu','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.48,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','CZ'),('rglu','OE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.93,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','CZ'),('rglu','OE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.34,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NE'),('rglu','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+28.04,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NE'),('rglu','OE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+28.54,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NE'),('rglu','OE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+27.90,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NH1'),('rglu','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.18,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NH1'),('rglu','OE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.63,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NH1'),('rglu','OE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+26.06,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','CZ'),('rlys','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.32,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','CZ'),('rlys','CE'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.36,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','CZ'),('rlys','NZ'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.97,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NE'),('rlys','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.80,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NE'),('rlys','CE'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+22.88,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NE'),('rlys','NZ'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+23.56,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg','NH1'),('rlys','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+20.11,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg','NH1'),('rlys','CE'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.16,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg','NH1'),('rlys','NZ'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.75,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+31.01,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+31.53,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+29.77,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+31.98,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+32.46,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+30.74,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+29.89,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+30.42,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+28.64,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('rglu','CD'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.60,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg_i','CZ'),('rglu','OE1'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.04,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg_i','CZ'),('rglu','OE2'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.75,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg_i','NE'),('rglu','CD'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.24,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg_i','NE'),('rglu','OE1'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.70,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg_i','NE'),('rglu','OE2'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.54,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg_i','NH1'),('rglu','CD'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.35,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg_i','NH1'),('rglu','OE1'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.89,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg_i','NH1'),('rglu','OE2'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.45,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg_i','CZ'),('rlys','CD'))] = cmd.select('arg_i19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.82,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg_i','CZ'),('rlys','CE'))] = cmd.select('arg_i20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.92,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg_i','CZ'),('rlys','NZ'))] = cmd.select('arg_i21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.21,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg_i','NE'),('rlys','CD'))] = cmd.select('arg_i22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.77,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg_i','NE'),('rlys','CE'))] = cmd.select('arg_i23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.96,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg_i','NE'),('rlys','NZ'))] = cmd.select('arg_i24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.33,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('arg_i','NH1'),('rlys','CD'))] = cmd.select('arg_i25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.82,resSelectionSubs('lys','CD',subs)))
IDSpec[(('arg_i','NH1'),('rlys','CE'))] = cmd.select('arg_i26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.02,resSelectionSubs('lys','CE',subs)))
IDSpec[(('arg_i','NH1'),('rlys','NZ'))] = cmd.select('arg_i27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.24,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('glu','CD'),('sarg','CZ'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+27.48,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+28.04,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NH1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+26.18,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','CZ'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+27.93,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+28.54,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NH1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+26.63,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','CZ'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+27.34,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+27.90,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NH1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+26.06,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg_i','CZ'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.60,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg_i','NE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.24,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg_i','NH1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.35,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg_i','CZ'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.04,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg_i','NE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.70,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg_i','NH1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.89,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg_i','CZ'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.75,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg_i','NE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.54,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg_i','NH1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.45,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.88,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.64,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.56,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.73,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.42,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.22,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.15,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.75,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.71,resSelectionSubs('lys','NZ',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27')
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
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
IDSpec[(('lys','CD'),('sarg','CZ'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.32,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.80,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg','NH1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+20.11,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','CZ'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+22.36,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+22.88,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg','NH1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.16,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','CZ'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+22.97,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.56,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg','NH1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+21.75,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg_i','CZ'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.82,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg_i','NE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.77,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('lys','CD'),('sarg_i','NH1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.82,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg_i','CZ'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.92,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg_i','NE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.96,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('lys','CE'),('sarg_i','NH1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.02,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg_i','CZ'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.21,resSelectionSubs('arg_i','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg_i','NE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.33,resSelectionSubs('arg_i','NE',subs,selection=True)))
IDSpec[(('lys','NZ'),('sarg_i','NH1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.24,resSelectionSubs('arg_i','NH1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.88,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.73,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.15,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.64,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.42,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.75,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.56,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.22,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.71,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
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
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
IDSpec['S_3ice_3_6_1_-'] = cmd.select('S_3ice_3_6_1_-', 'arg|arg_i|glu|lys')
cmd.delete('arg')
cmd.delete('arg_i')
cmd.delete('glu')
cmd.delete('lys')
