'''
FUNC:S_3g77_3_5_4_1
PDB:3g77
EC:3.5.4.1
RESI:gln,glu
LOCI:a-156,217;
'''
IDSpec[(('gln','CD'),('rglu','CD'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.81,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gln','CD'),('rglu','OE1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.18,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gln','CD'),('rglu','OE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.72,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gln','NE2'),('rglu','CD'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.01,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gln','NE2'),('rglu','OE1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.51,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gln','NE2'),('rglu','OE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.90,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('gln','OE1'),('rglu','CD'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.53,resSelectionSubs('glu','CD',subs)))
IDSpec[(('gln','OE1'),('rglu','OE1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.75,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('gln','OE1'),('rglu','OE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.49,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('sgln','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.81,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('sgln','NE2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.01,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('glu','CD'),('sgln','OE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.53,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgln','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.18,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgln','NE2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.51,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sgln','OE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.75,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgln','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.72,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgln','NE2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.90,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sgln','OE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.49,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_3g77_3_5_4_1'] = cmd.select('S_3g77_3_5_4_1', 'gln|glu')
cmd.delete('gln')
cmd.delete('glu')
