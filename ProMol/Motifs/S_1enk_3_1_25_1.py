'''
FUNC:S_1enk_3_1_25_1
PDB:1enk
EC:3.1.25.1
RESI:thr,arg,asp,arg
LOCI:a-2,22,23,26;
'''
IDSpec[(('arg','CZ'),('rthr','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.55,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','CZ'),('rthr','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+16.07,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','CZ'),('rthr','OG1'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+15.68,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NE'),('rthr','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.27,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NE'),('rthr','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.78,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NE'),('rthr','OG1'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.36,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NH1'),('rthr','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.05,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NH1'),('rthr','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.62,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NH1'),('rthr','OG1'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+16.35,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.90,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.01,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.88,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.69,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.76,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.69,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.26,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.48,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.19,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','CZ'),('rarg','CZ'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg','NE'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.33,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','CZ'),('rarg','NH1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.51,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NE'),('rarg','CZ'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.00,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NE'),('rarg','NE'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.07,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NE'),('rarg','NH1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.20,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg','CZ'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.27,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg','NE'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.27,resSelectionSubs('arg','NE',subs)))
IDSpec[(('arg','NH1'),('rarg','NH1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.47,resSelectionSubs('arg','NH1',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
IDSpec[(('thr','CA'),('sarg','CZ'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+15.55,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+14.27,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NH1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+16.05,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','CZ'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.07,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+14.78,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NH1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+16.62,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','CZ'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+15.68,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+14.36,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NH1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+16.35,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CA'),('rasp','CG'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.96,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CA'),('rasp','OD1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.58,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CA'),('rasp','OD2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.40,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','CB'),('rasp','CG'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.78,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','CB'),('rasp','OD1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.36,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','CB'),('rasp','OD2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.54,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','OG1'),('rasp','CG'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.07,resSelectionSubs('asp','CG',subs)))
IDSpec[(('thr','OG1'),('rasp','OD1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.34,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('thr','OG1'),('rasp','OD2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.07,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('thr','CA'),('rarg','CZ'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.75,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CA'),('rarg','NE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.15,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CA'),('rarg','NH1'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.39,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','CB'),('rarg','CZ'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.64,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','CB'),('rarg','NE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.81,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','CB'),('rarg','NH1'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.55,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('thr','OG1'),('rarg','CZ'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.67,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('thr','OG1'),('rarg','NE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.80,resSelectionSubs('arg','NE',subs)))
IDSpec[(('thr','OG1'),('rarg','NH1'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.73,resSelectionSubs('arg','NH1',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27')
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
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.90,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.69,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.26,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.01,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.76,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.48,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.88,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.69,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.19,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.96,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.78,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sthr','OG1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.07,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.58,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.36,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sthr','OG1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.34,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.40,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.54,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sthr','OG1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.07,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.09,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.96,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.28,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.14,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.21,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.19,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.14,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.98,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.31,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.26,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.00,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.27,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.33,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.07,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.27,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.51,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.20,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.47,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sthr','CA'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.75,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sthr','CB'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.64,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sthr','OG1'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.67,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sthr','CA'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.15,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sthr','CB'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.81,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sthr','OG1'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.80,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sthr','CA'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.39,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sthr','CB'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.55,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sthr','OG1'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.73,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','CG'))] = cmd.select('arg_i19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.09,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','OD1'))] = cmd.select('arg_i20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.14,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','OD2'))] = cmd.select('arg_i21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.14,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','CG'))] = cmd.select('arg_i22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.96,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','OD1'))] = cmd.select('arg_i23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.21,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','OD2'))] = cmd.select('arg_i24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.98,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','CG'))] = cmd.select('arg_i25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.28,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','OD1'))] = cmd.select('arg_i26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.19,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','OD2'))] = cmd.select('arg_i27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.31,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['arg_i'] = cmd.select('arg_i',' br. arg_i1&br. arg_i2&br. arg_i3&br. arg_i4&br. arg_i5&br. arg_i6&br. arg_i7&br. arg_i8&br. arg_i9&br. arg_i10&br. arg_i11&br. arg_i12&br. arg_i13&br. arg_i14&br. arg_i15&br. arg_i16&br. arg_i17&br. arg_i18&br. arg_i19&br. arg_i20&br. arg_i21&br. arg_i22&br. arg_i23&br. arg_i24&br. arg_i25&br. arg_i26&br. arg_i27')
IDSpec['r_arg_i'] = cmd.count_atoms(resSelectionSubs('arg_i', subs=subs, selection=True))
cmd.delete('arg_i1')
cmd.delete('arg_i2')
cmd.delete('arg_i3')
cmd.delete('arg_i4')
cmd.delete('arg_i5')
cmd.delete('arg_i6')
cmd.delete('arg_i7')
cmd.delete('arg_i8')
cmd.delete('arg_i9')
cmd.delete('arg_i10')
cmd.delete('arg_i11')
cmd.delete('arg_i12')
cmd.delete('arg_i13')
cmd.delete('arg_i14')
cmd.delete('arg_i15')
cmd.delete('arg_i16')
cmd.delete('arg_i17')
cmd.delete('arg_i18')
cmd.delete('arg_i19')
cmd.delete('arg_i20')
cmd.delete('arg_i21')
cmd.delete('arg_i22')
cmd.delete('arg_i23')
cmd.delete('arg_i24')
cmd.delete('arg_i25')
cmd.delete('arg_i26')
cmd.delete('arg_i27')
IDSpec['S_1enk_3_1_25_1'] = cmd.select('S_1enk_3_1_25_1', 'arg|thr|asp|arg_i')
cmd.delete('arg')
cmd.delete('thr')
cmd.delete('asp')
cmd.delete('arg_i')
