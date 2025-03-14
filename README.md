# Spectral Shadows Unmasking Voices & Faces Using Deep Learning
Deepfake Detection using AI & Spectral Analysis

### Project Description
Spectral Shadow is a deep learning-based deepfake detection system that analyzes audio and video spectral features to identify AI-generated manipulations. The project applies convolutional neural networks (CNNs) and spectrogram analysis for enhanced detection accuracy.

### Video Processing and Frame Extraction
To analyze deepfake videos, the system first converts video files into individual frames. This process helps in breaking down the video into a sequence of images that can be used for deep learning-based classification. Each frame is extracted systematically to ensure that relevant visual cues indicating deepfake manipulation are captured.

![Image Extraction](https://github.com/user-attachments/assets/77988efe-1fac-4f84-8fbd-85eadb0ec8bf)


### Deepfake Video Classification
The extracted frames are then processed using a deep learning model trained to distinguish between real and fake videos. The model predicts whether the given input belongs to an authentic source or if it has been artificially generated.

![Video_prediction](https://github.com/user-attachments/assets/bd83c7ba-f377-4ee7-841f-90a68e6fd0f6)


### Audio Analysis Using MFCC Features
In addition to video analysis, this project also investigates deepfake detection in audio. Mel-Frequency Cepstral Coefficients (MFCC) are extracted from the audio files to analyze spectral patterns. Deepfake audio often contains anomalies that can be identified using MFCC visualization.

### MFCC plot for a fake audio sample:
![mfcc_fake1](https://github.com/user-attachments/assets/b6f02881-1520-40e8-a371-f6c62c927b64)

### MFCC plot for a real audio sample:
![mfcc_real1](https://github.com/user-attachments/assets/bf7e9471-d2d7-4a4b-b26c-ddee699ac5b4)


# Conclusion
This project aims to enhance the detection of deepfake content by combining both visual and audio analysis. By leveraging deep learning techniques, it provides an effective way to differentiate between real and fake media. The dashboard serves as a tool to visualize and interpret the classification results, making deepfake detection more accessible and transparent.

