'''
FUNC:S_2el7_6_1_1_2
PDB:2el7
EC:6.1.1.2
RESI:lys,lys
LOCI:a-195,198;
'''
IDSpec[(('lys','CD'),('rlys','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.52,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CD'),('rlys','CE'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.78,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CD'),('rlys','NZ'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.46,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','CE'),('rlys','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.95,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','CE'),('rlys','CE'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.97,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','CE'),('rlys','NZ'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.64,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.67,resSelectionSubs('lys','CD',subs)))
IDSpec[(('lys','NZ'),('rlys','CE'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.73,resSelectionSubs('lys','CE',subs)))
IDSpec[(('lys','NZ'),('rlys','NZ'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.31,resSelectionSubs('lys','NZ',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9')
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
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.52,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.95,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.67,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.78,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.97,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.73,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.46,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.64,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.31,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9')
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
IDSpec['S_2el7_6_1_1_2'] = cmd.select('S_2el7_6_1_1_2', 'lys|lys_i')
cmd.delete('lys')
cmd.delete('lys_i')