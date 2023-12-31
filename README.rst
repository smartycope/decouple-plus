# Decouple Plus
A complete settings solution for various Python projects

## WARNING: This repo is a work in progress.

## Required Features
I made this repo to make an all-inclusive, fully featured, general settings solution for Python projects. I got sick of re-writing settings implementations for projects and decided to do it right. 
I like the python-decouple module, but it doesn't have some features that I want.
I require the following features:
- Easy access
  - It should be super easy to access settings
    - It should act just like a regular Python variables, with additional members & methods
- Easy changing
  - It should be super simple to change settings in the program
    - Override the = operator to have it auto edit the settings file in real-time
- Portable
  - Sometimes, you don't want to refactor code to add settings. It should work like normal Python variables
- File saving
  - It should be able to read and set to and from multiple file formats
    - settings.json, settings.ini, .env, settings.env, settings.csv
  - It should auto-detect settings files in the project directory
  - It should have an option to not save settings to the settings file
  - It should distinguish between settings that get reset every run, and settings that persist across several runs, and read-only settings that can only be changed by editing the file directly, or by changing enviorment variables
    - It should default to persisting, and automatically edit the file every time the variable is reset
- Organized
  - Settings should have the option to be grouped under "folders"
- Automated
  - It should auto-generate an options menu, for lazy people who don't care to make their own (I'm thinking it'll use TKinter, because even though it's terrible, it's built into python)
    - The auto-generated GUI should be available by itself as well, to edit the settings file directly
  - Sometimes, you don't want to do much. I want to be able to add a metaclass that grabs the static vars in the class and makes them into settings for you
- Customizable
  - Settings should be able to have limits (both for the sake of the generated GUI, as well as validation)
- Typing
  - It should handle bool, int, float, str, percentage, and Enum, automatically, and should have support to use custom types
