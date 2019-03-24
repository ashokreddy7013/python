class PaymentMode:
    @classmethod
    def payment_class_Options(cls):
        print("Payment Options")
        if cls.__name__== "Online":
            print("I am Online Process")
            print("Please Login to Your Bank ACC")
        if cls.__name__ == "COD":
            print("I am COD")
            print("Please Provide your Current Ad")

class Online(PaymentMode):
    def payment_Online_Options(self):
        print("Online")

class COD(PaymentMode):
    def payment_COD_Options(self):
        print("Online")

o1 = Online()
o1.payment_class_Options()

c1 = COD()
c1.payment_class_Options()