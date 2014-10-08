'''
FUNC:S_1z4i_3_1_3_-
PDB:1z4i
EC:3.1.3.-
RESI:asn,asp
LOCI:a-41,43;
'''
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.70,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.45,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.33,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.60,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.43,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.23,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.78,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.29,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.56,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.60,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.78,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.45,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.43,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.29,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.33,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.23,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.56,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_1z4i_3_1_3_-'] = cmd.select('S_1z4i_3_1_3_-', 'asp|asn')
cmd.delete('asp')
cmd.delete('asn')
