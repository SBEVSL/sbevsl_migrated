'''
FUNC:S_1yoo_2_6_1_1
PDB:1yoo
EC:2.6.1.1
RESI:trp,asp,lys
LOCI:a-140,222,258;
'''
IDSpec[(('trp','CE2'),('rasp','CG'))] = cmd.select('trp1', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.90,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','CE2'),('rasp','OD1'))] = cmd.select('trp2', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.13,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','CE2'),('rasp','OD2'))] = cmd.select('trp3', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+7.85,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','CZ2'),('rasp','CG'))] = cmd.select('trp4', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.86,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','CZ2'),('rasp','OD1'))] = cmd.select('trp5', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.91,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','CZ2'),('rasp','OD2'))] = cmd.select('trp6', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+7.88,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','NE1'),('rasp','CG'))] = cmd.select('trp7', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.88,resSelectionSubs('asp','CG',subs)))
IDSpec[(('trp','NE1'),('rasp','OD1'))] = cmd.select('trp8', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('trp','NE1'),('rasp','OD2'))] = cmd.select('trp9', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.87,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('trp','CE2'),('rlys','CD'))] = cmd.select('trp10', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+10.67,resSelectionSubs('lys','CD',subs)))
IDSpec[(('trp','CE2'),('rlys','CE'))] = cmd.select('trp11', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+9.38,resSelectionSubs('lys','CE',subs)))
IDSpec[(('trp','CE2'),('rlys','NZ'))] = cmd.select('trp12', '%s w. %s of %s'%(resSelectionSubs('trp','CE2',subs),d+8.24,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('trp','CZ2'),('rlys','CD'))] = cmd.select('trp13', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+10.21,resSelectionSubs('lys','CD',subs)))
IDSpec[(('trp','CZ2'),('rlys','CE'))] = cmd.select('trp14', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+8.95,resSelectionSubs('lys','CE',subs)))
IDSpec[(('trp','CZ2'),('rlys','NZ'))] = cmd.select('trp15', '%s w. %s of %s'%(resSelectionSubs('trp','CZ2',subs),d+7.87,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('trp','NE1'),('rlys','CD'))] = cmd.select('trp16', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+10.71,resSelectionSubs('lys','CD',subs)))
IDSpec[(('trp','NE1'),('rlys','CE'))] = cmd.select('trp17', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+9.33,resSelectionSubs('lys','CE',subs)))
IDSpec[(('trp','NE1'),('rlys','NZ'))] = cmd.select('trp18', '%s w. %s of %s'%(resSelectionSubs('trp','NE1',subs),d+8.31,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('asp','CG'),('strp','CE2'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.90,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','CG'),('strp','CZ2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.86,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','CG'),('strp','NE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.88,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','CE2'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.13,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','CZ2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.91,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','OD1'),('strp','NE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.10,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','CE2'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.85,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','CZ2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.88,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('asp','OD2'),('strp','NE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.87,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.49,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.19,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.80,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.57,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.40,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.08,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.59,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.09,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.66,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('strp','CE2'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.67,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('lys','CD'),('strp','CZ2'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.21,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('lys','CD'),('strp','NE1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.71,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('lys','CE'),('strp','CE2'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.38,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('lys','CE'),('strp','CZ2'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.95,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('lys','CE'),('strp','NE1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.33,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('strp','CE2'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.24,resSelectionSubs('trp','CE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('strp','CZ2'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.87,resSelectionSubs('trp','CZ2',subs,selection=True)))
IDSpec[(('lys','NZ'),('strp','NE1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.31,resSelectionSubs('trp','NE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.49,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.59,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.19,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+10.40,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.09,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.80,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.08,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+9.66,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec['S_1yoo_2_6_1_1'] = cmd.select('S_1yoo_2_6_1_1', 'trp|asp|lys')
cmd.delete('trp')
cmd.delete('asp')
cmd.delete('lys')
