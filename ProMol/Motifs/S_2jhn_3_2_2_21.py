'''
FUNC:S_2jhn_3_2_2_21
PDB:2jhn
EC:3.2.2.21
RESI:trp,asp
LOCI:a-221,239;
'''
IDSpec[(('trp','CE2'),('rasp','CG'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.56,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','CE2'),('rasp','OD1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+10.54,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','CE2'),('rasp','OD2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.80,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','CZ2'),('rasp','CG'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.88,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','CZ2'),('rasp','OD1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+11.81,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','CZ2'),('rasp','OD2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+11.18,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','NE1'),('rasp','CG'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.88,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','NE1'),('rasp','OD1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.91,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','NE1'),('rasp','OD2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.09,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('strp','CE2'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.56,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','CG'),('strp','CZ2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.88,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','CG'),('strp','NE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.88,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','CE2'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.54,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','CZ2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.81,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','NE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.91,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','CE2'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.80,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','CZ2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.18,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','NE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.09,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9')
IDSpec['r_asp'] = cmd.count_atoms(resSelectionSubs('asp', subs=subs, selection=True))
cmd.delete('asp1')
cmd.delete('asp2')
cmd.delete('asp3')
cmd.delete('asp4')
cmd.delete('asp5')
cmd.delete('asp6')
cmd.delete('asp7')
cmd.delete('asp8')
cmd.delete('asp9')
IDSpec['S_2jhn_3_2_2_21'] = cmd.select('S_2jhn_3_2_2_21', 'trp|asp')
cmd.delete('trp')
cmd.delete('asp')
