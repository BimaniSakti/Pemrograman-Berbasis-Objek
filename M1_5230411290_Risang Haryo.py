# luas bangun ruang 2d (Segitiga)
luasSegitiga = lambda a, t : 1/2 * a * t

# Volume bangun ruang 3d (Limas Segitiga)
volumeLimas = lambda a, t, T : 1/3 * luasSegitiga(a, t) * T

print(luasSegitiga(2, 4))
print(volumeLimas(2, 4, 9))