# Setting up the emulator to emulate Nexus S with API level 25 as required by CS-E4100

## The Problem
Intellij (or Java? I don't know) uses /tmp for downloading the SDK. The downloaded package is huge. The /tmp, by default, is set to 1/2 of the RAM when the machine is booted. If the size of the /tmp is not enough, move it to other location.

## How?
1. Download the SDK as usual
2. Observe the folder name created by the Android Studio. Mine is `PackageOperation01`
3. Stop the download process since you know it's not gonna make it.
4. Create your temporary folder elsewhere, in `$HOME`, for instance. For me, I created a folder `$HOME/junk/PackageOperation01`
5. Create a symlink from your temporary folder to tmp.
```
cd /tmp
ln -s /home/my_username/junk/PackageOperation01
```
6. Start the Android Studio. It will use your `$HOME/junk/PackageOperation01` instead of the /tmp.