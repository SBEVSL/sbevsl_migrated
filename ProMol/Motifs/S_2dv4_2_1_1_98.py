'''
FUNC:S_2dv4_2_1_1_98
PDB:2dv4
EC:2.1.1.98
RESI:glu,lys,met
LOCI:a-33,53,176;
'''
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+21.07,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+21.93,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+22.97,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+21.62,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+22.55,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.60,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+21.49,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+22.28,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+23.34,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','CD'),('rmet','CE'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+20.69,resSelectionSubs('met','CE',subs)))
IDSpec[(('glu','CD'),('rmet','CG'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+20.55,resSelectionSubs('met','CG',subs)))
IDSpec[(('glu','CD'),('rmet','SD'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+20.55,resSelectionSubs('met','SD',subs)))
IDSpec[(('glu','OE1'),('rmet','CE'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+19.85,resSelectionSubs('met','CE',subs)))
IDSpec[(('glu','OE1'),('rmet','CG'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+19.69,resSelectionSubs('met','CG',subs)))
IDSpec[(('glu','OE1'),('rmet','SD'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+19.76,resSelectionSubs('met','SD',subs)))
IDSpec[(('glu','OE2'),('rmet','CE'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+20.48,resSelectionSubs('met','CE',subs)))
IDSpec[(('glu','OE2'),('rmet','CG'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+20.32,resSelectionSubs('met','CG',subs)))
IDSpec[(('glu','OE2'),('rmet','SD'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+20.25,resSelectionSubs('met','SD',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.62,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.49,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.93,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+22.55,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+22.28,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+22.97,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.60,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.34,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CD'),('rmet','CE'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+38.61,resSelectionSubs('met','CE',subs)))
IDSpec[(('lys','CD'),('rmet','CG'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+37.74,resSelectionSubs('met','CG',subs)))
IDSpec[(('lys','CD'),('rmet','SD'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+38.23,resSelectionSubs('met','SD',subs)))
IDSpec[(('lys','CE'),('rmet','CE'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+39.58,resSelectionSubs('met','CE',subs)))
IDSpec[(('lys','CE'),('rmet','CG'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+38.70,resSelectionSubs('met','CG',subs)))
IDSpec[(('lys','CE'),('rmet','SD'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+39.16,resSelectionSubs('met','SD',subs)))
IDSpec[(('lys','NZ'),('rmet','CE'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+40.79,resSelectionSubs('met','CE',subs)))
IDSpec[(('lys','NZ'),('rmet','CG'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+39.97,resSelectionSubs('met','CG',subs)))
IDSpec[(('lys','NZ'),('rmet','SD'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+40.41,resSelectionSubs('met','SD',subs)))
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
IDSpec[(('met','CE'),('sglu','CD'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+20.69,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('met','CE'),('sglu','OE1'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+19.85,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('met','CE'),('sglu','OE2'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+20.48,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('met','CG'),('sglu','CD'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+20.55,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('met','CG'),('sglu','OE1'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+19.69,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('met','CG'),('sglu','OE2'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+20.32,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('met','SD'),('sglu','CD'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+20.55,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('met','SD'),('sglu','OE1'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+19.76,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('met','SD'),('sglu','OE2'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+20.25,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('met','CE'),('slys','CD'))] = cmd.select('met10', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+38.61,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('met','CE'),('slys','CE'))] = cmd.select('met11', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+39.58,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('met','CE'),('slys','NZ'))] = cmd.select('met12', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+40.79,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('met','CG'),('slys','CD'))] = cmd.select('met13', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+37.74,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('met','CG'),('slys','CE'))] = cmd.select('met14', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+38.70,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('met','CG'),('slys','NZ'))] = cmd.select('met15', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+39.97,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('met','SD'),('slys','CD'))] = cmd.select('met16', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+38.23,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('met','SD'),('slys','CE'))] = cmd.select('met17', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+39.16,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('met','SD'),('slys','NZ'))] = cmd.select('met18', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+40.41,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2dv4_2_1_1_98'] = cmd.select('S_2dv4_2_1_1_98', 'glu|lys|met')
cmd.delete('glu')
cmd.delete('lys')
cmd.delete('met')
