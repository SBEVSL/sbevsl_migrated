'''
FUNC:S_2jio_1_7_99_4
PDB:2jio
EC:1.7.99.4
RESI:arg,cys,met
LOCI:a-138,140,141;
'''
IDSpec[(('cys','CA'),('rmet','CE'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.39,resSelectionSubs('met','CE',subs)))
IDSpec[(('cys','CA'),('rmet','CG'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.72,resSelectionSubs('met','CG',subs)))
IDSpec[(('cys','CA'),('rmet','SD'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.95,resSelectionSubs('met','SD',subs)))
IDSpec[(('cys','CB'),('rmet','CE'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.28,resSelectionSubs('met','CE',subs)))
IDSpec[(('cys','CB'),('rmet','CG'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.19,resSelectionSubs('met','CG',subs)))
IDSpec[(('cys','CB'),('rmet','SD'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.66,resSelectionSubs('met','SD',subs)))
IDSpec[(('cys','SG'),('rmet','CE'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.52,resSelectionSubs('met','CE',subs)))
IDSpec[(('cys','SG'),('rmet','CG'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.86,resSelectionSubs('met','CG',subs)))
IDSpec[(('cys','SG'),('rmet','SD'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.76,resSelectionSubs('met','SD',subs)))
IDSpec[(('cys','CA'),('rarg','CZ'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.85,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','CA'),('rarg','NE'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10.82,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','CA'),('rarg','NH1'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.76,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','CB'),('rarg','CZ'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.38,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','CB'),('rarg','NE'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.40,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','CB'),('rarg','NH1'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+13.15,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('cys','SG'),('rarg','CZ'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.02,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('cys','SG'),('rarg','NE'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+13.09,resSelectionSubs('arg','NE',subs)))
IDSpec[(('cys','SG'),('rarg','NH1'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+14.81,resSelectionSubs('arg','NH1',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18')
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
IDSpec[(('met','CE'),('scys','CA'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.39,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('met','CE'),('scys','CB'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.28,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('met','CE'),('scys','SG'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+7.52,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('met','CG'),('scys','CA'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+6.72,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('met','CG'),('scys','CB'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+6.19,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('met','CG'),('scys','SG'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+5.86,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('met','SD'),('scys','CA'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.95,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('met','SD'),('scys','CB'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.66,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('met','SD'),('scys','SG'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+5.76,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('met','CE'),('rarg','CZ'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+14.74,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CE'),('rarg','NE'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+14.25,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CE'),('rarg','NH1'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+15.59,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','CG'),('rarg','CZ'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+13.07,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','CG'),('rarg','NE'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+12.50,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','CG'),('rarg','NH1'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+13.79,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('met','SD'),('rarg','CZ'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+14.35,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('met','SD'),('rarg','NE'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+13.72,resSelectionSubs('arg','NE',subs)))
IDSpec[(('met','SD'),('rarg','NH1'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+15.18,resSelectionSubs('arg','NH1',subs)))
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
IDSpec[(('arg','CZ'),('scys','CA'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.85,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('scys','CB'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.38,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('scys','SG'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.02,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','CA'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.82,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','CB'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.40,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('scys','SG'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.09,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','CA'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.76,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','CB'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.15,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('scys','SG'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.81,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','CE'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.74,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','CG'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.07,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('smet','SD'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.35,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CE'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.25,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','CG'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.50,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('smet','SD'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+13.72,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CE'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.59,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','CG'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.79,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('smet','SD'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+15.18,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18')
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
IDSpec['S_2jio_1_7_99_4'] = cmd.select('S_2jio_1_7_99_4', 'cys|met|arg')
cmd.delete('cys')
cmd.delete('met')
cmd.delete('arg')
