'''
FUNC:S_1hg1_3_5_1_1
PDB:1hg1
EC:3.5.1.1
RESI:thr,thr,asp,lys,val
LOCI:a-15,95,96,168,284;
'''
IDSpec[(('thr','CA'),('rthr_i','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.71,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','CA'),('rthr_i','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.53,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','CA'),('rthr_i','OG1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.06,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','CB'),('rthr_i','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.08,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','CB'),('rthr_i','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.65,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','CB'),('rthr_i','OG1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.03,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','OG1'),('rthr_i','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.88,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','OG1'),('rthr_i','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.48,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','OG1'),('rthr_i','OG1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.62,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','CA'),('rasp','CG'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.91,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CA'),('rasp','OD1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.81,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CA'),('rasp','OD2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.73,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','CB'),('rasp','CG'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.15,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CB'),('rasp','OD1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.88,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CB'),('rasp','OD2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.04,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','OG1'),('rasp','CG'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.06,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','OG1'),('rasp','OD1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.85,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','OG1'),('rasp','OD2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','CA'),('rlys','CD'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.13,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CA'),('rlys','CE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.43,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CA'),('rlys','NZ'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.21,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','CB'),('rlys','CD'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.01,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','CB'),('rlys','CE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.19,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','CB'),('rlys','NZ'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.99,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','OG1'),('rlys','CD'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.45,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr','OG1'),('rlys','CE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.60,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr','OG1'),('rlys','NZ'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.28,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr','CA'),('rval','CA'))] = cmd.select('thr28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+35.29,resSelectionSubs('val','CA',subs)))
IDSpec[(('thr','CA'),('rval','CB'))] = cmd.select('thr29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+34.52,resSelectionSubs('val','CB',subs)))
IDSpec[(('thr','CA'),('rval','CG1'))] = cmd.select('thr30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+35.50,resSelectionSubs('val','CG1',subs)))
IDSpec[(('thr','CB'),('rval','CA'))] = cmd.select('thr31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+34.47,resSelectionSubs('val','CA',subs)))
IDSpec[(('thr','CB'),('rval','CB'))] = cmd.select('thr32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+33.73,resSelectionSubs('val','CB',subs)))
IDSpec[(('thr','CB'),('rval','CG1'))] = cmd.select('thr33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+34.73,resSelectionSubs('val','CG1',subs)))
IDSpec[(('thr','OG1'),('rval','CA'))] = cmd.select('thr34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+33.91,resSelectionSubs('val','CA',subs)))
IDSpec[(('thr','OG1'),('rval','CB'))] = cmd.select('thr35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+33.13,resSelectionSubs('val','CB',subs)))
IDSpec[(('thr','OG1'),('rval','CG1'))] = cmd.select('thr36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+34.08,resSelectionSubs('val','CG1',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27&br. thr28&br. thr29&br. thr30&br. thr31&br. thr32&br. thr33&br. thr34&br. thr35&br. thr36')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
cmd.delete('thr19')
cmd.delete('thr20')
cmd.delete('thr21')
cmd.delete('thr22')
cmd.delete('thr23')
cmd.delete('thr24')
cmd.delete('thr25')
cmd.delete('thr26')
cmd.delete('thr27')
cmd.delete('thr28')
cmd.delete('thr29')
cmd.delete('thr30')
cmd.delete('thr31')
cmd.delete('thr32')
cmd.delete('thr33')
cmd.delete('thr34')
cmd.delete('thr35')
cmd.delete('thr36')
IDSpec[(('thr_i','CA'),('sthr','CA'))] = cmd.select('thr_i1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.71,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','CB'))] = cmd.select('thr_i2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.08,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','OG1'))] = cmd.select('thr_i3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.88,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CA'))] = cmd.select('thr_i4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.53,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CB'))] = cmd.select('thr_i5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.65,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','OG1'))] = cmd.select('thr_i6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.48,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CA'))] = cmd.select('thr_i7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.06,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CB'))] = cmd.select('thr_i8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.03,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','OG1'))] = cmd.select('thr_i9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.62,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','CA'),('rasp','CG'))] = cmd.select('thr_i10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.15,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr_i','CA'),('rasp','OD1'))] = cmd.select('thr_i11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.80,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr_i','CA'),('rasp','OD2'))] = cmd.select('thr_i12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.09,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr_i','CB'),('rasp','CG'))] = cmd.select('thr_i13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.38,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr_i','CB'),('rasp','OD1'))] = cmd.select('thr_i14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.69,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr_i','CB'),('rasp','OD2'))] = cmd.select('thr_i15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.32,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr_i','OG1'),('rasp','CG'))] = cmd.select('thr_i16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.40,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr_i','OG1'),('rasp','OD1'))] = cmd.select('thr_i17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.60,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr_i','OG1'),('rasp','OD2'))] = cmd.select('thr_i18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.24,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr_i','CA'),('rlys','CD'))] = cmd.select('thr_i19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.86,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr_i','CA'),('rlys','CE'))] = cmd.select('thr_i20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.18,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr_i','CA'),('rlys','NZ'))] = cmd.select('thr_i21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.61,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr_i','CB'),('rlys','CD'))] = cmd.select('thr_i22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.25,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr_i','CB'),('rlys','CE'))] = cmd.select('thr_i23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.22,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr_i','CB'),('rlys','NZ'))] = cmd.select('thr_i24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.72,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr_i','OG1'),('rlys','CD'))] = cmd.select('thr_i25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.11,resSelectionSubs('lys','CD',subs)))
IDSpec[(('thr_i','OG1'),('rlys','CE'))] = cmd.select('thr_i26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.70,resSelectionSubs('lys','CE',subs)))
IDSpec[(('thr_i','OG1'),('rlys','NZ'))] = cmd.select('thr_i27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+4.77,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('thr_i','CA'),('rval','CA'))] = cmd.select('thr_i28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+27.69,resSelectionSubs('val','CA',subs)))
IDSpec[(('thr_i','CA'),('rval','CB'))] = cmd.select('thr_i29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+26.96,resSelectionSubs('val','CB',subs)))
IDSpec[(('thr_i','CA'),('rval','CG1'))] = cmd.select('thr_i30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+28.00,resSelectionSubs('val','CG1',subs)))
IDSpec[(('thr_i','CB'),('rval','CA'))] = cmd.select('thr_i31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+27.99,resSelectionSubs('val','CA',subs)))
IDSpec[(('thr_i','CB'),('rval','CB'))] = cmd.select('thr_i32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+27.32,resSelectionSubs('val','CB',subs)))
IDSpec[(('thr_i','CB'),('rval','CG1'))] = cmd.select('thr_i33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+28.39,resSelectionSubs('val','CG1',subs)))
IDSpec[(('thr_i','OG1'),('rval','CA'))] = cmd.select('thr_i34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+28.48,resSelectionSubs('val','CA',subs)))
IDSpec[(('thr_i','OG1'),('rval','CB'))] = cmd.select('thr_i35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+27.77,resSelectionSubs('val','CB',subs)))
IDSpec[(('thr_i','OG1'),('rval','CG1'))] = cmd.select('thr_i36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+28.79,resSelectionSubs('val','CG1',subs)))
IDSpec['thr_i'] = cmd.select('thr_i',' br. thr_i1&br. thr_i2&br. thr_i3&br. thr_i4&br. thr_i5&br. thr_i6&br. thr_i7&br. thr_i8&br. thr_i9&br. thr_i10&br. thr_i11&br. thr_i12&br. thr_i13&br. thr_i14&br. thr_i15&br. thr_i16&br. thr_i17&br. thr_i18&br. thr_i19&br. thr_i20&br. thr_i21&br. thr_i22&br. thr_i23&br. thr_i24&br. thr_i25&br. thr_i26&br. thr_i27&br. thr_i28&br. thr_i29&br. thr_i30&br. thr_i31&br. thr_i32&br. thr_i33&br. thr_i34&br. thr_i35&br. thr_i36')
IDSpec['r_thr_i'] = cmd.count_atoms(resSelectionSubs('thr_i', subs=subs, selection=True))
cmd.delete('thr_i1')
cmd.delete('thr_i2')
cmd.delete('thr_i3')
cmd.delete('thr_i4')
cmd.delete('thr_i5')
cmd.delete('thr_i6')
cmd.delete('thr_i7')
cmd.delete('thr_i8')
cmd.delete('thr_i9')
cmd.delete('thr_i10')
cmd.delete('thr_i11')
cmd.delete('thr_i12')
cmd.delete('thr_i13')
cmd.delete('thr_i14')
cmd.delete('thr_i15')
cmd.delete('thr_i16')
cmd.delete('thr_i17')
cmd.delete('thr_i18')
cmd.delete('thr_i19')
cmd.delete('thr_i20')
cmd.delete('thr_i21')
cmd.delete('thr_i22')
cmd.delete('thr_i23')
cmd.delete('thr_i24')
cmd.delete('thr_i25')
cmd.delete('thr_i26')
cmd.delete('thr_i27')
cmd.delete('thr_i28')
cmd.delete('thr_i29')
cmd.delete('thr_i30')
cmd.delete('thr_i31')
cmd.delete('thr_i32')
cmd.delete('thr_i33')
cmd.delete('thr_i34')
cmd.delete('thr_i35')
cmd.delete('thr_i36')
IDSpec[(('asp','CG'),('sthr','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.91,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.15,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','OG1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.06,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.81,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.88,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','OG1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.85,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.73,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.04,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','OG1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.82,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr_i','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.15,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr_i','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.38,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr_i','OG1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.40,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr_i','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.80,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr_i','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.69,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr_i','OG1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.60,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr_i','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.09,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr_i','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.32,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr_i','OG1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.24,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.23,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.18,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.99,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.26,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.00,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.76,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.40,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.19,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.91,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rval','CA'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.69,resSelectionSubs('val','CA',subs)))
IDSpec[(('asp','CG'),('rval','CB'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+26.78,resSelectionSubs('val','CB',subs)))
IDSpec[(('asp','CG'),('rval','CG1'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.60,resSelectionSubs('val','CG1',subs)))
IDSpec[(('asp','OD1'),('rval','CA'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.55,resSelectionSubs('val','CA',subs)))
IDSpec[(('asp','OD1'),('rval','CB'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+26.70,resSelectionSubs('val','CB',subs)))
IDSpec[(('asp','OD1'),('rval','CG1'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.57,resSelectionSubs('val','CG1',subs)))
IDSpec[(('asp','OD2'),('rval','CA'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.63,resSelectionSubs('val','CA',subs)))
IDSpec[(('asp','OD2'),('rval','CB'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.69,resSelectionSubs('val','CB',subs)))
IDSpec[(('asp','OD2'),('rval','CG1'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.47,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('lys','CD'),('sthr','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.13,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.01,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr','OG1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.45,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.43,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.19,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr','OG1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.60,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.21,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.99,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr','OG1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.28,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr_i','CA'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.86,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr_i','CB'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.25,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sthr_i','OG1'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.11,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr_i','CA'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.18,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr_i','CB'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.22,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sthr_i','OG1'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.70,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr_i','CA'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.61,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr_i','CB'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.72,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sthr_i','OG1'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.77,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.26,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.40,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.18,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.19,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.99,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.76,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('rval','CA'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+24.80,resSelectionSubs('val','CA',subs)))
IDSpec[(('lys','CD'),('rval','CB'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+24.13,resSelectionSubs('val','CB',subs)))
IDSpec[(('lys','CD'),('rval','CG1'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+25.16,resSelectionSubs('val','CG1',subs)))
IDSpec[(('lys','CE'),('rval','CA'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.05,resSelectionSubs('val','CA',subs)))
IDSpec[(('lys','CE'),('rval','CB'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+25.41,resSelectionSubs('val','CB',subs)))
IDSpec[(('lys','CE'),('rval','CG1'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+26.43,resSelectionSubs('val','CG1',subs)))
IDSpec[(('lys','NZ'),('rval','CA'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.12,resSelectionSubs('val','CA',subs)))
IDSpec[(('lys','NZ'),('rval','CB'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+26.42,resSelectionSubs('val','CB',subs)))
IDSpec[(('lys','NZ'),('rval','CG1'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.40,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('val','CA'),('sthr','CA'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+35.29,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('val','CA'),('sthr','CB'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+34.47,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('val','CA'),('sthr','OG1'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+33.91,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('val','CB'),('sthr','CA'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+34.52,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('val','CB'),('sthr','CB'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+33.73,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('val','CB'),('sthr','OG1'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+33.13,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('val','CG1'),('sthr','CA'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+35.50,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('sthr','CB'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+34.73,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('val','CG1'),('sthr','OG1'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+34.08,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('val','CA'),('sthr_i','CA'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+27.69,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('val','CA'),('sthr_i','CB'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+27.99,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('val','CA'),('sthr_i','OG1'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+28.48,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('val','CB'),('sthr_i','CA'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+26.96,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('val','CB'),('sthr_i','CB'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+27.32,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('val','CB'),('sthr_i','OG1'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+27.77,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('val','CG1'),('sthr_i','CA'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+28.00,resSelectionSubs('thr_i','CA',subs,selection=True)))
IDSpec[(('val','CG1'),('sthr_i','CB'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+28.39,resSelectionSubs('thr_i','CB',subs,selection=True)))
IDSpec[(('val','CG1'),('sthr_i','OG1'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+28.79,resSelectionSubs('thr_i','OG1',subs,selection=True)))
IDSpec[(('val','CA'),('sasp','CG'))] = cmd.select('val19', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+27.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('val','CA'),('sasp','OD1'))] = cmd.select('val20', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+27.55,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('val','CA'),('sasp','OD2'))] = cmd.select('val21', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+28.63,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('val','CB'),('sasp','CG'))] = cmd.select('val22', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+26.78,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('val','CB'),('sasp','OD1'))] = cmd.select('val23', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+26.70,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('val','CB'),('sasp','OD2'))] = cmd.select('val24', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+27.69,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('val','CG1'),('sasp','CG'))] = cmd.select('val25', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+27.60,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('val','CG1'),('sasp','OD1'))] = cmd.select('val26', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+27.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('val','CG1'),('sasp','OD2'))] = cmd.select('val27', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+28.47,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('val','CA'),('slys','CD'))] = cmd.select('val28', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+24.80,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('val','CA'),('slys','CE'))] = cmd.select('val29', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+26.05,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('val','CA'),('slys','NZ'))] = cmd.select('val30', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+27.12,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('val','CB'),('slys','CD'))] = cmd.select('val31', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+24.13,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('val','CB'),('slys','CE'))] = cmd.select('val32', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+25.41,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('val','CB'),('slys','NZ'))] = cmd.select('val33', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+26.42,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('val','CG1'),('slys','CD'))] = cmd.select('val34', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+25.16,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('val','CG1'),('slys','CE'))] = cmd.select('val35', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+26.43,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('val','CG1'),('slys','NZ'))] = cmd.select('val36', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+27.40,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['val'] = cmd.select('val',' br. val1&br. val2&br. val3&br. val4&br. val5&br. val6&br. val7&br. val8&br. val9&br. val10&br. val11&br. val12&br. val13&br. val14&br. val15&br. val16&br. val17&br. val18&br. val19&br. val20&br. val21&br. val22&br. val23&br. val24&br. val25&br. val26&br. val27&br. val28&br. val29&br. val30&br. val31&br. val32&br. val33&br. val34&br. val35&br. val36')
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
cmd.delete('val28')
cmd.delete('val29')
cmd.delete('val30')
cmd.delete('val31')
cmd.delete('val32')
cmd.delete('val33')
cmd.delete('val34')
cmd.delete('val35')
cmd.delete('val36')
IDSpec['S_1hg1_3_5_1_1'] = cmd.select('S_1hg1_3_5_1_1', 'thr|thr_i|asp|lys|val')
cmd.delete('thr')
cmd.delete('thr_i')
cmd.delete('asp')
cmd.delete('lys')
cmd.delete('val')
