<?xml version="1.0" encoding="UTF-8" ?>
<Package name="聞き取りベース" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="Step1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="test" src="test/test.dlg" />
    </Dialogs>
    <Resources>
        <File name="axis" src="axis.pmt" />
        <File name="qa" src="qa.py" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="enu" />
        <Topic name="test_jpj" src="test/test_jpj.top" topicName="test" language="ja_JP" />
    </Topics>
</Package>
