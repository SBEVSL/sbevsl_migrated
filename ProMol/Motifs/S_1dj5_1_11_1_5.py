'''
FUNC:S_1dj5_1_11_1_5
PDB:1dj5
EC:1.11.1.5
RESI:ala,his,trp
LOCI:a-48,52,191;
'''
IDSpec[(('ala','CA'),('rhis','CE1'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.67,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ala','CA'),('rhis','ND1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.37,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ala','CA'),('rhis','NE2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.44,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ala','CB'),('rhis','CE1'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.31,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ala','CB'),('rhis','ND1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.15,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ala','CB'),('rhis','NE2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.28,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ala','CG'),('rhis','CE1'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.28,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ala','CG'),('rhis','ND1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.28,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ala','CG'),('rhis','NE2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.28,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ala','CA'),('rtrp','CE2'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+13.16,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('ala','CA'),('rtrp','CZ2'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.17,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('ala','CA'),('rtrp','NE1'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+14.23,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('ala','CB'),('rtrp','CE2'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+12.28,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('ala','CB'),('rtrp','CZ2'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+11.21,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('ala','CB'),('rtrp','NE1'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+13.42,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('ala','CG'),('rtrp','CE2'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+13.42,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('ala','CG'),('rtrp','CZ2'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+13.42,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('ala','CG'),('rtrp','NE1'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+13.42,resSelectionSubs('trp','NE1',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18')
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
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.delete('ala14')
cmd.delete('ala15')
cmd.delete('ala16')
cmd.delete('ala17')
cmd.delete('ala18')
IDSpec[(('his','CE1'),('sala','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.67,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sala','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.31,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sala','CG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.31,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sala','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.37,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sala','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.15,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sala','CG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.15,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sala','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.44,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sala','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.28,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sala','CG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.28,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('rtrp','CE2'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+13.99,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('his','CE1'),('rtrp','CZ2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.67,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('his','CE1'),('rtrp','NE1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+14.78,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('his','ND1'),('rtrp','CE2'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+14.98,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('his','ND1'),('rtrp','CZ2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.66,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('his','ND1'),('rtrp','NE1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.82,resSelectionSubs('trp','NE1',subs)))
IDSpec[(('his','NE2'),('rtrp','CE2'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+13.62,resSelectionSubs('trp','CE2',subs)))
IDSpec[(('his','NE2'),('rtrp','CZ2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.36,resSelectionSubs('trp','CZ2',subs)))
IDSpec[(('his','NE2'),('rtrp','NE1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+14.33,resSelectionSubs('trp','NE1',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
IDSpec[(('trp','CE2'),('sala','CA'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.16,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('trp','CE2'),('sala','CB'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+12.28,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('trp','CE2'),('sala','CG'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+12.28,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sala','CA'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.17,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sala','CB'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+11.21,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('trp','CZ2'),('sala','CG'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+11.21,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('trp','NE1'),('sala','CA'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.23,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('trp','NE1'),('sala','CB'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+13.42,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('trp','NE1'),('sala','CG'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+13.42,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('trp','CE2'),('shis','CE1'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.99,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('trp','CE2'),('shis','ND1'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+14.98,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('trp','CE2'),('shis','NE2'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+13.62,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('trp','CZ2'),('shis','CE1'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.67,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('shis','ND1'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+13.66,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('trp','CZ2'),('shis','NE2'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+12.36,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('trp','NE1'),('shis','CE1'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.78,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('trp','NE1'),('shis','ND1'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+15.82,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('trp','NE1'),('shis','NE2'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+14.33,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['trp'] = cmd.select('trp',' br. trp1&br. trp2&br. trp3&br. trp4&br. trp5&br. trp6&br. trp7&br. trp8&br. trp9&br. trp10&br. trp11&br. trp12&br. trp13&br. trp14&br. trp15&br. trp16&br. trp17&br. trp18')
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
cmd.delete('trp10')
cmd.delete('trp11')
cmd.delete('trp12')
cmd.delete('trp13')
cmd.delete('trp14')
cmd.delete('trp15')
cmd.delete('trp16')
cmd.delete('trp17')
cmd.delete('trp18')
IDSpec['S_1dj5_1_11_1_5'] = cmd.select('S_1dj5_1_11_1_5', 'ala|his|trp')
cmd.delete('ala')
cmd.delete('his')
cmd.delete('trp')