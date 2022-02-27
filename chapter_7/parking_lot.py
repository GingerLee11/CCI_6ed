# python3
# parking_lot.py - ParkingLot class that takes in a specified max number of parking spots
# with a required number of handicap spots.

from collections import deque
from re import S

import unittest

from random import randint

class ParkingSpot:
    """
    ParkingSpot class is a subclass of ParkingLot. 
    Each spot has a unique id, a specific type and a boolean handicap attribute.
    """
    def __init__(self, type='automobile', handicap=False):
        self.type = type
        self.handicap = handicap
        self.car = None
        self.id = None


class Car:
    """
    Simple Car class to be used in the ParkingLot class.
    """
    def __init__(self, name, type='automobile', handicap=False):
        self.name = name
        self.type = type
        self.handicap = handicap


class ParkingLot:
    """
    ParkingLot class that takes in a specified max number of parking spots
    with a required number of handicap spots.
    """
    all_parking_spots = []
    parking_spots_dict = {}
    handicap_parking_spots_dict = {}
    queue_to_enter = deque()

    def __init__(self, max_capacity, required_number_handicap_spots):
        self.max_capacity = max_capacity
        self.req_num_handi_spots = required_number_handicap_spots
        self.full_spots = 0
        self.num_handi_spots = 0

    def _add_parking_spot(self, parking_spot):
        """
        Helper method that adds parking spots one by one.
        """
        if len(self.all_parking_spots) <= self.max_capacity:
            self.all_parking_spots.append(parking_spot)
            parking_spot.id = len(self.all_parking_spots)
            


            if parking_spot.handicap == True:
                if parking_spot.type not in self.handicap_parking_spots_dict:
                    self.handicap_parking_spots_dict[parking_spot.type] = [parking_spot]
                else:
                    self.handicap_parking_spots_dict[parking_spot.type].append(parking_spot)
                self.num_handi_spots += 1
            else:
                if parking_spot.type not in self.parking_spots_dict:
                    self.parking_spots_dict[parking_spot.type] = [parking_spot]
                else:
                    self.parking_spots_dict[parking_spot.type].append(parking_spot)
            
        else:
            return print(f"Parking lot is already built to full capacity; there are {self.max_capacity} spots.")

    
    def build_parking_lot(self, parking_spots_list):
        """
        Builds out a parking lot based on specifications from the parking_spots_list.
        """
        if len(parking_spots_list) > self.max_capacity:
            return print(f"Design for parking lot exceeds the maximum capacity of {self.max_capacity}.")

        for parking_spot in parking_spots_list:

            self._add_parking_spot(parking_spot)

        if self.num_handi_spots < self.req_num_handi_spots:
            self.all_parking_spots = []
            self.handicap_parking_spots_dict = {}
            self.parking_spots_dict = {}
            return print(f"""
                        Design not accepted.
                        Required number of handicap spots: {self.req_num_handi_spots}.
                        There are currently {self.num_handi_spots} handicap parking spots.
                        Please add {self.req_num_handi_spots - self.num_handi_spots} more spots to the design and try again.
                        """)

    def _search_for_spot(self, car, parking_dict):
        """
        Search through the parking dictionaries for an empty parking spot.
        Returns the id of the parking spot.
        """
        if car.type in parking_dict:
            for parking_spot in parking_dict[car.type]:
                if parking_spot.car == None:
                    parking_spot.car = car
                    # Adds one more car to the total count
                    self.full_spots += 1
                    return parking_spot.id

            # If all the parking spots are full, 
            # append the car to the queue
            self.queue_to_enter.append(car)
            if len(self.queue_to_enter) > 10:
                return print(f"""
                The parking lot is currently full.
                Please wait in the queue.
                There are {len(self.queue_to_enter) - 1} cars ahead in the queue.
                """)
            
        else:
            return print(f"There are no parking spots for {car.type} vehicles in this parking lot.")


    def enter(self, car):
        """
        A car "enters" the parking lot.
        Checks to see if there are available spots, if not the car is put into a queue.
        """
        if self.full_spots >= self.max_capacity:
            self.queue_to_enter.append(car)    
            return print(f"""
                The parking lot is currently full.
                Please wait in the queue.
                There are {len(self.queue_to_enter) - 1} cars ahead in the queue.
                """)
        else:
            if car.handicap == True:
                parking_spot_id = self._search_for_spot(car, self.handicap_parking_spots_dict)
            else:
                parking_spot_id = self._search_for_spot(car, self.parking_spots_dict)
        
            if parking_spot_id != None:
                return print(f"{car.name} is parked in parking spot {parking_spot_id}.")

    def _search_for_car(self, parking_spot, parking_dict):
        """
        Given a parking spot from all the parking spots list.
        Returns car from parking dict.
        """
        if parking_spot.type in parking_dict:
            for p_spot in parking_dict[parking_spot.type]:
                if p_spot.id == parking_spot.id:
                    parking_spot.car = p_spot.car
                    p_spot.car = None
                    self.full_spots -= 1
                    return parking_spot.car
        else:
            raise Exception(f"Error: {parking_spot.type} not in the system.")


    def _enter_from_queue(self):
        checked = []
        

        while len(self.queue_to_enter) != 0:
            
            # To prevent an infinite loop
            if len(checked) >= (self.max_capacity - self.full_spots) or len(checked) > len(self.queue_to_enter):
                break
            car = self.queue_to_enter.popleft()
            checked.append(car)
            self.enter(car)


    def leave(self, parking_spot_id):
        """
        Given a parking spot id, it will find the parking spot and return the car.
        """
        if self.full_spots == 0:
            return print(f"There are no cars in the parking lot.")

        if parking_spot_id < len(self.all_parking_spots) - 1:
            parking_spot = self.all_parking_spots[parking_spot_id - 1]
            car_leaving = parking_spot.car
            # Removes the relationship from parking_spot, all_parking_spots and dict
            self.all_parking_spots[parking_spot_id - 1].car = None
            self.full_spots -= 1
        else:
            return print(f"{parking_spot_id} is not a valid parking spot id.")
        
        '''
        if parking_spot.handicap == True:
            car_leaving = self._search_for_car(parking_spot, self.handicap_parking_spots_dict)
        else:
            car_leaving = self._search_for_car(parking_spot, self.parking_spots_dict)
        '''
        
        if len(self.queue_to_enter) != 0:
            self._enter_from_queue()
        
        if car_leaving != None:
            return print(f"{car_leaving.name} is leaving the lot. \nParking spot {parking_spot_id} is now open.")

    
def example():

    parking_lot = ParkingLot(100, 4)
    parking_spots = []

    # Create parking spots
    for x in range(100):
        type = 'automobile'
        handicap = False
        if x % 25 == 0:
            handicap = True
        if x % 10 == 0:
            type = 'electric'

        parking_spot = ParkingSpot(type, handicap)
        parking_spots.append(parking_spot)

    parking_lot.build_parking_lot(parking_spots)


    # Create cars



    for x in range(1, 150):
        type = 'automobile'
        handicap = False
        if x % 25 == 0:
            handicap = True
        if x % 10 == 0:
            type = 'electric'

        car = Car(f'Car {x}', type, handicap)
        parking_lot.enter(car)

        if x % 15 == 0:
            if x > 100:
                x = 99
            random_parking_spot = randint(1, x)
            parking_lot.leave(random_parking_spot)

    for x in range(1, 145):
        if x > 100:
            x = 99
        random_parking_spot = randint(1, x)
        parking_lot.leave(random_parking_spot)
        
    parking_lot.enter(car)

if __name__ == "__main__":
    example()