from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("SilverServiceTaxi", 100, 2)
taxi.drive(18)
print("{}, Total = ${}".format(taxi, taxi.get_fare()))
