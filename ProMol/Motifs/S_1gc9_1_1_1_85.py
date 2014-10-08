'''
FUNC:S_1gc9_1_1_1_85
PDB:1gc9
EC:1.1.1.85
RESI:tyr,lys,asp
LOCI:a-139,185,217;
'''
IDSpec[(('tyr','CE1'),('rlys','CD'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.03,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CE1'),('rlys','CE'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.54,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CE1'),('rlys','NZ'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+19.21,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CZ'),('rlys','CD'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.18,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CZ'),('rlys','CE'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.62,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CZ'),('rlys','NZ'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+18.31,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','OH'),('rlys','CD'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.82,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','OH'),('rlys','CE'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+18.15,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','OH'),('rlys','NZ'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+17.74,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+20.33,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+20.08,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+21.41,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.43,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+19.24,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+20.47,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+18.65,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+18.52,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+19.68,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('lys','CD'),('styr','CE1'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+19.03,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','CZ'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.18,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','OH'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+17.82,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CE1'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.54,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CZ'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.62,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','OH'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.15,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CE1'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+19.21,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CZ'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.31,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','OH'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+17.74,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.65,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.98,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.05,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.57,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.16,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.80,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.21,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.76,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.69,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('styr','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+20.33,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CZ'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+19.43,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','OH'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.65,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+20.08,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CZ'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.24,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','OH'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+18.52,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+21.41,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CZ'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+20.47,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','OH'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.68,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.65,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.57,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.21,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.98,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.16,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.76,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.05,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.80,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.69,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_1gc9_1_1_1_85'] = cmd.select('S_1gc9_1_1_1_85', 'tyr|lys|asp')
cmd.delete('tyr')
cmd.delete('lys')
cmd.delete('asp')
