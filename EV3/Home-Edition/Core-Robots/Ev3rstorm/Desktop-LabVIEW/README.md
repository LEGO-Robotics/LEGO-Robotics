# EV3RSTORM

EV3RSTORM moves around in tracked skates and can attack with its Spinning Tri-Blade or Blasting Bazooka. He can detect objects, follow the Infrared Beacon and receive commands remotely.


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>EV3RSTORM 01: Driving and Turning</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will drive and turn EV3RSTORM.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place EV3RSTORM on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does EV3RSTORM turn in the same direction the eyes look?</b> If not, make sure the Large Motors are connected to the correct ports of the EV3.

<b>Does EV3RSTORM make a complete turn?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#Mode_Rotations">Rotations</a></u></font> inputs on the Move Steering blocks are set to <b>5</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast EV3RSTORM drives by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html#MotorPowerAndDirection">Power</a></u></font><font size="12"> input on the Move Steering blocks.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>EV3RSTORM 02: Activate!</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will press the Touch Sensor to activate EV3RSTORM or put him back to sleep.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place EV3RSTORM on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Press the Touch Sensor to activate EV3RSTORM or put him to sleep.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does EV3RSTORM snore the whole time while sleeping?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Sound.html#PlayType">Play Type</a></u></font> input on the first Sound block is set to <b>2: Repeat</b>.

<b>Does EV3RSTORM wake up or go to sleep each time you bump the Touch Sensor?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Wait.html#Mode_TouchSensor_CompareState">State inputs on the Wait blocks</a></u></font> are set to <b>2: Bumped</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="16"><b>Tip:</b></font> You can make EV3RSTORM say your name by recording your own sounds with the <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/SoundEditor.html">Sound Editor</a></u></font> and change the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Sound.html#Mode_File">File Name</a></u></font> of a Sound block.</p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>EV3RSTORM 03: Stay Out of the Dark</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will make clever use of the Color Sensor so EV3RSTORM stays out of the dark and attacks with the Spinning Triblade using the Touch Sensor.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place EV3RSTORM on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Press the Touch Sensor to activate the Spinning Tri-Blade.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does EV3RSTORM turn around when he drives towards the dark?</b> If not, make sure the mode of the Switch block is set to <b>Color Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Ambient Light Intensity</b>.

<b>Does EV3RSTORM make a smooth turn when it gets dark?</b> If not, make sure you have used <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MoveTank.html">Move Tank</a></u></font> blocks and not <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/Move.html">Move Steering</a></u></font> blocks.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how dark it needs to be before EV3RSTORM turns around by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/CaseSelector.html#TestingASensorThreshold">Threshold Value</a></u></font><font size="12"> input on the Switch block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>EV3RSTORM 04: Attack on Sight</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will attack with the Spinning Tri-Blade when something comes too close.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place EV3RSTORM on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Move something in front of the Infrared Sensor to make EV3RSTORM attack with his Spinning Tri-Blade.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does EV3RSTORM react to objects?</b> If not, make sure the mode of the Switch block is set to <b>Infrared Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Proximity</b>.

<b>Does EV3RSTORM turn around completely after the attack?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MoveTank.html#Mode_Rotations">Rotations</a></u></font> input on the fourth Move Tank block inside the true case of the Switch block is set to <b>2</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change the proximity at which EV3RSTORM will react to objects by changing the </font><font size="12" color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/CaseSelector.html#TestingASensorThreshold">Threshold Value</a></u></font><font size="12"> input on the Switch block.</font></p></ActivityCopyPaste>


# <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>EV3RSTORM 05: Command and Blast</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will control EV3RSTORM remotely with the Infrared Beacon and shoot with the Blasting Bazooka using the Touch Sensor and the Color Sensor.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place EV3RSTORM on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Use the Infrared Beacon on Channel 1 to control EV3RSTORM and use the Touch Sensor and Color Sensor to attack with the Blasting Bazooka.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does EV3RSTORM shoot differently when the Color Sensor is covered?</b> If not, make sure the mode of the Switch block is set to <b>Color Sensor <img src="arrow.png" width="6" height="14" /> Compare <img src="arrow.png" width="6" height="14" /> Ambient Light Intensity</b>.

<b>Does EV3RSTORM shoot upwards after playing the Up sound?</b> If not, make sure the <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/MediumMotor.html#MotorPowerAndDirection">Power</a></u></font> input of the Medium Motor block inside the true case of the Switch block is set to <b>-100</b>.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change how fast EV3RSTORM moves when you control him with the Infrared Beacon by changing the Power input on the IR Control block.</font></p></ActivityCopyPaste>


## <?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="14" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><font size="6"></font><b>EV3RSTORM 06: Search and Destroy</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>In this mission, you will search for Wheeler using the Infrared Sensor to aim and shoot with the Blasting Bazooka.</b></p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Place EV3RSTORM and Wheeler on a smooth surface.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p>Press the Beacon Mode button on the Infrared Beacon.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="12" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Does EV3RSTORM find Wheeler?</b> If not, make sure the Infrared Beacon is set to Channel 1, turned on and not too far away from EV3RSTORM.

<b>Does EV3RSTORM shoot when Wheeler is detected?</b> If not, make sure the mode of the Switch block is set to <font color="#666666"><u><a action="OpenWebsite:ev3help\://blocks/LEGO/CaseSelector.html#Mode_Boolean">Logic</a></u></font> and the Target Found output is <font color="#666666"><u><a action="OpenWebsite:ev3help\://editor/DataWires.html#CreatingADataWire">wired into</a></u></font> the Logic input.</p></ActivityCopyPaste>

<?xml version="1.0" encoding="utf-8"?><ActivityCopyPaste fontsize="16" fontfamily="Verdana" xmlns="http://www.ni.com/ActivityRichTextDocument.xsd"><p><b>Tip:</b> <font size="12">You can change the heading at which EV3RSTORM will shoot at Wheeler by changing the Target Heading input on the IR Target block.</font></p></ActivityCopyPaste>
