'''
FUNC:S_1cui_3_1_1_3
PDB:1cui
EC:3.1.1.3
RESI:ser,ala,gln,asp,his
LOCI:a-42,120,121,175,188;
'''
IDSpec[(('asp','CG'),('rgln','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.40,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','CG'),('rgln','NE2'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.17,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','CG'),('rgln','OE1'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.57,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD1'),('rgln','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.79,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD1'),('rgln','NE2'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.49,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD1'),('rgln','OE1'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.95,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD2'),('rgln','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.89,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD2'),('rgln','NE2'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.70,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD2'),('rgln','OE1'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.05,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.72,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.16,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.02,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.16,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.48,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+13.32,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.19,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.76,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+13.61,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','CG'),('rala','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.93,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','CG'),('rala','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.78,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','CG'),('rala','CG'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.78,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','OD1'),('rala','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.77,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','OD1'),('rala','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.53,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','OD1'),('rala','CG'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.53,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','OD2'),('rala','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.08,resSelectionSubs('ala','CA',subs)))
IDSpec[(('asp','OD2'),('rala','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.00,resSelectionSubs('ala','CB',subs)))
IDSpec[(('asp','OD2'),('rala','CG'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.00,resSelectionSubs('ala','CG',subs)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.52,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.40,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.47,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.15,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.12,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.97,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.97,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.94,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.05,resSelectionSubs('his','NE2',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27&br. asp28&br. asp29&br. asp30&br. asp31&br. asp32&br. asp33&br. asp34&br. asp35&br. asp36')
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
cmd.delete('asp19')
cmd.delete('asp20')
cmd.delete('asp21')
cmd.delete('asp22')
cmd.delete('asp23')
cmd.delete('asp24')
cmd.delete('asp25')
cmd.delete('asp26')
cmd.delete('asp27')
cmd.delete('asp28')
cmd.delete('asp29')
cmd.delete('asp30')
cmd.delete('asp31')
cmd.delete('asp32')
cmd.delete('asp33')
cmd.delete('asp34')
cmd.delete('asp35')
cmd.delete('asp36')
IDSpec[(('gln','CD'),('sasp','CG'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.40,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD1'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.79,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD2'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+15.89,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','CG'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.17,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD1'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+15.49,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD2'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+15.70,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','CG'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.57,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD1'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.95,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD2'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','CD'),('rser','CA'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.45,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gln','CD'),('rser','CB'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+7.27,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gln','CD'),('rser','OG'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+6.06,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gln','NE2'),('rser','CA'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.47,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gln','NE2'),('rser','CB'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+6.14,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gln','NE2'),('rser','OG'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+5.01,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gln','OE1'),('rser','CA'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.45,resSelectionSubs('ser','CA',subs)))
IDSpec[(('gln','OE1'),('rser','CB'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+8.33,resSelectionSubs('ser','CB',subs)))
IDSpec[(('gln','OE1'),('rser','OG'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+7.19,resSelectionSubs('ser','OG',subs)))
IDSpec[(('gln','CD'),('rala','CA'))] = cmd.select('gln19', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.50,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gln','CD'),('rala','CB'))] = cmd.select('gln20', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.45,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gln','CD'),('rala','CG'))] = cmd.select('gln21', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.45,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gln','NE2'),('rala','CA'))] = cmd.select('gln22', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.63,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gln','NE2'),('rala','CB'))] = cmd.select('gln23', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.31,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gln','NE2'),('rala','CG'))] = cmd.select('gln24', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.31,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gln','OE1'),('rala','CA'))] = cmd.select('gln25', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.59,resSelectionSubs('ala','CA',subs)))
IDSpec[(('gln','OE1'),('rala','CB'))] = cmd.select('gln26', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.63,resSelectionSubs('ala','CB',subs)))
IDSpec[(('gln','OE1'),('rala','CG'))] = cmd.select('gln27', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.63,resSelectionSubs('ala','CG',subs)))
IDSpec[(('gln','CD'),('rhis','CE1'))] = cmd.select('gln28', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.28,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','CD'),('rhis','ND1'))] = cmd.select('gln29', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.58,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','CD'),('rhis','NE2'))] = cmd.select('gln30', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.86,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','NE2'),('rhis','CE1'))] = cmd.select('gln31', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.95,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','NE2'),('rhis','ND1'))] = cmd.select('gln32', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+13.22,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','NE2'),('rhis','NE2'))] = cmd.select('gln33', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.37,resSelectionSubs('his','NE2',subs)))
IDSpec[(('gln','OE1'),('rhis','CE1'))] = cmd.select('gln34', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.49,resSelectionSubs('his','CE1',subs)))
IDSpec[(('gln','OE1'),('rhis','ND1'))] = cmd.select('gln35', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+14.79,resSelectionSubs('his','ND1',subs)))
IDSpec[(('gln','OE1'),('rhis','NE2'))] = cmd.select('gln36', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.09,resSelectionSubs('his','NE2',subs)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27&br. gln28&br. gln29&br. gln30&br. gln31&br. gln32&br. gln33&br. gln34&br. gln35&br. gln36')
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
cmd.delete('gln19')
cmd.delete('gln20')
cmd.delete('gln21')
cmd.delete('gln22')
cmd.delete('gln23')
cmd.delete('gln24')
cmd.delete('gln25')
cmd.delete('gln26')
cmd.delete('gln27')
cmd.delete('gln28')
cmd.delete('gln29')
cmd.delete('gln30')
cmd.delete('gln31')
cmd.delete('gln32')
cmd.delete('gln33')
cmd.delete('gln34')
cmd.delete('gln35')
cmd.delete('gln36')
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.72,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.16,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.19,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+14.16,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.76,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+14.02,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.32,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.61,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sgln','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.45,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('sgln','NE2'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.47,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ser','CA'),('sgln','OE1'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.45,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sgln','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.27,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('sgln','NE2'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.14,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ser','CB'),('sgln','OE1'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.33,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sgln','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.06,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('sgln','NE2'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+5.01,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ser','OG'),('sgln','OE1'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.19,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ser','CA'),('rala','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.01,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CA'),('rala','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.91,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CA'),('rala','CG'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.91,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','CB'),('rala','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.98,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','CB'),('rala','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.87,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','CB'),('rala','CG'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.87,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','OG'),('rala','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.41,resSelectionSubs('ala','CA',subs)))
IDSpec[(('ser','OG'),('rala','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.54,resSelectionSubs('ala','CB',subs)))
IDSpec[(('ser','OG'),('rala','CG'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.54,resSelectionSubs('ala','CG',subs)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser28', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.24,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser29', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.37,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser30', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.29,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser31', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.79,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser32', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.91,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser33', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.81,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser34', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.68,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser35', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.89,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser36', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.87,resSelectionSubs('his','NE2',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27&br. ser28&br. ser29&br. ser30&br. ser31&br. ser32&br. ser33&br. ser34&br. ser35&br. ser36')
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
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.delete('ser23')
cmd.delete('ser24')
cmd.delete('ser25')
cmd.delete('ser26')
cmd.delete('ser27')
cmd.delete('ser28')
cmd.delete('ser29')
cmd.delete('ser30')
cmd.delete('ser31')
cmd.delete('ser32')
cmd.delete('ser33')
cmd.delete('ser34')
cmd.delete('ser35')
cmd.delete('ser36')
IDSpec[(('ala','CA'),('sasp','CG'))] = cmd.select('ala1', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.93,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CA'),('sasp','OD1'))] = cmd.select('ala2', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.77,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CA'),('sasp','OD2'))] = cmd.select('ala3', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.08,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','CG'))] = cmd.select('ala4', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.78,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','OD1'))] = cmd.select('ala5', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.53,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CB'),('sasp','OD2'))] = cmd.select('ala6', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','CG'))] = cmd.select('ala7', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','OD1'))] = cmd.select('ala8', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ala','CG'),('sasp','OD2'))] = cmd.select('ala9', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+9.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ala','CA'),('sgln','CD'))] = cmd.select('ala10', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.50,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ala','CA'),('sgln','NE2'))] = cmd.select('ala11', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.63,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ala','CA'),('sgln','OE1'))] = cmd.select('ala12', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+10.59,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ala','CB'),('sgln','CD'))] = cmd.select('ala13', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.45,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ala','CB'),('sgln','NE2'))] = cmd.select('ala14', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+9.31,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ala','CB'),('sgln','OE1'))] = cmd.select('ala15', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+10.63,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ala','CG'),('sgln','CD'))] = cmd.select('ala16', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.63,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('ala','CG'),('sgln','NE2'))] = cmd.select('ala17', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.63,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('ala','CG'),('sgln','OE1'))] = cmd.select('ala18', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+10.63,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','CA'))] = cmd.select('ala19', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+9.01,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','CB'))] = cmd.select('ala20', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.98,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CA'),('sser','OG'))] = cmd.select('ala21', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+8.41,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','CA'))] = cmd.select('ala22', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.91,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','CB'))] = cmd.select('ala23', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.87,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CB'),('sser','OG'))] = cmd.select('ala24', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+7.54,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','CA'))] = cmd.select('ala25', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.54,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','CB'))] = cmd.select('ala26', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.54,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('ala','CG'),('sser','OG'))] = cmd.select('ala27', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+7.54,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('ala','CA'),('rhis','CE1'))] = cmd.select('ala28', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.22,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ala','CA'),('rhis','ND1'))] = cmd.select('ala29', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+7.38,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ala','CA'),('rhis','NE2'))] = cmd.select('ala30', '%s w. %s of %s'%(resSelectionSubs('ala','CA',subs),d+6.59,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ala','CB'),('rhis','CE1'))] = cmd.select('ala31', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.53,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ala','CB'),('rhis','ND1'))] = cmd.select('ala32', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+6.77,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ala','CB'),('rhis','NE2'))] = cmd.select('ala33', '%s w. %s of %s'%(resSelectionSubs('ala','CB',subs),d+5.50,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ala','CG'),('rhis','CE1'))] = cmd.select('ala34', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.50,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ala','CG'),('rhis','ND1'))] = cmd.select('ala35', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.50,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ala','CG'),('rhis','NE2'))] = cmd.select('ala36', '%s w. %s of %s'%(resSelectionSubs('ala','CG',subs),d+5.50,resSelectionSubs('his','NE2',subs)))
IDSpec['ala'] = cmd.select('ala',' br. ala1&br. ala2&br. ala3&br. ala4&br. ala5&br. ala6&br. ala7&br. ala8&br. ala9&br. ala10&br. ala11&br. ala12&br. ala13&br. ala14&br. ala15&br. ala16&br. ala17&br. ala18&br. ala19&br. ala20&br. ala21&br. ala22&br. ala23&br. ala24&br. ala25&br. ala26&br. ala27&br. ala28&br. ala29&br. ala30&br. ala31&br. ala32&br. ala33&br. ala34&br. ala35&br. ala36')
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
cmd.delete('ala19')
cmd.delete('ala20')
cmd.delete('ala21')
cmd.delete('ala22')
cmd.delete('ala23')
cmd.delete('ala24')
cmd.delete('ala25')
cmd.delete('ala26')
cmd.delete('ala27')
cmd.delete('ala28')
cmd.delete('ala29')
cmd.delete('ala30')
cmd.delete('ala31')
cmd.delete('ala32')
cmd.delete('ala33')
cmd.delete('ala34')
cmd.delete('ala35')
cmd.delete('ala36')
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.52,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.15,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.97,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.40,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.94,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.47,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.97,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.28,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','NE2'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+11.95,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','CE1'),('sgln','OE1'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+13.49,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.58,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','NE2'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.22,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','ND1'),('sgln','OE1'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+14.79,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.86,resSelectionSubs('gln','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','NE2'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.37,resSelectionSubs('gln','NE2',subs,selection=True)))
IDSpec[(('his','NE2'),('sgln','OE1'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+13.09,resSelectionSubs('gln','OE1',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.24,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.79,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.68,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.37,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.91,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.89,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.29,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.81,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.87,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','CE1'),('sala','CA'))] = cmd.select('his28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.22,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sala','CB'))] = cmd.select('his29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.53,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sala','CG'))] = cmd.select('his30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.53,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sala','CA'))] = cmd.select('his31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.38,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sala','CB'))] = cmd.select('his32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.77,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sala','CG'))] = cmd.select('his33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.77,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sala','CA'))] = cmd.select('his34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.59,resSelectionSubs('ala','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sala','CB'))] = cmd.select('his35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.50,resSelectionSubs('ala','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sala','CG'))] = cmd.select('his36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.50,resSelectionSubs('ala','CG',subs,selection=True)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36')
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
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
IDSpec['S_1cui_3_1_1_3'] = cmd.select('S_1cui_3_1_1_3', 'asp|gln|ser|ala|his')
cmd.delete('asp')
cmd.delete('gln')
cmd.delete('ser')
cmd.delete('ala')
cmd.delete('his')
