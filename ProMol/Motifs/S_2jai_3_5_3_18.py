'''
FUNC:S_2jai_3_5_3_18
PDB:2jai
EC:3.5.3.18
RESI:asp,cys
LOCI:a-126,273;
'''
IDSpec[(('cys','CA'),('rasp','CG'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CA'),('rasp','OD1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CA'),('rasp','OD2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CB'),('rasp','CG'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CB'),('rasp','OD1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CB'),('rasp','OD2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','SG'),('rasp','CG'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','SG'),('rasp','OD1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','SG'),('rasp','OD2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+10,resSelectionSubs('asp','OD2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
IDSpec[(('asp','CG'),('scys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10,resSelectionSubs('cys','SG',subs,selection=True)))
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
IDSpec['S_2jai_3_5_3_18'] = cmd.select('S_2jai_3_5_3_18', 'cys|asp')
cmd.delete('cys')
cmd.delete('asp')
