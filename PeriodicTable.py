from mendeleev import element
while True:
    try:
        el = element(input("Input element symbol or name ").capitalize())
        
        print("")
        print(f"Atomic Number: {el.atomic_number}")
        print(f"Element Symbol: {el.symbol}")
        print(f"Element Name: {el.name}")
        print(f"Name Origin: {el.name_origin}")
        print(f"Atomic Mass: {el.atomic_weight}")
        print(f"Oxidation Number(s): {el.oxistates}")
        print(f"Electron Config: {el.ec}")
        print(f"EC, Noble gas annotation: {el.econf}")
        print(f"Group/Column: {el.group_id}")
        print(f"Period/Row: {el.period}")
        print(f"Sources: {el.sources}")
        print(f"Uses: {el.uses}")
        print("\n############## Isotope List ##############")
        print("{0:^6s} {1:8s} {2:8s} {3:7s} {4:7s}\n{5}".format("MN", "Mass", "Unc.", "Abu.", "Rad.", "-" * 42))
        for iso in el.isotopes:
            print('{0:4d} {1:10.5f} {2:8.2e} {3:} {4:}'.format(iso.mass_number, iso.mass, iso.mass_uncertainty, str(iso.abundance).ljust(7, " "), iso.is_radioactive))
        print("")
    except:
        print("Error, Invalid element of typo")
