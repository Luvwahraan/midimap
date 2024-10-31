#!/usr/bin/env python3

# Quick script to generate CC changes for all rotary values.
# For a 4 channels mixer mutes controls, 127 = mute.

min_val = 0
div_val = 4
max_val = 127
start_cc = 25

values = [0]
CC = []

step = round( max_val / div_val )
for i in range(0, div_val-1):
  c_cc = start_cc + i
  values.append(127)

def search_not_muted():
  return values.index(0) + start_cc

def change_value():
  for i in range(0, div_val):
    if values[i] == 0:
      values[i] = 127
      if i+1 < div_val:
        values[i+1] = 0
        break


for check_val in range(0, max_val):
  mod = check_val % step
  if mod == 0 and check_val != 0:
    change_value()
  
  print( f"\n# {search_not_muted()} not muted" )
  for i in range(0, div_val):
    cc = start_cc + i
    print( f"CC 22 {check_val} | SAME {cc} {values[i]}")
  
