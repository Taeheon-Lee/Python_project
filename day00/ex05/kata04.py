t = (0, 4, 132.42222, 10000, 12345.67)

s = "day_{:0>2}, ex_{:0>2} : {:.2f}, {:.2e}, {:.2e}"
print(s.format(t[0], t[1], t[2], t[3], t[4]))
