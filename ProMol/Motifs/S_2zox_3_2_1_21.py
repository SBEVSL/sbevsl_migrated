'''
FUNC:S_2zox_3_2_1_21
PDB:2zox
EC:3.2.1.21
RESI:gln,gln,glu
LOCI:a-165,307,373;
'''
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.04,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.69,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.01,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.18,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.56,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.31,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.16,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.98,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.02,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.76,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.24,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.76,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.73,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.07,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.57,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.12,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.34,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.51,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sglu','CD'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.04,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.18,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.16,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','CD'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.69,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.56,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.98,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','CD'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.01,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.31,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.02,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','CD'),('rgln','CD'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.50,resSelectionSubs('gln','CD',subs)))
IDSpec[(('gln','CD'),('rgln','NE2'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+5.42,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('gln','CD'),('rgln','OE1'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.99,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('gln','NE2'),('rgln','CD'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.71,resSelectionSubs('gln','CD',subs)))
IDSpec[(('gln','NE2'),('rgln','NE2'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.69,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('gln','NE2'),('rgln','OE1'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.07,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('gln','OE1'),('rgln','CD'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.84,resSelectionSubs('gln','CD',subs)))
IDSpec[(('gln','OE1'),('rgln','NE2'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+4.92,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('gln','OE1'),('rgln','OE1'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.45,resSelectionSubs('gln','OE1',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
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
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec[(('gln_i','CD'),('sglu','CD'))] = cmd.select('gln_i1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+5.76,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln_i','CD'),('sglu','OE1'))] = cmd.select('gln_i2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.73,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln_i','CD'),('sglu','OE2'))] = cmd.select('gln_i3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+5.12,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln_i','NE2'),('sglu','CD'))] = cmd.select('gln_i4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.24,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln_i','NE2'),('sglu','OE1'))] = cmd.select('gln_i5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.07,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln_i','NE2'),('sglu','OE2'))] = cmd.select('gln_i6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.34,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln_i','OE1'),('sglu','CD'))] = cmd.select('gln_i7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.76,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln_i','OE1'),('sglu','OE1'))] = cmd.select('gln_i8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.57,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln_i','OE1'),('sglu','OE2'))] = cmd.select('gln_i9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.51,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln_i','CD'),('sgln','CD'))] = cmd.select('gln_i10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.50,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('gln_i','CD'),('sgln','NE2'))] = cmd.select('gln_i11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.71,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('gln_i','CD'),('sgln','OE1'))] = cmd.select('gln_i12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+5.84,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('gln_i','NE2'),('sgln','CD'))] = cmd.select('gln_i13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.42,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('gln_i','NE2'),('sgln','NE2'))] = cmd.select('gln_i14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.69,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('gln_i','NE2'),('sgln','OE1'))] = cmd.select('gln_i15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+4.92,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('gln_i','OE1'),('sgln','CD'))] = cmd.select('gln_i16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.99,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('gln_i','OE1'),('sgln','NE2'))] = cmd.select('gln_i17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.07,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('gln_i','OE1'),('sgln','OE1'))] = cmd.select('gln_i18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.45,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec['gln_i'] = cmd.select('gln_i',' br. gln_i1&br. gln_i2&br. gln_i3&br. gln_i4&br. gln_i5&br. gln_i6&br. gln_i7&br. gln_i8&br. gln_i9&br. gln_i10&br. gln_i11&br. gln_i12&br. gln_i13&br. gln_i14&br. gln_i15&br. gln_i16&br. gln_i17&br. gln_i18')
IDSpec['r_gln_i'] = cmd.count_atoms(resSelectionSubs('gln_i', subs=subs, selection=True))
cmd.delete('gln_i1')
cmd.delete('gln_i2')
cmd.delete('gln_i3')
cmd.delete('gln_i4')
cmd.delete('gln_i5')
cmd.delete('gln_i6')
cmd.delete('gln_i7')
cmd.delete('gln_i8')
cmd.delete('gln_i9')
cmd.delete('gln_i10')
cmd.delete('gln_i11')
cmd.delete('gln_i12')
cmd.delete('gln_i13')
cmd.delete('gln_i14')
cmd.delete('gln_i15')
cmd.delete('gln_i16')
cmd.delete('gln_i17')
cmd.delete('gln_i18')
IDSpec['S_2zox_3_2_1_21'] = cmd.select('S_2zox_3_2_1_21', 'glu|gln|gln_i')
cmd.delete('glu')
cmd.delete('gln')
cmd.delete('gln_i')
