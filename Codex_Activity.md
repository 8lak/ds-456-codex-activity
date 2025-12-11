Blake Kell

# Macalester DS 456 - Projects in Data Science - Codex Activity

*Shilad Sen (with help from Codex), 2025/11/25*

In this activity you will:

- Use Codex as a collaborator on a real spatial dataset.
- Practice being *critical* of Codex’s suggestions (not just accepting them).
- Compare different prompting styles (one-shot vs. planned) for research questions.

This activity was developed on a Mac in November 2025. It should work on other platforms, but tools change quickly—if something breaks, document it and ask questions!

# 0. Get the project

- Fork the [Codex Activity](https://github.com/shilad/ds-456-codex-activity) on GitHub.
- Clone **your fork** (not the original) to your computer.

# 1. Choose your tools and set up Codex

You may work in **Python (VS Code)** or **R (VS Code or RStudio)**.

## 1.1 Highly Recommended: VS Code + Codex (Python or R)

- Install [VS Code](https://code.visualstudio.com/).
- Install the [Codex VS Code extension](https://developers.openai.com/codex/ide/).
- If you are using R, also install the [VS Code R extension](https://marketplace.visualstudio.com/items?itemName=reditorsupport.r).
- Open your cloned repo folder in VS Code.
- In the Codex sidebar:
  - Click “Use API Key” and use the key Shilad gave you.  
    **DO NOT PUT THIS KEY ANYWHERE IN YOUR GITHUB REPO.**
  - Open Codex settings → “Open `config.toml`” and set it to:
    ```toml
    model = "gpt-5.1"
    model_reasoning_effort = "medium"

    [tools]
    web_search_request = true

    [sandbox_workspace_write]
    network_access = true
    ```
  - Restart VS Code after editing `config.toml`.

## 1.2 Optional: RStudio + Codex in a separate terminal

If you strongly prefer RStudio:

- Use **RStudio** for your R scripts / Rmd files.
- Using a terminal, install the Codex CLI: `npm i -g @openai/codex`
- In a terminal, run `codex` once so it creates a config file at `~/.codex/config.toml`.
- Open `~/.codex/config.toml` in any text editor you like (VS Code, TextEdit, Notepad, `nano`, etc.) and paste the same settings shown in 1.1.
- In a separate terminal window (**from the repo root**), run Codex and use it to:
  - Draft and refactor R code.
  - Ask questions about errors.
- You are still responsible for keeping all code and writeups in this repo so they can be graded.

# 2. Create your assignment skeleton

You will **not** edit this `README.md` directly. Instead:

- Copy `README.md` to `Codex_Activity.md`.
- Add your name(s) at the top of `Codex_Activity.md`.
- For every prompt marked **Task:** below, you will write your answers in `Codex_Activity.md`.
- Your actual analysis code should live in code files, for example:
  - R: `analysis/codex_activity.Rmd` or `analysis/codex_activity.R`
  - Python: `analysis/codex_activity.ipynb` or `analysis/codex_activity.py`

You may reference your code files from `Codex_Activity.md` (e.g., “see Figure 1 in `analysis/codex_activity.Rmd`”).


# 3. Early dataset interactions

- Pick a spatial dataset from [Open Data Minneapolis](https://opendata.minneapolismn.gov).  
  One fun option (used in the instructor example) is  
  [Motorized Foot & eBike Trips in 2023](https://opendata.minneapolismn.gov/datasets/95547087876344e592dbdfa6244bbc43_0/explore).
- Give Codex the URL for the dataset and ask it to help you get started understanding the data.  
  Keep your request intentionally vague (e.g., “Help me explore this dataset”).

**Task 3.1 (in `Codex_Activity.md`):**  
What do you notice about this early interaction? Consider:
- What did Codex assume or gloss over? It didn't state any assumption without a disclaimer attached to it. 
- Did it make any mistakes or questionable choices? For this initial question it didn't make any mistaks or questionable choices it just gave me a response with sections "What is this dataset?","What you can do in the portal’s dataset “Explore” view", "What you (or I) can do to analyze / interpret the data", "What to check / watch out for (common pitfalls)", and "What I can do now, if you want — and what I need from you". It was quite comprehensive from what I understood from the data set the options to explore were consistent as well as with the initial explanation of what the data set was.
- How clear or explainable was the code it produced? It just proposed the library stack to use which was very logical ,Pandas for data manipulation, seaborn for visuals , matplotlib for visuals(could be considered redundant) and folium for interactive maps using geo objects.

# 4. More directed exploration

- If you are partner coding, *switch partners*.
- Download the dataset you would like to analyze and move it under `data/`.
- Ask Codex to help you analyze the **basic information** about the dataset:
  - basic summaries (rows, columns, variable types),
  - simple visualizations,
  - any surprising patterns.
- Then ask Codex for specific improvements (e.g., “Use `dplyr` instead of base R”, “Add labels and titles”, “Handle missing values more carefully”).

**Task 4.1 (in `Codex_Activity.md`):**
- What did Codex do well? It made an initial output of basic information like dimensions, missing values, summary statistics, data types and list of column names. It made lots of different visuals ranging from geographic, a html interactive map, and categorical. It also highlighted patterns like North Loop having the most violations and ward 3 is the most cited which make sense given that ward 3 is that municipal area that covers north loop.
- What would you have done differently if you wrote the code yourself? I probably wouldn't of made the top 10 ordinance violations since the data set is about the snow emergency violations. A similar oversight with a visual for days of week since its all the same day. I would also plot the categorical visuals independently and until I found a combination of variables that were meaninful saved them rather than save all 4 at once without checking their ouput.
- Looking at the code Codex wrote, what could be improved (style, clarity, correctness, efficiency)? Other than the oversights of the data values it also incorrectly tried to set dow names without mapping the values of Day to string form so when renaming that column it has no data. Overall the clarity is very high the style is good, for correctness the only real error was the day mapping. For efficiency I would say its pretty good for the csv based visuals. I'm not sure how geo objects scale with size to properly assess that.

# 5. Mapping the data

- If you are partner coding, *switch partners*.
- Ask Codex to help you map your data. Pay attention to what happens at first:
  - Does it correctly identify what is needed to make a map? 
  - Does it confuse attributes (like IDs) with coordinates? 
- Try to figure out how to geocode / map the data:
  - See if Codex can find the right approach. 
  - See if you can figure it out yourself.
  - Don’t peek at the instructor’s solution scripts unless you are truly stuck.
- For the scooter/e‑bike example, the goal is to join trips to a street or trail network such as the  
  [PW Street Centerline dataset](https://opendata.minneapolismn.gov/datasets/pw-street-centerline/about) and then map trip counts by segment.

**Task 5.1 (in `Codex_Activity.md`):**
- Describe what was easier and harder about doing this with Codex. Finding the sources with which to do the spatial joining is infintely easier with codex. As well as writing out the boiler plate code using the Geopandas methods. 
- Where did Codex help, and where did it get in the way? It didn't really get in the way in fact since it was so easy to produce mismatch visualization I found a discrepenacy between the coordinates and the cited address. In fact some of the original labels and spatially joined results did not coincide with the 2022 city council ward map at all which was interesting. Given that my data set was collected in Feburary, 2022 -> Feb, 2023 and the newest City Council ward was adopte duuntil March, 2022 it is possible that the data collected in feburary and march weren't properly updated. If the ward changes were even drastic enough. But that still doesnt explain the discrepancy between addresses and coordinates. I think it might of been random cases since most other cases are consistent. There is an interesting set of cases at 15 street east between portland ave and pare avenue where according to the city council ward all of those are in ward 6 but several where labeled as 7 despite it not even being on the border. So I did some research and the discrepancies are due to that the snow emergencies used the previous ward bounds where 15 street east is in fact a boundary. So the snow emergencies data set could be considered deprecated or unreliable for analysis. 
- What would you do differently next time you had to map a new dataset with AI assistance? Probably research the underlying data used to create the labels and see if its outdated or not. 

# 6. Identifying a research question with Codex

- If you are partner coding, *switch partners*.
- You will now work with Codex to identify and refine a research question (RQ) about your dataset.

## 6.1 Brainstorm candidate questions

- Seed the brainstorming session with some themes or ideas of research questions that interest you.
- Ask Codex to propose several possible research questions.
- Collaborate with Codex to prioritize the questions along the decision dimensions you think are most appropriate.

**Task 6.1 (in `Codex_Activity.md`):**
- List at least two candidate research questions that Codex suggested. 1. Are snow-emergency violations more frequent in tow zones than in non-tow zones, and do patterns differ across neighborhoods?, Do violations cluster at particular times of day, and does time-of-day vary by ward or tow zone?
- For each, briefly note what seems interesting and what might be problematic (data, scope, ethics, feasibility). both are feasible since the original data set contains all extra information neccesary to observe the RQs. They both seem interesting and potentially could be tied together to a broader question involving more specific patterns that might influence a violation instance. Potentially creating a distribution of violation probabilty based on some grouping for example by neighborhood, time of day, population density or ward.

## 6.2 Refine and choose your question

- Pick one question (it may be a slight modification of a Codex suggestion).
- Ask Codex to critique and refine that question. For example:
  - “Here is my tentative research question: […]. Critique its clarity and feasibility. Propose 1–2 improved versions.”
- Decide on a **final RQ** you will try to answer. This choice is yours, not Codex’s.

**Task 6.2 (in `Codex_Activity.md`):**
- Write down your final research question in one clear sentence. "How are snow‑emergency parking violations distributed by time of day during Feb 24–25, 2023?"
- In 2–3 sentences, explain why you chose it (and why you rejected other candidates). I think its interesting since it can give an insight into patterns of the people who write the citations potentially allowing for people to be in violation but not actually get cited by knowing when the citers actually come. As well as maybe improving the citers schedule to be more active and reduce non-cited violations at other times of day. The other RQ about tows was discarded since these data set only includes violations in tow-zones.

# 7. Answering your question with Codex: one-shot vs. plan-first

- You will now use Codex to help answer your chosen research question in two different ways.

## 7.1 One-shot interaction

- In your R or Python environment, ask Codex for a **one-shot** solution to your chosen RQ. For example:
  - “Here is my research question: […]. Write code to answer it in one shot.”
- Run the code (after checking it!) and see what happens:
  - Does the analysis actually answer your question?
  - Does the code run?
  - Are the results interpretable and relevant?

**Task 7.1 (in `Codex_Activity.md`):**
- Briefly describe what analysis Codex performed and what results you obtained.
- What was good or bad about this one-shot attempt (data used, methods, code quality, clarity)?
**Task 7.1 (in `Codex_Activity.md`):**
Codex's one-shot script loaded the CSV, parsed the `Time` field into hours, aggregated counts by hour and by ward, and saved a CSV plus two plots (hourly histogram and ward-by-hour chart). The outputs show clear clusters of violations in specific hours during Feb 24–25, 2023 and different hourly profiles across wards. The main strength was speed: the one-shot produced usable artifacts quickly for exploration. The main weaknesses were brittle time parsing, no provenance or parsing diagnostics, and no normalization or statistical testing. Overall, one-shot is useful for quick descriptive checks but insufficient for a defensible final analysis.

## 7.2 Plan-first interaction

- Now ask Codex to **plan first, then code** for the *same* research question. For example:
  - “Here is my research question: […]. Help me design a 3–5 step plan to answer it. Don’t write any code yet.”
- Review the plan and edit it so it feels realistic and meaningful to you.
- Then, *step by step*, ask Codex to write code for each step:
  - “Now write code for step 1 only…”
  - Run and debug it.
  - “Now write code for step 2…”
- You may do this in `analysis/codex_activity.Rmd`, `.R`, `.py`, or a notebook.

**Task 7.2 (in `Codex_Activity.md`):**
- Briefly describe the main steps in your final plan and what you implemented for each.
- How did the planned interaction differ from the one-shot attempt?
- Which approach produced better code, and which felt more controllable?
**Task 7.2 (in `Codex_Activity.md`):**
My final plan had five steps: load & validate the CSV (preserving `ward_original`), parse and normalize `Time` into `hour`, aggregate hourly counts and save a CSV, visualize with clear captions, and run interpretation plus diagnostics (including ward mismatch checks). I implemented these steps incrementally in `codex_analysis.py`, and the stepwise approach caught parsing edge cases and produced diagnostics like `data/ward_mismatches.csv`. Compared with the one-shot, plan-first required explicit checks and intermediate outputs rather than returning only end results. The plan-first workflow yielded cleaner, more maintainable code and reproducible artifacts. It also felt more controllable for debugging and for building a defensible writeup.

## 7.3 Final reflection

**Task 7.3 (in `Codex_Activity.md`):**
- When would you choose one-shot prompting vs. plan-first prompting for future projects?
- What norms or habits do you want to adopt for working with tools like Codex in your own data science work?
**Task 7.3 (in `Codex_Activity.md`):**
Use one-shot prompting for quick exploration and prototyping when you want immediate visuals or to check basic assumptions. Use plan-first for reproducible or high-stakes analyses that need validation, provenance tracking, and intermediate diagnostics. Adopt these habits: preserve provenance columns, log parsing/validation issues to CSV, break work into small tested steps, and record dependencies in `requirements.txt`. Always document assumptions and limitations (for example, the ward vintage mismatch) in `Codex_Activity.md`. Combining both workflows—one-shot to explore, plan-first to harden—worked best for this project.

# 8. What to hand in

By the end of the activity, your repo should include at least:

- `Codex_Activity.md` with answers to all **Task** prompts (3.1, 4.1, 5.1, 6.1, 6.2, 7.1, 7.2, 7.3).
- At least one analysis file:
  - R: `analysis/codex_activity.Rmd` or `analysis/codex_activity.R`
  - Python: `analysis/codex_activity.ipynb` or `analysis/codex_activity.py`
- Any additional scripts or notebooks you used, committed in a reasonable state.

Before you’re done:

- Use Codex to help you **commit and push** your work to your forked repo.
- Make sure that your API key is **not** anywhere in the repo.
- Share the URL for the repo (including the markdown and script) on the Moodle activity.
