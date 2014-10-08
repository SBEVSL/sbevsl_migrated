'''
FUNC:S_1o5k_4_2_1_52
PDB:1o5k
EC:4.2.1.52
RESI:thr,thr,tyr,arg
LOCI:a-43,44,132,137;
'''
IDSpec[(('arg','CZ'),('rtyr','CE1'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.06,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','CZ'),('rtyr','CZ'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.02,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','CZ'),('rtyr','OH'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.84,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NE'),('rtyr','CE1'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.98,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NE'),('rtyr','CZ'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.04,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NE'),('rtyr','OH'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.90,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','NH1'),('rtyr','CE1'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.60,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('arg','NH1'),('rtyr','CZ'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.59,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('arg','NH1'),('rtyr','OH'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.32,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('arg','CZ'),('rthr','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.02,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','CZ'),('rthr','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.72,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','CZ'),('rthr','OG1'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.94,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NE'),('rthr','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.62,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NE'),('rthr','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.18,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NE'),('rthr','OG1'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.26,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','NH1'),('rthr','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.46,resSelectionSubs('thr','CA',subs)))
IDSpec[(('arg','NH1'),('rthr','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.06,resSelectionSubs('thr','CB',subs)))
IDSpec[(('arg','NH1'),('rthr','OG1'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.26,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('arg','CZ'),('rthr_i','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.60,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('arg','CZ'),('rthr_i','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.24,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('arg','CZ'),('rthr_i','OG1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.77,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('arg','NE'),('rthr_i','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.92,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('arg','NE'),('rthr_i','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.41,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('arg','NE'),('rthr_i','OG1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.52,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('arg','NH1'),('rthr_i','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.82,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('arg','NH1'),('rthr_i','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.57,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('arg','NH1'),('rthr_i','OG1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.29,resSelectionSubs('thr_i','OG1',subs)))
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
IDSpec[(('tyr','CE1'),('sarg','CZ'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.06,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.98,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sarg','NH1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.60,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','CZ'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.02,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.04,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sarg','NH1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.59,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','CZ'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.84,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.90,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('tyr','OH'),('sarg','NH1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.32,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rthr','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.65,resSelectionSubs('thr','CA',subs)))
IDSpec[(('tyr','CE1'),('rthr','CB'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.43,resSelectionSubs('thr','CB',subs)))
IDSpec[(('tyr','CE1'),('rthr','OG1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.41,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('tyr','CZ'),('rthr','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.48,resSelectionSubs('thr','CA',subs)))
IDSpec[(('tyr','CZ'),('rthr','CB'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.41,resSelectionSubs('thr','CB',subs)))
IDSpec[(('tyr','CZ'),('rthr','OG1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.47,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('tyr','OH'),('rthr','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.69,resSelectionSubs('thr','CA',subs)))
IDSpec[(('tyr','OH'),('rthr','CB'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.64,resSelectionSubs('thr','CB',subs)))
IDSpec[(('tyr','OH'),('rthr','OG1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.59,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('tyr','CE1'),('rthr_i','CA'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.77,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('tyr','CE1'),('rthr_i','CB'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.76,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('tyr','CE1'),('rthr_i','OG1'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.44,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('tyr','CZ'),('rthr_i','CA'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.40,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('tyr','CZ'),('rthr_i','CB'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.40,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('tyr','CZ'),('rthr_i','OG1'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.05,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('tyr','OH'),('rthr_i','CA'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.86,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('tyr','OH'),('rthr_i','CB'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.66,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('tyr','OH'),('rthr_i','OG1'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.50,resSelectionSubs('thr_i','OG1',subs)))
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
IDSpec[(('thr','CA'),('sarg','CZ'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.02,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NE'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.62,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CA'),('sarg','NH1'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.46,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','CZ'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.72,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NE'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.18,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','CB'),('sarg','NH1'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.06,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','CZ'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.94,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NE'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.26,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr','OG1'),('sarg','NH1'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.26,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr','CA'),('styr','CE1'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.65,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('thr','CA'),('styr','CZ'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.48,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('thr','CA'),('styr','OH'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.69,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('thr','CB'),('styr','CE1'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.43,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('thr','CB'),('styr','CZ'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.41,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('thr','CB'),('styr','OH'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.64,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('thr','OG1'),('styr','CE1'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.41,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('styr','CZ'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.47,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('styr','OH'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.59,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('thr','CA'),('rthr_i','CA'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.77,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','CA'),('rthr_i','CB'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.37,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','CA'),('rthr_i','OG1'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.38,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','CB'),('rthr_i','CA'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.81,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','CB'),('rthr_i','CB'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.20,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','CB'),('rthr_i','OG1'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.94,resSelectionSubs('thr_i','OG1',subs)))
IDSpec[(('thr','OG1'),('rthr_i','CA'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.89,resSelectionSubs('thr_i','CA',subs)))
IDSpec[(('thr','OG1'),('rthr_i','CB'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.84,resSelectionSubs('thr_i','CB',subs)))
IDSpec[(('thr','OG1'),('rthr_i','OG1'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.42,resSelectionSubs('thr_i','OG1',subs)))
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
IDSpec[(('thr_i','CA'),('sarg','CZ'))] = cmd.select('thr_i1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.60,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sarg','NE'))] = cmd.select('thr_i2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.92,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sarg','NH1'))] = cmd.select('thr_i3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.82,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sarg','CZ'))] = cmd.select('thr_i4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.24,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sarg','NE'))] = cmd.select('thr_i5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.41,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sarg','NH1'))] = cmd.select('thr_i6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.57,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sarg','CZ'))] = cmd.select('thr_i7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.77,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sarg','NE'))] = cmd.select('thr_i8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.52,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sarg','NH1'))] = cmd.select('thr_i9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.29,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('thr_i','CA'),('styr','CE1'))] = cmd.select('thr_i10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.77,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('thr_i','CA'),('styr','CZ'))] = cmd.select('thr_i11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.40,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('thr_i','CA'),('styr','OH'))] = cmd.select('thr_i12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.86,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('thr_i','CB'),('styr','CE1'))] = cmd.select('thr_i13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.76,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('thr_i','CB'),('styr','CZ'))] = cmd.select('thr_i14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.40,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('thr_i','CB'),('styr','OH'))] = cmd.select('thr_i15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.66,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('styr','CE1'))] = cmd.select('thr_i16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.44,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('styr','CZ'))] = cmd.select('thr_i17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.05,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('styr','OH'))] = cmd.select('thr_i18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.50,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','CA'))] = cmd.select('thr_i19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+5.77,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','CB'))] = cmd.select('thr_i20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.81,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CA'),('sthr','OG1'))] = cmd.select('thr_i21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.89,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CA'))] = cmd.select('thr_i22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.37,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','CB'))] = cmd.select('thr_i23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.20,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','CB'),('sthr','OG1'))] = cmd.select('thr_i24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.84,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CA'))] = cmd.select('thr_i25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.38,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','CB'))] = cmd.select('thr_i26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.94,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('thr_i','OG1'),('sthr','OG1'))] = cmd.select('thr_i27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.42,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['thr_i'] = cmd.select('thr_i',' br. thr_i1&br. thr_i2&br. thr_i3&br. thr_i4&br. thr_i5&br. thr_i6&br. thr_i7&br. thr_i8&br. thr_i9&br. thr_i10&br. thr_i11&br. thr_i12&br. thr_i13&br. thr_i14&br. thr_i15&br. thr_i16&br. thr_i17&br. thr_i18&br. thr_i19&br. thr_i20&br. thr_i21&br. thr_i22&br. thr_i23&br. thr_i24&br. thr_i25&br. thr_i26&br. thr_i27')
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
IDSpec['S_1o5k_4_2_1_52'] = cmd.select('S_1o5k_4_2_1_52', 'arg|tyr|thr|thr_i')
cmd.delete('arg')
cmd.delete('tyr')
cmd.delete('thr')
cmd.delete('thr_i')
