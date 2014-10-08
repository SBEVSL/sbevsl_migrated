'''
FUNC:S_1b7b_2_7_2_2
PDB:1b7b
EC:2.7.2.2
RESI:lys,lys,lys
LOCI:a-128,209,271;
'''
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.51,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.02,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.71,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.31,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.65,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.31,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.02,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.25,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.15,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rlys_ii','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.42,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','CD'),('rlys_ii','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.07,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','CD'),('rlys_ii','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.03,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_ii','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.59,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','CE'),('rlys_ii','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.34,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','CE'),('rlys_ii','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.22,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.38,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.25,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_ii','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.13,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.51,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.31,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.02,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.02,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.65,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.25,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.71,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.31,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.15,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rlys_ii','CD'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.21,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','CE'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.68,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','CD'),('rlys_ii','NZ'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.98,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','CD'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.76,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','CE'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.18,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','CE'),('rlys_ii','NZ'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.29,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','CD'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.47,resSelectionSubs('lys_ii','CD',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','CE'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.70,resSelectionSubs('lys_ii','CE',subs)))
IDSpec[(('lys_i','NZ'),('rlys_ii','NZ'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.73,resSelectionSubs('lys_ii','NZ',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18')
IDSpec['r_lys_i'] = cmd.count_atoms(resSelectionSubs('lys_i', subs=subs, selection=True))
cmd.delete('lys_i1')
cmd.delete('lys_i2')
cmd.delete('lys_i3')
cmd.delete('lys_i4')
cmd.delete('lys_i5')
cmd.delete('lys_i6')
cmd.delete('lys_i7')
cmd.delete('lys_i8')
cmd.delete('lys_i9')
cmd.delete('lys_i10')
cmd.delete('lys_i11')
cmd.delete('lys_i12')
cmd.delete('lys_i13')
cmd.delete('lys_i14')
cmd.delete('lys_i15')
cmd.delete('lys_i16')
cmd.delete('lys_i17')
cmd.delete('lys_i18')
IDSpec[(('lys_ii','CD'),('slys','CD'))] = cmd.select('lys_ii1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.42,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','CE'))] = cmd.select('lys_ii2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.59,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','NZ'))] = cmd.select('lys_ii3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.38,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CD'))] = cmd.select('lys_ii4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CE'))] = cmd.select('lys_ii5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','NZ'))] = cmd.select('lys_ii6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.25,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CD'))] = cmd.select('lys_ii7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.03,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CE'))] = cmd.select('lys_ii8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.22,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','NZ'))] = cmd.select('lys_ii9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.13,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CD'))] = cmd.select('lys_ii10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+13.21,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CE'))] = cmd.select('lys_ii11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.76,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','NZ'))] = cmd.select('lys_ii12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.47,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CD'))] = cmd.select('lys_ii13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.68,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CE'))] = cmd.select('lys_ii14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.18,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','NZ'))] = cmd.select('lys_ii15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.70,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CD'))] = cmd.select('lys_ii16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.98,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CE'))] = cmd.select('lys_ii17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+12.29,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','NZ'))] = cmd.select('lys_ii18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+11.73,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec['lys_ii'] = cmd.select('lys_ii',' br. lys_ii1&br. lys_ii2&br. lys_ii3&br. lys_ii4&br. lys_ii5&br. lys_ii6&br. lys_ii7&br. lys_ii8&br. lys_ii9&br. lys_ii10&br. lys_ii11&br. lys_ii12&br. lys_ii13&br. lys_ii14&br. lys_ii15&br. lys_ii16&br. lys_ii17&br. lys_ii18')
IDSpec['r_lys_ii'] = cmd.count_atoms(resSelectionSubs('lys_ii', subs=subs, selection=True))
cmd.delete('lys_ii1')
cmd.delete('lys_ii2')
cmd.delete('lys_ii3')
cmd.delete('lys_ii4')
cmd.delete('lys_ii5')
cmd.delete('lys_ii6')
cmd.delete('lys_ii7')
cmd.delete('lys_ii8')
cmd.delete('lys_ii9')
cmd.delete('lys_ii10')
cmd.delete('lys_ii11')
cmd.delete('lys_ii12')
cmd.delete('lys_ii13')
cmd.delete('lys_ii14')
cmd.delete('lys_ii15')
cmd.delete('lys_ii16')
cmd.delete('lys_ii17')
cmd.delete('lys_ii18')
IDSpec['S_1b7b_2_7_2_2'] = cmd.select('S_1b7b_2_7_2_2', 'lys|lys_i|lys_ii')
cmd.delete('lys')
cmd.delete('lys_i')
cmd.delete('lys_ii')