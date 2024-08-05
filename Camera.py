import cv2
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime
import os
import json
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import torch.nn as nn
import requests
import ssl
import urllib3

bgColor = "#0e1017"
paused = False

# -------------------------------- Bypass and weights --------------------------------
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download_file(url, local_path):
    response = requests.get(url, verify=False)
    with open(local_path, 'wb') as f:
        f.write(response.content)


weights_url = "/Users/apple/Desktop/Git/Parking_classifier_mobilenet_v2.pth"
local_weights_path = "/Users/apple/.cache/torch/hub/checkpoints/mobilenet_v2-b0353104.pth"
download_file(weights_url, local_weights_path)

json_file_path = '/Users/apple/Desktop/Git/_annotations.coco.json'
with open(json_file_path, 'r') as f:
    spot_data = json.load(f)

spots = spot_data['annotations']

model_ft = models.mobilenet_v2(weights=None)
num_features = model_ft.classifier[1].in_features
model_ft.classifier[1] = nn.Linear(num_features, 2)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model_ft = model_ft.to(device)

model_ft.load_state_dict(
    torch.load('/Users/apple/Desktop/Git/Parking_classifier_mobilenet_v2.pth',
               map_location=device))

model_ft.eval()

data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Paths
video_path = '/Users/apple/Desktop/Git/Dataset.mp4'
output_path = '/Users/apple/PycharmProjects/ResearchPaper/MobileNet34/processed_video.mp4'
final_output_path = '/Users/apple/PycharmProjects/ResearchPaper/MobileNet34/annotated_video.mp4'

# Load the video
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Class labels
class_labels = {0: 'Parked', 1: 'Not Parked'}

frame_count = 0


# -------------------------------- Frame Update --------------------------------
def classify_image(image, model):
    image = data_transforms(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(image)
        _, preds = torch.max(outputs, 1)
        return preds[0].item()


def updateFrame(labelCamera, camera):
    global frame_count, out, paused

    ret, frame = camera.read()
    if ret:
        if not paused:
            if frame_count % int(fps) == 0:
                pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                for spot in spots:
                    x1, y1, w, h = spot['bbox']
                    x2 = int(x1 + w)
                    y2 = int(y1 + h)
                    x1 = int(x1)
                    y1 = int(y1)
                    crop_img = pil_image.crop((x1, y1, x2, y2))

                    label_index = classify_image(crop_img, model_ft)
                    label_text = class_labels[label_index]

                    color = (0, 255, 0) if label_index == 0 else (0, 0, 255)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

                out.write(frame)

            frame_count += 1

            # img = cv2.flip(frame, 1)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)

            labelCamera.imgtk = img
            labelCamera.configure(image=img)

    labelCamera.after(1, updateFrame, labelCamera, camera)


# Function to resize the processed video
def resizeProcessedVideo():
    cap = cv2.VideoCapture(output_path)
    out_resized = cv2.VideoWriter(final_output_path, fourcc, fps, (1280, 720))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (1280, 720))
        out_resized.write(resized_frame)

    cap.release()
    out_resized.release()


def takeSnapshot(camera):
    if camera is not None:
        ret, img = camera.read()
        if ret:
            output_folder = 'screenshotImages'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            timestamp = datetime.now().strftime("%d-%m-%y_%H:%M:%S")
            filename = os.path.join(output_folder, f"{timestamp}.png")

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img)

            img_pil.save(filename)
            print(f"Snapshot saved as {filename}")


def togglePause(pause_button):
    global paused
    paused = not paused
    pause_button.configure(text="Play" if paused else "Pause")


def exitCommand(app, camera):
    from MainPage import Dashboard
    Dashboard(app)
    camera.release()


def Camera(app, cameraNo=None):
    for widget in app.winfo_children():
        widget.destroy()

    app.title("Parking Scan")
    app.configure(bg=bgColor)

    camera = cv2.VideoCapture(video_path)
    if not camera.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return

    # Frame
    frame = ctk.CTkFrame(
        master=app,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight(),
        bg_color=bgColor,
        fg_color=bgColor
    )
    frame.pack(expand=True, fill='both')

    # -------------------------------- Frame Top --------------------------------
    frameTop = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight() * 0.1,
        bg_color=bgColor,
        fg_color=bgColor
    )
    frameTop.pack(fill='x')

    date_label = ctk.CTkLabel(
        master=frameTop,
        text="",
        font=("Arial", 26),
        fg_color=bgColor,
        bg_color=bgColor
    )
    date_label.pack(side="left", padx=77, pady=5)

    project_name_label = ctk.CTkLabel(
        master=frameTop,
        text="Parking Scan",
        font=("Arial", 26, "bold"),
        fg_color=bgColor,
        bg_color=bgColor
    )
    project_name_label.pack(side="left", expand=True, pady=(10, 10))

    time_label = ctk.CTkLabel(
        master=frameTop,
        text="",
        font=("Arial", 26),
        fg_color=bgColor,
        bg_color=bgColor
    )
    time_label.pack(side="right", padx=77, pady=5)

    # -------------------------------- Frame Center --------------------------------
    frameCenter = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight() * 0.8,
        bg_color=bgColor,
        fg_color=bgColor,
    )
    frameCenter.pack(expand=True, fill='both')

    labelCamera = ctk.CTkLabel(
        master=frameCenter,
        text="",
    )
    labelCamera.pack(fill="both", expand=True)

    updateFrame(labelCamera, camera)

    # -------------------------------- Frame Bottom --------------------------------
    frameBottom = ctk.CTkFrame(
        master=frame,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight() * 0.1,
        bg_color=bgColor,
        fg_color=bgColor
    )
    frameBottom.pack(expand=True, fill='x')

    button_frame = ctk.CTkFrame(
        master=frameBottom,
        bg_color=bgColor,
        fg_color=bgColor
    )
    button_frame.pack(expand=True)

    snapshot_button = ctk.CTkButton(
        master=button_frame,
        text="Take Snapshot",
        command=lambda: takeSnapshot(camera),
        width=150,
        height=40,
        border_color="#81e6dd",
        fg_color=bgColor,
        bg_color=bgColor,
        border_width=2,
    )
    snapshot_button.pack(side="left", padx=10, pady=(10, 30))

    pause_button = ctk.CTkButton(
        master=button_frame,
        text="Pause",
        command=lambda: togglePause(pause_button),
        width=150,
        height=40,
        border_color="#81e6dd",
        fg_color=bgColor,
        bg_color=bgColor,
        border_width=2,
    )
    pause_button.pack(side="left", padx=10, pady=(10, 30))

    exit_button = ctk.CTkButton(
        master=button_frame,
        text="Back",
        command=lambda: exitCommand(app, camera),
        width=150,
        height=40,
        border_color="#81e6dd",
        fg_color=bgColor,
        bg_color=bgColor,
        border_width=2,
    )
    exit_button.pack(side="left", padx=10, pady=(10, 30))

    # -------------------------------- Date and Time --------------------------------
    def updateDateTime():
        current_date_time = datetime.now()
        current_date = current_date_time.strftime("%Y-%m-%d")
        current_time = current_date_time.strftime("%H:%M:%S")
        date_label.configure(text=current_date)
        time_label.configure(text=current_time)
        frameTop.after(1000, updateDateTime)

    updateDateTime()

    # -------------------------------- Destroy All --------------------------------
    def on_closing():
        camera.release()
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)
