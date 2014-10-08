'''
FUNC:S_2bgd_3_1_3_48
PDB:2bgd
EC:3.1.3.48
RESI:asp,cys,arg,ser
LOCI:a-181,215,221,222;
'''
IDSpec[(('arg','CZ'),('rasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.22,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','CZ'),('rasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.21,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','CZ'),('rasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.60,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NE'),('rasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.99,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NE'),('rasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.92,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NE'),('rasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.46,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','NH1'),('rasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.16,resSelectionSubs('asp','CG',subs)))
IDSpec[(('arg','NH1'),('rasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.31,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('arg','NH1'),('rasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.24,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('arg','CZ'),('rcys','CA'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.11,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','CZ'),('rcys','CB'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.12,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','CZ'),('rcys','SG'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+7.11,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NE'),('rcys','CA'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.07,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NE'),('rcys','CB'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.79,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NE'),('rcys','SG'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.50,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','NH1'),('rcys','CA'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.84,resSelectionSubs('cys','CA',subs)))
IDSpec[(('arg','NH1'),('rcys','CB'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.04,resSelectionSubs('cys','CB',subs)))
IDSpec[(('arg','NH1'),('rcys','SG'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+8.24,resSelectionSubs('cys','SG',subs)))
IDSpec[(('arg','CZ'),('rser','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.13,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','CZ'),('rser','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.36,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','CZ'),('rser','OG'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.57,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NE'),('rser','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.09,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NE'),('rser','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.48,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NE'),('rser','OG'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.85,resSelectionSubs('ser','OG',subs)))
IDSpec[(('arg','NH1'),('rser','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.03,resSelectionSubs('ser','CA',subs)))
IDSpec[(('arg','NH1'),('rser','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.35,resSelectionSubs('ser','CB',subs)))
IDSpec[(('arg','NH1'),('rser','OG'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.50,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('asp','CG'),('sarg','CZ'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.22,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.99,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','CG'),('sarg','NH1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.16,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','CZ'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.21,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.92,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD1'),('sarg','NH1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.31,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','CZ'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.60,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.46,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('asp','OD2'),('sarg','NH1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.24,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('asp','CG'),('rcys','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.77,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','CG'),('rcys','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.93,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','CG'),('rcys','SG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.48,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD1'),('rcys','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.52,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD1'),('rcys','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.69,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD1'),('rcys','SG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.08,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','OD2'),('rcys','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.28,resSelectionSubs('cys','CA',subs)))
IDSpec[(('asp','OD2'),('rcys','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.51,resSelectionSubs('cys','CB',subs)))
IDSpec[(('asp','OD2'),('rcys','SG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.24,resSelectionSubs('cys','SG',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.79,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.97,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.32,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.58,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.98,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.70,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.99,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('cys','CA'),('sarg','CZ'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.11,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys','CA'),('sarg','NE'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.07,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys','CA'),('sarg','NH1'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.84,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys','CB'),('sarg','CZ'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.12,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys','CB'),('sarg','NE'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.79,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys','CB'),('sarg','NH1'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.04,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys','SG'),('sarg','CZ'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.11,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('cys','SG'),('sarg','NE'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.50,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('cys','SG'),('sarg','NH1'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.24,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.77,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.52,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CA'),('sasp','OD2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.93,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.69,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','CB'),('sasp','OD2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.51,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.48,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.08,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('cys','SG'),('sasp','OD2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('cys','CA'),('rser','CA'))] = cmd.select('cys19', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.81,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CA'),('rser','CB'))] = cmd.select('cys20', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.25,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CA'),('rser','OG'))] = cmd.select('cys21', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.91,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','CB'),('rser','CA'))] = cmd.select('cys22', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.08,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','CB'),('rser','CB'))] = cmd.select('cys23', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.80,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','CB'),('rser','OG'))] = cmd.select('cys24', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.70,resSelectionSubs('ser','OG',subs)))
IDSpec[(('cys','SG'),('rser','CA'))] = cmd.select('cys25', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.16,resSelectionSubs('ser','CA',subs)))
IDSpec[(('cys','SG'),('rser','CB'))] = cmd.select('cys26', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.71,resSelectionSubs('ser','CB',subs)))
IDSpec[(('cys','SG'),('rser','OG'))] = cmd.select('cys27', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.96,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('sarg','CZ'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.13,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NE'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.09,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CA'),('sarg','NH1'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.03,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','CZ'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.36,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NE'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.48,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','CB'),('sarg','NH1'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.35,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','CZ'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.57,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NE'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.85,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('ser','OG'),('sarg','NH1'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.50,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.46,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.46,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+14.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.58,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.70,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+14.32,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+14.98,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+14.99,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.81,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.08,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CA'),('scys','SG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.16,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.25,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.80,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','CB'),('scys','SG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.71,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.91,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.70,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('ser','OG'),('scys','SG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.96,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
IDSpec['S_2bgd_3_1_3_48'] = cmd.select('S_2bgd_3_1_3_48', 'arg|asp|cys|ser')
cmd.delete('arg')
cmd.delete('asp')
cmd.delete('cys')
cmd.delete('ser')
