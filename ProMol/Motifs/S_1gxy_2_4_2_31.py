'''
FUNC:S_1gxy_2_4_2_31
PDB:1gxy
EC:2.4.2.31
RESI:ser,glu,arg,glu
LOCI:a-147,159,184,189;
'''
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.34,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.89,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.51,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.86,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.19,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.03,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.45,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.10,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.68,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','CD'),('rser','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.97,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','CD'),('rser','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.91,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','CD'),('rser','OG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.62,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE1'),('rser','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.91,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE1'),('rser','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.94,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE1'),('rser','OG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.66,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE2'),('rser','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.84,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE2'),('rser','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.60,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE2'),('rser','OG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.46,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','CD'),('rglu_i','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.07,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE1'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.97,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE2'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.47,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu_i','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.97,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE1'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.79,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE2'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.35,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu_i','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.10,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE1'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.10,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE2'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.40,resSelectionSubs('glu_i','OE2',subs)))
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
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.34,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.86,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.45,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.89,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.19,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.10,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.51,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.03,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.68,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('rser','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.92,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','CZ'),('rser','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.44,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','CZ'),('rser','OG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.70,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NE'),('rser','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.18,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NE'),('rser','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.72,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NE'),('rser','OG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.88,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NH1'),('rser','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.93,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NH1'),('rser','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.48,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NH1'),('rser','OG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.76,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','CZ'),('rglu_i','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.11,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('arg','CZ'),('rglu_i','OE1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.73,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('arg','CZ'),('rglu_i','OE2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.64,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('arg','NE'),('rglu_i','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.43,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('arg','NE'),('rglu_i','OE1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.02,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('arg','NE'),('rglu_i','OE2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.91,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('arg','NH1'),('rglu_i','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.61,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('arg','NH1'),('rglu_i','OE1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+4.95,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('arg','NH1'),('rglu_i','OE2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.48,resSelectionSubs('glu_i','OE2',subs)))
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
IDSpec[(('ser','CA'),('sglu','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.97,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.84,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.91,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.94,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.60,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.62,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.66,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.46,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','CZ'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.92,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.18,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NH1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.93,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','CZ'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.44,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.72,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NH1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.48,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','CZ'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.70,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.88,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NH1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.76,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CA'),('rglu_i','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.29,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('ser','CA'),('rglu_i','OE1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.80,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('ser','CA'),('rglu_i','OE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.68,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('ser','CB'),('rglu_i','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.91,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('ser','CB'),('rglu_i','OE1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.43,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('ser','CB'),('rglu_i','OE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.25,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('ser','OG'),('rglu_i','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.60,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('ser','OG'),('rglu_i','OE1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.96,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('ser','OG'),('rglu_i','OE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.98,resSelectionSubs('glu_i','OE2',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.97,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.10,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.97,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.79,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.10,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.47,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.35,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.40,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sarg','CZ'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.11,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sarg','NE'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.43,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sarg','NH1'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.61,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sarg','CZ'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.73,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sarg','NE'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.02,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sarg','NH1'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+4.95,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sarg','CZ'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.64,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sarg','NE'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.91,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sarg','NH1'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.48,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sser','CA'))] = cmd.select('glu_i19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.29,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sser','CB'))] = cmd.select('glu_i20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.91,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sser','OG'))] = cmd.select('glu_i21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.60,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sser','CA'))] = cmd.select('glu_i22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.80,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sser','CB'))] = cmd.select('glu_i23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.43,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sser','OG'))] = cmd.select('glu_i24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.96,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sser','CA'))] = cmd.select('glu_i25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.68,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sser','CB'))] = cmd.select('glu_i26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.25,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sser','OG'))] = cmd.select('glu_i27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.98,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_1gxy_2_4_2_31'] = cmd.select('S_1gxy_2_4_2_31', 'glu|arg|ser|glu_i')
cmd.delete('glu')
cmd.delete('arg')
cmd.delete('ser')
cmd.delete('glu_i')
