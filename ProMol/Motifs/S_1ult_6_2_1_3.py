'''
FUNC:S_1ult_6_2_1_3
PDB:1ult
EC:6.2.1.3
RESI:lys,trp
LOCI:a-439,444;
'''
IDSpec[(('lys','CD'),('rtrp','CE2'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.69,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('lys','CD'),('rtrp','CZ2'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.90,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('lys','CD'),('rtrp','NE1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.56,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('lys','CE'),('rtrp','CE2'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.89,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('lys','CE'),('rtrp','CZ2'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.09,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('lys','CE'),('rtrp','NE1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.46,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('lys','NZ'),('rtrp','CE2'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.70,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('lys','NZ'),('rtrp','CZ2'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.64,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('lys','NZ'),('rtrp','NE1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.31,resSelectionSubs('trp','NE1',subs)))
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
IDSpec[(('trp','CE2'),('slys','CD'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+6.69,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('trp','CE2'),('slys','CE'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+6.89,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('trp','CE2'),('slys','NZ'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.70,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('trp','CZ2'),('slys','CD'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+5.90,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('trp','CZ2'),('slys','CE'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.09,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('trp','CZ2'),('slys','NZ'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+6.64,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('trp','NE1'),('slys','CD'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.56,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('trp','NE1'),('slys','CE'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+7.46,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('trp','NE1'),('slys','NZ'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.31,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9')
IDSpec['r_trp'] = cmd.count_atoms(resSelectionSubs('trp', subs=subs, selection=True))
cmd.delete('trp1')
cmd.delete('trp2')
cmd.delete('trp3')
cmd.delete('trp4')
cmd.delete('trp5')
cmd.delete('trp6')
cmd.delete('trp7')
cmd.delete('trp8')
cmd.delete('trp9')
IDSpec['S_1ult_6_2_1_3'] = cmd.select('S_1ult_6_2_1_3', 'lys|trp')
cmd.delete('lys')
cmd.delete('trp')
