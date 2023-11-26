# RateGain Code Rangers - Submission Report
### Team:  Geeky_Potential_Players

* Raag Bhutani
* Shudhant
* Priyank


### _Project Name_
RateCrawlerX

### _Project Ppt_
[RateCrawlerX.pptx](https://github.com/bhutani2002/Web_Scrapper_Rategain_Blogs/files/13465384/RateCrawlerX.pptx)


<!-- ABOUT THE PROJECT -->
# The Problem
The project entails a web scraping challenge where the task is to develop a program capable of extracting specific information from multiple pages of the "https://rategain.com/blog" website. The goal is to identify and collect data, highlighted in red, from various blog posts. The required information includes blog titles, publication dates, image URLs associated with the blogs, and the number of likes each post has received. The program is expected to navigate through different pages, and the gathered data should be efficiently organized and saved in either Excel or CSV format for easy analysis.

# Our Solution
This solution combines a React frontend with a Flask backend to facilitate web scraping of RateGain's blog website. The React frontend communicates with the Flask server to initiate the scraping process and subsequently download the extracted data. The backend utilizes Selenium to scrape blog information, organizes it into an Excel file using openpyxl, and provides an endpoint for the frontend to download the created file. Port information is exchanged through a JSON file, allowing seamless communication between the frontend and backend. The structured approach ensures modularity and maintainability, facilitating clear communication between the user interface and the web scraping functionality.

To collect data efficiently, the backend clicks and moves on to the next blog on each page, overcoming the challenge posed by pagination. Additionally, handling lazy-loaded images is implemented by scrolling the webpage both up and down, ensuring the comprehensive collection of image URLs.

### Technology Stack used:
```
- Python
- Flask
- Selenium
- React JS
- Tailwind CSS
```


<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

- [Node.js](https://nodejs.org/en/download/) (ensure Node.js is installed on your system)
- npm
  ```sh
  npm install npm@latest -g
  ```
- [Python](https://www.python.org/downloads/) (ensure Python is installed on your system)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bhutani2002/Web_Scrapper_Rategain_Blogs.git
   ```
3. Open a terminal, change directory to frontend folder and install npm packages
   ```sh
   cd frontend
   npm install
   ```
4. Run the frontend
   ```sh
   npm run start
   ```
This will execute the frontend code, and it will be accessible on a port number assigned by your computer.

5. Open a second terminal and change directory to backend folder and install npm packages
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
6. Run the backend
   ```sh
   python Blog_Details_Scrapper.py
   ```
7. Open your browser and go to the frontend hosted URL (usually http://localhost:3000).

8. Click on the "Scrape Data" button. The process of scraping data from RateGain's blog website will begin. The "Download Extracted Data" button will be disabled during this process.

9. Once the web scraping is complete, the "Download Extracted Data" button will be enabled. Click on it to download the Excel file containing all the required data from RateGain's blog website.

Now, you have successfully completed the web scraping process and downloaded the extracted data.

#### Working of RateCrawlerX
### VIDEO
```
[![Watch the video](https://img.youtube.com/vi/9bvI8clkIU8/maxresdefault.jpg)](https://www.youtube.com/watch?v=9bvI8clkIU8)

```
### SnapShot of the Landing Page
![image](https://github.com/bhutani2002/Web_Scrapper_Rategain_Blogs/assets/84590758/77d2b5bd-44e4-4bb3-965a-be78dcda3e51)



## Project Scalability / Future Plans
```
1. Optimize runtime by exploring alternative scraping methods to enhance data retrieval speed from the website.

2. Implement a user-friendly component or input mechanism allowing users to specify the desired blog page for data extraction. This feature would enhance customization and enable users to retrieve data from specific sections of the blog website.

3.Enhance modularity by breaking down complex functions into smaller, reusable components, promoting easier maintenance and scalability of the codebase.
```
