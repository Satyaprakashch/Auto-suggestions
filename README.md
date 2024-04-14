# Auto-suggestions
This repository contains A Python code for generating auto-suggestions based on input patterns utilizing regular expressions, alongside Python unittest code for automated testing.
# auto_suggestions.py
# test_auto_suggestions.py

# AutoSuggestify 🌟
AutoSuggestify is your go-to tool for generating slick suggestions based on funky patterns. With its powerful regular expression magic, it can match patterns against a list of words to provide you with snazzy suggestions in no time!

# Usage
# 1) In test_auto_suggestions.py Import the AutoSuggestions class from the auto_suggestions module.

     from auto_suggestions import AutoSuggestions
   
# 2) Get Suggestions: Call the get_auto_suggestions(input1, input2) method, providing a list of words (input1) and a pattern (input2) for which you desire suggestions.

     # Example usage
      input1 = ['take', 'make', 'check', 'ackec', 'cake']
      input2 = "*k"
      suggestions = AutoSuggestions.get_auto_suggestions(input1, input2)
      print(suggestions)

Running the Tests: Execute the below code

# Run this command for automated testing.
python -m unittest test_auto_suggestions.py
