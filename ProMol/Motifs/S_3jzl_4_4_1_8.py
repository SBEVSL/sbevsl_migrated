'''
FUNC:S_3jzl_4_4_1_8
PDB:3jzl
EC:4.4.1.8
RESI:asp,tyr,asp
LOCI:a-57,111,200;
'''
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.86,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.54,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.72,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.64,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.63,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.79,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.15,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.99,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+30.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+30.95,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+29.88,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+29.79,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+30.26,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+29.12,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+28.56,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+29.05,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+27.89,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('styr','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.86,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CZ'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.64,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','OH'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.79,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.54,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CZ'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.10,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','OH'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.15,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.72,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CZ'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.63,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','OH'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.99,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','CG'),('rasp','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.99,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','CG'),('rasp','OD1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+29.27,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','CG'),('rasp','OD2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.53,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD1'),('rasp','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+28.20,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD1'),('rasp','OD1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+28.44,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD1'),('rasp','OD2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.73,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('asp','OD2'),('rasp','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+29.73,resSelectionSubs('asp','CG',subs)))
IDSpec[(('asp','OD2'),('rasp','OD1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+30.04,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('asp','OD2'),('rasp','OD2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+29.23,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp_i','CG'),('styr','CE1'))] = cmd.select('asp_i1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+30.50,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('styr','CZ'))] = cmd.select('asp_i2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+29.79,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp_i','CG'),('styr','OH'))] = cmd.select('asp_i3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.56,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('styr','CE1'))] = cmd.select('asp_i4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.95,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('styr','CZ'))] = cmd.select('asp_i5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.26,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('styr','OH'))] = cmd.select('asp_i6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+29.05,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('styr','CE1'))] = cmd.select('asp_i7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+29.88,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('styr','CZ'))] = cmd.select('asp_i8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+29.12,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('styr','OH'))] = cmd.select('asp_i9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.89,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','CG'))] = cmd.select('asp_i10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.99,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD1'))] = cmd.select('asp_i11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+28.20,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','CG'),('sasp','OD2'))] = cmd.select('asp_i12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+29.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','CG'))] = cmd.select('asp_i13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+29.27,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD1'))] = cmd.select('asp_i14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+28.44,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD1'),('sasp','OD2'))] = cmd.select('asp_i15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+30.04,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','CG'))] = cmd.select('asp_i16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.53,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD1'))] = cmd.select('asp_i17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asp_i','OD2'),('sasp','OD2'))] = cmd.select('asp_i18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+29.23,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['asp_i'] = cmd.select('asp_i',' br. asp_i1&br. asp_i2&br. asp_i3&br. asp_i4&br. asp_i5&br. asp_i6&br. asp_i7&br. asp_i8&br. asp_i9&br. asp_i10&br. asp_i11&br. asp_i12&br. asp_i13&br. asp_i14&br. asp_i15&br. asp_i16&br. asp_i17&br. asp_i18')
IDSpec['r_asp_i'] = cmd.count_atoms(resSelectionSubs('asp_i', subs=subs, selection=True))
cmd.delete('asp_i1')
cmd.delete('asp_i2')
cmd.delete('asp_i3')
cmd.delete('asp_i4')
cmd.delete('asp_i5')
cmd.delete('asp_i6')
cmd.delete('asp_i7')
cmd.delete('asp_i8')
cmd.delete('asp_i9')
cmd.delete('asp_i10')
cmd.delete('asp_i11')
cmd.delete('asp_i12')
cmd.delete('asp_i13')
cmd.delete('asp_i14')
cmd.delete('asp_i15')
cmd.delete('asp_i16')
cmd.delete('asp_i17')
cmd.delete('asp_i18')
IDSpec['S_3jzl_4_4_1_8'] = cmd.select('S_3jzl_4_4_1_8', 'tyr|asp|asp_i')
cmd.delete('tyr')
cmd.delete('asp')
cmd.delete('asp_i')