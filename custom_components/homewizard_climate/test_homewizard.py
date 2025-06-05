import asyncio
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from homewizard_climate_ws.api.api import HomeWizardClimateApi
from homewizard_climate_ws.ws.hw_websocket import HomeWizardClimateWebSocket

USERNAME = "peppebarchetta@gmail.com"
PASSWORD = "Ciaociao12!"

async def main():
    print("Login in corso...")
    api = HomeWizardClimateApi(USERNAME, PASSWORD)
    api.login()

    print("Login effettuato!")

    print("Recupero dispositivi...")
    devices = api.get_devices()

    print(f"{len(devices)} dispositivo/i trovati.")
    websockets = []

    for device in devices:
        print(f"- {device.name} ({device.identifier})")
        websocket = HomeWizardClimateWebSocket(api, device)
        websocket.connect_in_thread()
        websockets.append(websocket)

    print("WebSocket attivi. Premi INVIO per uscire...")
    input()

    for ws in websockets:
        ws.disconnect()

asyncio.run(main())
