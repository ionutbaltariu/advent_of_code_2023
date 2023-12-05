import re
from typing import List

seed_number_rgx = re.compile(r"seeds:(.+)\n")
seed_to_soil_rgx = re.compile(r"seed-to-soil map:([\d+ \n]+)\n\n")
soil_to_fertilizer_rgx = re.compile(r"soil-to-fertilizer map:([\d+ \n]+)\n\n")
fertilizer_to_water_rgx = re.compile(r"fertilizer-to-water map:([\d+ \n]+)\n\n")
water_to_light_rgx = re.compile(r"water-to-light map:([\d+ \n]+)\n\n")
light_to_temperature_rgx = re.compile(r"light-to-temperature map:([\d+ \n]+)\n\n")
temperature_to_humidity_rgx = re.compile(r"temperature-to-humidity map:([\d+ \n]+)\n\n")
humidity_to_location_rgx = re.compile(r"humidity-to-location map:([\d+ \n]+)")


class NumberTranslator:
    def __init__(self, translations: List[tuple]):
        # sorting the translations allows to find the

        self.translations = translations

    def get(self, val):
        for translation in self.translations:
            dest, src, limit = translation
            if src + limit > val >= src:
                return dest + val - src

        return val


def get_maps(text: str) -> (dict, dict, dict, dict, dict, dict, dict):
    seed_to_soil = get_conversion_dict(text, seed_to_soil_rgx)
    soil_to_fertilizer = get_conversion_dict(text, soil_to_fertilizer_rgx)
    fertilizer_to_water = get_conversion_dict(text, fertilizer_to_water_rgx)
    water_to_light = get_conversion_dict(text, water_to_light_rgx)
    light_to_temperature = get_conversion_dict(text, light_to_temperature_rgx)
    temperature_to_humidity = get_conversion_dict(text, temperature_to_humidity_rgx)
    humidity_to_location = get_conversion_dict(text, humidity_to_location_rgx)

    return seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location


def get_conversion_dict(text, rgx):
    ranges = re.findall(rgx, text)
    ranges = ranges[0].strip().split("\n")

    translations = []
    for _range in ranges:
        dest_start, source_start, limit = [int(x) for x in _range.split()]
        translations.append((dest_start, source_start, limit))

    return NumberTranslator(translations)


def map_from_seed_to_location(seed, maps: List[dict]):
    seed_to_soil = maps[0]
    soil_to_fertilizer = maps[1]
    fertilizer_to_water = maps[2]
    water_to_light = maps[3]
    light_to_temperature = maps[4]
    temperature_to_humidity = maps[5]
    humidity_to_location = maps[6]

    seed_to_soil_val = seed_to_soil.get(seed)
    soil_to_fertilizer_val = soil_to_fertilizer.get(seed_to_soil_val)
    fertilizer_to_water_val = fertilizer_to_water.get(soil_to_fertilizer_val)
    water_to_light_val = water_to_light.get(fertilizer_to_water_val)
    light_to_temperature_val = light_to_temperature.get(water_to_light_val)
    temperature_to_humidity_val = temperature_to_humidity.get(light_to_temperature_val)
    humidity_to_location_val = humidity_to_location.get(temperature_to_humidity_val)

    return humidity_to_location_val


if __name__ == "__main__":
    # file_handler = open("5_example.in", "r")
    file_handler = open("5.in", "r")

    text = file_handler.read()
    file_handler.close()
    seeds = [int(x) for x in re.findall(seed_number_rgx, text)[0].split()]
    locations = []
    maps = [x for x in get_maps(text)]
    for seed in seeds:
        location = map_from_seed_to_location(seed, maps)
        print(f"Seed {seed} was mapped to {location}")
        locations.append(location)

    print(f"Part one solution: {min(locations)}")

    # biggest integer on 64 bits
    locations_min = 18446744073709551615

    import time
    start = time.time()

    # part two
    # brute force takes some minutes using PyPy
    # gotta think of something better
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i + 1]):
            location = map_from_seed_to_location(seeds[i] + j, maps)
            # print(location)
            # print(f"Seed {seeds[i] + j} was mapped to {location}")
            locations_min = min(locations_min, location)

    print(f"It took {time.time() - start} seconds.")
    print(f"Part two solution: {locations_min}")
