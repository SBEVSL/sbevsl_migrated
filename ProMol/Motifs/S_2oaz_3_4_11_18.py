'''
FUNC:S_2oaz_3_4_11_18
PDB:2oaz
EC:3.4.11.18
RESI:lys,glu
LOCI:a-342,364;
'''
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.87,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+18.10,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+16.19,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+18.35,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+19.58,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+17.65,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.88,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+20.13,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+18.24,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.87,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+18.35,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+18.88,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+18.10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+19.58,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+20.13,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+16.19,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.65,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+18.24,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2oaz_3_4_11_18'] = cmd.select('S_2oaz_3_4_11_18', 'lys|glu')
cmd.delete('lys')
cmd.delete('glu')
