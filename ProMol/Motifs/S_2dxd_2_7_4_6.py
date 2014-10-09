'''
FUNC:S_2dxd_2_7_4_6
PDB:2dxd
EC:2.7.4.6
RESI:lys,tyr,asn
LOCI:a-15,55,121;
'''
IDSpec[(('lys','CD'),('rasn','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.73,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CD'),('rasn','ND2'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.54,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CD'),('rasn','OD1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.50,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','CE'),('rasn','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.67,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CE'),('rasn','ND2'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.14,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CE'),('rasn','OD1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.56,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','NZ'),('rasn','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.70,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','NZ'),('rasn','ND2'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.93,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','NZ'),('rasn','OD1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.75,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','CD'),('rtyr','CE1'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.14,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CD'),('rtyr','CZ'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.16,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CD'),('rtyr','OH'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.83,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','CE'),('rtyr','CE1'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.84,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','CE'),('rtyr','CZ'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.01,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','CE'),('rtyr','OH'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.64,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('lys','NZ'),('rtyr','CE1'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.48,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('lys','NZ'),('rtyr','CZ'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.86,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('lys','NZ'),('rtyr','OH'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.59,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('asn','CG'),('slys','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.73,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.67,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','NZ'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.70,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.54,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.14,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','NZ'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.50,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.56,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','NZ'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+4.75,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','CG'),('rtyr','CE1'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.67,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','CG'),('rtyr','CZ'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.28,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','CG'),('rtyr','OH'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.16,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','ND2'),('rtyr','CE1'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.24,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','ND2'),('rtyr','CZ'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.06,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','ND2'),('rtyr','OH'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.06,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('asn','OD1'),('rtyr','CE1'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.05,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('asn','OD1'),('rtyr','CZ'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.51,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('asn','OD1'),('rtyr','OH'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.31,resSelectionSubs('tyr','OH',subs)))
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
IDSpec[(('tyr','CE1'),('slys','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.14,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','CE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.84,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CE1'),('slys','NZ'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.48,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.16,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','CE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.01,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','CZ'),('slys','NZ'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.86,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','CE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.64,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('tyr','OH'),('slys','NZ'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.59,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.67,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','ND2'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.24,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('sasn','OD1'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.05,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.28,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','ND2'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+10.06,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('sasn','OD1'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+9.51,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.16,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','ND2'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+9.06,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('tyr','OH'),('sasn','OD1'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.31,resSelectionSubs('asn','OD1',subs,selection=True)))
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
IDSpec['S_2dxd_2_7_4_6'] = cmd.select('S_2dxd_2_7_4_6', 'lys|asn|tyr')
cmd.delete('lys')
cmd.delete('asn')
cmd.delete('tyr')