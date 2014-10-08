'''
FUNC:S_1utt_3_4_24_65
PDB:1utt
EC:3.4.24.65
RESI:glu,met
LOCI:a-219,236;
'''
IDSpec[(('met','CE'),('rglu','CD'))] = cmd.select('met1', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.19,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','CE'),('rglu','OE1'))] = cmd.select('met2', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.23,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','CE'),('rglu','OE2'))] = cmd.select('met3', '%s w. %s of %s'%(resSelectionSubs('met','CE',subs),d+9.06,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','CG'),('rglu','CD'))] = cmd.select('met4', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.63,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','CG'),('rglu','OE1'))] = cmd.select('met5', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.83,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','CG'),('rglu','OE2'))] = cmd.select('met6', '%s w. %s of %s'%(resSelectionSubs('met','CG',subs),d+11.43,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('met','SD'),('rglu','CD'))] = cmd.select('met7', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+9.94,resSelectionSubs('glu','CD',subs)))
IDSpec[(('met','SD'),('rglu','OE1'))] = cmd.select('met8', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+10.16,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('met','SD'),('rglu','OE2'))] = cmd.select('met9', '%s w. %s of %s'%(resSelectionSubs('met','SD',subs),d+9.84,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('smet','CE'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.19,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('smet','CG'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.63,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('smet','SD'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.94,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','CE'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.23,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','CG'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.83,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('smet','SD'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.16,resSelectionSubs('met','SD',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','CE'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.06,resSelectionSubs('met','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','CG'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.43,resSelectionSubs('met','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('smet','SD'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.84,resSelectionSubs('met','SD',subs,selection=True)))
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
IDSpec['S_1utt_3_4_24_65'] = cmd.select('S_1utt_3_4_24_65', 'met|glu')
cmd.delete('met')
cmd.delete('glu')
