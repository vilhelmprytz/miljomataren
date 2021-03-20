from geopy.distance import geodesic
from orm import Car


def car_statistics(car: Car, positions: list):
    """
    Calculate car statistics (cost, emissions, distance travelled) using provided data and mathematical models.

    Args:
        car (Car): The car used to calculate costs for.
        positions (list): List of Positions

    Returns:
        Dictionary with key statistical information.
    """

    # calculate total distance
    distance_travelled = 0
    for i in range(1, len(positions)):
        previous_pos = (positions[i - 1].lat, positions[i - 1].lon)
        current_pos = (positions[i].lat, positions[i].lon)

        distance_travelled = distance_travelled + geodesic(previous_pos, current_pos).m

    # convert from l/100km to l per meter
    fuel_consumption = car.fuel_consumption / (
        100 * 1000
    )  # divide by 100 to get per km and 1000 to get per m
    used_fuel = fuel_consumption * distance_travelled

    # current speed
    if len(positions) > 1:  # we need to have at least 2 pos to calc speed
        curr_pos = positions[-1]  # last element in list
        prev_pos = positions[-2]  # second to last element in list

        delta_distance = geodesic(
            (prev_pos.lat, prev_pos.lon), (curr_pos.lat, curr_pos.lon)
        ).km  # calculate distance between these to in km
        delta_time = (
            curr_pos.time_created - prev_pos.time_created
        ).seconds / 3600  # calculate time difference in hours between these
        speed = delta_distance / delta_time  # km/h
    else:
        # if there are 0 or 1 positions in the list, no speed yet
        speed = 0

    # co2_emissions
    co2_emissions = (distance_travelled / 1000) * car.co2_emissions

    return {
        "distance_travelled": distance_travelled,
        "used_fuel": used_fuel,
        "speed": speed,
        "co2_emissions": co2_emissions,
    }
