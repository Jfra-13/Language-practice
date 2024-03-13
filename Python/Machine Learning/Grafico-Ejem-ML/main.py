import subprocess


def get_wifi_passwords():
    try:
        wifi_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='backslashreplace')
        wifi_profiles = wifi_profiles.split('\n')

        profile_names = [line.split(":")[1][1:-1] for line in wifi_profiles if "All User Profile" in line]

        print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
        print("--------------------------------")

        for profile_name in profile_names:
            try:
                results = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profiles', profile_name, 'key=clear']).decode('utf-8',
                                                                                             errors='backslashreplace')
                password_line = [line.split(":")[1][1:-1] for line in results.split('\n') if "Key Content" in line]
                password = password_line[0] if password_line else ""

                print("{:<30}| {:<}".format(profile_name, password))
            except subprocess.CalledProcessError:
                print("Error Occurred")

    except subprocess.CalledProcessError:
        print("Error Occurred")


if __name__ == "__main__":
    get_wifi_passwords()





