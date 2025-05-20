import pickle
import streamlit as st
model=pickle.load(open('C:/Users/srava/Downloads/project_version_share/onehot_encoder_output.pkl','rb'))

def main():
    st.title('pose estimation')
    
    
    #input varibales
    Height=st.text_input('Height')
    weight=st.text_input('weight')
    age=st.text_input('age')
    
    #prediction code
    if st.button('predict'):
          makeprediction=model.predict([[Height,weight,age]])
          output=round(makeprediction[0],2)
          st.success('You are good with your pose {}'.format(output))
    if  __name__=='__main__':
        main()  
    
    
    
    

                  
                  
                  