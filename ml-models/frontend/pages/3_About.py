import streamlit as st

def main():
 
    st.title("About Us")
 
    
    
    st.header("Our Guide")
    st.markdown(
        """
        <style>
        body {
     background-color:#e5e5e5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
      
<h4><strong>Dr. P Varaprasada Rao</strong></h4> He is a Professor of Computer Science and Engineering, He Joined in this institute since November 2006, completed his Ph.D from Jawaharlal Nehru Technological University Kakinada (JNTUK) year of 2017 under the Supervision of Dr A Govardhan, Rector at JNTUH. His Ph.D work on “Evaluating The Dependencies Of Various Bibliometric Indices On Citation Parameters Of Journals Using Linear Regression And Partition Based K-Centroid Clustering Algorithm”. He is around 14 years of Teaching and Research Experience. He completed M.Tech from A.U College Of engineering at Andhra University, Visakhapatnam year of 2006.He Completed B.E.(CSE) from BDU University year of 2002. Dr. P Varaprasada Rao Research interesting areas are Data Mining, Computer Networking and Security and its application areas. He had published around 30 papers in various International Journals and Conferences and also he has filed 2 Patents from Intellectual Property of India. He Guided 12 M.Tech Projects and 24 B.Tech Projects. Dr P Varaprasada Rao is Coordinator for GRIET-CSI Student Branch, during that period and he was conducted various Technical Fests and Activities under CSI Student Branch.
        """,unsafe_allow_html=True
    )
    
   
    
    st.subheader("Team")
    st.markdown(
        """
        - Singotam Harsha Teja(20241A05S8)
        - Yeluru Srinivas(20241A05T9)
        - Yerra Tejeshwar Goud(20241A05U0)
        - Vemuri Manoj Sai(20241A05T6)
        """
    )

   
if __name__ == "__main__":
    main()