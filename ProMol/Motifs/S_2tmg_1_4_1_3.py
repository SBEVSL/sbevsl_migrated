'''
FUNC:S_2tmg_1_4_1_3
PDB:2tmg
EC:1.4.1.3
RESI:lys,asp
LOCI:a-104,144;
'''
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.85,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.24,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.37,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.16,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.71,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.37,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.56,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.51,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.54,resSelectionSubs('asp','OD2',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9')
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
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.85,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.16,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.56,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.24,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.71,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.51,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.37,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.37,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.54,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2tmg_1_4_1_3'] = cmd.select('S_2tmg_1_4_1_3', 'lys|asp')
cmd.delete('lys')
cmd.delete('asp')
