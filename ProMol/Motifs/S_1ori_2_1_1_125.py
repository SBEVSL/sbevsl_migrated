'''
FUNC:S_1ori_2_1_1_125
PDB:1ori
EC:2.1.1.125
RESI:thr,glu,glu
LOCI:a-57,144,153;
'''
IDSpec[(('glu','CD'),('rglu','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.47,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','CD'),('rglu','OE1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.58,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','CD'),('rglu','OE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.67,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.41,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE1'),('rglu','OE1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.47,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu','OE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.60,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.64,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE2'),('rglu','OE1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.78,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu','OE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.86,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','CD'),('rthr','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.53,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','CD'),('rthr','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.86,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','CD'),('rthr','OG1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.63,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE1'),('rthr','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.37,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE1'),('rthr','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.72,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE1'),('rthr','OG1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.45,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE2'),('rthr','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.23,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE2'),('rthr','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.43,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE2'),('rthr','OG1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.14,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.47,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.41,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.64,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.58,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.47,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.78,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.67,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.60,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.86,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('rthr','CA'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.40,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu_i','CD'),('rthr','CB'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+23.44,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu_i','CD'),('rthr','OG1'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+23.77,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu_i','OE1'),('rthr','CA'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.37,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu_i','OE1'),('rthr','CB'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+22.40,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu_i','OE1'),('rthr','OG1'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+22.70,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu_i','OE2'),('rthr','CA'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+25.56,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu_i','OE2'),('rthr','CB'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.60,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu_i','OE2'),('rthr','OG1'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.91,resSelectionSubs('thr','OG1',subs)))
IDSpec['glu_i'] = cmd.select('glu_i',' br. glu_i1&br. glu_i2&br. glu_i3&br. glu_i4&br. glu_i5&br. glu_i6&br. glu_i7&br. glu_i8&br. glu_i9&br. glu_i10&br. glu_i11&br. glu_i12&br. glu_i13&br. glu_i14&br. glu_i15&br. glu_i16&br. glu_i17&br. glu_i18')
IDSpec['r_glu_i'] = cmd.count_atoms(resSelectionSubs('glu_i', subs=subs, selection=True))
cmd.delete('glu_i1')
cmd.delete('glu_i2')
cmd.delete('glu_i3')
cmd.delete('glu_i4')
cmd.delete('glu_i5')
cmd.delete('glu_i6')
cmd.delete('glu_i7')
cmd.delete('glu_i8')
cmd.delete('glu_i9')
cmd.delete('glu_i10')
cmd.delete('glu_i11')
cmd.delete('glu_i12')
cmd.delete('glu_i13')
cmd.delete('glu_i14')
cmd.delete('glu_i15')
cmd.delete('glu_i16')
cmd.delete('glu_i17')
cmd.delete('glu_i18')
IDSpec[(('thr','CA'),('sglu','CD'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.53,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.37,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.23,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','CD'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.86,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.72,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.43,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','CD'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.63,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.45,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.14,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu_i','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+24.40,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu_i','OE1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+23.37,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu_i','OE2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+25.56,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu_i','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+23.44,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu_i','OE1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+22.40,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu_i','OE2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+24.60,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu_i','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+23.77,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu_i','OE1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+22.70,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu_i','OE2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+24.91,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
IDSpec['S_1ori_2_1_1_125'] = cmd.select('S_1ori_2_1_1_125', 'glu|glu_i|thr')
cmd.delete('glu')
cmd.delete('glu_i')
cmd.delete('thr')
