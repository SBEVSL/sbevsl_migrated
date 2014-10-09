'''
FUNC:S_2f61_3_2_1_45
PDB:2f61
EC:3.2.1.45
RESI:glu,glu,cys
LOCI:a-235,340,342;
'''
IDSpec[(('cys','CA'),('rglu','CD'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.48,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CA'),('rglu','OE1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+9.66,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CA'),('rglu','OE2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.10,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CB'),('rglu','CD'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.72,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CB'),('rglu','OE1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+8.85,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CB'),('rglu','OE2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.21,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','SG'),('rglu','CD'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.21,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','SG'),('rglu','OE1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.37,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','SG'),('rglu','OE2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.37,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CA'),('rglu','CD'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.45,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CA'),('rglu','OE1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.37,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CA'),('rglu','OE2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.07,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','CB'),('rglu','CD'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.68,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','CB'),('rglu','OE1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.45,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','CB'),('rglu','OE2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.40,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('cys','SG'),('rglu','CD'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.27,resSelectionSubs('glu','CD',subs)))
IDSpec[(('cys','SG'),('rglu','OE1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10.06,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('cys','SG'),('rglu','OE2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.89,resSelectionSubs('glu','OE2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
IDSpec[(('glu','CD'),('scys','CA'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.48,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','CD'),('scys','CB'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.72,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','CD'),('scys','SG'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.21,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','CA'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.66,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','CB'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.85,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','OE1'),('scys','SG'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.37,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','CA'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.10,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','CB'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.21,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu','OE2'),('scys','SG'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.37,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu','CD'),('rglu','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.46,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','CD'),('rglu','OE1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.23,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','CD'),('rglu','OE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.80,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.35,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE1'),('rglu','OE1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.01,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu','OE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.94,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.01,resSelectionSubs('glu','CD',subs)))
IDSpec[(('glu','OE2'),('rglu','OE1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.72,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu','OE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.18,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu_i','CD'),('scys','CA'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.45,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu_i','CD'),('scys','CB'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.68,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu_i','CD'),('scys','SG'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.27,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('scys','CA'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.37,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('scys','CB'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.45,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('scys','SG'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.06,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('scys','CA'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.07,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('scys','CB'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.40,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('scys','SG'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.89,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.46,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.35,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.23,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.01,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.72,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.80,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.94,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.18,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_2f61_3_2_1_45'] = cmd.select('S_2f61_3_2_1_45', 'cys|glu|glu_i')
cmd.delete('cys')
cmd.delete('glu')
cmd.delete('glu_i')
