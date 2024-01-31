import subete_ga_F_ni_naru as F

f = F.Sequential(
    F.filter(lambda x: x % 2 == 1),
    F.map(lambda x: x*2),
)

print([*f(range(7))])
