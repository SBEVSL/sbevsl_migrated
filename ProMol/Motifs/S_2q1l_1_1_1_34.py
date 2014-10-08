'''
FUNC:S_2q1l_1_1_1_34
PDB:2q1l
EC:1.1.1.34
RESI:glu,lys,asp
LOCI:a-559,691,767;
'''
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.16,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.89,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.85,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.76,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.72,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.37,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.62,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.65,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.87,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+23.96,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+22.81,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+24.63,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+24.00,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+22.84,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+24.75,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+24.77,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+23.63,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+25.54,resSelectionSubs('glu','OE2',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18')
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
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.16,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.76,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.89,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.72,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.65,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.85,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.37,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.87,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+22.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+21.76,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+23.82,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+22.02,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+20.88,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+22.90,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+24.09,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+22.94,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+24.98,resSelectionSubs('glu','OE2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18')
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
cmd.delete('asp10')
cmd.delete('asp11')
cmd.delete('asp12')
cmd.delete('asp13')
cmd.delete('asp14')
cmd.delete('asp15')
cmd.delete('asp16')
cmd.delete('asp17')
cmd.delete('asp18')
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+23.96,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.00,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.77,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+22.81,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+22.84,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.63,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.63,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.75,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+25.54,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+22.92,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+22.02,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.09,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+21.76,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+20.88,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+22.94,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+23.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+22.90,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.98,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18')
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
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
IDSpec['S_2q1l_1_1_1_34'] = cmd.select('S_2q1l_1_1_1_34', 'lys|asp|glu')
cmd.delete('lys')
cmd.delete('asp')
cmd.delete('glu')
