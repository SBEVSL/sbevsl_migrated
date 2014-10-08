'''
FUNC:S_1w07_1_3_3_6
PDB:1w07
EC:1.3.3.6
RESI:val,gln,glu
LOCI:a-284,286,424;
'''
IDSpec[(('val','CA'),('rglu','CD'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.60,resSelectionSubs('glu','CD',subs)))
IDSpec[(('val','CA'),('rglu','OE1'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.48,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('val','CA'),('rglu','OE2'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+9.08,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('val','CB'),('rglu','CD'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+7.32,resSelectionSubs('glu','CD',subs)))
IDSpec[(('val','CB'),('rglu','OE1'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+7.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('val','CB'),('rglu','OE2'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+7.70,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('val','CG1'),('rglu','CD'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+6.41,resSelectionSubs('glu','CD',subs)))
IDSpec[(('val','CG1'),('rglu','OE1'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+6.07,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('val','CG1'),('rglu','OE2'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+7.05,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('val','CA'),('rgln','CD'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+9.42,resSelectionSubs('gln','CD',subs)))
IDSpec[(('val','CA'),('rgln','NE2'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+10.55,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('val','CA'),('rgln','OE1'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+8.91,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('val','CB'),('rgln','CD'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.95,resSelectionSubs('gln','CD',subs)))
IDSpec[(('val','CB'),('rgln','NE2'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+12.07,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('val','CB'),('rgln','OE1'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.45,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('val','CG1'),('rgln','CD'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+11.60,resSelectionSubs('gln','CD',subs)))
IDSpec[(('val','CG1'),('rgln','NE2'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+12.62,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('val','CG1'),('rgln','OE1'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+11.09,resSelectionSubs('gln','OE1',subs)))
IDSpec['val'] = cmd.select('val',' br. val1&br. val2&br. val3&br. val4&br. val5&br. val6&br. val7&br. val8&br. val9&br. val10&br. val11&br. val12&br. val13&br. val14&br. val15&br. val16&br. val17&br. val18')
IDSpec['r_val'] = cmd.count_atoms(resSelectionSubs('val', subs=subs, selection=True))
cmd.delete('val1')
cmd.delete('val2')
cmd.delete('val3')
cmd.delete('val4')
cmd.delete('val5')
cmd.delete('val6')
cmd.delete('val7')
cmd.delete('val8')
cmd.delete('val9')
cmd.delete('val10')
cmd.delete('val11')
cmd.delete('val12')
cmd.delete('val13')
cmd.delete('val14')
cmd.delete('val15')
cmd.delete('val16')
cmd.delete('val17')
cmd.delete('val18')
IDSpec[(('glu','CD'),('sval','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.60,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('sval','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.32,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('sval','CG1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.41,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sval','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.48,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('sval','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.20,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('sval','CG1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.07,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sval','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.08,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('sval','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.70,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('sval','CG1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.05,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.35,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.26,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+15.06,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+15.32,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.23,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+14.94,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.00,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.96,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.72,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sval','CA'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.42,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sval','CB'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+10.95,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sval','CG1'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.60,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sval','CA'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+10.55,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sval','CB'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.07,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sval','CG1'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.62,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sval','CA'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.91,resSelectionSubs('val','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sval','CB'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.45,resSelectionSubs('val','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sval','CG1'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+11.09,resSelectionSubs('val','CG1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','CD'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.35,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.32,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.00,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','CD'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.26,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.23,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.96,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','CD'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+15.06,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.94,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+15.72,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_1w07_1_3_3_6'] = cmd.select('S_1w07_1_3_3_6', 'val|glu|gln')
cmd.delete('val')
cmd.delete('glu')
cmd.delete('gln')
