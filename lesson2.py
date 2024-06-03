import librosa
import librosa.feature
import librosa.display
import matplotlib.pyplot as plt

file_path = 'song for testing.mp3'
y, sr = librosa.load(file_path)
#  Mel-Frequency Cepstral Coefficients (MFCCs)
mfccs = librosa.feature.mfcc(y=y, sr=sr)

# Display MFCCs
plt.figure(figsize=(8, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()