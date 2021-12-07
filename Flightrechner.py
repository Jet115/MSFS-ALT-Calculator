print("Aktuelle Flughöhe in ft:")
aktuelle_alt = input()
print("Ziel Flughöhe in ft:")
anflug_alt = input()
print("Aktuelle Speed over Ground:")
aktuelle_sog = input()

aktuelle_alt = int(aktuelle_alt)
anflug_alt =int(anflug_alt)
aktuelle_sog =int(aktuelle_sog)

aktuelle_alt_10 = 100 * aktuelle_alt
anflug_alt_10 = 100 * anflug_alt
differenz = aktuelle_alt_10 - anflug_alt_10
print("---------------------------------")
print("Differenz beträgt", differenz,"ft")

entfernung = differenz / 1000
entfernung_nm = entfernung * 3
print("Entfernung:", entfernung_nm,"nm")

ft_down = aktuelle_sog * 5
print(ft_down,"ft/min")

print("press Enter to Close...", input())