'''
FUNC:S_1w6k_5_4_99_7
PDB:1w6k
EC:5.4.99.7
RESI:phe,gly,tyr
LOCI:a-585,588,704;
'''
IDSpec[(('gly','CA'),('rtyr','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.78,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','CA'),('rtyr','CZ'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.11,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','CA'),('rtyr','OH'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+15.08,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','N'),('rtyr','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+15.00,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','N'),('rtyr','CZ'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.35,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','N'),('rtyr','OH'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+14.45,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','O'),('rtyr','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.34,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('gly','O'),('rtyr','CZ'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.80,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('gly','O'),('rtyr','OH'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.75,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('gly','CA'),('rphe','CD1'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.84,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('gly','CA'),('rphe','CE1'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.64,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('gly','CA'),('rphe','CZ'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.46,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('gly','N'),('rphe','CD1'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.82,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('gly','N'),('rphe','CE1'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.72,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('gly','N'),('rphe','CZ'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.38,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('gly','O'),('rphe','CD1'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.10,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('gly','O'),('rphe','CE1'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.96,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('gly','O'),('rphe','CZ'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+12.01,resSelectionSubs('phe','CZ',subs)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9&br. gly10&br. gly11&br. gly12&br. gly13&br. gly14&br. gly15&br. gly16&br. gly17&br. gly18')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
cmd.delete('gly10')
cmd.delete('gly11')
cmd.delete('gly12')
cmd.delete('gly13')
cmd.delete('gly14')
cmd.delete('gly15')
cmd.delete('gly16')
cmd.delete('gly17')
cmd.delete('gly18')
IDSpec[(('tyr','CE1'),('sgly','CA'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+15.78,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','N'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+15.00,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sgly','O'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+17.34,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','CA'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+15.11,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','N'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+14.35,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sgly','O'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+16.80,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','CA'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+15.08,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','N'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+14.45,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('tyr','OH'),('sgly','O'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+16.75,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rphe','CD1'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+20.22,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('tyr','CE1'),('rphe','CE1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+20.62,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('tyr','CE1'),('rphe','CZ'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+20.46,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('tyr','CZ'),('rphe','CD1'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.28,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('tyr','CZ'),('rphe','CE1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.61,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('tyr','CZ'),('rphe','CZ'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.40,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('tyr','OH'),('rphe','CD1'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+19.30,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('tyr','OH'),('rphe','CE1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+19.56,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('tyr','OH'),('rphe','CZ'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+19.36,resSelectionSubs('phe','CZ',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18')
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
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
IDSpec[(('phe','CD1'),('sgly','CA'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.84,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('phe','CD1'),('sgly','N'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+8.82,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('phe','CD1'),('sgly','O'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.10,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('phe','CE1'),('sgly','CA'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.64,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('phe','CE1'),('sgly','N'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.72,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('phe','CE1'),('sgly','O'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+10.96,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('phe','CZ'),('sgly','CA'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.46,resSelectionSubs('gly','CA',subs,selection=True)))
IDSpec[(('phe','CZ'),('sgly','N'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.38,resSelectionSubs('gly','N',subs,selection=True)))
IDSpec[(('phe','CZ'),('sgly','O'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+12.01,resSelectionSubs('gly','O',subs,selection=True)))
IDSpec[(('phe','CD1'),('styr','CE1'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+20.22,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('phe','CD1'),('styr','CZ'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+19.28,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('phe','CD1'),('styr','OH'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+19.30,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('phe','CE1'),('styr','CE1'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+20.62,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('phe','CE1'),('styr','CZ'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+19.61,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('phe','CE1'),('styr','OH'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+19.56,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('phe','CZ'),('styr','CE1'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+20.46,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('phe','CZ'),('styr','CZ'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+19.40,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('phe','CZ'),('styr','OH'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+19.36,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec['phe'] = cmd.select('phe',' br. phe1&br. phe2&br. phe3&br. phe4&br. phe5&br. phe6&br. phe7&br. phe8&br. phe9&br. phe10&br. phe11&br. phe12&br. phe13&br. phe14&br. phe15&br. phe16&br. phe17&br. phe18')
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
cmd.delete('phe10')
cmd.delete('phe11')
cmd.delete('phe12')
cmd.delete('phe13')
cmd.delete('phe14')
cmd.delete('phe15')
cmd.delete('phe16')
cmd.delete('phe17')
cmd.delete('phe18')
IDSpec['S_1w6k_5_4_99_7'] = cmd.select('S_1w6k_5_4_99_7', 'gly|tyr|phe')
cmd.delete('gly')
cmd.delete('tyr')
cmd.delete('phe')
