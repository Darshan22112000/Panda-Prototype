class Map_values:

    agent_mapping = {
        "Wesley": "Wesley",
        "Filips": "Filips",
        "Basty": "Basty",
        "Thabo": "Thabo",
        "Daniel": "Daniel",
        "Georgina": "Georgina",
        "Aditya": "Aditya",
        "Raghavi": "Raghavi",
        "Aaron": "Aaron",
        "Aayush": "Aayush",
        "Kashish": "Kashish",
        "Ajay": "Ajay",
        "Prithwik": "Prithwik",
        "Darshan": "Darshan",
        "Shivani": "Shivani",
        "Luke": "Luke",
        "Sohail": "Sohail",
        "Royston": "Royston",
        "Govind": "Govind",
        "Clyde": "Clyde",
        "Ryan": "Ryan",
        "Paul": "Paul",
        "Percy": "Percy",
        "Manoj": "Manoj",
        "Thulani": "Thulani",
        "Josh K": "Josh K",
        "Muadh": "Muadh",
        "Josh H": "Josh H",
        "Seamus": "Seamus",
        "Feziwe": "Feziwe",
        "Ciara": "Ciara",
        "Cian": "Cian",
        "Michelle": "Michelle",
        "Eamonn": "Eamonn",
        "Eamonn OC": "Eamonn O'Connor",
        "Elton": "Elton",
        "Vinced": "Vinced",
        "Adam": "Adam",
        "Dean": "Dean",
        "Tadhg": "Tadhg",
        "Marc": "Marc",
        "Colm": "Colm",
        "Shane": "Shane",
        "Raj": "Raj",
        "Roshini": "Roshini",
        "Cruz": "Cruz",
        "Kevin": "Kevin",
        "Jacob": "Jacob",
        "TEST": "TEST"
    }

    area_mapping = {
        "6|131": "Tullamore",
        "6|117": "Meath",
        "3|116": "Fingal",
        "16|130": "Wexford",
        "5|126": "Finglas",
        "4|121": "South Dublin",
        "39|135": "McElvaneys"
    }

    plan_mapping = {
        "131": "Tullamore €17/month 65kg (€120/year)",
        "15/mo 1 year upfront 120": "Tullamore €15/month 35kg (€120/Year)",
        "117": "Navan €13/month 50 kg (€120 for the Year)",
        "126": "Dublin City €13 (€99) 42kg",
        "128": "Dublin City €19 (€145) 65kg",
        "121": "South Dublin €13 (€99) 42kg",
        "124": "South Dublin €19 (€145) 65kg",
        "118": "Wexford €15/month",
        "McElvaneys €135 HY": "McElvaneys €135 HY",
        "McElvaneys €150 HY": "McElvaneys €150 HY",
        "McElvaneys €180 HY": "McElvaneys €180 HY",
        "McElvaneys €270 HY": "McElvaneys €270 HY"
    }

    inverse_agent_mapping = {v: k for k, v in agent_mapping.items()}
    inverse_area_mapping = {v: k for k, v in area_mapping.items()}
    inverse_plan_mapping = {v: k for k, v in plan_mapping.items()}

    AGENTS = ["Darshan", "Aayush", "Kashish"]
    AREAS = ["Tullamore", "Meath", "South Dublin"]
    PLANS = ["Tullamore €17/month 65kg (€120/year)", "Navan €13/month 50 kg (€120 for the Year)",
             "South Dublin €13 (€99) 42kg"]
