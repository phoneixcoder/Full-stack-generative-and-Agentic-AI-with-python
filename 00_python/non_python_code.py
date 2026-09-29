def make_chai():
    if not kettle_has_watter():
        fill_water()
    plug_in_kettle()
    boil_water()
    if not if_cup_clean():
        wash_cup()
    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stir("cup")
    serve("cup")

make_chai()