# Goal: Apply Open/Closed Principle (OCP) in SOLID
# # ❌ OCP Violation
# class DiscountCalculator:
#     def calculate(self, customer_type, price):
#         if customer_type == "regular":
#             return price * 0.9
#         elif customer_type == "vip":
#             return price * 0.8
#         elif customer_type == "employee":
#             return price * 0.5
        
class RegularCustomer:
    def get_post_discount_rate(self):
        return 0.9

class VIPCustomer:
    def get_post_discount_rate(self):
        return 0.8
    
class EmployeeCustomer:
    def get_post_discount_rate(self):
        return 0.5

class DiscountCalculator:
    def calculate(self, customer_type, price):
        return price * customer_type.get_post_discount_rate()


