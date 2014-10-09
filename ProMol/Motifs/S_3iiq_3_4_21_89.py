'''
FUNC:S_3iiq_3_4_21_89
PDB:3iiq
EC:3.4.21.89
RESI:ser,ser,lys
LOCI:a-88,90,145;
'''
IDSpec[(('ser','CA'),('rlys','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.83,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CA'),('rlys','CE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.35,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CA'),('rlys','NZ'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.14,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CB'),('rlys','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.72,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CB'),('rlys','CE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.01,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CB'),('rlys','NZ'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.67,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','OG'),('rlys','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.49,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','OG'),('rlys','CE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.97,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','OG'),('rlys','NZ'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.22,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CA'),('rser','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.76,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','CA'),('rser','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.29,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','CA'),('rser','OG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.15,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ser','CB'),('rser','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.90,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','CB'),('rser','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.09,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','CB'),('rser','OG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.81,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ser','OG'),('rser','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.73,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','OG'),('rser','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.03,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','OG'),('rser','OG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.58,resSelectionSubs('ser','OG',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
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
IDSpec[(('lys','CD'),('sser','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.83,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.72,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','OG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.49,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.35,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.01,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','OG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.97,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.14,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.67,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','OG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.22,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.12,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.18,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.81,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.26,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.17,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.89,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.26,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.19,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.89,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser_i','CA'),('sser','CA'))] = cmd.select('ser_i1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.76,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CB'))] = cmd.select('ser_i2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.90,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','OG'))] = cmd.select('ser_i3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.73,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CA'))] = cmd.select('ser_i4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.29,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CB'))] = cmd.select('ser_i5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.09,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','OG'))] = cmd.select('ser_i6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.03,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CA'))] = cmd.select('ser_i7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.15,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CB'))] = cmd.select('ser_i8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.81,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','OG'))] = cmd.select('ser_i9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.58,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CD'))] = cmd.select('ser_i10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.12,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CE'))] = cmd.select('ser_i11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.26,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','NZ'))] = cmd.select('ser_i12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.26,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CD'))] = cmd.select('ser_i13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.18,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CE'))] = cmd.select('ser_i14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.17,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','NZ'))] = cmd.select('ser_i15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.19,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CD'))] = cmd.select('ser_i16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.81,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CE'))] = cmd.select('ser_i17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.89,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','NZ'))] = cmd.select('ser_i18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.89,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['ser_i'] = cmd.select('ser_i',' br. ser_i1&br. ser_i2&br. ser_i3&br. ser_i4&br. ser_i5&br. ser_i6&br. ser_i7&br. ser_i8&br. ser_i9&br. ser_i10&br. ser_i11&br. ser_i12&br. ser_i13&br. ser_i14&br. ser_i15&br. ser_i16&br. ser_i17&br. ser_i18')
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
IDSpec['S_3iiq_3_4_21_89'] = cmd.select('S_3iiq_3_4_21_89', 'ser|lys|ser_i')
cmd.delete('ser')
cmd.delete('lys')
cmd.delete('ser_i')
