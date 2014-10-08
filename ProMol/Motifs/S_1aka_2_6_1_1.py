'''
FUNC:S_1aka_2_6_1_1
PDB:1aka
EC:2.6.1.1
RESI:trp,asp,his
LOCI:a-140,222,258;
'''
IDSpec[(('trp','CE2'),('rasp','CG'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.60,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','CE2'),('rasp','OD1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.87,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','CE2'),('rasp','OD2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.49,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','CZ2'),('rasp','CG'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.77,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','CZ2'),('rasp','OD1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.87,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','CZ2'),('rasp','OD2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.76,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','NE1'),('rasp','CG'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.54,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','NE1'),('rasp','OD1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.86,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','NE1'),('rasp','OD2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.41,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','CE2'),('rhis','CE1'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+10.21,resSelectionSubs('his','CE1',subs)))
IDSpec[(('trp','CE2'),('rhis','ND1'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+11.00,resSelectionSubs('his','ND1',subs)))
IDSpec[(('trp','CE2'),('rhis','NE2'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+10.95,resSelectionSubs('his','NE2',subs)))
IDSpec[(('trp','CZ2'),('rhis','CE1'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+9.95,resSelectionSubs('his','CE1',subs)))
IDSpec[(('trp','CZ2'),('rhis','ND1'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.71,resSelectionSubs('his','ND1',subs)))
IDSpec[(('trp','CZ2'),('rhis','NE2'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.81,resSelectionSubs('his','NE2',subs)))
IDSpec[(('trp','NE1'),('rhis','CE1'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('trp','NE1'),('rhis','ND1'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+11.14,resSelectionSubs('his','ND1',subs)))
IDSpec[(('trp','NE1'),('rhis','NE2'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.78,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('asp','CG'),('strp','CE2'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.60,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','CG'),('strp','CZ2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.77,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','CG'),('strp','NE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.54,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','CE2'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.87,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','CZ2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.87,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','NE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.86,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','CE2'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.49,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','CZ2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.76,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','NE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.41,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.21,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.99,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.27,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.61,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.28,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.72,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.96,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.90,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.99,resSelectionSubs('his','NE2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
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
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
IDSpec[(('his','CE1'),('strp','CE2'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.21,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('his','CE1'),('strp','CZ2'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.95,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('his','CE1'),('strp','NE1'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.22,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('his','ND1'),('strp','CE2'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.00,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('his','ND1'),('strp','CZ2'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.71,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('his','ND1'),('strp','NE1'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.14,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('his','NE2'),('strp','CE2'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.95,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('his','NE2'),('strp','CZ2'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.81,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('his','NE2'),('strp','NE1'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.78,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.61,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.96,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.99,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.90,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+13.27,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.99,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_1aka_2_6_1_1'] = cmd.select('S_1aka_2_6_1_1', 'trp|asp|his')
cmd.delete('trp')
cmd.delete('asp')
cmd.delete('his')