'''
FUNC:S_2qjs_3_5_2_6
PDB:2qjs
EC:3.5.2.6
RESI:asn,tyr
LOCI:a-120,228;
'''
IDSpec[(('asn','CG'),('rtyr','CE1'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+15.16,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','CG'),('rtyr','CZ'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+15.23,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','CG'),('rtyr','OH'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+14.20,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','ND2'),('rtyr','CE1'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+14.79,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','ND2'),('rtyr','CZ'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+14.94,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','ND2'),('rtyr','OH'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+14.01,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','OD1'),('rtyr','CE1'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+16.21,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','OD1'),('rtyr','CZ'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+16.29,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','OD1'),('rtyr','OH'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+15.26,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('sasn','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+15.16,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','ND2'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+14.79,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','OD1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+16.21,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+15.23,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','ND2'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.94,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','OD1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.29,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+14.20,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','ND2'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+14.01,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','OD1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.26,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_2qjs_3_5_2_6'] = cmd.select('S_2qjs_3_5_2_6', 'asn|tyr')
cmd.delete('asn')
cmd.delete('tyr')