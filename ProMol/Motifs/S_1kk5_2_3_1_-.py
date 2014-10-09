'''
FUNC:S_1kk5_2_3_1_-
PDB:1kk5
EC:2.3.1.-
RESI:phe,phe
LOCI:a-91,94;
'''
IDSpec[(('phe','CD1'),('rphe','CD1'))] = cmd.select('phe1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.08,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('phe','CD1'),('rphe','CE1'))] = cmd.select('phe2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.91,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('phe','CD1'),('rphe','CZ'))] = cmd.select('phe3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.82,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('phe','CE1'),('rphe','CD1'))] = cmd.select('phe4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.21,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('phe','CE1'),('rphe','CE1'))] = cmd.select('phe5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.89,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('phe','CE1'),('rphe','CZ'))] = cmd.select('phe6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.80,resSelectionSubs('phe','CZ',subs)))
IDSpec[(('phe','CZ'),('rphe','CD1'))] = cmd.select('phe7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.54,resSelectionSubs('phe','CD1',subs)))
IDSpec[(('phe','CZ'),('rphe','CE1'))] = cmd.select('phe8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+11.14,resSelectionSubs('phe','CE1',subs)))
IDSpec[(('phe','CZ'),('rphe','CZ'))] = cmd.select('phe9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.99,resSelectionSubs('phe','CZ',subs)))
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
IDSpec[(('phe_i','CD1'),('sphe','CD1'))] = cmd.select('phe_i1', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.08,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sphe','CE1'))] = cmd.select('phe_i2', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+9.21,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('phe_i','CD1'),('sphe','CZ'))] = cmd.select('phe_i3', '%s w. %s of %s'%(resSelectionSubs('phe','CD1',subs),d+10.54,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sphe','CD1'))] = cmd.select('phe_i4', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.91,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sphe','CE1'))] = cmd.select('phe_i5', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+9.89,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('phe_i','CE1'),('sphe','CZ'))] = cmd.select('phe_i6', '%s w. %s of %s'%(resSelectionSubs('phe','CE1',subs),d+11.14,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sphe','CD1'))] = cmd.select('phe_i7', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.82,resSelectionSubs('phe','CD1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sphe','CE1'))] = cmd.select('phe_i8', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+9.80,resSelectionSubs('phe','CE1',subs,selection=True)))
IDSpec[(('phe_i','CZ'),('sphe','CZ'))] = cmd.select('phe_i9', '%s w. %s of %s'%(resSelectionSubs('phe','CZ',subs),d+10.99,resSelectionSubs('phe','CZ',subs,selection=True)))
IDSpec['phe_i'] = cmd.select('phe_i',' br. phe_i1&br. phe_i2&br. phe_i3&br. phe_i4&br. phe_i5&br. phe_i6&br. phe_i7&br. phe_i8&br. phe_i9')
IDSpec['r_phe_i'] = cmd.count_atoms(resSelectionSubs('phe_i', subs=subs, selection=True))
cmd.delete('phe_i1')
cmd.delete('phe_i2')
cmd.delete('phe_i3')
cmd.delete('phe_i4')
cmd.delete('phe_i5')
cmd.delete('phe_i6')
cmd.delete('phe_i7')
cmd.delete('phe_i8')
cmd.delete('phe_i9')
IDSpec['S_1kk5_2_3_1_-'] = cmd.select('S_1kk5_2_3_1_-', 'phe|phe_i')
cmd.delete('phe')
cmd.delete('phe_i')
