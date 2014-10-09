'''
FUNC:S_2bs9_3_2_1_37
PDB:2bs9
EC:3.2.1.37
RESI:arg,trp,glu,glu
LOCI:a-52,153,160,278;
'''
IDSpec[(('glu','CD'),('rglu','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.28,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','CD'),('rglu','OE1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.89,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','CD'),('rglu','OE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.04,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.10,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE1'),('rglu','OE1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.57,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu','OE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.85,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.51,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE2'),('rglu','OE1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.99,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu','OE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.54,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.62,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.89,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.17,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.61,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.91,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.06,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.31,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.53,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.79,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','CD'),('rtrp','CE2'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+25.49,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','CD'),('rtrp','CZ2'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+26.10,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','CD'),('rtrp','NE1'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+25.83,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE1'),('rtrp','CE2'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+26.44,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE1'),('rtrp','CZ2'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+27.00,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE1'),('rtrp','NE1'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+26.81,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE2'),('rtrp','CE2'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+25.30,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE2'),('rtrp','CZ2'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+25.94,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE2'),('rtrp','NE1'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+25.58,resSelectionSubs('trp','NE1',subs)))
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
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.28,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.10,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.51,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.89,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.57,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.99,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.04,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.85,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.54,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('rarg','CZ'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.23,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu_i','CD'),('rarg','NE'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.22,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu_i','CD'),('rarg','NH1'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.26,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu_i','OE1'),('rarg','CZ'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.48,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu_i','OE1'),('rarg','NE'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.47,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu_i','OE1'),('rarg','NH1'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.49,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu_i','OE2'),('rarg','CZ'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.54,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu_i','OE2'),('rarg','NE'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.69,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu_i','OE2'),('rarg','NH1'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.54,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu_i','CD'),('rtrp','CE2'))] = cmd.select('glu_i19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+21.85,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu_i','CD'),('rtrp','CZ2'))] = cmd.select('glu_i20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+22.46,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu_i','CD'),('rtrp','NE1'))] = cmd.select('glu_i21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+22.05,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu_i','OE1'),('rtrp','CE2'))] = cmd.select('glu_i22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.07,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu_i','OE1'),('rtrp','CZ2'))] = cmd.select('glu_i23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.67,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu_i','OE1'),('rtrp','NE1'))] = cmd.select('glu_i24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.26,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu_i','OE2'),('rtrp','CE2'))] = cmd.select('glu_i25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+21.33,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu_i','OE2'),('rtrp','CZ2'))] = cmd.select('glu_i26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+21.91,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu_i','OE2'),('rtrp','NE1'))] = cmd.select('glu_i27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+21.61,resSelectionSubs('trp','NE1',subs)))
IDSpec['glu_i'] = cmd.select('glu_i',' br. glu_i1&br. glu_i2&br. glu_i3&br. glu_i4&br. glu_i5&br. glu_i6&br. glu_i7&br. glu_i8&br. glu_i9&br. glu_i10&br. glu_i11&br. glu_i12&br. glu_i13&br. glu_i14&br. glu_i15&br. glu_i16&br. glu_i17&br. glu_i18&br. glu_i19&br. glu_i20&br. glu_i21&br. glu_i22&br. glu_i23&br. glu_i24&br. glu_i25&br. glu_i26&br. glu_i27')
IDSpec['r_glu_i'] = cmd.count_atoms(resSelectionSubs('glu_i', subs=subs, selection=True))
cmd.delete('glu_i1')
cmd.delete('glu_i2')
cmd.delete('glu_i3')
cmd.delete('glu_i4')
cmd.delete('glu_i5')
cmd.delete('glu_i6')
cmd.delete('glu_i7')
cmd.delete('glu_i8')
cmd.delete('glu_i9')
cmd.delete('glu_i10')
cmd.delete('glu_i11')
cmd.delete('glu_i12')
cmd.delete('glu_i13')
cmd.delete('glu_i14')
cmd.delete('glu_i15')
cmd.delete('glu_i16')
cmd.delete('glu_i17')
cmd.delete('glu_i18')
cmd.delete('glu_i19')
cmd.delete('glu_i20')
cmd.delete('glu_i21')
cmd.delete('glu_i22')
cmd.delete('glu_i23')
cmd.delete('glu_i24')
cmd.delete('glu_i25')
cmd.delete('glu_i26')
cmd.delete('glu_i27')
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.62,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.61,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.31,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.89,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.53,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.17,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.06,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.79,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu_i','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.23,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu_i','OE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.48,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu_i','OE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.54,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu_i','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.22,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu_i','OE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.47,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu_i','OE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.69,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu_i','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.26,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu_i','OE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.49,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu_i','OE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+4.54,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rtrp','CE2'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.03,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('arg','CZ'),('rtrp','CZ2'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.67,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('arg','CZ'),('rtrp','NE1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.31,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('arg','NE'),('rtrp','CE2'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.85,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('arg','NE'),('rtrp','CZ2'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.52,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('arg','NE'),('rtrp','NE1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.08,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('arg','NH1'),('rtrp','CE2'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.79,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('arg','NH1'),('rtrp','CZ2'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.37,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('arg','NH1'),('rtrp','NE1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.08,resSelectionSubs('trp','NE1',subs)))
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
IDSpec[(('trp','CE2'),('sglu','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+25.49,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+26.44,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+25.30,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+26.10,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+27.00,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+25.94,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+25.83,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+26.81,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+25.58,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu_i','CD'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+21.85,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu_i','OE1'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+23.07,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu_i','OE2'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+21.33,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu_i','CD'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+22.46,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu_i','OE1'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+23.67,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu_i','OE2'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+21.91,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu_i','CD'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+22.05,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu_i','OE1'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+23.26,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu_i','OE2'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+21.61,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('trp','CE2'),('sarg','CZ'))] = cmd.select('trp19', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+18.03,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('trp','CE2'),('sarg','NE'))] = cmd.select('trp20', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+16.85,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('trp','CE2'),('sarg','NH1'))] = cmd.select('trp21', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+18.79,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sarg','CZ'))] = cmd.select('trp22', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+18.67,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sarg','NE'))] = cmd.select('trp23', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+17.52,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sarg','NH1'))] = cmd.select('trp24', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+19.37,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sarg','CZ'))] = cmd.select('trp25', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+18.31,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('trp','NE1'),('sarg','NE'))] = cmd.select('trp26', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+17.08,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('trp','NE1'),('sarg','NH1'))] = cmd.select('trp27', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+19.08,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9&br. trp10&br. trp11&br. trp12&br. trp13&br. trp14&br. trp15&br. trp16&br. trp17&br. trp18&br. trp19&br. trp20&br. trp21&br. trp22&br. trp23&br. trp24&br. trp25&br. trp26&br. trp27')
IDSpec['r_trp'] = cmd.count_atoms(resSelectionSubs('trp', subs=subs, selection=True))
cmd.delete('trp1')
cmd.delete('trp2')
cmd.delete('trp3')
cmd.delete('trp4')
cmd.delete('trp5')
cmd.delete('trp6')
cmd.delete('trp7')
cmd.delete('trp8')
cmd.delete('trp9')
cmd.delete('trp10')
cmd.delete('trp11')
cmd.delete('trp12')
cmd.delete('trp13')
cmd.delete('trp14')
cmd.delete('trp15')
cmd.delete('trp16')
cmd.delete('trp17')
cmd.delete('trp18')
cmd.delete('trp19')
cmd.delete('trp20')
cmd.delete('trp21')
cmd.delete('trp22')
cmd.delete('trp23')
cmd.delete('trp24')
cmd.delete('trp25')
cmd.delete('trp26')
cmd.delete('trp27')
IDSpec['S_2bs9_3_2_1_37'] = cmd.select('S_2bs9_3_2_1_37', 'glu|glu_i|arg|trp')
cmd.delete('glu')
cmd.delete('glu_i')
cmd.delete('arg')
cmd.delete('trp')
