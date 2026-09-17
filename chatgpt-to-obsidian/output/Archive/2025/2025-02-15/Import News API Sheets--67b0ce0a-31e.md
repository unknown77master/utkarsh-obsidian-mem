---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "67b0ce0a-31e4-8007-9f54-d618e986f00e"
created: 1739640330.408564
updated: 1739816113.989196
resource_section: true
---

# Import News API Sheets

## User

i want to import entire live news article with entire text of article not snippets of article in sheets. which API should i use

Please write in English language.

## Assistant

To import entire live news articles (not just snippets) into Google Sheets, you can use the following APIs: 

### **1. NewsAPI** (\[newsapi.org\](https://newsapi.org/)) 
- Provides news articles from major publishers. 
- Free version only includes headlines and snippets. 
- **Paid version** allows access to full articles. 

### **2. GNews API** (\[gnews.io\](https://gnews.io/)) 
- Offers full-text articles with a paid plan. 
- Supports Google Sheets integration via Apps Script. 

### **3. Aylien News API** (\[aylien.com\](https://aylien.com/)) 
- Provides enriched full-text articles with NLP features. 
- Paid service required for full content. 

### **4. Newscatcher API** (\[newscatcherapi.com\](https://newscatcherapi.com/)) 
- Fetches full news articles from various sources. 
- Offers structured data for easy integration into Sheets. 

### **5. Bing News Search API** (\[Azure Bing News\](https://www.microsoft.com/en-us/bing/apis/bing-news-search-api)) 
- Provides full-text articles from Bing’s news index. 
- Requires an Azure subscription. 

### **How to Import into Google Sheets?** 
1. **Use Apps Script**: Write a Google Apps Script to fetch data from the API and insert it into Sheets. 
2. **Use a No-Code Solution**: Platforms like **Zapier** or **Make (Integromat)** can fetch and update articles in Sheets. 

#### **Recommendation:** 
For **free** options, use **GNews API**. 
For **paid**, **NewsAPI or Aylien News API** provide better coverage. 

Would you like help with writing a Google Apps Script to import articles? 🚀

## User

Use a No-Code Solution: Platforms like Zapier or Make (Integromat) can fetch and update articles in Sheets.

Please write in English language.

## Assistant

If you want to import full-text news articles into **Google Sheets** without coding, you can use **Zapier** or **Make (Integromat)**. Here's how: 

---

### **Option 1: Using Zapier** 
Zapier allows you to connect a news API with Google Sheets automatically. 

#### **Steps to Set Up:**
1. **Sign up for Zapier** (\[zapier.com\](https://zapier.com/)). 
2. **Choose a News API** as the trigger (e.g., **GNews, NewsAPI, or Newscatcher**). 
3. **Set up the trigger:** 
 - Enter API key and configure the filters (e.g., keywords, sources). 
 - Select the data you need (title, full text, URL, etc.). 
4. **Choose Google Sheets as the action app.** 
5. **Map the data fields** (e.g., article title in column A, full text in column B). 
6. **Turn on the Zap** to automate article imports. 

🚀 **Zapier is easy but may require a paid plan for full-text data.** 

---

### **Option 2: Using Make (Integromat)** 
Make (formerly Integromat) is another **automation platform** that can fetch full news articles and insert them into Google Sheets. 

#### **Steps to Set Up:**
1. **Sign up for Make** (\[make.com\](https://www.make.com/)). 
2. **Create a new scenario.** 
3. **Add a trigger module** (use **"HTTP" or a specific News API module**). 
4. **Set up the API request** to fetch full articles. 
5. **Add a Google Sheets module** and select "Add Row." 
6. **Map fields (title, content, URL, etc.) into the sheet.** 
7. **Schedule the automation** (e.g., run every hour). 
8. **Save and activate the scenario.** 

🎯 **Make offers more flexibility and pricing options compared to Zapier.** 

---

### **Which One to Use?**
- **For simplicity → Zapier** 
- **For flexibility & cost-effectiveness → Make (Integromat)** 

Would you like step-by-step guidance for a specific news API? 😊

## User

yes

Please write in English language.

## Assistant

Let's go step by step to import **full-text news articles** into **Google Sheets** using **Make (Integromat)** with **GNews API**. 

---

### **Step 1: Get GNews API Key** 
1. Go to **\[GNews API\](https://gnews.io/)** and sign up. 
2. Get your **API key** (you need a paid plan for full-text articles). 

---

### **Step 2: Set Up Make (Integromat) Account** 
1. Sign up at **\[make.com\](https://www.make.com/)**. 
2. Click **"Create a new scenario."** 

---

### **Step 3: Add GNews API Module** 
1. Click the **"+" button** and search for **"HTTP"** (since Make does not have a direct GNews module). 
2. Select **"Make a request."** 
3. In the **URL field**, enter: 
 ```
 https://gnews.io/api/v4/search?q=technology&token=YOUR_API_KEY&lang=en&max=10
 ```
 - Replace `YOUR_API_KEY` with your actual GNews API key. 
 - Change **`q=technology`** to your preferred topic. 
4. Set **Method** to **GET**. 
5. Click **"OK."** 

---

### **Step 4: Add Google Sheets Module** 
1. Click the **"+" button** and search for **"Google Sheets."** 
2. Select **"Add a row."** 
3. Connect your **Google account.** 
4. Choose your **Google Sheet** where you want to save news articles. 
5. Map fields from the API response: 
 - **Column A → Title** → `articles.title` 
 - **Column B → Full Text** → `articles.content` 
 - **Column C → URL** → `articles.url` 
 - **Column D → Source** → `articles.source.name` 
6. Click **"OK."** 

---

### **Step 5: Test & Activate** 
1. Click **"Run Once"** to test the automation. 
2. Check if articles appear in your **Google Sheet**. 
3. If everything is correct, **schedule** it to run **every 1 hour.** 
4. Click **"Save & Activate."** 

---

### **Done! 🎉** 
Now, your Google Sheet will update automatically with **full-text news articles** from GNews API! 🚀 

Would you like a video tutorial link or help with another API? 😊

## User

yes

Please write in English language.

## Assistant

Certainly! Let's walk through the process of importing **full-text news articles** into **Google Sheets** using **Make (formerly Integromat)** and the **GNews API**. This method allows you to automate the retrieval and storage of live news articles without any coding.

---

### **Prerequisites**

1. **GNews API Key**: Sign up at \[GNews\](https://gnews.io/) to obtain your API key. Note that full-text articles require a paid plan.
2. **Make Account**: Create an account at \[Make\](https://www.make.com/).
3. **Google Sheet**: Prepare a Google Sheet where the articles will be stored.

---

### **Step 1: Set Up the GNews API Request in Make**

1. **Create a New Scenario**:
 - Log in to your Make account.
 - Click on **"Create a new scenario"**.

2. **Add an HTTP Module**:
 - Click the **"+"** icon to add a module.
 - Search for **"HTTP"** and select the **"Make a request"** module.

3.

## User

free api to scrape latest full text article with unlimited api calls

Please write in English language.

## Assistant

Finding a **free** API that provides **full-text news articles** with **unlimited API calls** is difficult because most news APIs have restrictions. However, here are some **free options** that you can try: 

---

### **1. NewsData.io API** (\[newsdata.io\](https://newsdata.io/)) 
✅ **Free Plan**: Yes (Limited requests) 
✅ **Full-Text Articles**: Available for some sources 
✅ **Unlimited API Calls**: No (Free plan has limits) 
🔗 **Sign Up**: \[newsdata.io\](https://newsdata.io/) 

💡 **Best for:** Fetching news articles with content from multiple sources. 

---

### **2. Free News API (by Marketaux)** (\[marketaux.com\](https://www.marketaux.com/)) 
✅ **Free Plan**: Yes (100 API calls/day) 
✅ **Full-Text Articles**: Available 
✅ **Unlimited API Calls**: No 
🔗 **Sign Up**: \[marketaux.com\](https://www.marketaux.com/) 

💡 **Best for:** Financial and general news. 

---

### **3. Scraping with RSS Feeds** (No API needed) 
✅ **Free Plan**: Yes 
✅ **Full-Text Articles**: Available (depends on the source) 
✅ **Unlimited API Calls**: Yes (depends on the site) 

🔹 **How to use:** 
1. Find the **RSS feed** of a news website (e.g., `https://www.bbc.co.uk/news/rss.xml`). 
2. Use a tool like **Zapier, Make, or Google Apps Script** to fetch and store news articles in Google Sheets. 

💡 **Best for:** Unlimited scraping of news articles without using an API. 

---

### **4. Web Scraping with Python (If Allowed)** 
If APIs don’t work, you can use Python with **BeautifulSoup** or **Selenium** to scrape full-text articles from news websites (if allowed by their terms of service). 

---

### **Which One to Choose?** 
- If you want **an API**, try **NewsData.io** or **Marketaux**. 
- If you want **unlimited free access**, use **RSS feeds** or **web scraping** (if legal). 

Would you like a step-by-step guide for any of these options? 😊

## User

i want to import all news along with their entire text of every news

Please write in English language.

## Assistant

If you want to **import all news articles with their full text**, here are the best methods: 

---

## **1. Use a Free or Paid News API** 
### **Best APIs for Full-Text News Articles:** 
| API Name | Free Plan? | Full-Text Available? | Limitations |
|----------|------------|----------------------|-------------|
| **NewsData.io** | ✅ Yes | ✅ Some sources | Free plan has limits |
| **GNews API** | ✅ Yes | ❌ Only summaries | Paid plan for full text |
| **Marketaux API** | ✅ Yes | ✅ Yes | 100 API calls/day |
| **Newscatcher API** | ❌ No | ✅ Yes | Paid only |

🔗 **Best Option**: \[NewsData.io\](https://newsdata.io/) (for free access) 

### **How to Import News into Google Sheets Using APIs (No Code)**
1. **Sign up** on \[NewsData.io\](https://newsdata.io/) and get an API key. 
2. **Use Zapier or Make (Integromat)** to fetch articles and store them in Google Sheets. 
3. **Set API request URL** in Make/Zapier: 
 ```
 https://newsdata.io/api/1/news?apikey=YOUR_API_KEY&language=en
 ```
4. **Map the fields** (Title, Full Text, URL) to Google Sheets. 
5. **Schedule the automation** to update regularly. 

🚀 **Now, your sheet will update automatically!** 

---

## **2. Use RSS Feeds (Unlimited & Free)**
✅ **No API needed** 
✅ **Unlimited news** 
❌ **Not all sources provide full text** 

### **How to Use RSS Feeds**
1. Find the **RSS feed** of a news site (e.g., BBC: `https://feeds.bbci.co.uk/news/rss.xml`). 
2. Use **Google Apps Script** or **Zapier** to fetch and store data in Sheets. 
3. **Extract full text** using an RSS parser. 

---

## **3. Use Web Scraping (If Allowed)**
If no API gives full text, you can scrape news articles using: 
- **Python (BeautifulSoup, Scrapy, Selenium)** 
- **Google Apps Script (for lightweight scraping)** 

⚠️ **Check the website’s terms before scraping!** 

---

### **Which Option is Best?**
- **For a simple & legal way** → Use **NewsData.io API** 
- **For unlimited free news** → Use **RSS Feeds** 
- **For extracting full text when APIs fail** → Use **Web Scraping** 

Would you like a **step-by-step tutorial** for any method? 😊

## Resources

### External references
- [Google Sheets API Overview | Google for Developers](https://developers.google.com/sheets/api/guides/concepts)
- [Google Sheets | Google for Developers](https://developers.google.com/sheets)
- [Create car slideshow videos using Make (Integromat) and Google Sheets — Shotstack](https://shotstack.io/learn/automatically-generate-car-slideshow-videos-integromat/)
- [Google Sheets API v4 Integration Guide — SitePoint](https://www.sitepoint.com/google-sheets-api-v4-integration-guide/)
- [Google Sheets](https://www.make.com/en/help/app/google-sheets)
- [How to Connect & Load Data from GNews to Google Sheets?](https://airbyte.com/how-to-sync/gnews-to-googlesheets)
- [Google Sheets (legacy) App Help Docs](https://www.integromat.com/en/help/app/google-sheets-legacy)
- [Google Sheets API Setup](https://ai2.appinventor.mit.edu/reference/other/googlesheets-api-setup.html)
- [How to generate images from Google Sheet data with Integromat - Placid.app](https://placid.app/blog/how-to-generate-images-from-google-sheet-data-with-integromat)
- [How to Connect Typeform And Google Sheets With Integromat - YouTube](https://www.youtube.com/watch?v=xqAMxszC3nM)
- [Sheety - Turn your Google Sheet into an API](https://sheety.co/)
- [How to Use The Google Sheets Watch Changes Module | by Integromat | Medium](https://medium.com/%40integromat/use-the-google-sheets-watch-changes-webhook-to-instantly-retrieve-and-email-data-6cd22418e2c5)
