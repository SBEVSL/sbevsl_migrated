'''
FUNC:S_3fua_4_1_2_17
PDB:3fua
EC:4.1.2.17
RESI:glu,tyr,ala
LOCI:a-73,113,117;
'''
IDSpec[(('tyr','CE1'),('rglu','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+32.73,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+32.21,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CE1'),('rglu','OE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+32.42,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CZ'),('rglu','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+33.24,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+32.68,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','CZ'),('rglu','OE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+32.93,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','OH'),('rglu','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+33.58,resSelectionSubs('glu','CD',subs)))
IDSpec[(('tyr','OH'),('rglu','OE1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+32.98,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('tyr','OH'),('rglu','OE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+33.33,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('tyr','CE1'),('rala','CA'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.77,resSelectionSubs('ala','CA',subs)))
IDSpec[(('tyr','CE1'),('rala','CB'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.40,resSelectionSubs('ala','CB',subs)))
IDSpec[(('tyr','CE1'),('rala','CG'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.40,resSelectionSubs('ala','CG',subs)))
IDSpec[(('tyr','CZ'),('rala','CA'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.87,resSelectionSubs('ala','CA',subs)))
IDSpec[(('tyr','CZ'),('rala','CB'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.37,resSelectionSubs('ala','CB',subs)))
IDSpec[(('tyr','CZ'),('rala','CG'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.37,resSelectionSubs('ala','CG',subs)))
IDSpec[(('tyr','OH'),('rala','CA'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+12.46,resSelectionSubs('ala','CA',subs)))
IDSpec[(('tyr','OH'),('rala','CB'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.85,resSelectionSubs('ala','CB',subs)))
IDSpec[(('tyr','OH'),('rala','CG'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+11.85,resSelectionSubs('ala','CG',subs)))
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
IDSpec[(('glu','CD'),('styr','CE1'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+32.73,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','CZ'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+33.24,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','CD'),('styr','OH'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+33.58,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CE1'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+32.21,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','CZ'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+32.68,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('styr','OH'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+32.98,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CE1'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.42,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','CZ'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+32.93,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('styr','OH'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+33.33,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('glu','CD'),('rala','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+25.68,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','CD'),('rala','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+25.26,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','CD'),('rala','CG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+25.26,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE1'),('rala','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+25.33,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE1'),('rala','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+24.84,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE1'),('rala','CG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+24.84,resSelectionSubs('ala','CG',subs)))
IDSpec[(('glu','OE2'),('rala','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+25.38,resSelectionSubs('ala','CA',subs)))
IDSpec[(('glu','OE2'),('rala','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.99,resSelectionSubs('ala','CB',subs)))
IDSpec[(('glu','OE2'),('rala','CG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.99,resSelectionSubs('ala','CG',subs)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
IDSpec[(('ala','CA'),('styr','CE1'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.77,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ala','CA'),('styr','CZ'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+11.87,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ala','CA'),('styr','OH'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+12.46,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ala','CB'),('styr','CE1'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10.40,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ala','CB'),('styr','CZ'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+11.37,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ala','CB'),('styr','OH'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+11.85,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ala','CG'),('styr','CE1'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+11.85,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ala','CG'),('styr','CZ'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+11.85,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ala','CG'),('styr','OH'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+11.85,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','CD'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+25.68,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE1'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+25.33,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CA'),('sglu','OE2'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+25.38,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','CD'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+25.26,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE1'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+24.84,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CB'),('sglu','OE2'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+24.99,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','CD'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+24.99,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE1'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+24.99,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ala','CG'),('sglu','OE2'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+24.99,resSelectionSubs('glu','OE2',subs,selection=True)))
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
IDSpec['S_3fua_4_1_2_17'] = cmd.select('S_3fua_4_1_2_17', 'tyr|glu|ala')
cmd.delete('tyr')
cmd.delete('glu')
cmd.delete('ala')
