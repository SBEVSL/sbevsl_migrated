'''
FUNC:S_1v03_3_2_1_21
PDB:1v03
EC:3.2.1.21
RESI:asp,asn,glu
LOCI:a-189,329,404;
'''
IDSpec[(('glu','CD'),('rasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.05,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','CD'),('rasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.56,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','CD'),('rasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.53,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE1'),('rasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.82,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE1'),('rasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.57,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE1'),('rasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.15,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','OE2'),('rasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.65,resSelectionSubs('asp','CG',subs)))
IDSpec[(('glu','OE2'),('rasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.14,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('glu','OE2'),('rasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.16,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('glu','CD'),('rasn','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.47,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','CD'),('rasn','ND2'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.29,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','CD'),('rasn','OD1'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.72,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE1'),('rasn','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.91,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE1'),('rasn','ND2'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.37,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE1'),('rasn','OD1'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.15,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE2'),('rasn','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.77,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE2'),('rasn','ND2'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.62,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE2'),('rasn','OD1'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.31,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asp','CG'),('sglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.05,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.82,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','CG'),('sglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.65,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.56,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.57,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.14,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.53,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.15,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.16,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.90,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.82,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.02,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.84,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+4.92,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.02,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.24,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.13,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.25,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sglu','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.47,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.77,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.29,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.37,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.62,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.72,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.15,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.31,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.90,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.84,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.24,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+4.92,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.13,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.02,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.02,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.25,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
IDSpec['S_1v03_3_2_1_21'] = cmd.select('S_1v03_3_2_1_21', 'glu|asp|asn')
cmd.delete('glu')
cmd.delete('asp')
cmd.delete('asn')
