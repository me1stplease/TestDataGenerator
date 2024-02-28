import pandas as pd
from ctgan import CTGAN
from io import StringIO
import streamlit as st


def SDUI():
    global data
    global records
    trig = False

    try:
        records = int(st.text_input('Number of records to be generated: ', '10', key=100007))
        trig = True

    except:
        e = RuntimeError('Enter a valid number.')
        st.exception(e)

    uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False)
    if uploaded_file is not None:
        # # To read file as bytes:
        # bytes_data = uploaded_file.getvalue()
        # # st.write(bytes_data)
        #
        # # To convert to a string based IO:
        # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # # st.write(stringio)
        #
        # # To read file as string:
        # string_data = stringio.read()
        # # st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        data = pd.read_csv(uploaded_file)
        print(data)

        coltype = data.columns.to_series().groupby(data.dtypes).groups
        obj = []
        for i, j in coltype.items():
            if str(i) == 'object':
                obj = list(j)

        catCol = st.text_input('Categorical Features: ', '')
        catCol = catCol.replace(" ", "")

        if catCol == '' and len(obj) <= 0:
            if trig:
                if st.button("Generate Data", type="primary", key=100008):
                    ctgan = CTGAN(verbose=True)
                    ctgan.fit(data, epochs=200)

                    samples = ctgan.sample(10)
                    print(samples)

        elif catCol == '' and len(obj) > 0:
            categorical_features = obj
            if trig:

                if st.button("Generate Data", type="primary", key=100009):
                    ctgan = CTGAN(verbose=True)
                    ctgan.fit(data, categorical_features, epochs=200)

                    samples = ctgan.sample(10)
                    print(samples)

        else:
            if len(obj) > 0:
                for i in obj:
                    catCol += "," + i

            categorical_features = set(catCol.split(','))
            categorical_features = list(categorical_features)

            if trig:
                if st.button("Generate Data", type="primary", key=100009):
                    ctgan = CTGAN(verbose=True)
                    ctgan.fit(data, categorical_features, epochs=200)
                    samples = ctgan.sample(10)
                    print(samples)

    else:
        e = RuntimeError('Upload a file.')
        st.exception(e)
