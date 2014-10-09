'''
FUNC:S_1s5e_2_4_2_36
PDB:1s5e
EC:2.4.2.36
RESI:arg,ser,glu,glu
LOCI:a-7,61,110,112;
'''
IDSpec[(('ser','CA'),('rarg','CZ'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.27,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CA'),('rarg','NE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.81,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CA'),('rarg','NH1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.05,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CB'),('rarg','CZ'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.55,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CB'),('rarg','NE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.33,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CB'),('rarg','NH1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.25,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','OG'),('rarg','CZ'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.47,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','OG'),('rarg','NE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.15,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','OG'),('rarg','NH1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.19,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CA'),('rglu','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.56,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CA'),('rglu','OE1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.64,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CA'),('rglu','OE2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.76,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CB'),('rglu','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.31,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CB'),('rglu','OE1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.38,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CB'),('rglu','OE2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.40,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','OG'),('rglu','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.20,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','OG'),('rglu','OE1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.53,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','OG'),('rglu','OE2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.40,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CA'),('rglu','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.97,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CA'),('rglu','OE1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.43,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CA'),('rglu','OE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.22,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CB'),('rglu','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.76,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CB'),('rglu','OE1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.27,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CB'),('rglu','OE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.01,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','OG'),('rglu','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.58,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','OG'),('rglu','OE1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.11,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','OG'),('rglu','OE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.84,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('arg','CZ'),('sser','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.27,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.55,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','OG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.47,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.81,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.33,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','OG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.15,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.05,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.25,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','OG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.19,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','CZ'),('rglu','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.17,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','CZ'),('rglu','OE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.52,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','CZ'),('rglu','OE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.66,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NE'),('rglu','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.97,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NE'),('rglu','OE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NE'),('rglu','OE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.49,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NH1'),('rglu','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.94,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NH1'),('rglu','OE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.26,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NH1'),('rglu','OE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.49,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','CZ'),('rglu','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.15,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','CZ'),('rglu','OE1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.31,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','CZ'),('rglu','OE2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.34,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NE'),('rglu','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+15.82,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NE'),('rglu','OE1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.91,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NE'),('rglu','OE2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.00,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('arg','NH1'),('rglu','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.19,resSelectionSubs('glu','CD',subs)))
IDSpec[(('arg','NH1'),('rglu','OE1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('arg','NH1'),('rglu','OE2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.41,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('sser','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.56,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.31,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','OG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.20,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.64,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.38,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','OG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.53,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.40,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','OG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.40,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','CZ'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.17,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.97,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','CD'),('sarg','NH1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.94,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','CZ'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.52,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.40,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE1'),('sarg','NH1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.26,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','CZ'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.66,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.49,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu','OE2'),('sarg','NH1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.49,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu','CD'),('rglu','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.97,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','CD'),('rglu','OE1'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.85,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','CD'),('rglu','OE2'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.16,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.79,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE1'),('rglu','OE1'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.83,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu','OE2'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.92,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.51,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE2'),('rglu','OE1'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.24,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu','OE2'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.73,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu_i','CD'),('sser','CA'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.97,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sser','CB'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.76,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sser','OG'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.58,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sser','CA'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.43,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sser','CB'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.27,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sser','OG'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.11,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sser','CA'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.22,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sser','CB'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.01,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sser','OG'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.84,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sarg','CZ'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.15,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sarg','NE'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.82,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sarg','NH1'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.19,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sarg','CZ'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.31,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sarg','NE'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.91,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sarg','NH1'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.40,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sarg','CZ'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.34,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sarg','NE'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.00,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sarg','NH1'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.41,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.97,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.79,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.51,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.85,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.83,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.24,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.16,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.92,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.73,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1s5e_2_4_2_36'] = cmd.select('S_1s5e_2_4_2_36', 'ser|arg|glu|glu_i')
cmd.delete('ser')
cmd.delete('arg')
cmd.delete('glu')
cmd.delete('glu_i')
