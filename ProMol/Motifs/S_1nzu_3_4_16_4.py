'''
FUNC:S_1nzu_3_4_16_4
PDB:1nzu
EC:3.4.16.4
RESI:ser,lys,ser,gln
LOCI:a-44,47,110,148;
'''
IDSpec[(('ser','CA'),('rlys','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.73,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CA'),('rlys','CE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.56,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CA'),('rlys','NZ'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.48,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CB'),('rlys','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.33,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CB'),('rlys','CE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.09,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CB'),('rlys','NZ'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.65,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','OG'),('rlys','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.20,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','OG'),('rlys','CE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.20,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','OG'),('rlys','NZ'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.60,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CA'),('rgln','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.94,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CA'),('rgln','NE2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.92,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CA'),('rgln','OE1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.61,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','CB'),('rgln','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+17.23,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CB'),('rgln','NE2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+17.13,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CB'),('rgln','OE1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+17.93,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','OG'),('rgln','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.32,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','OG'),('rgln','NE2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.27,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','OG'),('rgln','OE1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.97,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','CA'),('rser','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.74,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','CA'),('rser','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.05,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','CA'),('rser','OG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.25,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ser','CB'),('rser','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','CB'),('rser','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.82,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','CB'),('rser','OG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.00,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ser','OG'),('rser','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.94,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','OG'),('rser','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.33,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','OG'),('rser','OG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.44,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('lys','CD'),('sser','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.73,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.33,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','OG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.20,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.56,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.09,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','OG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.20,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.48,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.65,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','OG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.60,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CD'),('rgln','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.84,resSelectionSubs('gln','CD',subs)))
IDSpec[(('lys','CD'),('rgln','NE2'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.70,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('lys','CD'),('rgln','OE1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.76,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('lys','CE'),('rgln','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.21,resSelectionSubs('gln','CD',subs)))
IDSpec[(('lys','CE'),('rgln','NE2'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.96,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('lys','CE'),('rgln','OE1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.16,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('lys','NZ'),('rgln','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.33,resSelectionSubs('gln','CD',subs)))
IDSpec[(('lys','NZ'),('rgln','NE2'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.00,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('lys','NZ'),('rgln','OE1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.28,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.96,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.33,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.16,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.04,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.32,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.08,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.60,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.90,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.74,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('gln','CD'),('sser','CA'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.94,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CB'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+17.23,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','OG'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+18.32,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CA'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+15.92,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CB'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+17.13,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','OG'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+18.27,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CA'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.61,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CB'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.93,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','OG'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+18.97,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','CD'),('slys','CD'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+17.84,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('slys','CE'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+17.21,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gln','CD'),('slys','NZ'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+18.33,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gln','NE2'),('slys','CD'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+17.70,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('slys','CE'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.96,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gln','NE2'),('slys','NZ'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+18.00,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gln','OE1'),('slys','CD'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+18.76,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('slys','CE'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+18.16,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('gln','OE1'),('slys','NZ'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+19.28,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('gln','CD'),('rser','CA'))] = cmd.select('gln19', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+21.45,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gln','CD'),('rser','CB'))] = cmd.select('gln20', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+22.05,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gln','CD'),('rser','OG'))] = cmd.select('gln21', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+22.18,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gln','NE2'),('rser','CA'))] = cmd.select('gln22', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+20.91,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gln','NE2'),('rser','CB'))] = cmd.select('gln23', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+21.42,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gln','NE2'),('rser','OG'))] = cmd.select('gln24', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+21.52,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gln','OE1'),('rser','CA'))] = cmd.select('gln25', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+22.39,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gln','OE1'),('rser','CB'))] = cmd.select('gln26', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+23.01,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gln','OE1'),('rser','OG'))] = cmd.select('gln27', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+23.09,resSelectionSubs('ser','OG',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
cmd.delete('gln19')
cmd.delete('gln20')
cmd.delete('gln21')
cmd.delete('gln22')
cmd.delete('gln23')
cmd.delete('gln24')
cmd.delete('gln25')
cmd.delete('gln26')
cmd.delete('gln27')
IDSpec[(('ser_i','CA'),('sser','CA'))] = cmd.select('ser_i1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.74,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CB'))] = cmd.select('ser_i2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.46,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','OG'))] = cmd.select('ser_i3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.94,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CA'))] = cmd.select('ser_i4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.05,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CB'))] = cmd.select('ser_i5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.82,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','OG'))] = cmd.select('ser_i6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.33,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CA'))] = cmd.select('ser_i7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.25,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CB'))] = cmd.select('ser_i8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.00,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','OG'))] = cmd.select('ser_i9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.44,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CD'))] = cmd.select('ser_i10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.96,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CE'))] = cmd.select('ser_i11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.04,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','NZ'))] = cmd.select('ser_i12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.60,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CD'))] = cmd.select('ser_i13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.33,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CE'))] = cmd.select('ser_i14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.32,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','NZ'))] = cmd.select('ser_i15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.90,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CD'))] = cmd.select('ser_i16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.16,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CE'))] = cmd.select('ser_i17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.08,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','NZ'))] = cmd.select('ser_i18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.74,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sgln','CD'))] = cmd.select('ser_i19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+21.45,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sgln','NE2'))] = cmd.select('ser_i20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+20.91,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sgln','OE1'))] = cmd.select('ser_i21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+22.39,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sgln','CD'))] = cmd.select('ser_i22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+22.05,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sgln','NE2'))] = cmd.select('ser_i23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+21.42,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sgln','OE1'))] = cmd.select('ser_i24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+23.01,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sgln','CD'))] = cmd.select('ser_i25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+22.18,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sgln','NE2'))] = cmd.select('ser_i26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+21.52,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sgln','OE1'))] = cmd.select('ser_i27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+23.09,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_1nzu_3_4_16_4'] = cmd.select('S_1nzu_3_4_16_4', 'ser|lys|gln|ser_i')
cmd.delete('ser')
cmd.delete('lys')
cmd.delete('gln')
cmd.delete('ser_i')
