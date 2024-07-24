import unittest
from src.models.car import Car
from src.models.motorcycle import Motorcycle
from src.models.truck import Truck
from src.services.rental_service import RentalService

class TestRentalService(unittest.TestCase):

    def setUp(self):
        self.rental_service = RentalService()
        self.car = Car("Toyota", "Corolla", 2020, 50, 4)
        self.motorcycle = Motorcycle("Honda", "CB500", 2019, 30)
        self.truck = Truck("Volvo", "FH", 2018, 100)
        self.rental_service.add_vehicle(self.car)
        self.rental_service.add_vehicle(self.motorcycle)
        self.rental_service.add_vehicle(self.truck)

    def test_list_available_vehicles(self):
        available_vehicles = self.rental_service.list_available_vehicles()
        self.assertEqual(len(available_vehicles), 3)

    def test_rent_vehicle(self):
        self.assertTrue(self.rental_service.rent_vehicle(self.car))
        self.assertFalse(self.car.is_available)
        self.assertEqual(len(self.rental_service.list_available_vehicles()), 2)

    def test_return_vehicle(self):
        self.rental_service.rent_vehicle(self.car)
        self.rental_service.return_vehicle(self.car)
        self.assertTrue(self.car.is_available)
        self.assertEqual(len(self.rental_service.list_available_vehicles()), 3)

if __name__ == '__main__':
    unittest.main()
