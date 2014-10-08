'''
FUNC:S_2qfu_2_5_1_19
PDB:2qfu
EC:2.5.1.19
RESI:lys,asp,glu,his,lys
LOCI:a-22,313,341,385,411;
'''
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.01,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.83,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.68,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.97,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.86,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.63,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.78,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.67,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.32,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CD'),('rlys_i','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.35,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CD'),('rlys_i','CE'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.07,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CD'),('rlys_i','NZ'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.80,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CE'),('rlys_i','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.31,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','CE'),('rlys_i','CE'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.18,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','CE'),('rlys_i','NZ'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.91,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.62,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('lys','NZ'),('rlys_i','CE'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.34,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('lys','NZ'),('rlys_i','NZ'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.93,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('lys','CD'),('rhis','CE1'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.60,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','CD'),('rhis','ND1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.43,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','CD'),('rhis','NE2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.16,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','CE'),('rhis','CE1'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.12,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','CE'),('rhis','ND1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.03,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','CE'),('rhis','NE2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.67,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','NZ'),('rhis','CE1'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.21,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys','NZ'),('rhis','ND1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.33,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys','NZ'),('rhis','NE2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.56,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys','CD'),('rglu','CD'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.02,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CD'),('rglu','OE1'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+10.53,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CD'),('rglu','OE2'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.83,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','CE'),('rglu','CD'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.73,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','CE'),('rglu','OE1'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.26,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','CE'),('rglu','OE2'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.52,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys','NZ'),('rglu','CD'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.09,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys','NZ'),('rglu','OE1'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys','NZ'),('rglu','OE2'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.99,resSelectionSubs('glu','OE2',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27&br. lys28&br. lys29&br. lys30&br. lys31&br. lys32&br. lys33&br. lys34&br. lys35&br. lys36')
IDSpec['r_lys'] = cmd.count_atoms(resSelectionSubs('lys', subs=subs, selection=True))
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.delete('lys16')
cmd.delete('lys17')
cmd.delete('lys18')
cmd.delete('lys19')
cmd.delete('lys20')
cmd.delete('lys21')
cmd.delete('lys22')
cmd.delete('lys23')
cmd.delete('lys24')
cmd.delete('lys25')
cmd.delete('lys26')
cmd.delete('lys27')
cmd.delete('lys28')
cmd.delete('lys29')
cmd.delete('lys30')
cmd.delete('lys31')
cmd.delete('lys32')
cmd.delete('lys33')
cmd.delete('lys34')
cmd.delete('lys35')
cmd.delete('lys36')
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.01,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.97,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.78,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.86,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.67,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.68,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.63,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.32,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','CG'),('rlys_i','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.98,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('asp','CG'),('rlys_i','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+12.03,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('asp','CG'),('rlys_i','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.86,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys_i','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.49,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('asp','OD1'),('rlys_i','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.47,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('asp','OD1'),('rlys_i','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.22,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys_i','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.12,resSelectionSubs('lys_i','CD',subs)))
IDSpec[(('asp','OD2'),('rlys_i','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+12.06,resSelectionSubs('lys_i','CE',subs)))
IDSpec[(('asp','OD2'),('rlys_i','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.93,resSelectionSubs('lys_i','NZ',subs)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.70,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.79,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.85,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.33,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.47,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.21,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.34,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.14,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.20,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.64,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.82,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.07,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.66,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.51,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.92,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.17,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.74,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('lys_i','CD'),('slys','CD'))] = cmd.select('lys_i1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+9.35,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','CE'))] = cmd.select('lys_i2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.31,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CD'),('slys','NZ'))] = cmd.select('lys_i3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CD'))] = cmd.select('lys_i4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+9.07,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','CE'))] = cmd.select('lys_i5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.18,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','CE'),('slys','NZ'))] = cmd.select('lys_i6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.34,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CD'))] = cmd.select('lys_i7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.80,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','CE'))] = cmd.select('lys_i8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.91,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('slys','NZ'))] = cmd.select('lys_i9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.93,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','CG'))] = cmd.select('lys_i10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.98,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD1'))] = cmd.select('lys_i11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+11.49,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CD'),('sasp','OD2'))] = cmd.select('lys_i12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+12.12,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','CG'))] = cmd.select('lys_i13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.03,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD1'))] = cmd.select('lys_i14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+11.47,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','CE'),('sasp','OD2'))] = cmd.select('lys_i15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+12.06,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','CG'))] = cmd.select('lys_i16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.86,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD1'))] = cmd.select('lys_i17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.22,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys_i','NZ'),('sasp','OD2'))] = cmd.select('lys_i18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+10.93,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys_i','CD'),('rhis','CE1'))] = cmd.select('lys_i19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.60,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys_i','CD'),('rhis','ND1'))] = cmd.select('lys_i20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.87,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys_i','CD'),('rhis','NE2'))] = cmd.select('lys_i21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.93,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys_i','CE'),('rhis','CE1'))] = cmd.select('lys_i22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.52,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys_i','CE'),('rhis','ND1'))] = cmd.select('lys_i23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+8.05,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys_i','CE'),('rhis','NE2'))] = cmd.select('lys_i24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.80,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys_i','NZ'),('rhis','CE1'))] = cmd.select('lys_i25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.10,resSelectionSubs('his','CE1',subs)))
IDSpec[(('lys_i','NZ'),('rhis','ND1'))] = cmd.select('lys_i26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.89,resSelectionSubs('his','ND1',subs)))
IDSpec[(('lys_i','NZ'),('rhis','NE2'))] = cmd.select('lys_i27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.51,resSelectionSubs('his','NE2',subs)))
IDSpec[(('lys_i','CD'),('rglu','CD'))] = cmd.select('lys_i28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.15,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','CD'),('rglu','OE1'))] = cmd.select('lys_i29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.40,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','CD'),('rglu','OE2'))] = cmd.select('lys_i30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.59,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','CE'),('rglu','CD'))] = cmd.select('lys_i31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.00,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','CE'),('rglu','OE1'))] = cmd.select('lys_i32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.14,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','CE'),('rglu','OE2'))] = cmd.select('lys_i33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.50,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('lys_i','NZ'),('rglu','CD'))] = cmd.select('lys_i34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.66,resSelectionSubs('glu','CD',subs)))
IDSpec[(('lys_i','NZ'),('rglu','OE1'))] = cmd.select('lys_i35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.66,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('lys_i','NZ'),('rglu','OE2'))] = cmd.select('lys_i36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.86,resSelectionSubs('glu','OE2',subs)))
IDSpec['lys_i'] = cmd.select('lys_i',' br. lys_i1&br. lys_i2&br. lys_i3&br. lys_i4&br. lys_i5&br. lys_i6&br. lys_i7&br. lys_i8&br. lys_i9&br. lys_i10&br. lys_i11&br. lys_i12&br. lys_i13&br. lys_i14&br. lys_i15&br. lys_i16&br. lys_i17&br. lys_i18&br. lys_i19&br. lys_i20&br. lys_i21&br. lys_i22&br. lys_i23&br. lys_i24&br. lys_i25&br. lys_i26&br. lys_i27&br. lys_i28&br. lys_i29&br. lys_i30&br. lys_i31&br. lys_i32&br. lys_i33&br. lys_i34&br. lys_i35&br. lys_i36')
IDSpec['r_lys_i'] = cmd.count_atoms(resSelectionSubs('lys_i', subs=subs, selection=True))
cmd.delete('lys_i1')
cmd.delete('lys_i2')
cmd.delete('lys_i3')
cmd.delete('lys_i4')
cmd.delete('lys_i5')
cmd.delete('lys_i6')
cmd.delete('lys_i7')
cmd.delete('lys_i8')
cmd.delete('lys_i9')
cmd.delete('lys_i10')
cmd.delete('lys_i11')
cmd.delete('lys_i12')
cmd.delete('lys_i13')
cmd.delete('lys_i14')
cmd.delete('lys_i15')
cmd.delete('lys_i16')
cmd.delete('lys_i17')
cmd.delete('lys_i18')
cmd.delete('lys_i19')
cmd.delete('lys_i20')
cmd.delete('lys_i21')
cmd.delete('lys_i22')
cmd.delete('lys_i23')
cmd.delete('lys_i24')
cmd.delete('lys_i25')
cmd.delete('lys_i26')
cmd.delete('lys_i27')
cmd.delete('lys_i28')
cmd.delete('lys_i29')
cmd.delete('lys_i30')
cmd.delete('lys_i31')
cmd.delete('lys_i32')
cmd.delete('lys_i33')
cmd.delete('lys_i34')
cmd.delete('lys_i35')
cmd.delete('lys_i36')
IDSpec[(('his','CE1'),('slys','CD'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.60,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','CE'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.12,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','CE1'),('slys','NZ'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.21,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','CD'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.43,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','CE'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.03,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','ND1'),('slys','NZ'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.33,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','CD'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.16,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','CE'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.67,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('his','NE2'),('slys','NZ'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.56,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.70,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+8.33,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.21,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+9.47,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.34,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.85,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+8.60,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.14,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('slys_i','CD'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.60,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his','CE1'),('slys_i','CE'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.52,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his','CE1'),('slys_i','NZ'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.10,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his','ND1'),('slys_i','CD'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.87,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his','ND1'),('slys_i','CE'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.05,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his','ND1'),('slys_i','NZ'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.89,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his','NE2'),('slys_i','CD'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.93,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('his','NE2'),('slys_i','CE'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.80,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('his','NE2'),('slys_i','NZ'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.51,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('his','CE1'),('rglu','CD'))] = cmd.select('his28', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.66,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','CE1'),('rglu','OE1'))] = cmd.select('his29', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.39,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','CE1'),('rglu','OE2'))] = cmd.select('his30', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.79,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('his','ND1'),('rglu','CD'))] = cmd.select('his31', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.61,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','ND1'),('rglu','OE1'))] = cmd.select('his32', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+8.42,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','ND1'),('rglu','OE2'))] = cmd.select('his33', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.84,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('his','NE2'),('rglu','CD'))] = cmd.select('his34', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.49,resSelectionSubs('glu','CD',subs)))
IDSpec[(('his','NE2'),('rglu','OE1'))] = cmd.select('his35', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.28,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('his','NE2'),('rglu','OE2'))] = cmd.select('his36', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.80,resSelectionSubs('glu','OE2',subs)))
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
IDSpec[(('glu','CD'),('slys','CD'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.02,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','CE'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.73,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys','NZ'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.09,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CD'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.53,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','CE'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.26,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys','NZ'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.40,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CD'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.83,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','CE'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.52,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys','NZ'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.99,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.20,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.07,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.92,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.64,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.66,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.17,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.82,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.51,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.74,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','CD'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.15,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','CE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.00,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','CD'),('slys_i','NZ'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.66,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','CD'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.40,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','CE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.14,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','OE1'),('slys_i','NZ'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.66,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','CD'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.59,resSelectionSubs('lys_i','CD',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','CE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.50,resSelectionSubs('lys_i','CE',subs,selection=True)))
IDSpec[(('glu','OE2'),('slys_i','NZ'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.86,resSelectionSubs('lys_i','NZ',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','CE1'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.66,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','ND1'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.61,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','CD'),('shis','NE2'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.49,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','CE1'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.39,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','ND1'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.42,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','OE1'),('shis','NE2'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.28,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','CE1'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.79,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','ND1'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.84,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('glu','OE2'),('shis','NE2'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+4.80,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['glu'] = cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36')
IDSpec['r_glu'] = cmd.count_atoms(resSelectionSubs('glu', subs=subs, selection=True))
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
IDSpec['S_2qfu_2_5_1_19'] = cmd.select('S_2qfu_2_5_1_19', 'lys|asp|lys_i|his|glu')
cmd.delete('lys')
cmd.delete('asp')
cmd.delete('lys_i')
cmd.delete('his')
cmd.delete('glu')
