'''
FUNC:S_1geb_1_14_15_1
PDB:1geb
EC:1.14.15.1
RESI:asp,ile
LOCI:a-251,252;
'''
IDSpec[(('asp','CG'),('rile','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.63,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('asp','CG'),('rile','CG1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.35,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('asp','CG'),('rile','CG2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.70,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('asp','OD1'),('rile','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.20,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('asp','OD1'),('rile','CG1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.98,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('asp','OD1'),('rile','CG2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.16,resSelectionSubs('ile','CG2',subs)))
IDSpec[(('asp','OD2'),('rile','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.84,resSelectionSubs('ile','CD1',subs)))
IDSpec[(('asp','OD2'),('rile','CG1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.52,resSelectionSubs('ile','CG1',subs)))
IDSpec[(('asp','OD2'),('rile','CG2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.73,resSelectionSubs('ile','CG2',subs)))
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
IDSpec[(('ile','CD1'),('sasp','CG'))] = cmd.select('ile1', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+8.63,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ile','CD1'),('sasp','OD1'))] = cmd.select('ile2', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+8.20,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ile','CD1'),('sasp','OD2'))] = cmd.select('ile3', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+9.84,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ile','CG1'),('sasp','CG'))] = cmd.select('ile4', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+7.35,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ile','CG1'),('sasp','OD1'))] = cmd.select('ile5', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+6.98,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ile','CG1'),('sasp','OD2'))] = cmd.select('ile6', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+8.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ile','CG2'),('sasp','CG'))] = cmd.select('ile7', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+8.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ile','CG2'),('sasp','OD1'))] = cmd.select('ile8', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+8.16,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ile','CG2'),('sasp','OD2'))] = cmd.select('ile9', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+9.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['ile'] = cmd.select('ile',' br. ile1&br. ile2&br. ile3&br. ile4&br. ile5&br. ile6&br. ile7&br. ile8&br. ile9')
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
IDSpec['S_1geb_1_14_15_1'] = cmd.select('S_1geb_1_14_15_1', 'asp|ile')
cmd.delete('asp')
cmd.delete('ile')
