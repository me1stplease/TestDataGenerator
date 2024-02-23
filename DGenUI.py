import datetime

import streamlit as st
from faker import Faker
import csv
from Transpose import transpose as tps

from DataGen import Name as nm
from DataGen import Phone as ph
from DataGen import Email as em
from DataGen import Amount as amt
from DataGen import Text as txt
from DataGen import Address as addrs
from DataGen import Date as dt
from DataGen import Custom as cstm
from DataGen import Categorical as ctg

global datatype
global columnName
global property1
global property2
global property3
global property4

records = 10

# f = open("input.csv", "w")
# f.write("datatype,columnName,property1,property2,property3,property4\n")
# f.close()

with st.container(border=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        datatype = st.selectbox(
            'Data Type: ',
            ('Name', 'Phone', 'Email', 'Amount', 'Text', 'Address', 'Date', 'Custom', 'Categorical'))

    with col2:
        columnName = st.text_input('Attribute Name: ', 'Text')

    with col3:
        if datatype == "Name":
            ntype = st.selectbox(
                'Type: ',
                ('Full Name', 'First', 'Last'))
            property1 = ntype
            property2 = ''
            property3 = ''
            property4 = ''

        if datatype == "Phone":
            pformat = st.text_input('Number Format: ', '+##-##########')
            property1 = pformat
            property2 = ''
            property3 = ''
            property4 = ''

        if datatype == "Email":
            mprovider = st.text_input('Mail Providers: ', '@gmail.com, @yahoo.com, @hotmail.com')
            property1 = mprovider
            property2 = ''
            property3 = ''
            property4 = ''

        if datatype == "Amount":
            minV = st.text_input('Minimum Value: ', '0')
            maxV = st.text_input('Maximum Value: ', '999999')
            property1 = minV
            property2 = maxV
            property3 = ''
            property4 = ''

        if datatype == "Text":
            tlen = st.text_input('Text Length: ', '10')
            property1 = tlen
            property2 = ''
            property3 = ''
            property4 = ''

        if datatype == "Address":
            property1 = ''
            property2 = ''
            property3 = ''
            property4 = ''

        if datatype == "Date":
            startd = st.date_input("Start Date", datetime.date(1914, 7, 7))
            endd = st.date_input("Start Date", datetime.date(2024, 7, 7))
            property1 = startd
            property2 = endd
            property3 = ''
            property4 = ''

        if datatype == "Custom":
            cinput = st.text_input('Custom Value: ', 'ABC')
            property1 = cinput
            property2 = ''
            property3 = ''
            property4 = ''

        if datatype == "Categorical":
            cinput = st.text_input('Category List: ', 'A,B,C')
            property1 = cinput
            property2 = ''
            property3 = ''
            property4 = ''

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Attribute", type="primary"):
        f = open("input.csv", "a")
        f.write(
            str(datatype) + "," + str(columnName) + "," + str(property1) + "," + str(property2) + "," + str(property3) + "," + str(property4) + "\n")
        f.close()
        st.success("Attribute has been added")

with col2:
    if st.button("Clear All", type="secondary"):
        f = open("input.csv", "w")
        f.write("datatype,columnName,property1,property2,property3,property4\n")
        f.close()

st.divider()

if st.button("Generate Data", type="primary"):
    global data
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    output_record = []

    print(len(data))
    fake = Faker(['en_US'])

    for i in range(1, len(data)):
        if data[i][0] == "Name":
            name = nm(fake, records, data[i][2])
            output_record.append(name)

        if data[i][0] == "Phone":
            phone = ph(fake, records, data[i][2])
            output_record.append(phone)

        if data[i][0] == "Email":
            email = em(fake, records, data[i][2])
            output_record.append(email)

        if data[i][0] == "Amount":
            amount = amt(records, float(data[i][2]), float(data[i][3]))
            output_record.append(amount)

        if data[i][0] == "Text":
            text = txt(fake, records, data[i][2])
            output_record.append(text)

        if data[i][0] == "Address":
            address = addrs(fake, records)
            output_record.append(address)

        if data[i][0] == "Date":
            date = dt(fake, records, str(data[i][2]), str(data[i][3]))
            output_record.append(date)

        if data[i][0] == "Custom":
            custom = cstm(records, data[i][2])
            output_record.append(custom)

        if data[i][0] == "Categorical":
            categorical = ctg(fake, records, data[i][2])
            output_record.append(categorical)

    # f = open("input.csv", "w")
    # f.write("datatype,columnName,property1,property2,property3,property4\n")
    # f.close()

    # print("final_op:")
    # print(output_record)
    Tp_output = [['' for x in range(len(output_record))] for y in range(len(output_record[0]))]

    tps(output_record, Tp_output, len(output_record), len(output_record[0]))

    # print("Modified matrix is")
    st.write(str(Tp_output))

    myFile = open('output.csv', 'w')
    writer = csv.writer(myFile)

    for data_list in Tp_output:
        writer.writerow(data_list)
    myFile.close()
