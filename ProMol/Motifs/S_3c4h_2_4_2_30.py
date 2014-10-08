'''
FUNC:S_3c4h_2_4_2_30
PDB:3c4h
EC:2.4.2.30
RESI:tyr,glu
LOCI:a-425,514;
'''
IDSpec[(('glu','CD'),('rtyr','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.36,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','CD'),('rtyr','CZ'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.33,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','CD'),('rtyr','OH'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.43,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE1'),('rtyr','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.45,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE1'),('rtyr','CZ'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.60,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE1'),('rtyr','OH'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.75,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('glu','OE2'),('rtyr','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.83,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('glu','OE2'),('rtyr','CZ'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.74,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('glu','OE2'),('rtyr','OH'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.68,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('sglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.36,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.45,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.83,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.60,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.74,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.43,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.75,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.68,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9')
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
IDSpec['S_3c4h_2_4_2_30'] = cmd.select('S_3c4h_2_4_2_30', 'glu|tyr')
cmd.delete('glu')
cmd.delete('tyr')
