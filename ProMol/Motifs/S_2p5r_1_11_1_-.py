'''
FUNC:S_2p5r_1_11_1_-
PDB:2p5r
EC:1.11.1.-
RESI:glu,trp
LOCI:a-79,133;
'''
IDSpec[(('trp','CE2'),('rglu','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+15.08,resSelectionSubs('glu','CD',subs)))
IDSpec[(('trp','CE2'),('rglu','OE1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+15.50,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('trp','CE2'),('rglu','OE2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+15.76,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('trp','CZ2'),('rglu','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.75,resSelectionSubs('glu','CD',subs)))
IDSpec[(('trp','CZ2'),('rglu','OE1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.19,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('trp','CZ2'),('rglu','OE2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+14.45,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('trp','NE1'),('rglu','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+15.95,resSelectionSubs('glu','CD',subs)))
IDSpec[(('trp','NE1'),('rglu','OE1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+16.44,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('trp','NE1'),('rglu','OE2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+16.55,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('strp','CE2'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.08,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('glu','CD'),('strp','CZ2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.75,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('glu','CD'),('strp','NE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.95,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('strp','CE2'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.50,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('glu','OE1'),('strp','CZ2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.19,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('glu','OE1'),('strp','NE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.44,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('strp','CE2'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.76,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('glu','OE2'),('strp','CZ2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.45,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('glu','OE2'),('strp','NE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.55,resSelectionSubs('trp','NE1',subs,selection=True)))
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
IDSpec['S_2p5r_1_11_1_-'] = cmd.select('S_2p5r_1_11_1_-', 'trp|glu')
cmd.delete('trp')
cmd.delete('glu')