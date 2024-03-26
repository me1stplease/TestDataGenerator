import pandas as pd
# from ctgan import CTGAN
from io import StringIO
import streamlit as st
import sdv
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer
import json
import ast
from sdv.evaluation.single_table import get_column_plot



def SDUI():
    global data
    global records
    trig = False

    TypeOption = st.selectbox(
    'Select the type of feed to be generated: ',
    ('Singular', 'Multiple'))

    st.write('You selected:', TypeOption)

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
        print(type(data))

        if data is not None:
            metadata = SingleTableMetadata()
            metadata.detect_from_dataframe(data)
            st.write(metadata.to_dict())
            st.write(metadata.visualize())

            # Step 1: Create the synthesizer
            synthesizer = GaussianCopulaSynthesizer(metadata)

            if 'object_array' not in st.session_state:
                st.session_state.object_array = []

            # custom_constrants=[]
            json_input = st.text_area("Enter object of constrant:")

            if st.button("Add"):
                try:
                    # Safely evaluate input as Python literal
                    object_data = ast.literal_eval(json_input)

                    st.session_state.object_array.append(object_data)
                    # custom_constrants.append(object_data)
                    # Display object data
                    # st.write("Input object:")
                    # st.write(object_data)
                except (ValueError, SyntaxError) as e:
                    st.error("Invalid format. Please check your input.")

            st.write(st.session_state.object_array)

            if st.button("Add Constrant to the seynthesizer") and len(st.session_state.object_array)>0:
                synthesizer.add_constraints(
                    constraints=st.session_state.object_array
                )

            st.write("Constrants: ")
            st.write(synthesizer.get_constraints())


            if st.button("Click to train with provided data and Generate Synthetic Data"):
                # Step 2: Train the synthesizer
                synthesizer.fit(data)

                # Step 3: Generate synthetic data
                synthetic_data = synthesizer.sample(records)

                st.write(synthetic_data)

            # fig = get_column_plot(
            #     real_data=data,
            #     synthetic_data=synthetic_data,
            #     metadata=metadata,
            #     column_name=''
            # )
                
            # fig.show()
        

        

        # coltype = data.columns.to_series().groupby(data.dtypes).groups
        # obj = []
        # for i, j in coltype.items():
        #     if str(i) == 'object':
        #         obj = list(j)

        # catCol = st.text_input('Categorical Features: ', '')
        # catCol = catCol.replace(" ", "")

        # if catCol == '' and len(obj) <= 0:
        #     if trig:
        #         if st.button("Generate Data", type="primary", key=100008):
        #             # ctgan = CTGAN(verbose=True)
        #             # ctgan.fit(data, epochs=200)

        #             # samples = ctgan.sample(10)
        #             print('samples')

        # elif catCol == '' and len(obj) > 0:
        #     categorical_features = obj
        #     if trig:

        #         if st.button("Generate Data", type="primary", key=100009):
        #             # ctgan = CTGAN(verbose=True)
        #             # ctgan.fit(data, categorical_features, epochs=200)

        #             # samples = ctgan.sample(10)
        #             print('samples')

        # else:
        #     if len(obj) > 0:
        #         for i in obj:
        #             catCol += "," + i

        #     categorical_features = set(catCol.split(','))
        #     categorical_features = list(categorical_features)

        #     if trig:
        #         if st.button("Generate Data", type="primary", key=100009):
        #             # ctgan = CTGAN(verbose=True)
        #             # ctgan.fit(data, categorical_features, epochs=200)
        #             # samples = ctgan.sample(10)
        #             print("samples")

    else:
        e = RuntimeError('Upload a file.')
        st.exception(e)
