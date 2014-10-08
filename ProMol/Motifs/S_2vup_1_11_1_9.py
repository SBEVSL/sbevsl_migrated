'''
FUNC:S_2vup_1_11_1_9
PDB:2vup
EC:1.11.1.9
RESI:gln,trp
LOCI:a-74,129;
'''
IDSpec[(('gln','CD'),('rtrp','CE2'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.90,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('gln','CD'),('rtrp','CZ2'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.20,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('gln','CD'),('rtrp','NE1'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.02,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('gln','NE2'),('rtrp','CE2'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.02,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('gln','NE2'),('rtrp','CZ2'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.04,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('gln','NE2'),('rtrp','NE1'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.31,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('gln','OE1'),('rtrp','CE2'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.08,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('gln','OE1'),('rtrp','CZ2'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.69,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('gln','OE1'),('rtrp','NE1'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.99,resSelectionSubs('trp','NE1',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
IDSpec[(('trp','CE2'),('sgln','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+6.90,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('sgln','NE2'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.02,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('trp','CE2'),('sgln','OE1'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+6.08,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sgln','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.20,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sgln','NE2'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.04,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sgln','OE1'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+5.69,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('sgln','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.02,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('sgln','NE2'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.31,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('sgln','OE1'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+5.99,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_2vup_1_11_1_9'] = cmd.select('S_2vup_1_11_1_9', 'gln|trp')
cmd.delete('gln')
cmd.delete('trp')
