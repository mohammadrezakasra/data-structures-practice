import sys

# خواندن کل ورودی به صورت یکباره (بسیار سریع‌تر)
data = sys.stdin.read().strip().split()
n, k, l = map(int, data[:3])
a = list(map(int, data[3:3+n]))  # اگر n عدد بعدی لیست ماست

print(f"n={n}, k={k}, l={l}")
print(f"لیست a: {a}")