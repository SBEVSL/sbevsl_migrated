'''
FUNC:S_2det_2_8_1_-
PDB:2det
EC:2.8.1.-
RESI:lys,asp
LOCI:a-104,136;
'''
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.36,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.25,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+27.94,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+28.15,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+27.99,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+28.66,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.56,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+27.51,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+28.17,resSelectionSubs('lys','NZ',subs)))
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
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+27.36,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+28.15,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+27.56,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+27.25,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+27.99,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+27.51,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+27.94,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+28.66,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+28.17,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_2det_2_8_1_-'] = cmd.select('S_2det_2_8_1_-', 'asp|lys')
cmd.delete('asp')
cmd.delete('lys')
