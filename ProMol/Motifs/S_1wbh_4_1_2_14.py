'''
FUNC:S_1wbh_4_1_2_14
PDB:1wbh
EC:4.1.2.14
RESI:asn,lys
LOCI:a-45,133;
'''
IDSpec[(('lys','CD'),('rasn','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.10,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CD'),('rasn','ND2'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.97,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CD'),('rasn','OD1'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.60,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','CE'),('rasn','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.41,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CE'),('rasn','ND2'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.24,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CE'),('rasn','OD1'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.78,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','NZ'),('rasn','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.47,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','NZ'),('rasn','ND2'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.37,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','NZ'),('rasn','OD1'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.68,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('slys','CD'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CE'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.41,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','NZ'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.47,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CD'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.97,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CE'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.24,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','NZ'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.37,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CD'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.60,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CE'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.78,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','NZ'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.68,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_1wbh_4_1_2_14'] = cmd.select('S_1wbh_4_1_2_14', 'lys|asn')
cmd.delete('lys')
cmd.delete('asn')
