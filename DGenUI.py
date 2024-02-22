import streamlit as st
from faker import Faker
import csv
from Transpose import transpose as tps


from DataGen import Name as nm
from DataGen import Phone as ph
from DataGen import Email as em

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
            ('Name', 'Phone', 'Email'))

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
            plen = ''
            property1 = plen
            property2 = ''
            property3 = ''
            property4 = ''

        else:
            property1 = ''
            property2 = ''
            property3 = ''
            property4 = ''

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Attribute", type="primary"):
        f = open("input.csv", "a")
        f.write(
            datatype + "," + columnName + "," + property1 + "," + property2 + "," + property3 + "," + property4 + "\n")
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
            name = nm(fake, records, data[i][0])
            output_record.append(name)

        if data[i][0] == "Phone":
            phone = ph(fake, records)
            output_record.append(phone)

        if data[i][0] == "Email":
            email = em(fake, records)
            output_record.append(email)

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

