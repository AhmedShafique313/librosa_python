# Librosa
## Audio library of Python
Using `Librosa` we can perform lot of operation on audio file easily and it can computer complex computations on audio using `Librosa`
### Librosa Complete Guidance to use By Ahmed Shafique
- Lesson1.py
- lesson2.py
- lessons.ipynb
`Audio` file for testing `song for testing.mp3`

### Lesson1
- We plot the audio waveform before plotting we load using librosa
![Figure_1](https://github.com/AhmedShafique313/librosa_python/assets/99950606/b9dc0250-5857-4a52-acf0-762e6a144a7c)

### Lesson2
- We calculated the Mel-Frequency Cepstral Coeffiencts (MFCCS)
- Plotted the MFCCS
![Figure_2](https://github.com/AhmedShafique313/librosa_python/assets/99950606/bb8ea548-fa98-40e7-a208-e4eedba83728)

## All Important Features in Librosa
### Beat Tracking
Librosa also provides functionality for beat tracking in audio file

### Spectrogram
A spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time. Librosa can compute the spectrogram of an audio signal.
- librosa.stft(y): This function computes the Short-Time Fourier Transform (STFT) of the audio signal y. The STFT represents a signal in the time-frequency domain. It decomposes the signal into its constituent sinusoidal components over small time windows.

- np.abs(): This NumPy function takes the absolute value of each element in the STFT matrix. The STFT values can be complex numbers, but taking the absolute value gives us the magnitude or amplitude of each frequency component.

- librosa.amplitude_to_db(D, ref=np.max): This function converts the magnitude spectrogram D (computed from the STFT) to decibel (dB) units, which are commonly used in audio processing. It applies a logarithmic scale to the magnitude values, which can help visualize the dynamic range of the signal more clearly. The ref=np.max argument sets the reference power to the maximum value in the input spectrogram D.


### Chromagram
A chromagram is a representation of the energy distribution of pitch classes (or chroma) in an audio signal. It's useful for tasks like chord recognition and key estimation

### Tempo Estimation
Librosa can estimate the tempo (beats per minute) of an audio signal

### Onset Detection
Onsets are points in time where a sound event begins. Librosa can detect onsets in an audio signal.
- onset_frames = librosa.onset.onset_detect(y=y, sr=sr): This line detects onsets in the audio signal y using the librosa.onset.onset_detect() function. The sr=sr argument specifies the sampling rate of the audio signal. The function returns an array of frame indices where onsets are detected.

- onset_times = librosa.frames_to_time(onset_frames, sr=sr): This line converts the onset frame indices (onset_frames) into time values in seconds using the librosa.frames_to_time() function. The sr=sr argument specifies the sampling rate of the audio signal. The resulting onset_times array contains the time values (in seconds) corresponding to the detected onsets.


### Tempo and Beat Tracking Visualization
Combine beat tracking and onset detection for a comprehensive rhythm analysis visualization


### Harmonic-Percussive Source Separation
Separate an audio signal into harmonic and percussive components. 
