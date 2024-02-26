# utils.py

def preprocess_text(text):
    """Preprocess text before feeding it into the NLU pipeline"""
    # Add preprocessing logic here (e.g., lowercasing, removing punctuation, etc.)
    return text.lower().strip()

def get_location_from_user_profile(user_profile):
    """Extract location from user profile"""
    # Add logic to extract location from user profile (e.g., database lookup, API call, etc.)
    return user_profile.get("location", None)
