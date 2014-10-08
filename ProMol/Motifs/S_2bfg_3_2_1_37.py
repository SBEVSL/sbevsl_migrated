'''
FUNC:S_2bfg_3_2_1_37
PDB:2bfg
EC:3.2.1.37
RESI:trp,ala
LOCI:a-153,160;
'''
IDSpec[(('ala','CA'),('rtrp','CE2'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+24.44,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('ala','CA'),('rtrp','CZ2'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+25.07,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('ala','CA'),('rtrp','NE1'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+24.85,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('ala','CB'),('rtrp','CE2'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+24.96,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('ala','CB'),('rtrp','CZ2'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+25.55,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('ala','CB'),('rtrp','NE1'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+25.36,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('ala','CG'),('rtrp','CE2'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+25.36,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('ala','CG'),('rtrp','CZ2'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+25.36,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('ala','CG'),('rtrp','NE1'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+25.36,resSelectionSubs('trp','NE1',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
IDSpec[(('trp','CE2'),('sala','CA'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+24.44,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('trp','CE2'),('sala','CB'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+24.96,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('trp','CE2'),('sala','CG'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+24.96,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sala','CA'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+25.07,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sala','CB'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+25.55,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sala','CG'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+25.55,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('trp','NE1'),('sala','CA'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+24.85,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('trp','NE1'),('sala','CB'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+25.36,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('trp','NE1'),('sala','CG'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+25.36,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_2bfg_3_2_1_37'] = cmd.select('S_2bfg_3_2_1_37', 'ala|trp')
cmd.delete('ala')
cmd.delete('trp')
