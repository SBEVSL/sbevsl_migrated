'''
FUNC:S_1yoe_3_2_2_8
PDB:1yoe
EC:3.2.2.8
RESI:asp,asn,his
LOCI:a-10,166,240;
'''
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.80,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.00,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.97,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.48,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.42,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.82,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.27,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.71,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.27,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.91,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.57,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.23,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.15,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.72,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.50,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.51,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.28,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.84,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.80,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.27,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.42,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.71,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.97,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.82,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.27,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','CG'),('rhis','CE1'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.82,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asn','CG'),('rhis','ND1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.38,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asn','CG'),('rhis','NE2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.76,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asn','ND2'),('rhis','CE1'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.27,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asn','ND2'),('rhis','ND1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.66,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asn','ND2'),('rhis','NE2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.24,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asn','OD1'),('rhis','CE1'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.00,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asn','OD1'),('rhis','ND1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.69,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asn','OD1'),('rhis','NE2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.77,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+13.91,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+13.15,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+13.51,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+12.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+13.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.50,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.84,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('sasn','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.82,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasn','ND2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.27,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('his','CE1'),('sasn','OD1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.00,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasn','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.38,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasn','ND2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.66,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasn','OD1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.69,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasn','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.76,resSelectionSubs('asn','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasn','ND2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.24,resSelectionSubs('asn','ND2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasn','OD1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.77,resSelectionSubs('asn','OD1',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
IDSpec['r_his'] = cmd.count_atoms(resSelectionSubs('his', subs=subs, selection=True))
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
IDSpec['S_1yoe_3_2_2_8'] = cmd.select('S_1yoe_3_2_2_8', 'asp|asn|his')
cmd.delete('asp')
cmd.delete('asn')
cmd.delete('his')
