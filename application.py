from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Srikar Nekkanti"
PAGE_ICON = ":wave:"
NAME = "Srikar Nekkanti"
DESCRIPTION = """
Passionate Biomedical Engineer currently also pursuing a Master's in Data Science from Worcester Polytechnic Institute (WPI). Proven experience in R&D, algorithm development, and advanced data analysis in the medical tech sector. Adept at leveraging tools like MATLAB, Python, and R-Studio to drive innovations in bioengineering. Actively seeking co-op and internship roles where I can apply my interdisciplinary skillset, collaborate with forward-thinking teams, and further bridge the gap between biology and computation. Let's connect and explore how I can contribute to your mission!
"""
EMAIL = "snekkanti@wpi.edu"
# Define publications at the top of your script
Publications = {
    "🏆 Deep-learning-based skull-induced artifact reduction for transcranial ultrasound imaging: a simulation study": "https://doi.org/10.1117/12.2654685",
    # Add more publications as needed
}

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/srikar-nekkanti-3a288415b/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=330)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        if platform == "LinkedIn":
            # Using an emoji as a simple icon
            cols[index].markdown(f"[🌐 {platform}]({link})")
        else:
            cols[index].write(f"[{platform}]({link})")

# --- EDUCATION SECTION ---
st.write('\n')
st.subheader("Education")
st.write("---")

# Example Education Entry 1
st.write( "**MS in Data Science | Worcester Polytechnic Institute**| 4.0 GPA")
st.write("2023 - Present")
st.write(
    """
 -   ► Specializing in machine learning, data analytics, and advanced statistical methods.
 -   ► Coursework includes Data Mining, Statistical Learning, Big Data Analytics.
    """
)

# Example Education Entry 2
st.write('\n')
st.write( "**BS in Biomedical Engineering | Worcester Polytechnic Institute**| 3.6 GPA ")
st.write("2018 - 2023")
st.write(
    """
  -  ► Graduated with Honors, focusing on bioinstrumentation and medical imaging.
  -  ► Completed a capstone project on developing a novel medical device for kidney stone removal using Ultrasound Imaging.
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.write("---")
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ 2+ Years of experience in data science and biomedical engineering applications
- ✔️ Strong hands on experience in Python, R, MATLAB and SQL for data analysis and model development
- ✔️ Strong foundation in machine learning and statistical analysis
- ✔️ Demonstrated ability to translate complex datasets into actionable insights
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("---")
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy, SciPy), SQL, R, MATLAB, HTML/CSS, Arduino-IDE
- 📊 Data Visulization: PowerBI, MS Excel, Plotly, Tableau
- 📚 Machine Learning: Convolutional neural networks, Deep neural Networks, Supervised & Unsupervised Learning, GAN's 
- 📚 Modeling: Logistic regression, linear regression, decision trees, SVM, K-nearest Neighbor
- 👩 Software: ImageJ, FIJI, SOLIDWORKS, Fusion360, LabVIEW, IBM DOORS
"""
)

# --- PUBLICATIONS SECTION ---
st.write('\n')
st.subheader("Publications")
st.write("---")

for title, link in Publications.items():
    st.markdown(f"- {title}: [Read Here]({link})")


# --- WORK HISTORY ---
st.write("---")
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Research Associate: Engineer | Frontier Ultrasound and Robotic Instrumentation Lab WPI**")
st.write("08/2020 - 05/2023")

Experience1_image = Image.open(current_dir / "assets" / "Experience1.jpg")
st.image(Experience1_image, caption='Frontier Ultrasound and Robotic Instrumentation Lab', width=800)
st.write(
    """
- ► Implemented a U-net-based image regression convolutional neural network to improve image quality in transcranial ultrasound imaging on Python and MATLAB
- ► Used MATLAB to implement a Point-Net-based deep learning algorithm to track tissue deformation and movement for thyroid imaging
- ► Performed hyper-parameter optimization, training, and testing for a variety of deep and machine learning algorithms on Python and MATLAB
- ► Directed data collection,aggregation,and analysis for ultrasound imaging tests and simulations
- ► Implemented a beam-forming algorithm for functional ultrasound using advanced imaging techniques in MATLAB - cut down processing times by 40%
"""
)

# --- JOB 2
st.write('\n')
st.write("---")
st.write("🚧", "**Co-op: Advanced Development (R&D) Engineer | ZOLL Medical Corporation (RESUS Division)**")
st.write("08/2021 - 07/2022")
Experience2_image = Image.open(current_dir / "assets" / "Experience2.png")
st.image(Experience2_image, caption='ZOLL Medical Corporation', width=800)
st.write(
    """
- ► Collaborated with the Advanced Development team on cardiac rhythm, CPR feedback,and novel sensor algorithms using MATLAB and Python
- ► Developed and implemented testing and verification protocols for algorithms and prototype medical devices
- ► Authored MATLAB scripts for enhanced data organization, formatting, calculation,and analysis during product testing, cutting down testing times by 25%
- ► Led premarket application testing for ZOLL AED, X-series, Propaq-MD, and R-series devices for new features and software updates
- ► Collaborated with Quality, Software, and Electrical Engineering teams in a JIRA environment to debug and release 16 software sprints for prototype devices
- ► Led the complete automation and implementation of over 50 manual device testing protocols using purpose-built robots
- ► Contributed to data-driven decision-making for electrode sensor development using advanced analytics and modeling
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.write("---")
st.subheader("Projects & Accomplishments")
st.write("---")

# Project 1
project1_image = Image.open(current_dir / "assets" / "project1_image.jpg")
st.write("🔬", "**GAN-Generated Synthetic Image Detection using Res-Net-derived Model Architecture**")
st.write("11/2023 - Present")
st.image(project1_image, caption='GAN-Generated Synthetic Image Detection', width=800)
st.write(
    """
- ► Defined and trained a GAN for generating synthetic human face images, integrating them into an image classification pipeline.
- ► Utilized architectures including Res-Net 50, VGG-16, VGG-19, and custom models for synthetic image detection, achieving 95 to 98.5% accuracy.
"""
)

# Project 2
st.write('\n')
st.write("---")
project2_image = Image.open(current_dir / "assets" / "project2_image.jpg")
st.write("🔬", "**Improving Edge Detection for Low-Contrast Images using Image Processing Techniques**")
st.image(project2_image, caption='Edge Detection for Low-Contrast Images', width=800)
st.write("01/2024 - Present")
st.write(
    """
- ► Implemented a DNN approach with a VGG-based algorithm for end-to-end edge detection, surpassing conventional filters in performance.
- ► Utilized Holistically Nested Edge Detection techniques to achieve significantly improved outcomes in comparison to conventional filters such as Canny Edge
"""
)

# Project 3
st.write('\n')
st.write("---")
project3_image = Image.open(current_dir / "assets" / "project3_image.png")
st.write("🔬", "**Evaluation of Dense-Net Deep Learning Architecture in Chest X-Ray Image Classification**")
st.image(project3_image, caption='Dense-Net Deep Learning Architecture in Chest X-Ray Image Classification', width=800)
st.write("08/2023 - 01/2024")
st.write(
    """
- ► Applied Dense-Net 201, 121, Ensemble Methods, and custom architectures for multi-label chest X-ray classification across 15 different disease classes, achieving high accuracy and AUROC scores.
- ► Utilized under, over,and stratified sampling for class-imbalanced data
"""
)

# Project 4
st.write('\n')
st.write("---")
project4_image = Image.open(current_dir / "assets" / "project4_image.png")
st.write("🔬", "**R Shiny Data Visualization Application**")
st.image(project4_image, caption='R Shiny Data Visualization Application', width=800)
st.write("08/2023 - 10/2023")
st.write(
    """
- ► Developed an R Shiny app to explore SVMs and K-NN classifiers using the Iris dataset, analyzing decision boundaries based on predictor variables.
"""
)

# Project 5
st.write('\n')
st.write("---")
project5_image = Image.open(current_dir / "assets" / "project5_image.jpg")
st.write("🔬", "**Continuous Ambulatory Peritoneal Dialysis Algorithm & Sensor-based Volume Tracking**")
st.write("01/2023 - 06/2023")
st.image(project5_image, caption='Continuous Ambulatory Peritoneal Dialysis Algorithm', width=800)
st.write(
    """
- ► Worked as part of a team to evaluate the use of supervised learning techniques to evaluate dialysis outcomes along with flow sensor dialysis volume tracking
- ► Implemented Linear, Logistic and Generalised regression techniques to forecast expected dialysis volumes to provide patients with feedback
- ► Devised a"clamp-on" flow sensor solution for existing CAPD dialysis tubing to ensure a low-cost solution to measure incoming and outgoing dialysis volumes
"""
)

# Project 6
st.write('\n')
st.write("---")
project6_image = Image.open(current_dir / "assets" / "project6_image.jpg")
st.write("🔬", "**Ultrasound Guided Needle Insertion Device for Nephrolithotomy**")
st.image(project6_image, caption='Ultrasound Guided Needle Insertion Device', width=800)
st.write("08/2022 - 05/2023")
st.write(
    """
- ► Developed a 3-D printed prototype device to facilitate guided needle insertion for kidney stone removal using ultrasound imaging
- ► Took part in rapid prototyping and CAD design using SOLIDWORKS and various vendors for sourced components
- ► Conducted data analysis on device feasibility, safety, and image quality using data collected from ex-vivo experiments
"""
)
# Project 7: Public Health Dashboard Development

st.write('\n')
st.write("---")
project7_image = Image.open(current_dir / "assets" / "project7_image.png")
st.write("🔬", "**Public Health Dashboard Development for the City of Worcester**")
st.image(project7_image, caption='Public Health Dashboard Development for the City of Worcester', width=800)
st.write(
    """
- ► Partnered with the Coalition for a Greater Healthy Worcester to tackle public health disparities in Massachusetts through the development of an online public health dashboard.
- ► Employed semi-structured interviews, surveys, and online research to define key features of an effective public health dashboard.
- ► Selected and utilized Tableau dashboard development tool that prioritizes ease of use, maintenance, and accurate data representation, resulting in a prototype with guidelines for future updates and feature additions.
"""
)


