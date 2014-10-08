'''
FUNC:S_1zi4_2_4_1_40
PDB:1zi4
EC:2.4.1.40
RESI:trp,glu
LOCI:a-300,303;
'''
IDSpec[(('glu','CD'),('rtrp','CE2'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.40,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','CD'),('rtrp','CZ2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.26,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','CD'),('rtrp','NE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.53,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE1'),('rtrp','CE2'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.16,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE1'),('rtrp','CZ2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.85,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE1'),('rtrp','NE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.44,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('glu','OE2'),('rtrp','CE2'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.30,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('glu','OE2'),('rtrp','CZ2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.17,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('glu','OE2'),('rtrp','NE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.37,resSelectionSubs('trp','NE1',subs)))
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
IDSpec[(('trp','CE2'),('sglu','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.40,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.16,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CE2'),('sglu','OE2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.30,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.26,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.85,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sglu','OE2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.17,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.53,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.44,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sglu','OE2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.37,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9')
IDSpec['r_trp'] = cmd.count_atoms(resSelectionSubs('trp', subs=subs, selection=True))
cmd.delete('trp1')
cmd.delete('trp2')
cmd.delete('trp3')
cmd.delete('trp4')
cmd.delete('trp5')
cmd.delete('trp6')
cmd.delete('trp7')
cmd.delete('trp8')
cmd.delete('trp9')
IDSpec['S_1zi4_2_4_1_40'] = cmd.select('S_1zi4_2_4_1_40', 'glu|trp')
cmd.delete('glu')
cmd.delete('trp')
