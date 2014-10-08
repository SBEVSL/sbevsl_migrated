'''
FUNC:S_2v29_4_1_2_19
PDB:2v29
EC:4.1.2.19
RESI:glu,glu,val
LOCI:a-117,171,174;
'''
IDSpec[(('glu','CD'),('rglu_i','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+29.12,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+29.75,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','CD'),('rglu_i','OE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+28.48,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE1'),('rglu_i','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+29.57,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+30.24,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE1'),('rglu_i','OE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+28.93,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','OE2'),('rglu_i','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+27.96,resSelectionSubs('glu_i','CD',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+28.58,resSelectionSubs('glu_i','OE1',subs)))
IDSpec[(('glu','OE2'),('rglu_i','OE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+27.31,resSelectionSubs('glu_i','OE2',subs)))
IDSpec[(('glu','CD'),('rval','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+30.04,resSelectionSubs('val','CA',subs)))
IDSpec[(('glu','CD'),('rval','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+31.08,resSelectionSubs('val','CB',subs)))
IDSpec[(('glu','CD'),('rval','CG1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+31.35,resSelectionSubs('val','CG1',subs)))
IDSpec[(('glu','OE1'),('rval','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+30.30,resSelectionSubs('val','CA',subs)))
IDSpec[(('glu','OE1'),('rval','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+31.38,resSelectionSubs('val','CB',subs)))
IDSpec[(('glu','OE1'),('rval','CG1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+31.69,resSelectionSubs('val','CG1',subs)))
IDSpec[(('glu','OE2'),('rval','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+29.07,resSelectionSubs('val','CA',subs)))
IDSpec[(('glu','OE2'),('rval','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+30.07,resSelectionSubs('val','CB',subs)))
IDSpec[(('glu','OE2'),('rval','CG1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+30.35,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('glu_i','CD'),('sglu','CD'))] = cmd.select('glu_i1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+29.12,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE1'))] = cmd.select('glu_i2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+29.57,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','CD'),('sglu','OE2'))] = cmd.select('glu_i3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+27.96,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','CD'))] = cmd.select('glu_i4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+29.75,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE1'))] = cmd.select('glu_i5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+30.24,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE1'),('sglu','OE2'))] = cmd.select('glu_i6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+28.58,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','CD'))] = cmd.select('glu_i7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+28.48,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE1'))] = cmd.select('glu_i8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+28.93,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('glu_i','OE2'),('sglu','OE2'))] = cmd.select('glu_i9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+27.31,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('glu_i','CD'),('rval','CA'))] = cmd.select('glu_i10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.26,resSelectionSubs('val','CA',subs)))
IDSpec[(('glu_i','CD'),('rval','CB'))] = cmd.select('glu_i11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.69,resSelectionSubs('val','CB',subs)))
IDSpec[(('glu_i','CD'),('rval','CG1'))] = cmd.select('glu_i12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.33,resSelectionSubs('val','CG1',subs)))
IDSpec[(('glu_i','OE1'),('rval','CA'))] = cmd.select('glu_i13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.57,resSelectionSubs('val','CA',subs)))
IDSpec[(('glu_i','OE1'),('rval','CB'))] = cmd.select('glu_i14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.82,resSelectionSubs('val','CB',subs)))
IDSpec[(('glu_i','OE1'),('rval','CG1'))] = cmd.select('glu_i15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.26,resSelectionSubs('val','CG1',subs)))
IDSpec[(('glu_i','OE2'),('rval','CA'))] = cmd.select('glu_i16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.16,resSelectionSubs('val','CA',subs)))
IDSpec[(('glu_i','OE2'),('rval','CB'))] = cmd.select('glu_i17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.72,resSelectionSubs('val','CB',subs)))
IDSpec[(('glu_i','OE2'),('rval','CG1'))] = cmd.select('glu_i18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.43,resSelectionSubs('val','CG1',subs)))
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
IDSpec[(('val','CA'),('sglu','CD'))] = cmd.select('val1', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+30.04,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('val','CA'),('sglu','OE1'))] = cmd.select('val2', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+30.30,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('val','CA'),('sglu','OE2'))] = cmd.select('val3', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+29.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('val','CB'),('sglu','CD'))] = cmd.select('val4', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+31.08,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('val','CB'),('sglu','OE1'))] = cmd.select('val5', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+31.38,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('val','CB'),('sglu','OE2'))] = cmd.select('val6', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+30.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('val','CG1'),('sglu','CD'))] = cmd.select('val7', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+31.35,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('val','CG1'),('sglu','OE1'))] = cmd.select('val8', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+31.69,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('val','CG1'),('sglu','OE2'))] = cmd.select('val9', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+30.35,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('val','CA'),('sglu_i','CD'))] = cmd.select('val10', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+10.26,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('val','CA'),('sglu_i','OE1'))] = cmd.select('val11', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+10.57,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('val','CA'),('sglu_i','OE2'))] = cmd.select('val12', '%s w. %s of %s'%(resSelectionSubs('val','CA',subs),d+11.16,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('val','CB'),('sglu_i','CD'))] = cmd.select('val13', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.69,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('val','CB'),('sglu_i','OE1'))] = cmd.select('val14', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+9.82,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('val','CB'),('sglu_i','OE2'))] = cmd.select('val15', '%s w. %s of %s'%(resSelectionSubs('val','CB',subs),d+10.72,resSelectionSubs('glu_i','OE2',subs,selection=True)))
IDSpec[(('val','CG1'),('sglu_i','CD'))] = cmd.select('val16', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+10.33,resSelectionSubs('glu_i','CD',subs,selection=True)))
IDSpec[(('val','CG1'),('sglu_i','OE1'))] = cmd.select('val17', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+10.26,resSelectionSubs('glu_i','OE1',subs,selection=True)))
IDSpec[(('val','CG1'),('sglu_i','OE2'))] = cmd.select('val18', '%s w. %s of %s'%(resSelectionSubs('val','CG1',subs),d+11.43,resSelectionSubs('glu_i','OE2',subs,selection=True)))
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
IDSpec['S_2v29_4_1_2_19'] = cmd.select('S_2v29_4_1_2_19', 'glu|glu_i|val')
cmd.delete('glu')
cmd.delete('glu_i')
cmd.delete('val')
