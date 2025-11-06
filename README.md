<p align="center">
  <img src="https://raw.githubusercontent.com/Faizan-Ashiq/affordable-medicine-recommender/main/images/logo.png" alt="Logo" width="120" height="120">
</p>

<h1 align="center">💊 Affordable Medicine Recommendation System (Pakistan)</h1>
<p align="center">
  <strong>AI-powered solution to reduce medicine costs through data-driven recommendations.</strong><br/>
  <em>Developed by Muhammad Faizan — Data Scientist | AI Researcher </em>
</p>

---

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Data-50K%20Medicines-blue?style=for-the-badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Made%20with-Python🐍-green?style=for-the-badge"></a>
  <a href="#"><img src="https://img.shields.io/badge/Domain-Healthcare%20AI-red?style=for-the-badge"></a>
</p>

---

## 📘 **Table of Contents**

1. [About the Project](#about-the-project)
2. [Motivation](#motivation)
3. [Vision & Impact](#vision--impact)
4. [Project Phases](#project-phases)
5. [Data Extraction Phase](#data-extraction-phase)
6. [Machine Learning Phase](#machine-learning-phase)
7. [Architecture Overview](#architecture-overview)
8. [Example Recommendation Flow](#example-recommendation-flow)
9. [Visual Insights](#visual-insights)
10. [Tech Stack](#tech-stack)
11. [Installation](#installation)
12. [Usage Example](#usage-example)
13. [Future Scope](#future-scope)
14. [Results Preview](#results-preview)
15. [Contribute](#contribute)
16. [Author](#author)
17. [License](#license)
18. [Acknowledgments](#acknowledgments)

---

## 🧠 **About the Project**

> “Data Science meets Healthcare — to make medicine affordable for everyone.”

Every day, millions of patients in Pakistan struggle to afford high-cost medicines prescribed by doctors — often due to **brand sponsorship** influence.  
This project uses **Machine Learning + Web Scraping + Data Science** to solve that problem.

### 🎯 **Goal**
Build a system that:
1. Takes a **high-cost medicine** as input.
2. Recommends **affordable alternatives** with the same salt composition, use, and dosage.

### 💡 **Core Idea**
Replace expensive branded medicines with **clinically equivalent, low-cost alternatives** — using AI-driven matching algorithms.

---

## 💬 **Motivation**

In Pakistan’s healthcare system:
- Many doctors prescribe **branded** medicines under **sponsorship influence**.
- Patients **unaware** of affordable substitutes end up paying 2–5× higher costs.
- Pharmacists and consumers **lack a unified database** of medicine alternatives.

Hence, this AI project bridges that gap — by providing **fair, data-backed recommendations**.

---

## 🌍 **Vision & Impact**

> “To make affordable healthcare accessible to every individual, powered by transparent AI.”

| Impact Area | Description |
|--------------|-------------|
| 💰 Financial | Reduces patient medicine expenses by up to **60%** |
| ⚕️ Healthcare | Promotes **rational prescribing** |
| 🔬 Data Science | Uses ML to map **composition similarity** |
| 🧭 Social | Encourages transparency in healthcare |

---

## 🧩 **Project Phases**

### Phase 1: 🧾 **Data Extraction (Current)**
Extracting and cleaning medicine data from multiple pharmacy websites.

### Phase 2: 🧮 **Data Preprocessing**
Handling missing values, salt standardization, and feature engineering.

### Phase 3: 🤖 **Model Training**
Using similarity-based ML models to recommend cheaper alternatives.

### Phase 4: 💻 **Deployment**
Creating a web dashboard (Streamlit/Flask) for public use.

### Phase 5: 📊 **Visualization & Reporting**
Interactive charts to show savings, salt similarities, and brand comparisons.

---

## 🧾 **Data Extraction Phase**

Currently scraping over **50,000 medicine entries** from multiple sources:

| Source | Description | Status |
|---------|--------------|--------|
| dvago.pk | Primary data source | ✅ Done |
| emeds.pk | Backup source | ✅ Done |
| sehat.com.pk | Additional brands | 🔄 In Progress |
| oladoc.com | Doctor-linked pricing | 🔄 In Progress |

### ⚙️ Extracted Fields

| Field | Description |
|--------|--------------|
| `medicine_name` | Name of medicine |
| `brand` | Manufacturer/Company |
| `salt_composition` | Active ingredients |
| `price` | Retail price (PKR) |
| `category` | Genre (Antibiotic, Analgesic, etc.) |
| `dosage_form` | Tablet, Syrup, Injection, etc. |
| `store_name` | Data source |

---

### 📦 Sample JSON Data

```json
{
  "medicine_name": "Augmentin 625mg",
  "brand": "GSK",
  "salt_composition": "Amoxicillin + Clavulanic Acid",
  "price": 540,
  "category": "Antibiotic",
  "dosage_form": "Tablet",
  "store_name": "dvago.pk"
}
````

---

## 🧮 **Machine Learning Phase (Upcoming)**

### 📚 Step 1: Data Cleaning

* Remove duplicate brands.
* Normalize price scales.
* Standardize salt names (e.g., "Paracetamol" vs "Acetaminophen").

### 🧠 Step 2: Feature Engineering

* Convert salt composition to vectors using **TF-IDF / BERT embeddings**.
* Calculate **cosine similarity** between medicine compositions.

### 🔍 Step 3: Model Training

* Algorithms:

  * KNN (for similarity)
  * Clustering (k-means for grouping medicines)
  * Regression (to predict optimal price range)

### 🧾 Step 4: Output Example

| Input Medicine            | Recommended Alternatives     | Price Difference |
| ------------------------- | ---------------------------- | ---------------- |
| Augmentin 625mg (PKR 540) | AmoxyClav 625mg (PKR 320)    | -41%             |
|                           | Moxiclav 625mg (PKR 370)     | -31%             |
|                           | Novamox-Clav 625mg (PKR 350) | -35%             |

---

## 🏗️ **Architecture Overview**

```plaintext
                    ┌─────────────────────────────┐
                    │   Web Scraping Engine       │
                    │ (dvago, sehat, emeds, etc.) │
                    └──────────────┬──────────────┘
                                   │
                      Raw Data (50K+ Rows)
                                   │
                    ┌──────────────▼──────────────┐
                    │   Data Cleaning & EDA       │
                    └──────────────┬──────────────┘
                                   │
                        Standardized Dataset
                                   │
                    ┌──────────────▼──────────────┐
                    │   ML Model Training (KNN)   │
                    └──────────────┬──────────────┘
                                   │
                         Affordable Medicine Finder
                                   │
                    ┌──────────────▼──────────────┐
                    │   Streamlit / Flask UI App  │
                    └─────────────────────────────┘
```

---

## 🔁 **Example Recommendation Flow**

| Step | Description                               |
| ---- | ----------------------------------------- |
| 1️⃣  | User inputs a branded high-cost medicine  |
| 2️⃣  | Model extracts its salt composition       |
| 3️⃣  | Searches for same composition in dataset  |
| 4️⃣  | Sorts by lowest price                     |
| ✅    | Returns top 3 most affordable equivalents |

---

## 📊 **Visual Insights (Concept)**

### 1. Price Comparison Chart

> A bar chart showing price difference between prescribed and suggested medicines.

![Price Comparison](https://raw.githubusercontent.com/Faizan-Ashiq/affordable-medicine-recommender/main/images/price_chart.png)

### 2. Composition Similarity Map

> A 2D scatter plot showing clustering of medicines by salt similarity.

![Salt Similarity](https://raw.githubusercontent.com/Faizan-Ashiq/affordable-medicine-recommender/main/images/salt_map.png)

---

## ⚙️ **Tech Stack**

| Category              | Tools & Frameworks              |
| --------------------- | ------------------------------- |
| **Language**          | Python 3.12                     |
| **Scraping**          | Selenium, BeautifulSoup4        |
| **Data Handling**     | Pandas, NumPy                   |
| **Machine Learning**  | scikit-learn, TensorFlow        |
| **Visualization**     | Matplotlib, Seaborn             |
| **Database (Future)** | Firebase Firestore / PostgreSQL |
| **Frontend**          | Streamlit / Flask               |
| **Version Control**   | Git & GitHub                    |

---

## 🧭 **Progress Overview**

| Task          | Progress            | Status |
| ------------- | ------------------- | ------ |
| Web Scraping  | ██████████░░░░░░░░  | 70%    |
| Data Cleaning | ████████░░░░░░░░░░  | 50%    |
| Model Design  | █████░░░░░░░░░░░░░  | 40%    |
| Visualization | ████░░░░░░░░░░░░░░  | 35%    |
| Deployment    | ██░░░░░░░░░░░░░░░░░ | 20%    |

---

## 💻 **Installation**

```bash
# Clone the repository
git clone https://github.com/faizan-ai/Affordable-Medicine-Recommendation.git

# Navigate into folder
cd Affordable-Medicine-Recommendation

# Install dependencies
pip install -r requirements.txt

# (Optional) Run scraping
python scrape_data.py

# Train model
python train_model.py

# Launch app
streamlit run app.py
```

---

## 🚀 **Usage Example**

```bash
> Enter Medicine Name: Augmentin 625mg
✅ Fetching affordable alternatives...

🔹 AmoxyClav 625mg — PKR 320  (-41%)
🔹 Moxiclav 625mg — PKR 370   (-31%)
🔹 Novamox-Clav 625mg — PKR 350 (-35%)
```

---

## 🧭 **Future Scope**

* Integrate **real-time pharmacy APIs**.
* Add **side-effect & rating-based filtering**.
* Build **mobile app** (React Native or Flutter).
* Expand to **global markets** (India, Bangladesh, etc.).
* Integrate **Generative AI** to explain substitutions in simple terms.

---

## 🧪 **Results Preview**

![App UI Preview](https://raw.githubusercontent.com/Faizan-Ashiq/affordable-medicine-recommender/main/images/app_ui.png)

> A clean UI where users can enter any medicine name and instantly get 3+ cheaper alternatives with verified data.

---

## 🤝 **Contribute**

We welcome open-source contributions! 💡
Here’s how you can help:

1. Fork this repo
2. Create a feature branch (`feature/amoxy-matcher`)
3. Commit your changes
4. Push to your branch
5. Submit a Pull Request 🚀

---

## 👨‍💻 **Author**

**Muhammad Faizan**
📍 Faisalabad, Pakistan
💼 Data Scientist | AI/ML Engineer | Data Scientist 
📧 [hellofaizan899@gmail.com](mailto:hellofaizan899@gmail.com)
🐙 [GitHub](https://github.com/Faizan-Ashiq)

---

## 🛡️ **License**

Distributed under the **MIT License**.
See `LICENSE` for more information.

---

## 🙏 **Acknowledgments**

Special thanks to:

* Online pharmacies providing open data.
* Open-source ML & scraping libraries.
* Healthcare workers inspiring affordability.
* The global open-source community 🌍.

---

<p align="center">  
Made with ❤️ by <strong>Muhammad Faizan</strong> | Data Science for Humanity 🌐  
</p>
```
