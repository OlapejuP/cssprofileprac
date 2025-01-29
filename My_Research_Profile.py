import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")
import streamlit as st


# Collect basic information
name = "Dr. Olapeju Y Ekundayo"
field = "Climate and Environmental Science"
institution = "University of South Africa "
address = "7 Deslin Avenue, Florida Park, Roodepoort"
orcid = "https://orcid.org/0000-0001-7790-8277"
linkedin = "https://www.linkedin.com/in/olapeju-onamuti-ekundayo"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Address:** {address}")
st.write(f"**Orcid:** {orcid}")
st.write(f"**LinkedIn:** {linkedin}")

# Add a section for education
phd = "PhD in Geography and Environmental Science, University of Fort Hare, Alice 5700, South Africa 2025." 
msc = "Masters in Meteorology and Climate Science, Federal University of Technology, Akure, Nigeria 2018."
bsc = "Bachelors Degree in Meteorology, Federal University of Technology, Akure, Nigeria 2012."


# Display education information
st.header("Educational Background")
st.write(f"**Doctoral Degree:** {phd}")
st.write(f"**Masters Degree:** {msc}")
st.write(f"**Bachelors Degree:** {bsc}")


# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a section for publications
st.header("Publications Part B")
uploaded_file = st.file_uploader("Upload a Microsoft Word Document of List of Publications", type="docx")

if uploaded_file:
    publicationsb = pd.read_docx(uploaded_file)
    st.dataframe(publicationsb)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publicationsb[
            publicationsb.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a contact section
st.header("Contact Information")
email = "olapejuekundayo5@gmail.com"
telephone = "0606258205"
st.write(f"You can reach {name} at {email}.")
st.write(f"You can reach {name} at {telephone}.")











