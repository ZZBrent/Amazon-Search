# Amazon-Search
A Python program that allows the user to instantly search for a product and automatically select the first result.

This program is very short and fairly simple, but it did cause a little bit of trouble.  Amazon is equipped with safety features in order
to keep people from doing automation on it.  However, after running a few tests I was able to figure out what strings Amazon looks for in
the URL (which change over time based on how many searches you do within a small period of time).  I, of course, have made this app for
the casual online searcher who finds the name of a new product, wants to copy the name and press one button to find it on Amazon.  So, 
if a user performs more than ten searches in a short period of time the search will take the user to the product list page instead of
straight to the first product listed from the search.
