'''
FUNC:S_2gmx_2_7_11_24
PDB:2gmx
EC:2.7.11.24
RESI:asp,lys,ser,asn,thr
LOCI:a-151,153,155,156,188;
'''
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.40,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.69,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.61,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.82,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.94,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.06,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.47,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.40,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.87,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rlys','CD'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.07,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CA'),('rlys','CE'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.91,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CA'),('rlys','NZ'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.23,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CB'),('rlys','CD'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.25,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','CB'),('rlys','CE'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.91,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','CB'),('rlys','NZ'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.06,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','OG'),('rlys','CD'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.35,resSelectionSubs('lys','CD',subs)))
IDSpec[(('ser','OG'),('rlys','CE'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.34,resSelectionSubs('lys','CE',subs)))
IDSpec[(('ser','OG'),('rlys','NZ'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+7.35,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('ser','CA'),('rthr','CA'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+11.91,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','CA'),('rthr','CB'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.48,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','CA'),('rthr','OG1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.12,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','CB'),('rthr','CA'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.74,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','CB'),('rthr','CB'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.36,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','CB'),('rthr','OG1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.17,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','OG'),('rthr','CA'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.39,resSelectionSubs('thr','CA',subs)))
IDSpec[(('ser','OG'),('rthr','CB'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.99,resSelectionSubs('thr','CB',subs)))
IDSpec[(('ser','OG'),('rthr','OG1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.02,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('ser','CA'),('rasn','CG'))] = cmd.select('ser28', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.36,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ser','CA'),('rasn','ND2'))] = cmd.select('ser29', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+8.66,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ser','CA'),('rasn','OD1'))] = cmd.select('ser30', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.07,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ser','CB'),('rasn','CG'))] = cmd.select('ser31', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.57,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ser','CB'),('rasn','ND2'))] = cmd.select('ser32', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.88,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ser','CB'),('rasn','OD1'))] = cmd.select('ser33', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+7.08,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('ser','OG'),('rasn','CG'))] = cmd.select('ser34', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.83,resSelectionSubs('asn','CG',subs)))
IDSpec[(('ser','OG'),('rasn','ND2'))] = cmd.select('ser35', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+10.11,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('ser','OG'),('rasn','OD1'))] = cmd.select('ser36', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.39,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.40,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.82,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.47,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.69,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.94,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.40,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.61,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.06,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.87,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('rlys','CD'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.60,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','CG'),('rlys','CE'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.23,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','CG'),('rlys','NZ'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.01,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD1'),('rlys','CD'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.35,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD1'),('rlys','CE'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.09,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD1'),('rlys','NZ'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.55,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','OD2'),('rlys','CD'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.46,resSelectionSubs('lys','CD',subs)))
IDSpec[(('asp','OD2'),('rlys','CE'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.76,resSelectionSubs('lys','CE',subs)))
IDSpec[(('asp','OD2'),('rlys','NZ'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.71,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('asp','CG'),('rthr','CA'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.12,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','CG'),('rthr','CB'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.68,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','CG'),('rthr','OG1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.47,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD1'),('rthr','CA'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.92,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD1'),('rthr','CB'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.64,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD1'),('rthr','OG1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.52,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','OD2'),('rthr','CA'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.75,resSelectionSubs('thr','CA',subs)))
IDSpec[(('asp','OD2'),('rthr','CB'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.16,resSelectionSubs('thr','CB',subs)))
IDSpec[(('asp','OD2'),('rthr','OG1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.06,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('asp','CG'),('rasn','CG'))] = cmd.select('asp28', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.04,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','CG'),('rasn','ND2'))] = cmd.select('asp29', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.88,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','CG'),('rasn','OD1'))] = cmd.select('asp30', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.29,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD1'),('rasn','CG'))] = cmd.select('asp31', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.00,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD1'),('rasn','ND2'))] = cmd.select('asp32', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.00,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD1'),('rasn','OD1'))] = cmd.select('asp33', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.12,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('asp','OD2'),('rasn','CG'))] = cmd.select('asp34', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.99,resSelectionSubs('asn','CG',subs)))
IDSpec[(('asp','OD2'),('rasn','ND2'))] = cmd.select('asp35', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.91,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('asp','OD2'),('rasn','OD1'))] = cmd.select('asp36', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.11,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('lys','CD'),('sser','CA'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.07,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','CB'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.25,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CD'),('sser','OG'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.35,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CA'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.91,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','CB'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.91,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','CE'),('sser','OG'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.34,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CA'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.23,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','CB'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.06,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('lys','NZ'),('sser','OG'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.35,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','CG'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.60,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD1'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.35,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CD'),('sasp','OD2'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.46,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','CG'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.23,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD1'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.09,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','CE'),('sasp','OD2'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.76,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','CG'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.01,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD1'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.55,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('lys','NZ'),('sasp','OD2'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.71,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('lys','CD'),('rthr','CA'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.12,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CD'),('rthr','CB'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.73,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CD'),('rthr','OG1'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.08,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CE'),('rthr','CA'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.53,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','CE'),('rthr','CB'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.34,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','CE'),('rthr','OG1'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.79,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','NZ'),('rthr','CA'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.62,resSelectionSubs('thr','CA',subs)))
IDSpec[(('lys','NZ'),('rthr','CB'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.72,resSelectionSubs('thr','CB',subs)))
IDSpec[(('lys','NZ'),('rthr','OG1'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.39,resSelectionSubs('thr','OG1',subs)))
IDSpec[(('lys','CD'),('rasn','CG'))] = cmd.select('lys28', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.43,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CD'),('rasn','ND2'))] = cmd.select('lys29', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+8.27,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CD'),('rasn','OD1'))] = cmd.select('lys30', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.42,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','CE'),('rasn','CG'))] = cmd.select('lys31', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.73,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','CE'),('rasn','ND2'))] = cmd.select('lys32', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.62,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','CE'),('rasn','OD1'))] = cmd.select('lys33', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.43,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('lys','NZ'),('rasn','CG'))] = cmd.select('lys34', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.67,resSelectionSubs('asn','CG',subs)))
IDSpec[(('lys','NZ'),('rasn','ND2'))] = cmd.select('lys35', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+8.39,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('lys','NZ'),('rasn','OD1'))] = cmd.select('lys36', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.25,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('thr','CA'),('sser','CA'))] = cmd.select('thr1', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.91,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','CB'))] = cmd.select('thr2', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.74,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','CA'),('sser','OG'))] = cmd.select('thr3', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+10.39,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','CA'))] = cmd.select('thr4', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.48,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','CB'))] = cmd.select('thr5', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+9.36,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','CB'),('sser','OG'))] = cmd.select('thr6', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.99,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','CA'))] = cmd.select('thr7', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.12,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','CB'))] = cmd.select('thr8', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.17,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('thr','OG1'),('sser','OG'))] = cmd.select('thr9', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.02,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','CG'))] = cmd.select('thr10', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.12,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD1'))] = cmd.select('thr11', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.92,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CA'),('sasp','OD2'))] = cmd.select('thr12', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+8.75,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','CG'))] = cmd.select('thr13', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+7.68,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD1'))] = cmd.select('thr14', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.64,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','CB'),('sasp','OD2'))] = cmd.select('thr15', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+8.16,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','CG'))] = cmd.select('thr16', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+6.47,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD1'))] = cmd.select('thr17', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.52,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('thr','OG1'),('sasp','OD2'))] = cmd.select('thr18', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+7.06,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CD'))] = cmd.select('thr19', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.12,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','CE'))] = cmd.select('thr20', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+7.53,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CA'),('slys','NZ'))] = cmd.select('thr21', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+6.62,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CD'))] = cmd.select('thr22', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.73,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','CE'))] = cmd.select('thr23', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+6.34,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','CB'),('slys','NZ'))] = cmd.select('thr24', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+5.72,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CD'))] = cmd.select('thr25', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.08,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','CE'))] = cmd.select('thr26', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.79,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('thr','OG1'),('slys','NZ'))] = cmd.select('thr27', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+5.39,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('thr','CA'),('rasn','CG'))] = cmd.select('thr28', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.76,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CA'),('rasn','ND2'))] = cmd.select('thr29', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+12.23,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CA'),('rasn','OD1'))] = cmd.select('thr30', '%s w. %s of %s'%(resSelectionSubs('thr','CA',subs),d+11.63,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','CB'),('rasn','CG'))] = cmd.select('thr31', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.71,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','CB'),('rasn','ND2'))] = cmd.select('thr32', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+11.30,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','CB'),('rasn','OD1'))] = cmd.select('thr33', '%s w. %s of %s'%(resSelectionSubs('thr','CB',subs),d+10.61,resSelectionSubs('asn','OD1',subs)))
IDSpec[(('thr','OG1'),('rasn','CG'))] = cmd.select('thr34', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.70,resSelectionSubs('asn','CG',subs)))
IDSpec[(('thr','OG1'),('rasn','ND2'))] = cmd.select('thr35', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+10.18,resSelectionSubs('asn','ND2',subs)))
IDSpec[(('thr','OG1'),('rasn','OD1'))] = cmd.select('thr36', '%s w. %s of %s'%(resSelectionSubs('thr','OG1',subs),d+9.75,resSelectionSubs('asn','OD1',subs)))
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
IDSpec[(('asn','CG'),('sser','CA'))] = cmd.select('asn1', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.36,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sser','CB'))] = cmd.select('asn2', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.57,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sser','OG'))] = cmd.select('asn3', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.83,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sser','CA'))] = cmd.select('asn4', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.66,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sser','CB'))] = cmd.select('asn5', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.88,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sser','OG'))] = cmd.select('asn6', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.11,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sser','CA'))] = cmd.select('asn7', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.07,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sser','CB'))] = cmd.select('asn8', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.08,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sser','OG'))] = cmd.select('asn9', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.39,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','CG'))] = cmd.select('asn10', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.04,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD1'))] = cmd.select('asn11', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+8.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','CG'),('sasp','OD2'))] = cmd.select('asn12', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+5.99,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','CG'))] = cmd.select('asn13', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+6.88,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD1'))] = cmd.select('asn14', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.00,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sasp','OD2'))] = cmd.select('asn15', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+5.91,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','CG'))] = cmd.select('asn16', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.29,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD1'))] = cmd.select('asn17', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+8.12,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sasp','OD2'))] = cmd.select('asn18', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.11,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CD'))] = cmd.select('asn19', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.43,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','CE'))] = cmd.select('asn20', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+6.73,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','CG'),('slys','NZ'))] = cmd.select('asn21', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+7.67,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CD'))] = cmd.select('asn22', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.27,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','CE'))] = cmd.select('asn23', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+7.62,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','ND2'),('slys','NZ'))] = cmd.select('asn24', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+8.39,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CD'))] = cmd.select('asn25', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.42,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','CE'))] = cmd.select('asn26', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+6.43,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asn','OD1'),('slys','NZ'))] = cmd.select('asn27', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+7.25,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CA'))] = cmd.select('asn28', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+11.76,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','CB'))] = cmd.select('asn29', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+10.71,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','CG'),('sthr','OG1'))] = cmd.select('asn30', '%s w. %s of %s'%(resSelectionSubs('asn','CG',subs),d+9.70,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CA'))] = cmd.select('asn31', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+12.23,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','CB'))] = cmd.select('asn32', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+11.30,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','ND2'),('sthr','OG1'))] = cmd.select('asn33', '%s w. %s of %s'%(resSelectionSubs('asn','ND2',subs),d+10.18,resSelectionSubs('thr','OG1',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CA'))] = cmd.select('asn34', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+11.63,resSelectionSubs('thr','CA',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','CB'))] = cmd.select('asn35', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+10.61,resSelectionSubs('thr','CB',subs,selection=True)))
IDSpec[(('asn','OD1'),('sthr','OG1'))] = cmd.select('asn36', '%s w. %s of %s'%(resSelectionSubs('asn','OD1',subs),d+9.75,resSelectionSubs('thr','OG1',subs,selection=True)))
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
IDSpec['S_2gmx_2_7_11_24'] = cmd.select('S_2gmx_2_7_11_24', 'ser|asp|lys|thr|asn')
cmd.delete('ser')
cmd.delete('asp')
cmd.delete('lys')
cmd.delete('thr')
cmd.delete('asn')
