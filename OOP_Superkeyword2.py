#Car-Dealership Simulator:


class Customer:
    def __init__(self, name, customer_id, car):
        self.name = name
        self.customer_id = customer_id  # Fixed spelling here
        self.car = car

    def show_details(self):
        print(f"Customer's name: {self.name}")
        print(f"customer_id: {self.customer_id}")
        print(f"Purchased car: {self.car}")

class LuxuryCustomer(Customer):
    def __init__(self, name, customer_id, car, vip_membership):
        super().__init__(name, customer_id, car)
        self.vip_membership = vip_membership

    def show_vip(self):
        print(f"VIP membership: {self.vip_membership}")

c1 = LuxuryCustomer("Vishnu", 101, "Land Rover Defender", "Gold Member")
c2 = LuxuryCustomer("Jimmy", 102, "Mercedes G-Wagon", "Platinum Member")

print("----------customer 1----------")
c1.show_details()
c1.show_vip()

print("----------customer 2----------")
c2.show_details()
c2.show_vip()
