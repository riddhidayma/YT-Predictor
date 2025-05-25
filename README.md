# 📈 YouTube Channel Growth Predictor

This project uses **Multiple Linear Regression (MLR)** to predict **monthly views** for a YouTube channel based on key input features like subscriber count, upload frequency, channel age, and more. Built with Python and integrated with a Bolt AI-based front-end.

---

## 🚀 Features

- Predicts **monthly views** using historical channel data
- Calculates **view-to-subscriber ratio**
- Estimates **growth potential (%)**
- Shows **influencing factors** based on model weights
- Provides **confidence score** based on model performance
- Stores **recent predictions** in session

---

## 📊 Inputs

| Field                     | Description                             |
|--------------------------|-----------------------------------------|
| Channel Name             | (Text) - Identifier, not used in model  |
| Current Subscribers      | (Numeric) - Total subscribers            |
| Upload Frequency         | (Numeric) - Videos per month            |
| Channel Age (Months)     | (Numeric) - How old the channel is      |
| Channel Niche            | (Categorical) - Niche like Tech, Vlogs  |
| Avg. Video Length        | (Numeric) - Avg duration in minutes     |

---

## 🎯 Target Output

- `Predicted Monthly Views`
- `Confidence (%)` — based on R²
- `View/Subscriber Ratio`
- `Growth Potential (%)`
- `Influencing Factor Breakdown`
- AI-generated summary insights

---

## 🧠 Model Used

**Multiple Linear Regression (MLR)** using `scikit-learn`.



