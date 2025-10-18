# 🌿 Plant Genius: Your AI Plant Doctor 🩺

Welcome to **Plant Genius**, a deep learning-powered web application designed to help farmers and gardeners identify plant diseases quickly and accurately from leaf images.

![App Demo GIF](https://github.com/muzammil98k/plant-genius-app/blob/main/assets/background.gif) ---

## ✨ Key Features

-   **High Accuracy:** The core of the app is a Convolutional Neural Network (CNN) trained to achieve **95.53% accuracy** on the test set.
-   **Comprehensive Coverage:** The model can identify **38 different classes** of plant diseases and healthy leaves.
-   **Interactive UI:** Built with Streamlit, the app features a beautiful, dark-themed, and animated user interface for a great user experience.
-   **Live Deployment:** The application is deployed on Streamlit Community Cloud and is publicly accessible.

---

## 🚀 Live Demo

You can try out the live application here:
**[➡️ Launch Plant Genius](https://plant-genius-app-98k.streamlit.app/))** ---

## 🔬 Model Performance

The CNN model was trained on the augmented PlantVillage dataset and evaluated on an unseen test set.

-   **Test Accuracy:** `95.53%`
-   **Test Loss:** `0.1631`

<details>
<summary><b>Click to see all 38 supported classes</b></summary>

1.  Apple - Apple Scab
2.  Apple - Black Rot
3.  Apple - Cedar Apple Rust
4.  Apple - Healthy
5.  Blueberry - Healthy
6.  Cherry - Powdery Mildew
7.  Cherry - Healthy
8.  Corn - Cercospora Leaf Spot / Gray Leaf Spot
9.  Corn - Common Rust
10. Corn - Northern Leaf Blight
11. Corn - Healthy
12. Grape - Black Rot
13. Grape - Esca (Black Measles)
14. Grape - Leaf Blight (Isariopsis Leaf Spot)
15. Grape - Healthy
16. Orange - Haunglongbing (Citrus Greening)
17. Peach - Bacterial Spot
18. Peach - Healthy
19. Pepper, Bell - Bacterial Spot
20. Pepper, Bell - Healthy
21. Potato - Early Blight
22. Potato - Late Blight
23. Potato - Healthy
24. Raspberry - Healthy
25. Soybean - Healthy
26. Squash - Powdery Mildew
27. Strawberry - Leaf Scorch
28. Strawberry - Healthy
29. Tomato - Bacterial Spot
30. Tomato - Early Blight
31. Tomato - Late Blight
32. Tomato - Leaf Mold
33. Tomato - Septoria Leaf Spot
34. Tomato - Spider Mites (Two-spotted spider mite)
35. Tomato - Target Spot
36. Tomato - Yellow Leaf Curl Virus
37. Tomato - Mosaic Virus
38. Tomato - Healthy

</details>

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

---

## ⚙️ Setup and Run Locally

To run this project on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/muzammil98k/plant-genius-app.git](https://github.com/muzammil98k/plant-genius-app.git)
    cd plant-genius-app
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure
