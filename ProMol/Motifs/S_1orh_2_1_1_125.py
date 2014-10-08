'''
FUNC:S_1orh_2_1_1_125
PDB:1orh
EC:2.1.1.125
RESI:thr,glu,gln
LOCI:a-57,144,153;
'''
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.93,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.02,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.38,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.98,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+17.09,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.37,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.81,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.93,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.24,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','CD'),('rthr','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.72,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','CD'),('rthr','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.07,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','CD'),('rthr','OG1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.88,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE1'),('rthr','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.50,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE1'),('rthr','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.82,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE1'),('rthr','OG1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.63,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE2'),('rthr','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.64,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE2'),('rthr','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.88,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE2'),('rthr','OG1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.61,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('gln','CD'),('sglu','CD'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+14.93,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.98,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.81,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','CD'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.02,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+17.09,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+14.93,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','CD'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.38,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+15.37,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.24,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','CD'),('rthr','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+25.12,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gln','CD'),('rthr','CB'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+24.18,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gln','CD'),('rthr','OG1'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+24.59,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gln','NE2'),('rthr','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+26.27,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gln','NE2'),('rthr','CB'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+25.36,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gln','NE2'),('rthr','OG1'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+25.77,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('gln','OE1'),('rthr','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+24.36,resSelectionSubs('thr','CA',subs)))
IDSpec[(('gln','OE1'),('rthr','CB'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+23.40,resSelectionSubs('thr','CB',subs)))
IDSpec[(('gln','OE1'),('rthr','OG1'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+23.75,resSelectionSubs('thr','OG1',subs)))
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
IDSpec[(('thr','CA'),('sglu','CD'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.72,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.50,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+13.64,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','CD'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.82,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+12.88,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','CD'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.88,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.63,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+13.61,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CA'),('sgln','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+25.12,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('sgln','NE2'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+26.27,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('thr','CA'),('sgln','OE1'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+24.36,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('thr','CB'),('sgln','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+24.18,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('sgln','NE2'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+25.36,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('thr','CB'),('sgln','OE1'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+23.40,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgln','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+24.59,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgln','NE2'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+25.77,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sgln','OE1'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+23.75,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_1orh_2_1_1_125'] = cmd.select('S_1orh_2_1_1_125', 'glu|gln|thr')
cmd.delete('glu')
cmd.delete('gln')
cmd.delete('thr')
