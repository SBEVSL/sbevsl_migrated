'''
FUNC:S_1hgx_2_4_2_8
PDB:1hgx
EC:2.4.2.8
RESI:glu,asp,asp,lys,lys
LOCI:a-102,103,106,134,138;
'''
IDSpec[(('glu','CD'),('rasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.30,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','CD'),('rasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.38,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','CD'),('rasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE1'),('rasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE1'),('rasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+4.84,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE1'),('rasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.17,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE2'),('rasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.12,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE2'),('rasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.09,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE2'),('rasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.77,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','CD'),('rasp','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.73,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','CD'),('rasp','OD1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.64,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','CD'),('rasp','OD2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.07,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE1'),('rasp','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.36,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE1'),('rasp','OD1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.32,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE1'),('rasp','OD2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE2'),('rasp','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.39,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE2'),('rasp','OD1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.32,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE2'),('rasp','OD2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.72,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.39,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.64,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.04,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.83,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.96,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.29,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.43,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.75,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.07,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.07,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.07,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.07,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.07,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.07,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.07,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.07,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.07,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.07,resSelectionSubs('lys','NZ',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36')
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
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
IDSpec[(('asp','CG'),('sglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.30,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.12,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.38,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.84,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.09,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.10,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.17,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.77,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.67,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.67,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.69,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.80,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.80,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.89,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.12,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.18,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.01,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.28,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.13,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.35,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.72,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.67,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.93,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.78,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.55,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.61,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.61,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.61,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.61,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.61,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.61,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.61,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.61,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.61,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.61,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('asp_i','CG'),('sglu','CD'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.73,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sglu','OE1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.36,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sglu','OE2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.39,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sglu','CD'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.64,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sglu','OE1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.32,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sglu','OE2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.32,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sglu','CD'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sglu','OE1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.60,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sglu','OE2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.72,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.67,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.80,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.12,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.67,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.80,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.18,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.89,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.01,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rlys','CD'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.96,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp_i','CG'),('rlys','CE'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.30,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp_i','CG'),('rlys','NZ'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.32,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp_i','OD1'),('rlys','CD'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.70,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp_i','OD1'),('rlys','CE'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.46,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp_i','OD1'),('rlys','NZ'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.67,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp_i','OD2'),('rlys','CD'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.20,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp_i','OD2'),('rlys','CE'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.28,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp_i','OD2'),('rlys','NZ'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp_i','CG'),('rlys','CD'))] = cmd.select('asp_i28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.87,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp_i','CG'),('rlys','CE'))] = cmd.select('asp_i29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp_i','CG'),('rlys','NZ'))] = cmd.select('asp_i30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp_i','OD1'),('rlys','CD'))] = cmd.select('asp_i31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.87,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp_i','OD1'),('rlys','CE'))] = cmd.select('asp_i32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp_i','OD1'),('rlys','NZ'))] = cmd.select('asp_i33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp_i','OD2'),('rlys','CD'))] = cmd.select('asp_i34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.87,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp_i','OD2'),('rlys','CE'))] = cmd.select('asp_i35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp_i','OD2'),('rlys','NZ'))] = cmd.select('asp_i36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.39,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.83,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+14.43,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.64,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.96,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+13.75,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.04,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.29,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+14.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.28,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.13,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.67,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.55,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.35,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.93,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.61,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp_i','CG'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.96,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp_i','OD1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.70,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp_i','OD2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.20,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp_i','CG'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.30,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp_i','OD1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.46,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp_i','OD2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.28,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp_i','CG'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.32,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp_i','OD1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.67,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp_i','OD2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys_i','CD'),('sglu','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sglu','OE1'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sglu','OE2'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sglu','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sglu','OE1'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sglu','OE2'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sglu','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sglu','OE1'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sglu','OE2'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','CG'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','CG'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','CG'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp_i','CG'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp_i','OD1'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp_i','OD2'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp_i','CG'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp_i','OD1'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp_i','OD2'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp_i','CG'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp_i','OD1'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp_i','OD2'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.87,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.87,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.87,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_1hgx_2_4_2_8'] = cmd.select('S_1hgx_2_4_2_8', 'glu|asp|asp_i|lys|lys_i')
cmd.delete('glu')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('lys')
cmd.delete('lys_i')
