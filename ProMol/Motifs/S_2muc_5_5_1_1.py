'''
FUNC:S_2muc_5_5_1_1
PDB:2muc
EC:5.5.1.1
RESI:lys,lys,lys,glu
LOCI:a-167,169,273,327;
'''
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.06,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.11,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.84,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.60,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.62,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.13,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.85,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.89,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.24,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.22,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.54,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.15,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.08,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.53,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.98,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.74,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.35,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.57,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CD'),('rlys_ii','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.14,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','CD'),('rlys_ii','CE'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.82,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','CD'),('rlys_ii','NZ'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.72,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_ii','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.01,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','CE'),('rlys_ii','CE'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.73,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','CE'),('rlys_ii','NZ'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.67,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+13.19,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','CE'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.03,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','NZ'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.93,resSelectionSubs('lys_ii','NZ',subs)))
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
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.06,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.60,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.85,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.11,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.62,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.89,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.84,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.13,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.24,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rglu','CD'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.63,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','CD'),('rglu','OE1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','CD'),('rglu','OE2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.29,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','CE'),('rglu','CD'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.55,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','CE'),('rglu','OE1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.48,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','CE'),('rglu','OE2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.87,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','NZ'),('rglu','CD'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.49,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','NZ'),('rglu','OE1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.65,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','NZ'),('rglu','OE2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.57,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','CD'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.31,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','CE'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.82,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','NZ'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.63,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','CD'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.40,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','CE'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.88,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','NZ'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.50,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','CD'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.97,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','CE'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.46,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','NZ'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.18,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27')
IDSpec['r_lys_i'] = cmd.count_atoms(resSelectionSubs('lys_i', subs=subs, selection=True))
cmd.delete('lys_i1')
cmd.delete('lys_i2')
cmd.delete('lys_i3')
cmd.delete('lys_i4')
cmd.delete('lys_i5')
cmd.delete('lys_i6')
cmd.delete('lys_i7')
cmd.delete('lys_i8')
cmd.delete('lys_i9')
cmd.delete('lys_i10')
cmd.delete('lys_i11')
cmd.delete('lys_i12')
cmd.delete('lys_i13')
cmd.delete('lys_i14')
cmd.delete('lys_i15')
cmd.delete('lys_i16')
cmd.delete('lys_i17')
cmd.delete('lys_i18')
cmd.delete('lys_i19')
cmd.delete('lys_i20')
cmd.delete('lys_i21')
cmd.delete('lys_i22')
cmd.delete('lys_i23')
cmd.delete('lys_i24')
cmd.delete('lys_i25')
cmd.delete('lys_i26')
cmd.delete('lys_i27')
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.22,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.08,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.74,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.54,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.53,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.35,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.15,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.98,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.57,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.63,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','CE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.55,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','NZ'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.49,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.40,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','CE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.48,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','NZ'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+4.65,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.29,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','CE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.87,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','NZ'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.57,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('rlys_ii','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.81,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('glu','CD'),('rlys_ii','CE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.55,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('glu','CD'),('rlys_ii','NZ'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.94,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys_ii','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.75,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('glu','OE1'),('rlys_ii','CE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.39,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('glu','OE1'),('rlys_ii','NZ'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.60,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys_ii','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.61,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('glu','OE2'),('rlys_ii','CE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.32,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('glu','OE2'),('rlys_ii','NZ'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.70,resSelectionSubs('lys_ii','NZ',subs)))
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
IDSpec[(('lys_ii','CD'),('slys','CD'))] = cmd.select('lys_ii1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.14,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','CE'))] = cmd.select('lys_ii2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.01,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','NZ'))] = cmd.select('lys_ii3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.19,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CD'))] = cmd.select('lys_ii4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.82,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CE'))] = cmd.select('lys_ii5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.73,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','NZ'))] = cmd.select('lys_ii6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.03,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CD'))] = cmd.select('lys_ii7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.72,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CE'))] = cmd.select('lys_ii8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.67,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','NZ'))] = cmd.select('lys_ii9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CD'))] = cmd.select('lys_ii10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.31,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CE'))] = cmd.select('lys_ii11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.40,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','NZ'))] = cmd.select('lys_ii12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.97,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CD'))] = cmd.select('lys_ii13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.82,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CE'))] = cmd.select('lys_ii14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.88,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','NZ'))] = cmd.select('lys_ii15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.46,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CD'))] = cmd.select('lys_ii16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.63,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CE'))] = cmd.select('lys_ii17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.50,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','NZ'))] = cmd.select('lys_ii18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.18,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sglu','CD'))] = cmd.select('lys_ii19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.81,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sglu','OE1'))] = cmd.select('lys_ii20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.75,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('sglu','OE2'))] = cmd.select('lys_ii21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.61,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sglu','CD'))] = cmd.select('lys_ii22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.55,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sglu','OE1'))] = cmd.select('lys_ii23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.39,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('sglu','OE2'))] = cmd.select('lys_ii24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.32,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sglu','CD'))] = cmd.select('lys_ii25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.94,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sglu','OE1'))] = cmd.select('lys_ii26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.60,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('sglu','OE2'))] = cmd.select('lys_ii27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.70,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['lys_ii'] = cmd.select('lys_ii',' br. lys_ii1&br. lys_ii2&br. lys_ii3&br. lys_ii4&br. lys_ii5&br. lys_ii6&br. lys_ii7&br. lys_ii8&br. lys_ii9&br. lys_ii10&br. lys_ii11&br. lys_ii12&br. lys_ii13&br. lys_ii14&br. lys_ii15&br. lys_ii16&br. lys_ii17&br. lys_ii18&br. lys_ii19&br. lys_ii20&br. lys_ii21&br. lys_ii22&br. lys_ii23&br. lys_ii24&br. lys_ii25&br. lys_ii26&br. lys_ii27')
IDSpec['r_lys_ii'] = cmd.count_atoms(resSelectionSubs('lys_ii', subs=subs, selection=True))
cmd.delete('lys_ii1')
cmd.delete('lys_ii2')
cmd.delete('lys_ii3')
cmd.delete('lys_ii4')
cmd.delete('lys_ii5')
cmd.delete('lys_ii6')
cmd.delete('lys_ii7')
cmd.delete('lys_ii8')
cmd.delete('lys_ii9')
cmd.delete('lys_ii10')
cmd.delete('lys_ii11')
cmd.delete('lys_ii12')
cmd.delete('lys_ii13')
cmd.delete('lys_ii14')
cmd.delete('lys_ii15')
cmd.delete('lys_ii16')
cmd.delete('lys_ii17')
cmd.delete('lys_ii18')
cmd.delete('lys_ii19')
cmd.delete('lys_ii20')
cmd.delete('lys_ii21')
cmd.delete('lys_ii22')
cmd.delete('lys_ii23')
cmd.delete('lys_ii24')
cmd.delete('lys_ii25')
cmd.delete('lys_ii26')
cmd.delete('lys_ii27')
IDSpec['S_2muc_5_5_1_1'] = cmd.select('S_2muc_5_5_1_1', 'lys|lys_i|glu|lys_ii')
cmd.delete('lys')
cmd.delete('lys_i')
cmd.delete('glu')
cmd.delete('lys_ii')
