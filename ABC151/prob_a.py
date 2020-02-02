# Next Alphabet

c = input()

# アスキーコード変換
c_ascii = ord(c)
c_ascii = c_ascii + 1

# アスキーコードから文字に変換
ans = chr(c_ascii)

print(ans)
