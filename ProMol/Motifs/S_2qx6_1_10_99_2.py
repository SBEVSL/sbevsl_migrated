'''
FUNC:S_2qx6_1_10_99_2
PDB:2qx6
EC:1.10.99.2
RESI:gly,tyr,asn
LOCI:a-149,155,161;
'''
IDSpec[(('tyr','CE1'),('rasn','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.90,resSelectionSubs('asn','CG',subs)))
IDSpec[(('tyr','CE1'),('rasn','ND2'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.66,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('tyr','CE1'),('rasn','OD1'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.95,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasn','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.97,resSelectionSubs('asn','CG',subs)))
IDSpec[(('tyr','CZ'),('rasn','ND2'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.31,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('tyr','CZ'),('rasn','OD1'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.98,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('tyr','OH'),('rasn','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.22,resSelectionSubs('asn','CG',subs)))
IDSpec[(('tyr','OH'),('rasn','ND2'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.60,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('tyr','OH'),('rasn','OD1'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.97,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('tyr','CE1'),('rgly','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.22,resSelectionSubs('gly','CA',subs)))
IDSpec[(('tyr','CE1'),('rgly','N'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.37,resSelectionSubs('gly','N',subs)))
IDSpec[(('tyr','CE1'),('rgly','O'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.66,resSelectionSubs('gly','O',subs)))
IDSpec[(('tyr','CZ'),('rgly','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.84,resSelectionSubs('gly','CA',subs)))
IDSpec[(('tyr','CZ'),('rgly','N'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.01,resSelectionSubs('gly','N',subs)))
IDSpec[(('tyr','CZ'),('rgly','O'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.35,resSelectionSubs('gly','O',subs)))
IDSpec[(('tyr','OH'),('rgly','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.36,resSelectionSubs('gly','CA',subs)))
IDSpec[(('tyr','OH'),('rgly','N'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.54,resSelectionSubs('gly','N',subs)))
IDSpec[(('tyr','OH'),('rgly','O'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.23,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('asn','CG'),('styr','CE1'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.90,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asn','CG'),('styr','CZ'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.97,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('styr','OH'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.22,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asn','ND2'),('styr','CE1'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.66,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('styr','CZ'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.31,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('styr','OH'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.60,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asn','OD1'),('styr','CE1'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.95,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('styr','CZ'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.98,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('styr','OH'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.97,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asn','CG'),('rgly','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.70,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asn','CG'),('rgly','N'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.46,resSelectionSubs('gly','N',subs)))
IDSpec[(('asn','CG'),('rgly','O'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.56,resSelectionSubs('gly','O',subs)))
IDSpec[(('asn','ND2'),('rgly','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.47,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asn','ND2'),('rgly','N'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.26,resSelectionSubs('gly','N',subs)))
IDSpec[(('asn','ND2'),('rgly','O'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.26,resSelectionSubs('gly','O',subs)))
IDSpec[(('asn','OD1'),('rgly','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.19,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asn','OD1'),('rgly','N'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.06,resSelectionSubs('gly','N',subs)))
IDSpec[(('asn','OD1'),('rgly','O'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.08,resSelectionSubs('gly','O',subs)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
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
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
IDSpec[(('gly','CA'),('styr','CE1'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.22,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gly','CA'),('styr','CZ'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.84,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gly','CA'),('styr','OH'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+8.36,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gly','N'),('styr','CE1'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.37,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gly','N'),('styr','CZ'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+8.01,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gly','N'),('styr','OH'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+7.54,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gly','O'),('styr','CE1'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.66,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('gly','O'),('styr','CZ'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.35,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('gly','O'),('styr','OH'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.23,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('gly','CA'),('sasn','CG'))] = cmd.select('gly10', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+10.70,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasn','ND2'))] = cmd.select('gly11', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+9.47,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly','CA'),('sasn','OD1'))] = cmd.select('gly12', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+11.19,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly','N'),('sasn','CG'))] = cmd.select('gly13', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+10.46,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sasn','ND2'))] = cmd.select('gly14', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+9.26,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly','N'),('sasn','OD1'))] = cmd.select('gly15', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+11.06,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('gly','O'),('sasn','CG'))] = cmd.select('gly16', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+10.56,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sasn','ND2'))] = cmd.select('gly17', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+9.26,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('gly','O'),('sasn','OD1'))] = cmd.select('gly18', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+11.08,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_2qx6_1_10_99_2'] = cmd.select('S_2qx6_1_10_99_2', 'tyr|asn|gly')
cmd.delete('tyr')
cmd.delete('asn')
cmd.delete('gly')
