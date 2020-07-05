# GRIPP3R


GRIPP3R is a strong robot that can lift and carry heavy things with its Grasping Grippers. Control it remotely to make it pick up what you want!


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>GRIPP3R 01: Grasping It</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will practice using the Grasping Grippers.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place the Grasping Grippers on a smooth surface</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Do the Grasping Grippers move?</b> If not, make sure the mode of the first Medium Motor block is set to <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#Mode_Time">On for Seconds</a></u></font>.

<b>Do the Grasping Grippers go down in the end?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#MotorPowerAndDirection">Power</a></u></font> input on the last Medium Motor block is set to <b>-75</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast the Grasping Grippers open and close by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#MotorPowerAndDirection">Power</a></u></font><font size="12"> input on the Medium Motor blocks.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>GRIPP3R 02: Moving Around the Tire Stack</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will drive, pick up the Tire Stack, turn around and put it down again.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place GRIPP3R on a smooth surface. Place the Tire Stack a short distance in front of GRIPP3R. </p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does GRIPP3R pick up the Tire Stack?</b> If not, make sure the Tire Stack is placed at the right distance.

<b>Does GRIPP3R turn around to return the Tire Stack?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Degrees">Degrees</a></u></font> input on the second Move Steering block is set to <b>850</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how far GRIPP3R drives before picking up the Tire Stack by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Rotations">Rotations</a></u></font><font size="12"> input on the first Move Steering block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>GRIPP3R 03: Pick <i>That</i> Up!</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will use the Infrared Sensor to show GRIPP3R what objects you want it to pick up or put down.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place GRIPP3R on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Move your hand in front of the Infrared Sensor when you want GRIPP3R to pick something up or put it down.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does GRIPP3R react to your hand?</b> If not, make sure the mode of the Wait blocks is set to <b>Infrared Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Proximity</b>.

<b>Does GRIPP3R stop when it detects your hand?</b> If not, make sure the mode of the Move Steering block after the Wait block is set to <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Stop">Off</a></u></font>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change the proximity at which GRIPP3R will react to your hand by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Wait.html#WaitingForASensorThresholdValue">Threshold Value</a></u></font><font size="12"> input on the Wait blocks.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>GRIPP3R 04: At Your Service!</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will use the Infrared Beacon to control GRIPP3R remotely so you can carry around things as you please.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place GRIPP3R and the Tire Stack on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Use the Infrared Beacon on Channel 1 to control GRIPP3R (the Beacon Mode button controls the Grasping Grippers).</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does GRIPP3R react to the Infrared Beacon?</b> If not, make sure the Channel Selector on the Infrared Beacon is set to 1.

<b>Does GRIPP3R drive as expected?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/PortSelector.html#MotorSection">Ports</a></u></font> of the Large Motor blocks are set correctly.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast GRIPP3R drives by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Motor.html#MotorPowerAndDirection">Power</a></u></font><font size="12"> input on the Large Motor blocks.</font></p></ActivityCopyPaste>
