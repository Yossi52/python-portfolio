from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog
from google.cloud import texttospeech
import multiprocessing
from playsound import playsound
import os

MAIN_C1 = "#EDE9D5"
MAIN_C2 = "#E7AB9A"
MAIN_C3 = "#617143"
text = ""
play = None

# tts 설정
client = texttospeech.TextToSpeechClient()

voice_eng = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
voice_kor = texttospeech.VoiceSelectionParams(
    language_code='ko_KR', ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)


def play_tts(response):
    global play
    if play is not None:
        play.terminate()
        play = None
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
    mp3_path = os.getcwd() + "/output.mp3"
    play = multiprocessing.Process(target=playsound, args=(mp3_path,))
    play.start()


def exchange_eng(input_text):
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(input=synthesis_input, voice=voice_eng, audio_config=audio_config)
    play_tts(response)


def exchange_kor(input_text):
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(input=synthesis_input, voice=voice_kor, audio_config=audio_config)
    play_tts(response)


# multiprocessing 에서 창이 두번 나오는 현상 방지
def main():
    # pdf 열기 및 텍스트 불러오기
    def open_pdf():
        global text, play
        f_types = [("PDF files", "*.pdf")]
        filename = filedialog.askopenfilename(filetypes=f_types)
        text = ""
        if play is not None:
            play.terminate()
            play = None
        if filename != "":
            reader = PdfReader(filename)
            pages = reader.pages
            for page in pages:
                sub = page.extract_text()
                text += sub
            text_box.config(state='normal')
            text_box.delete(0.0, 'end')
            text_box.insert(0.0, text)
            text_box.config(state='disabled')

    # button command
    def read_eng():
        if text != "":
            exchange_eng(text)
        else:
            text_box.config(state='normal')
            text_box.delete(0.0, 'end')
            text_box.insert(0.0, "Please open pdf first.")
            text_box.config(state='disabled')

    def read_kor():
        if text != "":
            exchange_kor(text)
        else:
            text_box.config(state='normal')
            text_box.delete(0.0, 'end')
            text_box.insert(0.0, "Please open pdf first.")
            text_box.config(state='disabled')

    title_lb = tk.Label(text='My tiny PDF to Speech Program', font=('Courier', 30, "bold"), bg=MAIN_C1, fg=MAIN_C3)
    title_lb.grid(row=0, column=0, columnspan=4, pady=25)

    open_btn = tk.Button(text="Open", command=open_pdf)
    open_btn.config(bg=MAIN_C2, relief="groove", borderwidth=2, font=("Courier", 12))
    open_btn.grid(row=1, column=0, pady=25, sticky='e')

    read_btn = tk.Button(text="Read to Korean", command=read_kor)
    read_btn.config(bg=MAIN_C2, relief="groove", borderwidth=2, font=("Courier", 12))
    read_btn.grid(row=1, column=2, pady=25, sticky='w')

    read_btn = tk.Button(text="Read to English", command=read_eng)
    read_btn.config(bg=MAIN_C2, relief="groove", borderwidth=2, font=("Courier", 12))
    read_btn.grid(row=1, column=3, pady=25, sticky='w')

    text_box = tk.Text(window, state='disabled', wrap="word")
    text_box.config(font=("Courier", 18), spacing1=8, height=18, bd=0)
    text_box.grid(row=2, column=0, columnspan=4, pady=25)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("PDF to Speech")
    window.config(padx=100, pady=25, bg=MAIN_C1)
    main()
    window.mainloop()

    if play is not None:
        play.terminate()