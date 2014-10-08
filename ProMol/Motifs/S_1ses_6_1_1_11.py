'''
FUNC:S_1ses_6_1_1_11
PDB:1ses
EC:6.1.1.11
RESI:arg,glu,ser,asp,arg
LOCI:a-256,258,261,265,271;
'''
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.58,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.29,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.29,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.34,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.11,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+17.98,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.74,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.44,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+17.52,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','CG'),('rser','CA'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.79,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','CG'),('rser','CB'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+15.14,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','CG'),('rser','OG'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.56,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD1'),('rser','CA'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.19,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD1'),('rser','CB'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+15.42,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD1'),('rser','OG'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.83,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','OD2'),('rser','CA'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.65,resSelectionSubs('ser','CA',subs)))
IDSpec[(('asp','OD2'),('rser','CB'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+15.04,resSelectionSubs('ser','CB',subs)))
IDSpec[(('asp','OD2'),('rser','OG'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.45,resSelectionSubs('ser','OG',subs)))
IDSpec[(('asp','CG'),('rarg','CZ'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+23.19,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','CG'),('rarg','NE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+22.59,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','CG'),('rarg','NH1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+24.01,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg','CZ'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+23.81,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg','NE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+23.25,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD1'),('rarg','NH1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+24.65,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg','CZ'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+23.57,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg','NE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+22.91,resSelectionSubs('arg','NE',subs)))
IDSpec[(('asp','OD2'),('rarg','NH1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+24.40,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('asp','CG'),('rarg_i','CZ'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.00,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('asp','CG'),('rarg_i','NE'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+14.04,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('asp','CG'),('rarg_i','NH1'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+13.95,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('asp','OD1'),('rarg_i','CZ'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.55,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('asp','OD1'),('rarg_i','NE'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.66,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('asp','OD1'),('rarg_i','NH1'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+14.38,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('asp','OD2'),('rarg_i','CZ'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.31,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('asp','OD2'),('rarg_i','NE'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.35,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('asp','OD2'),('rarg_i','NH1'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+14.37,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.58,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+17.34,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+16.74,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.29,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+17.11,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+16.44,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.29,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.98,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+17.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','CD'),('rser','CA'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+11.03,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','CD'),('rser','CB'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.31,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','CD'),('rser','OG'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+12.88,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE1'),('rser','CA'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+11.80,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE1'),('rser','CB'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.13,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE1'),('rser','OG'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+13.78,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','OE2'),('rser','CA'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+11.40,resSelectionSubs('ser','CA',subs)))
IDSpec[(('glu','OE2'),('rser','CB'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+12.58,resSelectionSubs('ser','CB',subs)))
IDSpec[(('glu','OE2'),('rser','OG'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+13.07,resSelectionSubs('ser','OG',subs)))
IDSpec[(('glu','CD'),('rarg','CZ'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.52,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','CD'),('rarg','NE'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.54,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','CD'),('rarg','NH1'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.44,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg','CZ'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.83,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg','NE'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.91,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE1'),('rarg','NH1'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.62,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg','CZ'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.53,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg','NE'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.61,resSelectionSubs('arg','NE',subs)))
IDSpec[(('glu','OE2'),('rarg','NH1'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.54,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('glu','CD'),('rarg_i','CZ'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.91,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('glu','CD'),('rarg_i','NE'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+5.17,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('glu','CD'),('rarg_i','NH1'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.04,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('glu','OE1'),('rarg_i','CZ'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.53,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('glu','OE1'),('rarg_i','NE'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+5.51,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('glu','OE1'),('rarg_i','NH1'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.69,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('glu','OE2'),('rarg_i','CZ'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.01,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('glu','OE2'),('rarg_i','NE'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.41,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('glu','OE2'),('rarg_i','NH1'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.91,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('ser','CA'),('sasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.79,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+15.19,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CA'),('sasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+14.65,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.14,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.42,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','CB'),('sasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+15.04,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+16.56,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+16.83,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('ser','OG'),('sasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+16.45,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.03,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.80,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CA'),('sglu','OE2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.40,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+13.13,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','CB'),('sglu','OE2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+12.58,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+12.88,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.78,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('ser','OG'),('sglu','OE2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+13.07,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('ser','CA'),('rarg','CZ'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+17.21,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CA'),('rarg','NE'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+16.24,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CA'),('rarg','NH1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+18.41,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CB'),('rarg','CZ'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+18.18,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','CB'),('rarg','NE'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+17.27,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','CB'),('rarg','NH1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+19.41,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','OG'),('rarg','CZ'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+18.35,resSelectionSubs('arg','CZ',subs)))
IDSpec[(('ser','OG'),('rarg','NE'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+17.42,resSelectionSubs('arg','NE',subs)))
IDSpec[(('ser','OG'),('rarg','NH1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+19.59,resSelectionSubs('arg','NH1',subs)))
IDSpec[(('ser','CA'),('rarg_i','CZ'))] = cmd.select('ser28', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.83,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('ser','CA'),('rarg_i','NE'))] = cmd.select('ser29', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.93,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('ser','CA'),('rarg_i','NH1'))] = cmd.select('ser30', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.06,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('ser','CB'),('rarg_i','CZ'))] = cmd.select('ser31', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.81,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('ser','CB'),('rarg_i','NE'))] = cmd.select('ser32', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+11.01,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('ser','CB'),('rarg_i','NH1'))] = cmd.select('ser33', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.81,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('ser','OG'),('rarg_i','CZ'))] = cmd.select('ser34', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.66,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('ser','OG'),('rarg_i','NE'))] = cmd.select('ser35', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+11.87,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('ser','OG'),('rarg_i','NH1'))] = cmd.select('ser36', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.66,resSelectionSubs('arg_i','NH1',subs)))
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
IDSpec[(('arg','CZ'),('sasp','CG'))] = cmd.select('arg1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+23.19,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD1'))] = cmd.select('arg2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+23.81,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sasp','OD2'))] = cmd.select('arg3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+23.57,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','CG'))] = cmd.select('arg4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+22.59,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD1'))] = cmd.select('arg5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+23.25,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NE'),('sasp','OD2'))] = cmd.select('arg6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+22.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','CG'))] = cmd.select('arg7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+24.01,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD1'))] = cmd.select('arg8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+24.65,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sasp','OD2'))] = cmd.select('arg9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+24.40,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','CD'))] = cmd.select('arg10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.52,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE1'))] = cmd.select('arg11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.83,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','CZ'),('sglu','OE2'))] = cmd.select('arg12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.53,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','CD'))] = cmd.select('arg13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.54,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE1'))] = cmd.select('arg14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+8.91,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NE'),('sglu','OE2'))] = cmd.select('arg15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+7.61,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','CD'))] = cmd.select('arg16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.44,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE1'))] = cmd.select('arg17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.62,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg','NH1'),('sglu','OE2'))] = cmd.select('arg18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.54,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CA'))] = cmd.select('arg19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+17.21,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','CB'))] = cmd.select('arg20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.18,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','CZ'),('sser','OG'))] = cmd.select('arg21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+18.35,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CA'))] = cmd.select('arg22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+16.24,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','CB'))] = cmd.select('arg23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.27,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NE'),('sser','OG'))] = cmd.select('arg24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+17.42,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CA'))] = cmd.select('arg25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+18.41,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','CB'))] = cmd.select('arg26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.41,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg','NH1'),('sser','OG'))] = cmd.select('arg27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+19.59,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg','CZ'),('rarg_i','CZ'))] = cmd.select('arg28', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.98,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NE'))] = cmd.select('arg29', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.43,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','CZ'),('rarg_i','NH1'))] = cmd.select('arg30', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+12.33,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NE'),('rarg_i','CZ'))] = cmd.select('arg31', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.26,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NE'),('rarg_i','NE'))] = cmd.select('arg32', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.72,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NE'),('rarg_i','NH1'))] = cmd.select('arg33', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.73,resSelectionSubs('arg_i','NH1',subs)))
IDSpec[(('arg','NH1'),('rarg_i','CZ'))] = cmd.select('arg34', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.06,resSelectionSubs('arg_i','CZ',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NE'))] = cmd.select('arg35', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.42,resSelectionSubs('arg_i','NE',subs)))
IDSpec[(('arg','NH1'),('rarg_i','NH1'))] = cmd.select('arg36', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.43,resSelectionSubs('arg_i','NH1',subs)))
IDSpec['arg'] = cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14&br. arg15&br. arg16&br. arg17&br. arg18&br. arg19&br. arg20&br. arg21&br. arg22&br. arg23&br. arg24&br. arg25&br. arg26&br. arg27&br. arg28&br. arg29&br. arg30&br. arg31&br. arg32&br. arg33&br. arg34&br. arg35&br. arg36')
IDSpec['r_arg'] = cmd.count_atoms(resSelectionSubs('arg', subs=subs, selection=True))
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.delete('arg15')
cmd.delete('arg16')
cmd.delete('arg17')
cmd.delete('arg18')
cmd.delete('arg19')
cmd.delete('arg20')
cmd.delete('arg21')
cmd.delete('arg22')
cmd.delete('arg23')
cmd.delete('arg24')
cmd.delete('arg25')
cmd.delete('arg26')
cmd.delete('arg27')
cmd.delete('arg28')
cmd.delete('arg29')
cmd.delete('arg30')
cmd.delete('arg31')
cmd.delete('arg32')
cmd.delete('arg33')
cmd.delete('arg34')
cmd.delete('arg35')
cmd.delete('arg36')
IDSpec[(('arg_i','CZ'),('sasp','CG'))] = cmd.select('arg_i1', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','OD1'))] = cmd.select('arg_i2', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.55,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sasp','OD2'))] = cmd.select('arg_i3', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+14.31,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','CG'))] = cmd.select('arg_i4', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.04,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','OD1'))] = cmd.select('arg_i5', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.66,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sasp','OD2'))] = cmd.select('arg_i6', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+14.35,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','CG'))] = cmd.select('arg_i7', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.95,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','OD1'))] = cmd.select('arg_i8', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.38,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sasp','OD2'))] = cmd.select('arg_i9', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+14.37,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sglu','CD'))] = cmd.select('arg_i10', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+5.91,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sglu','OE1'))] = cmd.select('arg_i11', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.53,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sglu','OE2'))] = cmd.select('arg_i12', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+6.01,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sglu','CD'))] = cmd.select('arg_i13', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.17,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sglu','OE1'))] = cmd.select('arg_i14', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.51,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sglu','OE2'))] = cmd.select('arg_i15', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+5.41,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sglu','CD'))] = cmd.select('arg_i16', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.04,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sglu','OE1'))] = cmd.select('arg_i17', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+7.69,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sglu','OE2'))] = cmd.select('arg_i18', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+6.91,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sser','CA'))] = cmd.select('arg_i19', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+8.83,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sser','CB'))] = cmd.select('arg_i20', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+9.81,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sser','OG'))] = cmd.select('arg_i21', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+10.66,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sser','CA'))] = cmd.select('arg_i22', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+9.93,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sser','CB'))] = cmd.select('arg_i23', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.01,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sser','OG'))] = cmd.select('arg_i24', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.87,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sser','CA'))] = cmd.select('arg_i25', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.06,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sser','CB'))] = cmd.select('arg_i26', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+9.81,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sser','OG'))] = cmd.select('arg_i27', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+10.66,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','CZ'))] = cmd.select('arg_i28', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.98,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NE'))] = cmd.select('arg_i29', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+11.26,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','CZ'),('sarg','NH1'))] = cmd.select('arg_i30', '%s w. %s of %s'%(resSelectionSubs('arg','CZ',subs),d+13.06,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','CZ'))] = cmd.select('arg_i31', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+11.43,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NE'))] = cmd.select('arg_i32', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+10.72,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NE'),('sarg','NH1'))] = cmd.select('arg_i33', '%s w. %s of %s'%(resSelectionSubs('arg','NE',subs),d+12.42,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','CZ'))] = cmd.select('arg_i34', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+12.33,resSelectionSubs('arg','CZ',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NE'))] = cmd.select('arg_i35', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+11.73,resSelectionSubs('arg','NE',subs,selection=True)))
IDSpec[(('arg_i','NH1'),('sarg','NH1'))] = cmd.select('arg_i36', '%s w. %s of %s'%(resSelectionSubs('arg','NH1',subs),d+13.43,resSelectionSubs('arg','NH1',subs,selection=True)))
IDSpec['arg_i'] = cmd.select('arg_i',' br. arg_i1&br. arg_i2&br. arg_i3&br. arg_i4&br. arg_i5&br. arg_i6&br. arg_i7&br. arg_i8&br. arg_i9&br. arg_i10&br. arg_i11&br. arg_i12&br. arg_i13&br. arg_i14&br. arg_i15&br. arg_i16&br. arg_i17&br. arg_i18&br. arg_i19&br. arg_i20&br. arg_i21&br. arg_i22&br. arg_i23&br. arg_i24&br. arg_i25&br. arg_i26&br. arg_i27&br. arg_i28&br. arg_i29&br. arg_i30&br. arg_i31&br. arg_i32&br. arg_i33&br. arg_i34&br. arg_i35&br. arg_i36')
IDSpec['r_arg_i'] = cmd.count_atoms(resSelectionSubs('arg_i', subs=subs, selection=True))
cmd.delete('arg_i1')
cmd.delete('arg_i2')
cmd.delete('arg_i3')
cmd.delete('arg_i4')
cmd.delete('arg_i5')
cmd.delete('arg_i6')
cmd.delete('arg_i7')
cmd.delete('arg_i8')
cmd.delete('arg_i9')
cmd.delete('arg_i10')
cmd.delete('arg_i11')
cmd.delete('arg_i12')
cmd.delete('arg_i13')
cmd.delete('arg_i14')
cmd.delete('arg_i15')
cmd.delete('arg_i16')
cmd.delete('arg_i17')
cmd.delete('arg_i18')
cmd.delete('arg_i19')
cmd.delete('arg_i20')
cmd.delete('arg_i21')
cmd.delete('arg_i22')
cmd.delete('arg_i23')
cmd.delete('arg_i24')
cmd.delete('arg_i25')
cmd.delete('arg_i26')
cmd.delete('arg_i27')
cmd.delete('arg_i28')
cmd.delete('arg_i29')
cmd.delete('arg_i30')
cmd.delete('arg_i31')
cmd.delete('arg_i32')
cmd.delete('arg_i33')
cmd.delete('arg_i34')
cmd.delete('arg_i35')
cmd.delete('arg_i36')
IDSpec['S_1ses_6_1_1_11'] = cmd.select('S_1ses_6_1_1_11', 'asp|glu|ser|arg|arg_i')
cmd.delete('asp')
cmd.delete('glu')
cmd.delete('ser')
cmd.delete('arg')
cmd.delete('arg_i')
