# Replicating the "GyroPhone" experiments

## Gather data
(Note: My approach is to record all samples in one go; the GyroPhone folks 
instead [start--play back--stop--download for each speech sample](https://bitbucket.org/ymcrcat/gyrophone/src/aa816eec3d7a17d9e30ab7afa0d4b79ef0a7a82e/run_gyromic.py?at=master&fileviewer=file-view-default).)

* `adb install GyroMic-debug.apk`
* Run the app on your Android device. It now records gyroscope data to `/sdcard/gyro_samples.txt`.
* Play back audio.
* Stop the app: `adb shell am broadcast -a seclab.GyroMic.intent.action.SHUTDOWN`
* Download the samples: `adb pull /sdcard/gyro_samples.txt`

The [data format of the output file](https://bitbucket.org/ymcrcat/gyrophone/src/aa816eec3d7a17d9e30ab7afa0d4b79ef0a7a82e/App/src/seclab/GyroMic/GyroMic.java?at=master&fileviewer=file-view-default#GyroMic.java-130) is

```
int (timestamp in nanoseconds) float (gyro x) float (gyro y) float (gyro z)
```

[Ref for nanoseconds precision](https://developer.android.com/reference/android/hardware/SensorEvent.html#timestamp)


## Convert gyro readings to wave files
* Find the (absolute) maximum per axis per sample set,
  `python find_max.py <the_source_file.txt`
* Alternatively, use 0.02 which seems to be the 1st and 99th percentile 
  on my Sony Tablet S and Google Nexus 6.
* Convert the gyro readings to WAV files,
  `python gyro_record_to_wav.py ...` (see its help string for details). 
  You can find the gyro sample frequency from the differences in timestamps 
  in column 1 of the readings. (Nanoseconds precision, see above.)
  (Note: The resulting "audio" is *very low frequency*. Your laptop speaker 
  probably won't output anything, your headphones might or might not. 
  Use an audio editor to convince yourself that there actually is audio 
  in these files!)


## Then what?
* Run machine learning algorithms on the WAV files.

