
d = {
    "artist": "Radiohead"
}
try:
    s = d["year"]
except KeyError:
    s = ''

print(d["artist"])