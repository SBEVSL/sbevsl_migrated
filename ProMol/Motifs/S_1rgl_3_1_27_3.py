'''
FUNC:S_1rgl_3_1_27_3
PDB:1rgl
EC:3.1.27.3
RESI:his,glu,his
LOCI:a-40,58,92;
'''
IDSpec[(('glu','CD'),('rhis','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','CD'),('rhis','ND1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.07,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','CD'),('rhis','NE2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.74,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.00,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis','ND1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.91,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis','NE2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.02,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.18,resSelectionSubs('his','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis','ND1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.02,resSelectionSubs('his','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis','NE2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.90,resSelectionSubs('his','NE2',subs)))
IDSpec[(('glu','CD'),('rhis_i','CE1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.52,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('glu','CD'),('rhis_i','ND1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.60,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('glu','CD'),('rhis_i','NE2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.01,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('glu','OE1'),('rhis_i','CE1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.99,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('glu','OE1'),('rhis_i','ND1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.00,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('glu','OE1'),('rhis_i','NE2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.28,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('glu','OE2'),('rhis_i','CE1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.09,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('glu','OE2'),('rhis_i','ND1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.22,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('glu','OE2'),('rhis_i','NE2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.79,resSelectionSubs('his_i','NE2',subs)))
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
IDSpec[(('his','CE1'),('sglu','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.00,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sglu','OE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.18,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sglu','OE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.02,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.74,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.02,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sglu','OE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.90,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his','CE1'),('rhis_i','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.10,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','CE1'),('rhis_i','ND1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.38,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','CE1'),('rhis_i','NE2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.59,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('his','ND1'),('rhis_i','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.36,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','ND1'),('rhis_i','ND1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.63,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','ND1'),('rhis_i','NE2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.88,resSelectionSubs('his_i','NE2',subs)))
IDSpec[(('his','NE2'),('rhis_i','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.16,resSelectionSubs('his_i','CE1',subs)))
IDSpec[(('his','NE2'),('rhis_i','ND1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.42,resSelectionSubs('his_i','ND1',subs)))
IDSpec[(('his','NE2'),('rhis_i','NE2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.46,resSelectionSubs('his_i','NE2',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
IDSpec[(('his_i','CE1'),('sglu','CD'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.52,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sglu','OE1'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.99,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('sglu','OE2'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.09,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sglu','CD'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.60,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sglu','OE1'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.00,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('sglu','OE2'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.22,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sglu','CD'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.01,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sglu','OE1'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.28,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('sglu','OE2'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.79,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.10,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.36,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.16,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.38,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.63,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.42,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.59,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.88,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['his_i'] = cmd.select('his_i',' br. his_i1&br. his_i2&br. his_i3&br. his_i4&br. his_i5&br. his_i6&br. his_i7&br. his_i8&br. his_i9&br. his_i10&br. his_i11&br. his_i12&br. his_i13&br. his_i14&br. his_i15&br. his_i16&br. his_i17&br. his_i18')
IDSpec['r_his_i'] = cmd.count_atoms(resSelectionSubs('his_i', subs=subs, selection=True))
cmd.delete('his_i1')
cmd.delete('his_i2')
cmd.delete('his_i3')
cmd.delete('his_i4')
cmd.delete('his_i5')
cmd.delete('his_i6')
cmd.delete('his_i7')
cmd.delete('his_i8')
cmd.delete('his_i9')
cmd.delete('his_i10')
cmd.delete('his_i11')
cmd.delete('his_i12')
cmd.delete('his_i13')
cmd.delete('his_i14')
cmd.delete('his_i15')
cmd.delete('his_i16')
cmd.delete('his_i17')
cmd.delete('his_i18')
IDSpec['S_1rgl_3_1_27_3'] = cmd.select('S_1rgl_3_1_27_3', 'glu|his|his_i')
cmd.delete('glu')
cmd.delete('his')
cmd.delete('his_i')
