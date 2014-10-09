'''
FUNC:S_1y7o_3_4_21_92
PDB:1y7o
EC:3.4.21.92
RESI:gly,asp
LOCI:a-67,172;
'''
IDSpec[(('asp','CG'),('rgly','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.22,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','CG'),('rgly','N'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.32,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','CG'),('rgly','O'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.13,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD1'),('rgly','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.33,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD1'),('rgly','N'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.50,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD1'),('rgly','O'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.08,resSelectionSubs('gly','O',subs)))
IDSpec[(('asp','OD2'),('rgly','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.14,resSelectionSubs('gly','CA',subs)))
IDSpec[(('asp','OD2'),('rgly','N'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.23,resSelectionSubs('gly','N',subs)))
IDSpec[(('asp','OD2'),('rgly','O'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.18,resSelectionSubs('gly','O',subs)))
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
IDSpec[(('gly','CA'),('sasp','CG'))] = cmd.select('gly1', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+17.22,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD1'))] = cmd.select('gly2', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+17.33,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','CA'),('sasp','OD2'))] = cmd.select('gly3', '%s w. %s of %s'%(resSelectionSubs('gly','CA',subs),d+16.14,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','CG'))] = cmd.select('gly4', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+16.32,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD1'))] = cmd.select('gly5', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+16.50,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','N'),('sasp','OD2'))] = cmd.select('gly6', '%s w. %s of %s'%(resSelectionSubs('gly','N',subs),d+15.23,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','CG'))] = cmd.select('gly7', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.13,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD1'))] = cmd.select('gly8', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+17.08,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gly','O'),('sasp','OD2'))] = cmd.select('gly9', '%s w. %s of %s'%(resSelectionSubs('gly','O',subs),d+16.18,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['gly'] = cmd.select('gly',' br. gly1&br. gly2&br. gly3&br. gly4&br. gly5&br. gly6&br. gly7&br. gly8&br. gly9')
IDSpec['r_gly'] = cmd.count_atoms(resSelectionSubs('gly', subs=subs, selection=True))
cmd.delete('gly1')
cmd.delete('gly2')
cmd.delete('gly3')
cmd.delete('gly4')
cmd.delete('gly5')
cmd.delete('gly6')
cmd.delete('gly7')
cmd.delete('gly8')
cmd.delete('gly9')
IDSpec['S_1y7o_3_4_21_92'] = cmd.select('S_1y7o_3_4_21_92', 'asp|gly')
cmd.delete('asp')
cmd.delete('gly')