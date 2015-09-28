try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


xmlstream = StringIO.StringIO(
"""<?xml version="1.0"?>
<addressBook>
  <address id="ad01">
    <name>
      <first>Molly</first>
      <mi>S</mi>
      <last>Milligan</last>
    </name>
    <line>103 Joseph St.</line>
    <city>Somerville</city>
    <stateProv>MA</stateProv>
    <postCode>02119</postCode>
    <country>US</country>
  </address>
  <address id="ad02">
    <name>
      <first>Brendan</first>
      <mi>B</mi>
      <last>Slough</last>
    </name>
    <line>4322 Olive St.</line>
    <line>Apt. 415</line>
    <city>Eugene</city>
    <stateProv>OR</stateProv>
    <postCode>97405</postCode>
    <country>US</country>
  </address>
  <address id="ad04">
    <name>
      <first>Masahiro</first>
      <last>Kajiyama</last>
    </name>
    <line>N 34 W 12</line>
    <line>Kita-ku</line>
    <line>Manshon Waraigoto 525</line>
    <city>Sapporo</city>
    <stateProv>Hokkaido</stateProv>
    <postCode>001</postCode>
    <country>JP</country>
  </address>
  <address id="ad05">
    <name>
      <first>Kelly</first>
      <mi>R</mi>
      <last>Waldorf</last>
    </name>
    <line>1422 Pearl St.</line>
    <line>Apt. 1505</line>
    <city>Denver</city>
    <stateProv>CO</stateProv>
    <postCode>80215</postCode>
    <country>US</country>
  </address>
</addressBook>"""
)
