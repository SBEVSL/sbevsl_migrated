'''
FUNC:S_3b9d_3_2_1_14
PDB:3b9d
EC:3.2.1.14
RESI:asp,asp,met
LOCI:a-311,313,315;
'''
IDSpec[(('asp','CG'),('rmet','CE'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.08,resSelectionSubs('met','CE',subs)))
IDSpec[(('asp','CG'),('rmet','CG'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.53,resSelectionSubs('met','CG',subs)))
IDSpec[(('asp','CG'),('rmet','SD'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.75,resSelectionSubs('met','SD',subs)))
IDSpec[(('asp','OD1'),('rmet','CE'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.73,resSelectionSubs('met','CE',subs)))
IDSpec[(('asp','OD1'),('rmet','CG'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.14,resSelectionSubs('met','CG',subs)))
IDSpec[(('asp','OD1'),('rmet','SD'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.53,resSelectionSubs('met','SD',subs)))
IDSpec[(('asp','OD2'),('rmet','CE'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.27,resSelectionSubs('met','CE',subs)))
IDSpec[(('asp','OD2'),('rmet','CG'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.04,resSelectionSubs('met','CG',subs)))
IDSpec[(('asp','OD2'),('rmet','SD'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.94,resSelectionSubs('met','SD',subs)))
IDSpec[(('asp','CG'),('rasp_i','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.07,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.52,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','CG'),('rasp_i','OD2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.15,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp_i','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.24,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.44,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp_i','OD2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.58,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp_i','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.26,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.90,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp_i','OD2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.11,resSelectionSubs('asp_i','OD2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
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
IDSpec[(('met','CE'),('sasp','CG'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+10.08,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('met','CE'),('sasp','OD1'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+10.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('met','CE'),('sasp','OD2'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+10.27,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('met','CG'),('sasp','CG'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+8.53,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('met','CG'),('sasp','OD1'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+9.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('met','CG'),('sasp','OD2'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+9.04,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('met','SD'),('sasp','CG'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+8.75,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('met','SD'),('sasp','OD1'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+9.53,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('met','SD'),('sasp','OD2'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+8.94,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('met','CE'),('rasp_i','CG'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+13.84,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('met','CE'),('rasp_i','OD1'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+13.85,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('met','CE'),('rasp_i','OD2'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+12.95,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('met','CG'),('rasp_i','CG'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+12.38,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('met','CG'),('rasp_i','OD1'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+12.41,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('met','CG'),('rasp_i','OD2'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.59,resSelectionSubs('asp_i','OD2',subs)))
IDSpec[(('met','SD'),('rasp_i','CG'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+12.69,resSelectionSubs('asp_i','CG',subs)))
IDSpec[(('met','SD'),('rasp_i','OD1'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+12.83,resSelectionSubs('asp_i','OD1',subs)))
IDSpec[(('met','SD'),('rasp_i','OD2'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+11.76,resSelectionSubs('asp_i','OD2',subs)))
IDSpec['met'] = cmd.select('met',' br. met1&br. met2&br. met3&br. met4&br. met5&br. met6&br. met7&br. met8&br. met9&br. met10&br. met11&br. met12&br. met13&br. met14&br. met15&br. met16&br. met17&br. met18')
IDSpec['r_met'] = cmd.count_atoms(resSelectionSubs('met', subs=subs, selection=True))
cmd.delete('met1')
cmd.delete('met2')
cmd.delete('met3')
cmd.delete('met4')
cmd.delete('met5')
cmd.delete('met6')
cmd.delete('met7')
cmd.delete('met8')
cmd.delete('met9')
cmd.delete('met10')
cmd.delete('met11')
cmd.delete('met12')
cmd.delete('met13')
cmd.delete('met14')
cmd.delete('met15')
cmd.delete('met16')
cmd.delete('met17')
cmd.delete('met18')
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.07,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.26,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.52,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.90,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.15,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.58,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.11,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','CG'),('smet','CE'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.84,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asp_i','CG'),('smet','CG'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.38,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('smet','SD'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.69,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('smet','CE'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.85,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('smet','CG'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.41,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('smet','SD'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.83,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('smet','CE'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.95,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('smet','CG'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.59,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('smet','SD'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.76,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18')
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
IDSpec['S_3b9d_3_2_1_14'] = cmd.select('S_3b9d_3_2_1_14', 'asp|met|asp_i')
cmd.delete('asp')
cmd.delete('met')
cmd.delete('asp_i')
