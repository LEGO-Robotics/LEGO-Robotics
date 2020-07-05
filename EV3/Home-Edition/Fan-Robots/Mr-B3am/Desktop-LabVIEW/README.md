# Mr. B3am

A robot that can measure Technic beams!

MR-B3AM eats TECHNIC B3ams and tells your their lengths and colors!

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><u>MR-B3AM is very smart!</u></p><p>He eats TECHNIC B3ams and tell you the length and color of them.</p><p>But he doesn't like the B3ams so he will spit them out again!</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><u>MR-B3AM is very smart!</u></p><p>He eats TECHNIC B3ams and tell you the length and color of them.</p><p>But he doesn't like the B3ams so he will spit them out again!</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>MR-B3AM doesn't know yet how to eat B3ams, so he needs your help!</p><p /><p>Luckily, this project contains everything you need to help him!</p><p /><p>Connect MR-B3AM to your computer and press the Play-icon in the program to the left.</p><p /><p>When the wheels spins, try to feed him a straight TECHNIC B3am, with the holes pointing upwards!</p><p /><p>But don't feed him with a B3am that is 3 holes long or shorter! He will choke and you'll never get that B3am back again!</p><p /><p>After feeding him with a few B3ams, you can go ahead and investigate the <font color="#337CBB"><u><a action="NavigateActivity-GoToNextSlide">Program</a></u></font> to see how MR-B3AM eat his B3ams.</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Program Description</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>The MainLoop, which you see to the left procresses the B3am before it prints the results. After that is done it waits for you to press enter, before it starts over again and is able to continue endlessly, as MR-B3AM is always hungry!</p><p /><p>The <font color="#337CBB"><u><a action="GoToProgram:ProcessB3am.ev3p">ProcessB3am</a></u></font> block contains the logic for detecting and measuring the B3am. See the inline comments to get a deeper understanding of how MR-B3AM is eating the B3ams. Can you figure out how to make him eat faster?</p><p /><p>The <font color="#337CBB"><u><a action="GoToProgram:PrintResult.ev3p">PrintResult</a></u></font> block is what makes MR-B3AM appear smart. It takes the obtained values and transform them into readable text on the screen. If you want to see the actual length and color-ID MR-B3AM measured then open the <font color="#337CBB"><u><a action="GoToProgram:Debug.ev3p">Debug</a></u></font> block and change the input to the switch to 'True'. When starting the program again MR-B3AM will now print more information about the B3am.</p><p /><p>If you're up for a challenge or two then have a look of some proposed challenges on the <font color="#337CBB"><u><a action="NavigateActivity-GoToNextSlide">next page</a></u></font>.</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Challenges</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>There are some challenges you can try to do, in order to make MR-B3AM smarter:</p><p /><p>•  If you have B3ams in other colors than black and red, you can try to improve the program to make MR-B3AM able to recognize them.</p><p /><p>•  Make MR-B3AM say the color and length instead of showing the details on his screen. </p><p /><p>•  With the pieces that are left in the set, you can try to transform MR-B3AM into a B3am Sorter. By attaching an extra motor with wheels underneath him in order to go sideways, you would be able to accurately drop B3ams off different places along a surface and thereby making him sort your bricks for you!</p></ActivityCopyPaste>
