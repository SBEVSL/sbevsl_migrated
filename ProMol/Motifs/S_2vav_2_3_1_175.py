'''
FUNC:S_2vav_2_3_1_175
PDB:2vav
EC:2.3.1.175
RESI:asp,his
LOCI:a-333,362;
'''
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.39,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.23,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.70,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.25,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.11,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.71,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.38,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.05,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.81,resSelectionSubs('asp','OD2',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9')
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
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.39,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.25,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.38,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.23,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.11,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.05,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.70,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.71,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.81,resSelectionSubs('his','NE2',subs,selection=True)))
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
IDSpec['S_2vav_2_3_1_175'] = cmd.select('S_2vav_2_3_1_175', 'his|asp')
cmd.delete('his')
cmd.delete('asp')
