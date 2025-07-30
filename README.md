# Network Security - Phishing Detection System

A machine learning-based phishing detection system that analyzes website characteristics to identify potentially malicious URLs and protect users from phishing attacks.

## 🎯 Project Overview

This project implements an end-to-end machine learning pipeline for detecting phishing websites by analyzing various URL and website features. The system processes data from MongoDB, validates it, and builds predictive models to classify websites as legitimate or phishing attempts.

## 🚀 Features

- **Data Ingestion**: Automated data extraction from MongoDB collections
- **Data Validation**: Schema validation and drift detection using statistical tests
- **Feature Engineering**: Analysis of 30+ website characteristics including:
  - URL structure (IP addresses, length, special characters)
  - SSL certificates and domain registration
  - Website content features (iframes, pop-ups, redirects)
  - Traffic and ranking metrics
- **Machine Learning Pipeline**: Modular architecture for model training and prediction
- **Logging & Exception Handling**: Comprehensive error tracking and logging system

## 📊 Dataset Features

The system analyzes **31 key features** to detect phishing attempts:

### URL-Based Features
- `having_IP_Address` - Presence of IP address in URL
- `URL_Length` - Length of the URL
- `Shortining_Service` - Use of URL shortening services
- `having_At_Symbol` - Presence of '@' symbol
- `double_slash_redirecting` - Double slash redirecting
- `Prefix_Suffix` - Prefix or suffix separated by dash

### Domain & SSL Features  
- `having_Sub_Domain` - Number of subdomains
- `SSLfinal_State` - SSL certificate status
- `Domain_registeration_length` - Domain registration period
- `age_of_domain` - Age of domain
- `DNSRecord` - DNS record availability

### Content-Based Features
- `Favicon` - Favicon loading from external domain
- `HTTPS_token` - HTTPS token in domain
- `Request_URL` - Percentage of external requests
- `URL_of_Anchor` - Anchor URL analysis
- `Links_in_tags` - Links in meta, script, and link tags
- `SFH` - Server Form Handler
- `Submitting_to_email` - Form submission to email
- `Abnormal_URL` - Abnormal URL patterns
- `Redirect` - Number of redirects
- `on_mouseover` - onMouseOver event handling
- `RightClick` - Right-click disabling
- `popUpWidnow` - Pop-up window presence
- `Iframe` - Iframe usage

### Traffic & Reputation Features
- `port` - Abnormal port usage  
- `web_traffic` - Website traffic ranking
- `Page_Rank` - Google PageRank
- `Google_Index` - Google indexing status
- `Links_pointing_to_page` - Backlink analysis
- `Statistical_report` - Statistical reports from security vendors

## 🏗️ Project Structure

```
networksecurity/
├── components/
│   ├── data_ingestion.py      # MongoDB data extraction
│   └── data_validation.py     # Schema & drift validation
├── constant/
│   └── training_pipeline/     # Pipeline configurations
├── entity/
│   ├── config_entity.py       # Configuration classes
│   └── artifact_entity.py     # Data artifacts
├── exception/
│   └── exception.py           # Custom exception handling
├── logging/
│   └── logger.py              # Logging configuration
└── utils/
    └── main_utils/
        └── utils.py           # Utility functions

data_schema/
└── schema.yaml                # Data schema definition

main.py                        # Main pipeline execution
push_data.py                   # Data upload to MongoDB
requirements.txt               # Dependencies
setup.py                       # Package setup
```

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd network-security
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package**
```bash
pip install -e .
```

## ⚙️ Configuration

1. **Environment Setup**
   - Create a `.env` file in the root directory
   - Add your MongoDB connection string:
   ```
   MONGO_DB_URL=mongodb+srv://username:password@cluster.mongodb.net/
   ```

2. **Data Schema**
   - The `data_schema/schema.yaml` file defines the expected data structure
   - All 31 features are validated against this schema

## 🚀 Usage

### 1. Data Upload to MongoDB
```bash
python push_data.py
```

### 2. Run the Training Pipeline
```bash
python main.py
```

### 3. Pipeline Components

**Data Ingestion**
- Connects to MongoDB and extracts phishing dataset
- Splits data into training and testing sets (80:20 ratio)
- Saves processed data to feature store

**Data Validation**
- Validates schema compliance
- Performs drift detection using Kolmogorov-Smirnov test
- Generates drift reports for monitoring

## 📈 Model Performance

The system analyzes websites based on comprehensive feature engineering:
- **Accuracy**: Optimized through statistical validation
- **Drift Detection**: Monitors data quality over time
- **Scalability**: Modular design supports easy feature addition

## 🔧 Technical Stack

- **Language**: Python 3.8+
- **Database**: MongoDB
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Statistical Testing**: SciPy
- **Data Processing**: PyMongo, PyYAML
- **Environment Management**: python-dotenv

## 📝 Logging

- Automatic log generation with timestamps
- Comprehensive error tracking
- Pipeline execution monitoring
- Logs stored in `logs/` directory

## 🧪 Testing

The system includes:
- Schema validation tests
- Data drift detection
- Statistical significance testing (p-value < 0.05)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Ayush Poddar**
- Email: ayushpoddar351@gmail.com
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [Your GitHub Profile]

## 🙏 Acknowledgments

- Dataset contributors for phishing detection research
- Open source community for ML libraries
- MongoDB for database services

---

*This project demonstrates end-to-end machine learning pipeline development for cybersecurity applications, showcasing data engineering, validation, and model deployment capabilities.*
