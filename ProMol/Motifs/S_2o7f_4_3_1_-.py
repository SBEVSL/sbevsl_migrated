'''
FUNC:S_2o7f_4_3_1_-
PDB:2o7f
EC:4.3.1.-
RESI:tyr,phe
LOCI:a-300,350;
'''
IDSpec[(('phe','CD1'),('rtyr','CE1'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+47.86,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('phe','CD1'),('rtyr','CZ'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+47.19,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('phe','CD1'),('rtyr','OH'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+47.79,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('phe','CE1'),('rtyr','CE1'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+48.52,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('phe','CE1'),('rtyr','CZ'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+47.83,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('phe','CE1'),('rtyr','OH'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+48.40,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('phe','CZ'),('rtyr','CE1'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+49.83,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('phe','CZ'),('rtyr','CZ'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+49.13,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('phe','CZ'),('rtyr','OH'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+49.69,resSelectionSubs('tyr','OH',subs)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9')
IDSpec['r_phe'] = cmd.count_atoms(resSelectionSubs('phe', subs=subs, selection=True))
cmd.delete('phe1')
cmd.delete('phe2')
cmd.delete('phe3')
cmd.delete('phe4')
cmd.delete('phe5')
cmd.delete('phe6')
cmd.delete('phe7')
cmd.delete('phe8')
cmd.delete('phe9')
IDSpec[(('tyr','CE1'),('sphe','CD1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+47.86,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sphe','CE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+48.52,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sphe','CZ'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+49.83,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sphe','CD1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+47.19,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sphe','CE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+47.83,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sphe','CZ'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+49.13,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('sphe','CD1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+47.79,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sphe','CE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+48.40,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sphe','CZ'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+49.69,resSelectionSubs('phe','CZ',subs,selection=True)))
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
IDSpec['S_2o7f_4_3_1_-'] = cmd.select('S_2o7f_4_3_1_-', 'phe|tyr')
cmd.delete('phe')
cmd.delete('tyr')