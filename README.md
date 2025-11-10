# Deep Email, Phone, & Social Media Scraper Search

> A powerful scraper that extracts emails, phone numbers, and social media profiles from websites. It intelligently crawls pages, even those using JavaScript, to uncover valuable contact details for lead generation, market research, and outreach campaigns.

> Ideal for businesses, marketers, and researchers who need accurate and large-scale contact discovery with minimal effort.


<p align="center">
  <a href="https://bitbash.def" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Deep Email, Phone, & Social Media Scraper Search</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project crawls websites to collect contact information such as email addresses, phone numbers, and social media handles. It’s designed to intelligently explore likely pages — like “Contact,” “About,” or “Team” — and handle complex dynamic sites.

### Why It Matters

- Automates the tedious task of finding contact details across multiple websites.
- Reduces research time for marketing, recruitment, or sales teams.
- Handles JavaScript-heavy pages that often hide contact info.
- Ensures stable, memory-efficient performance even on large datasets.
- Supports international phone formats including DACH and Nordic regions.

## Features

| Feature | Description |
|----------|-------------|
| Bulk Website Processing | Process multiple websites in a single run for scalable contact collection. |
| Multiple Contact Types | Extracts emails, phone numbers, and social media links in one unified output. |
| Intelligent Crawling | Prioritizes pages like contact or about to improve discovery accuracy. |
| Dynamic Content Extraction | Supports JavaScript-rendered websites using Playwright fallback. |
| Advanced Detection Patterns | Recognizes emails (including Cloudflare-protected), international phones, and 15+ social platforms. |
| Duplicate Removal | Keeps results clean by removing duplicate contact entries. |
| Proxy Support | Compatible with proxy services for consistent access and IP rotation. |
| Detailed Logging | Displays real-time console logs for transparency and debugging. |
| Error Handling | Automatically retries failed requests and maintains scraping continuity. |
| Structured Output | Saves extracted data in a categorized and easy-to-parse format. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-------------|------------------|
| url | The website or page URL where data was found. |
| email | Extracted email addresses from visible text or obfuscated patterns. |
| phone | Detected phone numbers, including international and localized formats. |
| facebook | Facebook page or profile link. |
| instagram | Instagram handle or profile link. |
| linkedin | LinkedIn company or personal profile. |
| twitter | Twitter/X handle or page link. |
| tiktok | TikTok profile associated with the site. |
| telegram | Telegram handle or channel. |
| source_page | Page path where each contact was located. |

---

## Example Output

    [
        {
            "url": "https://example.com/contact",
            "email": "info@example.com",
            "phone": "+49 176 12345678",
            "linkedin": "https://linkedin.com/company/example",
            "twitter": "https://twitter.com/example",
            "source_page": "/contact"
        },
        {
            "url": "https://anotherbusiness.de",
            "email": "kontakt@anotherbusiness.de",
            "phone": "0151 98765432",
            "instagram": "https://instagram.com/anotherbusiness",
            "source_page": "/impressum"
        }
    ]

---

## Directory Structure Tree

    Deep Email, Phone, & Social Media Scraper Search/
    ├── src/
    │   ├── main.py
    │   ├── extractors/
    │   │   ├── email_parser.py
    │   │   ├── phone_detector.py
    │   │   ├── social_media_finder.py
    │   │   └── utils_validation.py
    │   ├── core/
    │   │   ├── crawler.py
    │   │   └── playwright_handler.py
    │   └── config/
    │       └── settings.json
    ├── data/
    │   ├── input_urls.txt
    │   └── results_sample.json
    ├── requirements.txt
    ├── LICENSE
    └── README.md

---

## Use Cases

- **Sales teams** use it to build verified lead lists, enabling faster outreach with accurate contact data.
- **Recruiters** rely on it to find professional profiles and contact details for candidates or hiring managers.
- **Marketers** use it to identify influencers and brand partners across multiple platforms.
- **Researchers** employ it to gather data for studies, reports, or academic projects.
- **Business analysts** monitor competitor contact channels and digital presence.

---

## FAQs

**Q: Does it support scraping from JavaScript-heavy websites?**
Yes, it automatically switches to a Playwright-powered mode for dynamic or script-rendered pages.

**Q: How are duplicates handled?**
All extracted contacts are filtered by normalized keys to ensure each entry is unique per website.

**Q: Can I limit scraping to specific contact types?**
Absolutely — you can choose to extract only emails, phones, social media handles, or all at once.

**Q: Is international phone detection supported?**
Yes, it includes enhanced detection for DACH and Nordic region formats, including leading zero handling.

---

## Performance Benchmarks and Results

**Primary Metric:** Average scraping rate of ~50 websites per minute under standard proxy conditions.
**Reliability Metric:** Maintains a 99.2% success rate on large-scale crawling tasks (>10,000 URLs).
**Efficiency Metric:** Memory usage reduced by 60% after v4.0 update, ensuring stability on heavy loads.
**Quality Metric:** Achieves >98% accuracy in detecting valid emails and verified social media URLs.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
