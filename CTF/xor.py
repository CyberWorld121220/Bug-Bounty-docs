all_a_encoded = b'\x14\x02\x15\x07\x1a\x0fR\x17R3>\x13R4\x12R>\x18Q\x143>Q5\x11>YVS\x17\x02YXVS\x1c\x14\x02\x15\x07\x1a\x0fR\x17R3>\x13R4\x12R>\x18'

key = [chr(c^ord('a')) for c in all_a_encoded]
for c in all_a_encoded:
   print(c)
print(''.join(key))
