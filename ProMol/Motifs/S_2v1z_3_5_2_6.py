'''
FUNC:S_2v1z_3_5_2_6
PDB:2v1z
EC:3.5.2.6
RESI:ser,lys,ser,glu
LOCI:a-50,53,110,146;
'''
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.49,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.09,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.35,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.81,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.25,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.47,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.89,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.16,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.49,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CD'),('rser_i','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.22,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('lys','CD'),('rser_i','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.88,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('lys','CD'),('rser_i','OG'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.89,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('lys','CE'),('rser_i','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.17,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('lys','CE'),('rser_i','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.84,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('lys','CE'),('rser_i','OG'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.33,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('lys','NZ'),('rser_i','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.41,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('lys','NZ'),('rser_i','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.62,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('lys','NZ'),('rser_i','OG'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.74,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.71,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.71,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.67,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.23,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.23,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.26,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.28,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.02,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.48,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('ser','CA'),('slys','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.49,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.81,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','NZ'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.89,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.09,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.25,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','NZ'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.16,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.35,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.47,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','NZ'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.49,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CA'),('rser_i','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.51,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','CA'),('rser_i','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.15,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','CA'),('rser_i','OG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.89,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','CB'),('rser_i','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.03,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','CB'),('rser_i','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.53,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','CB'),('rser_i','OG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.30,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','OG'),('rser_i','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.63,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','OG'),('rser_i','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.13,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','OG'),('rser_i','OG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.02,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','CA'),('rglu','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.07,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CA'),('rglu','OE1'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.62,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CA'),('rglu','OE2'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.33,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CB'),('rglu','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.08,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CB'),('rglu','OE1'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.46,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CB'),('rglu','OE2'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.32,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','OG'),('rglu','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.27,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','OG'),('rglu','OE1'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.66,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','OG'),('rglu','OE2'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.38,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('ser_i','CA'),('slys','CD'))] = cmd.select('ser_i1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.22,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CE'))] = cmd.select('ser_i2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.17,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','NZ'))] = cmd.select('ser_i3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.41,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CD'))] = cmd.select('ser_i4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.88,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CE'))] = cmd.select('ser_i5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.84,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','NZ'))] = cmd.select('ser_i6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CD'))] = cmd.select('ser_i7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.89,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CE'))] = cmd.select('ser_i8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.33,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','NZ'))] = cmd.select('ser_i9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.74,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CA'))] = cmd.select('ser_i10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.51,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CB'))] = cmd.select('ser_i11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.03,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','OG'))] = cmd.select('ser_i12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.63,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CA'))] = cmd.select('ser_i13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.15,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CB'))] = cmd.select('ser_i14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.53,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','OG'))] = cmd.select('ser_i15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.13,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CA'))] = cmd.select('ser_i16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.89,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CB'))] = cmd.select('ser_i17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.30,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','OG'))] = cmd.select('ser_i18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.02,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('rglu','CD'))] = cmd.select('ser_i19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser_i','CA'),('rglu','OE1'))] = cmd.select('ser_i20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser_i','CA'),('rglu','OE2'))] = cmd.select('ser_i21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.69,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser_i','CB'),('rglu','CD'))] = cmd.select('ser_i22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.03,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser_i','CB'),('rglu','OE1'))] = cmd.select('ser_i23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.45,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser_i','CB'),('rglu','OE2'))] = cmd.select('ser_i24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.88,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser_i','OG'),('rglu','CD'))] = cmd.select('ser_i25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.94,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser_i','OG'),('rglu','OE1'))] = cmd.select('ser_i26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.27,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser_i','OG'),('rglu','OE2'))] = cmd.select('ser_i27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.91,resSelectionSubs('glu','OE2',subs)))
IDSpec['ser_i'] = cmd.select('ser_i',' br. ser_i1&br. ser_i2&br. ser_i3&br. ser_i4&br. ser_i5&br. ser_i6&br. ser_i7&br. ser_i8&br. ser_i9&br. ser_i10&br. ser_i11&br. ser_i12&br. ser_i13&br. ser_i14&br. ser_i15&br. ser_i16&br. ser_i17&br. ser_i18&br. ser_i19&br. ser_i20&br. ser_i21&br. ser_i22&br. ser_i23&br. ser_i24&br. ser_i25&br. ser_i26&br. ser_i27')
IDSpec['r_ser_i'] = cmd.count_atoms(resSelectionSubs('ser_i', subs=subs, selection=True))
cmd.delete('ser_i1')
cmd.delete('ser_i2')
cmd.delete('ser_i3')
cmd.delete('ser_i4')
cmd.delete('ser_i5')
cmd.delete('ser_i6')
cmd.delete('ser_i7')
cmd.delete('ser_i8')
cmd.delete('ser_i9')
cmd.delete('ser_i10')
cmd.delete('ser_i11')
cmd.delete('ser_i12')
cmd.delete('ser_i13')
cmd.delete('ser_i14')
cmd.delete('ser_i15')
cmd.delete('ser_i16')
cmd.delete('ser_i17')
cmd.delete('ser_i18')
cmd.delete('ser_i19')
cmd.delete('ser_i20')
cmd.delete('ser_i21')
cmd.delete('ser_i22')
cmd.delete('ser_i23')
cmd.delete('ser_i24')
cmd.delete('ser_i25')
cmd.delete('ser_i26')
cmd.delete('ser_i27')
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.71,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.23,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.28,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.71,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.23,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.02,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.67,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.26,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.48,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.07,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.08,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','OG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.27,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.62,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.46,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','OG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.66,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.33,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.32,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','OG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.38,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','CD'),('sser_i','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.92,resSelectionSubs('ser_i','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sser_i','CB'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.03,resSelectionSubs('ser_i','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sser_i','OG'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.94,resSelectionSubs('ser_i','OG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser_i','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.40,resSelectionSubs('ser_i','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser_i','CB'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.45,resSelectionSubs('ser_i','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser_i','OG'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.27,resSelectionSubs('ser_i','OG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser_i','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.69,resSelectionSubs('ser_i','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser_i','CB'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.88,resSelectionSubs('ser_i','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser_i','OG'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.91,resSelectionSubs('ser_i','OG',subs,selection=True)))
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
IDSpec['S_2v1z_3_5_2_6'] = cmd.select('S_2v1z_3_5_2_6', 'lys|ser|ser_i|glu')
cmd.delete('lys')
cmd.delete('ser')
cmd.delete('ser_i')
cmd.delete('glu')
