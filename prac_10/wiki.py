import wiki

def wikipedia_search():
    """
    Conduct interactive searches on Wikipedia and display search results.
    """
    while True:
        # Prompt the user to input a Wikipedia page title or a search term
        query = input("Enter a Wikipedia page title or a search term: ")

        # Terminate the loop if the input is empty
        if not query:
            break

        try:
            # Obtain the Wikipedia page for the provided title
            page = wikipedia.page(query, auto_suggest=False)

            # Display the title, summary, and URL of the page
            print("Page Title:", page.title)
            print("Page Summary:", wikipedia.summary(query))
            print("Page URL:", page.url)

        except wikipedia.DisambiguationError as error:
            # Manage search queries leading to multiple results
            print("Multiple entries found. Please clarify your search from these options:", error.options)

        except wikipedia.PageError:
            # Address situations where no page matches the search
            print("No matching page found. Please try a different search term.")

        except Exception as general_error:
            # Address any other unforeseen errors
            print("An unexpected error occurred:", general_error)

# Run the wikipedia_search function when the script is executed directly
if __name__ == "__main__":
    wikipedia_search()
