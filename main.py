#coding:utf-8
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import  EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

def init(device):
    device.installPackage("D:\\workspace\\TestScript\\demo-monkeyrunner\\ContactManager.apk");
    print("install successfully!");
def launchApp(device):
    device.startActivity(component='com.example.android.contactmanager/com.example.android.contactmanager.ContactManager');
    MonkeyRunner.sleep(3);

def testAddContact(device,easy_device):
    easy_device.touch(By.id("id/addContactButton"),MonkeyDevice.DOWN_AND_UP);
    MonkeyRunner.sleep(1);
    print("click successfully!");
    easy_device.touch(By.id("id/contactNameEditText"), MonkeyDevice.DOWN_AND_UP);
    print("try to input some words!");
    MonkeyRunner.sleep(1);
    device.type("monkeyrunner");
    print("input successfully!");
    easy_device.touch(By.id("id/contactEmailEditText"),MonkeyDevice.DOWN_AND_UP);
    print("try to input some words!");
    MonkeyRunner.sleep(1);
    device.type("monkeyrunner@example.com");
    print("input successfully!");
    easy_device.touch(By.id("id/contactSaveButton"),MonkeyDevice.DOWN_AND_UP);
    print("save successfully!");
    MonkeyRunner.sleep(1);
    result  =device.takeSnapshot();
    result.writeToFile('D:\\workspace\\TestScript\\demo-monkeyrunner\\contact.png');

    # hierarchy_viewer = device.getHierarchyViewer();
    # viewnode = hierarchy_viewer.findViewById('id/contactList');

def tearDown(device):
    device.shell("am force-stop com.example.android.contactmanager.ContactManager");
    device.removePackage("com.example.android.contactmanager");


device = MonkeyRunner.waitForConnection();
easy_device = EasyMonkeyDevice(device);
init(device);
launchApp(device);
testAddContact(device,easy_device);
tearDown(device);

