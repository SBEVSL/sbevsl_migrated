'''
FUNC:S_3i2e_3_5_3_18
PDB:3i2e
EC:3.5.3.18
RESI:asp,his,cys
LOCI:a-127,173,274;
'''
IDSpec[(('cys','CA'),('rasp','CG'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.23,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CA'),('rasp','OD1'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.92,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CA'),('rasp','OD2'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+12.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CB'),('rasp','CG'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.89,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CB'),('rasp','OD1'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+12.64,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CB'),('rasp','OD2'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+11.69,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','SG'),('rasp','CG'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.69,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','SG'),('rasp','OD1'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+12.61,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','SG'),('rasp','OD2'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+11.38,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CA'),('rhis','CE1'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CA'),('rhis','ND1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.11,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CA'),('rhis','NE2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+11.01,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','CB'),('rhis','CE1'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.36,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','CB'),('rhis','ND1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.23,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','CB'),('rhis','NE2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+10.34,resSelectionSubs('his','NE2',subs)))
IDSpec[(('cys','SG'),('rhis','CE1'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.49,resSelectionSubs('his','CE1',subs)))
IDSpec[(('cys','SG'),('rhis','ND1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.11,resSelectionSubs('his','ND1',subs)))
IDSpec[(('cys','SG'),('rhis','NE2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+9.59,resSelectionSubs('his','NE2',subs)))
IDSpec['cys'] = cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12&br. cys13&br. cys14&br. cys15&br. cys16&br. cys17&br. cys18')
IDSpec['r_cys'] = cmd.count_atoms(resSelectionSubs('cys', subs=subs, selection=True))
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.delete('cys13')
cmd.delete('cys14')
cmd.delete('cys15')
cmd.delete('cys16')
cmd.delete('cys17')
cmd.delete('cys18')
IDSpec[(('asp','CG'),('scys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.23,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.89,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.69,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.92,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.64,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+12.61,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.22,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.69,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+11.38,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.54,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.61,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.47,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.68,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.81,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.69,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.54,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.71,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.69,resSelectionSubs('his','NE2',subs)))
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
IDSpec[(('his','CE1'),('scys','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.22,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.36,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('scys','SG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.49,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.11,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.23,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('scys','SG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.11,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.01,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.34,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('scys','SG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.59,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.54,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.68,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.54,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.61,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.81,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.71,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.47,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.69,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.69,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_3i2e_3_5_3_18'] = cmd.select('S_3i2e_3_5_3_18', 'cys|asp|his')
cmd.delete('cys')
cmd.delete('asp')
cmd.delete('his')
