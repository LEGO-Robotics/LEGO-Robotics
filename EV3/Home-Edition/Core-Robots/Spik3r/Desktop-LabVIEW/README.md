# SPIK3R

SPIK3R is a complex robot that crawls and turns in search for targets. It can attack with its Crushing Claws, or shoot with its Lightning Tail.
- __Lightning Tail__: Powered by a Large Motor, its Lightning Tail can shoot at targets far away.
- __Search for Targets__: With the Infrared Sensor it can detect objects and the Infrared Beacon.
- __Agile Turning__: SPIK3R can turn around quickly to search for enemies to attack.


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>SPIK3R 01: Lightning Tail</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will shoot a ball with the Lightning Tail.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does the Lightning Tail move forward?</b> If not, make sure <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#Mode_Degrees">Degrees</a></u></font> input on the second Large Motor block is set to <b>220</b>.

<b>Does it shoot?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#MotorPowerAndDirection">Power</a></u></font> input on the third Large Motor block is set to <b>-100</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change which sound is played by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Sound.html#Mode_File">File Name</a></u></font><font size="12"> input on the Sound block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>SPIK3R 02: Crawling Maneuvers</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will make a crawling maneuver and perform a long-range attack.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place SPIK3R on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does SPIK3R crawl around?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/PortSelector.html#MotorSection">Port</a></u></font> on the second and third Large Motor block is set to <b>B</b>.

<b>Does SPIK3R turn?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#MotorPowerAndDirection">Power</a></u></font> input on the third Large Motor block is set to <b>-100</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how far SPIK3R crawls by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#Mode_Rotations">Rotations</a></u></font><font size="12"> input on the second Large Motor block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>SPIK3R 03: Crush It!</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will add the Crushing Claws and perform a close range attack.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place SPIK3R on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Do the Crushing Claws open and close?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#MotorPowerAndDirection">Power</a></u></font> input on the fourth Medium Motor block is set to <b>-75</b>.

<b>Does SPIK3R move after using the Crushing Claws?</b> If not, make sure the mode of the second Loop block is set to <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/LoopCondition.html#Mode_Count">Count</a></u></font>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how often SPIK3R crawls and crushes by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/LoopCondition.html#Mode_Count">Count</a></u></font><font size="12"> input on the Loop blocks.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>SPIK3R 04: Wait for It…</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will make SPIK3R crawl around in place and wait until it detects something to attack.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place SPIK3R on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Move something in front of the Infrared Sensor to make SPIK3R attack.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does SPIK3R react to objects?</b> If not, make sure the mode of the Wait block is set to <b>Infrared Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Proximity</b>.

<b>Does SPIK3R make a sound while attacking with his Crushing Claws?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Sound.html#PlayType">Play Type</a></u></font> input on the last Sound block is set to <b>1: Play Once</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change the proximity at which SPIK3R will attack by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Wait.html#WaitingForASensorThresholdValue">Threshold Value</a></u></font><font size="12"> input on the Wait block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>SPIK3R 05: Catch That Bug</b></p></ActivityCopyPaste>

In this mission, you'll hunt the Bug and take it out with a long-range shot before moving in to finish the job with the Crushing Claws.

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place SPIK3R and the Bug on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Press the Beacon Mode button on the Infrared Beacon.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does SPIK3R find the Bug?</b> If not, make sure the Infrared Beacon is set to Channel 1, turned on and not too far away from SPIK3R.

<b>Does SPIK3R turn a bit before each shot?</b> If not, make sure the mode of the first Large Motor block inside the first Loop block is set to <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#Mode_Degrees">On for Degrees</a></u></font>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change the heading at which SPIK3R will shoot at the Bug by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Wait.html#WaitingForASensorThresholdValue">Threshold Value</a></u></font><font size="12"> input on the third Wait block.</font></p></ActivityCopyPaste>
