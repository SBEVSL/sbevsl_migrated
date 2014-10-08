'''
FUNC:S_3fvr_3_1_1_6
PDB:3fvr
EC:3.1.1.6
RESI:ser,gln,asp,his
LOCI:a-181,182,269,298;
'''
IDSpec[(('ser','CA'),('rasp','CG'))] = cmd.select('ser1', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.28,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CA'),('rasp','OD1'))] = cmd.select('ser2', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.31,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CA'),('rasp','OD2'))] = cmd.select('ser3', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.36,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CB'),('rasp','CG'))] = cmd.select('ser4', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.79,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','CB'),('rasp','OD1'))] = cmd.select('ser5', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.67,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','CB'),('rasp','OD2'))] = cmd.select('ser6', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+8.94,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','OG'),('rasp','CG'))] = cmd.select('ser7', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.34,resSelectionSubs('asp','CG',subs)))
IDSpec[(('ser','OG'),('rasp','OD1'))] = cmd.select('ser8', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.03,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('ser','OG'),('rasp','OD2'))] = cmd.select('ser9', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+8.68,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('ser','CA'),('rhis','CE1'))] = cmd.select('ser10', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.26,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CA'),('rhis','ND1'))] = cmd.select('ser11', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+7.41,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CA'),('rhis','NE2'))] = cmd.select('ser12', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+6.60,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CB'),('rhis','CE1'))] = cmd.select('ser13', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.30,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','CB'),('rhis','ND1'))] = cmd.select('ser14', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+6.56,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','CB'),('rhis','NE2'))] = cmd.select('ser15', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+5.30,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','OG'),('rhis','CE1'))] = cmd.select('ser16', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.94,resSelectionSubs('his','CE1',subs)))
IDSpec[(('ser','OG'),('rhis','ND1'))] = cmd.select('ser17', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+6.25,resSelectionSubs('his','ND1',subs)))
IDSpec[(('ser','OG'),('rhis','NE2'))] = cmd.select('ser18', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+4.96,resSelectionSubs('his','NE2',subs)))
IDSpec[(('ser','CA'),('rgln','CD'))] = cmd.select('ser19', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.45,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CA'),('rgln','NE2'))] = cmd.select('ser20', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+9.88,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CA'),('rgln','OE1'))] = cmd.select('ser21', '%s w. %s of %s'%(resSelectionSubs('ser','CA',subs),d+10.20,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','CB'),('rgln','CD'))] = cmd.select('ser22', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.33,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','CB'),('rgln','NE2'))] = cmd.select('ser23', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+9.63,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','CB'),('rgln','OE1'))] = cmd.select('ser24', '%s w. %s of %s'%(resSelectionSubs('ser','CB',subs),d+10.04,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('ser','OG'),('rgln','CD'))] = cmd.select('ser25', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.35,resSelectionSubs('gln','CD',subs)))
IDSpec[(('ser','OG'),('rgln','NE2'))] = cmd.select('ser26', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.81,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('ser','OG'),('rgln','OE1'))] = cmd.select('ser27', '%s w. %s of %s'%(resSelectionSubs('ser','OG',subs),d+9.87,resSelectionSubs('gln','OE1',subs)))
IDSpec['ser'] = cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22&br. ser23&br. ser24&br. ser25&br. ser26&br. ser27')
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
IDSpec[(('asp','CG'),('sser','CA'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.28,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','CB'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.79,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','CG'),('sser','OG'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.34,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CA'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.31,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','CB'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.67,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD1'),('sser','OG'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+9.03,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CA'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.36,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','CB'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.94,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('asp','OD2'),('sser','OG'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.68,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('asp','CG'),('rhis','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.69,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','CG'),('rhis','ND1'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.52,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','CG'),('rhis','NE2'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.59,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD1'),('rhis','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.48,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD1'),('rhis','ND1'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.41,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD1'),('rhis','NE2'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.24,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','OD2'),('rhis','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.00,resSelectionSubs('his','CE1',subs)))
IDSpec[(('asp','OD2'),('rhis','ND1'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.86,resSelectionSubs('his','ND1',subs)))
IDSpec[(('asp','OD2'),('rhis','NE2'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.00,resSelectionSubs('his','NE2',subs)))
IDSpec[(('asp','CG'),('rgln','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+16.66,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','CG'),('rgln','NE2'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.08,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','CG'),('rgln','OE1'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+17.07,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD1'),('rgln','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.22,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD1'),('rgln','NE2'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.66,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD1'),('rgln','OE1'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+16.55,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('asp','OD2'),('rgln','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.02,resSelectionSubs('gln','CD',subs)))
IDSpec[(('asp','OD2'),('rgln','NE2'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.41,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('asp','OD2'),('rgln','OE1'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+16.52,resSelectionSubs('gln','OE1',subs)))
IDSpec['asp'] = cmd.select('asp',' br. asp1&br. asp2&br. asp3&br. asp4&br. asp5&br. asp6&br. asp7&br. asp8&br. asp9&br. asp10&br. asp11&br. asp12&br. asp13&br. asp14&br. asp15&br. asp16&br. asp17&br. asp18&br. asp19&br. asp20&br. asp21&br. asp22&br. asp23&br. asp24&br. asp25&br. asp26&br. asp27')
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
IDSpec[(('his','CE1'),('sser','CA'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.26,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','CB'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.30,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','CE1'),('sser','OG'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+4.94,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CA'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.41,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','CB'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.56,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','ND1'),('sser','OG'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.25,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CA'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.60,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','CB'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.30,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('his','NE2'),('sser','OG'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+4.96,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','CG'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.69,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD1'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.48,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','CE1'),('sasp','OD2'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','CG'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.52,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD1'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.41,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','ND1'),('sasp','OD2'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+4.86,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','CG'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.59,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD1'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.24,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('his','NE2'),('sasp','OD2'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.00,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('his','CE1'),('rgln','CD'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.16,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','CE1'),('rgln','NE2'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.48,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','CE1'),('rgln','OE1'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+12.69,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','ND1'),('rgln','CD'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.47,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','ND1'),('rgln','NE2'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.76,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','ND1'),('rgln','OE1'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+13.99,resSelectionSubs('gln','OE1',subs)))
IDSpec[(('his','NE2'),('rgln','CD'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.65,resSelectionSubs('gln','CD',subs)))
IDSpec[(('his','NE2'),('rgln','NE2'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+11.85,resSelectionSubs('gln','NE2',subs)))
IDSpec[(('his','NE2'),('rgln','OE1'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+12.19,resSelectionSubs('gln','OE1',subs)))
IDSpec['his'] = cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27')
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
IDSpec[(('gln','CD'),('sser','CA'))] = cmd.select('gln1', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.45,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','CB'))] = cmd.select('gln2', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.33,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','CD'),('sser','OG'))] = cmd.select('gln3', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+9.35,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CA'))] = cmd.select('gln4', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.88,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','CB'))] = cmd.select('gln5', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.63,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','NE2'),('sser','OG'))] = cmd.select('gln6', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+9.81,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CA'))] = cmd.select('gln7', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.20,resSelectionSubs('ser','CA',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','CB'))] = cmd.select('gln8', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+10.04,resSelectionSubs('ser','CB',subs,selection=True)))
IDSpec[(('gln','OE1'),('sser','OG'))] = cmd.select('gln9', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+9.87,resSelectionSubs('ser','OG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','CG'))] = cmd.select('gln10', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.66,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD1'))] = cmd.select('gln11', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.22,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','CD'),('sasp','OD2'))] = cmd.select('gln12', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+16.02,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','CG'))] = cmd.select('gln13', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+17.08,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD1'))] = cmd.select('gln14', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.66,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','NE2'),('sasp','OD2'))] = cmd.select('gln15', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+16.41,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','CG'))] = cmd.select('gln16', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+17.07,resSelectionSubs('asp','CG',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD1'))] = cmd.select('gln17', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.55,resSelectionSubs('asp','OD1',subs,selection=True)))
IDSpec[(('gln','OE1'),('sasp','OD2'))] = cmd.select('gln18', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+16.52,resSelectionSubs('asp','OD2',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','CE1'))] = cmd.select('gln19', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+12.16,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','ND1'))] = cmd.select('gln20', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+13.47,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','CD'),('shis','NE2'))] = cmd.select('gln21', '%s w. %s of %s'%(resSelectionSubs('gln','CD',subs),d+11.65,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','CE1'))] = cmd.select('gln22', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+12.48,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','ND1'))] = cmd.select('gln23', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+13.76,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','NE2'),('shis','NE2'))] = cmd.select('gln24', '%s w. %s of %s'%(resSelectionSubs('gln','NE2',subs),d+11.85,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','CE1'))] = cmd.select('gln25', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+12.69,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','ND1'))] = cmd.select('gln26', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+13.99,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('gln','OE1'),('shis','NE2'))] = cmd.select('gln27', '%s w. %s of %s'%(resSelectionSubs('gln','OE1',subs),d+12.19,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec['gln'] = cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10&br. gln11&br. gln12&br. gln13&br. gln14&br. gln15&br. gln16&br. gln17&br. gln18&br. gln19&br. gln20&br. gln21&br. gln22&br. gln23&br. gln24&br. gln25&br. gln26&br. gln27')
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
IDSpec['S_3fvr_3_1_1_6'] = cmd.select('S_3fvr_3_1_1_6', 'ser|asp|his|gln')
cmd.delete('ser')
cmd.delete('asp')
cmd.delete('his')
cmd.delete('gln')
