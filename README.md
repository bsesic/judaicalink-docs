# JudaicaLink Documentation Repository

Welcome to the **JudaicaLink Documentation** repository. This repository contains the official documentation for JudaicaLink, a Linked Open Data knowledge graph for Jewish Studies.

## 📖 About JudaicaLink
JudaicaLink is a comprehensive knowledge graph that integrates various Jewish Studies datasets, connecting and enriching them using linked data technologies. The project is developed and maintained by Hochschule Mannheim in collaboration with FID Jüdische Studien, University of Frankfurt, and other partners.

🔗 **Website**: [https://www.judaicalink.org](https://www.judaicalink.org)  
🔗 **SPARQL Endpoint**: [https://data.judaicalink.org/sparql.html](https://data.judaicalink.org/sparql.html)  
🔗 **Read the Docs**: [https://judaicalink-docs.readthedocs.io/](https://judaicalink-docs.readthedocs.io/)  

---

## 📂 Repository Structure

```
/
│── docs/                  # Documentation source files
│   ├── conf.py            # Sphinx configuration
│   ├── index.rst          # Main documentation index
│   ├── getting_started.rst
│   ├── user_guide.rst
│   ├── developer_guide.rst
│   ├── api_reference.rst
│   ├── advanced_topics.rst
│   ├── contributing.rst
│   └── faq.rst
│── .readthedocs.yaml      # Read the Docs configuration
│── requirements.txt       # Python dependencies for documentation
│── README.md              # This file
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/judaicalink/judaicalink-docs.git
cd judaicalink-docs
```

### 2️⃣ Install Dependencies
Install the required packages to build the documentation:
```sh
pip install -r requirements.txt
```

### 3️⃣ Build the Documentation Locally
To generate the HTML documentation locally, run:
```sh
cd docs
make html  # On Linux/Mac
# or
make.bat html  # On Windows
```
The built documentation will be in `docs/_build/html/`. Open `index.html` in your browser to view it.

---

## 📄 Contributing
We welcome contributions! To contribute:
1. **Fork** the repository.
2. **Create a feature branch** for your changes.
3. **Submit a Pull Request** with a clear description of your changes.

For detailed guidelines, check the [Contributing Guide](docs/contributing.rst).

---

## 🔧 Read the Docs Integration
This repository is automatically built and hosted on Read the Docs. Any changes pushed to the repository will trigger an automatic rebuild of the documentation.

You can access the live documentation at:
➡ **[JudaicaLink Docs on Read the Docs](https://judaicalink-docs.readthedocs.io/)**

---

## 📞 Contact
For any inquiries, please reach out via:
- **Contact Page**: [https://labs.judaicalink.org/contact/](https://labs.judaicalink.org/contact/)
- **Email**: [info@judaicalink.org](mailto:info@judaicalink.org)

---

## 📜 License
This documentation is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

