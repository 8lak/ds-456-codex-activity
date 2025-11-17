# Macalester DS 456 - Projects in Data Science - Codex Activity

*Shilad Sen  (with help from Codex), 2025/11/25*

This activity was developed using a Mac in 11/2025. It may work in the future, or on other platforms, but things change quickly!

# 0. Setup IDE / project

* Fork the repo: https://github.com/shilad/ds-456-codex-activity in GitHub
* Download and install VS Code https://code.visualstudio.com/
* Clone your fork (not the original!) to your computer
* If you are going to use R (not Python) download and install the (VSCode R extension)[https://marketplace.visualstudio.com/items?itemName=reditorsupport.r]


# 1. Create an assignment skeleton

Copy this `README.md` to `Codex_Activity.md`.
Add your name and your partners' name to this assignment.
You will add your answer to the questions marked **Task:** below and commit this activity to GitHub.


# 1. Setup Codex
* Install the (Codex VSCode IDE Extension)[https://developers.openai.com/codex/ide/]
* Click "Use API Key" in the Codex side bar, and use the API key shilad provided to you.
* In the settings for Codex (gear icon in the upper right of the Codex tab), select Codex settings -> Open `config.toml` and set it to this:
    ```toml
    model = "gpt-5.1"
    model_reasoning_effort = "medium"

    [tools]
    web_search_request = true

    [sandbox_workspace_write]
    network_access = true
    ```
* Restart your VSCode

# 2. Early dataset interactions

* Pick a spatial dataset from (Open Data Minneapolis)[https://opendata.minneapolismn.gov]. One fun one is [Motorized Foot & eBike Trips in 2023](https://opendata.minneapolismn.gov/datasets/95547087876344e592dbdfa6244bbc43_0/explore).
* Give codex the URL for the dataset and ask it to help you get started understanding the data. This is purposefully vague!
* **Task:** What do you notice about this early interaction?

# 3. More directed interaction

* If you are partner coding, *switch partners!*
* Download the dataset you would like to analyze and move it into your project directory.
* Ask codex to help you analyze the basic information about the dataset.
* Provide some instructions for improvements to this exploratory analysis.
* **Task:** What did Codex do well, and what would you have done better? Take a look at the code Codex wrote? What code be improved about it?

# 4. Mapping the data.

* If you are partner coding, *switch partners!*
* Ask Codex to help you map the data. Pay attention to what happens at first?
* Try to figure out how to geocode the data. See if codex can figure it out. See if you can figure it out. Don't peek at the answer! Bonus points if you actually get Codex to find the right dataset!
* Download the [Centerline dataset](https://opendata.minneapolismn.gov/datasets/pw-street-centerline/about)
* **Task:** Describe what was easier and harder about doing this with Codex? What would you do differently next time?


# 5. Brainstorming with Codex

* If you are partner coding, *switch partners!*
* Work with codex to identify a research question. 
* Perform one analysis of the research question.
* **Task:** In your RMD, 
* Work with codex to commit & push to your forked repo.





