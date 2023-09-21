#IMPORT REQUIRED LIBRARIES
import streamlit as st
import streamlit.components as stc
import pickle as pkle
import os.path
from PIL import Image


#NAVIGATION BAR
# create a button in the side bar that will move to the next page/radio button choice
next = st.sidebar.button('Next on list')

# will use this list and next button to increment page, MUST BE in the SAME order
# as the list passed to the radio button
new_choice = ['Home','About','Work Experience','Projects', 'Digital Badges & Certificates', 'Resume', 'Contact']

# This is what makes this work, check directory for a pickled file that contains
# the index of the page you want displayed, if it exists, then you pick up where the
#previous run through of your Streamlit Script left off,
# if it's the first go it's just set to 0
if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    # check if you are at the end of the list of pages
    if next_clicked == len(new_choice):
        next_clicked = 0 # go back to the beginning i.e. homepage
else:
    next_clicked = 0 #the start

# this is the second tricky bit, check to see if the person has clicked the
# next button and increment our index tracker (next_clicked)
if next:
    #increment value to get to the next page
    next_clicked = next_clicked +1

    # check if you are at the end of the list of pages again
    if next_clicked == len(new_choice):
        next_clicked = 0 # go back to the beginning i.e. homepage

# create your radio button with the index that we loaded
choice = st.sidebar.radio("Go to:",('Home', 'About', 'Work Experience', 'Projects', 'Digital Badges & Certificates', 'Resume', 'Contact'), index=next_clicked)

# pickle the index associated with the value, to keep track if the radio button has been used
pkle.dump(new_choice.index(choice), open('next.p', 'wb'))


#HOME
if choice == 'Home':

    # image = Image.open('D:\My Portfolio\my_portfolio\photo.png')
    # st.image(image, width = 150)
    # st.markdown("""![Foo](D:/My Portfolio/my_portfolio/img/photo.png)""")
    # st.markdown("<div style='text-align: center;'><img src='/img/photo.png' width='175' height='175'></div>", unsafe_allow_html=True)
    
    st.markdown("""<h1 style='text-align: center; color: darkblue;'>Hi👋, I'm Swati Gulati 😊</h1>""", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>IT Technologist Trainer | Data Science | Self-Taught Programmer | Continuous Learner</h1>", unsafe_allow_html=True)


#ABOUT
elif choice == 'About':
    st.markdown("<h1 style='text-align: center; color: darkblue;'>About Me</h1>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='text-align: center;'>Dedicated and enthusiastic IT trainer with significant experience in cutting-edge technologies and instructional techniques</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("<h2 style='text-align: center; color: #b8f224;'>Education</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: darkblue;'>1. Master of Computer Application (MCA)</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'>Indira Gandhi National Open University (IGNOU)</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>01/2023 - Present<span style='text-align: right; color: darkblue;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dehradun (UK), India</span></div>", unsafe_allow_html=True)
    st.markdown("""
- **Major Elective -** Data Structures and Algorithms, Discrete Mathematics, Software Engineering""")
    
    st.markdown("<h4 style='text-align: left; color: darkblue;'>2. Advanced Diploma (Vocational) in IT, Networking & Cloud Computing (NSQF Level - 6)</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'>National Skill Training Institute (Women), DGT- MSDE, GOI & in collaboration with IBM</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>09/2019 - 03/2022<span style='text-align: right; color: darkblue;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Panipat (Hr), India</span></div>", unsafe_allow_html=True)
    st.markdown('''
- **Web Designing -** HTML 5, CSS 3, DBMS, PHP 7, Python 3.9
- **Web Development -** Bootstrap 5, Cloud Computing (AWS and IBM Cloud)
- **Business Data Analytics -** Power BI, Excel, EDA, Python Libraries for Analytics point and Model Building''')

    st.markdown("<h4 style='text-align: left; color: darkblue;'>3. Business Analytics Masters</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'>iNeuron.ai</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>06/2021 - 11/2021", unsafe_allow_html=True)
    st.markdown("""- Detailed **Business Analytics** course, learned **Python Core, Power BI, Tableau, Advanced Excel and Statistics** to give me the most competitive edge
- **Python -** Python Core; **Libraries:** Pandas, Numpy, Seaborn, etc.
- **Business Statistics -** Data Analysis, Elementary Statistics
- **Descriptive Analytics -** EDA
- **Predictive  Analytics -** Machine Learning & Deep Learning Models
- **Excel -** Formulas, Linear & Growth Trend, Dollar Notation, Lookup, Statistical, Formatting, Pivot Tables, etc.
- **Power BI**
""")
    
    st.markdown("<h4 style='text-align: left; color: darkblue;'>4. Bachelor's Degree</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'>Indira Gandhi National Open University</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>01/2019 - 01/2022", unsafe_allow_html=True)
    
    st.markdown("""- **Major Elective -** Linear Programming; Probability And Statistics""")

    st.markdown("---")

    st.markdown("<h2 style='text-align: center; color: #b8f224;'>Skills</h2>", unsafe_allow_html=True)
    st.markdown("""- **IT Trainer**
- **Industry Knowledge**
    - **Artificial Intelligence(AI)**
    - **Data Analytics**
    - **Deep Learning**
    - **Machine Learning**
    - **Cloud Computing**
    - **Algorithms**
    
- **Tools & Technologies**
    - **Python 3.9**
    - **Power BI**
    - **HTML 5**
    - **CSS 3**
    - **JavaScript**
    - **Django**
    - **Bootstrap 5**
    - **PHP 7**
    - **SQL**
    - **DBeaver**
    - **MongoDB**
    - **Git**
    - **AWS**
    - **IBM Cloud**
    - **MS Excel**
    
- **Interpersonal Skills**
    - **Communication Skills**
    - **Presentation Skills**
    - **Flexibility & Adaptability**
    """)

    st.markdown("---")

    st.markdown("<h2 style='text-align: center; color: #b8f224;'>Achievement</h2>", unsafe_allow_html=True)
    
    st.markdown("<h5 style='color: darkblue;'>1. Secured 9th Position with 84.2% in All India Level Examination conducted by Government of India, MSDE, DGT in the female category for Advanced Diploma in IT, Networking & Cloud Computing</h5>", unsafe_allow_html=True)
    
    st.markdown("<h5 style='color: darkblue;'>2. Got Certified in Data Analyst awarded by IBM & Think-IT</h5>", unsafe_allow_html=True)
    st.markdown("""- I got an opportunity from **Edunet Foundation** for **IBM Skillsbuild Data Camp** that's of **5 months** and offered by **IBM** and **Think-it**
- I learned a lot of things during this camp and got exposure to new things as I worked on 2-mini projects and one team project based on **COVID-19 Data**
- From this camp, I learned many things about **Data Visualization, Data Science, and Machine Learning**
- These projects gave me exposure to industry-level working standards and helped me to learn a lot of things while doing my project
- **LinkenIn Post:** https://www.linkedin.com/feed/update/urn:li:activity:6798913910591295488/""")
   

# WORK EXPERIENCE
elif choice == 'Work Experience':
    st.markdown("<h1 style='text-align: center; color: darkblue;'>Work Experience</h1>", unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Subject Matter Expert</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: darkblue;'>Edunet Foundation</h4>", unsafe_allow_html=True)  
    st.markdown("<div style='color: darkblue;'>09/2022 - Present<span style='text-align: right; color: darkblue;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dehradun (UK), India</span></div>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: gray;'>Certified by the Great Place To Work®, an organization that works with Top Global Corporations & Indian Government</h6>", unsafe_allow_html=True)
    st.markdown("<div style='color: darkblue;'>Roles, Responsibilities & Achievements</div>", unsafe_allow_html=True)
    st.markdown("""
- Conveyed through pre-defined course materials & content via **webinars, virtual classrooms**, and **in-person** lectures in technical skill development programs.
- End-to-end creation of the highest quality based on the most recent technologies.
- Confronting technological problems, project development, and implementation.
- **IBM SkillsBuild Projects:** https://skillsbuild.edunetworld.com/internship-program/
""")

    st.markdown("***")
    
    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Artificial Intelligence Intern</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: darkblue;'>IBM</h4>", unsafe_allow_html=True)
    st.markdown("<div style='color: darkblue;'>09/2021 - 02/2022</div>", unsafe_allow_html=True)
    st.markdown("<div style='color: darkblue;'>Roles, Responsibilities & Achievements</div>", unsafe_allow_html=True)
    st.markdown("""- Understand what is AI, classification of AI, Applications of AI and latest market trends
    - Build **Design Thinking AI Project** and its **Architecture**
    - Perform **Exploratory Data Analysis (EDA)** with tools like Python and relevant packages
    - Build **Machine Learning Models** to develop new era AI applications
    - Understand what is **Deep Learning**, how to build and train Deep Learning models
    - **Statistical tools to interpret data sets**, paying particular attention to trends and patterns that could be valuable for diagnostic and predictive analytics efforts
    - **Prepare reports** for effectively communicating trends, patterns, and predictions using relevant data

- Check out my **GitHub repo**: https://github.com/iamswati/AI-Based-Brain-Tumor-Detection
- **Project Flow Chart:** https://drive.google.com/file/d/18S6yXmKtkfr5v3C8LKWl8W3N6rHzYXkW/view
- **LinkedIn Post:** https://www.linkedin.com/feed/update/urn:li:activity:6947782401255186432/""")

    st.markdown("***")

    st.write("""<h3 style='text-align: left; color: #b8f224;'>Data Science & Business Analytics Intern</h3>""", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: darkblue;'>The Sparks Foundation</h4>", unsafe_allow_html=True)
    st.markdown("<div style='color: darkblue;'>09/2021 - 09/2021</div>", unsafe_allow_html=True)
    st.markdown("<div style='color: darkblue;'>Achievements/Tasks</div>", unsafe_allow_html=True)
    st.markdown("""- Completed many **TASKS** provided by TSF:
    - **TASK 1 -** Predict the optimum number of clusters and represent it visually using Unsupervised ML algorithms
    - **TASK 2 -** Predict the percentage of a student based on the no. of study hours Supervised ML algorithms
    - **TASK 3 -** Create the Decision Tree classifier and visualize it graphically
    - **TASK 4 -** Create a dashboard through Excel and find out weak areas where you can work to make more profit
    
- Check out my **GitHub repo**: https://github.com/iamswati/TheSparksFoundation-Intern
- **Received LoR** from The Sparks Foundation: https://truecertificates.com/verified/GM5RV7YDGB""")


#PROJECTS
elif choice == 'Projects':
    st.markdown("<h1 style='text-align: center; color: darkblue;'>Projects</h1>", unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("<h3 style='text-align: left; color: #b8f224;'>AI Based Brain Tumor Detection</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Feb 2022 - Feb 2022</div>", unsafe_allow_html=True)
    st.markdown("""- This problem statement was given by **IBM Mentor** during my **Internship in Artificial Intelligence at IBM**. The main objective of this project:
    - To understand the Image data
    - To understand the basic concept of the project
    - To detect the right MRI scan images by using ML model
- **Team Size:** 5""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/AI-Based-Brain-Tumor-Detection)[![Foo](https://img.icons8.com/color/35/000000/chrome--v1.png)](https://nostalgic-wright-bf9840.netlify.app/)""")

    st.markdown("---")
    
    st.markdown("<h3 style='text-align: left; color: #b8f224;'>EDA on Loan Payments Data</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Sep 2021 - Oct 2021</div>", unsafe_allow_html=True)
    st.markdown("""- This project will perform initial Analysis and **EDA (Exploratory Data Analysis)** on Loan Payments Data""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/eda-loan)[![Foo](https://img.icons8.com/color/35/000000/chrome--v1.png)](https://iamswati.github.io/eda-loan/)""")

    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>The Sparks Foundation - Intern</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Sep 2021</div>", unsafe_allow_html=True)
    st.markdown("[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/TheSparksFoundation-Intern)")
    
    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Gold Price Prediction</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Aug 2021</div>", unsafe_allow_html=True)
    st.markdown("""- The main goal of this project is to build a **Machine Learning** system that can predict gold prices based on several other stock prices
- Obtain data insights using **Pandas**
- Find the **Correlation** of the other features with GLD (gold) price
- **Predict** the GLD (gold) price by splitting the data & evaluating the model""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/data_analysis_gold_price)[![Foo](https://img.icons8.com/color/35/000000/chrome--v1.png)](https://iamswati.github.io/data_analysis_gold_price/)""")
    
    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Haryana Data Analysis</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Jul 2021 - Aug 2021</div>", unsafe_allow_html=True)
    st.markdown("""- This project is about **Data Analysis on Covid-19 in Haryana state**
- This project starts with **Exploratory Data Analysis (EDA)** for the state of Haryana, India. The data contains various features regarding the COVID-19 outbreak like Date, TotalSamples, etc""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/Haryana_data_analysis)[![Foo](https://img.icons8.com/color/35/000000/chrome--v1.png)](https://iamswati.github.io/Haryana_data_analysis/)""")
    
    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Generate Password</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Jul 2021</div>", unsafe_allow_html=True)
    st.markdown("- This project is about generating passwords using python")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/Generate_Password)""")
    
    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Covid-19 Data Analysis Germany</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Feb 2021 - March 2021</div>", unsafe_allow_html=True)
    st.markdown("""- The main goal of this project is to **Analyze and Predict** the number of new cases for the country Germany in future days
- Obtain data insights using **Pandas**
- Cleaning the data with appropriate techniques
- Performing **Exploratory Data Analysis (EDA)** on the data to get better insights
- **Modeling** the data with the various models with appropriate feature selection techniques""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/covid_19_project)[![Foo](https://img.icons8.com/color/35/000000/chrome--v1.png)](https://iamswati.github.io/covid_19_project/)""")
    
    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Predict The Power Consumption Of Buildings</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>Jan 2021 - Feb 2021</div>", unsafe_allow_html=True)
    st.markdown("""You work for the city of Seattle. To achieve its goal of a carbon-neutral city in 2050, your team is taking a close interest 
    in emissions from non-residential buildings. For this, careful records were made by your agents in **2015 and 2016**. However, these surveys are
     expensive to obtain, and from those already done, you want to try to **predict** the emissions of buildings whose emissions have not yet been 
     measured. Two measures interest you: CO2 emissions and total energy consumption. You also want to evaluate the interest in the emission 
     prediction of the ENERGYSTAR Score(which is complicated to calculate)with the approach currently used by your team""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/Seattle_data_analysis)[![Foo](https://img.icons8.com/color/35/000000/chrome--v1.png)](https://iamswati.github.io/Seattle_data_analysis/)""")

    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Send Email</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>May 2020 - June 2020</div>", unsafe_allow_html=True)
    st.markdown("""- This project is about sending Emails to registered Email IDs using **Smtplib Module**""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/Send_email)""")

    st.markdown("---")

    st.markdown("<h3 style='text-align: left; color: #b8f224;'>Send Text Message</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: darkblue;'>June 2020 - July 2020</div>", unsafe_allow_html=True)
    st.markdown("""- This project is about sending text messages to the registered phone number using **FAST2SMS**""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/35/000000/github.png)](https://github.com/iamswati/Send_text_msg)""")


#DIGITAL BADGES & CERTIFICATES
elif choice == 'Digital Badges & Certificates':
    
    st.markdown("<h1 style='text-align: center; color: darkblue;'>Digital Badges & Certificates</h1>", unsafe_allow_html=True)
    st.markdown("<div><h4 style='text-align: left; colour: darkblue;'>Earned several Digital Badges & Certificates from HackerRank, IBM SkillsBuild, Udemy, etc.</h4></div>", unsafe_allow_html=True)

    st.markdown("""---""")

    st.markdown("""[![Career Explorer](https://images.credly.com/size/200x200/images/6235075a-ee6b-4f23-ad48-f06c20993fb2/Career_Explorer.png)](https://www.credly.com/earner/earned/badge/4b3a72ba-e060-4be5-9071-ee2471cd3db7)                                                                                                                         [![Machine Learning with Python](https://images.credly.com/size/200x200/images/5ae9bf9e-da6e-4cec-82eb-d2b4cfea9751/Machine_Learning_with_Python.png)](https://www.credly.com/earner/earned/badge/3a197375-1a1b-48ff-9c2a-848931b76a9c)                                                                                                                         [![Machine Learning, Deep Learning & Bayesian Learning](https://img-c.udemycdn.com/course/240x135/3780696_8049_7.jpg)](https://www.udemy.com/certificate/UC-250fea4f-970f-4f8e-8e8d-1770c8f109f0/)   """)

    st.markdown("***")

    st.markdown("""[![Data Visualization with Python](https://images.credly.com/size/200x200/images/76326afb-199d-4250-a74f-01bc86dda118/Cognitive_Class_-_Data_Visual_w_Python.png)](https://www.credly.com/earner/earned/badge/c46beb52-44d4-4b1d-9062-b25c97406fda)                                                                                                                                                             [![Statistics 101](https://images.credly.com/size/200x200/images/49211314-919e-4207-885a-7d2ff76ddb07/Statistics_101_-_CC.png)](https://www.credly.com/earner/earned/badge/8c47a5d2-48a6-4ddb-b5b7-044a52909c24)                                                                                                                                                                                                                                                                                                       [![Working in a Digital World: Professional Skills](https://images.credly.com/size/200x200/images/4f76c627-c180-49ae-a5a0-742885eef581/Working_in_a_Digital_World-_Professional_Skills.png)](https://www.credly.com/earner/earned/badge/a56638c4-093e-48dc-a8fa-dc22ab22fb13)""")

    st.markdown("""---""")
    
    st.markdown("""[![Build Your Own Chatbot - Level 1](https://images.credly.com/size/200x200/images/b5243e36-b05f-426b-994a-87a535f1c217/Build_your_own_chatbot_-_CC_v3.png)](https://www.credly.com/earner/earned/badge/b2349367-3ec3-430f-b7cc-8daa93765c8e)                                                                                                                               [![Explorations into Mindfulness](https://images.credly.com/size/200x200/images/6599523a-e811-4775-b037-c4c1417b0b4e/Explorations_into_Mindfulness.png)](https://www.credly.com/earner/earned/badge/858666af-3c5d-4aa2-965b-b8c36eea9dcf)                                                                                                                                                [![Agile Explorer](https://images.credly.com/size/200x200/images/89e728ec-27f8-49ce-a8ea-2df7768f9594/Agile_Explorer.png)](https://www.credly.com/earner/earned/badge/a9477a0d-0395-4da0-bc34-5a155e74f9bd)""")

    st.markdown("""---""")

    st.markdown("""[![iamswati13](https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/8b9fc1fa-bb42-45c6-957b-3b6611c542f1.png?auto=format&ixlib=react-9.0.3)](https://www.hackerrank.com/iamswati13?hr_r=1)                                                                                                                                         [![Job Application Essentials](https://images.credly.com/size/200x200/images/7ae738cc-d7af-45fd-ad53-3e21666cdeca/Job_Application_Essentials.png)](https://www.credly.com/earner/earned/badge/f69dbed9-485a-423a-9f02-77907a7bbec7)                                                                                                                                                                                    [![verify-certificate?id=62iO0c98911j8kvfY1](https://www.guvi.in/images/webps/guvi-logo-full.webp)](https://www.guvi.in/verify-certificate?id=62iO0c98911j8kvfY1)""")

    st.markdown("***")
    
    st.markdown("""[![Data Science Tools](https://images.credly.com/size/200x200/images/de9471ce-018c-4bf4-af49-5c9c1d488613/Data_Science_Tools.png)](https://www.credly.com/earner/earned/badge/ecb7003b-6858-40ac-b2e1-c8cceb2271b8)                             [![Data Science Foundations - Level 1](https://images.credly.com/size/200x200/images/5ca7b236-6105-4154-ba22-c8ae12ec1d8c/Data_Sci_Found_Level_1_-_CC_-_2019.png)](https://www.credly.com/earner/earned/badge/724ca5a7-5a00-412a-ac18-b1730653a3b6)                             [![Python for Data Science](https://images.credly.com/size/200x200/images/84ac9eff-b8a2-4683-846b-f59887a73801/Python_101_Data_Science.png)](https://www.credly.com/earner/earned/badge/3f6b8d3a-13de-4995-84ef-8ebfefc22a0a)                             """)

    st.markdown("***")

    st.markdown("""[![Data Analysis Using Python](https://images.credly.com/size/200x200/images/ba34cb1c-4344-43f5-9685-55e2e901c0f0/Data_Analysis_using_Python.png)](https://www.credly.com/earner/earned/badge/214b047a-f936-4e73-8a5a-c5114f6043b6)                             [![Data Visualization Using Python](https://images.credly.com/size/200x200/images/087eaefb-61a2-426b-ae74-74efca195667/Data_Visualization_Using_Python.png)](https://www.credly.com/earner/earned/badge/52b808f8-0c72-4dc2-b800-67997313aebc)                             [![Machine Learning with Python - Level 1](https://images.credly.com/size/200x200/images/53caf8cc-b5e9-4424-b4a7-7b069fa13db4/Machine_Learning_with_Python.png)](https://www.credly.com/earner/earned/badge/4bf02298-2f24-4d0f-863d-b1cbd5072ddd)                             """)

    st.markdown("***")

    st.markdown("""[![Data Science Methodologies](https://images.credly.com/size/200x200/images/dfd6eb51-4caa-4ffe-b107-85ece064370c/Data_Science_Methodologies.png)](https://www.credly.com/earner/earned/badge/dd218b52-34a9-4e32-a5da-e9a136d35972)                             [![Data Science Foundations - Level 2 (V2)](https://images.credly.com/size/200x200/images/d7321425-c989-4bf9-846a-cd2a647d213b/Data_Sci_Foundations_Level_2_-_CC_-_2019.png)](https://www.credly.com/earner/earned/badge/a265f8a4-bd0c-47a5-ba44-4da15432e6e9)                             """)

    st.markdown("***")


#RESUME
elif choice == 'Resume':
    st.markdown("<h1 style='text-align: center; color: darkblue;'>Resume</h1>", unsafe_allow_html=True)

    st.markdown("<div><h4 style='text-align: left; colour: darkblue;'><a href='https://iamswati.github.io/Resume.pdf', target='_blank'>Click here for my Resume</a></h4></div>", unsafe_allow_html=True)
    

#CONTACT
elif choice == 'Contact':
    
    st.markdown("<h1 style='text-align: center; color: darkblue;'>Contact</h1>", unsafe_allow_html=True)
    
    st.markdown("""[![Foo](https://img.icons8.com/external-kiranshastry-solid-kiranshastry/25/000000/external-email-advertising-kiranshastry-solid-kiranshastry-1.png)](sg131019@gmail.com)[ **sg131019@gmail.com**](sg131019@gmail.com)""")
    st.markdown("""![Foo](https://img.icons8.com/external-those-icons-fill-those-icons/25/000000/external-mobile-phone-mobile-telephone-those-icons-fill-those-icons-4.png) **+919306979702**""")
    st.markdown("""![Foo](https://img.icons8.com/material-rounded/25/000000/marker.png) **Delhi, India**""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/25/000000/linkedin.png)](https://www.linkedin.com/in/iamswatigulati/)[ **iamswatigulati**](https://www.linkedin.com/in/iamswatigulati/)""")
    st.markdown("""![Foo](https://img.icons8.com/ios-glyphs/25/000000/skype.png) **live:.cid.a9e896b0474b62f0**""")
    st.markdown("""[![Foo](https://img.icons8.com/ios-glyphs/25/000000/github.png)](https://github.com/iamswati)[ **iamswati**](https://github.com/iamswati)""")
    st.markdown("""[![Foo](https://img.icons8.com/windows/25/000000/hackerrank.png)](https://www.hackerrank.com/iamswati13)[ **iamswati13**](https://www.hackerrank.com/iamswati13)""")
    
    
