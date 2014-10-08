'''
FUNC:S_2bgs_1_1_1_21
PDB:2bgs
EC:1.1.1.21
RESI:asp,tyr,lys,his
LOCI:a-55,60,88,121;
'''
IDSpec[(('his','CE1'),('rtyr','CE1'))] = cmd.select('his1', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.63,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','CE1'),('rtyr','CZ'))] = cmd.select('his2', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.24,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','CE1'),('rtyr','OH'))] = cmd.select('his3', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.21,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','ND1'),('rtyr','CE1'))] = cmd.select('his4', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+6.81,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','ND1'),('rtyr','CZ'))] = cmd.select('his5', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.33,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','ND1'),('rtyr','OH'))] = cmd.select('his6', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.27,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','NE2'),('rtyr','CE1'))] = cmd.select('his7', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.00,resSelectionSubs('tyr','CE1',subs)))
IDSpec[(('his','NE2'),('rtyr','CZ'))] = cmd.select('his8', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.46,resSelectionSubs('tyr','CZ',subs)))
IDSpec[(('his','NE2'),('rtyr','OH'))] = cmd.select('his9', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.06,resSelectionSubs('tyr','OH',subs)))
IDSpec[(('his','CE1'),('rlys','CD'))] = cmd.select('his10', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+5.99,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','CE1'),('rlys','CE'))] = cmd.select('his11', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+6.98,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','CE1'),('rlys','NZ'))] = cmd.select('his12', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+7.17,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','ND1'),('rlys','CD'))] = cmd.select('his13', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+5.90,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','ND1'),('rlys','CE'))] = cmd.select('his14', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.20,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','ND1'),('rlys','NZ'))] = cmd.select('his15', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+7.62,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','NE2'),('rlys','CD'))] = cmd.select('his16', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+5.95,resSelectionSubs('lys','CD',subs)))
IDSpec[(('his','NE2'),('rlys','CE'))] = cmd.select('his17', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+6.74,resSelectionSubs('lys','CE',subs)))
IDSpec[(('his','NE2'),('rlys','NZ'))] = cmd.select('his18', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+7.12,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('his','CE1'),('rasp','CG'))] = cmd.select('his19', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.55,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','CE1'),('rasp','OD1'))] = cmd.select('his20', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+10.72,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','CE1'),('rasp','OD2'))] = cmd.select('his21', '%s w. %s of %s'%(resSelectionSubs('his','CE1',subs),d+9.53,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','ND1'),('rasp','CG'))] = cmd.select('his22', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.03,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','ND1'),('rasp','OD1'))] = cmd.select('his23', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+11.05,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','ND1'),('rasp','OD2'))] = cmd.select('his24', '%s w. %s of %s'%(resSelectionSubs('his','ND1',subs),d+10.14,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('his','NE2'),('rasp','CG'))] = cmd.select('his25', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.46,resSelectionSubs('asp','CG',subs)))
IDSpec[(('his','NE2'),('rasp','OD1'))] = cmd.select('his26', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+10.57,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('his','NE2'),('rasp','OD2'))] = cmd.select('his27', '%s w. %s of %s'%(resSelectionSubs('his','NE2',subs),d+9.43,resSelectionSubs('asp','OD2',subs)))
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
IDSpec[(('tyr','CE1'),('shis','CE1'))] = cmd.select('tyr1', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+5.63,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','ND1'))] = cmd.select('tyr2', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.81,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CE1'),('shis','NE2'))] = cmd.select('tyr3', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.00,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','CE1'))] = cmd.select('tyr4', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.24,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','ND1'))] = cmd.select('tyr5', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+7.33,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','CZ'),('shis','NE2'))] = cmd.select('tyr6', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','CE1'))] = cmd.select('tyr7', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.21,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','ND1'))] = cmd.select('tyr8', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.27,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('tyr','OH'),('shis','NE2'))] = cmd.select('tyr9', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.06,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('tyr','CE1'),('rlys','CD'))] = cmd.select('tyr10', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.51,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CE1'),('rlys','CE'))] = cmd.select('tyr11', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+7.60,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CE1'),('rlys','NZ'))] = cmd.select('tyr12', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+6.81,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CZ'),('rlys','CD'))] = cmd.select('tyr13', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.98,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','CZ'),('rlys','CE'))] = cmd.select('tyr14', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.74,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','CZ'),('rlys','NZ'))] = cmd.select('tyr15', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+5.72,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','OH'),('rlys','CD'))] = cmd.select('tyr16', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.30,resSelectionSubs('lys','CD',subs)))
IDSpec[(('tyr','OH'),('rlys','CE'))] = cmd.select('tyr17', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+5.82,resSelectionSubs('lys','CE',subs)))
IDSpec[(('tyr','OH'),('rlys','NZ'))] = cmd.select('tyr18', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+4.98,resSelectionSubs('lys','NZ',subs)))
IDSpec[(('tyr','CE1'),('rasp','CG'))] = cmd.select('tyr19', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+9.36,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD1'))] = cmd.select('tyr20', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+10.03,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CE1'),('rasp','OD2'))] = cmd.select('tyr21', '%s w. %s of %s'%(resSelectionSubs('tyr','CE1',subs),d+8.14,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','CZ'),('rasp','CG'))] = cmd.select('tyr22', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.01,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD1'))] = cmd.select('tyr23', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+8.73,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','CZ'),('rasp','OD2'))] = cmd.select('tyr24', '%s w. %s of %s'%(resSelectionSubs('tyr','CZ',subs),d+6.77,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('tyr','OH'),('rasp','CG'))] = cmd.select('tyr25', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+7.39,resSelectionSubs('asp','CG',subs)))
IDSpec[(('tyr','OH'),('rasp','OD1'))] = cmd.select('tyr26', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+8.00,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('tyr','OH'),('rasp','OD2'))] = cmd.select('tyr27', '%s w. %s of %s'%(resSelectionSubs('tyr','OH',subs),d+6.15,resSelectionSubs('asp','OD2',subs)))
IDSpec['tyr'] = cmd.select('tyr',' br. tyr1&br. tyr2&br. tyr3&br. tyr4&br. tyr5&br. tyr6&br. tyr7&br. tyr8&br. tyr9&br. tyr10&br. tyr11&br. tyr12&br. tyr13&br. tyr14&br. tyr15&br. tyr16&br. tyr17&br. tyr18&br. tyr19&br. tyr20&br. tyr21&br. tyr22&br. tyr23&br. tyr24&br. tyr25&br. tyr26&br. tyr27')
IDSpec['r_tyr'] = cmd.count_atoms(resSelectionSubs('tyr', subs=subs, selection=True))
cmd.delete('tyr1')
cmd.delete('tyr2')
cmd.delete('tyr3')
cmd.delete('tyr4')
cmd.delete('tyr5')
cmd.delete('tyr6')
cmd.delete('tyr7')
cmd.delete('tyr8')
cmd.delete('tyr9')
cmd.delete('tyr10')
cmd.delete('tyr11')
cmd.delete('tyr12')
cmd.delete('tyr13')
cmd.delete('tyr14')
cmd.delete('tyr15')
cmd.delete('tyr16')
cmd.delete('tyr17')
cmd.delete('tyr18')
cmd.delete('tyr19')
cmd.delete('tyr20')
cmd.delete('tyr21')
cmd.delete('tyr22')
cmd.delete('tyr23')
cmd.delete('tyr24')
cmd.delete('tyr25')
cmd.delete('tyr26')
cmd.delete('tyr27')
IDSpec[(('lys','CD'),('shis','CE1'))] = cmd.select('lys1', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.99,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','ND1'))] = cmd.select('lys2', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.90,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','CD'),('shis','NE2'))] = cmd.select('lys3', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+5.95,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','CE1'))] = cmd.select('lys4', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.98,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','ND1'))] = cmd.select('lys5', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.20,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','CE'),('shis','NE2'))] = cmd.select('lys6', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.74,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','CE1'))] = cmd.select('lys7', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.17,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','ND1'))] = cmd.select('lys8', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.62,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('lys','NZ'),('shis','NE2'))] = cmd.select('lys9', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+7.12,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','CE1'))] = cmd.select('lys10', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.51,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','CZ'))] = cmd.select('lys11', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.98,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CD'),('styr','OH'))] = cmd.select('lys12', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+6.30,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CE1'))] = cmd.select('lys13', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+7.60,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','CZ'))] = cmd.select('lys14', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.74,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','CE'),('styr','OH'))] = cmd.select('lys15', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.82,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CE1'))] = cmd.select('lys16', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+6.81,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','CZ'))] = cmd.select('lys17', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.72,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('lys','NZ'),('styr','OH'))] = cmd.select('lys18', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.98,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('lys','CD'),('rasp','CG'))] = cmd.select('lys19', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.69,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CD'),('rasp','OD1'))] = cmd.select('lys20', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.41,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CD'),('rasp','OD2'))] = cmd.select('lys21', '%s w. %s of %s'%(resSelectionSubs('lys','CD',subs),d+7.10,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','CE'),('rasp','CG'))] = cmd.select('lys22', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.30,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','CE'),('rasp','OD1'))] = cmd.select('lys23', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+6.04,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','CE'),('rasp','OD2'))] = cmd.select('lys24', '%s w. %s of %s'%(resSelectionSubs('lys','CE',subs),d+5.73,resSelectionSubs('asp','OD2',subs)))
IDSpec[(('lys','NZ'),('rasp','CG'))] = cmd.select('lys25', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.43,resSelectionSubs('asp','CG',subs)))
IDSpec[(('lys','NZ'),('rasp','OD1'))] = cmd.select('lys26', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+5.58,resSelectionSubs('asp','OD1',subs)))
IDSpec[(('lys','NZ'),('rasp','OD2'))] = cmd.select('lys27', '%s w. %s of %s'%(resSelectionSubs('lys','NZ',subs),d+4.60,resSelectionSubs('asp','OD2',subs)))
IDSpec['lys'] = cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15&br. lys16&br. lys17&br. lys18&br. lys19&br. lys20&br. lys21&br. lys22&br. lys23&br. lys24&br. lys25&br. lys26&br. lys27')
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
IDSpec[(('asp','CG'),('shis','CE1'))] = cmd.select('asp1', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.55,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','ND1'))] = cmd.select('asp2', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+11.03,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','CG'),('shis','NE2'))] = cmd.select('asp3', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+10.46,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','CE1'))] = cmd.select('asp4', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.72,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','ND1'))] = cmd.select('asp5', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+11.05,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD1'),('shis','NE2'))] = cmd.select('asp6', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.57,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','CE1'))] = cmd.select('asp7', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.53,resSelectionSubs('his','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','ND1'))] = cmd.select('asp8', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+10.14,resSelectionSubs('his','ND1',subs,selection=True)))
IDSpec[(('asp','OD2'),('shis','NE2'))] = cmd.select('asp9', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+9.43,resSelectionSubs('his','NE2',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CE1'))] = cmd.select('asp10', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+9.36,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','CZ'))] = cmd.select('asp11', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+8.01,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','CG'),('styr','OH'))] = cmd.select('asp12', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.39,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CE1'))] = cmd.select('asp13', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+10.03,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','CZ'))] = cmd.select('asp14', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.73,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('styr','OH'))] = cmd.select('asp15', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+8.00,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CE1'))] = cmd.select('asp16', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+8.14,resSelectionSubs('tyr','CE1',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','CZ'))] = cmd.select('asp17', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.77,resSelectionSubs('tyr','CZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('styr','OH'))] = cmd.select('asp18', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+6.15,resSelectionSubs('tyr','OH',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CD'))] = cmd.select('asp19', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+7.69,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','CE'))] = cmd.select('asp20', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+6.30,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','CG'),('slys','NZ'))] = cmd.select('asp21', '%s w. %s of %s'%(resSelectionSubs('asp','CG',subs),d+5.43,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CD'))] = cmd.select('asp22', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+7.41,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','CE'))] = cmd.select('asp23', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+6.04,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD1'),('slys','NZ'))] = cmd.select('asp24', '%s w. %s of %s'%(resSelectionSubs('asp','OD1',subs),d+5.58,resSelectionSubs('lys','NZ',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CD'))] = cmd.select('asp25', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+7.10,resSelectionSubs('lys','CD',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','CE'))] = cmd.select('asp26', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+5.73,resSelectionSubs('lys','CE',subs,selection=True)))
IDSpec[(('asp','OD2'),('slys','NZ'))] = cmd.select('asp27', '%s w. %s of %s'%(resSelectionSubs('asp','OD2',subs),d+4.60,resSelectionSubs('lys','NZ',subs,selection=True)))
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
IDSpec['S_2bgs_1_1_1_21'] = cmd.select('S_2bgs_1_1_1_21', 'his|tyr|lys|asp')
cmd.delete('his')
cmd.delete('tyr')
cmd.delete('lys')
cmd.delete('asp')
