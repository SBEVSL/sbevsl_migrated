'''
FUNC:S_1u0b_6_1_1_16
PDB:1u0b
EC:6.1.1.16
RESI:asp,his,his,lys,lys
LOCI:b-34,37,40,266,269;
'''
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CD'),('rhis','CE1'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','CD'),('rhis','ND1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','CD'),('rhis','NE2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','CE'),('rhis','CE1'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','CE'),('rhis','ND1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','CE'),('rhis','NE2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','NZ'),('rhis','CE1'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','NZ'),('rhis','ND1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','NZ'),('rhis','NE2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','CD'),('rhis_i','CE1'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('lys','CD'),('rhis_i','ND1'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('lys','CD'),('rhis_i','NE2'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('lys','CE'),('rhis_i','CE1'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('lys','CE'),('rhis_i','ND1'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('lys','CE'),('rhis_i','NE2'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('lys','NZ'),('rhis_i','CE1'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('lys','NZ'),('rhis_i','ND1'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('lys','NZ'),('rhis_i','NE2'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his_i','NE2',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27&br. lys28&br. lys29&br. lys30&br. lys31&br. lys32&br. lys33&br. lys34&br. lys35&br. lys36')
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
cmd.delete('lys28')
cmd.delete('lys29')
cmd.delete('lys30')
cmd.delete('lys31')
cmd.delete('lys32')
cmd.delete('lys33')
cmd.delete('lys34')
cmd.delete('lys35')
cmd.delete('lys36')
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rasp','CG'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys_i','CD'),('rasp','OD1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys_i','CD'),('rasp','OD2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys_i','CE'),('rasp','CG'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys_i','CE'),('rasp','OD1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys_i','CE'),('rasp','OD2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys_i','NZ'),('rasp','CG'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys_i','NZ'),('rasp','OD1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys_i','NZ'),('rasp','OD2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys_i','CD'),('rhis','CE1'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys_i','CD'),('rhis','ND1'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys_i','CD'),('rhis','NE2'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys_i','CE'),('rhis','CE1'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys_i','CE'),('rhis','ND1'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys_i','CE'),('rhis','NE2'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys_i','NZ'),('rhis','CE1'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys_i','NZ'),('rhis','ND1'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys_i','NZ'),('rhis','NE2'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys_i','CD'),('rhis_i','CE1'))] = cmd.select('lys_i28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('lys_i','CD'),('rhis_i','ND1'))] = cmd.select('lys_i29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('lys_i','CD'),('rhis_i','NE2'))] = cmd.select('lys_i30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('lys_i','CE'),('rhis_i','CE1'))] = cmd.select('lys_i31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('lys_i','CE'),('rhis_i','ND1'))] = cmd.select('lys_i32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('lys_i','CE'),('rhis_i','NE2'))] = cmd.select('lys_i33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('lys_i','NZ'),('rhis_i','CE1'))] = cmd.select('lys_i34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('lys_i','NZ'),('rhis_i','ND1'))] = cmd.select('lys_i35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('lys_i','NZ'),('rhis_i','NE2'))] = cmd.select('lys_i36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10,resSelectionSubs('his_i','NE2',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27&br. lys_i28&br. lys_i29&br. lys_i30&br. lys_i31&br. lys_i32&br. lys_i33&br. lys_i34&br. lys_i35&br. lys_i36')
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
cmd.delete('lys_i28')
cmd.delete('lys_i29')
cmd.delete('lys_i30')
cmd.delete('lys_i31')
cmd.delete('lys_i32')
cmd.delete('lys_i33')
cmd.delete('lys_i34')
cmd.delete('lys_i35')
cmd.delete('lys_i36')
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('slys_i','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys_i','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys_i','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys_i','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys_i','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys_i','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys_i','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys_i','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys_i','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.39,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.24,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.17,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.56,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.36,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.32,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.84,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.69,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','CG'),('rhis_i','CE1'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.86,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('asp','CG'),('rhis_i','ND1'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.97,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('asp','CG'),('rhis_i','NE2'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.00,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis_i','CE1'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.01,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis_i','ND1'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.06,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis_i','NE2'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.12,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis_i','CE1'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.93,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis_i','ND1'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.98,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis_i','NE2'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.07,resSelectionSubs('his_i','NE2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36')
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
cmd.delete('asp28')
cmd.delete('asp29')
cmd.delete('asp30')
cmd.delete('asp31')
cmd.delete('asp32')
cmd.delete('asp33')
cmd.delete('asp34')
cmd.delete('asp35')
cmd.delete('asp36')
IDSpec[(('his','CE1'),('slys','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','CE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.07,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','NZ'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.07,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','CE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','NZ'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','CE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','NZ'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','CE1'),('slys_i','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.07,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('slys_i','CE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.07,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his','CE1'),('slys_i','NZ'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.07,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his','ND1'),('slys_i','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('slys_i','CE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his','ND1'),('slys_i','NZ'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.07,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his','NE2'),('slys_i','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('slys_i','CE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his','NE2'),('slys_i','NZ'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.39,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.56,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.84,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.24,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.36,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.69,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.32,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.60,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('rhis_i','CE1'))] = cmd.select('his28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.43,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','CE1'),('rhis_i','ND1'))] = cmd.select('his29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.09,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','CE1'),('rhis_i','NE2'))] = cmd.select('his30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.64,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('his','ND1'),('rhis_i','CE1'))] = cmd.select('his31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.03,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','ND1'),('rhis_i','ND1'))] = cmd.select('his32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.63,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','ND1'),('rhis_i','NE2'))] = cmd.select('his33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.84,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('his','NE2'),('rhis_i','CE1'))] = cmd.select('his34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.08,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','NE2'),('rhis_i','ND1'))] = cmd.select('his35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.34,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','NE2'),('rhis_i','NE2'))] = cmd.select('his36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('his_i','NE2',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
IDSpec[(('his_i','CE1'),('slys','CD'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.59,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his_i','CE1'),('slys','CE'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.59,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his_i','CE1'),('slys','NZ'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.59,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his_i','ND1'),('slys','CD'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.59,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his_i','ND1'),('slys','CE'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.59,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his_i','ND1'),('slys','NZ'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.59,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his_i','NE2'),('slys','CD'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his_i','NE2'),('slys','CE'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his_i','NE2'),('slys','NZ'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his_i','CE1'),('slys_i','CD'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.59,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his_i','CE1'),('slys_i','CE'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.59,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his_i','CE1'),('slys_i','NZ'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.59,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his_i','ND1'),('slys_i','CD'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.59,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his_i','ND1'),('slys_i','CE'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.59,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his_i','ND1'),('slys_i','NZ'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.59,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his_i','NE2'),('slys_i','CD'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his_i','NE2'),('slys_i','CE'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his_i','NE2'),('slys_i','NZ'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sasp','CG'))] = cmd.select('his_i19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.86,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sasp','OD1'))] = cmd.select('his_i20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.01,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sasp','OD2'))] = cmd.select('his_i21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.93,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sasp','CG'))] = cmd.select('his_i22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sasp','OD1'))] = cmd.select('his_i23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.06,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sasp','OD2'))] = cmd.select('his_i24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.98,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sasp','CG'))] = cmd.select('his_i25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sasp','OD1'))] = cmd.select('his_i26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+13.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sasp','OD2'))] = cmd.select('his_i27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.07,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.43,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.03,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.08,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.09,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.63,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.34,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.64,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.59,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['his_i'] = cmd.select('his_i',' br. his_i1&br. his_i2&br. his_i3&br. his_i4&br. his_i5&br. his_i6&br. his_i7&br. his_i8&br. his_i9&br. his_i10&br. his_i11&br. his_i12&br. his_i13&br. his_i14&br. his_i15&br. his_i16&br. his_i17&br. his_i18&br. his_i19&br. his_i20&br. his_i21&br. his_i22&br. his_i23&br. his_i24&br. his_i25&br. his_i26&br. his_i27&br. his_i28&br. his_i29&br. his_i30&br. his_i31&br. his_i32&br. his_i33&br. his_i34&br. his_i35&br. his_i36')
IDSpec['r_his_i'] = cmd.count_atoms(resSelectionSubs('his_i', subs=subs, selection=True))
cmd.delete('his_i1')
cmd.delete('his_i2')
cmd.delete('his_i3')
cmd.delete('his_i4')
cmd.delete('his_i5')
cmd.delete('his_i6')
cmd.delete('his_i7')
cmd.delete('his_i8')
cmd.delete('his_i9')
cmd.delete('his_i10')
cmd.delete('his_i11')
cmd.delete('his_i12')
cmd.delete('his_i13')
cmd.delete('his_i14')
cmd.delete('his_i15')
cmd.delete('his_i16')
cmd.delete('his_i17')
cmd.delete('his_i18')
cmd.delete('his_i19')
cmd.delete('his_i20')
cmd.delete('his_i21')
cmd.delete('his_i22')
cmd.delete('his_i23')
cmd.delete('his_i24')
cmd.delete('his_i25')
cmd.delete('his_i26')
cmd.delete('his_i27')
cmd.delete('his_i28')
cmd.delete('his_i29')
cmd.delete('his_i30')
cmd.delete('his_i31')
cmd.delete('his_i32')
cmd.delete('his_i33')
cmd.delete('his_i34')
cmd.delete('his_i35')
cmd.delete('his_i36')
IDSpec['S_1u0b_6_1_1_16'] = cmd.select('S_1u0b_6_1_1_16', 'lys|lys_i|asp|his|his_i')
cmd.delete('lys')
cmd.delete('lys_i')
cmd.delete('asp')
cmd.delete('his')
cmd.delete('his_i')
