'''
FUNC:S_2w3v_1_5_1_3
PDB:2w3v
EC:1.5.1.3
RESI:ile,asp
LOCI:a-24,31;
'''
IDSpec[(('ile','CD1'),('rasp','CG'))] = cmd.select('ile1', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+8.36,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ile','CD1'),('rasp','OD1'))] = cmd.select('ile2', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+9.13,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ile','CD1'),('rasp','OD2'))] = cmd.select('ile3', '%s w. %s of %s'%(resSelectionSubs('ile','CD1',subs),d+7.16,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ile','CG1'),('rasp','CG'))] = cmd.select('ile4', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+9.68,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ile','CG1'),('rasp','OD1'))] = cmd.select('ile5', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+10.45,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ile','CG1'),('rasp','OD2'))] = cmd.select('ile6', '%s w. %s of %s'%(resSelectionSubs('ile','CG1',subs),d+8.53,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ile','CG2'),('rasp','CG'))] = cmd.select('ile7', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+8.98,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ile','CG2'),('rasp','OD1'))] = cmd.select('ile8', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+9.85,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ile','CG2'),('rasp','OD2'))] = cmd.select('ile9', '%s w. %s of %s'%(resSelectionSubs('ile','CG2',subs),d+8.06,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('asp','CG'),('sile','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.36,resSelectionSubs('ile','CD1',subs,selection=True)))
IDSpec[(('asp','CG'),('sile','CG1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.68,resSelectionSubs('ile','CG1',subs,selection=True)))
IDSpec[(('asp','CG'),('sile','CG2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.98,resSelectionSubs('ile','CG2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sile','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.13,resSelectionSubs('ile','CD1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sile','CG1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.45,resSelectionSubs('ile','CG1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sile','CG2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.85,resSelectionSubs('ile','CG2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sile','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.16,resSelectionSubs('ile','CD1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sile','CG1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.53,resSelectionSubs('ile','CG1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sile','CG2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.06,resSelectionSubs('ile','CG2',subs,selection=True)))
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
IDSpec['S_2w3v_1_5_1_3'] = cmd.select('S_2w3v_1_5_1_3', 'ile|asp')
cmd.delete('ile')
cmd.delete('asp')
