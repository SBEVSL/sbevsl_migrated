'''
FUNC:S_2wud_3_7_1_8
PDB:2wud
EC:3.7.1.8
RESI:ala,asp,his
LOCI:a-114,241,269;
'''
IDSpec[(('his','CE1'),('rala','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.29,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','CE1'),('rala','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.58,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','CE1'),('rala','CG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.58,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','ND1'),('rala','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.47,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','ND1'),('rala','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.80,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','ND1'),('rala','CG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.80,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','NE2'),('rala','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.46,resSelectionSubs('ala','CA',subs)))
IDSpec[(('his','NE2'),('rala','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.35,resSelectionSubs('ala','CB',subs)))
IDSpec[(('his','NE2'),('rala','CG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.35,resSelectionSubs('ala','CG',subs)))
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.34,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.11,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.70,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.25,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.11,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.72,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.32,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.93,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.82,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('ala','CA'),('shis','CE1'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.29,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','ND1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.47,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CA'),('shis','NE2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','CE1'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.58,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','ND1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.80,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CB'),('shis','NE2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.35,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','CE1'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.35,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','ND1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.35,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ala','CG'),('shis','NE2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.35,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ala','CA'),('rasp','CG'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.06,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CA'),('rasp','OD1'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.08,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CA'),('rasp','OD2'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.08,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CB'),('rasp','CG'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.76,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CB'),('rasp','OD1'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.63,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CB'),('rasp','OD2'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+8.89,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ala','CG'),('rasp','CG'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.89,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ala','CG'),('rasp','OD1'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.89,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ala','CG'),('rasp','OD2'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+8.89,resSelectionSubs('asp','OD2',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18')
IDSpec['r_ala'] = cmd.count_atoms(resSelectionSubs('ala', subs=subs, selection=True))
cmd.delete('ala1')
cmd.delete('ala2')
cmd.delete('ala3')
cmd.delete('ala4')
cmd.delete('ala5')
cmd.delete('ala6')
cmd.delete('ala7')
cmd.delete('ala8')
cmd.delete('ala9')
cmd.delete('ala10')
cmd.delete('ala11')
cmd.delete('ala12')
cmd.delete('ala13')
cmd.delete('ala14')
cmd.delete('ala15')
cmd.delete('ala16')
cmd.delete('ala17')
cmd.delete('ala18')
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.34,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.25,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.32,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.11,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.11,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.93,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.70,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.72,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.82,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.06,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.76,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sala','CG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.76,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.08,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.63,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sala','CG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.63,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.08,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.89,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sala','CG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.89,resSelectionSubs('ala','CG',subs,selection=True)))
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
IDSpec['S_2wud_3_7_1_8'] = cmd.select('S_2wud_3_7_1_8', 'his|ala|asp')
cmd.delete('his')
cmd.delete('ala')
cmd.delete('asp')
