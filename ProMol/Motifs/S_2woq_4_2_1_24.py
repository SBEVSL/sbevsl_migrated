'''
FUNC:S_2woq_4_2_1_24
PDB:2woq
EC:4.2.1.24
RESI:asp,ser,lys,lys
LOCI:a-127,175,205,260;
'''
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.61,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.49,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.08,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.42,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.29,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.87,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.58,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.69,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.78,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rlys','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.79,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CA'),('rlys','CE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.27,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CA'),('rlys','NZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.32,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CB'),('rlys','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.15,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CB'),('rlys','CE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.40,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CB'),('rlys','NZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.28,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','OG'),('rlys','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.10,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','OG'),('rlys','CE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.08,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','OG'),('rlys','NZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.79,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CA'),('rlys','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.99,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CA'),('rlys','CE'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.52,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CA'),('rlys','NZ'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.63,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CB'),('rlys','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.08,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CB'),('rlys','CE'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.29,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CB'),('rlys','NZ'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.12,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','OG'),('rlys','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.90,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','OG'),('rlys','CE'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.82,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','OG'),('rlys','NZ'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.46,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.61,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.42,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.58,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.49,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.29,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.69,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.08,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.87,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.78,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.04,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.76,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.36,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.14,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.02,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.67,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.28,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.82,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.36,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.05,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.76,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.29,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.07,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.92,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.50,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.13,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.65,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.15,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sser','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.79,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.15,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','OG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.10,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.27,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.40,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','OG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.08,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.32,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.28,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','OG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.79,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.04,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.02,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.82,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.67,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.36,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.94,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.96,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.22,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.45,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.91,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.97,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.37,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.67,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.17,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys_i','CD'),('sser','CA'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.99,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sser','CB'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.08,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sser','OG'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.90,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sser','CA'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.52,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sser','CB'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.29,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sser','OG'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.82,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sser','CA'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.63,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sser','CB'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.12,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sser','OG'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.46,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','CG'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.05,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.07,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.13,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','CG'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.92,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.65,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','CG'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.29,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.50,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.15,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.94,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.45,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.37,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.96,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.91,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.67,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.22,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.97,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.17,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2woq_4_2_1_24'] = cmd.select('S_2woq_4_2_1_24', 'ser|asp|lys|lys_i')
cmd.delete('ser')
cmd.delete('asp')
cmd.delete('lys')
cmd.delete('lys_i')