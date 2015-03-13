Hackbright review: 10/28/2014 6-7:30 PM

Questions from group (what to review during review session):
Javascript3!
Bootstrap – when to add CSS and focus on front-end design vs. when to focus on logic? 
How to start building from scratch?

Advice: Start small – build a small app with Flask and all the right pieces.

Let’s try to make a button – here’s the process we used:
Create a Python file (button.py)
Create virtual environment (pip install Flask and any other requirements in shell)
Activate our virtual environment.

source env/bin/activate
pip install flask (this time into your virtual environment!)

Import headers (e.g., from flask import Flask, render_template)
Add “app = Flask (__name__)”
Switch from Python file to HTML – let’s make the actual button. (index.html)
<html><head><title> Button</title></head><body></body></html>
Let’s decide what functionality the button will have
Note that the form needs to be in the body portion of the HTML file.
<form action = “/wonderful”> <button type = “submit” id =“mybutton>  BEST BUTTON </button> </form>
We added an ID to the button so that we have an event listener if we want to do anything in JavaScript with it
If you put any text in between your tags, it will print inside the button (e.g., THE BEST BUTTON above)
Back to Python – you can do routing for the button in Flask or in JavaScript. Let’s do Flask first (because we all want to avoid JS for time being):

@app.route(‘/wonderful’)
def go_to_wonderful():
     return render_template(“wonderful.html”)
      
@app.route(‘/‘)
def home_page():
     return render_template(“index.html”)

 Now let’s go make wonderful.html:
<html><head><title> Wonderful</title></head><body> Hooray! </body></html>

	It works!

Issues we ran into as we went and created app:
Remember to activate virtual environment as soon as possible (or else)
We needed to change app_route to app.route (made change)
As we went along, we realized we need to also import render template on the first line where we import everything we need in from flask
We forgot to add in:
    		  if __name__ == "__main__":
         	 		app.run(debug = True)
     * You want to add this in every time you start making a Python file!!!
     

Questions from group on example:
Why does it say form action = “/wonderful” without method == GET? Because GET is default. 
Button type = submit is a sneaky event listener (or so we think)
Can you also use A HREF? Yes.
Julie got up and showed us how to do this:
	<a href = “/”> <button> AHSDKASDAS </button> </a>
Essentially the same thing for our example app – normally there’s text inside the a tag and people are clicking on the text link, you could put images inside the tag, etc.
History/evolution of HTML:
Started with a tag to link to other pages
Then form tags came about,
Then submit button came about <input_type = “submit”> 
So now there is a button tag.  
Input_type has no meaning outside of a form – until JavaScript came along. These buttons could be tied to JavaScript actions that are called when the button is clicked. HTML standard has moved away from input type = submit to button where <button type = “submit”> (which submits a form). 
This can be confusing, but tl;dr – use <button type = “submit”> most of the time.

In AJAX, you can use serialize to take in multiple text inputs (used in MadLibs) – this can only be used on forms
Tip: instead of putting index.html, put {{url_for(‘home_page’)}} – use Jinja here and give it the name of the function that you want to access. 
This is helpful in case you change the name of index.html or have the app.route point to a different URL. 
When we work on our projects, instead of hardcoding your routes, use the url for function so that if you change the URLs/routes, it still works. 
Now let’s try something in JavaScript:
Make a static folder and a JavaScript file – OR – we could just put this in HTML as a script tag (we opted to do the latter in index.html)
We could add a click listener, but if we want to use that, we need to first use jQuery and add it in. We do this by adding it into from a developer library. Where should we place it? Doesn’t matter, so long as it’s before we call script (so that we have it available to use). We added it into the head as <script src = “ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery...js”> </script> (this link is truncated, you’ll want to look it up via Google)
Now we go and put JS in the bottom of index.html:
<script> $(“#my_button”).click(alert”Hi”)); </script>
Need to pass alert an argument (so we added “Hi” in)
It worked!
In sum – all we did was add .click to one of our ids, then added an alert so that when it’s clicked on, it will pop up a message (reading “Hi”). Remember to use semi-colons.

Let’s try something else in JavaScript – passing data back and forth confuses a lot of people, so we’re going to pass some data.

<script> $(“#my_button”).click(julie_function);
# this function julie_function would live right below inside the JS
function julie_function(){
	$.get(‘wonderful/hello’, 
function (result){
		alert(result);
} 
	
}

</script>

This (the julie_function) is an anonymous function – you can pass as many things through .get as you like within those curly braces for get. (Python and Flask are going to take this and hopefully return something to you.)

Here’s the app route we added to our Python file (button.py) that gets returned by julie_function:

@app.route(‘/wonderful/hello’)
	return “What’s up?”

 

