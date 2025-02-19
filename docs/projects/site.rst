JudaicaLink Site
================

JudaicaLink Site is the **public-facing portal** of the JudaicaLink project. It provides background information, dataset overviews, project updates, and links to related JudaicaLink resources, including Labs and Pubby. The site is built using **Hugo**, a static site generator, ensuring fast performance and easy maintainability.

## **Features of JudaicaLink Site**

### **1. Overview of JudaicaLink**
- Describes the mission and goals of JudaicaLink.
- Explains how JudaicaLink integrates Jewish studies datasets into a Linked Open Data knowledge graph.

### **2. Dataset Information**
- Lists available **datasets** and their sources.
- Provides links to **entity pages** and **SPARQL queries**.

### **3. News and Updates**
- Regular updates on JudaicaLink’s latest developments, publications, and features.
- Information about conferences and workshops related to JudaicaLink.

### **4. Legal and Contact Information**
- Licensing information for datasets and code.
- Contact details for JudaicaLink project maintainers.

## **How to Use JudaicaLink Site**

### **Navigating the Website**
1. Visit **[https://www.judaicalink.org](https://www.judaicalink.org)**.
2. Browse the menu for **Datasets, Documentation, News, and Project Information**.
3. Click on dataset links to explore entity data and SPARQL examples.

### **Finding Dataset Details**
- Go to **Datasets** and select a dataset to view its metadata and sources.
- Use provided **SPARQL query examples** to interact with structured data.

### **Reading News & Updates**
- Visit **[https://www.judaicalink.org/news/](https://www.judaicalink.org/news/)** for the latest project announcements.

## **Technical Overview**

### **Backend**
- Built using **Hugo**, a static site generator.
- Hosted on **GitHub Pages** and **Netlify** for continuous deployment.

### **Data Sources**
- All datasets are sourced from **JudaicaLink Labs** and **SPARQL endpoints**.
- Links to external data sources like **Wikidata, GND, and Compact Memory**.

## **Contributing to JudaicaLink Site**

### **Setting Up the Site Locally**

1. **Clone the repository**
   ```sh
   git clone https://github.com/judaicalink/judaicalink-site.git
   cd judaicalink-site
   ```
2. **Install Hugo** (if not already installed)
   ```sh
   brew install hugo  # macOS
   sudo apt install hugo  # Linux
   ```
3. **Run the local server**
   ```sh
   hugo server
   ```
4. Open **http://localhost:1313/** in your browser to preview the site.

### **Making Changes**
- Edit `.md` files in the **content/** directory.
- Update **dataset descriptions** in the `content/datasets/` folder.
- Add news updates in the `content/news/` directory.
- Commit changes and push them to GitHub for deployment.

### **Deployment**
- The site is automatically built and deployed using **Netlify/GitHub Actions**.
- All changes to the `main` branch trigger an automatic update.

## **Troubleshooting & Support**
- **Website not loading?** Check [GitHub Issues](https://github.com/judaicalink/judaicalink-site/issues).
- **Errors in dataset links?** Verify entity URLs in **Labs or Pubby**.
- **Need help?** Contact us at [https://www.judaicalink.org/contact/](https://www.judaicalink.org/contact/).

---
JudaicaLink Site serves as the main entry point for users exploring Jewish studies data. Stay updated with the latest project news and dataset expansions at **[https://www.judaicalink.org](https://www.judaicalink.org)**.

