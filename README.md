<h1 align="center"><center>G-Scraper</center></h1>
<h2 align="center"><center>A GUI based web scraper, written wholly in Python</center></h2>
<hr>
<h3>What:</h3>
<p>
  A fun little side project that I made.
</p>
<hr>
<h3>Why:</h3>
<p>I was searching through reddit one day for project ideas and came across a post complaining about there not being any GUI web scrapers. So without looking any further into it on whether there is one or is'nt I decided to put my webscraping and python knowledge to use.</p>
<hr>
<h3>Features:</h3>(✅means that it is implemented. ❌means that i am working on it.)
<br>
<ol>
  <li>✅ Supports 2 request types; GET & POST (at the moment)</li>
  <li>✅ Shows all your added info in a list</li>
  <li>✅ Can scrape multiple URLs</li>
  <li>✅ Can scrape multiple elements from the same URL (webpage)</li>
  <li>✅ So putting the two together, can scrape multiple elements from multiple URLs, ensuring that the element is from the URL it was assigned to</li>
  <li>✅ Can pass request parameters into the request to send for scrape</li>
  <li>✅ Since parameters can be passed, it can also handle logins/signups</li>
  <li>✅ Saves the scraped data in a seperate 'data/scraped-data' folder</li>
  <li>Has a logging function: logs 3 types of outputs<ul>
    <li>✅ Elemental (for elements)</li>
    <li>✅ Pagical   (for webpages)</li>
    <li>✅ Error     (for errors)</li>
  </ul></li>
  <li>Handles all types of errors</li>
  <li>✅ Request function runs in a seperate thread than GUI so you can do things while your request is being run</li>
  <li>❌ Functionality to edit the variables once they have been added</li>
  <li>❌ Can delete an unwanted item from the list of added variables</li>
  <li>✅ Can reset the entire app to start brand new after a scrape/set of scrapes</li>
  <li>❌ Provides verbose output to user in the GUI (this is very hard)</li>
  <li>❌ User can set 'presets', basically if user does a scrape repetitively they can set a preset. User can then just load and run the preset without having to define the variables each time</li>
  <li>✅ Unique way for generating unique filename for each log AND save data file so that no mixups happen</li>
</ol>
<hr>
<h3>What is used to create this:</h3>
<b>Main:</b>
<ul>
  <li>PyQT5 (for the GUI)</li>
  <li>Requests (for the web requests)</li>
  <li>BeautifulSoup4 (for scraping and parsing the HTML)</li>
  <li>threading (for the seperate threads)</li>
</ul>
<b>Add ons:</b>
<ul>
  <li>datetime (used in logging and saved data file creation)</li>
  <li>random (used in file creation)</li>
  <li>os (used to get current working directory)</li>
  Note: all these are Python libraries
</ul>
