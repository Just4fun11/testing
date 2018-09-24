from collections import namedtuple

Subscriber = namedtuple('subscriber', ['addr', 'joined'])
sub = Subscriber('abc@gmail.com', '2012-10-19')
print(sub) #prints subscriber(addr='abc@gmail.com', joined='2012-10-19')
print(sub.addr) #prints abc@gmail.com
print(sub.joined) #prints 2012-10-19

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def main(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
        print(total)
    return total


if __name__ == '__main__':
    main(records=Subscriber)