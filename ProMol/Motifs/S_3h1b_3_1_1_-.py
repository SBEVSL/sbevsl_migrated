'''
FUNC:S_3h1b_3_1_1_-
PDB:3h1b
EC:3.1.1.-
RESI:ser,asp,his
LOCI:a-144,237,268;
'''
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+14.79,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.50,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+15.42,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.52,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+14.26,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+14.12,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+15.46,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.23,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+16.02,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','CE1'),('rser','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.87,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','CE1'),('rser','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.92,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','CE1'),('rser','OG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.50,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','ND1'),('rser','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.05,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','ND1'),('rser','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.10,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','ND1'),('rser','OG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.72,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','NE2'),('rser','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.79,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','NE2'),('rser','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.32,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','NE2'),('rser','OG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.74,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.79,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.52,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.50,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.26,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.23,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.42,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.12,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.02,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.41,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.59,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+18.14,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.12,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+19.35,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+18.87,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.01,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+19.13,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+18.73,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('shis','CE1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.87,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','ND1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.05,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','NE2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+5.79,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','CE1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.92,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','ND1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.10,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','NE2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.32,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','CE1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.50,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','ND1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.72,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','NE2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.74,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+18.41,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+19.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+19.01,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+18.59,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+19.35,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+19.13,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.14,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.87,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.73,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18')
IDSpec['r_ser'] = cmd.count_atoms(resSelectionSubs('ser', subs=subs, selection=True))
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
IDSpec['S_3h1b_3_1_1_-'] = cmd.select('S_3h1b_3_1_1_-', 'his|asp|ser')
cmd.delete('his')
cmd.delete('asp')
cmd.delete('ser')
