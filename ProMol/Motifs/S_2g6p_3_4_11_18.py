'''
FUNC:S_2g6p_3_4_11_18
PDB:2g6p
EC:3.4.11.18
RESI:asn,glu
LOCI:a-314,336;
'''
IDSpec[(('asn','CG'),('rglu','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.08,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','CG'),('rglu','OE1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.85,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','CG'),('rglu','OE2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.62,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','ND2'),('rglu','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.72,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','ND2'),('rglu','OE1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.61,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','ND2'),('rglu','OE2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+13.24,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asn','OD1'),('rglu','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.18,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asn','OD1'),('rglu','OE1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.97,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asn','OD1'),('rglu','OE2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.64,resSelectionSubs('glu','OE2',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
IDSpec[(('glu','CD'),('sasn','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.08,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','ND2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.72,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','CD'),('sasn','OD1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.18,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.85,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','ND2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.61,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasn','OD1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.97,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.62,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','ND2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.24,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasn','OD1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.64,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_2g6p_3_4_11_18'] = cmd.select('S_2g6p_3_4_11_18', 'asn|glu')
cmd.delete('asn')
cmd.delete('glu')