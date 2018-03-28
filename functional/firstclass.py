# in python every thing is object

# you can use a function as argument or return function

class Order:
    name = ''
    itemnumber = 0
    quantity = 0
    price = 0
    background = False


class Orders:
    orders = []
    orderid = 0
    shipping_address = ''
    expediated = False
    shipped = False
    customer = None

    def get_expid_customers(self, findBy):
        # findBy accepts:
        output = []
        for order in self.orders:
            if order.exped:
                output.append(order.customer[findBy])
        return output


# composotion
def f(x):
    return x + 2


def y(f, x):
    return f(x) * 2


# closure

def addx(x):
    def _(y):
        return x + y

    return _


add2 = addx(2)
add3 = addx(3)


# currying

def ff(x, y):
    return x * y


def f2(x):
    def _(y):
        return ff(x, y)

    return _

print(f2(2))
