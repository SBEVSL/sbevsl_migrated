'''
FUNC:S_2pbc_5_2_1_8
PDB:2pbc
EC:5.2.1.8
RESI:asp,ile,tyr
LOCI:a-67,86,112;
'''
IDSpec[(('tyr','CE1'),('rile','CD1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.71,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('tyr','CE1'),('rile','CG1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.84,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('tyr','CE1'),('rile','CG2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.67,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('tyr','CZ'),('rile','CD1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.89,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('tyr','CZ'),('rile','CG1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.25,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('tyr','CZ'),('rile','CG2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.56,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('tyr','OH'),('rile','CD1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.86,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('tyr','OH'),('rile','CG1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.07,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('tyr','OH'),('rile','CG2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.82,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+11.63,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+12.69,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.73,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.60,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+11.73,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.72,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.75,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+10.86,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.75,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('ile','CD1'),('styr','CE1'))] = cmd.select('ile1', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+7.71,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ile','CD1'),('styr','CZ'))] = cmd.select('ile2', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+6.89,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ile','CD1'),('styr','OH'))] = cmd.select('ile3', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+6.86,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ile','CG1'),('styr','CE1'))] = cmd.select('ile4', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+7.84,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ile','CG1'),('styr','CZ'))] = cmd.select('ile5', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+7.25,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ile','CG1'),('styr','OH'))] = cmd.select('ile6', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+7.07,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ile','CG2'),('styr','CE1'))] = cmd.select('ile7', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+5.67,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('ile','CG2'),('styr','CZ'))] = cmd.select('ile8', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+5.56,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('ile','CG2'),('styr','OH'))] = cmd.select('ile9', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+5.82,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('ile','CD1'),('rasp','CG'))] = cmd.select('ile10', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+12.76,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ile','CD1'),('rasp','OD1'))] = cmd.select('ile11', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+13.98,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ile','CD1'),('rasp','OD2'))] = cmd.select('ile12', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+11.90,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ile','CG1'),('rasp','CG'))] = cmd.select('ile13', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+13.40,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ile','CG1'),('rasp','OD1'))] = cmd.select('ile14', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+14.58,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ile','CG1'),('rasp','OD2'))] = cmd.select('ile15', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+12.43,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ile','CG2'),('rasp','CG'))] = cmd.select('ile16', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+13.30,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ile','CG2'),('rasp','OD1'))] = cmd.select('ile17', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+14.45,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ile','CG2'),('rasp','OD2'))] = cmd.select('ile18', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+12.29,resSelectionSubs('asp','OD2',subs)))
IDSpec['ile'] = cmd.select('ile',' br. ile1&br. ile2&br. ile3&br. ile4&br. ile5&br. ile6&br. ile7&br. ile8&br. ile9&br. ile10&br. ile11&br. ile12&br. ile13&br. ile14&br. ile15&br. ile16&br. ile17&br. ile18')
IDSpec['r_ile'] = cmd.count_atoms(resSelectionSubs('ile', subs=subs, selection=True))
cmd.delete('ile1')
cmd.delete('ile2')
cmd.delete('ile3')
cmd.delete('ile4')
cmd.delete('ile5')
cmd.delete('ile6')
cmd.delete('ile7')
cmd.delete('ile8')
cmd.delete('ile9')
cmd.delete('ile10')
cmd.delete('ile11')
cmd.delete('ile12')
cmd.delete('ile13')
cmd.delete('ile14')
cmd.delete('ile15')
cmd.delete('ile16')
cmd.delete('ile17')
cmd.delete('ile18')
IDSpec[(('asp','CG'),('styr','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.63,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CZ'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.60,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','OH'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.75,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.69,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CZ'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.73,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','OH'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.86,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.73,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CZ'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.72,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','OH'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.75,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','CG'),('sile','CD1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.76,resSelectionSubs('ile','CD1',subs,selection=True)))
IDSpec[(('asp','CG'),('sile','CG1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.40,resSelectionSubs('ile','CG1',subs,selection=True)))
IDSpec[(('asp','CG'),('sile','CG2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.30,resSelectionSubs('ile','CG2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sile','CD1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.98,resSelectionSubs('ile','CD1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sile','CG1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.58,resSelectionSubs('ile','CG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sile','CG2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.45,resSelectionSubs('ile','CG2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sile','CD1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.90,resSelectionSubs('ile','CD1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sile','CG1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.43,resSelectionSubs('ile','CG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sile','CG2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.29,resSelectionSubs('ile','CG2',subs,selection=True)))
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
IDSpec['S_2pbc_5_2_1_8'] = cmd.select('S_2pbc_5_2_1_8', 'tyr|ile|asp')
cmd.delete('tyr')
cmd.delete('ile')
cmd.delete('asp')
