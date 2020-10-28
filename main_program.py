
from Classes.LandingPage import LandingPage
from Data.Doctor import Doctor

# Navigate to our SAMS.GOV Site and click the "Search Records" tab
landingPage = LandingPage(None)
searchRecordsPage = landingPage.click_search_records()

# Create our doctor and search for him
doctor = Doctor(first_name = "Elizabeth", last_name = "Williams")
searchResultsPage = searchRecordsPage.search_for_doctor(doctor)