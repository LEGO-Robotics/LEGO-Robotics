# R3PTAR

R3PTAR is a tall, long and powerful robot. It moves like a real snake and can strike with its Fearsome Fangs when it detects something.
- __Detect Objects__: With the Infrared Sensor, R3PTAR can detect objects in front of it.
- __Strike!__: Using the powerful Large Motor, R3PTAR can strike with its Fearsome Fangs at lightning speed.
- __Slither__: Combining a Large Motor for moving forward and a Medium Motor for steering, R3PTAR can slither like a real snake.


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>R3PTAR 01: Slither like a Snake</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will make a slithering movement like a real snake.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place R3PTAR on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does R3PTAR move forward?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/PortSelector.html#MotorSection">Port</a></u></font> of the Large Motor block is set to <b>B</b>.

<b>Does R3PTAR move smoothly?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#Mode_Time">Brake at End</a></u></font> inputs on the Medium Motor blocks are set to <img src="false.png" width="17" height="17" /><b>Coast</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how far R3PTAR slithers by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/LoopCondition.html#Mode_Count">Count</a></u></font><font size="12"> input on the Loop block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>R3PTAR 02: Rattling R3PTAR</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will make R3PTAR rattle and wait until it detects something to strike with its Fearsome Fangs.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place R3PTAR on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Move something in front of the Infrared Sensor to make R3PTAR strike.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does R3PTAR react to objects?</b> If not, make sure the mode of the Wait block is set to <b>Infrared Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Proximity</b>.

<b>Does R3PTAR make a hissing sound while striking with its Fearsome Fangs?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Sound.html#PlayType">Play Type</a></u></font> input on the last Sound block is set to <b>1: Play Once</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change the proximity at which R3PTAR will strike by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Wait.html#WaitingForASensorThresholdValue">Threshold Value</a></u></font><font size="12"> input on the Wait block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>R3PTAR 03: Hunting</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will enable R3PTAR to slither around by itself and strike with its Fearsome Fangs when it detects something.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place R3PTAR on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Move something in front of the Infrared Sensor to make R3PTAR strike.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does R3PTAR slither and strike as in the video?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/PortSelector.html#MotorSection">Ports</a></u></font> of the Large Motor blocks are set correctly.

<b>Does R3PTAR move backwards after striking?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#MotorPowerAndDirection">Power</a></u></font> input on the third Large Motor block inside the true case of the Switch block is set to <b>-75</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast R3PTAR turns by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Random.html#Mode_Numeric">Lower Bound and Upper Bound</a></u></font><font size="12"> inputs on the Random block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>R3PTAR 04: Take Control </b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will use the Infrared Beacon to control R3PTAR remotely.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place R3PTAR on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Use the Infrared Beacon to control R3PTAR (the Beacon Mode button makes R3PTAR strike).</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does R3PTAR react to the Infrared Beacon?</b> If not, make sure the Channel Selector on the Infrared Beacon is set to 1.

<b>Does R3PTAR behave as expected?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/PortSelector.html#MotorSection">Ports</a></u></font> of the Large Motor blocks are set correctly.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast R3PTAR turns by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#MotorPowerAndDirection">Power</a></u></font><font size="12"> input on the Medium Motor blocks.</font></p></ActivityCopyPaste>
