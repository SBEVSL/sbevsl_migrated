'''
FUNC:S_1ghp_3_5_2_6
PDB:1ghp
EC:3.5.2.6
RESI:ser,lys,ser,asp
LOCI:a-70,73,130,166;
'''
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.32,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.18,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.74,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.75,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.66,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.90,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.28,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.25,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.05,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.45,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.46,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.51,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.68,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.46,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.43,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.78,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.91,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.95,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','CG'),('rser_i','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.49,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('asp','CG'),('rser_i','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.83,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('asp','CG'),('rser_i','OG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.88,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('asp','OD1'),('rser_i','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.06,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('asp','OD1'),('rser_i','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.41,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('asp','OD1'),('rser_i','OG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.44,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('asp','OD2'),('rser_i','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.97,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('asp','OD2'),('rser_i','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.35,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('asp','OD2'),('rser_i','OG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.52,resSelectionSubs('ser_i','OG',subs)))
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
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.32,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.75,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.18,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.66,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.25,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.74,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.90,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('rser','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.82,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CD'),('rser','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.35,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CD'),('rser','OG'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.60,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CE'),('rser','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.79,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','CE'),('rser','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.29,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','CE'),('rser','OG'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.59,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','NZ'),('rser','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.98,resSelectionSubs('ser','CA',subs)))
IDSpec[(('lys','NZ'),('rser','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.92,resSelectionSubs('ser','CB',subs)))
IDSpec[(('lys','NZ'),('rser','OG'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.93,resSelectionSubs('ser','OG',subs)))
IDSpec[(('lys','CD'),('rser_i','CA'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.79,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('lys','CD'),('rser_i','CB'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.45,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('lys','CD'),('rser_i','OG'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.30,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('lys','CE'),('rser_i','CA'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.06,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('lys','CE'),('rser_i','CB'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.65,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('lys','CE'),('rser_i','OG'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.05,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('lys','NZ'),('rser_i','CA'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.14,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('lys','NZ'),('rser_i','CB'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.58,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('lys','NZ'),('rser_i','OG'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.71,resSelectionSubs('ser_i','OG',subs)))
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
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.45,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.68,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.46,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.46,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.51,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.43,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.95,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.82,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','CE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.79,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CA'),('slys','NZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.98,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.35,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','CE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.29,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','CB'),('slys','NZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.92,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.60,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','CE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.59,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser','OG'),('slys','NZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser','CA'),('rser_i','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.79,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','CA'),('rser_i','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.63,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','CA'),('rser_i','OG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.18,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','CB'),('rser_i','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.05,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','CB'),('rser_i','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.70,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','CB'),('rser_i','OG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.27,resSelectionSubs('ser_i','OG',subs)))
IDSpec[(('ser','OG'),('rser_i','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.64,resSelectionSubs('ser_i','CA',subs)))
IDSpec[(('ser','OG'),('rser_i','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.31,resSelectionSubs('ser_i','CB',subs)))
IDSpec[(('ser','OG'),('rser_i','OG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.92,resSelectionSubs('ser_i','OG',subs)))
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
IDSpec[(('ser_i','CA'),('sasp','CG'))] = cmd.select('ser_i1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.49,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sasp','OD1'))] = cmd.select('ser_i2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.06,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sasp','OD2'))] = cmd.select('ser_i3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.97,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sasp','CG'))] = cmd.select('ser_i4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.83,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sasp','OD1'))] = cmd.select('ser_i5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.41,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sasp','OD2'))] = cmd.select('ser_i6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.35,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sasp','CG'))] = cmd.select('ser_i7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.88,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sasp','OD1'))] = cmd.select('ser_i8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sasp','OD2'))] = cmd.select('ser_i9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CD'))] = cmd.select('ser_i10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.79,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','CE'))] = cmd.select('ser_i11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.06,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CA'),('slys','NZ'))] = cmd.select('ser_i12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.14,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CD'))] = cmd.select('ser_i13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.45,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','CE'))] = cmd.select('ser_i14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.65,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','CB'),('slys','NZ'))] = cmd.select('ser_i15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.58,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CD'))] = cmd.select('ser_i16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.30,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','CE'))] = cmd.select('ser_i17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.05,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('ser_i','OG'),('slys','NZ'))] = cmd.select('ser_i18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.71,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CA'))] = cmd.select('ser_i19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.79,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','CB'))] = cmd.select('ser_i20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.05,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CA'),('sser','OG'))] = cmd.select('ser_i21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.64,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CA'))] = cmd.select('ser_i22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.63,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','CB'))] = cmd.select('ser_i23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.70,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','CB'),('sser','OG'))] = cmd.select('ser_i24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.31,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CA'))] = cmd.select('ser_i25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.18,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','CB'))] = cmd.select('ser_i26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.27,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ser_i','OG'),('sser','OG'))] = cmd.select('ser_i27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.92,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_1ghp_3_5_2_6'] = cmd.select('S_1ghp_3_5_2_6', 'asp|lys|ser|ser_i')
cmd.delete('asp')
cmd.delete('lys')
cmd.delete('ser')
cmd.delete('ser_i')
