'''
FUNC:S_1rjp_3_5_1_81
PDB:1rjp
EC:3.5.1.81
RESI:gln,asp
LOCI:a-338,366;
'''
IDSpec[(('asp','CG'),('rgln','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+20.97,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','CG'),('rgln','NE2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+22.16,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','CG'),('rgln','OE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+20.03,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD1'),('rgln','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+20.50,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD1'),('rgln','NE2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+21.68,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD1'),('rgln','OE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.59,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD2'),('rgln','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+20.51,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD2'),('rgln','NE2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+21.69,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD2'),('rgln','OE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.52,resSelectionSubs('gln','OE1',subs)))
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
IDSpec[(('gln','CD'),('sasp','CG'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+20.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+20.50,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+20.51,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','CG'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+22.16,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+21.68,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+21.69,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','CG'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+20.03,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+19.59,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+19.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9')
IDSpec['r_gln'] = cmd.count_atoms(resSelectionSubs('gln', subs=subs, selection=True))
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
IDSpec['S_1rjp_3_5_1_81'] = cmd.select('S_1rjp_3_5_1_81', 'asp|gln')
cmd.delete('asp')
cmd.delete('gln')
