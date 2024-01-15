import tkinter as tk
from tkinter import messagebox

class MacCompatibilityFinderApp:
    mac_versions = {
        #macbook pros
    "MacBook Pro (14-inch, Nov 2023) - M3 chip, Two Thunderbolt / USB 4 ports": "macOS Sonoma",
    "MacBook Pro (14-inch, Nov 2023) - M3 Pro or M3 Max chip, Three Thunderbolt 4 ports": "macOS Sonoma",
    "MacBook Pro (16-inch, Nov 2023) - M3 Pro or M3 Max chip, Three Thunderbolt 4 ports": "macOS Sonoma",
    "MacBook Pro (14-inch, 2023)": "macOS Sonoma",
    "MacBook Pro (16-inch, 2023)": "macOS Sonoma",
    "MacBook Pro (13-inch, M2, 2022)": "macOS Sonoma",
    "MacBook Pro (14-inch, 2021)": "macOS Sonoma",
    "MacBook Pro (16-inch, 2021)": "macOS Sonoma",
    "MacBook Pro (13-inch, M1, 2020)": "macOS Sonoma",
    "MacBook Pro (13-inch, 2020, Two Thunderbolt 3 ports)": "macOS Sonoma",
    "MacBook Pro (13-inch, 2020, Four Thunderbolt 3 ports)": "macOS Sonoma",
    "MacBook Pro (16-inch, 2019)": "macOS Sonoma",
    "MacBook Pro (15-inch, 2019)": "macOS Sonoma",
    "MacBook Pro (13-inch, 2019, Four Thunderbolt 3 ports)": "macOS Sonoma",
    "MacBook Pro (15-inch, 2018)": "macOS Sonoma",
    "MacBook Pro (13-inch, 2018, Four Thunderbolt 3 ports)": "macOS Sonoma",
    "MacBook Pro (15-inch, 2017)": "macOS Ventura",
    "MacBook Pro (13-inch, 2017, Four Thunderbolt 3 ports)": "macOS Ventura",
    "MacBook Pro (13-inch, 2017, Two Thunderbolt 3 ports)": "macOS Ventura",
    "MacBook Pro (15-inch, 2016)": "macOS Monterey",
    "MacBook Pro (13-inch, 2016, Four Thunderbolt 3 ports)": "macOS Monterey",
    "MacBook Pro (13-inch, 2016, Two Thunderbolt 3 ports)": "macOS Monterey",
    "MacBook Pro (Retina, 15-inch, Mid 2015)": "macOS Monterey",
    "MacBook Pro (Retina, 13-inch, Early 2015)": "macOS Monterey",
    "MacBook Pro (Retina, 15-inch, Mid 2014)": "macOS Big Sur",
    "MacBook Pro (Retina, 13-inch, Mid 2014)": "macOS Big Sur",
    "MacBook Pro (Retina, 15-inch, Late 2013)": "macOS Big Sur",
    "MacBook Pro (Retina, 13-inch, Late 2013)": "macOS Big Sur",
    "MacBook Pro (Retina, 15-inch, Early 2013)": "macOS Catalina",
    "MacBook Pro (Retina, 13-inch, Early 2013)": "macOS Catalina",
    "MacBook Pro (Retina, 13-inch, Late 2012)": "macOS Catalina",
    "MacBook Pro (Retina, 15-inch, Mid 2012)": "macOS Catalina",
    "MacBook Pro (15-inch, Mid 2012)": "macOS Catalina",
    "MacBook Pro (13-inch, Mid 2012)": "macOS Catalina",
    "MacBook Pro (17-inch, Late 2011)": "macOS High Sierra",
    "MacBook Pro (15-inch, Late 2011)": "macOS High Sierra",
    "MacBook Pro (13-inch, Late 2011)": "macOS High Sierra",
    "MacBook Pro (17-inch, Early 2011)": "macOS High Sierra",
    "MacBook Pro (15-inch, Early 2011)": "macOS High Sierra",
    "MacBook Pro (13-inch, Early 2011)": "macOS High Sierra",
    "MacBook Pro (17-inch, Mid 2010)": "macOS High Sierra",
    "MacBook Pro (15-inch, Mid 2010)": "macOS High Sierra",
    "MacBook Pro (13-inch, Mid 2010)": "macOS High Sierra",
    "MacBook Pro (17-inch, Mid 2009)": "OS X El Capitan",
    "MacBook Pro (15-inch, Mid 2009)": "OS X El Capitan",
    "MacBook Pro (15-inch, 2.53GHz, Mid 2009)": "OS X El Capitan",
    "MacBook Pro (13-inch, Mid 2009)": "OS X El Capitan",
    "MacBook Pro (17-inch, Early 2009)": "OS X El Capitan",
    "MacBook Pro (15-inch, Late 2008)": "OS X El Capitan",
    "MacBook Pro (17-inch, Early 2008)": "OS X El Capitan",
    "MacBook Pro (15-inch, Early 2008)": "OS X El Capitan",


#macbook airs

    "MacBook Air (15-inch, M2, 2023)": "Sonoma",
    "MacBook Air (M2, 2022)": "Sonoma",
    "MacBook Air (M1, 2020)": "Sonoma",
    "MacBook Air (Retina, 13-inch, 2020)": "Sonoma",
    "MacBook Air (Retina, 13-inch, 2019)": "Sonoma",
    "MacBook Air (Retina, 13-inch, 2018)": "Sonoma",
    "MacBook Air (13-inch, 2017)": "Monterey",
    "MacBook Air (13-inch, Early 2015)": "Monterey",
    "MacBook Air (11-inch, Early 2015)": "Monterey",
    "MacBook Air (13-inch, Early 2014)": "Big Sur",
    "MacBook Air (11-inch, Early 2014)": "Big Sur",
    "MacBook Air (13-inch, Mid 2013)": "Big Sur",
    "MacBook Air (11-inch, Mid 2013)": "Big Sur",
    "MacBook Air (13-inch, Mid 2012)": "Catalina",
    "MacBook Air (11-inch, Mid 2012)": "Catalina",
    "MacBook Air (13-inch, Mid 2011)": "High Sierra",
    "MacBook Air (11-inch, Mid 2011)": "High Sierra",
    "MacBook Air (13-inch, Late 2010)": "High Sierra",
    "MacBook Air (11-inch, Late 2010)": "High Sierra",
    "MacBook Air (Mid 2009)": "El Capitan",

#imacs

    "iMac (24-inch, 2023, Four ports)": "Sonoma",
    "iMac (24-inch, 2023, Two ports)": "Sonoma",
    "iMac (24-inch, M1, 2021)": "Sonoma",
    "iMac (24-inch, M1, 2021)": "Sonoma",
    "iMac (Retina 5K, 27-inch, 2020)": "Sonoma",
    "iMac (Retina 5K, 27-inch, 2019)": "Sonoma",
    "iMac (Retina 4K, 21.5-inch, 2019)": "Sonoma",
    "iMac Pro (2017)": "Sonoma",
    "iMac (Retina 5K, 27-inch, 2017)": "Ventura",
    "iMac (Retina 4K, 21.5-inch, 2017)": "Ventura",
    "iMac (21.5-inch, 2017)": "Ventura",
    "iMac (Retina 5K, 27-inch, Late 2015)": "Monterey",
    "iMac (Retina 4K, 21.5-inch, Late 2015)": "Monterey",
    "iMac (21.5-inch, Late 2015)": "Monterey",
    "iMac (Retina 5K, 27-inch, Mid 2015)": "Monterey",
    "iMac (Retina 5K, 27-inch, Late 2014)": "Big Sur",
    "iMac (21.5-inch, Mid 2014)": "Big Sur",
    "iMac (27-inch, Late 2013)": "Catalina",
    "iMac (21.5-inch, Late 2013)": "Catalina",
    "iMac (27-inch, Late 2012)": "Catalina",
    "iMac (21.5-inch, Late 2012)": "Catalina",
    "iMac (27-inch, Mid 2011)": "High Sierra",
    "iMac (21.5-inch, Mid 2011)": "High Sierra",
    "iMac (27-inch, Mid 2010)": "High Sierra",
    "iMac (21.5-inch, Mid 2010)": "High Sierra",
    "iMac (27-inch, Late 2009)": "High Sierra",
    "iMac (21.5-inch, Late 2009)": "High Sierra",
    "iMac (24-inch, Early 2009)": "El Capitan",
    "iMac (20-inch, Early 2009)": "El Capitan",
    }

    def __init__(self, master):
        self.master = master
        master.title("Mac OS Compatibility Finder")

        self.label = tk.Label(master, text="Enter the Mac model:")
        self.label.pack()

        self.mac_model_entry = tk.Entry(master)
        self.mac_model_entry.pack()

        self.check_button = tk.Button(master, text="Check Compatibility", command=self.check_compatibility)
        self.check_button.pack()

    def check_compatibility(self):
        mac_model = self.mac_model_entry.get().lower()
        mac_versions_lower = {key.lower(): value for key, value in self.mac_versions.items()}

        if mac_model in mac_versions_lower:
            result = f"The latest supported operating system for {mac_model.capitalize()} is: {mac_versions_lower[mac_model]}"
        else:
            result = "Model not found"

        messagebox.showinfo("Compatibility Result", result)

# Create the Tkinter window
root = tk.Tk()
app = MacCompatibilityFinderApp(root)


root.mainloop()
