import pandas as pd


def clean_data(matches):
    # Name to replace
    old_name = 'Rising Pune Supergiant'
    new_name = 'Rising Pune Supergiants'

    # Create a function to replace the name
    def replace_name(value):
        return new_name if value == old_name else value

    # Apply the replacement function to the entire DataFrame
    cleaned_matches = matches.applymap(replace_name)

    # Other cleaning operation
    return cleaned_matches  # Return the cleaned DataFrame
