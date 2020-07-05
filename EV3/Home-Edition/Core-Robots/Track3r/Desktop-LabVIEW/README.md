# TRACK3R

TRACK3R is easy to create & command, and has a lot of tools. Use the Bi-Blade Blender, Blasting Bazooka, Gripping Claw and Heavy Hammer to complete different missions on the Mission Pad.


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>TRACK3R 01: Blend It with Precision</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will use the Bi-blade Blender to remove a tire from the Mission Pad.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place TRACK3R at the start position on the Mission Pad and place a tire on the circle as shown in the video.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does TRACK3R drive forward and stop before the tire?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Rotations">Rotations</a></u></font> input on the first Move Steering block is set to <b>2</b>.

<b>Does TRACK3R return to the start position after removing the tire?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#MotorPowerAndDirection">Power</a></u></font> input on the second Move Steering block is set to <b>-75</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast the Bi-blade Blender spins by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#MotorPowerAndDirection">Power</a></u></font><font size="12"> input on the Medium Motor block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>TRACK3R 02: Blast It Away</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will blast away tires with the Blasting Bazooka.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place TRACK3R at the start position on the Mission Pad and stack two tires on each of the two circles near the edge of the Mission Pad as shown in the video.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does TRACK3R hit the top tires?</b> If not, make sure TRACK3R is placed straight on the Mission Pad and try again.

<b>Does TRACK3R first hit the left tire and then the right tire?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#SteeringAndMotorSpeed">Steering</a></u></font> input on the first Move Steering block is set to <b>-100</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how many times the Blasting Bazooka shoots by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#Mode_Rotations">Rotations</a></u></font><font size="12"> input on the Medium Motor block (1 shot takes 3 Rotations).</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>TRACK3R 03: Take Them Away</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will move two tires with the Gripping Claw and place them inside the squares on the Mission Pad.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place TRACK3R at the start position on the Mission Pad and place a tire on the two circles as shown in the video.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does TRACK3R place the tires inside the squares?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#SteeringAndMotorSpeed">Steering</a></u></font> input on the second Move Steering block is set to <b>35</b> and the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Rotations">Rotations</a></u></font> input is set to <b>3</b>.

<b>Does TRACK3R move both tires?</b> If not, make sure the mode of the Loop block is set to <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/LoopCondition.html#Mode_Count">Count</a></u></font> and the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/LoopCondition.html#IterationsToRun">Count</a></u></font> input is set to <b>2</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast TRACK3R drives by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#MotorPowerAndDirection">Power</a></u></font><font size="12"> input on the Move Steering blocks.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>TRACK3R 04: Tactical Defense System</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will create a Tactical Defense System using the Heavy Hammer to protect TRACK3R from ambushes from behind.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place TRACK3R on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Move something in front of the Infrared Sensor to make TRACK3R turn around and attack.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does TRACK3R react to objects?</b> If not, make sure the mode of the Switch block is set to <b>Infrared Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Proximity</b>.

<b>Does TRACK3R turn around to hit the object?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Degrees">Degrees</a></u></font> input on the Move Steering block inside the true case of the Switch block is set to <b>1000</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b></p>< <font size="12">You can change the proximity at which TRACK3R will react to objects by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/CaseSelector.html#TestingASensorThreshold">Threshold Value</a></u></font><font size="12"> input on the Switch block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>TRACK3R 05: Time Trial</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will command TRACK3R with the Infrared Beacon to pass through all the checkpoints on the Mission Pad before time runs out!</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place TRACK3R at the start position on the Mission Pad and place a tire on each of the four colored circles as shown in the video.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Use the Infrared Beacon on Channel 1 to control TRACK3R.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Remove each tire from the four checkpoints before time runs out. Avoid the red lines!</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does TRACK3R react to the Infrared Beacon?</b> If not, make sure the Channel Selector on the Infrared Beacon is set to 1.

<b>Does TRACK3R play a sound when the color sensor detects the colored circles?</b> If not, make sure the Set of Colors input on the Wait blocks are set correctly.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="16"> <b>Tip:</b></font> You can change the difficulty of the time trial by changing the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/CaseSelector.html#TestingASensorThreshold">Threshold Value</a></u></font> input on the Switch block, which sets the time limit (default <b>60</b> seconds).</p></ActivityCopyPaste>
