'''
FUNC:S_1dmn_5_3_3_1
PDB:1dmn
EC:5.3.3.1
RESI:tyr,phe,asp,phe,asp
LOCI:a-16,32,40,57,103;
'''
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.38,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.98,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.45,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.41,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.91,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.52,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.21,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.44,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','CG'),('rphe','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.39,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','CG'),('rphe','CE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.17,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','CG'),('rphe','CZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.07,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD1'),('rphe','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.93,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD1'),('rphe','CE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.70,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD1'),('rphe','CZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.56,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD2'),('rphe','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.42,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD2'),('rphe','CE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.16,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD2'),('rphe','CZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.16,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr','CE1'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.60,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','CG'),('rtyr','CZ'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.50,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr','OH'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.20,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD1'),('rtyr','CE1'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.37,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD1'),('rtyr','CZ'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.22,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD1'),('rtyr','OH'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.67,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD2'),('rtyr','CE1'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.40,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD2'),('rtyr','CZ'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.27,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD2'),('rtyr','OH'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.04,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','CG'),('rphe','CD1'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.47,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','CG'),('rphe','CE1'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.22,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','CG'),('rphe','CZ'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.10,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD1'),('rphe','CD1'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.56,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD1'),('rphe','CE1'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.36,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD1'),('rphe','CZ'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.25,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp','OD2'),('rphe','CD1'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.50,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp','OD2'),('rphe','CE1'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.25,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp','OD2'),('rphe','CZ'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.10,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.38,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.41,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.98,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.91,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.21,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.45,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.60,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.44,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rphe','CD1'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.19,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp_i','CG'),('rphe','CE1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.07,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp_i','CG'),('rphe','CZ'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.05,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rphe','CD1'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.37,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp_i','OD1'),('rphe','CE1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.23,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rphe','CZ'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.24,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rphe','CD1'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.34,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp_i','OD2'),('rphe','CE1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.16,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rphe','CZ'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.16,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp_i','CG'),('rtyr','CE1'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.27,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','CG'),('rtyr','CZ'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.27,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','CG'),('rtyr','OH'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.99,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','CE1'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.25,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','CZ'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.17,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','OH'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.90,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','CE1'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.09,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','CZ'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.05,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','OH'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.78,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','CG'),('rphe','CD1'))] = cmd.select('asp_i28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.80,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp_i','CG'),('rphe','CE1'))] = cmd.select('asp_i29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.02,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp_i','CG'),('rphe','CZ'))] = cmd.select('asp_i30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.28,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rphe','CD1'))] = cmd.select('asp_i31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.70,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp_i','OD1'),('rphe','CE1'))] = cmd.select('asp_i32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.01,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rphe','CZ'))] = cmd.select('asp_i33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.22,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rphe','CD1'))] = cmd.select('asp_i34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.09,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('asp_i','OD2'),('rphe','CE1'))] = cmd.select('asp_i35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.22,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rphe','CZ'))] = cmd.select('asp_i36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.35,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('phe','CD1'),('sasp','CG'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.39,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD1'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.93,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp','OD2'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.42,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','CG'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD1'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.70,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp','OD2'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.16,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','CG'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.07,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD1'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.56,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp','OD2'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.16,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp_i','CG'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+13.19,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp_i','OD1'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+14.37,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('phe','CD1'),('sasp_i','OD2'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.34,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp_i','CG'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+12.07,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp_i','OD1'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+13.23,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('phe','CE1'),('sasp_i','OD2'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.16,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp_i','CG'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.05,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp_i','OD1'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.24,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('phe','CZ'),('sasp_i','OD2'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.16,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('phe','CD1'),('rtyr','CE1'))] = cmd.select('phe19', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.20,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('phe','CD1'),('rtyr','CZ'))] = cmd.select('phe20', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.31,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('phe','CD1'),('rtyr','OH'))] = cmd.select('phe21', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.46,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('phe','CE1'),('rtyr','CE1'))] = cmd.select('phe22', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+5.96,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('phe','CE1'),('rtyr','CZ'))] = cmd.select('phe23', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.99,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('phe','CE1'),('rtyr','OH'))] = cmd.select('phe24', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.08,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('phe','CZ'),('rtyr','CE1'))] = cmd.select('phe25', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+5.83,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('phe','CZ'),('rtyr','CZ'))] = cmd.select('phe26', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.60,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('phe','CZ'),('rtyr','OH'))] = cmd.select('phe27', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.54,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('phe','CD1'),('rphe','CD1'))] = cmd.select('phe28', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.56,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('phe','CD1'),('rphe','CE1'))] = cmd.select('phe29', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.79,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('phe','CD1'),('rphe','CZ'))] = cmd.select('phe30', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.48,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('phe','CE1'),('rphe','CD1'))] = cmd.select('phe31', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.87,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('phe','CE1'),('rphe','CE1'))] = cmd.select('phe32', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+5.88,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('phe','CE1'),('rphe','CZ'))] = cmd.select('phe33', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.31,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('phe','CZ'),('rphe','CD1'))] = cmd.select('phe34', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.29,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('phe','CZ'),('rphe','CE1'))] = cmd.select('phe35', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.07,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('phe','CZ'),('rphe','CZ'))] = cmd.select('phe36', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.28,resSelectionSubs('phe','CZ',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18&br. phe19&br. phe20&br. phe21&br. phe22&br. phe23&br. phe24&br. phe25&br. phe26&br. phe27&br. phe28&br. phe29&br. phe30&br. phe31&br. phe32&br. phe33&br. phe34&br. phe35&br. phe36')
IDSpec['r_phe'] = cmd.count_atoms(resSelectionSubs('phe', subs=subs, selection=True))
cmd.delete('phe1')
cmd.delete('phe2')
cmd.delete('phe3')
cmd.delete('phe4')
cmd.delete('phe5')
cmd.delete('phe6')
cmd.delete('phe7')
cmd.delete('phe8')
cmd.delete('phe9')
cmd.delete('phe10')
cmd.delete('phe11')
cmd.delete('phe12')
cmd.delete('phe13')
cmd.delete('phe14')
cmd.delete('phe15')
cmd.delete('phe16')
cmd.delete('phe17')
cmd.delete('phe18')
cmd.delete('phe19')
cmd.delete('phe20')
cmd.delete('phe21')
cmd.delete('phe22')
cmd.delete('phe23')
cmd.delete('phe24')
cmd.delete('phe25')
cmd.delete('phe26')
cmd.delete('phe27')
cmd.delete('phe28')
cmd.delete('phe29')
cmd.delete('phe30')
cmd.delete('phe31')
cmd.delete('phe32')
cmd.delete('phe33')
cmd.delete('phe34')
cmd.delete('phe35')
cmd.delete('phe36')
IDSpec[(('tyr','CE1'),('sasp','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.60,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.37,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.40,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.50,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.22,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.27,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.20,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.67,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.04,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.27,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','OD1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.25,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','OD2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.09,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.27,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','OD1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.17,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','OD2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.05,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.99,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','OD1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.90,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','OD2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.78,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sphe','CD1'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.20,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sphe','CE1'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.96,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sphe','CZ'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.83,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sphe','CD1'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.31,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sphe','CE1'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.99,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sphe','CZ'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.60,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('sphe','CD1'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.46,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sphe','CE1'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.08,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sphe','CZ'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.54,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rphe','CD1'))] = cmd.select('tyr28', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.24,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('tyr','CE1'),('rphe','CE1'))] = cmd.select('tyr29', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.13,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('tyr','CE1'),('rphe','CZ'))] = cmd.select('tyr30', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.34,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('tyr','CZ'),('rphe','CD1'))] = cmd.select('tyr31', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.48,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('tyr','CZ'),('rphe','CE1'))] = cmd.select('tyr32', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.34,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('tyr','CZ'),('rphe','CZ'))] = cmd.select('tyr33', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.26,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('tyr','OH'),('rphe','CD1'))] = cmd.select('tyr34', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.76,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('tyr','OH'),('rphe','CE1'))] = cmd.select('tyr35', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.59,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('tyr','OH'),('rphe','CZ'))] = cmd.select('tyr36', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.38,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('phe_i','CD1'),('sasp','CG'))] = cmd.select('phe_i1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.47,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sasp','OD1'))] = cmd.select('phe_i2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+12.56,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sasp','OD2'))] = cmd.select('phe_i3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.50,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sasp','CG'))] = cmd.select('phe_i4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.22,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sasp','OD1'))] = cmd.select('phe_i5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.36,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sasp','OD2'))] = cmd.select('phe_i6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.25,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sasp','CG'))] = cmd.select('phe_i7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.10,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sasp','OD1'))] = cmd.select('phe_i8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.25,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sasp','OD2'))] = cmd.select('phe_i9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.10,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sasp_i','CG'))] = cmd.select('phe_i10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.80,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sasp_i','OD1'))] = cmd.select('phe_i11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+11.70,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sasp_i','OD2'))] = cmd.select('phe_i12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.09,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sasp_i','CG'))] = cmd.select('phe_i13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.02,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sasp_i','OD1'))] = cmd.select('phe_i14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.01,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sasp_i','OD2'))] = cmd.select('phe_i15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.22,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sasp_i','CG'))] = cmd.select('phe_i16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.28,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sasp_i','OD1'))] = cmd.select('phe_i17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.22,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sasp_i','OD2'))] = cmd.select('phe_i18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.35,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sphe','CD1'))] = cmd.select('phe_i19', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.56,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sphe','CE1'))] = cmd.select('phe_i20', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.87,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sphe','CZ'))] = cmd.select('phe_i21', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.29,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sphe','CD1'))] = cmd.select('phe_i22', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.79,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sphe','CE1'))] = cmd.select('phe_i23', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+5.88,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sphe','CZ'))] = cmd.select('phe_i24', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.07,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sphe','CD1'))] = cmd.select('phe_i25', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.48,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sphe','CE1'))] = cmd.select('phe_i26', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.31,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sphe','CZ'))] = cmd.select('phe_i27', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.28,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('styr','CE1'))] = cmd.select('phe_i28', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.24,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('styr','CZ'))] = cmd.select('phe_i29', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.48,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('styr','OH'))] = cmd.select('phe_i30', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.76,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('styr','CE1'))] = cmd.select('phe_i31', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.13,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('styr','CZ'))] = cmd.select('phe_i32', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.34,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('styr','OH'))] = cmd.select('phe_i33', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.59,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('styr','CE1'))] = cmd.select('phe_i34', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.34,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('styr','CZ'))] = cmd.select('phe_i35', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.26,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('styr','OH'))] = cmd.select('phe_i36', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+5.38,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['phe_i'] = cmd.select('phe_i',' br. phe_i1&br. phe_i2&br. phe_i3&br. phe_i4&br. phe_i5&br. phe_i6&br. phe_i7&br. phe_i8&br. phe_i9&br. phe_i10&br. phe_i11&br. phe_i12&br. phe_i13&br. phe_i14&br. phe_i15&br. phe_i16&br. phe_i17&br. phe_i18&br. phe_i19&br. phe_i20&br. phe_i21&br. phe_i22&br. phe_i23&br. phe_i24&br. phe_i25&br. phe_i26&br. phe_i27&br. phe_i28&br. phe_i29&br. phe_i30&br. phe_i31&br. phe_i32&br. phe_i33&br. phe_i34&br. phe_i35&br. phe_i36')
IDSpec['r_phe_i'] = cmd.count_atoms(resSelectionSubs('phe_i', subs=subs, selection=True))
cmd.delete('phe_i1')
cmd.delete('phe_i2')
cmd.delete('phe_i3')
cmd.delete('phe_i4')
cmd.delete('phe_i5')
cmd.delete('phe_i6')
cmd.delete('phe_i7')
cmd.delete('phe_i8')
cmd.delete('phe_i9')
cmd.delete('phe_i10')
cmd.delete('phe_i11')
cmd.delete('phe_i12')
cmd.delete('phe_i13')
cmd.delete('phe_i14')
cmd.delete('phe_i15')
cmd.delete('phe_i16')
cmd.delete('phe_i17')
cmd.delete('phe_i18')
cmd.delete('phe_i19')
cmd.delete('phe_i20')
cmd.delete('phe_i21')
cmd.delete('phe_i22')
cmd.delete('phe_i23')
cmd.delete('phe_i24')
cmd.delete('phe_i25')
cmd.delete('phe_i26')
cmd.delete('phe_i27')
cmd.delete('phe_i28')
cmd.delete('phe_i29')
cmd.delete('phe_i30')
cmd.delete('phe_i31')
cmd.delete('phe_i32')
cmd.delete('phe_i33')
cmd.delete('phe_i34')
cmd.delete('phe_i35')
cmd.delete('phe_i36')
IDSpec['S_1dmn_5_3_3_1'] = cmd.select('S_1dmn_5_3_3_1', 'asp|asp_i|phe|tyr|phe_i')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('phe')
cmd.delete('tyr')
cmd.delete('phe_i')
