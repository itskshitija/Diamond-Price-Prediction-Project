# 💎 **Diamond Price Prediction** 🏷️

This project is focused on predicting the price of diamonds based on various features like **carat weight**, **cut quality**, **color**, **clarity**, and other attributes. By applying machine learning models, we aim to predict the price of a diamond using its characteristics, providing valuable insights into what influences diamond pricing.

## 🔍 **Project Overview**

The primary goal of this project is to create a machine-learning model capable of predicting diamond prices. The dataset includes various diamond characteristics, and multiple regression models are trained and evaluated to select the best one based on the R² score. The **Decision Tree Regressor** was found to be the best performing model for this task.

## 🛠️ **Technologies Used**

- **Python 3.x**
- Libraries:
  - `numpy` - For numerical operations
  - `pandas` - For data manipulation and analysis
  - `scikit-learn` - For machine learning models and model evaluation
  - `matplotlib` & `seaborn` - For data visualization
  - `joblib` - For model serialization
- Machine Learning Algorithms:
  - **Linear Regression**
  - **Lasso Regression**
  - **Ridge Regression**
  - **ElasticNet Regression**
  - **Decision Tree Regressor** *(Best Performing Model)*
 
## 🔖Dataset
The diamond_data.csv file contains information about diamonds, including the following features:
- Carat
- Cut
- Color
- Clarity
- Price (target variable)

## 2️⃣ **Model Training**

To train the model, simply run the training script, which evaluates multiple regression models and selects the best one based on the R² score. In this case, the **Decision Tree Regressor** was selected as the best model based on performance.

## 3️⃣ **Making Predictions**

Once the model is trained, you can use it to predict the price of a diamond based on new input data.

## 4️⃣ **Model Evaluation**

The project evaluates different regression models using various performance metrics to select the most accurate model. The following evaluation metrics were used:

- **RMSE (Root Mean Squared Error):** Measures the average magnitude of the error in the model's predictions.
- **MAE (Mean Absolute Error):** Provides the average absolute difference between predicted and actual values.
- **R² Score:** Indicates how well the model explains the variance in the target variable.

## 📦 **Installation**

To set up the project on your local machine, follow these steps:

### Step 1: Clone the Repository

```bash
git clone https://github.com/itskshitija/Diamond-Price-Prediction.git
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## ⛳Final Output
![image](https://github.com/user-attachments/assets/281d8539-cd93-49c0-b36b-73a60e7dcf5e)
