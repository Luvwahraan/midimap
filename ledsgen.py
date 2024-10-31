#!/usr/bin/env python3

for col in range(1, 10):
  for row in range(0, 2):
    print( f"CC {col}{row} 0 | 0x90 0x19 0x00")
    print( f"CC {col}{row} 127 | 0x90 0x19 0x7F")
  print('')
