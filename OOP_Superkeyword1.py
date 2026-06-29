class customer:
    def __init__(self,name,customer_id,bill):
        self.name = name
        self.customer_id = customer_id
        self.bill = bill
    def show_bill(self):
        print(f"{self.name}'s Bill is: {self.bill}")
class membercustomer(customer):
    def __init__(name,customer_id,bill,card_number):
        super().__init__(self,name,customer_id,bill)
        self.card_number = card_number
    def show_membership(self):
        print(f"{self.name} had V-mart Membership card: {self.card_number}")
c1 = membercustomer("Vishnu",1784,7210,VM967)
c2 = membercustomer("Leon",8784,8310,VM960)
c3 = membercustomer("Ramon",9784,7230,VM667)
c1.show_bill()
c1.show_membership()
c2.show_bill()
c2.show_membership()
c3.show_bill()
c3.show_membership()
