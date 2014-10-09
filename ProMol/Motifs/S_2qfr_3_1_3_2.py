'''
FUNC:S_2qfr_3_1_3_2
PDB:2qfr
EC:3.1.3.2
RESI:his,his,his
LOCI:a-202,295,296;
'''
IDSpec[(('his','CE1'),('rhis','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','CE1'),('rhis','ND1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.21,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','CE1'),('rhis','NE2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.31,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','ND1'),('rhis','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.57,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','ND1'),('rhis','ND1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.42,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','ND1'),('rhis','NE2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.56,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','NE2'),('rhis','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.12,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','NE2'),('rhis','ND1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.05,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','NE2'),('rhis','NE2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.03,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','CE1'),('rhis','CE1'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.01,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','CE1'),('rhis','ND1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.60,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','CE1'),('rhis','NE2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.58,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','ND1'),('rhis','CE1'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.73,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','ND1'),('rhis','ND1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','ND1'),('rhis','NE2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.19,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his','NE2'),('rhis','CE1'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.24,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his','NE2'),('rhis','ND1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.69,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his','NE2'),('rhis','NE2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.25,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his_i','CE1'),('shis','CE1'))] = cmd.select('his_i1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.31,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','ND1'))] = cmd.select('his_i2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.57,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','CE1'),('shis','NE2'))] = cmd.select('his_i3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.12,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','CE1'))] = cmd.select('his_i4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.21,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','ND1'))] = cmd.select('his_i5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.42,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','ND1'),('shis','NE2'))] = cmd.select('his_i6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.05,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','CE1'))] = cmd.select('his_i7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.31,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','ND1'))] = cmd.select('his_i8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.56,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_i','NE2'),('shis','NE2'))] = cmd.select('his_i9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.03,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_i','CE1'),('rhis','CE1'))] = cmd.select('his_i10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his_i','CE1'),('rhis','ND1'))] = cmd.select('his_i11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.79,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his_i','CE1'),('rhis','NE2'))] = cmd.select('his_i12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.09,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his_i','ND1'),('rhis','CE1'))] = cmd.select('his_i13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.88,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his_i','ND1'),('rhis','ND1'))] = cmd.select('his_i14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.93,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his_i','ND1'),('rhis','NE2'))] = cmd.select('his_i15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.28,resSelectionSubs('his','NE2',subs)))
IDSpec[(('his_i','NE2'),('rhis','CE1'))] = cmd.select('his_i16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.79,resSelectionSubs('his','CE1',subs)))
IDSpec[(('his_i','NE2'),('rhis','ND1'))] = cmd.select('his_i17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.81,resSelectionSubs('his','ND1',subs)))
IDSpec[(('his_i','NE2'),('rhis','NE2'))] = cmd.select('his_i18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.25,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his_ii','CE1'),('shis','CE1'))] = cmd.select('his_ii1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.01,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_ii','CE1'),('shis','ND1'))] = cmd.select('his_ii2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.73,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_ii','CE1'),('shis','NE2'))] = cmd.select('his_ii3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.24,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_ii','ND1'),('shis','CE1'))] = cmd.select('his_ii4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.60,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_ii','ND1'),('shis','ND1'))] = cmd.select('his_ii5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.03,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_ii','ND1'),('shis','NE2'))] = cmd.select('his_ii6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.69,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_ii','NE2'),('shis','CE1'))] = cmd.select('his_ii7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.58,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('his_ii','NE2'),('shis','ND1'))] = cmd.select('his_ii8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.19,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('his_ii','NE2'),('shis','NE2'))] = cmd.select('his_ii9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.25,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('his_ii','CE1'),('shis_i','CE1'))] = cmd.select('his_ii10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.70,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('his_ii','CE1'),('shis_i','ND1'))] = cmd.select('his_ii11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.88,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('his_ii','CE1'),('shis_i','NE2'))] = cmd.select('his_ii12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.79,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('his_ii','ND1'),('shis_i','CE1'))] = cmd.select('his_ii13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.79,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('his_ii','ND1'),('shis_i','ND1'))] = cmd.select('his_ii14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.93,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('his_ii','ND1'),('shis_i','NE2'))] = cmd.select('his_ii15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.81,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec[(('his_ii','NE2'),('shis_i','CE1'))] = cmd.select('his_ii16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.09,resSelectionSubs('his_i','CE1',subs,selection=True)))
IDSpec[(('his_ii','NE2'),('shis_i','ND1'))] = cmd.select('his_ii17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.28,resSelectionSubs('his_i','ND1',subs,selection=True)))
IDSpec[(('his_ii','NE2'),('shis_i','NE2'))] = cmd.select('his_ii18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.25,resSelectionSubs('his_i','NE2',subs,selection=True)))
IDSpec['his_ii'] = cmd.select('his_ii',' br. his_ii1&br. his_ii2&br. his_ii3&br. his_ii4&br. his_ii5&br. his_ii6&br. his_ii7&br. his_ii8&br. his_ii9&br. his_ii10&br. his_ii11&br. his_ii12&br. his_ii13&br. his_ii14&br. his_ii15&br. his_ii16&br. his_ii17&br. his_ii18')
IDSpec['r_his_ii'] = cmd.count_atoms(resSelectionSubs('his_ii', subs=subs, selection=True))
cmd.delete('his_ii1')
cmd.delete('his_ii2')
cmd.delete('his_ii3')
cmd.delete('his_ii4')
cmd.delete('his_ii5')
cmd.delete('his_ii6')
cmd.delete('his_ii7')
cmd.delete('his_ii8')
cmd.delete('his_ii9')
cmd.delete('his_ii10')
cmd.delete('his_ii11')
cmd.delete('his_ii12')
cmd.delete('his_ii13')
cmd.delete('his_ii14')
cmd.delete('his_ii15')
cmd.delete('his_ii16')
cmd.delete('his_ii17')
cmd.delete('his_ii18')
IDSpec['S_2qfr_3_1_3_2'] = cmd.select('S_2qfr_3_1_3_2', 'his|his_i|his_ii')
cmd.delete('his')
cmd.delete('his_i')
cmd.delete('his_ii')
