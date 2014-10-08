'''
FUNC:S_3hb6_1_11_1_6
PDB:3hb6
EC:1.11.1.6
RESI:phe,ser,asn
LOCI:a-54,93,127;
'''
IDSpec[(('phe','CD1'),('rasn','CG'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.58,resSelectionSubs('asn','CG',subs)))
IDSpec[(('phe','CD1'),('rasn','ND2'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.95,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('phe','CD1'),('rasn','OD1'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.52,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('phe','CE1'),('rasn','CG'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.29,resSelectionSubs('asn','CG',subs)))
IDSpec[(('phe','CE1'),('rasn','ND2'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.55,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('phe','CE1'),('rasn','OD1'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+5.34,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('phe','CZ'),('rasn','CG'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.26,resSelectionSubs('asn','CG',subs)))
IDSpec[(('phe','CZ'),('rasn','ND2'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+6.13,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('phe','CZ'),('rasn','OD1'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+5.55,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('phe','CD1'),('rser','CA'))] = cmd.select('phe10', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+7.13,resSelectionSubs('ser','CA',subs)))
IDSpec[(('phe','CD1'),('rser','CB'))] = cmd.select('phe11', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+6.31,resSelectionSubs('ser','CB',subs)))
IDSpec[(('phe','CD1'),('rser','OG'))] = cmd.select('phe12', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+5.27,resSelectionSubs('ser','OG',subs)))
IDSpec[(('phe','CE1'),('rser','CA'))] = cmd.select('phe13', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+8.11,resSelectionSubs('ser','CA',subs)))
IDSpec[(('phe','CE1'),('rser','CB'))] = cmd.select('phe14', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+7.51,resSelectionSubs('ser','CB',subs)))
IDSpec[(('phe','CE1'),('rser','OG'))] = cmd.select('phe15', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+6.39,resSelectionSubs('ser','OG',subs)))
IDSpec[(('phe','CZ'),('rser','CA'))] = cmd.select('phe16', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.46,resSelectionSubs('ser','CA',subs)))
IDSpec[(('phe','CZ'),('rser','CB'))] = cmd.select('phe17', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+8.75,resSelectionSubs('ser','CB',subs)))
IDSpec[(('phe','CZ'),('rser','OG'))] = cmd.select('phe18', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+7.62,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('asn','CG'),('sphe','CD1'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.58,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sphe','CE1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.29,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sphe','CZ'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.26,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('sphe','CD1'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.95,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sphe','CE1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.55,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sphe','CZ'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.13,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('sphe','CD1'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.52,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sphe','CE1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.34,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sphe','CZ'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.55,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('asn','CG'),('rser','CA'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.96,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','CG'),('rser','CB'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.81,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','CG'),('rser','OG'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.56,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','ND2'),('rser','CA'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.83,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','ND2'),('rser','CB'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.59,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','ND2'),('rser','OG'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.35,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asn','OD1'),('rser','CA'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.87,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asn','OD1'),('rser','CB'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.65,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asn','OD1'),('rser','OG'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.36,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('sphe','CD1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.13,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sphe','CE1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.11,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sphe','CZ'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.46,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('ser','CB'),('sphe','CD1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.31,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sphe','CE1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.51,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sphe','CZ'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.75,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('ser','OG'),('sphe','CD1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.27,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sphe','CE1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.39,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sphe','CZ'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.62,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.96,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','ND2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.83,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasn','OD1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.87,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.81,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','ND2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.59,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasn','OD1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.65,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.56,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','ND2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.35,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasn','OD1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.36,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
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
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
IDSpec['S_3hb6_1_11_1_6'] = cmd.select('S_3hb6_1_11_1_6', 'phe|asn|ser')
cmd.delete('phe')
cmd.delete('asn')
cmd.delete('ser')
