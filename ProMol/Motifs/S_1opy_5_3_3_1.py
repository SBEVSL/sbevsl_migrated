'''
FUNC:S_1opy_5_3_3_1
PDB:1opy
EC:5.3.3.1
RESI:tyr,tyr,asp,tyr,asp
LOCI:a-16,32,40,57,103;
'''
IDSpec[(('asp','CG'),('rasp_i','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.55,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.16,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.76,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp_i','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.69,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.17,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.02,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp_i','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.59,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.33,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.63,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','CG'),('rtyr','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.75,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','CG'),('rtyr','CZ'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.17,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr','OH'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.89,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD1'),('rtyr','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.35,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD1'),('rtyr','CZ'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.78,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD1'),('rtyr','OH'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.46,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD2'),('rtyr','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.00,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD2'),('rtyr','CZ'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.28,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD2'),('rtyr','OH'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.01,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','CG'),('rtyr_i','CE1'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.57,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('asp','CG'),('rtyr_i','CZ'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.44,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr_i','OH'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.16,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('asp','OD1'),('rtyr_i','CE1'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.42,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('asp','OD1'),('rtyr_i','CZ'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.23,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('asp','OD1'),('rtyr_i','OH'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.72,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('asp','OD2'),('rtyr_i','CE1'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.35,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('asp','OD2'),('rtyr_i','CZ'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.19,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('asp','OD2'),('rtyr_i','OH'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.96,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('asp','CG'),('rtyr_ii','CE1'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.35,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('asp','CG'),('rtyr_ii','CZ'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.12,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr_ii','OH'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.91,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('asp','OD1'),('rtyr_ii','CE1'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.57,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('asp','OD1'),('rtyr_ii','CZ'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.41,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('asp','OD1'),('rtyr_ii','OH'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.28,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('asp','OD2'),('rtyr_ii','CE1'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.28,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('asp','OD2'),('rtyr_ii','CZ'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.07,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('asp','OD2'),('rtyr_ii','OH'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.87,resSelectionSubs('tyr_ii','OH',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.55,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.69,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.59,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.16,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.17,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.33,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.02,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.63,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rtyr','CE1'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.63,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','CG'),('rtyr','CZ'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.08,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','CG'),('rtyr','OH'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.89,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','CE1'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.87,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','CZ'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.32,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','OH'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.11,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','CE1'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.02,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','CZ'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.34,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','OH'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.10,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','CG'),('rtyr_i','CE1'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.30,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('asp_i','CG'),('rtyr_i','CZ'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.34,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('asp_i','CG'),('rtyr_i','OH'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.07,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('asp_i','OD1'),('rtyr_i','CE1'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.33,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rtyr_i','CZ'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.29,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rtyr_i','OH'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.02,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('asp_i','OD2'),('rtyr_i','CE1'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.16,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rtyr_i','CZ'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.15,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rtyr_i','OH'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.88,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('asp_i','CG'),('rtyr_ii','CE1'))] = cmd.select('asp_i28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.40,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('asp_i','CG'),('rtyr_ii','CZ'))] = cmd.select('asp_i29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.30,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('asp_i','CG'),('rtyr_ii','OH'))] = cmd.select('asp_i30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.83,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('asp_i','OD1'),('rtyr_ii','CE1'))] = cmd.select('asp_i31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.33,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rtyr_ii','CZ'))] = cmd.select('asp_i32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.36,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rtyr_ii','OH'))] = cmd.select('asp_i33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.95,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('asp_i','OD2'),('rtyr_ii','CE1'))] = cmd.select('asp_i34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.39,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rtyr_ii','CZ'))] = cmd.select('asp_i35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.35,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rtyr_ii','OH'))] = cmd.select('asp_i36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.85,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18&br. asp_i19&br. asp_i20&br. asp_i21&br. asp_i22&br. asp_i23&br. asp_i24&br. asp_i25&br. asp_i26&br. asp_i27&br. asp_i28&br. asp_i29&br. asp_i30&br. asp_i31&br. asp_i32&br. asp_i33&br. asp_i34&br. asp_i35&br. asp_i36')
IDSpec['r_asp_i'] = cmd.count_atoms(resSelectionSubs('asp_i', subs=subs, selection=True))
cmd.delete('asp_i1')
cmd.delete('asp_i2')
cmd.delete('asp_i3')
cmd.delete('asp_i4')
cmd.delete('asp_i5')
cmd.delete('asp_i6')
cmd.delete('asp_i7')
cmd.delete('asp_i8')
cmd.delete('asp_i9')
cmd.delete('asp_i10')
cmd.delete('asp_i11')
cmd.delete('asp_i12')
cmd.delete('asp_i13')
cmd.delete('asp_i14')
cmd.delete('asp_i15')
cmd.delete('asp_i16')
cmd.delete('asp_i17')
cmd.delete('asp_i18')
cmd.delete('asp_i19')
cmd.delete('asp_i20')
cmd.delete('asp_i21')
cmd.delete('asp_i22')
cmd.delete('asp_i23')
cmd.delete('asp_i24')
cmd.delete('asp_i25')
cmd.delete('asp_i26')
cmd.delete('asp_i27')
cmd.delete('asp_i28')
cmd.delete('asp_i29')
cmd.delete('asp_i30')
cmd.delete('asp_i31')
cmd.delete('asp_i32')
cmd.delete('asp_i33')
cmd.delete('asp_i34')
cmd.delete('asp_i35')
cmd.delete('asp_i36')
IDSpec[(('tyr','CE1'),('sasp','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.75,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.35,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.78,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.89,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.46,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.01,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.63,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','OD1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.87,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','OD2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.02,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.08,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','OD1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.32,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','OD2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.34,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.89,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','OD1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.11,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','OD2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.10,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rtyr_i','CE1'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.81,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','CZ'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.49,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','CE1'),('rtyr_i','OH'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.45,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','CE1'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.58,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','CZ'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.29,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','CZ'),('rtyr_i','OH'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.23,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','CE1'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.99,resSelectionSubs('tyr_i','CE1',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','CZ'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.38,resSelectionSubs('tyr_i','CZ',subs)))
IDSpec[(('tyr','OH'),('rtyr_i','OH'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.14,resSelectionSubs('tyr_i','OH',subs)))
IDSpec[(('tyr','CE1'),('rtyr_ii','CE1'))] = cmd.select('tyr28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.00,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('tyr','CE1'),('rtyr_ii','CZ'))] = cmd.select('tyr29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.65,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('tyr','CE1'),('rtyr_ii','OH'))] = cmd.select('tyr30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.90,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('tyr','CZ'),('rtyr_ii','CE1'))] = cmd.select('tyr31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.71,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('tyr','CZ'),('rtyr_ii','CZ'))] = cmd.select('tyr32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.41,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('tyr','CZ'),('rtyr_ii','OH'))] = cmd.select('tyr33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.65,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('tyr','OH'),('rtyr_ii','CE1'))] = cmd.select('tyr34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.08,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('tyr','OH'),('rtyr_ii','CZ'))] = cmd.select('tyr35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.84,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('tyr','OH'),('rtyr_ii','OH'))] = cmd.select('tyr36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.77,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27&br. tyr28&br. tyr29&br. tyr30&br. tyr31&br. tyr32&br. tyr33&br. tyr34&br. tyr35&br. tyr36')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
cmd.delete('tyr28')
cmd.delete('tyr29')
cmd.delete('tyr30')
cmd.delete('tyr31')
cmd.delete('tyr32')
cmd.delete('tyr33')
cmd.delete('tyr34')
cmd.delete('tyr35')
cmd.delete('tyr36')
IDSpec[(('tyr_i','CE1'),('sasp','CG'))] = cmd.select('tyr_i1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sasp','OD1'))] = cmd.select('tyr_i2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.42,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sasp','OD2'))] = cmd.select('tyr_i3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.35,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sasp','CG'))] = cmd.select('tyr_i4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sasp','OD1'))] = cmd.select('tyr_i5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.23,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sasp','OD2'))] = cmd.select('tyr_i6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.19,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sasp','CG'))] = cmd.select('tyr_i7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.16,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sasp','OD1'))] = cmd.select('tyr_i8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sasp','OD2'))] = cmd.select('tyr_i9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.96,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sasp_i','CG'))] = cmd.select('tyr_i10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.30,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sasp_i','OD1'))] = cmd.select('tyr_i11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.33,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('sasp_i','OD2'))] = cmd.select('tyr_i12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.16,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sasp_i','CG'))] = cmd.select('tyr_i13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.34,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sasp_i','OD1'))] = cmd.select('tyr_i14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.29,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('sasp_i','OD2'))] = cmd.select('tyr_i15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.15,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sasp_i','CG'))] = cmd.select('tyr_i16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.07,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sasp_i','OD1'))] = cmd.select('tyr_i17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.02,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('sasp_i','OD2'))] = cmd.select('tyr_i18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.88,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','CE1'))] = cmd.select('tyr_i19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.81,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','CZ'))] = cmd.select('tyr_i20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.58,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('styr','OH'))] = cmd.select('tyr_i21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.99,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','CE1'))] = cmd.select('tyr_i22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.49,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','CZ'))] = cmd.select('tyr_i23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.29,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','CZ'),('styr','OH'))] = cmd.select('tyr_i24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.38,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','CE1'))] = cmd.select('tyr_i25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.45,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','CZ'))] = cmd.select('tyr_i26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.23,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_i','OH'),('styr','OH'))] = cmd.select('tyr_i27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.14,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_i','CE1'),('rtyr_ii','CE1'))] = cmd.select('tyr_i28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.61,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('tyr_i','CE1'),('rtyr_ii','CZ'))] = cmd.select('tyr_i29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.30,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('tyr_i','CE1'),('rtyr_ii','OH'))] = cmd.select('tyr_i30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.52,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('tyr_i','CZ'),('rtyr_ii','CE1'))] = cmd.select('tyr_i31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.51,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('tyr_i','CZ'),('rtyr_ii','CZ'))] = cmd.select('tyr_i32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.40,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('tyr_i','CZ'),('rtyr_ii','OH'))] = cmd.select('tyr_i33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.50,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec[(('tyr_i','OH'),('rtyr_ii','CE1'))] = cmd.select('tyr_i34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.63,resSelectionSubs('tyr_ii','CE1',subs)))
IDSpec[(('tyr_i','OH'),('rtyr_ii','CZ'))] = cmd.select('tyr_i35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.57,resSelectionSubs('tyr_ii','CZ',subs)))
IDSpec[(('tyr_i','OH'),('rtyr_ii','OH'))] = cmd.select('tyr_i36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.66,resSelectionSubs('tyr_ii','OH',subs)))
IDSpec['tyr_i'] = cmd.select('tyr_i',' br. tyr_i1&br. tyr_i2&br. tyr_i3&br. tyr_i4&br. tyr_i5&br. tyr_i6&br. tyr_i7&br. tyr_i8&br. tyr_i9&br. tyr_i10&br. tyr_i11&br. tyr_i12&br. tyr_i13&br. tyr_i14&br. tyr_i15&br. tyr_i16&br. tyr_i17&br. tyr_i18&br. tyr_i19&br. tyr_i20&br. tyr_i21&br. tyr_i22&br. tyr_i23&br. tyr_i24&br. tyr_i25&br. tyr_i26&br. tyr_i27&br. tyr_i28&br. tyr_i29&br. tyr_i30&br. tyr_i31&br. tyr_i32&br. tyr_i33&br. tyr_i34&br. tyr_i35&br. tyr_i36')
IDSpec['r_tyr_i'] = cmd.count_atoms(resSelectionSubs('tyr_i', subs=subs, selection=True))
cmd.delete('tyr_i1')
cmd.delete('tyr_i2')
cmd.delete('tyr_i3')
cmd.delete('tyr_i4')
cmd.delete('tyr_i5')
cmd.delete('tyr_i6')
cmd.delete('tyr_i7')
cmd.delete('tyr_i8')
cmd.delete('tyr_i9')
cmd.delete('tyr_i10')
cmd.delete('tyr_i11')
cmd.delete('tyr_i12')
cmd.delete('tyr_i13')
cmd.delete('tyr_i14')
cmd.delete('tyr_i15')
cmd.delete('tyr_i16')
cmd.delete('tyr_i17')
cmd.delete('tyr_i18')
cmd.delete('tyr_i19')
cmd.delete('tyr_i20')
cmd.delete('tyr_i21')
cmd.delete('tyr_i22')
cmd.delete('tyr_i23')
cmd.delete('tyr_i24')
cmd.delete('tyr_i25')
cmd.delete('tyr_i26')
cmd.delete('tyr_i27')
cmd.delete('tyr_i28')
cmd.delete('tyr_i29')
cmd.delete('tyr_i30')
cmd.delete('tyr_i31')
cmd.delete('tyr_i32')
cmd.delete('tyr_i33')
cmd.delete('tyr_i34')
cmd.delete('tyr_i35')
cmd.delete('tyr_i36')
IDSpec[(('tyr_ii','CE1'),('sasp','CG'))] = cmd.select('tyr_ii1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.35,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('sasp','OD1'))] = cmd.select('tyr_ii2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('sasp','OD2'))] = cmd.select('tyr_ii3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('sasp','CG'))] = cmd.select('tyr_ii4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.12,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('sasp','OD1'))] = cmd.select('tyr_ii5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.41,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('sasp','OD2'))] = cmd.select('tyr_ii6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.07,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('sasp','CG'))] = cmd.select('tyr_ii7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.91,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('sasp','OD1'))] = cmd.select('tyr_ii8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('sasp','OD2'))] = cmd.select('tyr_ii9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('sasp_i','CG'))] = cmd.select('tyr_ii10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.40,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('sasp_i','OD1'))] = cmd.select('tyr_ii11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.33,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('sasp_i','OD2'))] = cmd.select('tyr_ii12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.39,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('sasp_i','CG'))] = cmd.select('tyr_ii13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.30,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('sasp_i','OD1'))] = cmd.select('tyr_ii14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.36,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('sasp_i','OD2'))] = cmd.select('tyr_ii15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.35,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('sasp_i','CG'))] = cmd.select('tyr_ii16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.83,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('sasp_i','OD1'))] = cmd.select('tyr_ii17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.95,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('sasp_i','OD2'))] = cmd.select('tyr_ii18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.85,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('styr','CE1'))] = cmd.select('tyr_ii19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.00,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('styr','CZ'))] = cmd.select('tyr_ii20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.71,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('styr','OH'))] = cmd.select('tyr_ii21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.08,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('styr','CE1'))] = cmd.select('tyr_ii22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.65,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('styr','CZ'))] = cmd.select('tyr_ii23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.41,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('styr','OH'))] = cmd.select('tyr_ii24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.84,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('styr','CE1'))] = cmd.select('tyr_ii25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.90,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('styr','CZ'))] = cmd.select('tyr_ii26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.65,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('styr','OH'))] = cmd.select('tyr_ii27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.77,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('styr_i','CE1'))] = cmd.select('tyr_ii28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.61,resSelectionSubs('tyr_i','CE1',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('styr_i','CZ'))] = cmd.select('tyr_ii29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.51,resSelectionSubs('tyr_i','CZ',subs,selection=True)))
IDSpec[(('tyr_ii','CE1'),('styr_i','OH'))] = cmd.select('tyr_ii30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.63,resSelectionSubs('tyr_i','OH',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('styr_i','CE1'))] = cmd.select('tyr_ii31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.30,resSelectionSubs('tyr_i','CE1',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('styr_i','CZ'))] = cmd.select('tyr_ii32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.40,resSelectionSubs('tyr_i','CZ',subs,selection=True)))
IDSpec[(('tyr_ii','CZ'),('styr_i','OH'))] = cmd.select('tyr_ii33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.57,resSelectionSubs('tyr_i','OH',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('styr_i','CE1'))] = cmd.select('tyr_ii34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.52,resSelectionSubs('tyr_i','CE1',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('styr_i','CZ'))] = cmd.select('tyr_ii35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.50,resSelectionSubs('tyr_i','CZ',subs,selection=True)))
IDSpec[(('tyr_ii','OH'),('styr_i','OH'))] = cmd.select('tyr_ii36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.66,resSelectionSubs('tyr_i','OH',subs,selection=True)))
IDSpec['tyr_ii'] = cmd.select('tyr_ii',' br. tyr_ii1&br. tyr_ii2&br. tyr_ii3&br. tyr_ii4&br. tyr_ii5&br. tyr_ii6&br. tyr_ii7&br. tyr_ii8&br. tyr_ii9&br. tyr_ii10&br. tyr_ii11&br. tyr_ii12&br. tyr_ii13&br. tyr_ii14&br. tyr_ii15&br. tyr_ii16&br. tyr_ii17&br. tyr_ii18&br. tyr_ii19&br. tyr_ii20&br. tyr_ii21&br. tyr_ii22&br. tyr_ii23&br. tyr_ii24&br. tyr_ii25&br. tyr_ii26&br. tyr_ii27&br. tyr_ii28&br. tyr_ii29&br. tyr_ii30&br. tyr_ii31&br. tyr_ii32&br. tyr_ii33&br. tyr_ii34&br. tyr_ii35&br. tyr_ii36')
IDSpec['r_tyr_ii'] = cmd.count_atoms(resSelectionSubs('tyr_ii', subs=subs, selection=True))
cmd.delete('tyr_ii1')
cmd.delete('tyr_ii2')
cmd.delete('tyr_ii3')
cmd.delete('tyr_ii4')
cmd.delete('tyr_ii5')
cmd.delete('tyr_ii6')
cmd.delete('tyr_ii7')
cmd.delete('tyr_ii8')
cmd.delete('tyr_ii9')
cmd.delete('tyr_ii10')
cmd.delete('tyr_ii11')
cmd.delete('tyr_ii12')
cmd.delete('tyr_ii13')
cmd.delete('tyr_ii14')
cmd.delete('tyr_ii15')
cmd.delete('tyr_ii16')
cmd.delete('tyr_ii17')
cmd.delete('tyr_ii18')
cmd.delete('tyr_ii19')
cmd.delete('tyr_ii20')
cmd.delete('tyr_ii21')
cmd.delete('tyr_ii22')
cmd.delete('tyr_ii23')
cmd.delete('tyr_ii24')
cmd.delete('tyr_ii25')
cmd.delete('tyr_ii26')
cmd.delete('tyr_ii27')
cmd.delete('tyr_ii28')
cmd.delete('tyr_ii29')
cmd.delete('tyr_ii30')
cmd.delete('tyr_ii31')
cmd.delete('tyr_ii32')
cmd.delete('tyr_ii33')
cmd.delete('tyr_ii34')
cmd.delete('tyr_ii35')
cmd.delete('tyr_ii36')
IDSpec['S_1opy_5_3_3_1'] = cmd.select('S_1opy_5_3_3_1', 'asp|asp_i|tyr|tyr_i|tyr_ii')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('tyr')
cmd.delete('tyr_i')
cmd.delete('tyr_ii')
