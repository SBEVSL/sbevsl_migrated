'''
FUNC:S_2bn4_1_6_2_4
PDB:2bn4
EC:1.6.2.4
RESI:ser,ser,cys,asp
LOCI:a-442,444,644,689;
'''
IDSpec[(('ser','CA'),('rcys','CA'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.84,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','CA'),('rcys','CB'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.39,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','CA'),('rcys','SG'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.52,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','CB'),('rcys','CA'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+14.15,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','CB'),('rcys','CB'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.77,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','CB'),('rcys','SG'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.82,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','OG'),('rcys','CA'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+15.17,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','OG'),('rcys','CB'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.81,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','OG'),('rcys','SG'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.72,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.72,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.07,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.01,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.44,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.68,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.86,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+14.10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+14.24,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.50,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rser','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.22,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','CA'),('rser','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.26,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','CA'),('rser','OG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.65,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ser','CB'),('rser','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.64,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','CB'),('rser','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.65,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','CB'),('rser','OG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.02,resSelectionSubs('ser','OG',subs)))
IDSpec[(('ser','OG'),('rser','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.79,resSelectionSubs('ser','CA',subs)))
IDSpec[(('ser','OG'),('rser','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.08,resSelectionSubs('ser','CB',subs)))
IDSpec[(('ser','OG'),('rser','OG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.48,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('cys','CA'),('sser','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.84,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sser','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.15,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('sser','OG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+15.17,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys','CB'),('sser','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.39,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sser','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.77,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('sser','OG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.81,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys','SG'),('sser','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.52,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sser','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.82,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('sser','OG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.72,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys','CA'),('rasp','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.51,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CA'),('rasp','OD1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.83,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CA'),('rasp','OD2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.33,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CB'),('rasp','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.95,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CB'),('rasp','OD1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.43,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CB'),('rasp','OD2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.52,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','SG'),('rasp','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.23,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','SG'),('rasp','OD1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.43,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','SG'),('rasp','OD2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CA'),('rser','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.04,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CA'),('rser','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.59,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CA'),('rser','OG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.76,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CB'),('rser','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.90,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CB'),('rser','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.42,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CB'),('rser','OG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.76,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','SG'),('rser','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.35,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','SG'),('rser','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.88,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','SG'),('rser','OG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.12,resSelectionSubs('ser','OG',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18&br. cys19&br. cys20&br. cys21&br. cys22&br. cys23&br. cys24&br. cys25&br. cys26&br. cys27')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
cmd.delete('cys19')
cmd.delete('cys20')
cmd.delete('cys21')
cmd.delete('cys22')
cmd.delete('cys23')
cmd.delete('cys24')
cmd.delete('cys25')
cmd.delete('cys26')
cmd.delete('cys27')
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.72,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.44,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.10,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.07,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.68,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.24,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.01,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.86,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.50,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.51,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','SG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.23,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.83,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.43,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','SG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.43,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.33,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.52,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','SG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.82,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.08,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.30,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.90,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.21,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.94,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.62,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.99,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.17,resSelectionSubs('ser','OG',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
IDSpec[(('ser_i','CA'),('sser','CA'))] = cmd.select('ser_i1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.22,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CB'))] = cmd.select('ser_i2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.64,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','OG'))] = cmd.select('ser_i3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.79,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CA'))] = cmd.select('ser_i4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.26,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CB'))] = cmd.select('ser_i5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.65,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','OG'))] = cmd.select('ser_i6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.08,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CA'))] = cmd.select('ser_i7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.65,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CB'))] = cmd.select('ser_i8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.02,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','OG'))] = cmd.select('ser_i9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.48,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('scys','CA'))] = cmd.select('ser_i10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.04,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('scys','CB'))] = cmd.select('ser_i11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.90,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('scys','SG'))] = cmd.select('ser_i12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.35,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('scys','CA'))] = cmd.select('ser_i13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.59,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('scys','CB'))] = cmd.select('ser_i14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.42,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('scys','SG'))] = cmd.select('ser_i15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.88,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('scys','CA'))] = cmd.select('ser_i16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.76,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('scys','CB'))] = cmd.select('ser_i17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.76,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('scys','SG'))] = cmd.select('ser_i18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.12,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sasp','CG'))] = cmd.select('ser_i19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.08,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sasp','OD1'))] = cmd.select('ser_i20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.90,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sasp','OD2'))] = cmd.select('ser_i21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.62,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sasp','CG'))] = cmd.select('ser_i22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.30,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sasp','OD1'))] = cmd.select('ser_i23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.21,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sasp','OD2'))] = cmd.select('ser_i24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.99,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sasp','CG'))] = cmd.select('ser_i25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sasp','OD1'))] = cmd.select('ser_i26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.94,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sasp','OD2'))] = cmd.select('ser_i27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.17,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_2bn4_1_6_2_4'] = cmd.select('S_2bn4_1_6_2_4', 'ser|cys|asp|ser_i')
cmd.delete('ser')
cmd.delete('cys')
cmd.delete('asp')
cmd.delete('ser_i')
