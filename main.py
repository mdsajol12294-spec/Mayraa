# main.py
from voice_engine import MayraVoiceController

def main():
    # Mayra Voice Controller ইনিশিয়ালাইজ করা হচ্ছে
    mayra = MayraVoiceController()

    # টেস্ট মেসেজ
    message = "হ্যালো মাস্টার সজল, আমি এখন আপনার কমান্ড অনুযায়ী কথা বলতে প্রস্তুত!"
    output = mayra.process_speech_output(message, mood="happy")
    
    print(output)

if __name__ == "__main__":
    main()
  
