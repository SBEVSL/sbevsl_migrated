'''
FUNC:S_1xog_3_2_1_18
PDB:1xog
EC:3.2.1.18
RESI:asp,glu
LOCI:a-152,279;
'''
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.47,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.97,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.40,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.27,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.69,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.18,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.77,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.80,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.47,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.27,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.69,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.20,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.40,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.18,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+10.80,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
IDSpec['S_1xog_3_2_1_18'] = cmd.select('S_1xog_3_2_1_18', 'asp|glu')
cmd.delete('asp')
cmd.delete('glu')
