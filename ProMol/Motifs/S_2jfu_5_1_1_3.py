'''
FUNC:S_2jfu_5_1_1_3
PDB:2jfu
EC:5.1.1.3
RESI:asp,ser,cys,cys
LOCI:a-14,15,77,188;
'''
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.54,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.68,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.74,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.30,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.23,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.39,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.83,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.63,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.77,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rcys','CA'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.77,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','CA'),('rcys','CB'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.32,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','CA'),('rcys','SG'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.62,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','CB'),('rcys','CA'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.60,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','CB'),('rcys','CB'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.08,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','CB'),('rcys','SG'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.35,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','OG'),('rcys','CA'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.90,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','OG'),('rcys','CB'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.38,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','OG'),('rcys','SG'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.14,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','CA'),('rcys','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.80,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','CA'),('rcys','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.05,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','CA'),('rcys','SG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+13.79,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','CB'),('rcys','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+14.38,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','CB'),('rcys','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+14.55,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','CB'),('rcys','SG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.34,resSelectionSubs('cys','SG',subs)))
IDSpec[(('ser','OG'),('rcys','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.05,resSelectionSubs('cys','CA',subs)))
IDSpec[(('ser','OG'),('rcys','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.17,resSelectionSubs('cys','CB',subs)))
IDSpec[(('ser','OG'),('rcys','SG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.93,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.54,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.30,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.83,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.68,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.23,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.63,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.74,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.39,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.77,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.54,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.83,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.46,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.48,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.42,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.00,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.42,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.08,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.08,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.93,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.50,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.44,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.79,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.23,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.08,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.08,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.73,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.75,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys','CA'),('sser','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.77,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys','CA'),('sser','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.60,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys','CA'),('sser','OG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.90,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys','CB'),('sser','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.32,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys','CB'),('sser','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.08,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys','CB'),('sser','OG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.38,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys','SG'),('sser','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.62,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys','SG'),('sser','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.35,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys','SG'),('sser','OG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.14,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.54,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.42,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.83,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.42,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.08,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.46,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.08,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CA'),('rcys','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.14,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CA'),('rcys','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.03,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CA'),('rcys','SG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.63,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CB'),('rcys','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.72,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CB'),('rcys','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.40,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CB'),('rcys','SG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.74,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','SG'),('rcys','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.46,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','SG'),('rcys','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.11,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','SG'),('rcys','SG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.42,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys_i','CA'),('sser','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.80,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sser','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.38,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sser','OG'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.05,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sser','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+15.05,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sser','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.55,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sser','OG'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.17,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sser','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.79,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sser','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.34,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sser','OG'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.93,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sasp','CG'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.93,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sasp','OD1'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.79,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sasp','OD2'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.08,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sasp','CG'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.50,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sasp','OD1'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.23,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sasp','OD2'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sasp','CG'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sasp','OD1'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.08,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sasp','OD2'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.75,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.14,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.72,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.46,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.03,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.40,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.11,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.63,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.74,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.42,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18&br. cys_i19&br. cys_i20&br. cys_i21&br. cys_i22&br. cys_i23&br. cys_i24&br. cys_i25&br. cys_i26&br. cys_i27')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
cmd.delete('cys_i19')
cmd.delete('cys_i20')
cmd.delete('cys_i21')
cmd.delete('cys_i22')
cmd.delete('cys_i23')
cmd.delete('cys_i24')
cmd.delete('cys_i25')
cmd.delete('cys_i26')
cmd.delete('cys_i27')
IDSpec['S_2jfu_5_1_1_3'] = cmd.select('S_2jfu_5_1_1_3', 'ser|asp|cys|cys_i')
cmd.delete('ser')
cmd.delete('asp')
cmd.delete('cys')
cmd.delete('cys_i')
