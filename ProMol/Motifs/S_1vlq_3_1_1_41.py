'''
FUNC:S_1vlq_3_1_1_41
PDB:1vlq
EC:3.1.1.41
RESI:ser,asp,his
LOCI:a-188,274,303;
'''
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.44,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.31,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.43,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.28,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.19,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.13,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.67,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.65,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.77,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.21,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.79,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.38,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.29,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.72,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.09,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.21,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.87,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.63,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.44,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.28,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.67,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.31,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.19,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.65,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.43,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.13,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.77,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('rser','CA'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.40,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','CE1'),('rser','CB'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.54,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','CE1'),('rser','OG'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','ND1'),('rser','CA'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.64,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','ND1'),('rser','CB'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.84,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','ND1'),('rser','OG'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.52,resSelectionSubs('ser','OG',subs)))
IDSpec[(('his','NE2'),('rser','CA'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.59,resSelectionSubs('ser','CA',subs)))
IDSpec[(('his','NE2'),('rser','CB'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.36,resSelectionSubs('ser','CB',subs)))
IDSpec[(('his','NE2'),('rser','OG'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.04,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.21,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.29,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.21,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.72,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.87,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.38,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.09,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.63,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','CE1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.40,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','ND1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.64,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CA'),('shis','NE2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.59,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','CE1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.54,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','ND1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','CB'),('shis','NE2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.36,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','CE1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.21,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','ND1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.52,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('ser','OG'),('shis','NE2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.04,resSelectionSubs('his','NE2',subs,selection=True)))
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
IDSpec['S_1vlq_3_1_1_41'] = cmd.select('S_1vlq_3_1_1_41', 'asp|his|ser')
cmd.delete('asp')
cmd.delete('his')
cmd.delete('ser')
