import librosa
import matplotlib.pyplot as plt

file_path = 'song for testing.mp3'
y, sr = librosa.load(file_path)

# Plot the audio waveform
plt.figure(figsize=(12, 4))
plt.plot(y)
plt.title('Audio Waveform')
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.show()

