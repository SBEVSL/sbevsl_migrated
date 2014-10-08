'''
FUNC:S_2buu_1_13_11_3
PDB:2buu
EC:1.13.11.3
RESI:tyr,ser
LOCI:b-447,457;
'''
IDSpec[(('tyr','CE1'),('rser','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.02,resSelectionSubs('ser','CA',subs)))
IDSpec[(('tyr','CE1'),('rser','CB'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.29,resSelectionSubs('ser','CB',subs)))
IDSpec[(('tyr','CE1'),('rser','OG'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.70,resSelectionSubs('ser','OG',subs)))
IDSpec[(('tyr','CZ'),('rser','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.02,resSelectionSubs('ser','CA',subs)))
IDSpec[(('tyr','CZ'),('rser','CB'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.20,resSelectionSubs('ser','CB',subs)))
IDSpec[(('tyr','CZ'),('rser','OG'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.37,resSelectionSubs('ser','OG',subs)))
IDSpec[(('tyr','OH'),('rser','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.30,resSelectionSubs('ser','CA',subs)))
IDSpec[(('tyr','OH'),('rser','CB'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.48,resSelectionSubs('ser','CB',subs)))
IDSpec[(('tyr','OH'),('rser','OG'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.54,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('styr','CE1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.02,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('styr','CZ'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.02,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('styr','OH'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.30,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ser','CB'),('styr','CE1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.29,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('styr','CZ'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.20,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('styr','OH'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.48,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ser','OG'),('styr','CE1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.70,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('styr','CZ'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.37,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('styr','OH'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.54,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
IDSpec['S_2buu_1_13_11_3'] = cmd.select('S_2buu_1_13_11_3', 'tyr|ser')
cmd.delete('tyr')
cmd.delete('ser')
