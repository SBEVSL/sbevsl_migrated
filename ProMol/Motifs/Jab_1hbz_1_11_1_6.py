'''
FUNC:Jab_1hbz_1_11_1_6
PDB:1hbz
EC:1.11.1.6
RESI:his,ser,asn
LOCI:a-61,99,133;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. his'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. his'
jesstemp4 ='jessatom0 x. %s'%(1.541540+(d*0.050000))
jesstemp4 = '('+jesstemp4+') and not (jessatom0 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom1 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
jesstemp6 ='r. ser'
jesstemp7 ='r. thr'
jesstemp8 ='jessatom0 x. %s'%(5.635630+(d*0.050000))
jesstemp8 = '('+jesstemp8+') and not (jessatom0 x. %s)'%(max(0.05,5.624376-(d*0.050000)))
jesstemp9 ='jessatom1 x. %s'%(5.405400+(d*0.050000))
jesstemp9 = '('+jesstemp9+') and not (jessatom1 x. %s)'%(max(0.05,5.394605-(d*0.050000)))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(5.635630+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom2 x. %s)'%(max(0.05,5.624376-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(5.405400+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom2 x. %s)'%(max(0.05,5.394605-(d*0.050000))))
jesstemp10 ='jessatom0 x. %s'%(4.374370+(d*0.050000))
jesstemp10 = '('+jesstemp10+') and not (jessatom0 x. %s)'%(max(0.05,4.365634-(d*0.050000)))
jesstemp11 ='jessatom1 x. %s'%(3.993990+(d*0.050000))
jesstemp11 = '('+jesstemp11+') and not (jessatom1 x. %s)'%(max(0.05,3.986014-(d*0.050000)))
jesstemp12 ='jessatom2 x. %s'%(1.531530+(d*0.050000))
jesstemp12 = '('+jesstemp12+') and not (jessatom2 x. %s)'%(max(0.05,1.528472-(d*0.050000)))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp2+')&('+jesstemp6+'))|(('+jesstemp2+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.374370+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom3 x. %s)'%(max(0.05,4.365634-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.993990+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom3 x. %s)'%(max(0.05,3.986014-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.531530+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom3 x. %s)'%(max(0.05,1.528472-(d*0.050000))))
jesstemp14 ='r. asn'
jesstemp15 ='r. gln'
jesstemp16 ='jessatom0 x. %s'%(10.620610+(d*0.050000))
jesstemp16 = '('+jesstemp16+') and not (jessatom0 x. %s)'%(max(0.05,10.599401-(d*0.050000)))
jesstemp17 ='jessatom1 x. %s'%(9.529520+(d*0.050000))
jesstemp17 = '('+jesstemp17+') and not (jessatom1 x. %s)'%(max(0.05,9.510490-(d*0.050000)))
jesstemp18 ='jessatom2 x. %s'%(8.998990+(d*0.050000))
jesstemp18 = '('+jesstemp18+') and not (jessatom2 x. %s)'%(max(0.05,8.981019-(d*0.050000)))
jesstemp19 ='jessatom3 x. %s'%(9.029020+(d*0.050000))
jesstemp19 = '('+jesstemp19+') and not (jessatom3 x. %s)'%(max(0.05,9.010989-(d*0.050000)))
cmd.select('jessatom4', '(((('+jesstemp0+')&('+jesstemp14+'))|(('+jesstemp0+')&('+jesstemp15+')))&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(10.620610+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom4 x. %s)'%(max(0.05,10.599401-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(9.529520+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom4 x. %s)'%(max(0.05,9.510490-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(8.998990+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom4 x. %s)'%(max(0.05,8.981019-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(9.029020+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom4 x. %s)'%(max(0.05,9.010989-(d*0.050000))))
jesstemp20 ='jessatom0 x. %s'%(10.430420+(d*0.050000))
jesstemp20 = '('+jesstemp20+') and not (jessatom0 x. %s)'%(max(0.05,10.409590-(d*0.050000)))
jesstemp21 ='jessatom1 x. %s'%(9.439430+(d*0.050000))
jesstemp21 = '('+jesstemp21+') and not (jessatom1 x. %s)'%(max(0.05,9.420579-(d*0.050000)))
jesstemp22 ='jessatom2 x. %s'%(9.449440+(d*0.050000))
jesstemp22 = '('+jesstemp22+') and not (jessatom2 x. %s)'%(max(0.05,9.430569-(d*0.050000)))
jesstemp23 ='jessatom3 x. %s'%(9.399390+(d*0.050000))
jesstemp23 = '('+jesstemp23+') and not (jessatom3 x. %s)'%(max(0.05,9.380619-(d*0.050000)))
jesstemp24 ='jessatom4 x. %s'%(1.541540+(d*0.050000))
jesstemp24 = '('+jesstemp24+') and not (jessatom4 x. %s)'%(max(0.05,1.538462-(d*0.050000)))
jesstemp25 ='br. jessatom4'
cmd.select('jessatom5', '(((('+jesstemp2+')&('+jesstemp14+'))|(('+jesstemp2+')&('+jesstemp15+')))&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(10.430420+(d*0.050000)))
cmd.select('jessatom0', 'jessatom0 & not (jessatom5 x. %s)'%(max(0.05,10.409590-(d*0.050000))))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(9.439430+(d*0.050000)))
cmd.select('jessatom1', 'jessatom1 & not (jessatom5 x. %s)'%(max(0.05,9.420579-(d*0.050000))))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(9.449440+(d*0.050000)))
cmd.select('jessatom2', 'jessatom2 & not (jessatom5 x. %s)'%(max(0.05,9.430569-(d*0.050000))))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(9.399390+(d*0.050000)))
cmd.select('jessatom3', 'jessatom3 & not (jessatom5 x. %s)'%(max(0.05,9.380619-(d*0.050000))))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.541540+(d*0.050000)))
cmd.select('jessatom4', 'jessatom4 & not (jessatom5 x. %s)'%(max(0.05,1.538462-(d*0.050000))))
cmd.select('Jab_1hbz_1_11_1_6', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
