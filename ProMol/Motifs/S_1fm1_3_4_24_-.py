'''
FUNC:S_1fm1_3_4_24_-
PDB:1fm1
EC:3.4.24.-
RESI:glu,met
LOCI:a-120,137;
'''
IDSpec[(('glu','CD'),('rmet','CE'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.18,resSelectionSubs('met','CE',subs)))
IDSpec[(('glu','CD'),('rmet','CG'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.17,resSelectionSubs('met','CG',subs)))
IDSpec[(('glu','CD'),('rmet','SD'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.51,resSelectionSubs('met','SD',subs)))
IDSpec[(('glu','OE1'),('rmet','CE'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.48,resSelectionSubs('met','CE',subs)))
IDSpec[(('glu','OE1'),('rmet','CG'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.57,resSelectionSubs('met','CG',subs)))
IDSpec[(('glu','OE1'),('rmet','SD'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.90,resSelectionSubs('met','SD',subs)))
IDSpec[(('glu','OE2'),('rmet','CE'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.07,resSelectionSubs('met','CE',subs)))
IDSpec[(('glu','OE2'),('rmet','CG'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.94,resSelectionSubs('met','CG',subs)))
IDSpec[(('glu','OE2'),('rmet','SD'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.32,resSelectionSubs('met','SD',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9')
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
IDSpec[(('met','CE'),('sglu','CD'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+13.18,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('met','CE'),('sglu','OE1'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+13.48,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('met','CE'),('sglu','OE2'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+14.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('met','CG'),('sglu','CD'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+14.17,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('met','CG'),('sglu','OE1'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+14.57,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('met','CG'),('sglu','OE2'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+14.94,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('met','SD'),('sglu','CD'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+12.51,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('met','SD'),('sglu','OE1'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+12.90,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('met','SD'),('sglu','OE2'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+13.32,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['met'] = cmd.select('met',' br. met1&br. met2&br. met3&br. met4&br. met5&br. met6&br. met7&br. met8&br. met9')
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
IDSpec['S_1fm1_3_4_24_-'] = cmd.select('S_1fm1_3_4_24_-', 'glu|met')
cmd.delete('glu')
cmd.delete('met')