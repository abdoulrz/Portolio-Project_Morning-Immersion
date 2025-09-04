# Portfolio Project: Morning Immersion

A 30-min reading habit that will nourish your intellect and life with Culture, Nature, Tech, and Business.


## Overview

Welcome to the Morning Immersion, a great newsletter recommendation system! This is a command-line application designed for curious, lifelong learners and avid readers who want to discover their next favorite newsletter. Whether you're looking to gain new insights or stay in touch with the world around you, this tool helps you find curated recommendations tailored to your interests.

_The system is built to be simple, interactive, and easy to use, running entirely within your terminal._

## Features

-   **Browse by Topic**: Explore a wide range of topics, including **Culture**, **Nature**, **Tech**, and **Business**.
    
-   **Drill Down into Subcategories**: Each main topic is broken down into four distinct subcategories, allowing you to fine-tune your search for the perfect content.
    
-   **General Recommendations**: Not sure where to start? Use the "General" option to get a random selection of top newsletters from all categories.
    
-   **Detailed Information**: Each recommendation comes with:
    
    -   **Title**: The name of the newsletter.
        
    -   **Description**: A concise, one-line summary of what to expect.
        
    -   **Rating**: A quality score from 1 to 5 stars.
        
    -   **Authority**: A score from 1 to 10 indicating the source's credibility and influence.
        
-   **Interactive & User-Friendly**: A simple, text-based interface guides you through the selection process.
    
-   **Continuous Exploration**: After receiving recommendations, you can easily choose to explore other topics without restarting the program.
    

## How It Works

The program guides you through a simple, step-by-step process to find newsletters you'll love.

1.  **Welcome**: When you launch the application, you're greeted with a welcome message.
    
2.  **Select a Topic**: You'll be prompted to choose a main topic by typing its first letter:
    
    -   `C` for **Culture**
        
    -   `N` for **Nature**
        
    -   `T` for **Tech**
        
    -   `B` for **Business**
        
    -   Or, type `G` to get **General** recommendations from all topics.
        
3.  **Refine Your Choice**: If you select a specific topic, a second prompt will appear, allowing you to choose a subcategory (again, by typing its first letter) or typing `G` to get recommendations from the entire main topic.
    
4.  **Get Recommendations**: Once you've made your final selection, the system will display a list of five curated newsletter recommendations, complete with their titles, descriptions, ratings, and authority scores.
    
5.  **Explore More**: After you've reviewed your list, you'll be asked if you want to search again.
    
    -   Typing `Y` (Yes) will restart the process from the topic selection.
        
    -   Typing `N` (No) will end the program with a friendly "Enjoy your reading!" message.
        

## File Structure

The project consists of two main Python files:

-   `main.py`: This file contains the core logic of the application. It handles user input, processes choices, and displays the final recommendations.
    
-   `newsletter_data.py`: This file acts as the database. It stores all the newsletter information in a well-structured Python dictionary, making it easy to view, manage, and expand the collection of recommendations.
    

## How to Run the Program

1.  **Prerequisites**: Ensure you have Python installed on your system.
    
2.  **Download Files**: Save both `main.py` and `newsletter_data.py` in the same directory.
    
3.  **Open Terminal**: Navigate to the directory where you saved the files using your command line or terminal.
    
4.  **Execute**: Run the program with the following command:
    
    ```
    python main.py
    ```
    
5.  **Follow the Prompts**: The application will start, and you can begin exploring Morning Immersion immediately!