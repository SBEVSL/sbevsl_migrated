'''
FUNC:S_3a62_2_7_11_1
PDB:3a62
EC:2.7.11.1
RESI:asp,lys,glu,asn,thr
LOCI:a-218,220,222,223,256;
'''
IDSpec[(('asp','CG'),('rglu','CD'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.08,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','CG'),('rglu','OE1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.00,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','CG'),('rglu','OE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.65,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD1'),('rglu','CD'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.45,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD1'),('rglu','OE1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.20,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD1'),('rglu','OE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.12,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','OD2'),('rglu','CD'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.95,resSelectionSubs('glu','CD',subs)))
IDSpec[(('asp','OD2'),('rglu','OE1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.03,resSelectionSubs('glu','OE1',subs)))
IDSpec[(('asp','OD2'),('rglu','OE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.35,resSelectionSubs('glu','OE2',subs)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.26,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.86,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.99,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.02,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.78,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.13,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.05,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.30,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.16,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rthr','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.06,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','CG'),('rthr','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.16,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','CG'),('rthr','OG1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.46,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD1'),('rthr','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.96,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD1'),('rthr','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.82,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD1'),('rthr','OG1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.96,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD2'),('rthr','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.23,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD2'),('rthr','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.50,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD2'),('rthr','OG1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.99,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.45,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.26,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.27,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.61,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.60,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.47,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.58,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.39,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.19,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('glu','CD'),('sasp','CG'))] = cmd.select('glu1', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+10.08,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD1'))] = cmd.select('glu2', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.45,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','CD'),('sasp','OD2'))] = cmd.select('glu3', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.95,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','CG'))] = cmd.select('glu4', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.00,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD1'))] = cmd.select('glu5', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.20,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE1'),('sasp','OD2'))] = cmd.select('glu6', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+10.03,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','CG'))] = cmd.select('glu7', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.65,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD1'))] = cmd.select('glu8', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('glu','OE2'),('sasp','OD2'))] = cmd.select('glu9', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+9.35,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('glu','CD'),('rlys','CD'))] = cmd.select('glu10', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.14,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','CD'),('rlys','CE'))] = cmd.select('glu11', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+6.85,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','CD'),('rlys','NZ'))] = cmd.select('glu12', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+7.11,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE1'),('rlys','CD'))] = cmd.select('glu13', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+6.45,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE1'),('rlys','CE'))] = cmd.select('glu14', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.19,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE1'),('rlys','NZ'))] = cmd.select('glu15', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+7.74,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','OE2'),('rlys','CD'))] = cmd.select('glu16', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+5.73,resSelectionSubs('lys','CD',subs)))
IDSpec[(('glu','OE2'),('rlys','CE'))] = cmd.select('glu17', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.11,resSelectionSubs('lys','CE',subs)))
IDSpec[(('glu','OE2'),('rlys','NZ'))] = cmd.select('glu18', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+6.13,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('glu','CD'),('rthr','CA'))] = cmd.select('glu19', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.73,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','CD'),('rthr','CB'))] = cmd.select('glu20', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.54,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','CD'),('rthr','OG1'))] = cmd.select('glu21', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.07,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE1'),('rthr','CA'))] = cmd.select('glu22', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.98,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE1'),('rthr','CB'))] = cmd.select('glu23', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.69,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE1'),('rthr','OG1'))] = cmd.select('glu24', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.98,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','OE2'),('rthr','CA'))] = cmd.select('glu25', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.63,resSelectionSubs('thr','CA',subs)))
IDSpec[(('glu','OE2'),('rthr','CB'))] = cmd.select('glu26', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+7.50,resSelectionSubs('thr','CB',subs)))
IDSpec[(('glu','OE2'),('rthr','OG1'))] = cmd.select('glu27', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.20,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('glu','CD'),('rasn','CG'))] = cmd.select('glu28', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.55,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','CD'),('rasn','ND2'))] = cmd.select('glu29', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+9.03,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','CD'),('rasn','OD1'))] = cmd.select('glu30', '%s w. %s of %s'%(resSelectionSubs('glu','CD',subs),d+8.31,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE1'),('rasn','CG'))] = cmd.select('glu31', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.87,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE1'),('rasn','ND2'))] = cmd.select('glu32', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+9.29,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE1'),('rasn','OD1'))] = cmd.select('glu33', '%s w. %s of %s'%(resSelectionSubs('glu','OE1',subs),d+8.84,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('glu','OE2'),('rasn','CG'))] = cmd.select('glu34', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.59,resSelectionSubs('asn','CG',subs)))
IDSpec[(('glu','OE2'),('rasn','ND2'))] = cmd.select('glu35', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.90,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('glu','OE2'),('rasn','OD1'))] = cmd.select('glu36', '%s w. %s of %s'%(resSelectionSubs('glu','OE2',subs),d+8.30,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.26,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.02,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.05,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.86,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.78,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.30,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.99,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.13,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.16,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','CD'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.14,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.45,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CD'),('sglu','OE2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.73,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','CD'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.85,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.19,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','CE'),('sglu','OE2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.11,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','CD'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.11,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.74,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sglu','OE2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.13,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('lys','CD'),('rthr','CA'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.55,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CD'),('rthr','CB'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.02,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CD'),('rthr','OG1'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.73,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CE'),('rthr','CA'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.15,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CE'),('rthr','CB'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.82,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CE'),('rthr','OG1'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.64,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr','CA'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.88,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','NZ'),('rthr','CB'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.73,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','NZ'),('rthr','OG1'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.84,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CD'),('rasn','CG'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.67,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CD'),('rasn','ND2'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.46,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CD'),('rasn','OD1'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.84,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','CE'),('rasn','CG'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.83,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CE'),('rasn','ND2'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.32,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CE'),('rasn','OD1'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.97,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','NZ'),('rasn','CG'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.38,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','NZ'),('rasn','ND2'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.98,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','NZ'),('rasn','OD1'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.19,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('thr','CA'),('sasp','CG'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.06,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD1'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.96,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD2'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.23,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','CG'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.16,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD1'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.82,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD2'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.50,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','CG'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.46,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD1'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.96,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD2'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.99,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','CD'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.73,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+9.98,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CA'),('sglu','OE2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.63,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','CD'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.54,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.69,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','CB'),('sglu','OE2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.50,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','CD'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.07,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.98,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sglu','OE2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.20,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CD'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.55,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.15,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','NZ'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.88,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CD'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.02,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.82,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','NZ'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.73,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CD'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+8.73,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.64,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','NZ'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.84,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CA'),('rasn','CG'))] = cmd.select('thr28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.96,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CA'),('rasn','ND2'))] = cmd.select('thr29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.31,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CA'),('rasn','OD1'))] = cmd.select('thr30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.98,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','CB'),('rasn','CG'))] = cmd.select('thr31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.62,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CB'),('rasn','ND2'))] = cmd.select('thr32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.13,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CB'),('rasn','OD1'))] = cmd.select('thr33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.65,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','OG1'),('rasn','CG'))] = cmd.select('thr34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.36,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','OG1'),('rasn','ND2'))] = cmd.select('thr35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+11.83,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','OG1'),('rasn','OD1'))] = cmd.select('thr36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+12.51,resSelectionSubs('asn','OD1',subs)))
IDSpec['thr'] = cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18&br. thr19&br. thr20&br. thr21&br. thr22&br. thr23&br. thr24&br. thr25&br. thr26&br. thr27&br. thr28&br. thr29&br. thr30&br. thr31&br. thr32&br. thr33&br. thr34&br. thr35&br. thr36')
IDSpec['r_thr'] = cmd.count_atoms(resSelectionSubs('thr', subs=subs, selection=True))
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
cmd.delete('thr19')
cmd.delete('thr20')
cmd.delete('thr21')
cmd.delete('thr22')
cmd.delete('thr23')
cmd.delete('thr24')
cmd.delete('thr25')
cmd.delete('thr26')
cmd.delete('thr27')
cmd.delete('thr28')
cmd.delete('thr29')
cmd.delete('thr30')
cmd.delete('thr31')
cmd.delete('thr32')
cmd.delete('thr33')
cmd.delete('thr34')
cmd.delete('thr35')
cmd.delete('thr36')
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.45,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.61,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.58,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.26,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.60,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.39,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.27,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.47,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.19,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','CD'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.55,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.87,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','CG'),('sglu','OE2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.59,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','CD'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.03,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+9.29,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sglu','OE2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.90,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','CD'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.31,resSelectionSubs('glu','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.84,resSelectionSubs('glu','OE1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sglu','OE2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.30,resSelectionSubs('glu','OE2',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CD'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.67,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CE'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.83,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','NZ'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.38,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CD'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.46,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CE'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.32,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','NZ'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.98,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CD'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+5.84,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CE'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.97,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','NZ'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.19,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CA'))] = cmd.select('asn28', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.96,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CB'))] = cmd.select('asn29', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.62,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','OG1'))] = cmd.select('asn30', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+12.36,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CA'))] = cmd.select('asn31', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.31,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CB'))] = cmd.select('asn32', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.13,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','OG1'))] = cmd.select('asn33', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.83,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CA'))] = cmd.select('asn34', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.98,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CB'))] = cmd.select('asn35', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.65,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','OG1'))] = cmd.select('asn36', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+12.51,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec['asn'] = cmd.select('asn',' br. asn1&br. asn2&br. asn3&br. asn4&br. asn5&br. asn6&br. asn7&br. asn8&br. asn9&br. asn10&br. asn11&br. asn12&br. asn13&br. asn14&br. asn15&br. asn16&br. asn17&br. asn18&br. asn19&br. asn20&br. asn21&br. asn22&br. asn23&br. asn24&br. asn25&br. asn26&br. asn27&br. asn28&br. asn29&br. asn30&br. asn31&br. asn32&br. asn33&br. asn34&br. asn35&br. asn36')
IDSpec['r_asn'] = cmd.count_atoms(resSelectionSubs('asn', subs=subs, selection=True))
cmd.delete('asn1')
cmd.delete('asn2')
cmd.delete('asn3')
cmd.delete('asn4')
cmd.delete('asn5')
cmd.delete('asn6')
cmd.delete('asn7')
cmd.delete('asn8')
cmd.delete('asn9')
cmd.delete('asn10')
cmd.delete('asn11')
cmd.delete('asn12')
cmd.delete('asn13')
cmd.delete('asn14')
cmd.delete('asn15')
cmd.delete('asn16')
cmd.delete('asn17')
cmd.delete('asn18')
cmd.delete('asn19')
cmd.delete('asn20')
cmd.delete('asn21')
cmd.delete('asn22')
cmd.delete('asn23')
cmd.delete('asn24')
cmd.delete('asn25')
cmd.delete('asn26')
cmd.delete('asn27')
cmd.delete('asn28')
cmd.delete('asn29')
cmd.delete('asn30')
cmd.delete('asn31')
cmd.delete('asn32')
cmd.delete('asn33')
cmd.delete('asn34')
cmd.delete('asn35')
cmd.delete('asn36')
IDSpec['S_3a62_2_7_11_1'] = cmd.select('S_3a62_2_7_11_1', 'asp|glu|lys|thr|asn')
cmd.delete('asp')
cmd.delete('glu')
cmd.delete('lys')
cmd.delete('thr')
cmd.delete('asn')
