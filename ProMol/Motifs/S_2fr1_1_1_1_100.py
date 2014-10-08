'''
FUNC:S_2fr1_1_1_1_100
PDB:2fr1
EC:1.1.1.100
RESI:tyr,asn
LOCI:a-1813,1817;
'''
IDSpec[(('tyr','CE1'),('rasn','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.72,resSelectionSubs('asn','CG',subs)))
IDSpec[(('tyr','CE1'),('rasn','ND2'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.68,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('tyr','CE1'),('rasn','OD1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.88,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasn','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.35,resSelectionSubs('asn','CG',subs)))
IDSpec[(('tyr','CZ'),('rasn','ND2'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.40,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('tyr','CZ'),('rasn','OD1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.41,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('tyr','OH'),('rasn','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.59,resSelectionSubs('asn','CG',subs)))
IDSpec[(('tyr','OH'),('rasn','ND2'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.99,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('tyr','OH'),('rasn','OD1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.28,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('styr','CE1'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.72,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asn','CG'),('styr','CZ'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.35,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('styr','OH'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.59,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asn','ND2'),('styr','CE1'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.68,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('styr','CZ'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.40,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('styr','OH'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.99,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asn','OD1'),('styr','CE1'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.88,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('styr','CZ'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.41,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('styr','OH'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.28,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
IDSpec['S_2fr1_1_1_1_100'] = cmd.select('S_2fr1_1_1_1_100', 'tyr|asn')
cmd.delete('tyr')
cmd.delete('asn')
