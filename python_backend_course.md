**PYTHON BACKEND DEVELOPER**
COURSE CURRICULUM

100 Hours • Zero to Deployment
Designed for Brazilian Public School Students








Version 1.0 • 2025

# **Course Overview**
This 100-hour course takes students with zero programming experience to deploying a working web application. Every lesson is designed with concrete, visible outcomes so students always know exactly what they built and why it matters.

## **Pedagogical Principles**
**1. Concrete before abstract: **Students see results on screen before learning theory. We type code, see output, then explain why.
**2. Spiral learning: **Core concepts (variables, functions, data) appear first simply, then revisit with depth. Nothing is taught once and forgotten.
**3. Real-world anchoring: **Every exercise connects to something students already know: social media, games, messaging, shopping.
**4. Low floor, high ceiling: **Every lesson has a baseline everyone can reach, plus stretch challenges for faster students. Nobody waits, nobody drowns.
**5. Minimal math dependency: **We avoid algebra-heavy examples. Logic and problem-solving are taught through everyday scenarios, not formulas.
**6. Portuguese-friendly resources: **All variable names, comments, and examples should use Portuguese where it aids comprehension. English terms are introduced gradually as industry vocabulary.

## **Course Structure at a Glance**

Total: 100 hours. Modules 1–6 build progressively. Module 7 is the capstone. Module 8 is flexible and can be distributed throughout or used as buffer time.

# **Module 1: Getting Started — Your First Code (12h)**
Goal: Students go from never having written code to building a working interactive program. Every lesson produces something they can show to a friend or family member.




**Lesson 1.1 — What is Programming? Setup (2h)**
**Hook: **Show a finished chatbot or game running in the terminal. Tell students: “In 12 hours, you will build something like this.”
**Core content: **What is a program? (a recipe for the computer). Install Python. Open the terminal. Type python3. Type print(“Olá, mundo!”). Celebrate.
**Exercise: **Make the computer print your name, your school’s name, and a joke. Experiment with what happens when you remove the quotes.
**Outcome: **Every student has Python running and has seen code produce output.

**Lesson 1.2 — Variables & print() (2h)**
**Analogy: **Variables are labeled boxes. Show a physical box with a label. Put something in it. Change what’s inside. The label stays.
**Core content: **nome = “Maria”, idade = 17, print(f“Olá, {nome}! Você tem {idade} anos.”). String vs number (you can’t add a name to a number).
**Exercise: **Create a program that asks for your name and age, then prints a personalized greeting with how old you will be in 10 years.

**Lesson 1.3 — Input & Simple Decisions (2h)**
**Analogy: **Your brain makes if/else decisions all day: “If it’s raining, take umbrella, else wear sunglasses.” Code does the same thing.
**Core content: **input() to get user data. if/elif/else. Comparison operators (==, >, <). Convert text to number with int().
**Exercise: **Build an age checker: input your age, program tells you if you can vote (16+), drive (18+), or run for president (35+).

**Lesson 1.4 — Repeated Actions: Loops (2h)**
**Analogy: **When you send the same message to 10 friends, you don’t write it 10 times. Loops let the computer repeat things.
**Core content: **for loop with range(). while loop for “keep going until...”. Using loops with variables (counters, accumulators).
**Exercise: **Multiplication table generator: user picks a number, program prints the full table. Then: countdown timer from 10 to 0 with “Liftoff!”

**Lesson 1.5 — Lists & Everyday Collections (2h)**
**Analogy: **A playlist is a list of songs. You can add songs, remove songs, shuffle, and count them.
**Core content: **Creating lists. append(), remove(), len(). Looping through lists. Indexing (the first item is [0]).
**Exercise: **Shopping list manager: user can add items, remove items, view the list, and see how many items are on it.

**Lesson 1.6 — Mini-Project: Interactive Quiz (2h)**
**Structure: **Students build a quiz with 5+ questions on a topic they like (sports, music, movies). Program tracks score and shows result at the end.
**Minimum: **5 questions with if/else checking, final score display.
**Stretch: **Randomize question order, add timer, categorize questions by difficulty.


# **Module 2: Organizing Code & Data (12h)**
Goal: Students learn to write reusable code with functions, work with dictionaries, read/write files, and handle errors gracefully. By the end, they have a contact book application that saves data permanently.




**Lesson 2.1 — Functions: Reusable Recipes (2h)**
**Analogy: **A recipe tells you how to make a cake. You don’t rewrite the recipe every time—you just follow it again. Functions are recipes for the computer.
**Core content: **def keyword. Parameters as ingredients. return as the final dish. Functions calling other functions.
**Exercise: **Build a calculator: separate functions for add, subtract, multiply, divide. A menu asks which operation, gets two numbers, calls the right function.

**Lesson 2.2 — Dictionaries: Labeled Data (2h)**
**Analogy: **A dictionary is like a contact card: each piece of info has a label (name, phone, email).
**Core content: **Creating dicts. Accessing by key. Adding/updating values. Looping through .items(). Lists of dicts for collections.
**Exercise: **Student profile generator: input name, age, favorite subject, hobby. Store as dict. Print a formatted profile card.

**Lesson 2.3 — Reading & Writing Files (2h)**
**Why it matters: **Until now, everything disappears when the program closes. Files let your program remember things.
**Core content: **open() with “r”, “w”, “a” modes. Reading lines. Writing text. Introduction to JSON for structured data (json.dump, json.load).
**Exercise: **To-do list that saves to a JSON file. When you restart the program, your tasks are still there.

**Lesson 2.4 — Error Handling (2h)**
**Motivation: **Show what happens when a user types “abc” when the program expects a number. The program crashes. That’s embarrassing. Let’s fix it.
**Core content: **try/except blocks. Catching specific errors (ValueError, FileNotFoundError). Creating a safe input function that keeps asking until valid.
**Exercise: **Wrap the calculator from 2.1 in try/except. Make it impossible to crash no matter what the user types.

**Lesson 2.5 — Modules & Imports (2h)**
**Core content: **Breaking code into files. import and from...import. Using the standard library (random, datetime). Installing packages with pip.
**Exercise: **Reorganize the contact book: one file for data handling, one for display, one for the main menu. See how much cleaner it looks.

**Lesson 2.6 — Mini-Project: Contact Book (2h)**
**Requirements: **Add contact (name, phone, email), search by name, list all contacts, delete a contact, save/load from JSON file, handle errors gracefully.
**Stretch: **Add edit functionality, search by partial name, group contacts by category.


# **Module 3: Your First Web Pages (12h)**
Goal: Students understand how the web works and can build attractive web pages. This is the bridge between Python console programs and the web. By the end, each student has a personal portfolio page.




**Key Concepts Covered**
**HTML: **Semantic tags (header, main, footer, nav, section, article), headings, paragraphs, links, images, lists, tables, forms.
**CSS: **Selectors, colors, fonts, box model (margin, padding, border), flexbox for layout, basic responsive design with media queries.
**Deployment: **Introduction to GitHub Pages as free hosting. Students will have a live URL they can share.


# **Module 4: Backend with Flask (14h)**
Goal: Students connect Python to the web. They learn that the beautiful pages from Module 3 can be powered by Python code that makes decisions and generates content dynamically. By the end, they have a working multi-page web application.




**Lesson 4.1 — Hello Flask (2h)**
**The magic moment: **Students type 5 lines of code, run the file, open a browser, and see their page. This is the most important moment in the course—when console Python becomes a website.
**Core content: **pip install flask. from flask import Flask. app = Flask(__name__). @app.route(“/”). def home(): return “Hello!”. app.run(debug=True). What localhost means. What port 5000 means.
**Exercise: **Create routes for /about and /contact that return different HTML strings. Celebrate when students visit each page in the browser.

**Lesson 4.3 — Templates with Jinja2 (2h)**
**Motivation: **Writing HTML inside Python strings is painful. Templates let you write normal HTML files that Python fills in with data.
**Core content: **render_template(). {{ variable }} syntax. {% if %} and {% for %} in templates. Passing data from Python to HTML.
**Exercise: **Create a page that greets the user by name (from URL or form) and shows a different background color based on time of day.


# **Module 5: Databases & Persistence (14h)**
Goal: Students learn to store, retrieve, update, and delete data permanently. The blog/app starts taking real shape here, with posts stored in a database instead of disappearing when the server restarts.




**Lesson 5.1 — What is a Database? (2h)**
**Analogy: **A database is a super-organized spreadsheet. Each table is a sheet. Each row is an entry. Each column is a field. But unlike a spreadsheet, it can hold millions of rows and find things instantly.
**Core content: **What SQLite is (a database in a single file). Creating a database. Tables, rows, columns. Using Flask-SQLAlchemy to define a model. db.create_all(). Adding data in the Python shell.
**Exercise: **Create a “students” table with name, age, course. Add 5 students. Query them back.

**Lesson 5.2 — Models as Python Classes (2h)**
**Key insight: **Each model is a Python class. Each column is a class attribute. Each row is an object. Students already know classes from their contact book dicts—this is the same idea, but the database remembers everything.
**Core content: **db.Model. db.Column types (String, Integer, Text, DateTime). Primary keys. Default values. The migration concept (creating/updating tables).
**Exercise: **Create a Post model with id, title, content, created_at. Add posts through the Flask shell. Query and display them.

**Lesson 5.5 — Relationships Between Data (2h)**
**Analogy: **On Instagram, each post belongs to one user, but each user has many posts. That’s a relationship. In a blog, each post can have many comments, and each comment belongs to one post.
**Core content: **db.relationship(). db.ForeignKey(). One-to-many pattern. Accessing related objects (post.comments, comment.post).
**Exercise: **Add a Category model. Each post belongs to one category. Create a page that shows posts filtered by category.


# **Module 6: Users & Authentication (10h)**
Goal: Students add user accounts to their application. Users can register, log in, log out, and own their content. This transforms the blog from a single-author site into a multi-user platform.





# **Module 7: Final Project — Build & Deploy (18h)**
Goal: This is the capstone. Students bring everything together into a polished application and deploy it to the internet. By the end, they have a live URL they can share with anyone in the world.



**Lesson 7.2 — Upgrading to PostgreSQL (2h)**
**Why: **SQLite is great for learning, but real web apps use PostgreSQL. The good news: with SQLAlchemy, switching is mostly changing one line of configuration.
**Core content: **Installing PostgreSQL. Creating a database. Changing DATABASE_URL in Flask config. Running migrations. Testing that everything still works.

**Lesson 7.4 — Git Basics (2h)**
**Analogy: **Git is like the “undo history” in a document, but much more powerful. You can go back to any previous version of your entire project.
**Core content: **git init, add, commit, status, log. What .gitignore is for. Pushing to GitHub. Students should commit after every significant change during project work.

**Lesson 7.5 — Deployment (3h)**
**Platform: **Render.com (free tier) or Railway.app. Both support Python/Flask + PostgreSQL and are simpler than Heroku.
**Steps: **Connect GitHub repo, set environment variables, configure build command (pip install), set start command (gunicorn app:app). Wait for deploy. Visit URL. Celebrate.
**Troubleshooting: **Common issues: missing requirements.txt, wrong start command, database not configured. Walk through each error message together.

**Suggested Final Project Options**
**Blog Platform: **Posts, comments, categories, user profiles, search. The default path, well-supported by all lessons.
**Task Manager: **To-do lists with priorities, due dates, categories, completion tracking. Good for students who prefer utility apps.
**Recipe Book: **Share recipes with ingredients, steps, photos (as URLs), and ratings. Great for students who love cooking.
**Event Board: **Community events with dates, locations, RSVPs. Good for students interested in community building.



# **Module 8: Bonus & Career Prep (8h)**
Goal: Prepare students for what comes next. This module is flexible—use it as buffer time if earlier modules run long, or as enrichment for groups that are on track. Topics can be taught in any order based on student interest.




# **Assessment Strategy**
Traditional exams are not the right tool for this course. Assessment should be continuous, project-based, and encouraging.

## **Continuous Assessment (60%)**
**Mini-projects (Modules 1–6): **Each module ends with a mini-project. These are graded on: Does it work? Is the code organized? Did the student handle edge cases? Rubric should be shared before students start.
**Participation & progress: **Completing exercises, asking questions, helping classmates. This rewards effort, not just talent.

## **Final Project (40%)**
Graded on the following criteria:
**Functionality (15%): **Does the app work? Can users register, log in, create content, and navigate the site?
**Code quality (10%): **Is the code organized? Are there functions, clear names, error handling?
**Design & usability (5%): **Does the site look decent? Is it easy to use?
**Deployment (5%): **Is it live on the internet? Does the deployment work?
**Presentation (5%): **Can the student explain what they built, how it works, and what they learned?


# **Recommended Tools & Resources**

## **Software Stack**
**Language: **Python 3.10+
**Editor: **VS Code (free, works on all platforms, great extensions)
**Framework: **Flask (simple, well-documented, perfect for learning)
**ORM: **Flask-SQLAlchemy
**Database (dev): **SQLite (zero setup)
**Database (prod): **PostgreSQL
**Authentication: **Flask-Login + Werkzeug password hashing
**Deployment: **Render.com or Railway.app (free tiers available)
**Version Control: **Git + GitHub

## **Key Python Packages**
**flask: **Web framework
**flask-sqlalchemy: **Database ORM
**flask-login: **User session management
**flask-wtf: **Form handling and validation
**python-dotenv: **Environment variable management
**gunicorn: **Production WSGI server for deployment
**psycopg2-binary: **PostgreSQL adapter for Python

## **Free Learning Resources (Portuguese-Friendly)**
**Python Documentation: **docs.python.org (has Portuguese translation)
**Flask Documentation: **flask.palletsprojects.com
**Curso em Vídeo: **YouTube channel with Python course in Portuguese
**W3Schools: **Simple HTML/CSS/Python references
**MDN Web Docs: **Comprehensive web development reference


# **Instructor Guide: Tips for Success**

## **Class Structure (Recommended 2h Sessions)**
**First 10 minutes: **Show the finished product. Let students see what they will build today. Build excitement and set the goal.
**Next 20 minutes: **Live coding demonstration. Type the code while explaining. Make deliberate mistakes and fix them—this normalizes errors.
**Next 60 minutes: **Hands-on practice. Students work on exercises. Walk around, help individuals. Encourage pair programming.
**Last 30 minutes: **Review, Q&A, preview of next lesson. Ask students to share what they built.

## **Handling Different Skill Levels**
**Fast students: **Direct them to the “Extra Challenges” boxes. Let them help slower classmates (teaching reinforces learning). Consider giving them a “teaching assistant” role.
**Struggling students: **Pair them with a slightly faster student. Provide starter code with blanks to fill in rather than starting from zero. Focus on getting one thing working, then building from there.
**Students with no computer at home: **All exercises should be completable in class. Provide a USB stick with Python + VS Code portable. Consider setting up a cloud-based editor (Replit) as backup.

## **Common Pitfalls to Avoid**
**Don’t lecture for more than 20 minutes: **Students learn by doing, not watching.
**Don’t skip the celebration: **When a student’s first server runs, when they see their page live—these are magical moments. Stop and acknowledge them.
**Don’t grade on code style too early: **Working > pretty for the first 60 hours. Introduce code quality expectations gradually.
**Don’t fear errors: **When something breaks in the demo, it’s a teaching opportunity. Walk through reading the error message. “Error messages are the computer trying to help you.”
**Don’t compare students to each other: **Compare each student to their past self. “Last week you didn’t know what a variable was. Now look at this program you built.”


| Prerequisites | None (absolute beginners) |
| --- | --- |
| Duration | 100 hours total |
| Final Project | Deploy a working blog/app |
| Database | SQLite → PostgreSQL |
| Philosophy | Low floor, high ceiling |


| Module | Title | Hours | Key Deliverable |
| --- | --- | --- | --- |
| 1 | Getting Started: Your First Code | 12 | Interactive quiz program |
| 2 | Organizing Code & Data | 12 | Contact book application |
| 3 | Your First Web Pages | 12 | Personal portfolio site |
| 4 | Backend with Flask | 14 | Working web app with routes |
| 5 | Databases & Persistence | 14 | Blog with database storage |
| 6 | Users & Authentication | 10 | Login/register system |
| 7 | Final Project: Build & Deploy | 18 | Deployed blog/app online |
| 8 | Bonus & Career Prep | 8 | Portfolio + resume |


| Teaching Note: Start every class by showing the finished result of what they will build. Let them get excited before writing a single line of code. |
| --- |


| MODULE 1: GETTING STARTED  (12h) | MODULE 1: GETTING STARTED  (12h) | MODULE 1: GETTING STARTED  (12h) | MODULE 1: GETTING STARTED  (12h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 1.1 | What is programming? Setup | Install Python, run "Hello World" in terminal | 2 |
| 1.2 | Variables & print() | Program that introduces itself with user’s name | 2 |
| 1.3 | Input & simple decisions (if/else) | Age checker: can you vote? can you drive? | 2 |
| 1.4 | Repeated actions (for/while loops) | Multiplication table generator for any number | 2 |
| 1.5 | Lists & everyday collections | Shopping list app (add, remove, show items) | 2 |
| 1.6 | Mini-project: Interactive Quiz | Quiz game with score tracking | 2 |


| Extra Challenges for Engaged Students
⭐ Add difficulty levels to the quiz (easy/medium/hard)
⭐ Create a number guessing game with hints (higher/lower)
⭐ Build a simple text-based adventure with multiple paths |
| --- |


| Teaching Note: This module introduces abstraction gently. Always show the messy version first (repeated code), then show how functions clean it up. Let students feel the pain of repetition before offering the cure. |
| --- |


| MODULE 2: ORGANIZING CODE & DATA  (12h) | MODULE 2: ORGANIZING CODE & DATA  (12h) | MODULE 2: ORGANIZING CODE & DATA  (12h) | MODULE 2: ORGANIZING CODE & DATA  (12h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 2.1 | Functions: reusable recipes | Calculator with functions for each operation | 2 |
| 2.2 | Dictionaries: labeled data | Student profile card generator | 2 |
| 2.3 | Reading & writing files | Program that saves/loads a to-do list from disk | 2 |
| 2.4 | Error handling (try/except) | Bulletproof input that never crashes | 2 |
| 2.5 | Combining it all: modules & imports | Organized multi-file project | 2 |
| 2.6 | Mini-project: Contact Book | Add, search, delete, save contacts to file | 2 |


| Extra Challenges for Engaged Students
⭐ Add search-by-partial-name to the contact book
⭐ Export contacts to a CSV file that opens in Excel
⭐ Create a simple expense tracker that calculates totals by category |
| --- |


| Teaching Note: This module temporarily steps away from Python to build web literacy. Students need to understand HTML/CSS before we introduce Flask. Keep it visual and hands-on—every change should be visible in the browser immediately. |
| --- |


| MODULE 3: YOUR FIRST WEB PAGES  (12h) | MODULE 3: YOUR FIRST WEB PAGES  (12h) | MODULE 3: YOUR FIRST WEB PAGES  (12h) | MODULE 3: YOUR FIRST WEB PAGES  (12h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 3.1 | How the web works | Draw the journey of a web request | 1 |
| 3.2 | HTML: the skeleton of a page | Personal bio page with headings, links, images | 2 |
| 3.3 | CSS: making it beautiful | Styled bio page with colors, fonts, layout | 3 |
| 3.4 | Responsive design basics | Page that looks good on phone and desktop | 2 |
| 3.5 | Forms: collecting user input | Contact form with validation | 2 |
| 3.6 | Mini-project: Portfolio Page | Complete personal portfolio deployed on GitHub Pages | 2 |


| Extra Challenges for Engaged Students
⭐ Add CSS animations or transitions to the portfolio
⭐ Create a dark mode toggle with CSS variables
⭐ Build a second page (hobby page or photo gallery) and link between them |
| --- |


| Teaching Note: Flask is chosen for its simplicity. A “Hello World” server is literally 5 lines of code. Always start each lesson with the simplest possible working example, then build complexity. |
| --- |


| MODULE 4: BACKEND WITH FLASK  (14h) | MODULE 4: BACKEND WITH FLASK  (14h) | MODULE 4: BACKEND WITH FLASK  (14h) | MODULE 4: BACKEND WITH FLASK  (14h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 4.1 | Your first server: Hello Flask | Running web server showing a page at localhost | 2 |
| 4.2 | Routes & dynamic pages | Multi-page site with navigation | 2 |
| 4.3 | Templates with Jinja2 | HTML pages powered by Python variables | 2 |
| 4.4 | Template inheritance & layouts | Consistent look across all pages (base template) | 2 |
| 4.5 | Forms & POST requests | Page that receives and processes form data | 2 |
| 4.6 | Static files & project structure | Organized Flask project with CSS, images, templates | 2 |
| 4.7 | Mini-project: Web App v1 | Multi-page app with forms, templates, navigation | 2 |


| Extra Challenges for Engaged Students
⭐ Add flash messages for user feedback (success/error notifications)
⭐ Create an API endpoint that returns JSON data
⭐ Build a page that shows the current weather using a free API |
| --- |


| Teaching Note: Start with SQLite (zero setup, just a file) and introduce PostgreSQL later. Use Flask-SQLAlchemy so students write Python instead of raw SQL—they can learn SQL concepts through the ORM without getting lost in syntax. |
| --- |


| MODULE 5: DATABASES & PERSISTENCE  (14h) | MODULE 5: DATABASES & PERSISTENCE  (14h) | MODULE 5: DATABASES & PERSISTENCE  (14h) | MODULE 5: DATABASES & PERSISTENCE  (14h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 5.1 | What is a database? SQLite intro | Create a database and add data via Python shell | 2 |
| 5.2 | Flask-SQLAlchemy: models as classes | Post model with title, content, date | 2 |
| 5.3 | CRUD: Create & Read | Page to create posts and list all posts | 2 |
| 5.4 | CRUD: Update & Delete | Edit and delete posts through the browser | 2 |
| 5.5 | Relationships between data | Posts with categories/tags | 2 |
| 5.6 | Search & pagination | Search posts by keyword, paginated results | 2 |
| 5.7 | Mini-project: Blog with database | Full blog: create, read, edit, delete, search posts | 2 |


| Extra Challenges for Engaged Students
⭐ Add a comments system (new model with relationship to posts)
⭐ Create an admin dashboard showing post statistics
⭐ Export all posts to a downloadable JSON or CSV file |
| --- |


| Teaching Note: Security is introduced gently. Focus on using Flask-Login properly rather than building authentication from scratch. Emphasize never storing plain-text passwords. |
| --- |


| MODULE 6: USERS & AUTHENTICATION  (10h) | MODULE 6: USERS & AUTHENTICATION  (10h) | MODULE 6: USERS & AUTHENTICATION  (10h) | MODULE 6: USERS & AUTHENTICATION  (10h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 6.1 | User model & password hashing | User table with secure password storage | 2 |
| 6.2 | Registration & login forms | Working signup and login pages | 2 |
| 6.3 | Sessions & Flask-Login | Users stay logged in, see their name in the header | 2 |
| 6.4 | Authorization: who can do what? | Only post authors can edit/delete their posts | 2 |
| 6.5 | User profiles & settings | Profile page with editable bio and avatar URL | 2 |


| Extra Challenges for Engaged Students
⭐ Add “forgot password” flow with email simulation
⭐ Implement admin role with special permissions
⭐ Add social features: follow users, see a feed of followed users’ posts |
| --- |


| Teaching Note: This module is half guided, half independent. The first 8 hours provide structure and fill gaps (PostgreSQL, deployment). The remaining 10 hours are project work time with instructor support. Let students choose their focus: some will want a beautiful blog, others a to-do app, others something creative. |
| --- |


| MODULE 7: FINAL PROJECT: BUILD & DEPLOY  (18h) | MODULE 7: FINAL PROJECT: BUILD & DEPLOY  (18h) | MODULE 7: FINAL PROJECT: BUILD & DEPLOY  (18h) | MODULE 7: FINAL PROJECT: BUILD & DEPLOY  (18h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 7.1 | Project planning & wireframing | Written plan with features, pages, and models defined | 2 |
| 7.2 | Upgrading to PostgreSQL | App running on PostgreSQL instead of SQLite | 2 |
| 7.3 | Environment variables & config | App reads secrets from .env, not hardcoded | 1 |
| 7.4 | Git basics & version control | Project in a Git repository with meaningful commits | 2 |
| 7.5 | Deployment to Render/Railway | App live on the internet with a public URL | 3 |
| 7.6 | Project work sessions | Independent building with instructor guidance | 6 |
| 7.7 | Final polish & presentation | Polished app, presented to peers | 2 |


| Extra Challenges for Engaged Students
⭐ Add a REST API to your app (JSON endpoints for external access)
⭐ Implement image uploads using Cloudinary or similar service
⭐ Add real-time notifications using Flask-SocketIO
⭐ Create an admin panel with usage statistics and charts |
| --- |


| MODULE 8: BONUS & CAREER PREP  (8h) | MODULE 8: BONUS & CAREER PREP  (8h) | MODULE 8: BONUS & CAREER PREP  (8h) | MODULE 8: BONUS & CAREER PREP  (8h) |
| --- | --- | --- | --- |
| Lesson | Topic | Outcome | Hours |
| 8.1 | Introduction to APIs & consuming data | App that shows live data from a public API | 2 |
| 8.2 | Testing your code | Write tests that verify your app works correctly | 2 |
| 8.3 | Developer portfolio & GitHub profile | Professional GitHub profile with pinned projects | 2 |
| 8.4 | Next steps & career paths | Roadmap for continued learning, mock interview prep | 2 |


| Extra Challenges for Engaged Students
⭐ Contribute to an open-source project on GitHub
⭐ Build a CLI tool and publish it on PyPI
⭐ Start learning Django and compare it to Flask
⭐ Explore Docker containers for deployment |
| --- |


| Teaching Note: Be generous with partial credit. A student who has a working but ugly site has learned more than a student who has nothing deployed. Celebrate progress, not perfection. |
| --- |


| Teaching Note: The single most important thing: Every student should leave every class having made something work. Even if it’s small, even if they needed help. The feeling of “I made the computer do something” is what keeps them coming back. |
| --- |
