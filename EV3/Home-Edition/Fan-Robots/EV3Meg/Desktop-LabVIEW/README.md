# EV3Meg

A friendly helper robot.

EV3MEG is a small helper robot that can drive and follow a black line on a light surface.
It uses a smart fuzzy logic to drive.


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>EV3MEG;<font color="#0000FF"> fuzzy line following</font></b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>EV3MEG is a small fuzzy line following robot that can detect objects and avoid them by making a quick 180 degree turn.</p><p>Have fun and start building.</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>EV3MEG; <font color="#0000FF">Program</font></b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>The Program is made in several separated loops,</p><p>they all wait for an init to complete before they run.</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>EV3MEG; <font color="#0000FF">Fuzzy calculation</font></b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Fuzzy logic is seen as a way to control with more then just black/white, or true/false variables.</p><p>In the speed loop there is a calculation based on the difference between the actual seen color (gray) and the min (dark) and max (Light) values. The further apart those are the better the controll works.</p><p>The now calculated value is multiplied with a &amp;quot;Speed &amp;quot; factor to use the max speed for following the line. by changing this factor you can slowdown or speed up the EV3MEG.</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>EV3MEG;<font color="#0000FF"> Program driving the motors</font></b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>With a complex program it is always best to make sure you control the motors on just one place in the program.</p><p>If you do that you will avoid strange motor behavior.</p><p>The below image shows the complete motor control loop. The &amp;quot;NoGo&amp;quot; variable controls the drive or turn selection.</p><p>EV3 Brick port wires C and B go to the left and right motor, wire A is for the middle small motor.</p></ActivityCopyPaste>
