import random
from newsletter_data import newsletter_data

def print_welcome_message():
    """Prints a welcome message to the user."""
    print("*" * 60)
    print("*" * 10 + " " * 8 + "Welcome to the Reading Immersion" + " " * 8 + "*" * 10)
    print("*" * 10 + " " * 8 + "A Newsletter Recommendation System!" + " " * 7 + "*" * 10)
    print("*" * 60)
    print()

def get_user_choice(options):
    """
    Prompts the user to make a choice from a list of options.

    Args:
        options (dict): A dictionary of options, where the keys are the letters
                        to be typed and the values are the descriptions.

    Returns:
        str: The user's valid choice (an uppercase letter).
    """
    while True:
        for key, value in options.items():
            print(f"Type '{key}' for {value}")
        choice = input("> ").upper()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

def print_recommendations(recommendations):
    """
    Prints a formatted list of newsletter recommendations.

    Args:
        recommendations (list): A list of recommendation dictionaries.
    """
    print("\nHere are your recommendations:\n")
    for rec in recommendations:
        print(f"Title: {rec['title']}")
        print(f"  Description: {rec['description']}")
        print(f"  Rating: {'*' * rec['rating']}{' ' * (5 - rec['rating'])} ({rec['rating']}/5)")
        print(f"  Authority: {'=' * rec['authority']}{' ' * (10 - rec['authority'])} ({rec['authority']}/10)")
        print("-" * 40)


def main():
    """The main function to run the newsletter recommendation system."""
    print_welcome_message()

    while True:
        # Get main topic choice
        main_topics = {
            'C': 'Culture',
            'N': 'Nature',
            'T': 'Tech',
            'B': 'Business',
            'G': 'General (All Topics)'
        }
        print("Which topic would you like to explore?")
        topic_choice_key = get_user_choice(main_topics)
        
        recommendations = []

        if topic_choice_key == 'G':
            # Get 5 random recommendations from all subcategories
            all_recs = [rec for topic in newsletter_data.values() for subcat in topic.values() for rec in subcat]
            recommendations = random.sample(all_recs, 5)
        else:
            topic_name = main_topics[topic_choice_key]
            subcategories = newsletter_data[topic_name]

            # Get subcategory choice
            sub_options = {'G': f"General ({topic_name})"}
            sub_options.update({sub[0].upper(): sub for sub in subcategories.keys()})
            
            print(f"\nDo you want to go deeper into {topic_name}?")
            sub_choice_key = get_user_choice(sub_options)

            if sub_choice_key == 'G':
                 # Get 5 random recommendations from all subcategories of the chosen topic
                all_topic_recs = [rec for subcat in subcategories.values() for rec in subcat]
                recommendations = random.sample(all_topic_recs, 5)
            else:
                sub_name = sub_options[sub_choice_key]
                recommendations = subcategories[sub_name]

        print_recommendations(recommendations)

        # Ask to continue
        print("\nWould you like to explore other topics?")
        continue_choice = get_user_choice({'Y': 'Yes', 'N': 'No'})

        if continue_choice == 'N':
            print("\nEnjoy your reading!")
            break
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
