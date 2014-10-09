'''
FUNC:S_1qv7_1_1_1_1
PDB:1qv7
EC:1.1.1.1
RESI:ser,gln,leu
LOCI:a-48,51,57;
'''
IDSpec[(('leu','CD1'),('rser','CA'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.76,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD1'),('rser','CB'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.39,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD1'),('rser','OG'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.40,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CD2'),('rser','CA'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.48,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD2'),('rser','CB'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.12,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD2'),('rser','OG'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.51,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CG'),('rser','CA'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.78,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CG'),('rser','CB'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.61,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CG'),('rser','OG'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.91,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CD1'),('rgln','CD'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.23,resSelectionSubs('gln','CD',subs)))
IDSpec[(('leu','CD1'),('rgln','NE2'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.80,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('leu','CD1'),('rgln','OE1'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.65,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('leu','CD2'),('rgln','CD'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.47,resSelectionSubs('gln','CD',subs)))
IDSpec[(('leu','CD2'),('rgln','NE2'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.60,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('leu','CD2'),('rgln','OE1'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.76,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('leu','CG'),('rgln','CD'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.76,resSelectionSubs('gln','CD',subs)))
IDSpec[(('leu','CG'),('rgln','NE2'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.54,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('leu','CG'),('rgln','OE1'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.28,resSelectionSubs('gln','OE1',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
IDSpec[(('ser','CA'),('sleu','CD1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.76,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CD2'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.48,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CG'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.78,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.39,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD2'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.12,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CG'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.61,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.40,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD2'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.51,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CG'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.91,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('rgln','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.62,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CA'),('rgln','NE2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.72,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CA'),('rgln','OE1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.35,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','CB'),('rgln','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.47,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CB'),('rgln','NE2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.42,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CB'),('rgln','OE1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.04,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','OG'),('rgln','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.17,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','OG'),('rgln','NE2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.08,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','OG'),('rgln','OE1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.50,resSelectionSubs('gln','OE1',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
IDSpec[(('gln','CD'),('sleu','CD1'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+8.23,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('gln','CD'),('sleu','CD2'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.47,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('gln','CD'),('sleu','CG'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.76,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sleu','CD1'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.80,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sleu','CD2'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.60,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sleu','CG'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.54,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sleu','CD1'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.65,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sleu','CD2'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.76,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sleu','CG'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.28,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.62,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CB'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.47,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','OG'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.17,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.72,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CB'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.42,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','OG'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.08,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.35,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CB'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.04,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','OG'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.50,resSelectionSubs('ser','OG',subs,selection=True)))
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
IDSpec['S_1qv7_1_1_1_1'] = cmd.select('S_1qv7_1_1_1_1', 'leu|ser|gln')
cmd.delete('leu')
cmd.delete('ser')
cmd.delete('gln')