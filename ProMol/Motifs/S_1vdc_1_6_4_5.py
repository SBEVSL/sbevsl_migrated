'''
FUNC:S_1vdc_1_6_4_5
PDB:1vdc
EC:1.6.4.5
RESI:cys,cys,asp
LOCI:a-135,138,139;
'''
IDSpec[(('cys','CA'),('rcys','CA'))] = cmd.select('cys1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.23,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CA'),('rcys','CB'))] = cmd.select('cys2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.47,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CA'),('rcys','SG'))] = cmd.select('cys3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.32,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CB'),('rcys','CA'))] = cmd.select('cys4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.55,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','CB'),('rcys','CB'))] = cmd.select('cys5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.52,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','CB'),('rcys','SG'))] = cmd.select('cys6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.01,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','SG'),('rcys','CA'))] = cmd.select('cys7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.71,resSelectionSubs('cys','CA',subs)))
IDSpec[(('cys','SG'),('rcys','CB'))] = cmd.select('cys8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.02,resSelectionSubs('cys','CB',subs)))
IDSpec[(('cys','SG'),('rcys','SG'))] = cmd.select('cys9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.02,resSelectionSubs('cys','SG',subs)))
IDSpec[(('cys','CA'),('rasp','CG'))] = cmd.select('cys10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.69,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CA'),('rasp','OD1'))] = cmd.select('cys11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+8.40,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CA'),('rasp','OD2'))] = cmd.select('cys12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.17,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','CB'),('rasp','CG'))] = cmd.select('cys13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.46,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','CB'),('rasp','OD1'))] = cmd.select('cys14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+7.91,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','CB'),('rasp','OD2'))] = cmd.select('cys15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.95,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys','SG'),('rasp','CG'))] = cmd.select('cys16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.12,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys','SG'),('rasp','OD1'))] = cmd.select('cys17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+8.31,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys','SG'),('rasp','OD2'))] = cmd.select('cys18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.95,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('cys_i','CA'),('scys','CA'))] = cmd.select('cys_i1', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.23,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','CB'))] = cmd.select('cys_i2', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.55,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CA'),('scys','SG'))] = cmd.select('cys_i3', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+5.71,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CA'))] = cmd.select('cys_i4', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.47,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','CB'))] = cmd.select('cys_i5', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.52,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','CB'),('scys','SG'))] = cmd.select('cys_i6', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.02,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CA'))] = cmd.select('cys_i7', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+6.32,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','CB'))] = cmd.select('cys_i8', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+5.01,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('cys_i','SG'),('scys','SG'))] = cmd.select('cys_i9', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+4.02,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('cys_i','CA'),('rasp','CG'))] = cmd.select('cys_i10', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.40,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys_i','CA'),('rasp','OD1'))] = cmd.select('cys_i11', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+6.09,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys_i','CA'),('rasp','OD2'))] = cmd.select('cys_i12', '%s w. %s of %s'%(resSelectionSubs('cys','CA',subs),d+7.01,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys_i','CB'),('rasp','CG'))] = cmd.select('cys_i13', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.94,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys_i','CB'),('rasp','OD1'))] = cmd.select('cys_i14', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+5.68,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys_i','CB'),('rasp','OD2'))] = cmd.select('cys_i15', '%s w. %s of %s'%(resSelectionSubs('cys','CB',subs),d+6.22,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('cys_i','SG'),('rasp','CG'))] = cmd.select('cys_i16', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('cys_i','SG'),('rasp','OD1'))] = cmd.select('cys_i17', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.30,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('cys_i','SG'),('rasp','OD2'))] = cmd.select('cys_i18', '%s w. %s of %s'%(resSelectionSubs('cys','SG',subs),d+7.50,resSelectionSubs('asp','OD2',subs)))
IDSpec['cys_i'] = cmd.select('cys_i',' br. cys_i1&br. cys_i2&br. cys_i3&br. cys_i4&br. cys_i5&br. cys_i6&br. cys_i7&br. cys_i8&br. cys_i9&br. cys_i10&br. cys_i11&br. cys_i12&br. cys_i13&br. cys_i14&br. cys_i15&br. cys_i16&br. cys_i17&br. cys_i18')
IDSpec['r_cys_i'] = cmd.count_atoms(resSelectionSubs('cys_i', subs=subs, selection=True))
cmd.delete('cys_i1')
cmd.delete('cys_i2')
cmd.delete('cys_i3')
cmd.delete('cys_i4')
cmd.delete('cys_i5')
cmd.delete('cys_i6')
cmd.delete('cys_i7')
cmd.delete('cys_i8')
cmd.delete('cys_i9')
cmd.delete('cys_i10')
cmd.delete('cys_i11')
cmd.delete('cys_i12')
cmd.delete('cys_i13')
cmd.delete('cys_i14')
cmd.delete('cys_i15')
cmd.delete('cys_i16')
cmd.delete('cys_i17')
cmd.delete('cys_i18')
IDSpec[(('asp','CG'),('scys','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.69,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.46,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys','SG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.12,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.40,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.91,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys','SG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.31,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.17,resSelectionSubs('cys','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.95,resSelectionSubs('cys','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys','SG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.95,resSelectionSubs('cys','SG',subs,selection=True)))
IDSpec[(('asp','CG'),('scys_i','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.40,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('scys_i','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.94,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('scys_i','SG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.50,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys_i','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.09,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys_i','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.68,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('scys_i','SG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.30,resSelectionSubs('cys_i','SG',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys_i','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.01,resSelectionSubs('cys_i','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys_i','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.22,resSelectionSubs('cys_i','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('scys_i','SG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.50,resSelectionSubs('cys_i','SG',subs,selection=True)))
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
IDSpec['S_1vdc_1_6_4_5'] = cmd.select('S_1vdc_1_6_4_5', 'cys|cys_i|asp')
cmd.delete('cys')
cmd.delete('cys_i')
cmd.delete('asp')