<h1 align="center"><center>G-Scraper</center></h1>
<h2 align="center"><center>A GUI based web scraper, written wholly in Python</center></h2>
<hr>
<h3>What❓:</h3>
<p>
  A GUI based web scraper written in Python. Useful for data collectors who want a nice UI for scraping data from many sites.
</p>
<hr>
<h3>Why❓:</h3>
<p>I was looking through Reddit for fun project ideas and came across a thread in which there was a comment of someone complaining about there not being a GUI Web Scraper. Thus I started working on G-Scraper.</p>
<hr>
<h3>Features ✨:</h3>(✅ means that it is implemented. ❌ means that i am working on it.)
<br>
<ol>
  <li>✅ Supports 2 request types; GET & POST (at the moment)</li>
  <li>✅ Shows all your added info in a list</li>
  <li>✅ Can scrape multiple URLs</li>
  <li>✅ Can scrape multiple elements from the same URL (webpage)</li>
  <li>✅ So putting the two together, can scrape multiple elements from multiple URLs, ensuring that the element is from the URL it was assigned to</li>
  <li>✅ Can pass request parameters into the request to send for scrape <b>EXCEPT FILES (for now)</b></li>
  <li>✅ Since parameters can be passed, it can also handle logins/signups</li>
  <li>✅ Saves the scraped data in a seperate 'data/scraped-data' folder</li>
  <li>Has a logging function: logs 3 types of outputs<ul>
    <li>✅ Elemental (for elements)</li>
    <li>✅ Pagical   (for webpages)</li>
    <li>✅ Error     (for errors)</li>
  </ul></li>
  <li>✅ Handles all types of errors</li>
  <li>✅ Request function runs in a seperate thread than GUI so you can do things while your request is being run</li>
  <li>✅ Functionality to edit the variables once they have been added</li>
  <li>❌ All errors can be handled, logged and shown to the user</li>
  <li>❌ Can delete an unwanted item from the list of added variables</li>
  <li>✅ Can reset the entire app to start brand new after a scrape/set of scrapes</li>
  <li>❌ Provides verbose output to user in the GUI</li>
  <li>❌ User can set 'presets', basically if user does a scrape repetitively they can set a preset. User can then just load and run the preset without having to define the variables each time</li>
  <li>❌ Can scrape images</li>
  <li>✅ Can scrape links</li>
  <li>✅ Unique way for generating unique filename for each log AND save data file so that no mixups happen</li>
</ol>
<hr>
<h3>Libraries used to create this:</h3>
<b>Main:</b>
<ul>
  <li>PyQT5 (for the GUI) 💻</li>
  <li>Requests (for the web requests) 📶</li>
  <li>BeautifulSoup4 (for scraping and parsing the HTML) 🍲</li>
  <li>threading (for the seperate threads) 🧵</li>
</ul>
<b>Add ons:</b>
<ul>
  <li>datetime (used in logging and saved data file creation) 📅⌚</li>
  <li>random (used in file creation) ❔</li>
  <li>os (used to get current working directory) ⚡</li>
</ul>
<hr>
<h3>Video Demo:</h3>
<a href="https://www.youtube.com/watch?v=2wB75X7samI">Here</a>
<hr>
<h3>How to use:</h3>
<p>
  <b>STEP 0: Install The App</b><br>
  -Clone this repository on your machine<br>
  -Run the command
  
  ```
    python gui.py
  ```
  inside your terminal to launch the app
  
  <b>STEP 1: Adding URLs</b><br>
  -Add sites to scrape.<br>
  -To do this select the "Set the Site to scrape" button and a enter in the URL of any number of websites you wish to scrape, along with its request method (THIS IS COMPULSORY).<br>
  -Then just click on the "+" button and it is added.<br>
  -Note: URL should have format like 'https://someurl.com; simply click the URL bar at the top of the webpage, Ctrl+C, then Ctrl+V in the textbox.<br>
  -Note 2: add one URL at a time. Dont just enter the entire list into the text-box.<br>
  -Note 3: As of now once you have added something you cannot remove it, you must reset the entire app's data.<br><br><br>
  
  <b>STEP 2: Adding Elements (OPTIONAL)</b><br>
  -Add elements of that site to scrape.<br>
  -This is optional in the sense that if you don't specify any elements the app will scrape the entire webpage.<br>
  -To specify, click the "Set the elements to scrape" button.<br>
  -In here you are presented with 3 text boxes: one for the element name, one for the attribute to specify (OPTIONAL) and one for the attribute value (OPTIONAL).<br>
  -So if you want to scrape a div with class of text-box, in the HTML of the webpage it would look like: div class="text-box". Here, "div" is the element name, "class" is the element attribute, "text-box" is the attribute value.<br>
  -Once you have entered the element, you must then select the URL/site this element belongs to from the URLs you added in the previous step.<br>
  -Finally click on the "+" button and its added. Note: if there are multiple elements with the same properties you specified, the script will scrape all their data. Note 2: it is possible you to only specify the element name, nothing else; this will scrape all the elements of that tag<br>
-Note: In order to obtain the necessary info about an element, you will have to inspect it. Just right click on the element, select 'Inspect' then you will be presented with the HTML of the element. Use the info in the HTML to scrape it<br>
-Note 2: If you have specified an a tag a.k.a a link tag to be scraped, it wont scrape the text it has, rather the link/href value of it. You can override this by going into 'requestExecutor.py' and finding the part where if says 'if x['name'] == 'a' then just comment out the else part, and the a tag's text will be scraped<br>

  <b>STEP 3: Specifying Request Parameters</b><br>
  -Add the web request parameters/payloads to send with your request.<br>
  -Click on "Set Payloads or Headers for scrape".<br>
  -First you select the site with which you want to associate these parameters with.<br>
  -Then you select the type. Currently, only FILE is not worked on, so it will probably throw an unexpected error.<br>
  -The rest work fine. (NOTE: IF YOU DONT WANT TO SEND ANY PARAMETERS YOU MUST SPECIFY SO BY SELECTING THE SITE YOU DONT WANT ANY PARAMETERS FOR AND SELECTING THE "NO PARAMETER" VALUE. LEAVE THE REST EMPTY AND ADD).<br>
  -After you have selected your parameter, specify its contents, then "ADD (+)"<br>
  -Note: If you want to obtain the payload, headers, or any web parameter data, you can do so in the Networking tab of Dev Tools.<br>
  -Note 2: For sending files, more specifically images (currently only images are tested for files), just type the payload name then specify the complete path to the image file.<br><br>

  <b>STEP 4: Starting Scrape</b><br>
  -Once you have everything set, you can start the scrape by clicking on "Start Scraping".<br>
  -Then once you have reviewed all the details, you can select "Yes".<br>
  -Note: If you havent specified any elements to scrape, app will give you a warning. If you forgot to, you can go back and specify them. Else you can just click on "Yes".<br><br>
</p>
<p>As of now, there really isnt a way to give verbose output to the user. So once you start the scrape, just wait for a few seconds and check the scraped data folder in the data folder. Alternatively, if you find nothing there, you can check the logs folder to see if any error had occured.</p>
<h3>Updates:</h3>
<h2>July 3, 2024</h2>
<ul>
  <li>URL editing is implemented, but not request type.</li>
  <li>Images are supported in files payload, since only they have been tested so far</li>
</ul>
<h2>July 4, 2024</h2>
<ul>
  <li>Added functionality to scrape the links of a tags</li>
</ul>
<h2>July 5, 2024</h2>
<ul>
  <li>Fixed some code mess</li>
  <li>Started working on preset adding function</li>
  <li>Finished the preset GUI elements</li>
</ul>
