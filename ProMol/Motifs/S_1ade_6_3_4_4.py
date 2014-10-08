'''
FUNC:S_1ade_6_3_4_4
PDB:1ade
EC:6.3.4.4
RESI:asp,his,gln
LOCI:a-13,41,224;
'''
IDSpec[(('asp','CG'),('rgln','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.13,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','CG'),('rgln','NE2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.23,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','CG'),('rgln','OE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.18,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD1'),('rgln','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.21,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD1'),('rgln','NE2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.33,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD1'),('rgln','OE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.24,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD2'),('rgln','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.80,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD2'),('rgln','NE2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.77,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD2'),('rgln','OE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.91,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.56,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.81,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.19,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.73,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.98,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.29,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.56,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.75,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.21,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('gln','CD'),('sasp','CG'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.13,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.21,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.80,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','CG'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+13.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+13.33,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','CG'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.18,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','CD'),('rhis','CE1'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.64,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','CD'),('rhis','ND1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.41,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','CD'),('rhis','NE2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+17.57,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','NE2'),('rhis','CE1'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+17.59,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','NE2'),('rhis','ND1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.34,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','NE2'),('rhis','NE2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+18.47,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','OE1'),('rhis','CE1'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','OE1'),('rhis','ND1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+15.49,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','OE1'),('rhis','NE2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.66,resSelectionSubs('his','NE2',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18')
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
cmd.delete('gln10')
cmd.delete('gln11')
cmd.delete('gln12')
cmd.delete('gln13')
cmd.delete('gln14')
cmd.delete('gln15')
cmd.delete('gln16')
cmd.delete('gln17')
cmd.delete('gln18')
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.56,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+14.73,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.56,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+14.81,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.98,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.75,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.19,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.29,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+17.21,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.64,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','NE2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+17.59,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','OE1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+16.70,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.41,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','NE2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+16.34,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','OE1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+15.49,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+17.57,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','NE2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+18.47,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','OE1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+17.66,resSelectionSubs('gln','OE1',subs,selection=True)))
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
IDSpec['S_1ade_6_3_4_4'] = cmd.select('S_1ade_6_3_4_4', 'asp|gln|his')
cmd.delete('asp')
cmd.delete('gln')
cmd.delete('his')
