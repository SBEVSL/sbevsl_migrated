'''
FUNC:S_2ix6_1_3_3_6
PDB:2ix6
EC:1.3.3.6
RESI:ser,gln,glu
LOCI:a-287,294,408;
'''
IDSpec[(('ser','CA'),('rglu','CD'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CA'),('rglu','OE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.36,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CA'),('rglu','OE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.50,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CB'),('rglu','CD'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.15,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','CB'),('rglu','OE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.44,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','CB'),('rglu','OE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.62,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','OG'),('rglu','CD'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.24,resSelectionSubs('glu','CD',subs)))
IDSpec[(('ser','OG'),('rglu','OE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.26,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('ser','OG'),('rglu','OE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.10,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('ser','CA'),('rgln','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.69,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CA'),('rgln','NE2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.52,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CA'),('rgln','OE1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.02,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','CB'),('rgln','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.13,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CB'),('rgln','NE2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.86,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CB'),('rgln','OE1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.37,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','OG'),('rgln','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.13,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','OG'),('rgln','NE2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.80,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','OG'),('rgln','OE1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.32,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('glu','CD'),('sser','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.92,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.15,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sser','OG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.24,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.36,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.44,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sser','OG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.26,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.50,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.62,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sser','OG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.10,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.05,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.28,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.46,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.77,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.03,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.03,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.09,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.37,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.51,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sser','CA'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.69,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CB'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.13,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','OG'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.13,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CA'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.52,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CB'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.86,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','OG'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.80,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CA'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+12.02,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CB'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+12.37,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','OG'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.32,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','CD'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.05,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.77,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.09,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','CD'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.28,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.03,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.37,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','CD'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.46,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.03,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+12.51,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_2ix6_1_3_3_6'] = cmd.select('S_2ix6_1_3_3_6', 'ser|glu|gln')
cmd.delete('ser')
cmd.delete('glu')
cmd.delete('gln')
