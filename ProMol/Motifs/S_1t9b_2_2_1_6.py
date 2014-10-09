'''
FUNC:S_1t9b_2_2_1_6
PDB:1t9b
EC:2.2.1.6
RESI:val,gly,met,val
LOCI:a-497,523,525,651;
'''
IDSpec[(('val','CA'),('rmet','CE'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+17.98,resSelectionSubs('met','CE',subs)))
IDSpec[(('val','CA'),('rmet','CG'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+17.81,resSelectionSubs('met','CG',subs)))
IDSpec[(('val','CA'),('rmet','SD'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+17.93,resSelectionSubs('met','SD',subs)))
IDSpec[(('val','CB'),('rmet','CE'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+16.86,resSelectionSubs('met','CE',subs)))
IDSpec[(('val','CB'),('rmet','CG'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+16.52,resSelectionSubs('met','CG',subs)))
IDSpec[(('val','CB'),('rmet','SD'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+16.73,resSelectionSubs('met','SD',subs)))
IDSpec[(('val','CG1'),('rmet','CE'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.53,resSelectionSubs('met','CE',subs)))
IDSpec[(('val','CG1'),('rmet','CG'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+16.95,resSelectionSubs('met','CG',subs)))
IDSpec[(('val','CG1'),('rmet','SD'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.32,resSelectionSubs('met','SD',subs)))
IDSpec[(('val','CA'),('rval','CA'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+14.87,resSelectionSubs('val','CA',subs)))
IDSpec[(('val','CA'),('rval','CB'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+15.78,resSelectionSubs('val','CB',subs)))
IDSpec[(('val','CA'),('rval','CG1'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+15.07,resSelectionSubs('val','CG1',subs)))
IDSpec[(('val','CB'),('rval','CA'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+13.46,resSelectionSubs('val','CA',subs)))
IDSpec[(('val','CB'),('rval','CB'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+14.34,resSelectionSubs('val','CB',subs)))
IDSpec[(('val','CB'),('rval','CG1'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+13.61,resSelectionSubs('val','CG1',subs)))
IDSpec[(('val','CG1'),('rval','CA'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+13.53,resSelectionSubs('val','CA',subs)))
IDSpec[(('val','CG1'),('rval','CB'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+14.41,resSelectionSubs('val','CB',subs)))
IDSpec[(('val','CG1'),('rval','CG1'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+13.71,resSelectionSubs('val','CG1',subs)))
IDSpec[(('val','CA'),('rgly','CA'))] = cmd.select('val19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+18.44,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val','CA'),('rgly','N'))] = cmd.select('val20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+19.55,resSelectionSubs('gly','N',subs)))
IDSpec[(('val','CA'),('rgly','O'))] = cmd.select('val21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+18.64,resSelectionSubs('gly','O',subs)))
IDSpec[(('val','CB'),('rgly','CA'))] = cmd.select('val22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+16.91,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val','CB'),('rgly','N'))] = cmd.select('val23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+18.02,resSelectionSubs('gly','N',subs)))
IDSpec[(('val','CB'),('rgly','O'))] = cmd.select('val24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+17.17,resSelectionSubs('gly','O',subs)))
IDSpec[(('val','CG1'),('rgly','CA'))] = cmd.select('val25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+16.72,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val','CG1'),('rgly','N'))] = cmd.select('val26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.76,resSelectionSubs('gly','N',subs)))
IDSpec[(('val','CG1'),('rgly','O'))] = cmd.select('val27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+17.21,resSelectionSubs('gly','O',subs)))
IDSpec['val'] = cmd.select('val',' br. val1&br. val2&br. val3&br. val4&br. val5&br. val6&br. val7&br. val8&br. val9&br. val10&br. val11&br. val12&br. val13&br. val14&br. val15&br. val16&br. val17&br. val18&br. val19&br. val20&br. val21&br. val22&br. val23&br. val24&br. val25&br. val26&br. val27')
IDSpec['r_val'] = cmd.count_atoms(resSelectionSubs('val', subs=subs, selection=True))
cmd.delete('val1')
cmd.delete('val2')
cmd.delete('val3')
cmd.delete('val4')
cmd.delete('val5')
cmd.delete('val6')
cmd.delete('val7')
cmd.delete('val8')
cmd.delete('val9')
cmd.delete('val10')
cmd.delete('val11')
cmd.delete('val12')
cmd.delete('val13')
cmd.delete('val14')
cmd.delete('val15')
cmd.delete('val16')
cmd.delete('val17')
cmd.delete('val18')
cmd.delete('val19')
cmd.delete('val20')
cmd.delete('val21')
cmd.delete('val22')
cmd.delete('val23')
cmd.delete('val24')
cmd.delete('val25')
cmd.delete('val26')
cmd.delete('val27')
IDSpec[(('met','CE'),('sval','CA'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+17.98,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('met','CE'),('sval','CB'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+16.86,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('met','CE'),('sval','CG1'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+17.53,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('met','CG'),('sval','CA'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+17.81,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('met','CG'),('sval','CB'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+16.52,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('met','CG'),('sval','CG1'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+16.95,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('met','SD'),('sval','CA'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+17.93,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('met','SD'),('sval','CB'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+16.73,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('met','SD'),('sval','CG1'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+17.32,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('met','CE'),('rval','CA'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.50,resSelectionSubs('val','CA',subs)))
IDSpec[(('met','CE'),('rval','CB'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.21,resSelectionSubs('val','CB',subs)))
IDSpec[(('met','CE'),('rval','CG1'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.61,resSelectionSubs('val','CG1',subs)))
IDSpec[(('met','CG'),('rval','CA'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+6.70,resSelectionSubs('val','CA',subs)))
IDSpec[(('met','CG'),('rval','CB'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+5.92,resSelectionSubs('val','CB',subs)))
IDSpec[(('met','CG'),('rval','CG1'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+6.39,resSelectionSubs('val','CG1',subs)))
IDSpec[(('met','SD'),('rval','CA'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+8.10,resSelectionSubs('val','CA',subs)))
IDSpec[(('met','SD'),('rval','CB'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+7.43,resSelectionSubs('val','CB',subs)))
IDSpec[(('met','SD'),('rval','CG1'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+7.57,resSelectionSubs('val','CG1',subs)))
IDSpec[(('met','CE'),('rgly','CA'))] = cmd.select('met19', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+11.63,resSelectionSubs('gly','CA',subs)))
IDSpec[(('met','CE'),('rgly','N'))] = cmd.select('met20', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+12.90,resSelectionSubs('gly','N',subs)))
IDSpec[(('met','CE'),('rgly','O'))] = cmd.select('met21', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.58,resSelectionSubs('gly','O',subs)))
IDSpec[(('met','CG'),('rgly','CA'))] = cmd.select('met22', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+8.89,resSelectionSubs('gly','CA',subs)))
IDSpec[(('met','CG'),('rgly','N'))] = cmd.select('met23', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+10.14,resSelectionSubs('gly','N',subs)))
IDSpec[(('met','CG'),('rgly','O'))] = cmd.select('met24', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+6.88,resSelectionSubs('gly','O',subs)))
IDSpec[(('met','SD'),('rgly','CA'))] = cmd.select('met25', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+10.21,resSelectionSubs('gly','CA',subs)))
IDSpec[(('met','SD'),('rgly','N'))] = cmd.select('met26', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+11.43,resSelectionSubs('gly','N',subs)))
IDSpec[(('met','SD'),('rgly','O'))] = cmd.select('met27', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+8.05,resSelectionSubs('gly','O',subs)))
IDSpec['met'] = cmd.select('met',' br. met1&br. met2&br. met3&br. met4&br. met5&br. met6&br. met7&br. met8&br. met9&br. met10&br. met11&br. met12&br. met13&br. met14&br. met15&br. met16&br. met17&br. met18&br. met19&br. met20&br. met21&br. met22&br. met23&br. met24&br. met25&br. met26&br. met27')
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
cmd.delete('met19')
cmd.delete('met20')
cmd.delete('met21')
cmd.delete('met22')
cmd.delete('met23')
cmd.delete('met24')
cmd.delete('met25')
cmd.delete('met26')
cmd.delete('met27')
IDSpec[(('val_i','CA'),('sval','CA'))] = cmd.select('val_i1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+14.87,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('val_i','CA'),('sval','CB'))] = cmd.select('val_i2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+13.46,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('val_i','CA'),('sval','CG1'))] = cmd.select('val_i3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+13.53,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('val_i','CB'),('sval','CA'))] = cmd.select('val_i4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+15.78,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('val_i','CB'),('sval','CB'))] = cmd.select('val_i5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+14.34,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('val_i','CB'),('sval','CG1'))] = cmd.select('val_i6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+14.41,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('val_i','CG1'),('sval','CA'))] = cmd.select('val_i7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+15.07,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('val_i','CG1'),('sval','CB'))] = cmd.select('val_i8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+13.61,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('val_i','CG1'),('sval','CG1'))] = cmd.select('val_i9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+13.71,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('val_i','CA'),('smet','CE'))] = cmd.select('val_i10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.50,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('val_i','CA'),('smet','CG'))] = cmd.select('val_i11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+6.70,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('val_i','CA'),('smet','SD'))] = cmd.select('val_i12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.10,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('val_i','CB'),('smet','CE'))] = cmd.select('val_i13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+8.21,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('val_i','CB'),('smet','CG'))] = cmd.select('val_i14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+5.92,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('val_i','CB'),('smet','SD'))] = cmd.select('val_i15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+7.43,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('val_i','CG1'),('smet','CE'))] = cmd.select('val_i16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+8.61,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('val_i','CG1'),('smet','CG'))] = cmd.select('val_i17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+6.39,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('val_i','CG1'),('smet','SD'))] = cmd.select('val_i18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+7.57,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('val_i','CA'),('rgly','CA'))] = cmd.select('val_i19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.07,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val_i','CA'),('rgly','N'))] = cmd.select('val_i20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+9.48,resSelectionSubs('gly','N',subs)))
IDSpec[(('val_i','CA'),('rgly','O'))] = cmd.select('val_i21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+7.67,resSelectionSubs('gly','O',subs)))
IDSpec[(('val_i','CB'),('rgly','CA'))] = cmd.select('val_i22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+6.75,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val_i','CB'),('rgly','N'))] = cmd.select('val_i23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+8.19,resSelectionSubs('gly','N',subs)))
IDSpec[(('val_i','CB'),('rgly','O'))] = cmd.select('val_i24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+6.13,resSelectionSubs('gly','O',subs)))
IDSpec[(('val_i','CG1'),('rgly','CA'))] = cmd.select('val_i25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+6.40,resSelectionSubs('gly','CA',subs)))
IDSpec[(('val_i','CG1'),('rgly','N'))] = cmd.select('val_i26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+7.85,resSelectionSubs('gly','N',subs)))
IDSpec[(('val_i','CG1'),('rgly','O'))] = cmd.select('val_i27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+5.84,resSelectionSubs('gly','O',subs)))
IDSpec['val_i'] = cmd.select('val_i',' br. val_i1&br. val_i2&br. val_i3&br. val_i4&br. val_i5&br. val_i6&br. val_i7&br. val_i8&br. val_i9&br. val_i10&br. val_i11&br. val_i12&br. val_i13&br. val_i14&br. val_i15&br. val_i16&br. val_i17&br. val_i18&br. val_i19&br. val_i20&br. val_i21&br. val_i22&br. val_i23&br. val_i24&br. val_i25&br. val_i26&br. val_i27')
IDSpec['r_val_i'] = cmd.count_atoms(resSelectionSubs('val_i', subs=subs, selection=True))
cmd.delete('val_i1')
cmd.delete('val_i2')
cmd.delete('val_i3')
cmd.delete('val_i4')
cmd.delete('val_i5')
cmd.delete('val_i6')
cmd.delete('val_i7')
cmd.delete('val_i8')
cmd.delete('val_i9')
cmd.delete('val_i10')
cmd.delete('val_i11')
cmd.delete('val_i12')
cmd.delete('val_i13')
cmd.delete('val_i14')
cmd.delete('val_i15')
cmd.delete('val_i16')
cmd.delete('val_i17')
cmd.delete('val_i18')
cmd.delete('val_i19')
cmd.delete('val_i20')
cmd.delete('val_i21')
cmd.delete('val_i22')
cmd.delete('val_i23')
cmd.delete('val_i24')
cmd.delete('val_i25')
cmd.delete('val_i26')
cmd.delete('val_i27')
IDSpec[(('gly','CA'),('sval','CA'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+18.44,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('sval','CB'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+16.91,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('sval','CG1'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+16.72,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gly','N'),('sval','CA'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+19.55,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gly','N'),('sval','CB'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+18.02,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gly','N'),('sval','CG1'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+17.76,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gly','O'),('sval','CA'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+18.64,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gly','O'),('sval','CB'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.17,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gly','O'),('sval','CG1'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.21,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gly','CA'),('smet','CE'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.63,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('gly','CA'),('smet','CG'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.89,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('smet','SD'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.21,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('gly','N'),('smet','CE'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+12.90,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('gly','N'),('smet','CG'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.14,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('gly','N'),('smet','SD'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.43,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('gly','O'),('smet','CE'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.58,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('gly','O'),('smet','CG'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.88,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('gly','O'),('smet','SD'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+8.05,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('gly','CA'),('sval_i','CA'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.07,resSelectionSubs('val_i','CA',subs,selection=True)))
IDSpec[(('gly','CA'),('sval_i','CB'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.75,resSelectionSubs('val_i','CB',subs,selection=True)))
IDSpec[(('gly','CA'),('sval_i','CG1'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.40,resSelectionSubs('val_i','CG1',subs,selection=True)))
IDSpec[(('gly','N'),('sval_i','CA'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.48,resSelectionSubs('val_i','CA',subs,selection=True)))
IDSpec[(('gly','N'),('sval_i','CB'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.19,resSelectionSubs('val_i','CB',subs,selection=True)))
IDSpec[(('gly','N'),('sval_i','CG1'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.85,resSelectionSubs('val_i','CG1',subs,selection=True)))
IDSpec[(('gly','O'),('sval_i','CA'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.67,resSelectionSubs('val_i','CA',subs,selection=True)))
IDSpec[(('gly','O'),('sval_i','CB'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.13,resSelectionSubs('val_i','CB',subs,selection=True)))
IDSpec[(('gly','O'),('sval_i','CG1'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.84,resSelectionSubs('val_i','CG1',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
IDSpec['S_1t9b_2_2_1_6'] = cmd.select('S_1t9b_2_2_1_6', 'val|met|val_i|gly')
cmd.delete('val')
cmd.delete('met')
cmd.delete('val_i')
cmd.delete('gly')
