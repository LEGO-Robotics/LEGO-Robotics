# LEGO Mindstorms

This repository is maintained by a father-and-son team based in Silicon Valley—
Lương Thế Vinh (__@TheVinhLuong102__, an Industrial IoT AI Scientist) and
Antoni Lương Phạm Anh Quân (__@AntoniLuongPham__, born 2014)—
and contains programming code (mostly in Python, some in other languages)
for numerous LEGO Mindstorms robots. Generally, __@TheVinhLuong102__ takes care
of the overall organization, documentation and maintenance,
while __@AntoniLuongPham__ codes the majority of the original programs.

For each robot, we experiment extensively with various ways to program it.
For the most performant Python programs, we leverage MicroPython by using
`EV3Dev2` (the 2nd-generation `EV3Dev` library) and the newer `PyBricks` library.
As "collectibles", we have also implemented programs using the
1st-generation `EV3Dev` library, and are planning to add programs using the
`NXT-Python` library for NXT robots too. We also try out parallel processing
using `MultiProcessing`, `Threading` and other means,
to see whether such mechanisms work well with the various libraries.
Occasionally, we take copies of other developers' old programs on GitHub
(with credits/references) and modify those with the latest modern libraries.
Hence, this repository should be considered a collection of
programming experiments based on LEGO Mindstorms.

From time to time, we extract and clean up a subset of our work and contribute
back to the wider LEGO Mindstorms developer & enthusiast community through the
[PyBricks-Projects](https://GitHub.com/PyBricks/PyBricks-Projects) and
[EV3Dev-Lang-Python-Demo](https://GitHub.com/EV3Dev/EV3Dev-Lang-Python-Demo)
repositories.


## [Open-Source Software Community/Ecosystem](OSS-ECOSYS.md)


## Official LEGO Mindstorms Software & Materials


### Robot Inventor

- Desktop Software: [Mac](https://apps.apple.com/us/app/lego-mindstorms-inventor/id1515448947) | [PC](https://www.microsoft.com/en-us/p/lego-mindstorms-robot-inventor/9mtq0n7w1d6x)


### SPIKE Prime

- Desktop Software: [SPIKE](https://education.lego.com/en-us/downloads/spike-prime/software)


### EV3

[Home Edition](https://www.lego.com/en-us/themes/mindstorms/downloads)

- [Desktop Software](https://www.lego.com/en-us/themes/mindstorms/downloads): [macOS](https://go.api.education.lego.com/v1/lms-scratch-retail#nourlrewrite) | [PC](https://go.api.education.lego.com/v1/lms-ev3_en-us_win32#nourlrewrite)
  
- [EV3 Mindstorms Firmware](https://ev3manager.education.lego.com)

- EV3 Programmer Apps: [iOS](https://apps.apple.com/us/app/lego-mindstorms-ev3-programmer/id1039354955) | [Android](https://play.google.com/store/apps/details?id=com.lego.mindstorms.ev3programmer)
  
- Robot Commander Apps: [iOS](https://apps.apple.com/us/app/lego-mindstorms-robot-commander/id681786521) | [Android](https://play.google.com/store/apps/details?id=com.lego.mindstorms.robotcommander)
  
- _Fix the Factory_ Game Apps: [iOS](https://apps.apple.com/us/app/lego-mindstorms-fix-factory/id671493323) | [Android](https://play.google.com/store/apps/details?id=com.lego.mindstorms.fixthefactory)
   
- [Building Instructions](https://www.lego.com/en-us/themes/mindstorms/buildarobot)

- [User Guide](https://www.lego.com/cdn/cs/set/assets/bltbef4d6ce0f40363c/LMSUser_Guide_LEGO_MINDSTORMS_EV3_11_Tablet_ENUS.pdf)

- [Retail Version Online Help](https://ev3-help-online.api.education.lego.com/Retail/en-us/index.html)


[Education Edition](https://education.lego.com/en-us/downloads/mindstorms-ev3)

- Desktop Software: [EV3 Classroom](https://education.lego.com/en-us/downloads/mindstorms-ev3/software)

- [Python for EV3](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)
  - [Getting started with LEGO® MINDSTORMS® Education EV3 MicroPython Version 2.0.0](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/getting-started-with-micropython-v2_enus-810818c6f91786794e324d3e9606b7d2.pdf)
     - [Outdated Version 1.0.0](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf)
  - [microSD Image](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv200sdcardimage-2c980f58ab30715f0659568970baf494.zip)
    - [Outdated Version 1.0.0](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100sdcardimage-4b8c8333736fafa1977ee7accbd3338f.zip)
  - [Documentation](https://pybricks.github.io/ev3-micropython)

- [eLearning](https://elearning.legoeducation.com)

- [Lessons](https://education.lego.com/en-us/lessons?rows=100) (330 as of June 2020)

- [Curriculum](https://education.lego.com/en-us/downloads/mindstorms-ev3/curriculum)
  - [Maker Activities](https://le-www-live-s.legocdn.com/downloads/LME-EV3/LME-EV3_MAKER_1.0_en-US.pdf)
  - [Coding Activities](https://le-www-live-s.legocdn.com/downloads/LME-EV3/LME-EV3_Coding-activities_2.0_en-US.pdf)
  - Curriculum Activity Packs (downloadable in Education Edition Desktop Software)
    - Design Engineering Process/Projects (DEP) / Robot Trainer 
      - [iOS](https://le-www-live-s.legocdn.com/downloads/LME-EV3/LME-EV3_DEP-full-setup_1.4.2_en-US_OSX.dmg)
    - Science/Engineering Lab
      - [iOS](https://le-www-live-s.legocdn.com/downloads/LME-EV3/LME-EV3_SCIENCE-full-setup_1.4.2_en-US_OSX.dmg)
    - Space Challenge
      - [iOS](https://le-www-live-s.legocdn.com/downloads/LME-EV3/LME-EV3_SPACE-full-setup_1.4.2_en-US_OSX.dmg)

- [Building Instructions & Program Descriptions](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions)

- [Building Ideas](https://education.lego.com/en-us/resources/building%20ideas)

- [Education Version Online Help](https://ev3-help-online.api.education.lego.com/Education/en-us/index.html)

- [MakeCode](https://makecode.mindstorms.com) by LEGO & Microsoft


### NXT

[NXT Retail Edition Software](https://www.lego.com/en-us/themes/mindstorms/downloads): [Mac](https://www.lego.com/assets/franchisesites/mindstorms/mac-window-installers/nxt-g-installer-v2.0f6-mac.zip#nourlrewrite) | [PC](https://www.lego.com/assets/franchisesites/mindstorms/mac-window-installers/nxt-g-installer-v2.0f6-windows.zip#nourlrewrite)
- [Firmware](https://www.lego.com/cdn/cs/set/assets/blt3502cca1438605b8/Firmware131_Download1.zip)
- [Fantom Driver](https://www.lego.com/cdn/cs/set/assets/bltea140e66e32fadf0/NXT_Fantom_Drivers_v120.zip)

[NXT Education Edition Software](https://education.lego.com/en-us/downloads/retiredproducts/nxt/software)

[NXT Programs](http://www.nxtprograms.com)
- [Projects for EV3](http://www.nxtprograms.com/index3.html)


## Other Educational Resources

[LEGO Education YouTube Channel](https://www.youtube.com/channel/UC2RjB15PI3IsXCDifNGTG9w)
- [Programming with LEGO Education Mindstorms EV3](https://www.youtube.com/playlist?list=PLXNn7QnqlNpjcIie_4j-I70NepPsT6ekK)

[LEGO Building Instructions](https://www.lego.com/en-us/service/buildinginstructions)

[Excellent blog on EV3 migration from LabVIEW to Scratch](https://medium.com/@dongliang/the-future-of-lego-mindstorms-ev3-programming-1921c2be8131)

[BluPants](https://blupants.com)
- [Documentation](https://blupants.org/help)
- https://github.com/blupants/blupants

[Robo Manuals](https://robomanuals.com)
