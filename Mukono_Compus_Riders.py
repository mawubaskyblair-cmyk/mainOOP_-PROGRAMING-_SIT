# 1. Class definition (1 mark)
class BodaBoda:
    # 2. Company as class variable (1 mark)
    company = "Mukono Campus Rides"

    # 3. __init__ to initialise attributes (3 marks)
    def __init__(self, reg_no, rider_name, location):
        self.reg_no = reg_no
        self.rider_name = rider_name
        self.location = location
        self.completed_trips = 0   # initially no trips

    # 4. Methods (2 marks)
    def complete_trip(self):
        self.completed_trips += 1

    def change_location(self, new_location):
        self.location = new_location

    def display_info(self):
        print(f"Reg: {self.reg_no}, Rider: {self.rider_name}, "
              f"Location: {self.location}, Trips: {self.completed_trips}, "
              f"Company: {BodaBoda.company}")

# 5. Create two objects (1 mark)
boda1 = BodaBoda("UBH 123K", "John", "Main Gate")
boda2 = BodaBoda("UBH 456L", "Sarah", "Library")

# 6. Demonstrate actions (2 marks)
boda1.complete_trip()   # trip 1
boda1.complete_trip()   # trip 2
boda2.complete_trip()   # trip 1
boda1.change_location("Hostel")

# Display final details
boda1.display_info()
boda2.display_info()