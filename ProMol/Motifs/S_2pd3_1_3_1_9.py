'''
FUNC:S_2pd3_1_3_1_9
PDB:2pd3
EC:1.3.1.9
RESI:tyr,met,lys
LOCI:a-155,158,162;
'''
IDSpec[(('tyr','CE1'),('rlys','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.83,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CE1'),('rlys','CE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.38,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CE1'),('rlys','NZ'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.65,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CZ'),('rlys','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.58,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CZ'),('rlys','CE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.31,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CZ'),('rlys','NZ'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.68,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','OH'),('rlys','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.54,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','OH'),('rlys','CE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.07,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','OH'),('rlys','NZ'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.40,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CE1'),('rmet','CE'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.09,resSelectionSubs('met','CE',subs)))
IDSpec[(('tyr','CE1'),('rmet','CG'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.53,resSelectionSubs('met','CG',subs)))
IDSpec[(('tyr','CE1'),('rmet','SD'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.26,resSelectionSubs('met','SD',subs)))
IDSpec[(('tyr','CZ'),('rmet','CE'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.90,resSelectionSubs('met','CE',subs)))
IDSpec[(('tyr','CZ'),('rmet','CG'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.14,resSelectionSubs('met','CG',subs)))
IDSpec[(('tyr','CZ'),('rmet','SD'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.72,resSelectionSubs('met','SD',subs)))
IDSpec[(('tyr','OH'),('rmet','CE'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.60,resSelectionSubs('met','CE',subs)))
IDSpec[(('tyr','OH'),('rmet','CG'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.08,resSelectionSubs('met','CG',subs)))
IDSpec[(('tyr','OH'),('rmet','SD'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.27,resSelectionSubs('met','SD',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18')
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
IDSpec[(('lys','CD'),('styr','CE1'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.83,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','CZ'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.58,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','OH'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.54,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CE1'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.38,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CZ'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.31,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','OH'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.07,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CE1'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.65,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CZ'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.68,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','OH'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.40,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CD'),('rmet','CE'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.47,resSelectionSubs('met','CE',subs)))
IDSpec[(('lys','CD'),('rmet','CG'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.28,resSelectionSubs('met','CG',subs)))
IDSpec[(('lys','CD'),('rmet','SD'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.80,resSelectionSubs('met','SD',subs)))
IDSpec[(('lys','CE'),('rmet','CE'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.84,resSelectionSubs('met','CE',subs)))
IDSpec[(('lys','CE'),('rmet','CG'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.85,resSelectionSubs('met','CG',subs)))
IDSpec[(('lys','CE'),('rmet','SD'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.34,resSelectionSubs('met','SD',subs)))
IDSpec[(('lys','NZ'),('rmet','CE'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.22,resSelectionSubs('met','CE',subs)))
IDSpec[(('lys','NZ'),('rmet','CG'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.85,resSelectionSubs('met','CG',subs)))
IDSpec[(('lys','NZ'),('rmet','SD'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.98,resSelectionSubs('met','SD',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
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
IDSpec[(('met','CE'),('styr','CE1'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.09,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('met','CE'),('styr','CZ'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+7.90,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('met','CE'),('styr','OH'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+7.60,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('met','CG'),('styr','CE1'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+5.53,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('met','CG'),('styr','CZ'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+5.14,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('met','CG'),('styr','OH'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+5.08,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('met','SD'),('styr','CE1'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+7.26,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('met','SD'),('styr','CZ'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.72,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('met','SD'),('styr','OH'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.27,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('met','CE'),('slys','CD'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.47,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('met','CE'),('slys','CE'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+7.84,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('met','CE'),('slys','NZ'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+8.22,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('met','CG'),('slys','CD'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+7.28,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('met','CG'),('slys','CE'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+6.85,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('met','CG'),('slys','NZ'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+7.85,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('met','SD'),('slys','CD'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.80,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('met','SD'),('slys','CE'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('met','SD'),('slys','NZ'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+6.98,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2pd3_1_3_1_9'] = cmd.select('S_2pd3_1_3_1_9', 'tyr|lys|met')
cmd.delete('tyr')
cmd.delete('lys')
cmd.delete('met')
