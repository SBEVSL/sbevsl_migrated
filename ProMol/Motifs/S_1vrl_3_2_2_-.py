'''
FUNC:S_1vrl_3_2_2_-
PDB:1vrl
EC:3.2.2.-
RESI:glu,asn
LOCI:a-43,144;
'''
IDSpec[(('glu','CD'),('rasn','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.94,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','CD'),('rasn','ND2'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.85,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','CD'),('rasn','OD1'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.89,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE1'),('rasn','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.14,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE1'),('rasn','ND2'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.00,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE1'),('rasn','OD1'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.96,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE2'),('rasn','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.93,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE2'),('rasn','ND2'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.86,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE2'),('rasn','OD1'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.95,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sglu','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.94,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.14,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.93,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.85,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.00,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.86,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.89,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.96,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.95,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9')
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
IDSpec['S_1vrl_3_2_2_-'] = cmd.select('S_1vrl_3_2_2_-', 'glu|asn')
cmd.delete('glu')
cmd.delete('asn')
