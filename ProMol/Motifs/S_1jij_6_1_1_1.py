'''
FUNC:S_1jij_6_1_1_1
PDB:1jij
EC:6.1.1.1
RESI:lys,arg,lys,lys
LOCI:a-84,88,231,234;
'''
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.41,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.53,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.97,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.15,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.98,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.11,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.21,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.94,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.70,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.97,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.54,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+19.07,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.66,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.34,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.95,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.83,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.62,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.31,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CD'),('rarg','CZ'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+21.02,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CD'),('rarg','NE'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+20.88,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CD'),('rarg','NH1'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+20.58,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','CE'),('rarg','CZ'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.85,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','CE'),('rarg','NE'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.63,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','CE'),('rarg','NH1'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+21.48,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys','NZ'),('rarg','CZ'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+21.14,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys','NZ'),('rarg','NE'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+20.83,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys','NZ'),('rarg','NH1'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+20.84,resSelectionSubs('arg','NH1',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
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
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.41,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.15,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.21,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.53,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.98,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.94,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.97,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.11,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.70,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rlys','CD'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.33,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys_i','CD'),('rlys','CE'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.76,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys_i','CD'),('rlys','NZ'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.48,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys_i','CE'),('rlys','CD'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.00,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys_i','CE'),('rlys','CE'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.46,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys_i','CE'),('rlys','NZ'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.27,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys_i','NZ'),('rlys','CD'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.71,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys_i','NZ'),('rlys','CE'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.30,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys_i','NZ'),('rlys','NZ'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.22,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys_i','CD'),('rarg','CZ'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.56,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_i','CD'),('rarg','NE'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.52,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_i','CD'),('rarg','NH1'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.28,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys_i','CE'),('rarg','CZ'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.01,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_i','CE'),('rarg','NE'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.97,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_i','CE'),('rarg','NH1'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.84,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys_i','NZ'),('rarg','CZ'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.86,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_i','NZ'),('rarg','NE'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.70,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_i','NZ'),('rarg','NH1'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.78,resSelectionSubs('arg','NH1',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27')
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
cmd.delete('lys_i19')
cmd.delete('lys_i20')
cmd.delete('lys_i21')
cmd.delete('lys_i22')
cmd.delete('lys_i23')
cmd.delete('lys_i24')
cmd.delete('lys_i25')
cmd.delete('lys_i26')
cmd.delete('lys_i27')
IDSpec[(('lys_ii','CD'),('slys','CD'))] = cmd.select('lys_ii1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.97,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','CE'))] = cmd.select('lys_ii2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+19.66,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys','NZ'))] = cmd.select('lys_ii3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.83,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CD'))] = cmd.select('lys_ii4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.54,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','CE'))] = cmd.select('lys_ii5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys','NZ'))] = cmd.select('lys_ii6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CD'))] = cmd.select('lys_ii7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','CE'))] = cmd.select('lys_ii8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.95,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys','NZ'))] = cmd.select('lys_ii9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.31,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CD'))] = cmd.select('lys_ii10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.33,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','CE'))] = cmd.select('lys_ii11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.00,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('slys_i','NZ'))] = cmd.select('lys_ii12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.71,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CD'))] = cmd.select('lys_ii13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+16.76,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','CE'))] = cmd.select('lys_ii14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.46,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','CE'),('slys_i','NZ'))] = cmd.select('lys_ii15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.30,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CD'))] = cmd.select('lys_ii16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.48,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','CE'))] = cmd.select('lys_ii17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.27,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('lys_ii','NZ'),('slys_i','NZ'))] = cmd.select('lys_ii18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.22,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('lys_ii','CD'),('rarg','CZ'))] = cmd.select('lys_ii19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.26,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_ii','CD'),('rarg','NE'))] = cmd.select('lys_ii20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.50,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_ii','CD'),('rarg','NH1'))] = cmd.select('lys_ii21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.07,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys_ii','CE'),('rarg','CZ'))] = cmd.select('lys_ii22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.65,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_ii','CE'),('rarg','NE'))] = cmd.select('lys_ii23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.36,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_ii','CE'),('rarg','NH1'))] = cmd.select('lys_ii24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.09,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('lys_ii','NZ'),('rarg','CZ'))] = cmd.select('lys_ii25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.18,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('lys_ii','NZ'),('rarg','NE'))] = cmd.select('lys_ii26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.21,resSelectionSubs('arg','NE',subs)))
IDSpec[(('lys_ii','NZ'),('rarg','NH1'))] = cmd.select('lys_ii27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.22,resSelectionSubs('arg','NH1',subs)))
IDSpec['lys_ii'] = cmd.select('lys_ii',' br. lys_ii1&br. lys_ii2&br. lys_ii3&br. lys_ii4&br. lys_ii5&br. lys_ii6&br. lys_ii7&br. lys_ii8&br. lys_ii9&br. lys_ii10&br. lys_ii11&br. lys_ii12&br. lys_ii13&br. lys_ii14&br. lys_ii15&br. lys_ii16&br. lys_ii17&br. lys_ii18&br. lys_ii19&br. lys_ii20&br. lys_ii21&br. lys_ii22&br. lys_ii23&br. lys_ii24&br. lys_ii25&br. lys_ii26&br. lys_ii27')
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
cmd.delete('lys_ii19')
cmd.delete('lys_ii20')
cmd.delete('lys_ii21')
cmd.delete('lys_ii22')
cmd.delete('lys_ii23')
cmd.delete('lys_ii24')
cmd.delete('lys_ii25')
cmd.delete('lys_ii26')
cmd.delete('lys_ii27')
IDSpec[(('arg','CZ'),('slys','CD'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.02,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','CE'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.85,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys','NZ'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+21.14,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CD'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+20.88,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','CE'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+21.63,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys','NZ'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+20.83,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CD'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+20.58,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','CE'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+21.48,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys','NZ'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+20.84,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_i','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.56,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_i','CE'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+19.01,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_i','NZ'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.86,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_i','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.52,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_i','CE'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.97,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_i','NZ'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+18.70,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_i','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.28,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_i','CE'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.84,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_i','NZ'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.78,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_ii','CD'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.26,resSelectionSubs('lys_ii','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_ii','CE'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.65,resSelectionSubs('lys_ii','CE',subs,selection=True)))
IDSpec[(('arg','CZ'),('slys_ii','NZ'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.18,resSelectionSubs('lys_ii','NZ',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_ii','CD'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.50,resSelectionSubs('lys_ii','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_ii','CE'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.36,resSelectionSubs('lys_ii','CE',subs,selection=True)))
IDSpec[(('arg','NE'),('slys_ii','NZ'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+6.21,resSelectionSubs('lys_ii','NZ',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_ii','CD'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.07,resSelectionSubs('lys_ii','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_ii','CE'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.09,resSelectionSubs('lys_ii','CE',subs,selection=True)))
IDSpec[(('arg','NH1'),('slys_ii','NZ'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+5.22,resSelectionSubs('lys_ii','NZ',subs,selection=True)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
IDSpec['S_1jij_6_1_1_1'] = cmd.select('S_1jij_6_1_1_1', 'lys|lys_i|lys_ii|arg')
cmd.delete('lys')
cmd.delete('lys_i')
cmd.delete('lys_ii')
cmd.delete('arg')
