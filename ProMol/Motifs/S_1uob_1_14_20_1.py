'''
FUNC:S_1uob_1_14_20_1
PDB:1uob
EC:1.14.20.1
RESI:arg,arg,tyr,met
LOCI:a-74,160,163,180;
'''
IDSpec[(('met','CE'),('rtyr','CE1'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+17.48,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('met','CE'),('rtyr','CZ'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+17.62,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('met','CE'),('rtyr','OH'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+18.56,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('met','CG'),('rtyr','CE1'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+18.38,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('met','CG'),('rtyr','CZ'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+18.50,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('met','CG'),('rtyr','OH'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+19.29,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('met','SD'),('rtyr','CE1'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+17.77,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('met','SD'),('rtyr','CZ'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+18.00,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('met','SD'),('rtyr','OH'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+18.89,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('met','CE'),('rarg','CZ'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+20.86,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CE'),('rarg','NE'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+19.78,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CE'),('rarg','NH1'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+21.44,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','CG'),('rarg','CZ'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+23.46,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CG'),('rarg','NE'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+22.37,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CG'),('rarg','NH1'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+24.09,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','SD'),('rarg','CZ'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+22.08,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','SD'),('rarg','NE'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+21.04,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','SD'),('rarg','NH1'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+22.70,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','CE'),('rarg_i','CZ'))] = cmd.select('met19', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+10.23,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('met','CE'),('rarg_i','NE'))] = cmd.select('met20', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+10.67,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('met','CE'),('rarg_i','NH1'))] = cmd.select('met21', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.01,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('met','CG'),('rarg_i','CZ'))] = cmd.select('met22', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+12.92,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('met','CG'),('rarg_i','NE'))] = cmd.select('met23', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+13.40,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('met','CG'),('rarg_i','NH1'))] = cmd.select('met24', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.65,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('met','SD'),('rarg_i','CZ'))] = cmd.select('met25', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+11.62,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('met','SD'),('rarg_i','NE'))] = cmd.select('met26', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+12.00,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('met','SD'),('rarg_i','NH1'))] = cmd.select('met27', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+10.36,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('tyr','CE1'),('smet','CE'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+17.48,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('smet','CG'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+18.38,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('smet','SD'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+17.77,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('smet','CE'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+17.62,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('smet','CG'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.50,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('smet','SD'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.00,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('tyr','OH'),('smet','CE'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+18.56,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('tyr','OH'),('smet','CG'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+19.29,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('smet','SD'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+18.89,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rarg','CZ'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+27.58,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CE1'),('rarg','NE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+26.97,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CE1'),('rarg','NH1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+27.34,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CZ'),('rarg','CZ'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+27.88,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','CZ'),('rarg','NE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+27.23,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','CZ'),('rarg','NH1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+27.63,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','OH'),('rarg','CZ'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+29.21,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('tyr','OH'),('rarg','NE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+28.55,resSelectionSubs('arg','NE',subs)))
IDSpec[(('tyr','OH'),('rarg','NH1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+28.96,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('tyr','CE1'),('rarg_i','CZ'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.75,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('tyr','CE1'),('rarg_i','NE'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+18.91,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('tyr','CE1'),('rarg_i','NH1'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.64,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('tyr','CZ'),('rarg_i','CZ'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.96,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('tyr','CZ'),('rarg_i','NE'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.16,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('tyr','CZ'),('rarg_i','NH1'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.85,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('tyr','OH'),('rarg_i','CZ'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+21.21,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('tyr','OH'),('rarg_i','NE'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+20.44,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('tyr','OH'),('rarg_i','NH1'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+21.07,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('arg','CZ'),('smet','CE'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+20.86,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','CG'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+23.46,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','SD'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+22.08,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CE'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+19.78,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CG'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+22.37,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','SD'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.04,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CE'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.44,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CG'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+24.09,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','SD'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+22.70,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CE1'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.58,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','CZ'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+27.88,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('styr','OH'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+29.21,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CE1'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+26.97,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','CZ'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+27.23,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NE'),('styr','OH'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+28.55,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CE1'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+27.34,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','CZ'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+27.63,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('styr','OH'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+28.96,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg','CZ'),('rarg_i','CZ'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.71,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NE'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.54,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NH1'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.87,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NE'),('rarg_i','CZ'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.63,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NE'),('rarg_i','NE'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.55,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NE'),('rarg_i','NH1'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.78,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg_i','CZ'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.24,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NE'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.95,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NH1'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.46,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('arg_i','CZ'),('smet','CE'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.23,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('smet','CG'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.92,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('smet','SD'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.62,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg_i','NE'),('smet','CE'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.67,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('smet','CG'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.40,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg_i','NE'),('smet','SD'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.00,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('smet','CE'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.01,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('smet','CG'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.65,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('smet','SD'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.36,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('styr','CE1'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+19.75,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('styr','CZ'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+19.96,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('styr','OH'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.21,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg_i','NE'),('styr','CE1'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.91,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('styr','CZ'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+19.16,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('styr','OH'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+20.44,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('styr','CE1'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.64,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('styr','CZ'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.85,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('styr','OH'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.07,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.71,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.63,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.24,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.54,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.55,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.95,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.87,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.78,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.46,resSelectionSubs('arg','NH1',subs,selection=True)))
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
IDSpec['S_1uob_1_14_20_1'] = cmd.select('S_1uob_1_14_20_1', 'met|tyr|arg|arg_i')
cmd.delete('met')
cmd.delete('tyr')
cmd.delete('arg')
cmd.delete('arg_i')
