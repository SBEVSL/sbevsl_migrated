'''
FUNC:S_1je0_2_4_2_28
PDB:1je0
EC:2.4.2.28
RESI:ser,asp,leu
LOCI:a-204,205,207;
'''
IDSpec[(('leu','CD1'),('rasp','CG'))] = cmd.select('leu1', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.65,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CD1'),('rasp','OD1'))] = cmd.select('leu2', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+8.10,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CD1'),('rasp','OD2'))] = cmd.select('leu3', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+9.21,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CD2'),('rasp','CG'))] = cmd.select('leu4', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.50,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CD2'),('rasp','OD1'))] = cmd.select('leu5', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+5.88,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CD2'),('rasp','OD2'))] = cmd.select('leu6', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+6.95,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CG'),('rasp','CG'))] = cmd.select('leu7', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.38,resSelectionSubs('asp','CG',subs)))
IDSpec[(('leu','CG'),('rasp','OD1'))] = cmd.select('leu8', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+6.99,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('leu','CG'),('rasp','OD2'))] = cmd.select('leu9', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+7.82,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('leu','CD1'),('rser','CA'))] = cmd.select('leu10', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+12.85,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD1'),('rser','CB'))] = cmd.select('leu11', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+13.22,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD1'),('rser','OG'))] = cmd.select('leu12', '%s w. %s of %s'%(resSelectionSubs('leu','CD1',subs),d+12.21,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CD2'),('rser','CA'))] = cmd.select('leu13', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+11.53,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CD2'),('rser','CB'))] = cmd.select('leu14', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+11.96,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CD2'),('rser','OG'))] = cmd.select('leu15', '%s w. %s of %s'%(resSelectionSubs('leu','CD2',subs),d+11.09,resSelectionSubs('ser','OG',subs)))
IDSpec[(('leu','CG'),('rser','CA'))] = cmd.select('leu16', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.78,resSelectionSubs('ser','CA',subs)))
IDSpec[(('leu','CG'),('rser','CB'))] = cmd.select('leu17', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+12.29,resSelectionSubs('ser','CB',subs)))
IDSpec[(('leu','CG'),('rser','OG'))] = cmd.select('leu18', '%s w. %s of %s'%(resSelectionSubs('leu','CG',subs),d+11.41,resSelectionSubs('ser','OG',subs)))
IDSpec['leu'] = cmd.select('leu',' br. leu1&br. leu2&br. leu3&br. leu4&br. leu5&br. leu6&br. leu7&br. leu8&br. leu9&br. leu10&br. leu11&br. leu12&br. leu13&br. leu14&br. leu15&br. leu16&br. leu17&br. leu18')
IDSpec['r_leu'] = cmd.count_atoms(resSelectionSubs('leu', subs=subs, selection=True))
cmd.delete('leu1')
cmd.delete('leu2')
cmd.delete('leu3')
cmd.delete('leu4')
cmd.delete('leu5')
cmd.delete('leu6')
cmd.delete('leu7')
cmd.delete('leu8')
cmd.delete('leu9')
cmd.delete('leu10')
cmd.delete('leu11')
cmd.delete('leu12')
cmd.delete('leu13')
cmd.delete('leu14')
cmd.delete('leu15')
cmd.delete('leu16')
cmd.delete('leu17')
cmd.delete('leu18')
IDSpec[(('asp','CG'),('sleu','CD1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.65,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','CG'),('sleu','CD2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.50,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','CG'),('sleu','CG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.38,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CD1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.10,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CD2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.88,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','OD1'),('sleu','CG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.99,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CD1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.21,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CD2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.95,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('asp','OD2'),('sleu','CG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.82,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.88,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.39,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.94,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.77,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.07,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.43,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.28,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.00,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.76,resSelectionSubs('ser','OG',subs)))
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
IDSpec[(('ser','CA'),('sleu','CD1'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+12.85,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CD2'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.53,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sleu','CG'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.78,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD1'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.22,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CD2'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.96,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sleu','CG'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.29,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD1'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.21,resSelectionSubs('leu','CD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CD2'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.09,resSelectionSubs('leu','CD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sleu','CG'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.41,resSelectionSubs('leu','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.88,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.77,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.28,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.39,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.07,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.94,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.43,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.76,resSelectionSubs('asp','OD2',subs,selection=True)))
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
IDSpec['S_1je0_2_4_2_28'] = cmd.select('S_1je0_2_4_2_28', 'leu|asp|ser')
cmd.delete('leu')
cmd.delete('asp')
cmd.delete('ser')