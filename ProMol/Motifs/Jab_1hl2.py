'''
FUNC:Jab_1hl2
PDB:1hl2
EC:4.1.3.3
PFAM:PF00701
RESI:ser,thr,lys
LOCI:a-47,48,165;
'''
jesstemp0 ='n.  ca '
jesstemp1 ='r. tyr'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  cb '
jesstemp3 ='r. tyr'
jesstemp4 ='jessatom0 x. %s'%(1.555400+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(('+jesstemp2+')&('+jesstemp3+')&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.555400+(d*0.300000)))
jesstemp6 ='r. arg'
jesstemp7 ='jessatom0 x. %s'%(11.261500+(d*0.300000))
jesstemp8 ='jessatom1 x. %s'%(10.978700+(d*0.300000))
cmd.select('jessatom2', '(('+jesstemp0+')&('+jesstemp6+')&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(11.261500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(10.978700+(d*0.300000)))
jesstemp9 ='jessatom0 x. %s'%(10.483800+(d*0.300000))
jesstemp10 ='jessatom1 x. %s'%(10.039400+(d*0.300000))
jesstemp11 ='jessatom2 x. %s'%(1.545300+(d*0.300000))
jesstemp12 ='br. jessatom2'
cmd.select('jessatom3', '(('+jesstemp2+')&('+jesstemp6+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(10.483800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(10.039400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(1.545300+(d*0.300000)))
jesstemp13 ='r. lys'
jesstemp14 ='jessatom0 x. %s'%(4.787400+(d*0.300000))
jesstemp15 ='jessatom1 x. %s'%(5.494400+(d*0.300000))
jesstemp16 ='jessatom2 x. %s'%(13.705700+(d*0.300000))
jesstemp17 ='jessatom3 x. %s'%(12.837100+(d*0.300000))
cmd.select('jessatom4', '(('+jesstemp0+')&('+jesstemp13+')&('+jesstemp14+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.787400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.494400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(13.705700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(12.837100+(d*0.300000)))
jesstemp18 ='jessatom0 x. %s'%(4.181400+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(4.474300+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(13.069400+(d*0.300000))
jesstemp21 ='jessatom3 x. %s'%(12.089700+(d*0.300000))
jesstemp22 ='jessatom4 x. %s'%(1.545300+(d*0.300000))
jesstemp23 ='br. jessatom4'
cmd.select('jessatom5', '(('+jesstemp2+')&('+jesstemp13+')&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.181400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(4.474300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(13.069400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(12.089700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.545300+(d*0.300000)))
cmd.select('Jab_1hl2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
