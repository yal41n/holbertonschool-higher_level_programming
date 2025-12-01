import os
import logging

# Configure basic logging to output messages to the console
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template string with placeholders.
        attendees (list): A list of dictionaries, where each dictionary
                         represents an attendee and their data.
    """
    
    # Define the expected placeholders to check for missing data
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # --- 1. Check Input Types ---
    if not isinstance(template, str):
        logging.error("Invalid input: Template must be a string.")
        return
    
    if not isinstance(attendees, list):
        logging.error("Invalid input: Attendees must be a list of dictionaries.")
        return
        
    for attendee in attendees:
        if not isinstance(attendee, dict):
            logging.error("Invalid input: Attendees list must contain only dictionaries.")
            return

    # --- 2. Handle Empty Inputs ---
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return
    
    # --- 3. Process Each Attendee and Generate Files ---
    for index, attendee in enumerate(attendees):
        # Start with a fresh copy of the template for each attendee
        invitation = template
        
        # Determine the output filename (starting index X from 1)
        filename = f"output_{index + 1}.txt"
        
        # Replace each placeholder
        for placeholder in placeholders:
            # Get the value, or use None if the key is missing
            value = attendee.get(placeholder)
            
            # --- 4. Handle Missing Data in Object ---
            # If value is None, or an empty string, replace it with "N/A"
            if value is None or str(value).strip() == "":
                replacement = "N/A"
            else:
                replacement = str(value)
                
            # Replace the placeholder (e.g., {name}) in the template
            invitation = invitation.replace(f"{{{placeholder}}}", replacement)
        
        # --- 5. Generate Output Files ---
        try:
            # Write the personalized invitation to the output file
            with open(filename, 'w') as f:
                f.write(invitation)
            logging.info(f"Generated invitation file: {filename}")
        except IOError as e:
            logging.error(f"Error writing file {filename}: {e}")

# --- Example Usage (Mirroring the expected main file content) ---
if __name__ == '__main__':
    # 1. Create the template file content as required by the example
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    # For testing completeness, we simulate reading from the file if needed, 
    # but the task specifies the function takes the template string directly.
    # To run this example, create a file named 'template.txt'
    try:
        with open('template.txt', 'w') as f:
            f.write(template_content)
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except IOError:
        print("Warning: Could not create/read template.txt. Using hardcoded string.")
        pass

    # 2. Example Data for Testing:
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        # Charlie is missing 'event_date' (set to None) to test "N/A" replacement
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Clean up old output files before testing (Optional, but useful)
    for i in range(1, len(attendees) + 3):
        try:
            os.remove(f"output_{i}.txt")
        except OSError:
            pass
            
    # 3. Call the function with valid input
    print("\n--- Testing Valid Input ---")
    generate_invitations(template_content, attendees)

    # 4. Test Error Cases
    print("\n--- Testing Empty Template ---")
    generate_invitations("", attendees)

    print("\n--- Testing Empty List ---")
    generate_invitations(template_content, [])
    
    print("\n--- Testing Invalid Input Types ---")
    generate_invitations(123, attendees)
    generate_invitations(template_content, "not a list")
