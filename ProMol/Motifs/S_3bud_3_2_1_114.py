'''
FUNC:S_3bud_3_2_1_114
PDB:3bud
EC:3.2.1.114
RESI:ala,asp
LOCI:a-204,341;
'''
IDSpec[(('ala','CA'),('rasp','CG'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.84,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CA'),('rasp','OD1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.81,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CA'),('rasp','OD2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.93,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CB'),('rasp','CG'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.70,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CB'),('rasp','OD1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.72,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CB'),('rasp','OD2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CG'),('rasp','CG'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.82,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CG'),('rasp','OD1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.82,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CG'),('rasp','OD2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.82,resSelectionSubs('asp','OD2',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9')
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
IDSpec[(('asp','CG'),('sala','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.84,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.70,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.70,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.81,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.72,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.72,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.93,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.82,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.82,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_3bud_3_2_1_114'] = cmd.select('S_3bud_3_2_1_114', 'ala|asp')
cmd.delete('ala')
cmd.delete('asp')
