'''
FUNC:S_2z00_3_5_2_3
PDB:2z00
EC:3.5.2.3
RESI:leu,glu,asp
LOCI:a-144,205,306;
'''
IDSpec[(('asp','CG'),('rleu','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+21.03,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','CG'),('rleu','CD2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+19.84,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','CG'),('rleu','CG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+19.75,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','OD1'),('rleu','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+21.57,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','OD1'),('rleu','CD2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+20.48,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','OD1'),('rleu','CG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+20.34,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','OD2'),('rleu','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+20.31,resSelectionSubs('leu','CD1',subs)))
IDSpec[(('asp','OD2'),('rleu','CD2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.02,resSelectionSubs('leu','CD2',subs)))
IDSpec[(('asp','OD2'),('rleu','CG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.01,resSelectionSubs('leu','CG',subs)))
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.90,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.94,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.37,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.99,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.98,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.51,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.72,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.78,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.25,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('leu','CD1'),('sasp','CG'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+21.03,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','OD1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+21.57,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CD1'),('sasp','OD2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+20.31,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','CG'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+19.84,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','OD1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+20.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CD2'),('sasp','OD2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+19.02,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','CG'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+19.75,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','OD1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+20.34,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('leu','CG'),('sasp','OD2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+19.01,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('leu','CD1'),('rglu','CD'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+23.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('leu','CD1'),('rglu','OE1'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+23.97,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('leu','CD1'),('rglu','OE2'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+24.35,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('leu','CD2'),('rglu','CD'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+24.07,resSelectionSubs('glu','CD',subs)))
IDSpec[(('leu','CD2'),('rglu','OE1'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+23.99,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('leu','CD2'),('rglu','OE2'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+24.52,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('leu','CG'),('rglu','CD'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+23.25,resSelectionSubs('glu','CD',subs)))
IDSpec[(('leu','CG'),('rglu','OE1'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+23.24,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('leu','CG'),('rglu','OE2'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+23.67,resSelectionSubs('glu','OE2',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18')
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
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+13.90,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.99,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+14.72,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+12.94,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.98,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+14.37,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.51,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+15.25,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','CD'),('sleu','CD1'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+23.92,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sleu','CD2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+24.07,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('glu','CD'),('sleu','CG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+23.25,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sleu','CD1'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.97,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sleu','CD2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.99,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sleu','CG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+23.24,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sleu','CD1'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.35,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sleu','CD2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+24.52,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sleu','CG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+23.67,resSelectionSubs('leu','CG',subs,selection=True)))
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
IDSpec['S_2z00_3_5_2_3'] = cmd.select('S_2z00_3_5_2_3', 'asp|leu|glu')
cmd.delete('asp')
cmd.delete('leu')
cmd.delete('glu')