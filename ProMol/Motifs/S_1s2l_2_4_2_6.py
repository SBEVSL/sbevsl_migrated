'''
FUNC:S_1s2l_2_4_2_6
PDB:1s2l
EC:2.4.2.6
RESI:tyr,asp,asp,glu
LOCI:a-11,75,95,101;
'''
IDSpec[(('asp','CG'),('rasp_i','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.17,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.40,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.03,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp_i','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.84,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.16,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.61,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp_i','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.18,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.42,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.01,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','CG'),('rtyr','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.12,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','CG'),('rtyr','CZ'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.87,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','CG'),('rtyr','OH'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.68,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD1'),('rtyr','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.04,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD1'),('rtyr','CZ'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.04,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD1'),('rtyr','OH'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.04,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','OD2'),('rtyr','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.91,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp','OD2'),('rtyr','CZ'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.39,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp','OD2'),('rtyr','OH'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.07,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.69,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.51,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.44,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.53,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.24,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.29,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.38,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.14,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.18,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.84,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.18,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.40,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.16,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.42,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.03,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.61,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.01,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rtyr','CE1'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.13,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','CG'),('rtyr','CZ'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.81,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','CG'),('rtyr','OH'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.12,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','CE1'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.43,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','CZ'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.09,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','OD1'),('rtyr','OH'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.36,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','CE1'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.25,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','CZ'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.98,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asp_i','OD2'),('rtyr','OH'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.24,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asp_i','CG'),('rglu','CD'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.69,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp_i','CG'),('rglu','OE1'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.85,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp_i','CG'),('rglu','OE2'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.23,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp_i','OD1'),('rglu','CD'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.74,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp_i','OD1'),('rglu','OE1'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.00,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp_i','OD1'),('rglu','OE2'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.31,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp_i','OD2'),('rglu','CD'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.13,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp_i','OD2'),('rglu','OE1'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.32,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp_i','OD2'),('rglu','OE2'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.50,resSelectionSubs('glu','OE2',subs)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18&br. asp_i19&br. asp_i20&br. asp_i21&br. asp_i22&br. asp_i23&br. asp_i24&br. asp_i25&br. asp_i26&br. asp_i27')
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
IDSpec[(('tyr','CE1'),('sasp','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.12,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.04,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp','OD2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.87,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.04,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp','OD2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.39,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.68,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.04,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp','OD2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.07,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.13,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','OD1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+13.43,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasp_i','OD2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.25,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.81,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','OD1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.09,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasp_i','OD2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+12.98,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.12,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','OD1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.36,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasp_i','OD2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.24,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rglu','CD'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.29,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE1'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.76,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE2'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.67,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CZ'),('rglu','CD'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.95,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE1'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.38,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE2'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.40,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','OH'),('rglu','CD'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.34,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','OH'),('rglu','OE1'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.96,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','OH'),('rglu','OE2'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.45,resSelectionSubs('glu','OE2',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27')
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
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.53,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.38,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.51,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.14,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.29,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.18,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp_i','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.69,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp_i','OD1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.74,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp_i','OD2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.13,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp_i','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.85,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp_i','OD1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.00,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp_i','OD2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.32,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp_i','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.23,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp_i','OD1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.31,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp_i','OD2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.50,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CE1'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.29,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CZ'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.95,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','OH'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.34,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CE1'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.76,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CZ'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.38,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','OH'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.96,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CE1'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.67,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CZ'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.40,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','OH'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.45,resSelectionSubs('tyr','OH',subs,selection=True)))
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
IDSpec['S_1s2l_2_4_2_6'] = cmd.select('S_1s2l_2_4_2_6', 'asp|asp_i|tyr|glu')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('tyr')
cmd.delete('glu')
