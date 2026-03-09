# 🔬 Academic Research Summarizer & Social Media Pipeline

## Project Overview
This automation pipeline streamlines the process of academic literature review and social media content creation. It fetches recent articles from PubMed, filters them for specific research priorities, and utilizes **Claude 3.5 Sonnet** to generate accessible, high-school-level summaries for LinkedIn, Facebook/Threads, and BlueSky.

---

## 🏗 Workflow Architecture

The workflow follows a linear logic with an iterative core to handle batches of research papers.

### 1. Data Retrieval & Preparation
* **HTTP (1) & Parse JSON (2):** Triggers the initial search to PubMed.
* **Router (3):** Manages flow control and ensures the batch doesn't exceed weekly processing limits.
* **Iterator (4):** Converts the array of article IDs into individual processing bundles.

### 2. Deep Enrichment
* **Tools (50) - Sleep:** A brief pause to ensure compliance with API rate limits (essential for academic databases).
* **HTTP (6) & Parse JSON (38):** Fetches the full metadata, including the abstract, DOI, and author list for each specific ID.

### 3. Logic Gate (The Filter)
* **Keyword Filter:** A Regex-based filter that scans the abstract for specific high-priority terms:
    * *Keywords:* `children`, `students`, `education`, `colorectal cancer`, `health`, `policy`, `socioeconomic`, `poverty`, `AI`, `learning`, `school`.
    * *Logic:* Only articles matching at least one keyword proceed to the AI processing stage.

### 4. AI Processing (Claude 3.5 Sonnet)
* **Tools (55) - Variable Mapping:** Consolidates metadata. Author arrays are flattened using:
    `{{join(map(55.articleAuthors; "LastName"); ", ")}}`
* **JSON Create (58):** Wraps the "Research Summary Generation Prompt" and article data into a structured JSON payload.
* **HTTP (54):** Sends the payload to Anthropic’s API.
* **JSON Parse (56):** Unpacks the AI's response into individual summaries and supporting quotes.

### 5. Final Output
* **Google Sheets (57):** Logs all generated content into a centralized database. Columns include:
    * Article Title & DOI
    * Formatted Authors
    * LinkedIn Summary (600-800 chars)
    * Threads/Facebook Summary (500 chars)
    * BlueSky Summary (300 chars)
    * 5 Supporting Quotes

---

## 🛠 Maintenance & Configuration

### Updating the AI Persona
To change the tone or character limits of the summaries, edit the **System Prompt** in **Module 58**. Ensure the "Strict Output Rule" remains at the top to prevent JSON parsing errors.

### Adjusting Research Scope
To monitor new topics, update the Filter between **Module 38** and **Module 55**. Use the pipe `|` symbol to separate new keywords in the Regex string.

### Troubleshooting JSON Errors
If the flow stops at **Module 56** with a "Source is not valid JSON" error, check the Claude response in **Module 54**. If Claude added conversational text, ensure the prompt explicitly forbids anything outside the `{ }` curly braces.

---
*Generated for workflow documentation - March 2026*
