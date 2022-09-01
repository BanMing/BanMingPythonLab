# from xml.etree.ElementTree import tostring
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import SystemAudio


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
muteState = volume.GetMute() == 1 and "Mute On" or "Mute Off"
initLevel = SystemAudio.GetInitVolumeLevel(volume.GetMasterVolumeLevel())

# button callback
def OnMuteClick(sender, app_data, user_data):
    mute = volume.GetMute()
    muteState = not mute and "Mute On" or "Mute Off"
    dpg.set_item_label(muteBtn, muteState)
    volume.SetMute(not mute, None)


def OnAudioLevelAddClick(sender, app_data, user_data):
    volumeLevel = dpg.get_value(volumeProgress)
    print(volumeLevel + 1)
    dpg.set_value("volume text", f"{volumeLevel + 1}")
    dpg.set_value(volumeProgress, volumeLevel + 1)
    dpg.set_item_label(volumeProgress, str(volumeLevel + 1))
    volume.SetMasterVolumeLevel(SystemAudio.SystemAudioLevel[volumeLevel + 1], None)


def OnAudioLevelDownClick(sender, app_data, user_data):
    volumeLevel = dpg.get_value(volumeProgress)
    print(volumeLevel - 1)
    dpg.set_value("volume text", f"{volumeLevel - 1}")
    dpg.set_value(volumeProgress, volumeLevel - 1)
    dpg.set_item_label(volumeProgress, volumeLevel - 1)
    volume.SetMasterVolumeLevel(SystemAudio.SystemAudioLevel[volumeLevel - 1], None)


def OnAudioLevelDrag(sender, app_data, user_data):
    volumeLevel = dpg.get_value(volumeProgress)
    print(volumeLevel)
    dpg.set_value("volume text", f"{volumeLevel}")
    volume.SetMasterVolumeLevel(SystemAudio.SystemAudioLevel[volumeLevel], None)


dpg.create_context()
dpg.create_viewport(title="Custom Title", width=1520, height=720)

dpg.set_global_font_scale(2)

with dpg.window(label="Example Window", width=1520, height=720):
    muteBtn = dpg.add_button(
        label=muteState, width=200, height=100, callback=OnMuteClick
    )

    dpg.add_spacing()

    volumeProgress = dpg.add_drag_int(
        label="Volume Level",
        format="%d%%",
        default_value=initLevel,
        callback=OnAudioLevelDrag,
    )

    dpg.add_spacing()

    with dpg.group(horizontal=True):
        dpg.add_button(
            label="Less", width=200, height=100, callback=OnAudioLevelDownClick
        )

        dpg.add_text(f"{dpg.get_value(volumeProgress)}", tag="volume text")

        dpg.add_button(
            label="More", width=200, height=100, callback=OnAudioLevelAddClick
        )


# demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
