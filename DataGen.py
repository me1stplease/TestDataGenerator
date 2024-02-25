import numpy as np
from faker import Factory as FakerFactory
from faker.providers import DynamicProvider
from dateutil import parser

fakeFact = FakerFactory.create()


def Name(fake, records, ntype):
    name = []
    for i in range(records):
        if ntype == 'Full Name':
            name.append(fake.name())
        elif ntype == 'First':
            name.append(fake.name().split(" ")[0])
        else:
            name.append(fake.name().split(" ")[1])

    return name


def Phone(fake, records, pformat):
    phone = []
    for i in range(records):
        phone.append(fake.unique.bothify(pformat))
    return phone


def Email(fake, records, domainList='gmail.com, yahoo.com, hotmail.com'):
    domainList = domainList.replace(" ", '')
    custom_domain_provider = DynamicProvider(
        provider_name="custom_domain",
        elements=domainList.split(","),
    )
    fake.add_provider(custom_domain_provider)
    email = []
    for i in range(records):
        nm = fake.name().split(" ")
        email.append(nm[0] + fake.unique.numerify('###') + "@" + fake.custom_domain())
    return email


def Amount(records, minN=0, maxN=9999999):
    amount = np.random.uniform(low=minN, high=maxN, size=(records,))
    # for _ in range(records):
    #     amount.append(np.random.uniform(low=minN, high=maxN, size=(records,)))
    return amount


def Text(fake, records, length=10):
    txt = []
    txtFormat = ''
    print("IN:"+length)
    for _ in length:
        txtFormat += '?'

    for _ in range(records):
        print("IN")
        txt.append(fake.bothify(text=txtFormat, letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    print("OUT")
    return txt


def Address(fake, records):
    address = []
    for _ in range(records):
        address.append(fake.address())
    return address


def Date(fake, records, start='-30y', end='today'):
    # print("type!!11111: "+str(type(parser.parse(start))))
    dateB = []
    for _ in range(records):
        dateB.append(str(fake.date_between(parser.parse(start), parser.parse(end))))
    return dateB


def Custom(records, cval="ABC"):
    custom = []
    for _ in range(records):
        custom.append(cval)
    return custom


def Categorical(fake, records, clist="A,B,C"):
    category_provider = DynamicProvider(
        provider_name="category",
        elements=clist.split(","),
    )
    fake.add_provider(category_provider)
    categorical = []
    for _ in range(records):
        categorical.append(fake.category())
    return categorical
