'''
FUNC:S_3dfr_1_5_1_3
PDB:3dfr
EC:1.5.1.3
RESI:leu,asp
LOCI:a-19,26;
'''
IDSpec[(('leu','CD1'),('rasp','CG'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.08,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CD1'),('rasp','OD1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+7.96,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CD1'),('rasp','OD2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+10.11,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CD2'),('rasp','CG'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+9.78,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CD2'),('rasp','OD1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+8.63,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CD2'),('rasp','OD2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+10.55,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CG'),('rasp','CG'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+10.18,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CG'),('rasp','OD1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+9.03,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CG'),('rasp','OD2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.10,resSelectionSubs('asp','OD2',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
IDSpec[(('asp','CG'),('sleu','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.08,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','CG'),('sleu','CD2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.78,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','CG'),('sleu','CG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.18,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.96,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CD2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.63,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.03,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.11,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CD2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.55,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.10,resSelectionSubs('leu','CG',subs,selection=True)))
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
IDSpec['S_3dfr_1_5_1_3'] = cmd.select('S_3dfr_1_5_1_3', 'leu|asp')
cmd.delete('leu')
cmd.delete('asp')
