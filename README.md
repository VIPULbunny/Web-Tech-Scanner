# 🔍 Technology Detector

A powerful Python-based tool that scrapes a given website and detects the technologies used on it! This tool utilizes web scraping and pattern matching to identify various technologies, frameworks, and libraries implemented in the site's HTML, scripts, and metadata.

## 🚀 Features
- Scrapes a website and analyzes its **HTML, meta tags, and scripts**
- Matches technologies against a predefined dataset
- Provides a **clean and accurate** list of detected technologies
- Fast and efficient, using **BeautifulSoup** for parsing and **requests** for fetching data

## 📌 Tags
`Python` `Web Scraping` `Technology Detector` `BeautifulSoup` `Requests` `Automation`

---

## 📥 Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with the required libraries.

```sh
pip install pandas requests beautifulsoup4
```

### Clone the Repository
```sh
git clone https://github.com/yourusername/technology-detector.git
cd technology-detector
```

---

## ⚡ Usage
Run the script and enter a website URL to analyze.

```sh
python technolog.py
```

### Example Output:
```
Enter the website URL: https://example.com
Formatted URL: example.com
Technologies used in this website: jQuery, Bootstrap, Google Analytics
```

---

## 🛠 How It Works
1. **Loads Technology Data** 📂
   - Fetches a dataset of web technologies from a JSON file.
   - Converts the dataset into a structured **pandas DataFrame**.

2. **Scrapes the Website** 🌐
   - Uses `requests` to fetch the page source.
   - Parses the HTML using `BeautifulSoup`.

3. **Matches Technologies** 🔍
   - Extracts **scripts, meta tags, and headers** from the website.
   - Checks for predefined technology patterns.
   - Returns a list of matched technologies.

---

---

## 🌟 Future Enhancements
✅ Add support for more technology datasets 🔧
✅ Improve accuracy with **machine learning-based detection** 🤖
✅ Build a **GUI or Web Interface** for ease of use 🖥️

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to modify.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📧 Contact
Have questions or suggestions? Feel free to reach out!

📩 Email: vipulsolanki339@gmail.com  
🔗 GitHub: [VIPULbunny](https://github.com/VIPULbunny)

