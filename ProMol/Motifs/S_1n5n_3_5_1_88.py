'''
FUNC:S_1n5n_3_5_1_88
PDB:1n5n
EC:3.5.1.88
RESI:gly,gln,leu,glu
LOCI:a-46,51,93,135;
'''
IDSpec[(('glu','CD'),('rgln','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.30,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','CD'),('rgln','NE2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.85,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','CD'),('rgln','OE1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.23,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE1'),('rgln','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.38,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE1'),('rgln','NE2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.14,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE1'),('rgln','OE1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.29,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','OE2'),('rgln','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.30,resSelectionSubs('gln','CD',subs)))
IDSpec[(('glu','OE2'),('rgln','NE2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.57,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('glu','OE2'),('rgln','OE1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.35,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('glu','CD'),('rgly','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.02,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','CD'),('rgly','N'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.15,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','CD'),('rgly','O'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.15,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','OE1'),('rgly','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.70,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','OE1'),('rgly','N'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.86,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','OE1'),('rgly','O'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.37,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','OE2'),('rgly','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.47,resSelectionSubs('gly','CA',subs)))
IDSpec[(('glu','OE2'),('rgly','N'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.33,resSelectionSubs('gly','N',subs)))
IDSpec[(('glu','OE2'),('rgly','O'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.43,resSelectionSubs('gly','O',subs)))
IDSpec[(('glu','CD'),('rleu','CD1'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.33,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('glu','CD'),('rleu','CD2'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.87,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('glu','CD'),('rleu','CG'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.50,resSelectionSubs('leu','CG',subs)))
IDSpec[(('glu','OE1'),('rleu','CD1'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.25,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('glu','OE1'),('rleu','CD2'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.91,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('glu','OE1'),('rleu','CG'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.46,resSelectionSubs('leu','CG',subs)))
IDSpec[(('glu','OE2'),('rleu','CD1'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.50,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('glu','OE2'),('rleu','CD2'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.84,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('glu','OE2'),('rleu','CG'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.55,resSelectionSubs('leu','CG',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27')
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
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
IDSpec[(('gln','CD'),('sglu','CD'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.30,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.38,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','CD'),('sglu','OE2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.30,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','CD'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.85,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.14,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sglu','OE2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.57,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','CD'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.23,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+5.29,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sglu','OE2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.35,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gln','CD'),('rgly','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.22,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gln','CD'),('rgly','N'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.86,resSelectionSubs('gly','N',subs)))
IDSpec[(('gln','CD'),('rgly','O'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.33,resSelectionSubs('gly','O',subs)))
IDSpec[(('gln','NE2'),('rgly','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.40,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gln','NE2'),('rgly','N'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.80,resSelectionSubs('gly','N',subs)))
IDSpec[(('gln','NE2'),('rgly','O'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.31,resSelectionSubs('gly','O',subs)))
IDSpec[(('gln','OE1'),('rgly','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.21,resSelectionSubs('gly','CA',subs)))
IDSpec[(('gln','OE1'),('rgly','N'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.99,resSelectionSubs('gly','N',subs)))
IDSpec[(('gln','OE1'),('rgly','O'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+6.53,resSelectionSubs('gly','O',subs)))
IDSpec[(('gln','CD'),('rleu','CD1'))] = cmd.select('gln19', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.78,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gln','CD'),('rleu','CD2'))] = cmd.select('gln20', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.21,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gln','CD'),('rleu','CG'))] = cmd.select('gln21', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.75,resSelectionSubs('leu','CG',subs)))
IDSpec[(('gln','NE2'),('rleu','CD1'))] = cmd.select('gln22', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+7.10,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gln','NE2'),('rleu','CD2'))] = cmd.select('gln23', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+8.16,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gln','NE2'),('rleu','CG'))] = cmd.select('gln24', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.78,resSelectionSubs('leu','CG',subs)))
IDSpec[(('gln','OE1'),('rleu','CD1'))] = cmd.select('gln25', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.70,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gln','OE1'),('rleu','CD2'))] = cmd.select('gln26', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.39,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gln','OE1'),('rleu','CG'))] = cmd.select('gln27', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.87,resSelectionSubs('leu','CG',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27')
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
cmd.delete('gln19')
cmd.delete('gln20')
cmd.delete('gln21')
cmd.delete('gln22')
cmd.delete('gln23')
cmd.delete('gln24')
cmd.delete('gln25')
cmd.delete('gln26')
cmd.delete('gln27')
IDSpec[(('gly','CA'),('sglu','CD'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.02,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('sglu','OE1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+6.70,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','CA'),('sglu','OE2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+5.47,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','CD'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.15,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','OE1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.86,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','N'),('sglu','OE2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+6.33,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','CD'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.15,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','OE1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.37,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('gly','O'),('sglu','OE2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.43,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('gly','CA'),('sgln','CD'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.22,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('gly','CA'),('sgln','NE2'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.40,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('gly','CA'),('sgln','OE1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.21,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('gly','N'),('sgln','CD'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.86,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('gly','N'),('sgln','NE2'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.80,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('gly','N'),('sgln','OE1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.99,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('gly','O'),('sgln','CD'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.33,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('gly','O'),('sgln','NE2'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.31,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('gly','O'),('sgln','OE1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.53,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('gly','CA'),('rleu','CD1'))] = cmd.select('gly19', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+7.78,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gly','CA'),('rleu','CD2'))] = cmd.select('gly20', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.46,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gly','CA'),('rleu','CG'))] = cmd.select('gly21', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.45,resSelectionSubs('leu','CG',subs)))
IDSpec[(('gly','N'),('rleu','CD1'))] = cmd.select('gly22', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.31,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gly','N'),('rleu','CD2'))] = cmd.select('gly23', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.67,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gly','N'),('rleu','CG'))] = cmd.select('gly24', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.90,resSelectionSubs('leu','CG',subs)))
IDSpec[(('gly','O'),('rleu','CD1'))] = cmd.select('gly25', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+5.63,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('gly','O'),('rleu','CD2'))] = cmd.select('gly26', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+7.53,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('gly','O'),('rleu','CG'))] = cmd.select('gly27', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+6.32,resSelectionSubs('leu','CG',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18&br. gly19&br. gly20&br. gly21&br. gly22&br. gly23&br. gly24&br. gly25&br. gly26&br. gly27')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
cmd.delete('gly19')
cmd.delete('gly20')
cmd.delete('gly21')
cmd.delete('gly22')
cmd.delete('gly23')
cmd.delete('gly24')
cmd.delete('gly25')
cmd.delete('gly26')
cmd.delete('gly27')
IDSpec[(('leu','CD1'),('sglu','CD'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.33,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('leu','CD1'),('sglu','OE1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.25,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('leu','CD1'),('sglu','OE2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.50,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('leu','CD2'),('sglu','CD'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+10.87,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('leu','CD2'),('sglu','OE1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+10.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sglu','OE2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.84,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('leu','CG'),('sglu','CD'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.50,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('leu','CG'),('sglu','OE1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.46,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('leu','CG'),('sglu','OE2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.55,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgln','CD'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.78,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgln','NE2'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.10,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgln','OE1'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.70,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgln','CD'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.21,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgln','NE2'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.16,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgln','OE1'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.39,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('leu','CG'),('sgln','CD'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.75,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('leu','CG'),('sgln','NE2'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+6.78,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('leu','CG'),('sgln','OE1'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.87,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgly','CA'))] = cmd.select('leu19', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.78,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgly','N'))] = cmd.select('leu20', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.31,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('leu','CD1'),('sgly','O'))] = cmd.select('leu21', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+5.63,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgly','CA'))] = cmd.select('leu22', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.46,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgly','N'))] = cmd.select('leu23', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.67,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('leu','CD2'),('sgly','O'))] = cmd.select('leu24', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+7.53,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('leu','CG'),('sgly','CA'))] = cmd.select('leu25', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+8.45,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('leu','CG'),('sgly','N'))] = cmd.select('leu26', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.90,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('leu','CG'),('sgly','O'))] = cmd.select('leu27', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+6.32,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18&br. leu19&br. leu20&br. leu21&br. leu22&br. leu23&br. leu24&br. leu25&br. leu26&br. leu27')
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
cmd.delete('leu19')
cmd.delete('leu20')
cmd.delete('leu21')
cmd.delete('leu22')
cmd.delete('leu23')
cmd.delete('leu24')
cmd.delete('leu25')
cmd.delete('leu26')
cmd.delete('leu27')
IDSpec['S_1n5n_3_5_1_88'] = cmd.select('S_1n5n_3_5_1_88', 'glu|gln|gly|leu')
cmd.delete('glu')
cmd.delete('gln')
cmd.delete('gly')
cmd.delete('leu')
