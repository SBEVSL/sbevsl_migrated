'''
FUNC:S_1dku_2_7_6_1
PDB:1dku
EC:2.7.6.1
RESI:asp,asp,asp,cys
LOCI:a-223,224,227,250;
'''
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.00,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.15,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.78,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.95,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.09,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.63,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.11,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.24,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.78,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.36,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.36,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.30,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.84,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.88,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.79,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.39,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.40,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.21,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.58,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.18,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.80,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.43,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.14,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.76,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.67,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.24,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.90,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.95,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.11,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.15,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.09,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.78,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.63,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('rasp','CG'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.05,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp_i','CG'),('rasp','OD1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.01,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp_i','CG'),('rasp','OD2'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.30,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp_i','OD1'),('rasp','CG'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.53,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp_i','OD1'),('rasp','OD1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.55,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp_i','OD1'),('rasp','OD2'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.66,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp_i','OD2'),('rasp','CG'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.38,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp_i','OD2'),('rasp','OD1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.35,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp_i','OD2'),('rasp','OD2'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.62,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp_i','CG'),('rcys','CA'))] = cmd.select('asp_i19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.46,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp_i','CG'),('rcys','CB'))] = cmd.select('asp_i20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.42,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp_i','CG'),('rcys','SG'))] = cmd.select('asp_i21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.02,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp_i','OD1'),('rcys','CA'))] = cmd.select('asp_i22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.19,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp_i','OD1'),('rcys','CB'))] = cmd.select('asp_i23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.02,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp_i','OD1'),('rcys','SG'))] = cmd.select('asp_i24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.48,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp_i','OD2'),('rcys','CA'))] = cmd.select('asp_i25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.09,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp_i','OD2'),('rcys','CB'))] = cmd.select('asp_i26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.17,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp_i','OD2'),('rcys','SG'))] = cmd.select('asp_i27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.87,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('asp_ii','CG'),('sasp','CG'))] = cmd.select('asp_ii1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_ii','CG'),('sasp','OD1'))] = cmd.select('asp_ii2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.84,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_ii','CG'),('sasp','OD2'))] = cmd.select('asp_ii3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.39,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_ii','OD1'),('sasp','CG'))] = cmd.select('asp_ii4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_ii','OD1'),('sasp','OD1'))] = cmd.select('asp_ii5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.88,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_ii','OD1'),('sasp','OD2'))] = cmd.select('asp_ii6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.40,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_ii','OD2'),('sasp','CG'))] = cmd.select('asp_ii7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.30,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_ii','OD2'),('sasp','OD1'))] = cmd.select('asp_ii8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.79,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_ii','OD2'),('sasp','OD2'))] = cmd.select('asp_ii9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.21,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_ii','CG'),('sasp_i','CG'))] = cmd.select('asp_ii10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.05,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('asp_ii','CG'),('sasp_i','OD1'))] = cmd.select('asp_ii11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.53,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('asp_ii','CG'),('sasp_i','OD2'))] = cmd.select('asp_ii12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.38,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('asp_ii','OD1'),('sasp_i','CG'))] = cmd.select('asp_ii13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.01,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('asp_ii','OD1'),('sasp_i','OD1'))] = cmd.select('asp_ii14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.55,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('asp_ii','OD1'),('sasp_i','OD2'))] = cmd.select('asp_ii15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.35,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('asp_ii','OD2'),('sasp_i','CG'))] = cmd.select('asp_ii16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.30,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('asp_ii','OD2'),('sasp_i','OD1'))] = cmd.select('asp_ii17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.66,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('asp_ii','OD2'),('sasp_i','OD2'))] = cmd.select('asp_ii18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.62,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('asp_ii','CG'),('rcys','CA'))] = cmd.select('asp_ii19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.20,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp_ii','CG'),('rcys','CB'))] = cmd.select('asp_ii20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.54,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp_ii','CG'),('rcys','SG'))] = cmd.select('asp_ii21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.21,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp_ii','OD1'),('rcys','CA'))] = cmd.select('asp_ii22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.52,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp_ii','OD1'),('rcys','CB'))] = cmd.select('asp_ii23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.87,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp_ii','OD1'),('rcys','SG'))] = cmd.select('asp_ii24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+18.67,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp_ii','OD2'),('rcys','CA'))] = cmd.select('asp_ii25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.04,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp_ii','OD2'),('rcys','CB'))] = cmd.select('asp_ii26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+18.35,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp_ii','OD2'),('rcys','SG'))] = cmd.select('asp_ii27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+18.93,resSelectionSubs('cys','SG',subs)))
IDSpec['asp_ii'] = cmd.select('asp_ii',' br. asp_ii1&br. asp_ii2&br. asp_ii3&br. asp_ii4&br. asp_ii5&br. asp_ii6&br. asp_ii7&br. asp_ii8&br. asp_ii9&br. asp_ii10&br. asp_ii11&br. asp_ii12&br. asp_ii13&br. asp_ii14&br. asp_ii15&br. asp_ii16&br. asp_ii17&br. asp_ii18&br. asp_ii19&br. asp_ii20&br. asp_ii21&br. asp_ii22&br. asp_ii23&br. asp_ii24&br. asp_ii25&br. asp_ii26&br. asp_ii27')
IDSpec['r_asp_ii'] = cmd.count_atoms(resSelectionSubs('asp_ii', subs=subs, selection=True))
cmd.delete('asp_ii1')
cmd.delete('asp_ii2')
cmd.delete('asp_ii3')
cmd.delete('asp_ii4')
cmd.delete('asp_ii5')
cmd.delete('asp_ii6')
cmd.delete('asp_ii7')
cmd.delete('asp_ii8')
cmd.delete('asp_ii9')
cmd.delete('asp_ii10')
cmd.delete('asp_ii11')
cmd.delete('asp_ii12')
cmd.delete('asp_ii13')
cmd.delete('asp_ii14')
cmd.delete('asp_ii15')
cmd.delete('asp_ii16')
cmd.delete('asp_ii17')
cmd.delete('asp_ii18')
cmd.delete('asp_ii19')
cmd.delete('asp_ii20')
cmd.delete('asp_ii21')
cmd.delete('asp_ii22')
cmd.delete('asp_ii23')
cmd.delete('asp_ii24')
cmd.delete('asp_ii25')
cmd.delete('asp_ii26')
cmd.delete('asp_ii27')
IDSpec[(('cys','CA'),('sasp','CG'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.58,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.43,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.67,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','CG'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.18,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','CG'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.80,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.76,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.90,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp_i','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.46,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp_i','OD1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.19,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp_i','OD2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.09,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp_i','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.42,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp_i','OD1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.02,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp_i','OD2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.17,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp_i','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.02,resSelectionSubs('asp_i','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp_i','OD1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.48,resSelectionSubs('asp_i','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp_i','OD2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.87,resSelectionSubs('asp_i','OD2',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp_ii','CG'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.20,resSelectionSubs('asp_ii','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp_ii','OD1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.52,resSelectionSubs('asp_ii','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp_ii','OD2'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+17.04,resSelectionSubs('asp_ii','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp_ii','CG'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+17.54,resSelectionSubs('asp_ii','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp_ii','OD1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+17.87,resSelectionSubs('asp_ii','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp_ii','OD2'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+18.35,resSelectionSubs('asp_ii','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp_ii','CG'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+18.21,resSelectionSubs('asp_ii','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp_ii','OD1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+18.67,resSelectionSubs('asp_ii','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp_ii','OD2'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+18.93,resSelectionSubs('asp_ii','OD2',subs,selection=True)))
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
IDSpec['S_1dku_2_7_6_1'] = cmd.select('S_1dku_2_7_6_1', 'asp|asp_i|asp_ii|cys')
cmd.delete('asp')
cmd.delete('asp_i')
cmd.delete('asp_ii')
cmd.delete('cys')
