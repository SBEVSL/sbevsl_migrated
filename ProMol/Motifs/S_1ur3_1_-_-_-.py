'''
FUNC:S_1ur3_1_-_-_-
PDB:1ur3
EC:1.-.-.-
RESI:tyr,lys
LOCI:m-55,83;
'''
IDSpec[(('lys','CD'),('rtyr','CE1'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.35,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CD'),('rtyr','CZ'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.74,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CD'),('rtyr','OH'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.22,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','CE'),('rtyr','CE1'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.32,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CE'),('rtyr','CZ'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.38,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CE'),('rtyr','OH'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.60,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','NZ'),('rtyr','CE1'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.58,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','NZ'),('rtyr','CZ'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.43,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','NZ'),('rtyr','OH'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.91,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('slys','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.35,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','CE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.32,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','NZ'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.58,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.74,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.38,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','NZ'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.43,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.22,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.60,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','NZ'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.91,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
IDSpec['S_1ur3_1_-_-_-'] = cmd.select('S_1ur3_1_-_-_-', 'lys|tyr')
cmd.delete('lys')
cmd.delete('tyr')
