'''
FUNC:S_2zup_1_8_5_-
PDB:2zup
EC:1.8.5.-
RESI:cys,cys,arg,cys
LOCI:b-41,44,48,104;
'''
IDSpec[(('cys','CA'),('rarg','CZ'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.51,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','CA'),('rarg','NE'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.65,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','CA'),('rarg','NH1'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.37,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','CB'),('rarg','CZ'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.79,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','CB'),('rarg','NE'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.20,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','CB'),('rarg','NH1'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.64,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','SG'),('rarg','CZ'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.72,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','SG'),('rarg','NE'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.29,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','SG'),('rarg','NH1'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.70,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','CA'),('rcys','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.88,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CA'),('rcys','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+14.41,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CA'),('rcys','SG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+16.08,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CB'),('rcys','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.78,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CB'),('rcys','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.24,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CB'),('rcys','SG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+15.82,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','SG'),('rcys','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.16,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','SG'),('rcys','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.42,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','SG'),('rcys','SG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.96,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CA'),('rcys','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.00,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CA'),('rcys','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.83,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CA'),('rcys','SG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.35,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CB'),('rcys','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.95,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CB'),('rcys','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.12,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CB'),('rcys','SG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.04,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','SG'),('rcys','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.15,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','SG'),('rcys','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.97,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','SG'),('rcys','SG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.03,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('arg','CZ'),('scys','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.51,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('scys','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.79,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('scys','SG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.72,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.65,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.20,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','SG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.29,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.37,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.64,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','SG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.70,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','CZ'),('rcys','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+19.16,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','CZ'),('rcys','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+19.61,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','CZ'),('rcys','SG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.05,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NE'),('rcys','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.84,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NE'),('rcys','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+19.33,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NE'),('rcys','SG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+20.84,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NH1'),('rcys','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.72,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NH1'),('rcys','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+20.24,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NH1'),('rcys','SG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.63,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','CZ'),('rcys','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.52,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','CZ'),('rcys','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.27,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','CZ'),('rcys','SG'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.62,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NE'),('rcys','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.42,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NE'),('rcys','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.00,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NE'),('rcys','SG'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.11,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NH1'),('rcys','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.18,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NH1'),('rcys','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.08,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NH1'),('rcys','SG'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.53,resSelectionSubs('cys','SG',subs)))
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
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.88,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.78,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+13.16,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.41,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+14.24,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.42,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+16.08,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+15.82,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.96,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sarg','CZ'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+19.16,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sarg','NE'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+18.84,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sarg','NH1'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+19.72,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sarg','CZ'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+19.61,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sarg','NE'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+19.33,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sarg','NH1'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+20.24,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sarg','CZ'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.05,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sarg','NE'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+20.84,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sarg','NH1'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+21.63,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rcys','CA'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.92,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys_i','CA'),('rcys','CB'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.36,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys_i','CA'),('rcys','SG'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.33,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys_i','CB'),('rcys','CA'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.20,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys_i','CB'),('rcys','CB'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.54,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys_i','CB'),('rcys','SG'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.60,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys_i','SG'),('rcys','CA'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.57,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys_i','SG'),('rcys','CB'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.03,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys_i','SG'),('rcys','SG'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.22,resSelectionSubs('cys','SG',subs)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18&br. cys_i19&br. cys_i20&br. cys_i21&br. cys_i22&br. cys_i23&br. cys_i24&br. cys_i25&br. cys_i26&br. cys_i27')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
cmd.delete('cys_i19')
cmd.delete('cys_i20')
cmd.delete('cys_i21')
cmd.delete('cys_i22')
cmd.delete('cys_i23')
cmd.delete('cys_i24')
cmd.delete('cys_i25')
cmd.delete('cys_i26')
cmd.delete('cys_i27')
IDSpec[(('cys_ii','CA'),('scys','CA'))] = cmd.select('cys_ii1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.00,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys','CB'))] = cmd.select('cys_ii2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys','SG'))] = cmd.select('cys_ii3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.15,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys','CA'))] = cmd.select('cys_ii4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.83,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys','CB'))] = cmd.select('cys_ii5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.12,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys','SG'))] = cmd.select('cys_ii6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+4.97,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys','CA'))] = cmd.select('cys_ii7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.35,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys','CB'))] = cmd.select('cys_ii8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.04,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys','SG'))] = cmd.select('cys_ii9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.03,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sarg','CZ'))] = cmd.select('cys_ii10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.52,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sarg','NE'))] = cmd.select('cys_ii11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.42,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('sarg','NH1'))] = cmd.select('cys_ii12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.18,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sarg','CZ'))] = cmd.select('cys_ii13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.27,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sarg','NE'))] = cmd.select('cys_ii14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.00,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('sarg','NH1'))] = cmd.select('cys_ii15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.08,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sarg','CZ'))] = cmd.select('cys_ii16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.62,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sarg','NE'))] = cmd.select('cys_ii17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.11,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('sarg','NH1'))] = cmd.select('cys_ii18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.53,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys_i','CA'))] = cmd.select('cys_ii19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.92,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys_i','CB'))] = cmd.select('cys_ii20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.20,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('cys_ii','CA'),('scys_i','SG'))] = cmd.select('cys_ii21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.57,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys_i','CA'))] = cmd.select('cys_ii22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.36,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys_i','CB'))] = cmd.select('cys_ii23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.54,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('cys_ii','CB'),('scys_i','SG'))] = cmd.select('cys_ii24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.03,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys_i','CA'))] = cmd.select('cys_ii25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.33,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys_i','CB'))] = cmd.select('cys_ii26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.60,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('cys_ii','SG'),('scys_i','SG'))] = cmd.select('cys_ii27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.22,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec['cys_ii'] = cmd.select('cys_ii',' br. cys_ii1&br. cys_ii2&br. cys_ii3&br. cys_ii4&br. cys_ii5&br. cys_ii6&br. cys_ii7&br. cys_ii8&br. cys_ii9&br. cys_ii10&br. cys_ii11&br. cys_ii12&br. cys_ii13&br. cys_ii14&br. cys_ii15&br. cys_ii16&br. cys_ii17&br. cys_ii18&br. cys_ii19&br. cys_ii20&br. cys_ii21&br. cys_ii22&br. cys_ii23&br. cys_ii24&br. cys_ii25&br. cys_ii26&br. cys_ii27')
IDSpec['r_cys_ii'] = cmd.count_atoms(resSelectionSubs('cys_ii', subs=subs, selection=True))
cmd.delete('cys_ii1')
cmd.delete('cys_ii2')
cmd.delete('cys_ii3')
cmd.delete('cys_ii4')
cmd.delete('cys_ii5')
cmd.delete('cys_ii6')
cmd.delete('cys_ii7')
cmd.delete('cys_ii8')
cmd.delete('cys_ii9')
cmd.delete('cys_ii10')
cmd.delete('cys_ii11')
cmd.delete('cys_ii12')
cmd.delete('cys_ii13')
cmd.delete('cys_ii14')
cmd.delete('cys_ii15')
cmd.delete('cys_ii16')
cmd.delete('cys_ii17')
cmd.delete('cys_ii18')
cmd.delete('cys_ii19')
cmd.delete('cys_ii20')
cmd.delete('cys_ii21')
cmd.delete('cys_ii22')
cmd.delete('cys_ii23')
cmd.delete('cys_ii24')
cmd.delete('cys_ii25')
cmd.delete('cys_ii26')
cmd.delete('cys_ii27')
IDSpec['S_2zup_1_8_5_-'] = cmd.select('S_2zup_1_8_5_-', 'cys|arg|cys_i|cys_ii')
cmd.delete('cys')
cmd.delete('arg')
cmd.delete('cys_i')
cmd.delete('cys_ii')
