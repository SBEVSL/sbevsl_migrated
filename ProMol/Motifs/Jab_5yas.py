'''
FUNC:Jab_5yas
PDB:5yas
EC:4.1.2.39
PFAM:PF12697,PF12695,PF00561
RESI:thr,ser,asp,his
LOCI:a-11,80,207,235;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. ser'
jesstemp2 ='r. thr'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  cb '
jesstemp4 ='jessatom0 x. %s'%(1.545300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.545300+(d*0.300000)))
jesstemp6 ='r. asp'
jesstemp7 ='r. glu'
jesstemp8 ='jessatom0 x. %s'%(10.786800+(d*0.300000))
jesstemp9 ='jessatom1 x. %s'%(10.473700+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp0+')&('+jesstemp6+'))|(('+jesstemp0+')&('+jesstemp7+')))&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(10.786800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.473700+(d*0.300000)))
jesstemp10 ='jessatom0 x. %s'%(9.635400+(d*0.300000))
jesstemp11 ='jessatom1 x. %s'%(9.473800+(d*0.300000))
jesstemp12 ='jessatom2 x. %s'%(1.515000+(d*0.300000))
jesstemp13 ='br. jessatom2'
cmd.select('jessatom3', '(((('+jesstemp3+')&('+jesstemp6+'))|(('+jesstemp3+')&('+jesstemp7+')))&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(9.473800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.515000+(d*0.300000)))
jesstemp14 ='r. his'
jesstemp15 ='jessatom0 x. %s'%(8.221400+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(7.564900+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(4.625800+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(4.545000+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(8.221400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(7.564900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.625800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(4.545000+(d*0.300000)))
jesstemp19 ='jessatom0 x. %s'%(7.807300+(d*0.300000))
jesstemp20 ='jessatom1 x. %s'%(6.969000+(d*0.300000))
jesstemp21 ='jessatom2 x. %s'%(4.888400+(d*0.300000))
jesstemp22 ='jessatom3 x. %s'%(4.817700+(d*0.300000))
jesstemp23 ='jessatom4 x. %s'%(1.535200+(d*0.300000))
jesstemp24 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp3+')&('+jesstemp14+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.807300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(6.969000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(4.888400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(4.817700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.535200+(d*0.300000)))
cmd.select('Jab_5yas', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
