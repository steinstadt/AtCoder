N, M, K = map(int, input().split())
out = 0
mod = 998244353

c = 1

for k in range(K+1):
  out += M * pow(M-1, N-k-1, mod) * c
  out %= mod
  c *= (N-k-1) * pow(k+1, mod-2, mod)
  c %= mod
print(out)
