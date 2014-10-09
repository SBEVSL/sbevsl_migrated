'''
FUNC:S_2p4u_3_1_3_2
PDB:2p4u
EC:3.1.3.2
RESI:cys,cys,arg,asp
LOCI:a-13,18,19,130;
'''
IDSpec[(('cys','CA'),('rarg','CZ'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.00,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','CA'),('rarg','NE'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.16,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','CA'),('rarg','NH1'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.78,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','CB'),('rarg','CZ'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.06,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','CB'),('rarg','NE'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.91,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','CB'),('rarg','NH1'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.00,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','SG'),('rarg','CZ'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.12,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','SG'),('rarg','NE'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.64,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','SG'),('rarg','NH1'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.28,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','CA'),('rcys','CA'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.13,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CA'),('rcys','CB'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.45,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CA'),('rcys','SG'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.51,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CB'),('rcys','CA'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.75,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CB'),('rcys','CB'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.03,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CB'),('rcys','SG'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.19,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','SG'),('rcys','CA'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.42,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','SG'),('rcys','CB'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.96,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','SG'),('rcys','SG'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.05,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CA'),('rasp','CG'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.26,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CA'),('rasp','OD1'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.31,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CA'),('rasp','OD2'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.42,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CB'),('rasp','CG'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.27,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CB'),('rasp','OD1'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.16,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CB'),('rasp','OD2'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','SG'),('rasp','CG'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.41,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','SG'),('rasp','OD1'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.05,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','SG'),('rasp','OD2'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.71,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('arg','CZ'),('scys','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.00,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('scys','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.06,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('scys','SG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.12,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.16,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.91,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','SG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.64,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.78,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.00,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','SG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.28,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','CZ'),('rcys','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.33,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','CZ'),('rcys','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.75,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','CZ'),('rcys','SG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.71,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NE'),('rcys','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.18,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NE'),('rcys','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.64,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NE'),('rcys','SG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.78,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NH1'),('rcys','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.48,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NH1'),('rcys','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.84,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NH1'),('rcys','SG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.83,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.34,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.61,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.97,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.44,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.34,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.27,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.99,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.42,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.65,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.13,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.75,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.42,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.45,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.03,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.96,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.51,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.19,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.05,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sarg','CZ'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.33,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sarg','NE'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.18,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_i','CA'),('sarg','NH1'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.48,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sarg','CZ'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.75,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sarg','NE'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.64,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_i','CB'),('sarg','NH1'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+9.84,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sarg','CZ'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.71,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sarg','NE'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.78,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys_i','SG'),('sarg','NH1'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.83,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rasp','CG'))] = cmd.select('cys_i19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.21,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys_i','CA'),('rasp','OD1'))] = cmd.select('cys_i20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.09,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys_i','CA'),('rasp','OD2'))] = cmd.select('cys_i21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.89,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys_i','CB'),('rasp','CG'))] = cmd.select('cys_i22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.98,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys_i','CB'),('rasp','OD1'))] = cmd.select('cys_i23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.79,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys_i','CB'),('rasp','OD2'))] = cmd.select('cys_i24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.73,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys_i','SG'),('rasp','CG'))] = cmd.select('cys_i25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.89,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys_i','SG'),('rasp','OD1'))] = cmd.select('cys_i26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.69,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys_i','SG'),('rasp','OD2'))] = cmd.select('cys_i27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.42,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('scys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.26,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.27,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.41,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.31,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.16,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.05,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.42,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.60,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.71,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.34,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.44,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.99,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.61,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.34,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.42,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.97,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.27,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.65,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','CG'),('scys_i','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.21,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys_i','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.98,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys_i','SG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.89,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys_i','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.09,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys_i','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.79,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys_i','SG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.69,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys_i','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.89,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys_i','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.73,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys_i','SG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.42,resSelectionSubs('cys_i','SG',subs,selection=True)))
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
IDSpec['S_2p4u_3_1_3_2'] = cmd.select('S_2p4u_3_1_3_2', 'cys|arg|cys_i|asp')
cmd.delete('cys')
cmd.delete('arg')
cmd.delete('cys_i')
cmd.delete('asp')