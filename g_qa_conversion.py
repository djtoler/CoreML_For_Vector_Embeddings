import google.generativeai as genai
import PIL.Image
import os
import time

# Ensure you have set the environment variable GOOGLE_API_KEY before running this code
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

chat = model.start_chat(history=[])

response = chat.send_message(
"""
You're a ciricuulum developer. Please read the following text and generate 12 questions for someone wanting to learn about gameification. Put the question and answer pairs into JSON format.

Chapter 2: Basic Page Structure 23
NOTE
You might also see more advanced types of pages on the Internet, such as Microsoft’s
Active Server Pages (.asp) or those written in the Extensible Markup Language (.xml).
These are beyond the scope of the traditional HTML page, and therefore not covered in
this book.
Naming Conventions
Remember the following few points when naming your HTML files.
● Although in most cases it doesn’t matter whether you use .html or .htm, you should be
consistent to avoid confusing yourself, the browser, and your users.
NOTE
Wondering why some people use .html and some use .htm? Older systems such as
Windows 3.1 and DOS could not understand four-letter file extensions, so anyone
creating web pages on those systems used .htm as the extension. In any case, because
the first three letters of .html and .htm are the same, those systems simply ignored the “I”
and recognized the file type without any problems.
24 HTML: A Beginner’s Guide
● Some web servers are case-sensitive, so remember this when naming and referencing
filenames and try to be consistent. If you name your file MyPage.html, and then reference
it later using mypage.html, you may end up with a broken link. One good technique is to
use only uppercase or lowercase to name your files. This way, if you see a file with a letter
in it that doesn’t match, you know instantly that file is probably the problem. Even the pros
run into case-sensitivity problems on an almost daily basis.
● Use simple filenames with only letters and numbers. Don’t use spaces, punctuation, or
special characters, other than hyphens (-) and underscores (_). Good examples might be
home.html, my-story.html, and contactme.html.
TIP
While it’s perfectly acceptable to use an underscore (_) in a file or folder name, I suggest
using a hyphen instead. Underscores can easily become confused with an underline,
especially when displayed as a link on a web page (because links are usually underlined).
These same recommendations hold true for any folder names you use. If you were creating
a web site that had your favorite links, family photos, and résumé, you might find it useful to
put each of those things in a separate folder.
TIP
If you decide to use Microsoft Word or WordPad to type your HTML, you need to
choose the file type “Text Document” or “Text Only” and give the file an .html extension
the first time you save it. This is because both of those programs default to saving
“Word for Windows” or “Microsoft Word” documents with a .doc or .docx extension.
Preview an HTML File in a Browser
You can view HTML files located on your personal computer within your own web browser.
It isn’t necessary for your files to be stored on a web server until you are ready to make them
visible on the Internet.
When you want to preview a page, open your web browser and choose File | Open (or
Open Page or Open File, depending on your browser), and then browse through your hard
Chapter 2: Basic Page Structure 25
drive until you locate the HTML file you want to open. (Note, if you don’t see any File menus
in IE, try pressing the ALT key to reveal those menus.)
If you’re going to make frequent changes to the HTML file in a text editor, and then switch
back to a web browser to preview the page, keeping both programs (a text editor and a web
browser) open at the same time makes sense. When using a basic text editor, the steps to edit
and preview HTML files are
1. Open/return to your HTML file in a text editor.
2. Edit your HTML file in a text editor.
3. Save your HTML file in a text editor.
4. Open/return to your HTML file in a web browser.
5. Click the Refresh or Reload button in your web browser to update the HTML page to reflect
the changes you just made to it.
By keeping your HTML file open in both a text editor and a browser, you can easily make
and preview changes.
Web browser Text editor
26 HTML: A Beginner’s Guide
If you’re using a graphical or WYSIWYG editor, the steps are slightly different because
these types of programs include a browser preview option. For example, Adobe Dreamweaver
offers three ways to work with an HTML file. One option is to view only the code, as you
would in a basic text editor. Another option is to work in the preview mode, moving page
elements around on the page by clicking and dragging. Finally, you can use a combination,
where the code is visible on part of the screen and the browser preview is visible on the rest (as
shown in Figure 2-1).
Figure 2-1 Accessing both the code and browser preview at once with Adobe
Dreamweaver
Chapter 2: Basic Page Structure 27
Describe and Apply the Basic
HTML Document Format
An HTML entity or tag is a command used to tell the browser how to display content on a
page. This command is similar to what happens behind the scenes when you highlight some
text in a word processor and click the Italic button to make the text italicized.
With HTML, instead of clicking a button to make text italicized, you can type a tag before
and after the text you want to emphasize, as in the following:
<em>Reminder:</em> There will be no band practice today.
You can easily recognize tags because they are placed within brackets (< >), or less-than and
greater-than symbols.
Did you notice that the tag to emphasize text and make it italic is em? Given that piece of
information, can you guess the tags to add a paragraph or create items in a list?
Purpose Tag
Create paragraphs <p>
Create list items <li>
Add a line break <br>
Now do you believe me when I say HTML is not rocket science? Don’t worry—most of the
tags are pretty intuitive and easy to remember.
Types of Tags
In HTML, there are usually both opening and closing tags. For example, if you use <p> as an
opening tag to signify where to start a new paragraph, you have to use a closing tag to signify
where that paragraph ends (unless you want your entire page to be contained within one
paragraph). To do so, use the same tag with a forward slash placed before it: </p>. Table 2-1
shows a list of basic HTML page tags.
Attributes
Many tags have additional aspects that you can customize. These options are called attributes
and are placed after the tag but before the final bracket. Specific attributes for each tag are
discussed as we move through the book. But to give you an idea of how attributes work, let’s
look at an example using the img tag.
<img src="mypicture.jpg" width="100" height="100" alt="A photo of me"/>
In this example, the base tag is img, which tells the browser I want to insert an image at
this spot. The attributes are src, width, height, and alt. Each attribute has a value, which
comes after an equal sign (=) and is placed within quotation marks.
28 HTML: A Beginner’s Guide
Opening Tag Closing Tag Description
!DOCTYPE n/a - Tells the browser which set of standards your page adheres to.
- Lists the standard (see the section “Doctype” later in this chapter).
- Identifies the location of the standard by linking to the URL.
<html> </html> - Frames the entire HTML page.
<head> </head> - Frames the identification information for the page, such as the title,
that is transferred to the browser and search engines.
<body> </body> - Frames the content of the page to be displayed in the browser
window.
<title> </title> - Gives the name of the page that will appear at the top of the browser
window and be listed in search engines.
- Is contained within <head> and </head>.
Table 2-1 Basic HTML Page Tags
There’s no need to repeat the img tag, because multiple attributes can be included in a
single tag. When you add attributes to a tag, you only put them in the opening tag. Then, you
only need to close the tag (not the attributes). Note that this tag is one that doesn’t have a
separate closing tag. (In fact, old versions of HTML didn’t require the img tag to be closed at
all.) To close tags without separate closing versions, simply place a forward slash (/) before the
final bracket, as shown in the preceding code example.
Required Tags
All HTML pages need to have the html, head, and body tags, along with the DOCTYPE
identifier. This means, at the very least, your pages should include the following:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/transitional.dtd">
<html>
<head>
<title>My First HTML Page</title>
</head>
<body>
This is a very basic HTML page.
</body>
</html>
Here is the result of this page when displayed in a browser.
Chapter 2: Basic Page Structure 29
To test this basic HTML page for yourself, try the following:
1. Open a basic text editor, such as TextEdit (Mac) or Notepad (PC).
2. Copy the preceding code into a new text document.
3. Save it as a text-only file (ASCII text) and name it test.html.
4. Launch your browser and choose File | Open File (Firefox or Safari) or File | Open (Internet
Explorer).
5. Browse your hard drive to locate the test.html file, and you’re off and running!
NOTE
If you’re using IE7+ and don’t see the File menus, press ALT to reveal those menus.
Doctype
The DOCTYPE tag is a required tag that is used to tell the browser which version of HTML
is used in the document. When the W3C released HTML4 and XHTML, it specified three
possible flavors, or versions, to accommodate the anticipated transition time during which
developers and browsers were supposed to migrate from HTML 4.0 to XML:
● XHTML Transitional For documents that contain a combination of old and new
HTML code
● XHTML Strict For documents that don’t contain any outdated code and are structurally
“clean”
● XHTML Frameset For documents containing frames
30 HTML: A Beginner’s Guide
However, the W3C eventually abandoned the concept of transitional documents, in favor
of HTML5, which will support both HTML and XML simultaneously. But until HTML5 is
finalized and fully adopted by the major web browsers, you still need to identify your page
with one of these three flavors listed to help the browser validate it. Given that we know these
three flavors will be phased out over the next few years, I suggest using the easiest one to work
with (transitional) to validate your current web pages. To validate your pages against this flavor
of XHTML, use
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/transitional.dtd">.
NOTE
To give you a glimpse as to what the future holds, after HTML5 is adopted, you’ll simply
have to use a doctype that identifies whether your page is HTML or XML. For example,
HTML files will use <!doctype html>. Simple, huh? In general, HTML5 looks to be a
great next step for this powerful language.
Validating Against These Doctypes
Wondering why you even need to validate your HTML against a particular doctype? The
purpose of validation is to help identify potential problems a browser might encounter
when displaying your page. Because browsers render pages according to the official HTML
specifications (as dictated by the W3C), it makes sense to double-check your pages against
those specs as part of your testing.
The official W3C validation service can be found at http://validator.w3.org. Once you get
there, you’ll notice you can use several different methods to test or validate your pages.
● Validate by URI If your page is already live on the Internet, you can simply enter the
page’s URI (address), and the tool will seek to validate your page.
● Validate by file upload If you’re working on pages currently stored on your hard drive
(but not live on the Internet), you can upload those pages to the online validator.
● Validate by direct input Alternatively, you can simply copy and paste the code into an
online form at the validation service.
Regardless of which method you choose, the results will be the same. The validator will
give you a passing or failing grade. If your page fails to validate against the standard you’ve
listed in your code, the tool will also tell you why the page fails. For example, it might tell
you if you’ve used a particular attribute in the wrong tag, or if you’ve used a tag that’s not
in the spec.
Chapter 2: Basic Page Structure 31
Ask the Expert
Q: I typed the preceding HTML into a text file, but when I tried to preview the page in
my browser, nothing happened. Why?
A: There are several possible reasons why your page might appear blank. First, review
the code in the preceding example and compare it line by line with the code you typed.
Forgetting a closing tag or maybe just a forward slash (/) is easy. Sometimes it’s helpful
to take a quick break before returning to scrutinize your page. If you do make a change,
be sure to save the file in your text editor, before clicking Refresh or Reload in your web
browser.
If you’re certain the code in your page matches the example, try resaving your file under
a new name. Close your browser, then relaunch your web browser and open the page in the
browser again.
Additional troubleshooting techniques are located in Appendix C.
Capitalization
Original versions of HTML were case-insensitive and, in fact, very forgiving. This means all
of the following examples would be considered the same by the browser:
● <html>
● <HTML>
● <HTml>
That said, HTML4/XHTML is case-sensitive and requires all tags to be lowercase. Of the three
preceding examples, the browser might properly interpret only the first.
To make it really confusing, HTML5 returns to being case-insensitive. Given the differences
between the various versions of HTML currently in use, I recommend using all-lowercase tags.
Quotations
HTML4/XHTML also requires all values to be placed within straight quotation marks, as in
the following example:
The value of the attribute
<p style="font-family: verdana;">
Nesting
The term nesting appears many times throughout the course of this book and refers to the
process of containing one HTML tag inside another. The em tag is nested
within the strong tag.
<strong>This text is bold and <em>italic</em></strong>
32 HTML: A Beginner’s Guide
You have a proper way and an improper way to nest tags. All tags should begin and end
starting in the middle and moving out. Another way of thinking about it involves the “circle
rule.” You should always be able to draw semicircles that connect the opening and closing
versions of each tag. If any of your semicircles intersect, your tags are not nested properly.
Using the following example, the first one is proper because the strong tags are both on
the outside and the em tags are both on the inside.
<strong><em>These tags are nested properly.</em></strong>
<strong><em>These tags are not nested properly.</strong></em>
Even though both may work in some browsers, you need to nest tags the proper way to ensure
that your pages display the same across all browsers.
Spacing and Breaks
Let’s look closely at some example HTML to identify where proper spacing should occur.
(Note, the a tag and href attribute are used to link something, in this case text.)
No space is between the No space should come between
<body> brackets and the tag. a tag and the text it affects.
<a href="http://www.google.com" title="Search Google">Search Google</a>
A single space should come A single space should come
between tags and attributes. between attributes.
Two places exist within an HTML file where you might like to add breaks:
● In between tags, to help you differentiate between sections of the page
● In between lines of text within the body of the page
Spacing and Breaks Between Tags
The first place you might like to add breaks is in between tags, as in the following example.
<html>
<head>
<title>My First Web Page</title>
</head>
Although this is not required, most people use the ENTER or RETURN key to separate
tags with line breaks. Others also indent tags that are contained within other tags, as in the
preceding example: the title tag is indented to show it is contained or nested within the
head tag. This may help you to identify the tags more quickly when viewing the page in a
text editor.
Spacing Between Lines of Text
The second place you add breaks is between the lines of text in the body of the page. If you
use the RETURN or ENTER key on your keyboard to add a line break in between two lines of text
on your page, that line break will not appear when the browser displays the page.
Chapter 2: Basic Page Structure 33
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/transitional.dtd">
<html>
<head>
<title>My first Web page</title>
</head>
<body>
Welcome.
Thank you for visiting my first Web page. I have several other pages
that you might be interested in.
</body>
</html>
In this code, I pressed the RETURN key twice after the word “Welcome.” In this example,
you can see that the browser ignored my returns and ran both lines of text together.
To make those line breaks appear, I’d have to use a tag to tell the browser to insert a line
break. Two tags are used for breaks in content.
<br />
<p></p>
The br tag inserts a simple line break. It tells the browser to drop down to the next line
before continuing. If you insert multiple br tags, the browser will drop down several lines
before continuing.
The p tag signifies a paragraph break. The difference between the two is that paragraph
breaks cause the browser to skip a line, while line breaks do not. Also, the p tag is considered
34 HTML: A Beginner’s Guide
a container tag because its opening and closing tags should be used to contain paragraphs of
content. The br and p tags are discussed in more detail in Chapter 4.
NOTE
Because the br tag doesn’t contain any text, as the p tag does, it doesn’t have
opening and closing versions. Instead, you place a slash before the closing bracket to
“terminate” the tag, as in: <br />.
If I enclose each of these paragraphs in p tags, like the following:
<p>Welcome.</p>
<p>Thank you for visiting my first Web page. I have several other
pages that you might be interested in.</p>
the browser will know to separate them with a blank line. The following screen shows how the
browser displays the text now that I have contained each of the paragraphs in p tags.
In addition, HTML neither recognizes more than a single space at a time nor interprets a
tab space as a way to indent. This means that in order to indent a paragraph or leave more than
one space between words, you must use style sheets (see Chapter 4) or special characters.
Use Character Entities to Display Special Characters
As crazy as this sounds, you technically shouldn’t include any characters in your HTML files
that you can’t type with only one finger. This means, if you have to hold down the SHIFT key
to type an exclamation mark or a dollar sign, you are supposed to use a character entity to
include that special character in your HTML file.
Chapter 2: Basic Page Structure 35
Even though you might be able to type a certain character on your computer system
without any problems, some characters may not translate properly when visitors to your web
site view your page. So, I recommend you use character entities to maintain consistency across
computer systems.
Character entities can be typed as either a numbered entity or a named entity. All character
entities begin with an ampersand (&) and end with a semicolon (;). Although every character
entity has a numbered version, not every one has a named version. While a full list of special
characters is included in Appendix D, a few are listed in the following table to give you an idea
of what they look like.
NOTE
A few characters are reserved and given special meaning in HTML. For example, the
brackets (< and >) are used to signify HTML tags, while the ampersand (&) is used to
begin these entities. If you need to use a bracket within the content of your HTML page,
such as when a greater-than symbol is needed, in the case of 3 > 2, you should use the
corresponding character entity (&gt;) to do so.
Character Numbered Entity Named Entity
" &#34; &quot;
& &#38; &amp;
(nonbreaking space) &#160 &nbsp;
© &#169; &copy;
® &#174; &reg;
é &#233; &eacute;
< &#60; &lt;
> &#62; &gt;
Having now made the case for using character entities, let me just say here that it’s been
my experience that certain characters can actually be used in a web page without causing any
problems. These include straight—not curly—quotation marks (''), exclamation marks (!),
question marks (?), colons (;), and parentheses (). While I haven’t noticed any of these to cause
problems in the majority of browsers, you should still test your pages thoroughly when using
any special characters.
Add Comments to an HTML File
Sometimes you might not want your web site visitors to see personal comments or notes
you’ve added to your web pages. These notes might be directions to another person or
reminders to yourself.
<!-- Remember to update this page after the new product becomes
available -->
36 HTML: A Beginner’s Guide
After the opening bracket, an exclamation mark and two hyphens signify the beginning of a
comment. A space should appear after the opening comment code, as well as before the closing
comment code.
Comments are not restricted in size but can cover many lines at a time. The end comment
code (-->) doesn’t need to be on the same line as the beginning comment code. If you
forget to close your comment tag, the rest of the page will not appear in your browser. If this
happens, don’t be alarmed. Simply go back to the code and close that comment. The rest of the
page will become visible when you save the file and reload it in the browser.
Set Up Style Sheets in an HTML File
I’ve already mentioned the phrase “style sheets” a few times, but haven’t really given them a
full explanation yet. Part of the reason is that style sheets weren’t really a part of HTML until
it was rewritten as XHTML. The purpose of cascading style sheets (abbreviated CSS) is to
separate the style of a web page from its content.
The current HTML “rules” dictate that we only use HTML to identify the content of the
page, and then use a style sheet to specify the presentation of that content. This not only makes
web pages more accessible and usable to all users (regardless of their browsers, platforms,
operating systems, physical limitations, and so forth), but also to search engines and other
types of software.
TIP
If you’ve ever used the Style drop-down menu in Microsoft Word, you’ve already used
a style sheet of sorts. The most basic style sheet might include a style called “Body Text,”
that specifies how the body text of the web page should look—which font and color to
use, how much space to leave around it, and so on.
Define the Style
To define a basic formatting style, you first must identify which tag you want to affect. This
tag is then called a selector in CSS. So, if you wanted to specify the style of all the level-2
headlines (<h2>) on a page, you would use h2 as your selector.
h2
In fact, the selector is essentially the tag without the brackets. With that in mind, can you
guess what the selector for <p> would be?
p
Once you have a selector, you can define its properties. Similar to how attributes work
in HTML, CSS properties alter specific attributes of a selector. Returning to the preceding
example, if you want to change the style of the level-2 headlines on your page to a 14-point
Verdana font, italic, and blue, you can use the following properties:
Chapter 2: Basic Page Structure 37
font-family
font-style
font-size
color
When you specify values for properties, you are creating a declaration for that selector.
The declaration and selector together are then referred to as a set of rules, or a ruleset. In the
typical ruleset, the declaration is enclosed in curly brackets after the selector.
So here are the first few pieces of our ruleset:
h2 Selector
font-family Property
verdana Value
{font-family: verdana;} Declaration
And here is how they all fit together to tell the browser to display all level-2 headlines in the
Verdana font.
h2 {font-family: verdana;}
To specify the font size, color, and style (italic), we simply add on a few more of those
properties.
h2 {font-family: verdana;
font-size: 14pt;
color: blue;
font-style: italic;}
At this point, you can probably start to see the pattern—a CSS property is followed by
a colon, and then its value, which in turn is followed by a semicolon.
Define the Values
As with attributes in HTML, properties have values. Most values can be specified in terms of
color, keyword, length, percentage, or URL, as listed in Table 2-2. Length and percentage units
can also be made positive or negative by adding a plus (+) or minus (−) sign in front of the
value.
Create the Structure
After you know a little about the individual parts of CSS, you can put them together to create a
few styles. The organization of these pieces depends a bit on which type of style sheet you are
creating. CSS offers three types of style sheets:
● Inline Styles are embedded right within the HTML code they affect.
● Internal Styles are placed within the header information of the web page, and then affect
all corresponding tags on a single page.
38 HTML: A Beginner’s Guide
Type of Value Description
Color When specifying color in a value, you can do so in one of three ways (see Chapter 3
for more information on color):
- hexadecimal code, such as #000000
- RGB values, such as rgb (0,0,0) or rgb (0%, 0%, 0%)
- one of the predefined keywords
Keyword A keyword is a word defined in CSS that’s translated into a numerical value by the
browser. For this reason, keywords are often considered relative because, ultimately,
it’s up to the browser to decide how to render the content. An example of a keyword
is small.
Length In HTML, most units are defined in pixels. In CSS, however, you have the option of
using many other types of units. For example, when specifying text sizes with the
font-size property, you can use any of the following. (Abbreviations are shown
in parentheses.)
- points (pt)—72 points in an inch
- picas (pc)—12 points in a pica
- pixels (px)— dots on the screen
- ems (em)—refers to the height of the font in general
- exs (ex)—refers to the height of an x in a particular font
- inches (in)
- millimeters (mm)
- centimeters (cm)
Percentage Relative percentages can be useful in CSS when used to position elements on a
page. This is because percentages allow elements to move around, depending on
how large the screen and window sizes are. When used in CSS, a percentage sign
(%) following a numerical value, such as 100%, indicates a relationship between the
surrounding elements.
URL When you reference an absolute URL in CSS, use the following form:
url (http://www.osborne.com)
Similarly, relative URLs (typically those found within the current web site) are
referenced in the following manner: url (home.html).
Table 2-2 Types of CSS Values
● External Styles are coded in a separate document, which is then referenced from within
the header of the actual web page. This means a single external style sheet can be used to
affect the presentation on a whole group of web pages.
You can use any or all of these types of style sheets in a single document. However, if you
do include more than one type, the rules of cascading order take over: these rules state that
inline rules take precedence over internal styles, which take precedence over external styles.
In a nutshell, CSS styles apply from general to specific. This means a ruleset in the head
tag of a document overrides a linked style sheet, while a ruleset in the body of a document
overrides one in the head tag. In addition, more local (or inline) styles only override the parent
attributes where overlap occurs.
Chapter 2: Basic Page Structure 39
Inline
Inline styles are created right within the HTML of the page, hence the name. In the previous
examples, a declaration was surrounded by curly quotes, but inline declarations are enclosed in
straight quotes using the style attribute of whichever tag you want to affect.
<h2 style="font-family: verdana;">
You can separate multiple rules by semicolons, but the entire declaration should be
included within quotes.
<h2 style="font-family: verdana; color: #003366;">
Inline styles are best for making quick changes to a page, but they aren’t suited for changes
to an entire document or web site. The reason for this is that when styles are added to a tag,
they occur only for that individual tag and not for all similar tags on the page.
TIP
Inline styles overrule internal and external styles when multiple types of style sheets are
found on the same page.
Internal
When you want to change the style of all the h2 tags on a single page, you can use an internal,
or embedded, style sheet. Instead of adding the style attribute to a tag, use the style tag to
contain all the instructions for the page. The style tag is placed in the header of the page, in
between the opening and closing head tags. Here’s an example of what an internal style sheet
might look like.
<head>
<title>CSS Example</title>
<style type="text/css">
h2 {font-family: verdana; color: blue;}
h3 {font-family: verdana; color: red;}
</style>
</head>
As this example shows, the selector is placed before the declaration, which is enclosed in
curly brackets. This entire ruleset can be contained on a single line or broken up into multiple
lines, as in the following example.
h2
{font-family: verdana;
color: blue;}
You can write styles in several ways. The following example is just as valid as the
preceding one and is preferred by some people because it is easier to read.
h2 {font-family: verdana;
color: blue;}
40 HTML: A Beginner’s Guide
In addition, you can use certain shorthand properties to reduce the amount of coding
necessary. For example, instead of specifying both font family (Verdana) and font size
(12 point), you could type the following because both properties begin with font.
h2 {font: verdana 12pt;}
TIP
Chapter 4 discusses how to style text in much more detail.
External
An external style sheet holds essentially the same information as an internal one, except an
external style sheet is contained in its own text file and then referenced from within the web
page. Thus, an external style sheet might look like this:
Notice that external style sheets don’t use the style tag or attribute but simply include a
list of rulesets as instructions for the browser. Once you create your external style sheet, save it
as a text file, with the .css file extension.
Then, return to your HTML file and add the link tag to the page header to reference the
external style sheet, as in the following example.
<head> This is where the name of
<title>Using an External Style Sheet</title> your style sheet is placed.
<link rel="stylesheet" type="text/css" href="styles.css">
</head>
In this case, I only needed to write styles.css because the style sheet is in the same folder as
my HTML page. However, if your style sheet is in a different folder than your HTML page, be
sure to reference that path appropriately.
NOTE
External style sheets can be overruled by internal and inline style sheets.
Chapter 2: Basic Page Structure 41
Try This 2 -1 Create the First Page of Your Site
To continue with the site you began planning for in the first chapter, we now begin the first
page in your site. These are the main goals for this project:
● Use all the necessary tags to create a basic web page.
● Use a character entity to add a copyright symbol to the page.
● Add space for an internal style sheet in the header of the page.
● Save the page as an HTML file that can be read by a web browser.
● Preview the page in a web browser.
NOTE
All the files needed to complete the projects in this book for the Chop Point site can be
downloaded from www.wendywillard.com. In addition, you can view my version of the
web site anytime by visiting www.choppoint.org.
1. Open a text editor on your computer (such as TextEdit on the Mac or Notepad in Windows).
Copy the following code to begin your web page. Feel free to make edits wherever necessary
to personalize your site for your organization.
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//
EN" "http://www.w3.org/TR/xhtml1/DTD/transitional.dtd">
<html>
<head>
<title>Chop Point Camp and School, located in Woolwich, Maine</title>
<style type="text/css">
</style>
</head>
<body>
<p>Chop Point </p>
<p>Chop Point is a non-profit organization operating a summer camp
and K-12 school in Woolwich, Maine.</p>
</body>
</html>
2. After the end of the second paragraph, use the code you learned in this chapter to add two
breaks and a copyright symbol (©), followed by the name of the organization. (Example:
© Chop Point Inc.)
3. Create a new folder on your hard drive, called choppoint (or the name of your organization
or web site). Save this file as index.html in the folder you just created.
4. Open your web browser and choose File | Open (or Open File, depending on the browser
you’re using). Locate the file index.html you just saved.
(continued)
42 HTML: A Beginner’s Guide
5. Preview the page and compare it to Figure 2-2. If you need to make changes, return to your
text editor (TextEdit or Notepad) to do so. Once you have made those changes, save the file
and switch back to your web browser. Click the Reload or Refresh button in your browser to
update your page according to the changes you just made. The complete code for your page
might look like this:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/transitional.dtd">
<html>
<head>
<title> Chop Point Camp and School, located in Woolwich, Maine </title>
<style type="text/css">
</style>
</head>
<body>
<p>Chop Point </p>
<p>Chop Point is a non-profit organization operating a summer camp and
K-12 school in Woolwich, Maine.</p>
<br />
<br />
&copy; Chop Point Inc.
</body>
</html>
Figure 2-2 Your page should look similar to this one when displayed in a browser,
depending on your organization and content.
Chapter 2: Basic Page Structure 43
TIP
Does your browser window appear blank when you try to preview your page? If so,
return to your text editor and make sure you have included all the necessary closing
tags (such as </body> and </html>). In addition, if you are using any editor other
than TextEdit or Notepad, don’t forget to save the file as “text only” within an .html file
extension. For more tips, see Appendix C, “Troubleshooting.”
Summary
Every web page needs a few tags to display properly in the browser. This project helps you
practice typing those tags and placing them in the correct order on the page.
Getting used to the process of editing, saving, and previewing pages is good because
this is used throughout the rest of this book and during the course of your continued web
development.
✓
Chapter 2 Self Test
1. What file extensions do HTML files use?
2. The following line of HTML code contains errors. What is the correct way to write this
line?
<p This is a paragraph of text p>
3. At the very least, which tags should be included in a basic HTML page?
4. Identify the tag name, attribute, and value in the following line of HTML code:
<a href="page.html">
5. Fill in the blank: XHTML requires all tags to be __________ case.
6. Which option is not acceptable for an HTML filename?
A. myfile.html
B. my-file.html
C. my file.html
D. my1file.html
7. What is the named character entity used to add a copyright symbol to a web page?
8. You just created a web page, and you’re previewing it in a web browser when you notice an
error. After fixing the error and saving the web page, which button should you click in the
browser to view the changes made?
44 HTML: A Beginner’s Guide
9. Which is the proper way to close the br tag in HTML4/XHTML?
A. <br>
B. </br>
C. <br/>
D. <br />
E. </ br>
10. The tags in the following line of code aren’t nested properly. Rewrite the code so that the
tags are nested properly.
<p><strong><em>Hello World!</p></em></strong>
11. How can you rewrite the following text so that it doesn’t display when the page is viewed in
a browser?
Hide Me!
12. Which two options will the browser ignore when they are coded in a web page?
A. <p>
B. A tab
C. <br>
D. <br><br>
E. Single space with the SPACEBAR
F. Double space with the SPACEBAR
13. Fill in the blank: The p tag is an example of a __________ tag because it contains sections
of text.
14. The following line of HTML code contains errors. What is the correct way to write the code?
< img src = "photo.jpg" >
15. What symbols must start and end all HTML tags?
3
Chapter
Color
45
46 HTML: A Beginner’s Guide
Key Skills & Concepts
● Identify the Ways in Which Color Is Referenced in Web Development
● Specify Document Colors
Each browser has a set of standard colors for web pages that can be customized by the user
(see Figure 3-1). If you don’t specify otherwise, your pages will display according to the
browser’s settings.
To change a color on your web page, you need to know the color you want to change it to,
as well as the corresponding color value (described in the following section).
Figure 3-1 Customizing color settings in a version of Firefox
Chapter 3: Color 47
Identify the Ways in Which Color
Is Referenced in Web Development
At the beginning of time—Web time—the only way to reference color in an HTML page was
to use its hexadecimal color value. When CSS became the preferred method of referencing
color in web pages, we were permitted to use a variety of other units to measure color,
including RGB (which stands for Red Green Blue) values, RGB percentages, hexadecimal
shorthand, and color names.
Hexadecimal Color
The “normal” number system in the U.S. is decimal—based on the number 10. This means we
have 10 units (0–9) to use before we have to repeat a unit (as with the number 10, which uses
the 0 and the 1).
The hexadecimal system (hex) uses the same concepts as the decimal system, except
it’s based on 16 units (see Table 3-1). Because standard HTML cannot handle decimal color
values, the hexadecimal system is used to specify color values on web pages. Instead of
making up new characters to represent the remaining units after 9, the hexadecimal system
uses the first six letters of the English alphabet (A–F).
Computer monitors display color in RGB mode, where R = Red, G = Green, and B = Blue.
Each letter (R, G, and B) is represented by a value between 0 and 255, with 0 being the darkest
and 255 representing the lightest in the spectrum. In RGB, white and black have the following
values:
Red Value Green Value Blue Value
White 255 255 255
Black 0 0 0
This is how one graphics program—Adobe Photoshop—displays the RGB values for blue
(R:00 G:00 B:255). Most other graphics programs have similar ways of helping you determine
the RGB values of your colors.
Decimal 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Hex 0 1 2 3 4 5 6 7 8 9 A B C D E F
Table 3-1 Decimal and Hexadecimal Units
48 HTML: A Beginner’s Guide
In Photoshop, one way to find out what the hexadecimal values are for that shade of blue
is to click the triangle in the upper-right corner of that color window and choose Web Color
Sliders from the menu.
The resulting window shows the corresponding hex values for that same blue are R:00
G:00 B:FF.
When using hexadecimal color values in an HTML page, you translate the color from
decimal (RGB) to hex. Each red, green, or blue value translates into a two-digit hex value. You
then combine all three of those two-digit hex values into a single string, preceded by a hash
mark. The following is an example where a hexadecimal color is used to change the text in one
paragraph to blue.
<p style="color: #0000FF;">
TIP
While you previously needed a scientific calculator to convert between decimal and
hexadecimal values, many charts, software programs, converters, and even web pages
are now available to do this for you. Check out www.psyclops.com/tools/rgb/ to see
an example.
Hexadecimal Shorthand
When referencing a color that has value pairs, you can use a bit of shorthand to reduce the
amount of typing necessary. For example, a color with a hexadecimal code of 003366 can be
shortened to 036. This is because each of the two red values is the same, as are each of the blue
and green values. That wouldn’t work for a hexadecimal code of 003466, because the green
values—34—aren’t the same.
Chapter 3: Color 49
The following shows how the same blue used in the preceding code example could be
referenced, using hex shorthand.
<p style="color: #00F;">
NOTE
Hexadecimal shorthand is only allowed when using style sheets—the preferred method
of presenting color in your pages. If you previously learned how to use code like this to
change page colors, <font color="#0000ff">, you can’t start using shorthand in
those hex values. Only complete hexadecimal codes are permitted in those older, now
defunct, HTML tags.
RGB Values and Percentages
If hexadecimal color values already have your head spinning, I have good news! Now that
style sheets are the preferred method of presenting color in all web pages, we no longer have
to struggle with hexadecimal codes. If a color’s RGB values are handy, use those in your style
sheet in place of the hexadecimal code, like in the following:
<p style="color: rgb(0,0,255);">
If you don’t have the RGB values handy, as when working in some page layout or design
programs other than Photoshop, you can also use the RGB percentages, like that shown in the
following example.
<p style="color: rgb(0%,0%,100%);">
Notice that a comma separates each RGB value and the entire set of values is placed inside
parentheses. A lowercase rgb precedes those parentheses. In the case of the previous code
example, R = 0, G = 0, and B = 255. As was the case with hexadecimal shorthand, RGB values
and percentages are only used to describe color in style sheets, not the older HTML color tags.
Color Names
HTML 3.2 and 4.0 defined a standard set of 16 colors, which could be referenced by names
in addition to hex values. The first version of CSS continued with these 16 colors, and orange
was added in CSS 2.1. Although CSS 3 finally gives us a larger set of acceptable colors, I don’t
encourage their use until the browsers have a chance to catch up with the standards. In the
meantime, Table 3-2 lists the 17 color names that are almost uniformly supported by browsers.
<p style="color: blue;">
So Which Should I Use?
The wonderful thing about using style sheets to define color in web pages is that we are
free to use any of the previously mentioned methods. This means you can tailor your color
presentation method to your particular needs and use whichever makes the most sense to you.
50 HTML: A Beginner’s Guide
Color Name Hex Value RGB Value
black #000000 0,0,0
white #ffffff 255,255,255
silver #c0c0c0 192,192,192
gray #808080 128,128,128
lime #00ff00 0,255,0
olive #808000 128,128,0
green #008000 0,128,0
yellow #ffff00 255,255,0
maroon #800000 128,0,0
navy #000080 0,0,128
red #ff0000 255,0,0
blue #0000ff 0,0,255
purple #800080 128,0,128
teal #008080 0,128,128
fuchsia #ff00ff 255,0,255
aqua #00ffff 0,255,255
orange #ffa500 255,165,0
Table 3-2 Standard Color Names as of CSS 2.1
Web-Safe Colors
Have you ever looked at your favorite web site on someone else’s monitor and noticed the
colors seemed a bit different? This may have been because of different monitor settings. For
example, all newer computer systems and monitors are capable of displaying millions of
colors. But that wasn’t the case a few years ago, when most DOS-based PCs were set up to
display 256 colors or fewer. This reduced color palette meant you couldn’t always be assured
the color you chose for your web page would be available on the viewer’s system.
To compound the problem, Macintosh systems displayed a different set of 256 colors than
their DOS-based PC counterparts. Only 216 colors between the two computer systems (Mac
and PC) were the same! Those 216 colors came to be known as the web-safe color palette. For
a long time, designers were greatly encouraged to use a color from this palette to ensure that
the majority of viewers would see approximately the same color selected.
However, a dozen years after the birth of the web-safe palette, the majority of viewers are
now using much better monitors and computers. This means there is significantly less of a push
to use web-safe colors, but I still mention them so that you are familiar with the palette should
you need to absolutely ensure the appearance of a particular color on a web page. In addition,
Chapter 3: Color 51
some design software applications may still warn you when you select a color that is not web-
safe for use in a web graphic.
You can easily recognize web-safe colors by their hexadecimal values. Each of the web-
safe colors has RGB values that are multiples of 51. So, every color in the 216-color web-safe
palette has a hex value made up of the values shown next.
RGB Hex
0 00
51 33
102 66
153 99
204 CC
255 FF
The color selected in this illustration is not web-safe. This is evident because the green
value is #55, which is not a web-safe hex value. To make this color web-safe, you would have
to change the green value to #66.
This symbol warns that the Photoshop’s color window has
color currently selected is not little black lines along each
web-safe. Clicking the square of the three color bars (red,
box next to the cube causes green, and blue) to show
Photoshop to change the color where the web-safe values are.
to the nearest web-safe color.
Specify Document Colors
The preferred method of changing document colors, such as the background and the text, is
with style sheets.
As with any style declaration, you can specify the background, text, and link colors in
either an inline, internal, or external style sheet. The actual properties used to do so are the
same, however, regardless of which type of style sheet you use. Unlike with the older HTML
tags previously used to change document colors, with CSS you aren’t restricted to specifying
this information within the body tag. In fact, you actually use the a tag (which is used to
add links to a web page) to change link colors in CSS. To understand, look at the following
example of an internal style sheet:
<style type="text/css">
body {background-color: white;
color: gray;}
a:link {color: blue;}
a:visited {color: purple;}
a:active {color: orange;}
</style>
52 HTML: A Beginner’s Guide
NOTE
Remember, internal style sheets are those placed in between the opening and closing
head tags in the HTML code of your web page.
With CSS, you have to consider which tag actually creates the content whose color you
want to change, and use that as your CSS selector. So, in the preceding internal style sheet
example, I first tell the browser to change the background color of the entire page to white (the
body tag determines the underlying features of a page, such as background color and default
text color). Adding the color property to the body selector also specifies that all text on the
page should be, in this case, gray.
Next, I’m telling the browser to select all content affected by a tags (a:link) and make
them blue. When those links have been visited, I want the browser to render them as purple,
as indicated by the line a:visited {color: purple;}. And, finally, the color of active
links—that is, the color visible when the user is clicking a link—is orange, as defined by the
line beginning with a:active.
TIP
Although we used the same property—color—to change the default text color and the
various link colors, remember that it is the selector (in this case body and a) that tells
the browser exactly which color to alter.
On the Horizon
One of my favorite upcoming aspects of web development is transparency. In the upcoming
CSS3 specification, the W3C has defined two new ways to create transparency in web pages.
RGBA
Once browsers start to support RGBA, you'll be able to specify the “alpha value” or the
transparency of a color. The transparency is defined by a number between 0.0 (completely
transparent) and 1.0 (fully opaque). For example, you might use the following code to tell the
browser to display a headline at 50 percent of the defined color.
h1 {color: rgba(255,68,253,0.5);}
As of this writing, the latest versions of Safari, Firefox, and Google Chrome all support
RGBA color specification. Unfortunately, Internet Explorer still does not support this alpha
transparency. So while it’s a fun bit of code to play with, I don't recommend using it for large
web audiences until it’s fully supported. In the meantime, if you really want to use alpha
transparency on your pages, check out this link for a great IE work-around: http://css-tricks
.com/rgba-browser-support/.
TIP
The closer to 0.0, the more the background will show through.
Chapter 3: Color 53
Opacity
Another new addition to the CSS3 specification is the opacity property. Similar to the RGBA
values just described, opacity values are defined between 0.0 (completely transparent) and 1.0
(fully opaque).
But even before the W3C added the opacity property to the CSS3 specification, Internet
Explorer users saw transparency in web pages thanks to the IE-only alpha filter. Different from
the opacity property adopted by the W3C, IE’s proprietary code uses a number between 0 and
100, with 100 being fully opaque.
So, until the CSS3 specification is supported universally, you’ll need to use both the
opacity property and the alpha filter to make sure your transparency works in the most popular
browsers.
div.transparentbox {
background-color:#036;
opacity: 0.7; /* CSS3 standard */
filter:alpha(opacity=60); /* IE only */
}
Try This 3 -1 Change the Colors of Your Page
Let’s take the index.html page from the last chapter, and change the background and text
colors of that page. Goals for this project include
● Choosing colors from the web-safe palette
● Specifying the background and text colors of the web page
● Referencing the colors with the appropriate color codes
NOTE
All the files needed to complete the projects in this book for the Chop Point site can be
downloaded from www.wendywillard.com. In addition, you can view my version of the
web site anytime by visiting www.choppoint.org.
1. Open your text editor and load the index.html page saved from Chapter 2.
2. Add the background-color and color properties to your internal style sheet as the following
shows. (Feel free to replace these color values with any you deem appropriate.) Save the file.
<style type="text/css">
body {background-color: #ffe188;
color: #602b00;}
</style>
(continued)
54 HTML: A Beginner’s Guide
You can find a color in several different ways:
● Go to www.colorblender.com and use the sliders to select your favorite colors. As a
bonus, this online tool will then suggest matching colors to create a harmonious color
palette.
● Use a color from Table 3-2.
● Choose one from the color-picker in your favorite graphics program (such as Adobe
Photoshop).
3. Open your web browser and choose File | Open Page (or Open File or Open, depending on
the browser you’re using). Locate the file index.html you just saved.
4. Preview the page to determine if you approve of your color choices. If you don’t, return to
your text editor to make changes. After making any changes, save the file and switch back
to the browser. Choose Refresh or Reload to preview the changes you just made.
Summary
Using a style sheet to change the colors of your web page is not difficult, but it does require
some planning to find a set of colors that work well together. Viewing your pages on several
different computer systems can help ensure they all appear as you would like.

""")

# Get the current timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")

# Write the response to a file with the timestamp in the filename
file_name = f"response_{timestamp}.json"
with open(file_name, "w") as file:
    file.write(response.text)

print(f"Response written to {file_name}")



