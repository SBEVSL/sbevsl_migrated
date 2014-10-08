'''
FUNC:S_1c24_3_4_11_18
PDB:1c24
EC:3.4.11.18
RESI:gln,glu
LOCI:a-182,204;
'''
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.27,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.72,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.53,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.97,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.45,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.12,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.80,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.35,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.08,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sglu','CD'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.27,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.97,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.80,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','CD'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+13.72,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+14.45,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+13.35,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','CD'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.53,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.12,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.08,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1c24_3_4_11_18'] = cmd.select('S_1c24_3_4_11_18', 'glu|gln')
cmd.delete('glu')
cmd.delete('gln')
