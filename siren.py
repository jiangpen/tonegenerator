
import wave, struct, math
sampleRate = 48000.0 # hertz
duration = 5.0       # seconds
outLevel=0.1
rate=2
vary=100
freq=860
curfreq=freq
vol=0.5 #-6db

wavef = wave.open('siren.wav','w')
wavef.setnchannels(1) # stereo
wavef.setsampwidth(2) 
wavef.setframerate(sampleRate)
numofsample=int(duration * sampleRate)
count=0

for j in range (numofsample/64):
    for i in range(64):
        t1=	curfreq*count
        count=count+1
        sample=math.sin(2.0*math.pi*t1/sampleRate)
        if t1>sampleRate:
            count=(count-float(sampleRate)/curfreq)
        r = int(sample*outLevel*32767.0)
        wavef.writeframesraw( struct.pack('<h', r ) )
    curfreq=round(curfreq+(vary*rate)/(375.0))
    if abs(curfreq-freq)>abs(vary):
        vary=-vary
        

wavef.writeframes('')
wavef.close()

