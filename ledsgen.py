#!/usr/bin/env python3

OFF = '0x00'
ON = '0x7F'



buttons = [
  { '11' : '0x1' },
  { '12' : '0x2' },
  { '10' : '0x3' },
  { '21' : '0x4' },
  { '22' : '0x5' },
  { '20' : '0x6' },
  { '31' : '0x7' },
  { '32' : '0x8' },
  { '30' : '0x9' },
  { '41' : '0xa' },
  { '42' : '0xb' },
  { '40' : '0xc' },
  { '51' : '0xd' },
  { '52' : '0xe' },
  { '50' : '0xf' },
  { '61' : '0x10' },
  { '62' : '0x11' },
  { '60' : '0x12' },
  { '71' : '0x13' },
  { '72' : '0x14' },
  { '70' : '0x15' },
  { '81' : '0x16' },
  { '82' : '0x17' },
  { '80' : '0x18' }
]

def genMidi():
  for item in buttons:
    button = list( item.keys() )[0]
    led = item[button]

    print( f"CC {button} 0 | 0x90 {led} {OFF}")
    print( f"CC {button} 127 | 0x90 {led} {ON}\n")
      
#genCC()
genMidi()       
