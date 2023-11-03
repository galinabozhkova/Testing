from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(30.5, 145)

    def test_class_init(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(145, self.vehicle.horse_power)
        self.assertEqual(30.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_func_with_more_km_than_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(30)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_after_drive_fuel_decrease(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.vehicle.drive(10)
        self.assertEqual(18, self.vehicle.fuel)

    def test_refuel_if_change_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(18, self.vehicle.fuel)
        self.vehicle.refuel(5)
        self.assertEqual(23, self.vehicle.fuel)


    def test_refuel_if_raise_exception_when_fuel_ofer_capacity(self):
        self.vehicle.drive(10)
        self.assertEqual(18, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_result_string_func(self):
        self.assertEqual(f"The vehicle has 145 " \
               f"horse power with 30.5 fuel left and 1.25 fuel consumption", self.vehicle.__str__())





if __name__ == "__main__":
    main()

